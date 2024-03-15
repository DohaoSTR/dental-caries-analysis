import pandas as pd

dataset = pd.read_excel('dataset_wo_nulls.xlsx')
print("Исходный набор данных:")
dataset.info()

print("\nНабор данных после удаления повторяющихся строк:")
dataset = dataset.drop_duplicates()

dataset.info()

print()
for column in dataset.columns:
    print(str(column) + ": " + "Мин. значение - " + str(dataset[column].min()) + ". Макс. значение - " + str(dataset[column].max()))

dataset.to_excel('dataset_wo_nulls.xlsx')