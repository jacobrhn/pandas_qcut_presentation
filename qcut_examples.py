
import pandas as pd


df = pd.read_csv('mountains.csv')

# (1) Print of DataFrame for context.
print(df)

# (2) This is the collumn we´ll be performing qcut today.
print(df["Height"])






# (3) Function call with the minimum parameters given (note that "labels", "precision", "retbins" and "duplicates" 
# are all set to the standard values and only serve the demonstration.)
hight_qcut_basic = pd.qcut(x=df["Height"], q=5, labels=None, precision=3, retbins=False, duplicates="raise")
print(hight_qcut_basic)




# (4) Now with "precision = 1" and "retbins = True" which will resolve in rounding adjustments for the bins 
# Also the bins (boundaries) now gat returned in an array.
hight_qcut_precision_retbins = pd.qcut(x=df["Height"], q=5, labels=None, precision=2, retbins=True, duplicates="raise")
print(hight_qcut_precision_retbins)




# Example with "labels = False", so that bins are labeld with ints.
hight_qcut_labels_false = pd.qcut(x=df["Height"], q=5, labels=False, precision=2, retbins=True, duplicates="raise")
print(hight_qcut_labels_false)





# (6) Introcucing custom labels in form of an array whichs length corresponds to the number of quantiles.
hight_labels = ["Boring", "Modest", "Medium", "High", "Super High"]
hight_qcut_labels = pd.qcut(x=df["Height"], q=len(hight_labels), labels=hight_labels, precision=2, retbins=False, duplicates="raise")
print(hight_qcut_labels)





# 7 Allows quick overview based on performed cuts.
print(hight_qcut_labels.value_counts())






# (8) Generated labels merged into original DataFrame.
df["Height_qcut"] = hight_qcut_labels












































