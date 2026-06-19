import pandas as pd
data = pd.read_csv('Topic3_healthcare_analytics_dataset.csv')

print(data["Age"][1])

# Prints rows, columns, column types, missinh values
"""
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
	print_summary(data)

	print("Loaded dataset from: Topic3_healthcare_analytics_dataset.csv")


def main() -> None:
	prepare_data()


if __name__ == "__main__":
	main()
"""
