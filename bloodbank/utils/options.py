KG = 'kg'
LB = 'lb'
GROUP_A = 'A'
GROUP_B = 'B'
GROUP_O = 'O'
GROUP_AB = 'AB'
CM = 'cm'
FT = 'ft'
G_L = 'g/L'
MMHG = 'mmHg'
CPDA_1 = 'CPDA-1'
SODIUM_CITRATE = 'NaCH'
RBC = 'RBC'
PLATELETS = 'PLATELETS'
PLASMA = 'PLASMA'
MALE = 'M'
FEMALE = 'F'
YES = True
NO = False


BLOOD_GROUPS = (
    (GROUP_A, 'A'),
    (GROUP_B, 'B'),
    (GROUP_O, 'O'),
    (GROUP_AB, 'AB'),
)

WEIGHT_UNITS = (
    (KG, 'Kilograms'),
    (LB, 'Pounds'),
)

HEIGHT_UNITS = (
    (CM, 'Centimeters'),
    (FT, 'Feet'),
)

HAEMOGLOBIN_UNITS = (
    (G_L, 'Gram per Liter'),
)

BLOOD_PRESSURE_UNITS = (
    (MMHG, 'Millimeters of Mercury'),
)

ANTICOAGULANTS = (
    (SODIUM_CITRATE, 'Sodium Citrate'),
)

BLOOD_PRODUCT_TYPES = (
    (RBC, 'Red Blood Cells'),
    (PLATELETS, 'Platelets'),
    (PLASMA, 'Plasma'),
)

GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

YES_NO = (
    (YES, 'Yes'),
    (NO, 'No'),
)
