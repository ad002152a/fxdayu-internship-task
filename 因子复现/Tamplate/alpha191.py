# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:13:18 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t1':20,'t2':5}
    if not param:
        param=default_param
    dv.add_formula('alpha191','((Correlation(Ts_Mean(volume,%s),low_adj,%s)+(high_adj+low_adj)/2)-close_adj)'%(param['t1'],param['t2']),
                            is_quarterly=False,
                            add_data=True)
    return dv.get_ts('alpha191')