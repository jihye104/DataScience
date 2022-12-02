import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

import random

sex_range=['남성', '여성']
# sex_range[0], sex_range[1]
# sex_range[[0]] => x
age_range=[20,21,22,23,24,25,26,27,28,29]
marrage_range=['독신','기혼','재혼']
income_range=['저소득자','3000만원대','4000만원대','5000만원대','6000만원대','고소득자']

MAX_RECORD=100000

sex_list=[]
age_list=[]
marrage_list=[]
income_list=[]


for i in range(MAX_RECORD):
    sex_list.append(
        sex_range[
            random.choices(
                range(0,len(sex_range)),
                weights=[0.35,0.65])[0]
        ]
    )
    #[0] 또는 [1]
    age_list.append(age_range[random.choices(range(0,len(age_range)), weights=[0.05,0.05,0.1,0.07,0.05,0.05,0.05,0.13,0.3,0.2])[0]])
    marrage_list.append(marrage_range[random.choices(range(0,len(marrage_range)), weights=[0.7,0.25,0.05])[0]])
    income_list.append(income_range[random.choices(range(0,len(income_range)), weights=[0.1,0.4,0.2,0.15,0.1,0.05])[0]])