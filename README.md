# AI Test

Evaluating if AI-generated code can be practicaly used

## Idea

Use AI to generate code and use manually-created unittests to validate code results.

## Version 1

### AI Prompt

I would like to have a python function named find_unused().
The function must accepts 2 parameters:
parameter 1 name is supernet - a string containing IPv4 network address in CIDR format
parameter 2 name is used_subnets - a list of strings with each elemnet being IPv4 network address in CIDR format which is a subnets of the supernet (parameter 1).

The function must return a list of strings with each element being IPv4 network address in CIDR format. The element must be the largest possible subnet of a given supernet (parameter 1), but must not overlap any subnet already listed in the used_subnets (parameter 2).

Only python module netaddr can be used to build the function.

### Outcome

* AI: MS Copilot
* Experience: Run it in a separate browser window and just pasted the prompt.
* Result: The answer was generated immediately and I saved it in `version1.py`
* Example run output:
    ```
    $ python version1.py
    ['192.168.0.0/24', '192.168.3.0/24', '192.168.4.0/22', '192.168.8.0/21', '192.168.16.0/20', '192.168.32.0/19', '192.168.64.0/18', '192.168.128.0/17']
   ```
* Correctness: seems to be correct

### Validation