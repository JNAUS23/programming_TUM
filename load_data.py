import pandas as pd
data = pd.read_csv('Topic3_healthcare_analytics_dataset.csv')

print(data["Age"][1])

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
