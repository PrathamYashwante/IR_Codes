import math
import pandas as pd

# data = {
#     "D0": [2, 0, 3],
#     "D1": [4, 0, 0],
#     "D2": [0, 3, 5],
#     "D3": [5, 0, 0],
#     "D4": [1, 4, 5],
#     "D5": [3, 1, 0],
#     "D6": [0, 0, 4]
# }

data = {
    "D0": [2, 2, 1, 1, 0, 0],
    "D1": [0, 0, 0, 2, 2, 0],
    "D2": [1, 0, 0, 1, 0, 1],
}
df = pd.DataFrame(data)

print(df)

max_list = []

for i in data:
    x = data[i]
    max_element = max(x)
    max_list.append(max_element)

print("Max Freq: ", max_list)


count = []
for j in range(0, 6):
    c = []
    for i in range(0, 3):
        key = "D" + str(i)
        x = data[key][j]
        c.append(x)
    count.append(c)

print(count)

cc = []

for list in count:
    x = 0
    for el in list:
        if el != 0:
            x = x + 1
    cc.append(x)

print(cc)

print(data)

df['Count'] = cc

print('df after count')
print(df)

query = [1, 0, 0, 0, 1, 0]

updated_query = []

for i in query:
    i = i + 0.5
    updated_query.append(i)

print(updated_query)


df['Query'] = updated_query

print('df after query + 0.5')
print(df)

N = len(data)
print("The no of docs - " , N)



idf = []

for count in cc:
    res = math.log(1 + (N/count), 10)
    res = round(res, 3)
    idf.append(res)

print(idf)

df['idf'] = idf

print('df after idf')
print(df)


## ------------------------------------------------------------
## normalize the values


for i in data:
    print(i)

X = df.drop(columns=['Count', 'Query', 'idf'])


X.loc[len(df.index)] = max_list

print(X)

y = df.iloc[:,3:]

print(y)

updated = []

for i in range(0, 3):
    key = "D" + str(i)
    x = data[key]
    print(x)
    res_list = []
    res_list.append(key)
    for el in x:
        res = el / max_list[i]
        res = round(res, 3)
        res_list.append(res)
    updated.append(res_list)
    res_list = []

print(updated)

new_data = {}

for dat in updated:
    new_data[dat[0]] = dat[1:]

print(new_data)

new_df = pd.DataFrame(new_data)

print(new_df)


combined_df = pd.concat([new_df, y], axis=1)
print(combined_df)



## multiply idf value with documents value
up_lists = []

for i in range(0, 3):
    key = "D" + str(i)
    x = new_df[key]
    print(x)
    ll = []
    for i in range(0, len(x)):
        res = x[i] * idf[i]
        ll.append(res)
    up_lists.append(ll)
    ll = []

print(up_lists)

for i, column in enumerate(new_df):
    new_df[column] = up_lists[i]

print("#############")
print(new_df)


combined_df = pd.concat([new_df, y], axis=1)
print(combined_df)

updated_query_2 = []

for i in range(0, len(updated_query)):
    print(updated_query[i])
    res = updated_query[i] * idf[i]
    updated_query_2.append(res)
    
print(updated_query_2)


combined_df['Query'] = updated_query_2
    
print(combined_df)

documents_df = new_df


for i in range(0, 3):
    key = "D" + str(i)
    documents_df[key] = new_df[key] * combined_df['Query']
    

### now we have original values in new_df and latest values in documents_df


og_docs = combined_df.iloc[:, :3]

print(og_docs)
print(documents_df)

query_col_answer = combined_df['Query'] ** 2

query_col_answer = query_col_answer.sum()

query_col_answer = math.sqrt(query_col_answer)

print(query_col_answer) 

og_docs_answers = []
documents_df_answer = []

for i in range(0, 3):
    key = "D" + str(i)
    res = og_docs[key] ** 2
    res = math.sqrt(res.sum())
    og_docs_answers.append(res)
    
    res1 = documents_df[key]  ** 2
    res1 = math.sqrt(res1.sum())
    documents_df_answer.append(res1)
    
print(og_docs_answers)
print(documents_df_answer)


similarity = []

for i in range(0, len(og_docs_answers)):
    res = (documents_df_answer[i]/(og_docs_answers[i] * query_col_answer))
    similarity.append(res)
    print("The similarity of doc", i, "and query is " , res)

