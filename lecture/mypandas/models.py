import random
import string

import numpy as np
import pandas as pd
from icecream import ic


class MyPandas(object):
    def id(self):
        return "".join(random.choice(string.ascii_letters) for i in range(5))

    def score(self):
        a = np.random.randint(0, 100)
        return a

    def __init__(self):
        print('### PANDAS QUIZ ###')
        '''
        ic| df1:   a  b  c
                1  1  3  5
                2  2  4  6
        '''
        df1 = pd.DataFrame({'a':[1,2], 'b':[3,4], 'c':[5,6]}, index=[1,2])
        df1_1 = pd.DataFrame.from_dict({"1":[1,3,5],"2":[2,4,6]}, orient='index', columns=['a','b','c'])
        ic('Q1')
        ic(df1)
        ic(df1_1)
        # df1 = self.df1_dict()
        # ic(df1)
        # def df1_dict(self):
        #   return pd.DataFrame({'a':[1,2], 'b':[3,4], 'c':[5,6]}, index=[1,2])
        #   return pd.DataFrame.from_dict({"1":[1,3,5],"2":[2,4,6]}, orient='index', columns=['a','b','c'])
        '''
        ic| df2:     A   B   C
                 1   1   2   3
                 2   4   5   6
                 3   7   8   9
                 4  10  11  12

        '''
        df2 = pd.DataFrame({'A': range(1, 11, 3), 'B': range(2, 12, 3), 'C': range(3, 13, 3)},
                           index=range(1, 5))
        df2_1 = pd.DataFrame([[1,2,3],
                             [4,5,6],
                             [7,8,9],
                             [10,11,12]], index=range(1,5),columns=['A','B','C'])
        ic('Q2')
        ic(df2)
        ic(df2_1)
        '''
        ic| df3:     0   1   2
                 0  18  33  43
                 1  63  32  53
        '''
        df3 = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic('Q3')
        ic(df3)
        '''
        ic| df4:       국어  영어   수학  사회
                 ipetl  39  52   96  60
                 RDZrZ  22  82   27  49
                 HOigd  39  47    9  19
                 VZEuz  97  94   45  19
                 AukYQ  64  61   25  52
                 cEFIS  23  75   91  97
                 kVNfa  13   1   59   0
                 XIYVu  32  69  100  60
                 wcNKj   3  82   18  56
                 yPuaY  92  60   69  63

        '''
        score = [list(map(lambda x: np.random.randint(0, 101), [i for i in range(1, 5)])) for i in range(1, 11)]
        students = ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
        subjects = ['국어', '영어', '수학', '사회']
        df4 = pd.DataFrame(score, index=students, columns=subjects)
        ic('Q4')
        ic(df4)
        # def score_random(self):
        #   return pd.DataFrame(np.random.randint(0, 100, (10, 4)),
        #   index=["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)],
        #   columns=['국어','영어','수학','사회'])
        '''
        ic| df5:       국어  영어  수학  사회
                 ckSVA  93  44  14  94
                 CAOot  25  54  29  10
                 fZTCh  82  65  31  31
                 mqZJJ  51  56  56   3
                 BKlLt  34  32  67  48
                 KKYUN  85  24  16   8
                 WAjFK  28  80  52  43
                 yBVgG  25  94  93  54
                 lGmwZ  32  50  95   1
                 GQzmY  26  37  80  27
        '''
        df5 = pd.DataFrame()
        name_list = []
        df5['국어'] = 0
        df5['영어'] = 0
        df5['수학'] = 0
        df5['사회'] = 0

        df5.loc['ckSVA'] = [93, 44, 14, 94]
        df5.loc['CAOot'] = [25, 54, 29, 10]
        df5.loc['fZTCh'] = [82, 65, 31, 31]
        df5.loc['mqZJJ'] = [51, 56, 56, 3]
        df5.loc['BKlLt'] = [34, 32, 67, 48]
        df5.loc['KKYUN'] = [85, 24, 16, 8]
        df5.loc['WAjFK'] = [28, 80, 52, 43]
        df5.loc['yBVgG'] = [25, 94, 93, 54]
        df5.loc['lGmwZ'] = [32, 50, 95, 1]
        df5.loc['GQzmY'] = [26, 37, 80, 27]
        ic('Q5')
        ic(df5)

        df_by_other_method = pd.DataFrame({
            '국어': self.score(),
            '영어': self.score(),
            '수학': self.score(),
            '사회': self.score()
        }, index=[self.id()])

        for i in range(1, 10):
            df_by_other_method.loc[self.id()] = {
                '국어': self.score(),
                '영어': self.score(),
                '수학': self.score(),
                '사회': self.score()
            }
        '''
        score = list(zip(["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)],
                 [list(map(lambda x: np.random.randint(0, 101), [i for i in range(1, 5)])) for i in range(1, 11)]))
        subjects = ['국어', '영어', '수학', '사회']
        df_by_other_method = [subjects, score ]
        ic(df_by_other_method)
        '''
        # subjects = ['국어', '영어', '수학', '사회']
        # scores = [np.random.randint(0, 101) for i in range(1, 5)]
        # student = "".join(random.choice(string.ascii_letters) for i in range(5))
        # dt = dict(zip(subjects, scores))
        # ic(dt)
        df5 = pd.DataFrame(dict(zip(['국어', '영어', '수학', '사회'],
                                      [np.random.randint(0, 101) for i in range(5)])),
                             index=["".join(random.choice(string.ascii_letters) for i in range(5))])
        for i in range(1,10):
            df5.loc["".join(random.choice(string.ascii_letters) for i in range(5))] = \
                dict(zip(['국어', '영어', '수학', '사회'], list(map(lambda x:np.random.randint(0, 101), range(5)))))
        ic(df5)
        '''
        ic| df5.loc[:,'국어']: losDz     5
                              dSguf    54
                              WhNoo    67
                              rqddf    40
                              rYNfy    23
                              CFfHt    28
                              oCbFp    79
                              WtXBG    40
                              AUfnJ    74
                              Zlget    82
                              Name: 국어, dtype: int64
        '''
        ic('Q5-1')
        ic(df5.loc[:,'국어'])
        ''' 
        Q5-2 TdQOI 점수만 출력
        ic| TdQOI	15	42	59	67
        '''
        ic('Q5-2')
        ic(df5.iloc[[0], :])
        ''' 
        Q5-3 기존 학생들에게 과학과목과 점수를 랜덤으로 추가
        ic| df5:     국어  영어  수학  사회  과학
                 hVoGW  93  44  14  94  86
                 QkpKK  25  54  29  10   8
                 oDmky  82  65  31  31   2
                 qdTeX  51  56  56   3  13
                 XGzWk  34  32  67  48  23
                 PAwgj  85  24  16   8  22
                 vnTmB  28  80  52  43  48
                 wuxIm  58  94  93  54  83
                 AOQFG  32  50  95   1  52
                 jHChe  59  37  80  27  39
        '''
        df5.loc[:, '과학'] = pd.Series([np.random.randint(0,101) for i in range(1,11)],
                                     index=df5.index)
        ic('Q5-3')
        ic(df5)
        ''' 
        Q5-4 각 학생들의 점수의 총점을 표현하는 컬럼을 추가
        ic| df5:    국어  영어  수학  사회  과학   총점
                 hVoGW  93  44  14  94  86  331
                 QkpKK  25  54  29  10   8  126
                 oDmky  82  65  31  31   2  211
                 qdTeX  51  56  56   3  13  179
                 XGzWk  34  32  67  48  23  204
                 PAwgj  85  24  16   8  22  155
                 vnTmB  28  80  52  43  48  251
                 wuxIm  58  94  93  54  83  382
                 AOQFG  32  50  95   1  52  230
                 jHChe  59  37  80  27  39  242
        '''
        df5['총점'] = df5.sum(axis=1)
        ic('Q5-4')
        ic(df5)
        ''' 
        Q5-5 각 학생들의 점수의 총합을 리스트로 출력
            ic| ls: [547, 536, 533, 319, 376, 2311]
        '''
        ls5 = df5.sum().tolist()
        ic('Q5-5')
        ic(ls5)
        ''' 
        Q5-6 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
        ic| df5:  국어   영어   수학   사회   과학    총점
                 hVoGW   93   44   14   94   86   331
                 QkpKK   25   54   29   10    8   126
                 oDmky   82   65   31   31    2   211
                 qdTeX   51   56   56    3   13   179
                 XGzWk   34   32   67   48   23   204
                 PAwgj   85   24   16    8   22   155
                 vnTmB   28   80   52   43   48   251
                 wuxIm   58   94   93   54   83   382
                 AOQFG   32   50   95    1   52   230
                 jHChe   59   37   80   27   39   242
                 과목총점   547  536  533  319  376  2311
        '''
        df5.loc['과목총점'] = ls5
        ic('Q5-6')
        ic(df5)
        ''' 
        Q5-7 방금 추가한 과목총점 삭제
        ic| df5:  국어  영어  수학  사회  과학   총점
                 hVoGW  93  44  14  94  86  331
                 QkpKK  25  54  29  10   8  126
                 oDmky  82  65  31  31   2  211
                 qdTeX  51  56  56   3  13  179
                 XGzWk  34  32  67  48  23  204
                 PAwgj  85  24  16   8  22  155
                 vnTmB  28  80  52  43  48  251
                 wuxIm  58  94  93  54  83  382
                 AOQFG  32  50  95   1  52  230
                 jHChe  59  37  80  27  39  242
        '''
        df5.drop('과목총점', inplace=True)
        ic('Q5-7')
        ic(df5)
        '''                         
        Q5-8 총점 열 기준 내림차순 정렬
                 wuxIm  58  94  93  54  83  382
                 hVoGW  93  44  14  94  86  331
                 vnTmB  28  80  52  43  48  251
                 jHChe  59  37  80  27  39  242
                 AOQFG  32  50  95   1  52  230
                 oDmky  82  65  31  31   2  211
                 XGzWk  34  32  67  48  23  204
                 qdTeX  51  56  56   3  13  179
                 PAwgj  85  24  16   8  22  155
                 QkpKK  25  54  29  10   8  126
        '''
        df5.sort_values(by=['총점'], ascending=False, inplace=True)
        ic('Q5-8')
        ic(df5)
        '''  
        Q6 주어진 값으로 DataFrame 객체 생성
        6-1 객체내부 정보를 출력
        ic| df6:   animal  age  visits priority
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  2.0       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        ic| df6.describe():             age     visits
                            count  8.000000  10.000000
                            mean   3.437500   1.900000
                            std    2.007797   0.875595
                            min    0.500000   1.000000
                            25%    2.375000   1.000000
                            50%    3.000000   2.000000
                            75%    4.625000   2.750000
                            max    7.000000   3.000000
        '''
        data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                'visits': [1,3,2,3,2,3,1,1,2,1],
                'priority': ['yes','yes','no','yes','no','no','no','yes','no','no']}
        labels = ['a','b','c','d','e','f','g','h','i','j']
        df6 = pd.DataFrame(data, index=labels)
        ic('Q6-1')
        ic(df6)
        '''  
        6-2 객체 상위 3열까지 출력
        ic| df6.iloc[:3]:   animal  age  visits priority
                          a    cat  2.5       1      yes
                          b    cat  3.0       3      yes
                          c  snake  0.5       2       no
        '''
        ic('Q6-2')
        ic(df6[:3])
        '''  
        6-3 animal과 age 컬럼만 출력
        ic| df6.loc[:, ['animal', 'age']]:   animal  age
                                           a    cat  2.5
                                           b    cat  3.0
                                           c  snake  0.5
                                           d    dog  NaN
                                           e    dog  5.0
                                           f    cat  2.0
                                           g  snake  4.5
                                           h    cat  NaN
                                           i    dog  7.0
                                           j    dog  3.0
        '''
        ic('Q6-3')
        ic(df6.loc[:, ['animal', 'age']])
        '''                                                            
        6-4 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력
        ic| df6.loc[df6.index[[3,4,8]], ['animal','age']]:   animal  age
                                                           d    dog  NaN
                                                           e    dog  5.0
                                                           i    dog  7.0
        '''
        ic('Q6-4')
        ic(df6.loc[df6.index[[3,4,8]], ['animal', 'age']])
        ''' 
        6-5 visit 컬럼에서 3 초과하는 값 출력
        ic| df6[df6['visits']>2]:   animal  age  visits priority
                                  b    cat  3.0       3      yes
                                  d    dog  NaN       3      yes
                                  f    cat  2.0       3       no
        '''
        ic('Q6-5')

        ''' 
        6-6 age 에서 NaN 값 출력
        ic| df6[df6['age'].isnull()]:   animal  age  visits priority
                                      d    dog  NaN       3      yes
                                      h    cat  NaN       1      yes
        '''
        ic('Q6-6')
        '''         
        6-7 age가 3살 미만 고양이값 출력
        ic| df6[(df6['age'] <3) & (df6['animal'] =='cat')]:   animal  age  visits priority
                                                            a    cat  2.5       1      yes
                                                            f    cat  2.0       3       no
        '''
        ic('Q6-7')
        '''        
        6-8 age가 2살이상 4살 미만인 값 출력
        ic| df6[df6['age'].between(2,4)]:   animal  age  visits priority
                                          a    cat  2.5       1      yes
                                          b    cat  3.0       3      yes
                                          f    cat  2.0       3       no
                                          j    dog  3.0       1       no
        '''
        ic('Q6-8')
        '''                    
        6-9 f 행의 나이를 1.5살로 변경
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  1.5       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        '''
        ic('Q6-9')
        ''' 
        6-10 객체에서 visit 의 합 출력
        ic| df6['visits'].sum(): 19
        '''
        ic('Q6-10')
        ''' 
        6-11 동물별로 나이의 평균 출력
        ic| df6.groupby('animal')['age'].mean(): animal
                                                 cat      2.333333
                                                 dog      5.000000
                                                 snake    2.500000
                                                 Name: age, dtype: float64
        '''
        ic('Q6-11')
        '''        
        6-12 k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  1.5       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
                 k    dog  5.5       2       no
        '''
        ic('Q6-12')
        '''         
        6-13 방금 추가한 열 삭제
        ic| df6:   animal  age  visits priority
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  2.0       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        '''
        ic('Q6-13')
        '''  
        6-14 객체에 있는 동물의 종류의 수 출력
        ic| df6['animal'].value_counts(): dog      4
                                          cat      4
                                          snake    2
                                          Name: animal, dtype: int64
        '''
        ic('Q6-14')
        '''                
        6-15 age 는 내림차순, visits 는 오름차순으로 정렬
        ic| df6.sort_values(by=['age','visits'], ascending=[False, True]):   animal  age  visits priority
                                                                           i    dog  7.0       2       no
                                                                           e    dog  5.0       2       no
                                                                           g  snake  4.5       1       no
                                                                           j    dog  3.0       1       no
                                                                           b    cat  3.0       3      yes
                                                                           a    cat  2.5       1      yes
                                                                           f    cat  2.0       3       no
                                                                           c  snake  0.5       2       no
                                                                           h    cat  NaN       1      yes
                                                                           d    dog  NaN       3      yes
        '''
        ic('Q6-15')
        '''  
        6-16 priority 의 yes를 True, no 를 False  로 맵핑 후 출력
        ic| df6:   animal  age  visits  priority
                 a    cat  2.5       1      True
                 b    cat  3.0       3      True
                 c  snake  0.5       2     False
                 d    dog  NaN       3      True
                 e    dog  5.0       2     False
                 f    cat  2.0       3     False
                 g  snake  4.5       1     False
                 h    cat  NaN       1      True
                 i    dog  7.0       2     False
                 j    dog  3.0       1     False
        '''
        ic('Q6-16')
        '''                
        6-17 snake 를 python 으로 값을 변경
        ic| df6:    animal  age  visits  priority
                 a     cat  2.5       1      True
                 b     cat  3.0       3      True
                 c  python  0.5       2     False
                 d     dog  NaN       3      True
                 e     dog  5.0       2     False
                 f     cat  2.0       3     False
                 g  python  4.5       1     False
                 h     cat  NaN       1      True
                 i     dog  7.0       2     False
                 j     dog  3.0       1     False
        '''
        ic('Q6-17')
        '''                  
        6-18 각각의 동물 유형과 방문 횟수에 대해, 평균나이 출력,
        즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령
        (힌트, 피벗 테이블을 활용해야 함)
        ic| df6: visits    1    2    3
                 animal
                 cat     2.5  NaN  2.5
                 dog     3.0  6.0  NaN
                 python  4.5  0.5  NaN
        '''
        ic('Q6-18')
        '''    
        Q7. 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출력
        ic| type(df7['A']): <class 'pandas.core.series.Series'>
          ic| df7:    A
                   0  1
                   1  2
                   3  3
                   4  4
                   5  5
                   8  6
                   9  7
        '''

        '''    
        Q8. 행의 각 요소에서 행의 평균을 뺀 값을 출력하되 부분집합으로 가로출력
        ic| df8:           0         1         2
                 0 -0.095803 -0.151800  0.247603
                 1 -0.254548  0.229442  0.025106
                 2 -0.134566  0.409687 -0.275121
                 3  0.340665  0.224261 -0.564927
                 4  0.059283  0.010734 -0.070017
        '''

        '''                
        Q9. 가장 작은 합계를 가진 숫자열의 열을 출력(최대값은 max)
        ic| df9.sum().idxmax(): 'b'
        '''

        '''    
        Q10. 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)
        ic| df10:    0  1  2
                  0  1  0  0
                  1  1  1  1
                  2  1  0  1
                  3  0  1  1
                  4  1  0  0
                  5  1  1  1
                  6  0  1  1
                  7  0  0  1
                  8  0  1  0
                  9  0  1  1
        ic| len(df10) - df10.duplicated(keep=False).sum():
            3
        ic| df10.drop_duplicates(keep=False):
                     0  1  2
                  2  1  0  1
                  7  0  0  1
                  8  0  1  0
        '''

        '''  
        Q11. 체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다.
        nan = np.nan
        data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
                [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
                [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
                [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
                [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
        columns = list('abcdefghij')
          ic| type(df11.isnull()): <class 'pandas.core.frame.DataFrame'>
          ic| df11: 0    e
                   1    c
                   2    d
                   3    h
                   4    d
                  dtype: object
        '''


        '''  
        Q12. grps 에서 a, b, c 별로 가장 큰 값
            df12 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                           'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
          ic| type(df12.groupby('grps')): <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
          ic| type(df12.groupby('grps')['vals']): <class 'pandas.core.groupby.generic.SeriesGroupBy'>
          ic| df12: grps
                  a    345
                  b     57
                  c    235
                  Name: vals, dtype: int64
        '''


        '''  
        Q13. 다음 DF13 객체를 list 로 변환
        df13 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        ic| type(ls): <class 'list'>
        ic| df13.values.tolist(): [[1, 4], [2, 5], [3, 6]]
        '''


        '''  
        Q14. 아래 결과로 출력되는 DF 객체 전환 코드작성
        ic| df14.to_dict(): {'A': {0: 1, 1: 2, 2: 3}, 'B': {0: 4, 1: 5, 2: 6}}
        '''


if __name__ == '__main__':
    MyPandas()