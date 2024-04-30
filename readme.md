# ComfyUI FlowNodes
A [ComfyUI](https://github.com/comfyanonymous/comfyui) node pack containing nodes for basic programming logic.

## Conditions
Condition nodes will behave differently depending on the condition's value.
### If
Takes a boolean (condition) and a value.
Two outputs: True, and False.
* True: if `true`, contains the input value, if `false`, contains `None`
* False: if `false`, contains the input value, if `true`, contains `None`

This node should be connected on the location of an `optional` input, as otherwise, returning `None` will cause errors.

### Switch (Bool)
Takes a boolean, and two values. If the boolean is `True`, the first value will be outputted, if it's `False`, the second value will be outputted.

### Switch (Int)
Same as `Switch (Bool)`, but instead of `True`/`False`, it's the numbers `0-9`

## Comparisons
Comparison nodes take multiple inputs, and perform a comparison between them, and output the result.

## Logic
Logic nodes take 1/2 boolean inputs, and return a boolean.
* And: `a && b`
* Or: `a || b`
* Eq: `a == b`
* Neq: `a != b`
* Not: `!a`

## Math
Math nodes take a few numerical inputs, 

## Function
Function nodes perform an operation on the inputs, and output the result. (Most similar to most other comfy nodes)

## Convert
Convert nodes specifically convert from one data type to another.