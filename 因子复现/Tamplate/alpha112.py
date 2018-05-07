# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:03:58 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    dv.add_formula('alpha112','((Ts_Sum(If((close_adj-Delay(close_adj,1))>0,(close_adj-Delay(close_adj,1)),0),12)-Ts_Sum(If((close_adj-Delay(close_adj,1))<0,Abs(close_adj-Delay(close_adj,1)),0),12))/(Ts_Sum(If((close_adj-Delay(close_adj,1))>0,(close_adj-Delay(close_adj,1)),0),12)+Ts_Sum(If((close_adj-Delay(close_adj,1))<0,Abs(close_adj-Delay(close_adj,1)),0),12))*100)',
                        is_quarterly=False,
                        add_data=True)
    return dv.get_ts('alpha112')