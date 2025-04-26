import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Titanic-Dataset.csv')

print("Summary Statistics:\n", df.describe())

sns.histplot(df['Age'], kde=True)
plt.title('Histogram of Age')
plt.show()

sns.boxplot(x=df['Age'])
plt.title('Boxplot of Age')
plt.show()

sns.pairplot(df.select_dtypes(include=['float64', 'int64']))
plt.title('Pairplot of Features')
plt.show()

corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

skewness = df['Age'].skew()
print(f"Skewness of 'Age': {skewness}")
