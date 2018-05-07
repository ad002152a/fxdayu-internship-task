# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:19:07 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    default_param={'t':9}
    if not param:
        param=default_param
    t=param['t']
    dv.add_formula("EMAHL","Ta('EMA',0,high_adj-low_adj,high_adj-low_adj,high_adj-low_adj,high_adj-low_adj,high_adj-close_adj,%s)"%param['t'],
                         is_quarterly=False,
                         add_data=True)
    dv.add_formula('EMA_Ratio_',"Ta('EMA',0,EMAHL,EMAHL,EMAHL,EMAHL,EMAHL,9)",
                              is_quarterly=False,
                              add_data=True)
    dv.add_formula('EMA_Ratio','EMAHL/EMA_Ratio_',
                             is_quarterly=False,
                             add_data=True)
    MassIndex=dv.add_formula('MassIndex_J','Ts_Sum(EMA_Ratio,25)',
                               is_quarterly=False,
                               add_data=True)
    return MassIndex
    