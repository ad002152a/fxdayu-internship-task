# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:01:24 2018

@author: Administrator
"""

def run_formula(dv,param=None):
    sw1=dv.get_ts('sw1')
    dict_classify = {'480000': '银行', '430000': '房地产', '460000': '休闲服务', '640000': '机械设备', '240000': '有色金属', '510000': '综合', '410000': '公用事业', '450000': '商业贸易', '730000': '通信', '330000': '家用电器', '720000': '传媒', '630000': '电气设备', '270000': '电子', '490000': '非银金融', '370000': '医药生物', '710000': '计算机', '280000': '汽车', '340000': '食品饮料', '220000': '化工', '210000': '采掘', '230000': '钢铁', '650000': '国防军工', '110000': '农林牧渔', '420000': '交通运输', '620000': '建筑装饰', '350000': '纺织服装', '610000': '建筑材料', '360000': '轻工制造'}
    industry_list=list(dict_classify.values())
    industry_code=dict()
    for i in industry_list:
        industry_code[i]=sw1[sw1==i].dropna(axis=1,how='all').columns.tolist()
        import pandas as pd
        industry_PE=dict()
    for i in industry_list:
        industry_PE[i]=pd.DataFrame(dv.get_ts('pe')[industry_code[i]])
        industry_PE_mean=pd.DataFrame(columns=industry_list)
    for i in industry_PE.keys():
        industry_PE_mean[i]=industry_PE[i].median(axis=1)
    pe_industry=pd.DataFrame(columns=dv.get_ts('pe').columns)
    for i in industry_code.keys():
        for j in industry_code[i]:
            pe_industry[j]=dv.get_ts('pe')[j]/industry_PE_mean[i]
    dv.append_df(pe_industry,'pe_industry')
    return dv.get_ts('pe_industry')