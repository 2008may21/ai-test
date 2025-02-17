# AI Test

Evaluating if AI-generated code can be practicaly used

## Idea

Use AI to generate code and use manually-created unittests to validate code results.

## AI Prompt

### Version 1
I would like to have a python function named find_unused().
The function must accepts 2 parameters:
parameter 1 name is supernet - a string containing IPv4 network address in CIDR format
parameter 2 name is used_subnets - a list of strings with each elemnet being IPv4 network address in CIDR format which is a subnets of the supernet (parameter 1).

The function must return a list of strings with each element being IPv4 network address in CIDR format. The element must be the largest possible subnet of a given supernet (parameter 1), but must not overlap any subnet already listed in the used_subnets (parameter 2).

Only python module netaddr can be used to build the function.
