import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo DataFrame với dữ liệu đã cho
data = {
    "Name": ["Mr. Harris", "Mrs. Bradley", "Miss. Laina", "Mrs. Heath", "Mr. William",
             "Mr. James", "Mr. Timothy", "Mrs. Oscar", "Mrs. Nicholas", "Miss. Marguerite",
             "Mr. William", "Miss. Hulda", "Mr. Lawrence", "Mr. Wilam"],
    "Height": [1.80, 1.61, 1.78, 1.74, 1.55, 1.9, 1.61, 1.40, 1.92, 1.77, 1.55, 1.85, 1.64, 1.77],
    "Weight": [90, 87, 64, 70, 100, 106, 82, 55, 77, 60, 100, 109, 80, 66],
    "AGE": [32, 45, 22, 52, 48, 21, 28, 69, 58, 21, 48, 33, 25, 70]
}

df = pd.DataFrame(data)

# 2. Hiển thị thông tin của DataFrame
print(df.info())

# 3. Tính giá trị trung bình của cột AGE
print("Mean AGE:", df["AGE"].mean())

# 4. Nhóm dữ liệu theo cột Height và tính trung bình cột Weight
print(df.groupby("Height")["Weight"].mean())

# 5. Sắp xếp DataFrame theo cột Weight tăng dần
df = df.sort_values(by="Weight")
print(df)

# 6. Vẽ biểu đồ cột cho AGE
df["AGE"].plot(kind="bar")
plt.show()

# 7. Vẽ biểu đồ phân tán cho AGE và Height
plt.scatter(df["AGE"], df["Height"])
plt.xlabel("AGE")
plt.ylabel("Height")
plt.show()

# 8. Vẽ biểu đồ đường cho Weight
df["Weight"].plot(kind="line")
plt.show()

# 9. Vẽ biểu đồ tròn cho Height
df["Height"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.show()

# 10. Vẽ biểu đồ phân tán cho Weight và AGE
plt.scatter(df["Weight"], df["AGE"])
plt.xlabel("Weight")
plt.ylabel("AGE")
plt.show()

# 11. Kiểm tra giá trị NaN trong DataFrame
print(df.isna().sum())

# 12. Loại bỏ các hàng trùng lặp dựa trên cột Name
df = df.drop_duplicates(subset=["Name"], keep="first")

# 13. Thay thế các giá trị của cột AGE lớn hơn 40 bằng giá trị trung bình của cột đó
mean_age = df["AGE"].mean()
df.loc[df["AGE"] > 40, "AGE"] = mean_age

# 14. Tính chỉ số BMI và thêm vào cột cs_BMI
df["cs_BMI"] = df["Weight"] / (df["Height"] ** 2)

# 15. Tạo cột Phan_Loai dựa trên giá trị BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return 0  # Thiếu cân
    elif 18.5 <= bmi < 23:
        return 1  # Bình thường
    elif 23 <= bmi < 25:
        return 2  # Thừa cân
    else:
        return 3  # Béo phì

df["Phan_Loai"] = df["cs_BMI"].apply(classify_bmi)

# 16. Chuẩn hóa giá trị của cột cs_BMI về khoảng 0 - 1
df["cs_BMI"] = (df["cs_BMI"] - df["cs_BMI"].min()) / (df["cs_BMI"].max() - df["cs_BMI"].min())

# 17. Xác định giới tính và làm sạch cột Name
df["GT"] = df["Name"].apply(lambda x: "male" if "Mr." in x else "female")
df["Name"] = df["Name"].str.replace("Mr. |Mrs. |Miss. ", "", regex=True)

# 18. Vẽ biểu đồ tròn cho giới tính (GT)
df["GT"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.show()

# 19. Trực quan hóa dữ liệu người nữ trên Phan_Loai
df[df["GT"] == "female"]["Phan_Loai"].value_counts().plot(kind="bar")
plt.show()

# 20. Lưu DataFrame vào file CSV
df.to_csv("BKT_MSSV_Hoten.csv", index=False)
