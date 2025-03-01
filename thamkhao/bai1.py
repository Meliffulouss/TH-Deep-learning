import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dữ liệu mới
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack', 'Kelly', 'Liam', 'Mona', 'Nina', 'Oscar'],
    'Age': [25, 30, 35, 28, 22, 45, 34, 31, 27, 29, 33, 40, 26, 32, 36],
    'Salary': [50000, 60000, 70000, 55000, 52000, 80000, 72000, 68000, 61000, 59000, 63000, 77000, 53000, 66000, 75000]
}

# 1. Tạo DataFrame
df = pd.DataFrame(data)

# 2. Hiển thị thông tin về DataFrame
print(df.info())

# 3. Lọc các hàng có 'Age' lớn hơn 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# 4. Tính giá trị trung bình của cột 'Salary'
avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)

# 5. Nhóm dữ liệu theo 'Age' và tính tổng 'Salary'
age_salary_sum = df.groupby('Age')['Salary'].sum()
print(age_salary_sum)

# 6. Sắp xếp DataFrame theo 'Salary' giảm dần
df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)

# 7. Vẽ biểu đồ cột cho 'Age'
df['Age'].value_counts().plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 8. Vẽ biểu đồ đường cho 'Salary'
plt.plot(df['Salary'])
plt.title('Salary Trend')
plt.xlabel('Index')
plt.ylabel('Salary')
plt.show()

# 9. Vẽ biểu đồ tròn cho 'Age'
df['Age'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Age Distribution')
plt.show()

# 10. Vẽ biểu đồ phân tán cho 'Age' và 'Salary'
sns.scatterplot(x=df['Age'], y=df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# 11. Kiểm tra giá trị NaN
print(df.isnull().sum())

# 12. Thay thế 'Age' > 30 bằng giá trị trung bình
df.loc[df['Age'] > 30, 'Age'] = df['Age'].mean()
print(df)

# 13. Chuẩn hóa cột 'Age'
df['Age_normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
print(df)

# 14. Phân loại tuổi thành nhóm
def classify_age(age):
    if age < 25:
        return 'Young'
    elif age < 35:
        return 'Middle-aged'
    else:
        return 'Old'

df['Age_group'] = df['Age'].apply(classify_age)
print(df)

# 15. Tính tỷ lệ phần trăm thay đổi của 'Salary'
df['Salary_pct_change'] = df['Salary'].pct_change() * 100
print(df)

# 16. Loại bỏ các hàng trùng lặp theo 'Name'
df.drop_duplicates(subset=['Name'], keep='first', inplace=True)
print(df)
