import pandas as pd
import lightgbm as lgb 


# 回答の配列から地域の幸福度を計算
def calc_happiness(data):
    columns = ['IAAB_E', 'IAAA_E', 'AAAX', 'AAAA', 'CKAB', 'AAAZ', 'AAAY', 'AAAU_01', 'CKAF_24', 'CKAF_21', 'CKAF_22']
    question = ['IAAB_E', 'AAAX', 'AAAA', 'CKAB', 'AAAZ', 'AAAY', 'AAAU_01', 'CKAF_24', 'CKAF_21', 'CKAF_22']
    exp_variable = ['CKAB', 'IAAA_E', 'IAAB_E', 'AAAA', 'AAAX', 'AAAY', 'AAAZ', 'AAAU_01']
    input_data = pd.DataFrame(columns=columns)
    for key, val in zip(question, data['answer']):
        input_data[key] = [int(val)] * 23
    input_data['IAAA_E'] = list(range(1, 24))
    for e in exp_variable:
        input_data[e] = input_data[e].astype('category')
    bst = lgb.Booster(model_file='gbm.txt')
    y_pred = bst.predict(input_data, num_iteration=bst.best_iteration)
    return list(y_pred)
