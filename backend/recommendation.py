import pandas as pd

class recommendArea:
    def __init__(self, happiness, data):
        self.vacancy_rate = pd.read_csv('data/vacancy_rate.csv')
        self.rent = pd.read_csv('data/rent.csv')
        self.happiness = pd.DataFrame({'幸福度': happiness})
        self.rent_lim = float(data["answer"][-2])
        self.layout = int(data["answer"][-1])+1

    def calc_recommendation(self):
        # 「空室率 * 幸福度」により'指標'を作成
        indicator = self.vacancy_rate['全住宅空室率'].values * self.happiness.values.reshape(-1,)
        indicator = pd.DataFrame({'指標': indicator})

        # 必要なDataFrameを結合
        data = pd.concat([self.vacancy_rate['区'], 
                          self.vacancy_rate['全住宅空室率'], 
                          self.rent.iloc[:, self.layout], 
                          self.happiness,
                          indicator], axis=1)
        
        # 家賃の上限額でエリアを絞った上で,'指標'を基準に降順にソート
        data = data[data.iloc[:, 2] <= self.rent_lim].sort_values('指標', ascending=False)

        # 上位3つの区を抽出
        recommend_area = data['区'][:3].values

        return recommend_area
