#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
import sys
sys.path.append("..")
from pyroxene_processor.module import *
from pyroxene_processor.global_variable import *
from pyroxene_processor.exception import *

def base_calculator(dataset, pattern=1):
    """calculator for the data set with designated oxide, store the results in "./results/***.xlsx"

    :param dataset: data set, like cpx_data, spl_data
    :param pattern: one of the three patterns
    """
    data_path = os.path.join(DATASET_PATH, dataset)
    try:
        data = pd.read_excel(data_path, engine='openpyxl')
    except ModuleNotFoundError:
        print("** Please download openpyxl by pip3 **")

    # replace the data whose kind is string with specific number 'NULL2VALUE'
    data = check_data_type(data)

    # fill the missing value with specific number 'NULL2VALUE'
    data = missing_filled(data, NULL2VALUE)
    # print(data.head())

    # combine the columns of FeO and Fe2O3 in a specific formula
    data = merge_fe(data)
    print("The oxides sheet: ")
    print(data)

    # check whether the basic oxides data is included in the data set
    check_oxide(data, pattern)

    print("Calculate cation data ......")

    # the name of the oxides
    data_columns = list(data.columns)

    # the number of cation and oxygen atom
    ion_num, oxy_num = find_num(data_columns)

    # the name of the cation
    ion = find_cation(data_columns)

    # relative molecular mass
    rmw = rel_mole_weight(ion, ion_num, oxy_num)

    # calculate the normalization factor
    normalization_factor = normalization_factor_calculation(rmw, oxy_num, data, pattern)

    # calculate the cation of the formula
    cation_formula = cation_formula_calculation(normalization_factor, rmw, ion_num, data, ion)

    # extract the designated columns according to different models
    if pattern == 1 or pattern == 2:
        cation_df = cation_formula[CPX_ION]
    elif pattern == 3:
        cation_df = cation_formula[SPL_ION]

    # change the value which is zero into 0.0000001
    cation_df_transformed = transform(cation_df)
    print("Replace the cation data 0 with 0.0000001")
    print("The cation sheet :")
    print(cation_df_transformed)

    # store the data in the form of .xlsx file with default name in a specific pattern
    # or designated name "df_name=sheet_name"
    result2sheet(cation_df_transformed, pattern=pattern)

def calculate(cpx_dataset, spl_dataset=None, pattern=1):
    """output the result of calculation in "***.xlsx" form with a specific pattern

    :param cpx_dataset: cpx data set
    :param spl_dataset: spl data set
    :param pattern: one of the three patterns
    """
    if pattern == 1 or pattern == 2:
        print("Processing the cpx data sheet ......")
        base_calculator(cpx_dataset, pattern)
    elif pattern == 3:
        print("Processing the cpx data sheet ......")
        base_calculator(cpx_dataset, 1)
        print("Processing the spl data sheet ......")
        base_calculator(spl_dataset, 3)



