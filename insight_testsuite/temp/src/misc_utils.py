'''
Parse command line arguments
'''

import argparse

def parse_command_line() -> argparse.Namespace:
    '''Return parsed arguments from the command line'''
    parser = argparse.ArgumentParser('script for parsing commandline args')

    parser.add_argument(
        '-input_file_path',
        help='inputfilepath for input file of presecriptions',
        dest='input_file_path',
    )

    parser.add_argument(
        '-output_file_path',
        help='outputfilepath for listing drugs by totalcost and uniqueids in desc',
        dest='output_file_path',
    )
    return parser.parse_args()
