# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:44:44 2021

@author: Seong
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Seong/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)
