# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:37:26 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t':30}
    if not param:
        param=default_param
    dv.add_formula('high_r_std_Nm','StdDev(high_adj/Delay(close_adj,1),%s)'%param['t'],is_quarterly=False,add_data=True)
    return dv.get_ts('high_r_std_Nm')