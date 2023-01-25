# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd
import re


def elegcal(url_eleg):
    all_fastas_eleg = requests.get(url_eleg).text
    # In[*]
    fasta_list_eleg = re.split(r'\n(?=>)', all_fastas_eleg)
    # create a list of FASTA sequences and find all sequences with header mentioning SPIKE:
    [fasta for fasta in fasta_list_eleg if 'SPIKE' in fasta]
    # all_fastas1_split = all_fastas1.split(">sp|")
    # delete the first null value
    # fastas_list = [x for index, x in enumerate(all_fastas1_split) if index > 0]
    # In[*]
    # split each element in list
    # result_1 = [item.split('SV=', 1) for item in fastas_list]
    # method 1by  List Comprehension
    result_eleg = [re.split(r'(SV=\d+)', item) for item in fasta_list_eleg]
    # method 2 by range function
    # result2 = []
    # for i in range(len(fastas_list)):
    #    c =  re.split(r'SV=\d+', fastas_list[i])
    #    result2.append(c)
    # In[*]
    df_eleg = pd.DataFrame(result_eleg, columns=['orig', 'version', 'sequences'])
    df_eleg.orig = df_eleg.orig.str.replace(r">sp\|", '', regex=True)
    # split the column of all
    df_eleg[['Uniprotid', 'character']] = df_eleg.orig.str.split("|", expand=True, )
    # split the column of character
    df_eleg[['protein', 'definition']] = df_eleg.character.str.split("_CAEEL", expand=True)
    df_eleg = df_eleg.drop(['character'], axis=1)
    return df_eleg
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    elegcal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# -*- coding: utf-8 -*-
