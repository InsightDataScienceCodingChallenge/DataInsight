import csv
from collections import defaultdict

import config



def main() -> None:
    '''Main function for the complete execution of algorithm step by step'''
    drugcost_dict = get_drugcostuniqueid(config.PATH_INPUT_FILE)
    totalcost_by_drug = get_drugcost(drugcost_dict)
    max_heap = heap_sort(totalcost_by_drug)
    extract_max(max_heap, drugcost_dict, config.PATH_OUTPUT_FILE)


if __name__ == "__main__":
    main()
