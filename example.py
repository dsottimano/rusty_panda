import rust_resample

# Example data: a list of tuples with timestamps and values
data = [
    (1609459200000, 1.0), 
    (1609459260000, 2.0), 
    (1609459320000, 3.0),
    (1609459380000, 4.0),
    (1609459440000, 5.0)
]

# Resample the data to 1-minute intervals
result_1min = rust_resample.resample(data, "1min")
print("1-minute resample:", result_1min)

# Resample the data to 5-minute intervals
result_5min = rust_resample.resample(data, "5min")
print("5-minute resample:", result_5min)

# Resample the data to 1-hour intervals
result_1h = rust_resample.resample(data, "1h")
print("1-hour resample:", result_1h)