# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd
import re


def cocal(url_coli):
    all_fastas_coli = requests.get(url_coli).text
    # In[*]
    fasta_list_coli = re.split(r'\n(?=>)', all_fastas_coli)
    # create a list of FASTA sequences and find all sequences with header mentioning SPIKE:
    [fasta for fasta in fasta_list_coli if 'SPIKE' in fasta]
    # all_fastas1_split = all_fastas1.split(">sp|")
    # delete the first null value
    # fastas_list = [x for index, x in enumerate(all_fastas1_split) if index > 0]
    # In[*]
    # split each element in list
    # result_1 = [item.split('SV=', 1) for item in fastas_list]
    # method 1by  List Comprehension
    result_coli = [re.split(r'(SV=\d+)', item) for item in fasta_list_coli]
    # method 2 by range function
    # result2 = []
    # for i in range(len(fastas_list)):
    #    c =  re.split(r'SV=\d+', fastas_list[i])
    #    result2.append(c)
    df_coli = pd.DataFrame(result_coli, columns=['orig', 'version', 'sequences'])
    df_coli.orig = df_coli.orig.str.replace(r">sp\|", '', regex=True)
    # split the column of all
    df_coli[['Uniprotid', 'character']] = df_coli.orig.str.split("|", expand=True, )
    # In[*]
    # split the column of character
    df_coli[['protein', 'definition']] = df_coli.character.str.split("_ECOLI", expand=True)
    df_coli = df_coli.drop(['character'], axis=1)
    return df_coli
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cocal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# -*- coding: utf-8 -*-
