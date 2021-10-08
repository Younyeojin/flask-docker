import pandas as pd


class Crime(object):

    def exec(self):
        df = pd.read_csv('./data/police_positions.csv.csv', encoding='UTF-8', thousands=',')
        # 발생 합치기
        df['범죄 발생'] = df.loc[[''],[2, 5, ]]
        print(df.info())

if __name__ == '__main__':
    c = Crime()
    c.exec()