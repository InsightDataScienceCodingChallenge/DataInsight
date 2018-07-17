'''helper functions for main module'''

import csv
from collections import defaultdict
from typing import Dict, Union, List

def get_drugcostuniqueid(
        input_filepath: str
) -> Dict[str, List[Union[float, str]]]:
    '''Returns the dictionary of Drugs with total_cost and count of UniqueID

   :param input_filepath: path to input file
    '''
    with open(input_filepath,'r') as fileobj:
        next(fileobj)
        drugcost_dict = defaultdict(list)
        drugln_dict = defaultdict(dict)
        for row in csv.reader(fileobj):
            if len(drugcost_dict[row[3]]) == 0:
                drugcost_dict[row[3]].append(float(row[4]))
                drugcost_dict[row[3]].append(1)
                drugln_dict[row[3]][row[1]] = [row[2]]
            else:
                drugcost_dict[row[3]][0] = round(
                    drugcost_dict[row[3]][0]
                    + float(row[4]),2
                )
                if row[1] not in drugln_dict[row[3]]:
                    drugln_dict[row[3]].clear()
                    drugln_dict[row[3]][row[1]] = [row[2]]
                    drugcost_dict[row[3]][1] += 1
                else:
                    if row[2] not in drugln_dict[row[3]][row[1]]:
                        drugln_dict[row[3]][row[1]].append(row[2])
                        drugcost_dict[row[3]][1] += 1
    return drugcost_dict

def get_drugcost(
        drugcost_dict: Dict[str, List[Union[float, int]]]
) -> List[float]:
    '''Returns the list of totalcost of all Drugs

    :parma drugcost_dict: dictionary with key as drug and values with cost
                          and distinct unique id's
    '''
    return [drugcost_dict[i][0] for i in drugcost_dict]

def swap(index1: int, index2: int, li: List[float]):
    '''It just swaps the values with the given indices
    '''
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp

def heap_sort(drug_cost: List[float]) -> List[float]:
    '''Returns the list of drug_totalcost with maxheapsort

    :param drug_cost: list of total sum values by drug name
    '''
    for index in range(len(drug_cost)//2 -1,-1,-1):
        heapify(index, drug_cost)
    return drug_cost

def heapify(index: int, drug_cost: List[float]) -> None:
    '''This function performs the algorithm of Heapsort

    :param index: indices of nodes in a binary tree
    :param drug_cost: list of total sum values by drug name
    '''
    if 2*index + 1 == len(drug_cost) -1 and 2*index + 2 > len(drug_cost) -1:
        if drug_cost[index] < drug_cost[2*index +1]:
            swap(index, 2*index + 1, drug_cost)
            heapify(2*index + 1,drug_cost)
    elif 2*index +1 < len(drug_cost) -1 and 2*index +2 <= len(drug_cost) -1:
        if drug_cost[index] < drug_cost[2*index +1]:
            greater = drug_cost[2*index +1]
            if greater < drug_cost[2*index +2]:
                swap(index,2*index +2,drug_cost)
                heapify(2*index +2,drug_cost)
            else:
                swap(index,2*index +1,drug_cost)
                heapify(2*index +1,drug_cost)
        elif drug_cost[index] < drug_cost[2*index +2]:
            swap(index,2*index +2,drug_cost)
            heapify(2*index +2,drug_cost)

def extract_max(
        drug_cost: List[float],
        drugcost_dict: Dict[str, List[Union[float, int]]],
        outputfile_path: str
) -> None:
    '''
    Extracts the max element and searches in a dict to get the
    required drug_name along with total_cost and Count_Unique_prescribers

    :param drug_cost: list of total cost by drug name post building Max heap
    :param drugcost_dict: dict of drugs with total_cost and count of UniqueID
    '''
    with open(outputfile_path, 'w') as fileobj:
        fileobj.write('{},{},{}\n'.format('drug_name',
                                          'num_prescriber',
                                          'total_cost'))
        total_length = len(drug_cost)
        unique_drugcost = []
        for i in range(total_length):
            if i < total_length -1:
                max_cost = drug_cost[0]
                swap(0, -1, drug_cost)
                del drug_cost[-1]
                heapify(0,drug_cost)
            else:
                max_cost = drug_cost[0]
            if max_cost not in unique_drugcost:
                unique_drugcost.append(max_cost)
                drugmaxcostuniqueid_dict = {}
                drugs = []
                for j in drugcost_dict:
                    if drugcost_dict[j][0] == max_cost:
                        drugmaxcostuniqueid_dict[j] = [drugcost_dict[j][0],
                                                       drugcost_dict[j][1]]
                        drugs.append(j)
                if len(drugs) == 1:
                    fileobj.write('{},{},{}\n'.format(
                        drugs[0],
                        drugmaxcostuniqueid_dict[drugs[0]][1],
                        drugmaxcostuniqueid_dict[drugs[0]][0]))
                else:
                    sorted_list = heap_sort(drugs)
                    length = len(sorted_list)
                    for i in range(length):
                        if i < length -1:
                            first_drug = sorted_list[0]
                            swap(0,-1,sorted_list)
                            del sorted_list[-1]
                            heapify(0,sorted_list)
                        else:
                            first_drug = sorted_list[0]
                        fileobj.write('{},{},{}\n'.format(
                            first_drug,
                            drugmaxcostuniqueid_dict[first_drug][1],
                            drugmaxcostuniqueid_dict[first_drug][0]))
