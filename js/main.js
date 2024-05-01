import { app } from '../../scripts/app.js'

const importCheck = /^[ \t]*import\s*/m;

app.registerExtension({
    name: "FlowNodes.warnUnsafe",
    loadedGraphNode(node, app) {
        if (node.type === "Execute Python") {
            const textBoxWidget = node?.widgets?.[0]
            const textBoxEl = textBoxWidget?.inputEl
            if (textBoxEl == null) return

            const fun = () => {
                const flag = importCheck.test(textBoxEl.value)
                if (flag) {
                    node.color = "#D10101"
                    node.bgcolor = "#830000"
                }
            }

            textBoxEl.addEventListener("change", fun)
            fun()
        }
    }
})

const colors = {
    "FLOW": ["#dddddd", "#ffffff"]
}

app.registerExtension({
    name: "FlowNodes.coloredConnections",
    init() {
        for (let type in colors) {
            LGraphCanvas.link_type_colors[type] = colors[type]
        }
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        let flag = false

        for (const output of nodeData?.output ?? []) {
            if (output in colors) {
                flag = true
                break
            }
        }

        if (!flag)
            for (const incat of nodeData?.input?.values?.() ?? []) { // Required, optional, hidden
                for (const inputVals of incat?.values?.() ?? []) { // Actual inputs
                    if (inputVals[0] in colors) {
                        flag = true
                        break
                    }
                }
            }

        if (!flag) {
            return;
        }

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = async function () {
            const me = onNodeCreated?.apply(this);
            const self = this;
            // const widget_reset = this.widgets.find(w => w.name === 'RESET');
            // widget_reset.callback = async (e) => {
            //     widget_reset.value = false;
                // api_cmd_jovian(self.id, "reset");
            // }
            return me;
        }

        const onConnectionsChange = nodeType.prototype.onConnectionsChange
        nodeType.prototype.onConnectionsChange = function (slotType, slot, event, link_info, data) {
            console.log("Connection change")
            const me = onConnectionsChange?.apply(this, arguments);
            if (!link_info) {
                return;
            }
            for (const input of this?.inputs ?? []) {
                const type = input?.type
                if (colors[type]) {
                    input.color_off = colors[type][0]
                    input.color_on = colors[type][1]
                }
            }
            for (const output of this?.outputs ?? []) {
                const type = output?.type
                if (colors[type]) {
                    output.color_off = colors[type][0]
                    output.color_on = colors[type][1]
                }
            }
            app.graph.setDirtyCanvas(true, true);
            return me;
        }
    }
})