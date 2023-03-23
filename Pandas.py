import pandas as pd

# read a CSV file into Dataframe
data = {'Name': ['John', 'Jane', 'Mike', 'Lisa'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('output.csv', index=False)

# Read CSV file back into a DataFrame
df_new = pd.read_csv('output.csv')

# Display the first few rows of the new DataFrame
print(df_new.head())

# to concatenate to dataframe :

data1 = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Branch': ['CSE', 'ME', 'EC', 'IOT', 'AI']
}

data2 = {
    'Marks': [98, 97, 56, 87, 56],
    'Grade': ['A', 'A', 'C', 'B', 'C']
}

dataframe1 = pd.DataFrame(data1)
dataframe2 = pd.DataFrame(data2)

dataframe1.to_csv('csv_1', index=False)
dataframe2.to_csv('csv_2', index=False)

concatenated_csv = pd.concat([dataframe1, dataframe2])
print()
print(concatenated_csv)