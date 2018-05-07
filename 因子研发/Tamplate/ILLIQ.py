# -*- coding: utf-8 -*-
"""
Created on Mon May  7 09:08:06 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t':30}
    if not param:
        param=default_param
    dv.add_formula("ILLIQ","(Ts_Mean((Return(close_adj,1)/(float_mv)),%s))"%(param['t']),is_quarterly=False,add_data=True)
    return dv.get_ts('ILLIQ')