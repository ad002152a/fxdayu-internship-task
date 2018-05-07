# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:43:15 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t1':30,'t2':30}
    if not param:
        param=default_param
    dv.add_formula('low_r_std_Nm','StdDev(low_adj/Delay(close_adj,1),%s)'%param['t1'],is_quarterly=False,add_data=True)
    dv.add_formula('high_r_std_Nm','StdDev(high_adj/Delay(close_adj,1),%s)'%param['t2'],is_quarterly=False,add_data=True)
    dv.add_formula('hml_r_std_Nm','high_r_std_Nm-low_r_std_Nm',is_quarterly=False,add_data=True)
    return dv.get_ts('hml_r_std_Nm')
