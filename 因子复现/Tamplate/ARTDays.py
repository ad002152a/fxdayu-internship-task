# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:33:56 2018

@author: Administrator
"""
'''因无法找到OpearatingNI和TP的数据，无法复现该因子,故选择编写ARTDays'''
def run_formula(dv, param = None):
    dv.add_field('ARTRate')
    dv.add_formula('ARTDays_J','360/ARTRate',is_quarterly=False,add_data=True)
    
    return dv.get_ts('ARTDays_J')