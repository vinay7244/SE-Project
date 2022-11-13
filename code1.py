'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    entropy = 0
    col_val = df[[df.columns[-1]]].values
    a, uniq_count = np.unique(col_val, return_counts = True)
    no_of_inst = len(col_val)
    if no_of_inst <= 1:
        return 0
    probs_arr = []
    for i in range(0, len(uniq_count)):
        probs = uniq_count[i]/no_of_inst 
        probs_arr.append(probs)
    for prob in probs_arr:
        if(prob!=0):
            entropy = entropy - (prob * np.log2(prob))
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    avg_info_attr = 0
    attr_val = df[attribute].values
    uniq_attr_val,uniq_attr_arr = np.unique(attr_val,return_counts = True)
    no_of_inst = len(attr_val)
    
    for attr_val in uniq_attr_val:
        sliced_dataframe = df[df[attribute] == attr_val]
        inst = sliced_dataframe[[sliced_dataframe.columns[-1]]].values
        inst_uniq_val,inst_uniq_counts = np.unique(inst, return_counts = True)
        total_count_each_instance = len(inst)
        entropy_of_attr_val = 0
        for i in inst_uniq_counts:
            j = i/total_count_each_instance
            if j != 0:
                entropy_of_attr_val = entropy_of_attr_val - (j*np.log2(j))
        avg_info_attr = avg_info_attr + entropy_of_attr_val*(total_count_each_instance/no_of_inst)
    return(abs(avg_info_attr))


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    info_gain = 0
    entropy_of_dataset = get_entropy_of_dataset(df)
    entropy_of_attr = get_avg_info_of_attribute(df, attribute)
    info_gain = entropy_of_dataset - entropy_of_attr
    return info_gain





#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    info_gains = {}
    selected_col = ''
    max_information_gain = float("-inf")
    for attribute in df.columns[:-1]:
        info_gain_of_attr = get_information_gain(df, attribute)
        if info_gain_of_attr > max_information_gain:
            selected_col = attribute
            max_information_gain = info_gain_of_attr
        info_gains[attribute] = info_gain_of_attr
    return (info_gains, selected_col)
