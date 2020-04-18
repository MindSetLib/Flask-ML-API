import h2o


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


def return_NewH2o_Frame():
    columns = [
        'LicAge',
        'Gender',
        'MariStat',
        'DrivAge',
        'HasKmLimit',
        'BonusMalus',
        'OutUseNb',
        'RiskArea',
        'VehUsg_Private',
        'VehUsg_Private+trip to office',
        'VehUsg_Professional',
        'VehUsg_Professional run',
        'CSP1',
        'CSP2',
        'CSP3',
        'CSP6',
        'CSP7',
        'CSP20',
        'CSP21',
        'CSP22',
        'CSP26',
        'CSP37',
        'CSP40',
        'CSP42',
        'CSP46',
        'CSP47',
        'CSP48',
        'CSP49',
        'CSP50',
        'CSP55',
        'CSP56',
        'CSP57',
        'CSP60',
        'CSP65',
        'CSP66'
    ]
    return h2o.H2OFrame(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        column_names=columns)

def process_input(json_input):
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
    CSP6 = 0
    CSP7 = 0
    CSP20 = 0
    CSP21 = 0
    CSP22 = 0
    CSP26 = 0
    CSP37 = 0
    CSP40 = 0
    CSP42 = 0
    CSP46 = 0
    CSP47 = 0
    CSP48 = 0
    CSP49 = 0
    CSP50 = 0
    CSP55 = 0
    CSP56 = 0
    CSP57 = 0
    CSP60 = 0
    CSP65 = 0
    CSP66 = 0

    hf = return_NewH2o_Frame()

    hf[0, 'LicAge'] = LicAge
    hf[0, 'Gender'] = Gender
    hf[0, 'MariStat'] = MariStat
    hf[0, 'DrivAge'] = DrivAge
    hf[0, 'HasKmLimit'] = HasKmLimit
    hf[0, 'BonusMalus'] = BonusMalus
    hf[0, 'OutUseNb'] = OutUseNb
    hf[0, 'RiskArea'] = RiskArea
    hf[0, 'VehUsg_Private'] = VehUsg_Private
    hf[0, 'VehUsg_Private+trip to office'] = VehUsg_Private_trip_to_office
    hf[0, 'VehUsg_Professional'] = VehUsg_Professional
    hf[0, 'VehUsg_Professional run'] = VehUsg_Professional_run
    hf[0, 'CSP1'] = CSP1
    hf[0, 'CSP2'] = CSP2
    hf[0, 'CSP3'] = CSP3
    hf[0, 'CSP6'] = CSP6
    hf[0, 'CSP7'] = CSP7
    hf[0, 'CSP20'] = CSP20
    hf[0, 'CSP21'] = CSP21
    hf[0, 'CSP22'] = CSP22
    hf[0, 'CSP26'] = CSP26
    hf[0, 'CSP37'] = CSP37
    hf[0, 'CSP40'] = CSP40
    hf[0, 'CSP42'] = CSP42
    hf[0, 'CSP46'] = CSP46
    hf[0, 'CSP47'] = CSP47
    hf[0, 'CSP48'] = CSP48
    hf[0, 'CSP49'] = CSP49
    hf[0, 'CSP50'] = CSP50
    hf[0, 'CSP55'] = CSP55
    hf[0, 'CSP56'] = CSP56
    hf[0, 'CSP57'] = CSP57
    hf[0, 'CSP60'] = CSP60
    hf[0, 'CSP65'] = CSP65
    hf[0, 'CSP66'] = CSP66
    return hf
