# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:57:52 2018

@author: Administrator
"""
def run_formula(dv,param=None):
    default_param={'t1':1,'t2':1,'t3':1,'t4':1,'t5':20}
    if not param:
        param=default_param
    dv.add_formula('alpha59',
                       'Ts_Sum(If(close_adj==Delay(close_adj,%s),0,close_adj-If(close_adj>Delay(close_adj,%s),Min(low_adj,Delay(close_adj,%s)),Max(high_adj,Delay(close_adj,%s)))),%s)'%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5']),
                       is_quarterly=False,
                       add_data=True)
    return dv.get_ts('alpha59')