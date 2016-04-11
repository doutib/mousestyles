## Instruction:
We need to create unit tests for each module and test each function of the module
For example, suppose we have a file called *data_utils.py* with two functions *pull_locom_tseries_subset* and *total_time_rectangle_bins*, we should have a corresponding test file called *test_data_utils.py* with the *data_utils.py* imported and have two corresponding test functions called *test_pull_locom* and *test_total_time*.

## What aspects of a function need to be tested:
- check if it returns correct type of object
- check if it returns correct dimension
- check if it returns the correct value, by
	- prior knowledge
	- different implementation: i.e. use R vs Python; use Var(X) vs. E(X^2) - E(X)^2
	- theoretical derivation 
- "regression": if the function is improved (by speed, efficiency) while has same functionality, check the output is the same with older version.
- assert errors occured: i.e. when the function takes three arguements while we only give two, make sure the function will throw an error message 

## Useful Command: 
```python
from numpy.testing import assert_almost_equal, assert_equal, assert_array_equal, assert_array_almost_equal
```

## Styles: 
- actual: the actual output of the function being tested
- expected: the expected output according to prior knowledge or obtained through other methods
- assert_equal(actual, expected)

## Examples: [*test_data_utils.py*](https://github.com/berkeley-stat222/mousestyles)

## Run the tests with the command: ```make test```
