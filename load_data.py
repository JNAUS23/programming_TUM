import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # usually the default
data = pd.read_csv('Topic3_healthcare_analytics_dataset.csv')

'''
#print dtype for each column
for column in data.columns:
    print(f"{column}: {type(data[column][1])}")
'''
def visualize_data(data):
    def plot_distribution(distribution, title):
        y = [element for element in distribution.values()]
        #x = [i for i in range(len(y))]
        x = [element for element in distribution.keys()]
        plt.figure(figsize=(8, 8))
        plt.title(title)
        plt.stem(x, y)
        plt.show()

    ignore_col = ["case_id", "patientid", "Admission_Deposit"]
    for column in data.columns:
        if column in ignore_col:
            continue
        ranges = data[column].value_counts()  # returns a pandas series
        counts_dict = {str(k): v for k, v in ranges.to_dict().items()}
        counts_dict = dict(sorted(counts_dict.items()))
        plot_distribution(counts_dict, column)

visualize_data(data)

for column in data.columns:
    if isinstance(data[column][1], float) or isinstance(data[column][1], int):
        # get min, max, avg, median
        max = data[column].max()
        min = data[column].min()
        mean = data[column].mean()
        std = data[column].std()
        print(f"{column} | min:{min} , max:{max} , mean:{mean:.2f} , std:{std:.2f}")

'''
To Do:
- for stay & Age map group to number such that it can be used instead of a string
- map the graphs to each other: does available bed influence the stay etc
- what is a hospital type code for example
'''



# Prints rows, columns, column types, missinh values.
# Basic stats ( print_data_quality function): Rows with at least one missing value, missing values by column
"""
def print_data_quality(frame: pd.DataFrame) -> None:
	total_rows = len(frame)
	duplicate_rows = frame.duplicated().sum()
	rows_with_missing = frame.isna().any(axis=1).sum()
	missing_counts = frame.isna().sum()
	missing_percent = (missing_counts / total_rows * 100).round(2)

	print("Duplicate rows-", duplicate_rows)
	print(f"Rows with at least one missing value- {rows_with_missing} ({(rows_with_missing / total_rows * 100):.2f}%)")
	print()
	print("Missing values by column:")
	for column in frame.columns:
		if missing_counts[column] > 0:
			print(f"{column}: {missing_counts[column]} missing ({missing_percent[column]:.2f}%)")


def print_summary(frame: pd.DataFrame) -> None:
	print(f"Rows: {len(frame)}")
	print(f"Columns: {len(frame.columns)}")
	print()
	print("Column types:")
	print(frame.dtypes.astype(str).to_string())
	print()
	print("Missing values:")
	print(frame.isna().sum().to_string())


def prepare_data() -> None:
	data = pd.read_csv("Topic3_healthcare_analytics_dataset.csv")
	print_data_quality(data)
	print()
	print_summary(data)


def main() -> None:
	prepare_data()


if __name__ == "__main__":
	main()
"""
