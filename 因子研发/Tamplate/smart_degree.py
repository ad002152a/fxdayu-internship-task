# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:54:18 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t1':25,'t2':25}
    if not param:
        param=default_param
    dv.add_formula('smart_degree','Abs(Return(close_adj,%s))/Log(Ewma(volume,%s))'%(param['t1'],param['t2']),is_quarterly=False,add_data=True)
    return dv.get_ts('smart_degree')