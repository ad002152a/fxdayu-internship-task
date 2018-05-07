# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:20:09 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t1':30,'t2':252}
    if not param:
        param=default_param
    dv.add_formula('bias_std_turn_Nm','(StdDev(turnover,%s)/StdDev(turnover,%s)-1)'%(param['t1'],param['t2']),is_quarterly=False,add_data=True)
    return dv.get_ts('bias_std_turn_Nm')
