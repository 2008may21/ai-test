# AI Test

## Idea

Use AI to implement business logic and validate results with manually (not AI) created tests.


## Outcome

* Code was generated instantly.
* Code yeided 100% correct results.
* Manually created unittests were a good way to validate code correctness and have piece of mind.


## Details

### Procedure
1. MS Copilot was used `as is` in Windows 10.
1. No any customization was applied to MS Copilot.
1. The following prompt was pasted into Copilot's chat input field:
    ```
    I would like to have a python function named find_unused().
    The function must accepts 2 parameters:
    parameter 1 name is supernet - a string containing IPv4 network address in CIDR format
    parameter 2 name is used_subnets - a list of strings with each elemnet being IPv4 network address in CIDR format which is a subnets of the supernet (parameter 1).

    The function must return a list of strings with each element being IPv4 network address in CIDR format. The element must be the largest possible subnet of a given supernet (parameter 1), but must not overlap any subnet already listed in the used_subnets (parameter 2).

    Only python module netaddr can be used to build the function.
    ```
1. Results were generated immediatelly (no latency/delay was noticed).
1. Copilot's answer was saved into `version1.py` (can be found in this repository)
1. Upon running, the following output was generated:
    ```
    $ python version1.py
    ['192.168.0.0/24', '192.168.3.0/24', '192.168.4.0/22', '192.168.8.0/21', '192.168.16.0/20', '192.168.32.0/19', '192.168.64.0/18', '192.168.128.0/17']
   ```
1. Result seemed to be correct

### Quality Assurance
1. Example at the end of `version1.py` was commented out.
1. `test_version1.py` was _manually_ created (can be found in this repository) with test-sets.
1. All tests passed!.. Wow!


## Conclusion
This excercise indicates that AI _can be_ used as a programmer-agent taken care of, at least, simple tasks assuming that proper quality assurance controls are in place.
