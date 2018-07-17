import config
from helper import (
    get_drugcostuniqueid,
    get_drugcost,
    heap_sort,
    extract_max
)
from misc_utils import parse_command_line

def main() -> None:
    '''Main function for the complete execution of algorithm step by step'''
    drugcost_dict = get_drugcostuniqueid(config.PATH_INPUT_FILE)
    totalcost_by_drug = get_drugcost(drugcost_dict)
    max_heap = heap_sort(totalcost_by_drug)
    extract_max(max_heap, drugcost_dict, config.PATH_OUTPUT_FILE)


if __name__ == "__main__":
    #ARGS = parse_command_line()
    #input_file_path = ARGS.input_file_path
    #output_file_path = ARGS.output_file_path
    main()
