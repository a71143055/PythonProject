import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

d = pd.DataFrame({
    'date' : ['2019-01-03', '2021-11-22', '2023-01-05'],
    'name' : ['J','Y','O'],
    'value' : ['123','456','789']
})

t1 = pd.to_datetime(d.date, format='%Y-%m-%d')
t2 = pd.to_numeric(d.value)
print(t1)
print(t2)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.fillna(0)
print(df)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.fillna(df.mean())
print(df)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df['location'] = ['서울','서울','경기','인천','강원','경기','서울','경기']
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df3 = df['location'].fillna(df['location'].mode()[0])
print(df3)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.dropna()
print(df)

a = ['A','B','A','C','C','A','B','A','D','D','A','D']
a = pd.Series(a)
a_dict = {'A':1,'B':2,'C':3,'D':4}
b = a.map(a_dict)
p = pd.DataFrame({'변환 전' : a, '변환 후' : b})
print(p)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = 1
df.loc[3,'C2'] = -10

plt.boxplot([df['C1'],df['C3']])
plt.show()

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = 1
df.loc[3,'C2'] = -10

sns.heatmap(df.corr(), annot=True)
plt.show()

pd.set_option('display.max_columns', None)
df = pd.read_csv('./data/medical.csv')
print(df.head())

print(df.columns)

df.rename(columns={'Hipertension':'Hypertension','Handcap':'Handicap'},inplace=True)
print(df.columns)

print(df.info())

print(df.isnull().any(axis=1))
print(df.isnull().any(axis=0))

print(df.describe())

df = df[df.Age >= 0]
print(df.Age.min())

df = df[(df.Handicap==0) | (df.Handicap==1)]
print(df['Handicap'].value_counts())

df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
print(df.info())

df['waiting_day'] = df['AppointmentDay'].dt.dayofyear - df['ScheduledDay'].dt.dayofyear
print(df.info())
print(df.describe())

df = df[df.waiting_day>=0]
print(df['waiting_day'].min())

print(df.Age.unique())

df = df[df.Age <= 110]
plt.figure(figsize=(16,2))
sns.boxplot(x=df.Age)
plt.show()

a = df[df.waiting_day==0]['waiting_day'].value_counts()
b = df[(df['waiting_day']==0) & (df['No-show']==1)]['waiting_day'].value_counts()
print(b/a)

no_show = df[df['No-show']==1]
show = df[df['No-show']==0]

no_show[no_show['waiting_day']<=10]['waiting_day'].hist(alpha=0.7, label='no_show')
show[show['waiting_day']<=10]['waiting_day'].hist(alpha=0.3, label='show')
plt.legend()
plt.show()

no_show['ScheduledDay'].hist(alpha=0.7, label='no_show')
show['ScheduledDay'].hist(alpha=0.3, label='show')
plt.legend()
plt.show()

no_show['AppointmentDay'].hist(alpha=0.7, label='no_show')
show['AppointmentDay'].hist(alpha=0.3, label='show')
plt.legend()
plt.show()

print(df.PatientId.value_counts().iloc[0:10])

data = df[(df['waiting_day']>=50) & (df['No-show']==1)].PatientId.value_counts().iloc[0:10]
print(data)

sns.barplot(y='waiting_day',x='SMS_received',hue='No-show', data = df)
plt.show()

# tmp = df[['waiting_day','SMS_received','No-show']].corr()
# sns.heatmap(tmp, annot=True)
# plt.show()

sns.countplot(x='No-show', data=df)
plt.show()

sns.countplot(x='Gender', hue='No-show', data=df)
plt.show()

F = df[(df['Gender']=='F') & (df['No-show']==1)]['Gender'].value_counts()
M = df[(df['Gender']=='M') & (df['No-show']==1)]['Gender'].value_counts()
total_F = df[df['Gender']=='F']['Gender'].value_counts()
total_M = df[df['Gender']=='M']['Gender'].value_counts()

print(F/total_F)
print(M/total_M)

sns.countplot(x='Scholarship', hue='No-show', data=df)
plt.show()

sns.countplot(x='Alcoholism', hue='No-show', data=df)
plt.show()