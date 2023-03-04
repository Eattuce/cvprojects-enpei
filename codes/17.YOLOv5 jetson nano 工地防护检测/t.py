import pandas as pd

# initialize a dataframe
df = pd.DataFrame(
    [[1, 2, 3],
     [1, 5, 6],
     # [7, 8, 9],
     # [10, 11, 12]
     ],
    columns=['John', 'May', 'Jane'],
    index=['Head', 'Body'])

# convert dataframe to numpy array
arr = df.to_numpy()

print(df)
print('--------------')

print(df[df['John'] == 1].to_numpy())

# print('\nNumpy Array\n----------\n', arr)
# print(type(arr))
