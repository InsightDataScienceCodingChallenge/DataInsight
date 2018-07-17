import csv
from collections import defaultdict


def get_drugcostuniqueid(input_filepath: str):
    ''' Returns the dictionary of Drugs with total_cost and count of UniqueID'''
    with open(input_filepath,'r') as fileobj:
        drugcostcount_dict = defaultdict(list)
        druglastname_dict = defaultdict(dict)
        for prescription in csv.reader(fileobj):
            if len(drugcostcount_dict[prescription[3]]) == 0:
                drugcostcount_dict[prescription[3]].append(float(prescription[4]))
                drugcostcount_dict[prescription[3]].append(1)
                druglastname_dict[prescription[3]][prescription[1]] = [prescription[2]]
            else:
                drugcostcount_dict[prescription[3]][0] = round(drugcostcount_dict[prescription[3]][0]+float(prescription[4]),2)
                if prescription[1] not in druglastname_dict[prescription[3]]:
                    druglastname_dict[prescription[3]].clear()
                    druglastname_dict[prescription[3]][prescription[1]] = [prescription[2]]
                    drugcostcount_dict[prescription[3]][1] += 1
                else:
                    if prescription[2] not in druglastname_dict[prescription[3]][prescription[1]]:
                        druglastname_dict[prescription[3]][prescription[1]].append(prescription[2])
                        drugcostcount_dict[prescription[3]][1] += 1
    b = time.time()
    print(b)
    return drugcostcount_dict

'''Returns the list of totalcost of all Drugs'''
def get_drugcost(drugcostcount_dict):
    drug_cost = []
    for i in drugcostcount_dict:
        drug_cost.append(drugcostcount_dict[i][0])
    #print(drug_cost)
    return drug_cost

'''It just swaps the values with the given indices'''
def swap(index1,index2,li):
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp

'''returns the list of drug_totalcost with maxheapsort'''
def heap_sort(drug_cost):
    for i in range(len(drug_cost)//2 -1,-1,-1):
        heapify(i,drug_cost)
    #print(drug_cost)
    return drug_cost

'''this function performs the algorithm of Heapsort'''
def heapify(i,drug_cost):
    if 2*i + 1 == len(drug_cost) -1 and 2*i + 2 > len(drug_cost) -1:
        if drug_cost[i] < drug_cost[2*i +1]:
            swap(i,2*i +1,drug_cost)
            heapify(2*i +1,drug_cost)
    elif 2*i +1 < len(drug_cost) -1 and 2*i +2 <= len(drug_cost) -1:
        if drug_cost[i] < drug_cost[2*i +1]:
            greater = drug_cost[2*i +1]
            if greater < drug_cost[2*i +2]:
                swap(i,2*i +2,drug_cost)
                heapify(2*i +2,drug_cost)
            else:
                swap(i,2*i +1,drug_cost)
                heapify(2*i +1,drug_cost)
        elif drug_cost[i] < drug_cost[2*i +2]:
            swap(i,2*i +2,drug_cost)
            heapify(2*i +2,drug_cost)

def extract_max(drug_cost,dict):
    total_length = len(drug_cost)
    unique_drugcost = []
    for i in range(0,total_length):
        if i < total_length -1:
            max_cost = drug_cost[0]
            swap(0,-1,drug_cost)
            del drug_cost[-1]
            heapify(0,drug_cost)
        else:
            max_cost = drug_cost[0]
        if max_cost not in unique_drugcost:
            unique_drugcost.append(max_cost)
            drugmaxcostuniqueid_dict = {}
            drugs = []
            for j in dict:
                if dict[j][0] == max_cost:
                    drugmaxcostuniqueid_dict[j] = [dict[j][0],dict[j][1]]
                    drugs.append(j)
                    #del dict[j]
            for drug in drugs:
                del dict[drug]
                #print(len(dict))
            if len(drugs) == 1:
                with open('ph_out.txt','a') as f:
                    f.write('{},{},{}\n'.format(drugs[0],drugmaxcostuniqueid_dict[drugs[0]][1],drugmaxcostuniqueid_dict[drugs[0]][0]))
            else:
                sorted_list = heap_sort(drugs)
                length = len(sorted_list)
                for i in range(0,length):
                    if i < length -1:
                        first_drug = sorted_list[0]
                        swap(0,-1,sorted_list)
                        del sorted_list[-1]
                        heapify(0,sorted_list)
                    else:
                        first_drug = sorted_list[0]
                    #for item in desc_di:
                        #if item == d:
                    with open('ph_out.txt','a') as f:
                        f.write('{},{},{}\n'.format(first_drug,drugmaxcostuniqueid_dict[first_drug][1],drugmaxcostuniqueid_dict[first_drug][0]))

def main():
    dict1 = get_drugcostuniqueid()
    count = get_drugcost(dict1)
    max_heap = heap_sort(count)
    extract_max(max_heap,dict1)

main()
