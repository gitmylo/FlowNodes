import { app } from '../../scripts/app.js'

const colors = {
    "FLOW": ["#dddddd", "#ffffff", LiteGraph.ARROW_SHAPE]
}

function updateNodeRender(node) {
    for (const input of node?.inputs ?? []) {
        const type = input?.type
        if (colors[type]) {
            const vals = colors[type]
            input.color_off = vals[0]
            input.color_on = vals[1]
            input.shape = vals[2]
        }
    }
    for (const output of node?.outputs ?? []) {
        const type = output?.type
        if (colors[type]) {
            const vals = colors[type]
            output.color_off = vals[0]
            output.color_on = vals[1]
            output.shape = vals[2]
        }
    }
    for (let type in colors) {
        LGraphCanvas.link_type_colors[type] = colors[type][1]
    }
    app.graph.setDirtyCanvas(true, true)
}

app.registerExtension({
    name: "FlowNodes.coloredConnections",
    init() {
        for (let type in colors) {
            // This doesn't always appear to work, which is why there's another variant for when nodes connections are updated.
            LGraphCanvas.link_type_colors[type] = colors[type][1]
        }
        const add = app.graph.add
        app.graph.add = function (node, skip_compute_order) {
            const result = add?.apply(this, arguments)
            updateNodeRender(node)
            return result
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
            return
        }

        const onConnectionsChange = nodeType.prototype.onConnectionsChange
        nodeType.prototype.onConnectionsChange = function (slotType, slot, event, link_info, data) {
            const result = onConnectionsChange?.apply(this, arguments)
            updateNodeRender(this)
            return result
        }
    },
    loadedGraphNode(node, app) {
        updateNodeRender(node)
    }
})