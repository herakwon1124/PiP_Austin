import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:.6f}")

df = pd.read_csv("austin_home_sales.csv")

print(df.shape)
print(df.describe())

plt.figure()
plt.scatter(df["Sq_Footage"], df["Sale_Price"])
plt.xlabel("Sq_Footage")
plt.ylabel("Sale_Price")
plt.savefig("scatter.png")
plt.close()
