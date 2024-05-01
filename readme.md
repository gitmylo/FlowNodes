# ComfyUI FlowNodes
A [ComfyUI](https://github.com/comfyanonymous/comfyui) node pack containing nodes for basic programming logic.

# Table of contents
<!-- TOC -->
* [ComfyUI FlowNodes](#comfyui-flownodes)
* [Table of contents](#table-of-contents)
* [Flow](#flow)
  * [What is "Flow"?](#what-is-flow)
* [Nodes](#nodes)
  * [Conditions](#conditions)
    * [If](#if)
    * [Switch (Bool)](#switch-bool)
    * [Switch (Int)](#switch-int)
  * [Comparisons](#comparisons)
    * [Compare (Both Int/Float)](#compare-both-intfloat)
  * [Logic](#logic)
    * [Operation](#operation)
  * [Math](#math)
    * [Expression (Both Int/Float)](#expression-both-intfloat)
  * [Function](#function)
    * [Regex match](#regex-match)
    * [Operations](#operations)
    * [Print to console](#print-to-console)
    * [Execute script (UNSAFE)](#execute-script-unsafe)
  * [Convert](#convert)
    * [Convert to type](#convert-to-type)
    * [Create empty object](#create-empty-object)
<!-- TOC -->

# Flow
## What is "Flow"?
Flow is a connection, which can be used to force comfyUI to perform function operations in a certain order. Flow is a single ton `None` value which can be passed through as optional input to enforce an order of operations.
A flow is started from one of the following:
1. a node with flow output
2. an `activate flow from any` node. (The input here is optional.)

Flows can be used in two ways
1. As input, for a node which takes a flow, like some of the function nodes.
2. As input for the `Merge flow (bottleneck)` node, this node makes sure the order is fixed, and can be used to repeat if the flow is repeated using a `repeater` node. (For example, from [Comfyui-custom-scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts))

![Flow](https://github.com/gitmylo/FlowNodes/blob/master/img/Flow%201.jpg?raw=true)

# Nodes
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
### Compare (Both Int/Float)
* Takes 2 inputs, and an operation.
* Returns the result of the operation on the two inputs.

## Logic
Logic nodes take 1/2 boolean inputs, and return a boolean.
### Operation
* Takes 2 booleans, and an operation
* Returns the result of the operation on the two inputs.

## Math
Math nodes take a few numerical inputs, and returns the result of the selected operation.
### Expression (Both Int/Float)
* Takes 2 inputs, and an operation.
* Returns the result of the operation on the two inputs.

## Function
Function nodes perform an operation on the inputs, and output the result. (Most similar to most other comfy nodes)
### Regex match
Takes a pattern and a string. Uses python regex. Returns an array containing the regex's matches.
### Operations
Simple operations like +, -, *, and some functions. Except they are executed on any object.
### Print to console
Prints its input to console. This is mainly for debugging.
### Execute script (UNSAFE)
**this function can be very unsafe because it executes user specified code. To check the code, look for imports.**  
Execute a python script, takes one input variable currently. Referred to in the code as `inp`.  
**example**:
```python
out = inp  # Output the input, this node will do nothing, just pass through.
```

## Convert
Convert nodes specifically convert from one data type to another.
### Convert to type
Converts from one type to the selected type.
### Create empty object
Create an empty object. Currently supports dicts and lists.