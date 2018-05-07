# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:34:28 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t':30}
    if not param:
        param=default_param
    dv.add_formula('std_turn_Nm','StdDev(turnover,%s)'%(param['t']),is_quarterly=False,add_data=True)
    return dv.get_ts('std_turn_Nm')