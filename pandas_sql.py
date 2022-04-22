import pandas as pd
import pandasql as ps

df = pd.DataFrame([[1234, 'Customer A', '123 Street', 'np.nan'],
                   [1234, 'Customer A', 'np.nan', '333 Street'],
                   [1233, 'Customer B', '444 Street', '333 Street'],
                   [1233, 'Customer B', '444 Street', '666 Street']], columns=['ID', 'Customer', 'Billing Address', 'Shipping Address'])

q1 = """SELECT ID FROM df  """

data = ps.sqldf(q1, locals())
print(data)
print(type(data))

q1 = """SELECT Customer , count(1) cnt FROM df group by Customer  """

data = ps.sqldf(q1, globals())
print(data)
print(type(data))

d = data.query(" cnt == 2")
print(d)
print(type(d))


groupData = df.groupby("Customer").agg(cnt=("ID", "count"))

print(groupData)
print(type(groupData))

print(groupData.query("cnt == 2"))

print(groupData.query("Customer == 'Customer A'"))



groupData = df.groupby(["ID","Customer"]).agg(cnt=("ID", "count"))

print(groupData)
print(type(groupData))

print(groupData.query("cnt == 2"))

print(groupData.query("Customer == 'Customer A'"))

# groupData.join


groupData.columns