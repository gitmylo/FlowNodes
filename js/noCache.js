import { app } from '../../scripts/app.js'

app.registerExtension({
    name: "FlowNodes.noCache",
    getCustomWidgets() {
        return {
            // Dummy widget, doesn't render, but returns a random value when the value is requested, this makes every forward-connected node re-run
            NO_CACHE (node, inputName, inputData, app) {
                return { widget: node.addCustomWidget({
                        type: "NO_CACHE",
                        name: inputName,
                        computeSize (...args) {
                            return [0, 0]
                        },
                        async serializeValue (nodeId, widgetIndex) {
                            return Math.random()
                        }
                    })
                }
            }
        }
    }
})