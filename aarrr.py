import pandas as pd
import revenue
import refer
import time

columns = ['user_id', 'item_id', 'category_id', 'behavior', 'timestamps']
df = pd.read_csv('/Users/llx/project/aarrr/UserBehavior.csv', nrows=100000, names = columns)
df.to_csv('/Users/llx/project/aarrr/UserBehavior2.csv', index=False)
df=pd.read_csv('/Users/llx/project/aarrr/UserBehavior2.csv')
df.head()

df['dt'] = df.timestamps.apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x)))
df['dt2'] = pd.to_datetime(df['timestamps'], unit='s')
df.to_csv('/Users/llx/project/aarrr/UserBehavior4.csv', index=False)

print(df['dt'].max())
print(df['dt'].min())

df1 = df[(df['dt']>'2017-11-15 00:00:00')&(df['dt']<'2017-12-04 00:00:00')]

print('len(df1): ', len(df1))
df2 = df1.drop_duplicates()
print('len(df2): ', len(df2))

# 没有空值
df2.isnull().sum()

# 每一列的不同元素
df2.nunique()

# 提取时间,只保留日期的年月日
df2['year']  = pd.to_datetime(df2['dt']).dt.year
df2['month'] = pd.to_datetime(df2['dt']).dt.month
df2['day']   = pd.to_datetime(df2['dt']).dt.day
df2['dates'] = pd.to_datetime(df2[['year', 'month', 'day']])

# 排除同一天用户多次登录的情况
df3 = df2.drop_duplicates(subset = ['user_id', 'dates'])

# 找到每个用户第一天登陆的日期
min_date = df2.groupby('user_id', as_index = False)['dates'].min()

df4 = df3[['user_id', 'dates']]

# min_date与df4两个表进行拼接
min_date.rename(columns = {'dates':'创角日期'}, inplace = True)
df5 = pd.merge(df4, min_date)

df5['天数'] = df5['dates'] - df5['创角日期']

# 使用透视表，计算创角日期对应用户第x天登陆的数量（非重复计数）
data = pd.pivot_table(df5, values = 'user_id', index = '创角日期', columns = '天数',
                        aggfunc = lambda x:len(x.unique()), fill_value = '').reset_index()

# 转为数字格式
data = data.applymap(lambda x:pd.to_numeric(x, errors='ignore'))

# 留存率计算
# 用 1days 列 / 0days 为次日留存率，以此类推
# 我们用for循环语句可以实现该算法
create_index = data.columns
df5 = data.iloc[:, [0, 1]]
for i in range(2, 9): #只计算到7日留存率
    s = data[create_index[i]] / data[create_index[1]]
    df5 = pd.concat([df5, s], axis = 1)

df5.columns = ['创角日期', '注册数量', '次日留存率', '2日留存率', '3日留存率', '4日留存率', '5日留存率', '6日留存率', '7日留存率']
df5.to_csv('/Users/llx/project/aarrr/UserBehavior3.csv', index=False)




