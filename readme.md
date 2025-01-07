# ComfyUI FlowNodes
A [ComfyUI](https://github.com/comfyanonymous/comfyui) node pack containing nodes for basic programming logic.

## NOTICE:
FlowNodes is very WIP and early in development. If you encounter a problem, please create an issue.

# Table of contents
<!-- TOC -->
* [ComfyUI FlowNodes](#comfyui-flownodes)
  * [NOTICE:](#notice)
* [Table of contents](#table-of-contents)
* [Examples](#examples)
  * [Counter](#counter)
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
    * [Execute script (UNSAFE) / Stack params](#execute-script-unsafe--stack-params)
    * [Get persistent dict](#get-persistent-dict)
  * [Convert](#convert)
    * [Convert to type](#convert-to-type)
    * [Create empty object](#create-empty-object)
    * [Convert List to Batch/Batch to List](#convert-list-to-batchbatch-to-list)
    * [Create list](#create-list)
<!-- TOC -->

# Examples
## Counter
The counter counts up one number on each run, each run will re-execute all the required nodes.  
**Additional nodes used in the example:**
* String and Int from [Various ComfyUI Nodes by Type](https://github.com/jamesWalker55/comfyui-various)
* Show text from [ComfyUI custom scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

![Counter example](https://github.com/gitmylo/FlowNodes/blob/master/img/Counter%20example.jpg?raw=true)

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
*(Screenshot was taken before flow nodes got styled)*

# Nodes
If any nodes are missing from this list, please inform me by making an issue.

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
![Switch (Int)](https://github.com/gitmylo/FlowNodes/blob/master/img/Int%20switch.jpg?raw=true)

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
### Execute script (UNSAFE) / Stack params
**this node can be very unsafe because it executes user specified code. To check the code, look for imports. Nodes will automatically become red if they contain import statements.**  
Execute a python script, takes one input variable currently. Referred to in the code as `input0`.  
If a parameter stacker node is connected, the node can have multiple inputs, referred to as inputN where N is the number of the input.
**example**:
```python
out = input0  # Output the input, this node will do nothing, just pass through.
```
### Get persistent dict
This node lets you access the persistent dict. This is a dictionary which is available between runs. Note that it resets when the server is restarted. And it's not stored in the workflow. It's specifically for changing things between runs.

## Convert
Convert nodes specifically convert from one data type to another.
### Convert to type
Converts from one type to the selected type.
### Create empty object
Create an empty object. Currently supports dicts and lists.
### Convert List to Batch/Batch to List
Convert a list (Items are executed separately when put into another node) to a batch (Items are all given at once, but the node needs to support it.)  
This is most useful for reading/writing individual batch items using operation nodes. Or to give it as an input for a script node.  
![Batch and list convert](https://github.com/gitmylo/FlowNodes/blob/master/img/Batch%20List%20Convert.jpg?raw=true)
### Create list
Uses no-cache, so it won't lead to unexpected results with caching.  
Creates a python list containing the items. (Can be modified with write operation nodes, using flow is recommended in this case, merge flow after the last operation.)