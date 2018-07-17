# Insight Coding Challenge

### Author: Anvesh Kumar Perugu

## Challenge
To generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.

## Implementation Details

* Programming Language: Python
* Version: 3.6
* Sorting Algorithm: Heap Sort
* Type Checking: mypy

## Algorithm

* Reading file and calculating total_cost and unique identifiers of a particular drug.
* Getting the list of all drug_total cost by iterating through dictionary.
* Implementing the Heap Sort Algorithm for getting all the drug_total cost in descending order
* Iterating through the drug dictionary and matching the drug_total cost write the output to a file.

## Execution detials

* Run shell script run.sh which will execute python main.py

## Test Cases

* 

```
[PASS]: test_1 top_cost_drug.txt[PASS]: your-own-test_1 top_cost_drug.txt[Tue

 Jul 17 09:29:03 EDT 2018] 2 of 2 tests passed
```
