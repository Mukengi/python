import pandas as pd

df = pd.read_excel("Test Files.xlsx")

print(df.head())

def generate_email(row):
    names = row['Student Name'].split()
    first_name = names[0]
    last_name = names[-1]
    email = f"{first_name[0]}{last_name}@gmail.com"
    return email


df['Email Address'] = df.apply(generate_email, axis=1)


print(df[['Student Name', 'Email Address']])