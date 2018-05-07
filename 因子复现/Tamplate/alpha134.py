# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:06:55 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t1':12,'t2':12}
    if not param:
        param=default_param
    dv.add_formula('alpha134','(((close_adj-Delay(close_adj,%s))/Delay(close_adj,%s))*volume)'%(param['t1'],param['t2']),
                   is_quarterly=False,
                   add_data=True)
    return dv.get_ts('alpha134')
    