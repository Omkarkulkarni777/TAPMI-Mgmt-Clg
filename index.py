import pandas as pd

# Load the Excel file into a DataFrame
file_path = 'original excel.xlsx'
df = pd.read_excel(file_path)

# Specify the entries to be replaced in the 7th column
entries_to_replace = ["Club 26", "Club 27", "Club 28", "Club 29", "Club 30"]
entries_to_replace1 = ["Club 23", "Club 24", "Club 25"]
entries_to_replace2 = ["Club 21", "Club 22"]

# Replace specified entries with None in the 7th column
df.loc[df['Preference6'].isin(entries_to_replace), 'Preference6'] = None
df.loc[df['Preference6'].isin(entries_to_replace1), 'Preference6'] = None
df.loc[df['Preference6'].isin(entries_to_replace2), 'Preference6'] = None
df.loc[df['Preference5'].isin(entries_to_replace), 'Preference5'] = None
df.loc[df['Preference5'].isin(entries_to_replace1), 'Preference5'] = None
df.loc[df['Preference4'].isin(entries_to_replace2), 'Preference4'] = None

# Save the modified DataFrame back to the Excel file
df.to_excel('mba.xlsx', index=False)
