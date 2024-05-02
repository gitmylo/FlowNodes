import { app } from '../../scripts/app.js'

let nodeGroups = {}

function updateNodeEnabledConnections(node) {
    if (!(node.type in nodeGroups)) return

    const group = nodeGroups[node.type]
    const hiddenInputs = []
    for (const inputGroupKey in group["groups"]) {
        let flag = false
        const inputGroup = group["groups"][inputGroupKey]
        for (const inputKey in inputGroup) {
            const input = node.inputs.filter(item => item?.name === inputKey)?.[0]

            if (flag && input?.link == null) hiddenInputs.push(inputKey)
            if (input?.link == null && !flag) {
                flag = true
            }
        }
    }

    // Filter groups
    const outGroup = []
    for (const inputKey in group["original"]) {
        if (!(hiddenInputs.includes(inputKey))) {
            const input = node.inputs.filter(item => item?.name === inputKey)?.[0]
            if (input == null) {
                outGroup.push({
                        name: inputKey,
                        type: group["original"][inputKey]?.[0],
                        link: null
                    })
            }
            if (input != null) outGroup.push(input)
        }
    }

    node.inputs = outGroup

    app.graph.setDirtyCanvas(true, true)
}

app.registerExtension({
    name: "FlowNodes.dynamicAvailable",
    init() {
        nodeGroups = {}

        const add = app.graph.add
        app.graph.add = function (node, skip_compute_order) {
            const result = add?.apply(this, arguments)
            updateNodeEnabledConnections(node)
            return result
        }
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        let flag = false
        const groups = {}

        const opt = nodeData?.input?.["optional"] ?? []
        for (const inputValKey in opt) { // All optional inputs
            const inputVal = opt[inputValKey]
            const flags = inputVal?.[1]
            const dya = flags?.dynamicAvailable
            if (flags && flags?.dynamicAvailable) {
                flag = true
                if (!groups?.[dya]) groups[dya] = {}
                // groups[dya].push({inputValKey: inputVal})
                groups[dya][inputValKey] = inputVal
            }
        }

        if (!flag) return

        // Register this group list
        nodeGroups[nodeData.name] = {
            "groups": groups,
            "original": opt
        }

        const onConnectionsChange = nodeType.prototype.onConnectionsChange
        nodeType.prototype.onConnectionsChange = function (slotType, slot, event, link_info, data) {
            const result = onConnectionsChange?.apply(this, arguments)
            updateNodeEnabledConnections(this)
            return result
        }
    },
    loadedGraphNode(node, app) {
        updateNodeEnabledConnections(node)
    }
})