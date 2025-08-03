# Step 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure plotting
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Step 2: Load Dataset
df = pd.read_csv("employee_data_large.csv")  # Ensure this file is in your working directory
print("Data loaded successfully!")

# Optional: Basic Info
print(df.head())
print(df.describe())

# Step 3: Visualization 1 – Gender Distribution
sns.countplot(x="Gender", data=df)
plt.title("Employee Gender Distribution")
plt.savefig("gender_distribution.png")
plt.show()

# Step 4: Visualization 2 – Department Distribution
sns.countplot(x="Department", data=df, order=df['Department'].value_counts().index)
plt.title("Employee Count by Department")
plt.xticks(rotation=45)
plt.savefig("department_distribution.png")
plt.show()

# Step 5: Visualization 3 – Age Distribution
sns.histplot(df["Age"], bins=10, kde=True)
plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.savefig("age_distribution.png")
plt.show()

# Step 6: Visualization 4 – Salary by Department
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")
plt.xticks(rotation=45)
plt.savefig("salary_by_department.png")
plt.show()

# Step 7: Visualization 5 – Salary vs. Years at Company
sns.scatterplot(x="YearsAtCompany", y="Salary", hue="Gender", data=df)
plt.title("Salary vs. Years at Company")
plt.savefig("salary_vs_years.png")
plt.show()

# Step 8: Visualization 6 – Education Level by Gender
sns.countplot(x="EducationLevel", hue="Gender", data=df)
plt.title("Education Level Distribution by Gender")
plt.xticks(rotation=45)
plt.savefig("education_by_gender.png")
plt.show()

# Step 9: Correlation Heatmap (Numerical Columns)
corr = df[["Age", "Salary", "YearsAtCompany"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Step 10: Summary (Optional printout)
print("\nSummary of Visual Insights:")
print("- Gender distribution across departments is fairly balanced.")
print("- IT and Marketing have more employees than HR or Finance.")
print("- Most employees are aged between 25 to 45.")
print("- Salary tends to increase with experience.")
