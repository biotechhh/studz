# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd
import re


def aracal(url_Ara):
    all_fastas_Ara = requests.get(url_Ara).text
    # In[*]
    fasta_list_Ara = re.split(r'\n(?=>)', all_fastas_Ara)
    # create a list of FASTA sequences and find all sequences with header mentioning SPIKE:
    [fasta for fasta in fasta_list_Ara if 'SPIKE' in fasta]
    # all_fastas1_split = all_fastas1.split(">sp|")
    # delete the first null value
    # fastas_list = [x for index, x in enumerate(all_fastas1_split) if index > 0]
    # In[*]
    # split each element in list
    # result_1 = [item.split('SV=', 1) for item in fastas_list]
    # method 1by  List Comprehension
    result_Ara = [re.split(r'(SV=\d+)', item) for item in fasta_list_Ara]
    # method 2 by range function
    # result2 = []
    # for i in range(len(fastas_list)):
    #    c =  re.split(r'SV=\d+', fastas_list[i])
    #    result2.append(c)
    # In[*]
    df_Ara = pd.DataFrame(result_Ara, columns=['orig', 'version', 'sequences'])
    df_Ara.orig = df_Ara.orig.str.replace(r">sp\|", '', regex=True)
    # split the column of all
    df_Ara[['Uniprotid', 'character']] = df_Ara.orig.str.split("|", expand=True, )

    # In[*]
    # split the column of character
    df_Ara[['protein', 'definition']] = df_Ara.character.str.split("_ARATH", expand=True)
    df_Ara = df_Ara.drop(['character'], axis=1)
    return df_Ara
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aracal()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# -*- coding: utf-8 -*-
