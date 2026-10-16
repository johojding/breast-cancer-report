from sklearn.datasets import load_breast_cancer
from biomedical_quality import quality_report

dataset = load_breast_cancer(as_frame=True)

df = dataset.data
target = dataset.target

print("Dataset shape:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn data types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

print("\nTarget names:")
print(dataset.target_names)

print("\nFirst five targets:")
print(target.head())

print("\nTarget class counts:")
print(target.value_counts())

print("\nDataset description:")
print(dataset.DESCR[:3000])