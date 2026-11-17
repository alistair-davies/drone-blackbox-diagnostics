import pandas as pd

print("Loading CSV...")
df = pd.read_csv("btfl_012.bbl.csv", skiprows=150)
print("CSV loaded")

# ------------------------
# Motor output statistics
# ------------------------

motor_cols = [
    "motor[0]",
    "motor[1]",
    "motor[2]",
    "motor[3]"
]

print("\nMotor Means")
print(df[motor_cols].mean())

print("\nMotor Medians")
print(df[motor_cols].median())

# ------------------------
# eRPM statistics
# ------------------------

erpm_cols = [
    "eRPM[0]",
    "eRPM[1]",
    "eRPM[2]",
    "eRPM[3]"
]

print("\neRPM Statistics")
print(df[erpm_cols].describe())

# ------------------------
# Motor correlation analysis
# ------------------------

print("\neRPM Correlation Matrix")
print(df[erpm_cols].corr())