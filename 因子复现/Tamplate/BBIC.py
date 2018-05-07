# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:53:13 2018

@author: Administrator
"""

def run_formula(dv,param=None):
   dv.add_formula('MA3','Ts_Mean(close_adj,3)',is_quarterly=False,add_data=True)
   dv.add_formula('MA6','Ts_Mean(close_adj,6)',is_quarterly=False,add_data=True)
   dv.add_formula('MA12','Ts_Mean(close_adj,12)',is_quarterly=False,add_data=True)
   dv.add_formula('MA24','Ts_Mean(close_adj,24)',is_quarterly=False,add_data=True)
   dv.add_formula('BBI_J','((MA3+MA6+MA12+MA24)/4)',is_quarterly=False,add_data=True)
   dv.add_formula('BBIC_J','BBI_J/close_adj',is_quarterly=False,add_data=True)
   return dv.get_ts('BBIC_J')