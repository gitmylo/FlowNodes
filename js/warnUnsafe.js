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