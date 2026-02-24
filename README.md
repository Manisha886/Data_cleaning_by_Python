# Data_cleaning_by_Python
This is my first project python related to data cleaning of dirty dataset
<br>
Result of clean data
<br><ls>
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(cleaned_df['Total Spent'], bins=20, kde=True)
plt.title('Distribution of Total Spent')
plt.xlabel('Total Spent')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
<ls><br>
<img width="859" height="547" alt="image" src="https://github.com/user-attachments/assets/075d16ee-2b84-4b0e-9036-8d3a5bb3f09c" />


