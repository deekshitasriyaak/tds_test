import csv

# Define the target symbols
target_symbols = {'„', 'Š'}
total_sum = 0

# Read data1.csv (CP-1252 encoding)
print("Processing data1.csv (CP-1252):")
with open('data1.csv', 'r', encoding='cp1252') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        if len(row) >= 2:
            symbol, value = row[0], row[1]
            if symbol in target_symbols:
                val = int(value)
                total_sum += val
                print(f"  Found '{symbol}' with value {val}")

# Read data2.csv (UTF-8 encoding)
print("\nProcessing data2.csv (UTF-8):")
with open('data2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        if len(row) >= 2:
            symbol, value = row[0], row[1]
            if symbol in target_symbols:
                val = int(value)
                total_sum += val
                print(f"  Found '{symbol}' with value {val}")

# Read data3.txt (UTF-16 encoding, tab-separated)
print("\nProcessing data3.txt (UTF-16, tab-separated):")
with open('data3.txt', 'r', encoding='utf-16') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)  # Skip header row
    for row in reader:
        if len(row) >= 2:
            symbol, value = row[0], row[1]
            if symbol in target_symbols:
                val = int(value)
                total_sum += val
                print(f"  Found '{symbol}' with value {val}")

print("\n" + "="*50)
print(f"TOTAL SUM: {total_sum}")
print("="*50)