import pandas as pd

df = pd.DataFrame({
    "Name": ["Allen, Mr. William Henry", "Allen, Mr. William Henry", "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]}
)
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(df)
df.plot.line()


print("=======iterrows========")
for index, r in df.iterrows():
    # r is <class 'pandas.core.series.Series'>
    print(type(r), r["Name"], isinstance(r, dict))

print("----items-- 按照列遍历--")
for index, r in df.items():
    # r is  <class 'pandas.core.series.Series'>
    print(type(index), type(r), index, r)

print("========grouby ===========")

d = df.groupby(["Name", "Sex"])["Age"].count()
print(type(d))  # <class 'pandas.core.series.Series'>
print(d)
print(d.to_dict())
print("---row---")
for index, r in d.items():
    print(type(index), type(r), index, r)  # r is int

print("=======groupBy agg======")

d = df.groupby("Name").agg(MyAge=("Age", "count"), SumAge=("Age", "sum"))
print(type(d))
print(d)

print("----iterrows---")
for index, r in d.iterrows():
    # r is <class 'pandas.core.series.Series'>
    print(type(index), type(r), index, r, r.to_dict(), r.MyAge)

print("----itertuples")
for r in d.itertuples():
    print(type(r), r, r.MyAge)  # r is <class 'pandas.core.frame.Pandas'>

print("----iteritems---")
for index, r in d.iteritems():
    # r is <class 'pandas.core.series.Series'>
    print(type(index), type(r), index, r)

print("----items----")
for index, r in d.items():
    # r is <class 'pandas.core.series.Series'>
    print(type(index), type(r), index, r)

print("----iterrows 2---")
for index, r in d.iterrows():
    print(type(index), type(r), index, r)
