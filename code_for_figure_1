import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('social media use by age.csv')
percentage = df['Percentage'].str.rstrip('%').astype('float')
age_groups = df['Age Group'].tolist()

plt.figure(figsize=(8, 8))
plt.pie(percentage, labels=age_groups, autopct='%1.1f%%', startangle=0)
plt.axis('equal')
plt.title('Social Media Use by Age Group in the US in 2023')
plt.show()
