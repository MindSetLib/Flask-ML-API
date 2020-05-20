import pandas as pd
import numpy as np

def map_for_dict_Gender(Gender):
    dict_Gender = {'Male': 0, 'Female': 1}
    res = dict_Gender.get(Gender)
    return res


def map_for_dict_MariStat(MariStat):
    dict_MariStat = {'Other': 0, 'Alone': 1}
    res = dict_MariStat.get(MariStat)
    return res


def f_VehUsage_Professional(VehUsage):
    if VehUsage == 'Professional':
        VehUsage_Professional = 1
    else:
        VehUsage_Professional = 0
    return VehUsage_Professional


def f_VehUsage_Private_trip_to_office(VehUsage):
    if VehUsage == 'Private+trip to office':
        VehUsage_Private_trip_to_office = 1
    else:
        VehUsage_Private_trip_to_office = 0
    return VehUsage_Private_trip_to_office


def f_VehUsage_Private(VehUsage):
    if VehUsage == 'Private':
        VehUsage_Private = 1
    else:
        VehUsage_Private = 0
    return VehUsage_Private


def f_VehUsage_Professional_run(VehUsage):
    if VehUsage == 'Professional run':
        VehUsage_Professional_run = 1
    else:
        VehUsage_Professional_run = 0
    return VehUsage_Professional_run

# def f_DrivAgeSq(DrivAge):
#     return DrivAge**2

# def return_Data_Frame():
#     columns_list = [
#         'LicAge',
#         'Gender',
#         'MariStat',
#         'DrivAge',
#         'HasKmLimit',
#         'BonusMalus',
#         'OutUseNb',
#         'RiskArea',
#         'VehUsg_Private',
#         'VehUsg_Private+trip to office',
#         'VehUsg_Professional',
#         'VehUsg_Professional run',
#         'SocioCateg_CSP1',
#         'SocioCateg_CSP2',
#         'SocioCateg_CSP3',
#         'SocioCateg_CSP6',
#         'SocioCateg_CSP7',
#         'DrivAgeSq'
#     ]
#     return pd.DataFrame(
#         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#         column_names=columns)

def process_input(json_input):

    columns_list =['LicAge', 'Gender', 'MariStat', 'DrivAge', 'HasKmLimit', 'BonusMalus',
     'OutUseNb', 'RiskArea', 'VehUsage_Private',
     'VehUsage_Private+trip to office', 'VehUsage_Professional',
     'VehUsage_Professional run', 'SocioCateg_CSP1', 'SocioCateg_CSP2',
     'SocioCateg_CSP3', 'SocioCateg_CSP4', 'SocioCateg_CSP5',
     'SocioCateg_CSP6', 'SocioCateg_CSP7', 'DrivAgeSq']

    LicAge = json_input["LicAge"]
    Gender = map_for_dict_Gender(json_input["Gender"])
    MariStat = map_for_dict_MariStat(json_input["MariStat"])
    DrivAge = json_input["DrivAge"]
    HasKmLimit = json_input["HasKmLimit"]
    BonusMalus = json_input["BonusMalus"]
    OutUseNb = json_input["OutUseNb"]
    RiskArea = json_input["RiskArea"]
    VehUsg_Private = f_VehUsage_Private(json_input["VehUsage"])
    VehUsg_Private_trip_to_office = f_VehUsage_Private_trip_to_office(json_input["VehUsage"])
    VehUsg_Professional = f_VehUsage_Professional(json_input["VehUsage"])
    VehUsg_Professional_run = f_VehUsage_Professional_run(json_input["VehUsage"])


    CSP1 = 0
    CSP2 = 0
    CSP3 = 0
    CSP4 = 0
    CSP5 = 0
    CSP6 = 0
    CSP7 = 0

    DrivAgeSq = json_input["DrivAge"] ** 2



    data_list=[(LicAge, Gender,  MariStat, DrivAge,
               HasKmLimit, BonusMalus, OutUseNb, RiskArea,
               VehUsg_Private, VehUsg_Private_trip_to_office,
               VehUsg_Professional, VehUsg_Professional_run,
               CSP1, CSP2, CSP3, CSP4, CSP5, CSP6, CSP7,
               DrivAgeSq)]


    print(data_list)

    df = pd.DataFrame.from_records(data_list, columns=columns_list)

    return df