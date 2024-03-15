import matplotlib.pyplot as plt
import pandas as pd

media_df = pd.read_csv('statistic.csv')

media_df.columns = media_df.columns.str.strip()

print(media_df.columns)


media_df['Year'] = media_df['Year'].astype(str).str.replace('-', '').astype(int)

plt.plot(media_df['Year'], 
         media_df.iloc[:, 1]) 
plt.xlabel('Year')
plt.ylabel('Number of social media users in the US (millions)')
plt.title('Social Media User Growth Over the Years')
plt.grid(True)
plt.xticks(media_df['Year']) 
plt.show()

