import pandas as pd
from scipy.stats import norm

class recommendArea:
    def __init__(self, happiness, data):
        self.vacancy_rate = pd.read_csv('data/vacancy_rate.csv')
        self.rent = pd.read_csv('data/rent.csv')
        self.happiness = pd.DataFrame({'幸福度': happiness})
        self.rent_lim = float(data["answer"][-2])
        self.layout = int(data["answer"][-1])+1

    def calc_recommendation(self):
        # 必要なDataFrameを結合
        data = pd.concat([self.vacancy_rate['区'], 
                          self.vacancy_rate['全住宅空室率'], 
                          self.rent.iloc[:, self.layout], 
                          self.happiness], axis=1)
        
        # 「重み付き空室率 * 幸福度」により'指標'を作成
        data['重み付き空室率'] = data['全住宅空室率'].values / data.iloc[:, 2].values
        data['重み付き空室率'] = (data['重み付き空室率'].values - data['重み付き空室率'].min()) / (data['重み付き空室率'].max() - data['重み付き空室率'].min())
        data['重み付き空室率'] = data['重み付き空室率'].values * (data.iloc[:, 3].max() - data.iloc[:, 3].min()) + data.iloc[:, 3].min()
        indicator = data['重み付き空室率'].values * data.iloc[:, 3].values
        data['指標'] = indicator
        
        # 家賃の上限額でエリアを絞った上で,'指標'を基準に降順にソート
        data = data[data.iloc[:, 2] <= self.rent_lim].sort_values('指標', ascending=False)

        # 上位3つの区を抽出
        recommend_area = data['区'][:3].values

        return recommend_area

    def show_pareto(self):
        pareto = {
            'area': self.vacancy_rate['区'].values.reshape(-1).tolist(),
            'happiness': self.happiness.values.reshape(-1).tolist(),
            'contract_rate': [],
            'pareto_optimal_flag': []
        }

        # 家賃相場の値を平均,家賃相場の値の1/3を標準偏差とする正規分布に従うと仮定
        mu = self.rent.iloc[:, self.layout].values.reshape(-1).tolist()
        sigma = (self.rent.iloc[:, self.layout].values * (1/3)).reshape(-1).tolist()

        # 上記正規分布における希望家賃額の値がとる確率密度と空室率との積を成約率とする
        contract_rate = norm.pdf(self.rent_lim, mu, sigma) * self.vacancy_rate['全住宅空室率'].values
        # 上記正規分布における希望家賃額の値がとる累積分布値と空室率との積を成約率とする
        # contract_rate = norm.cdf(self.rent_lim, mu, sigma) * self.vacancy_rate['全住宅空室率'].values

        # 成約率を0-10の値にスケーリング
        contract_rate = (contract_rate - contract_rate.min()) * 10 / (contract_rate.max() - contract_rate.min())
        pareto['contract_rate'] = contract_rate.reshape(-1).tolist()

        # Pareto最適解ならTrueとするフラグ
        for i in range(len(pareto['contract_rate'])):
            flag_tmp = True
            for j in range(len(pareto['contract_rate'])):
                if pareto['happiness'][i] < pareto['happiness'][j] and pareto['contract_rate'][i] < pareto['contract_rate'][j]:
                    flag_tmp = False
                    break
            pareto['pareto_optimal_flag'].append(flag_tmp)

        return pareto
