import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("austin_home_sales.csv")

model = smf.ols(
    "Sale_Price ~ Sq_Footage + Bedrooms + Home_Age_Years + Dist_Downtown_Mi",
    data=df,
).fit()

print(model.summary())

print()
for name, value in model.params.items():
    print(f"{name} coefficient: {round(value)}")

for name, value in model.pvalues.items():
    print(f"{name} p-value: {value:.4f}")

print(f"R-squared: {model.rsquared}")
print(f"Adjusted R-squared: {model.rsquared_adj}")
