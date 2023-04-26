
import pandas as pd

df = pd.read_csv("mountains.csv")

temperature_labels = ["Super Freezing", "Freezing",  "Cold", "Medium", "Warm"]        
temperature_qcut = pd.qcut(x=df["Temperature"], q=len(temperature_labels), retbins=True,
                            labels=temperature_labels)
temperature_qcut_labels = pd.qcut(x=df["Temperature"], q=len(temperature_labels), 
                                  labels=temperature_labels)

print(temperature_qcut)
print(temperature_qcut_labels.value_counts())