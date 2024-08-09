import rust_resample

def test_resample_1min():
    data = [
        (1609459200000, 1.0), 
        (1609459260000, 2.0), 
        (1609459320000, 3.0)
    ]
    expected = [
        (1609459200000, 1.0), 
        (1609459260000, 2.0), 
        (1609459320000, 3.0)
    ]
    result = rust_resample.resample(data, "1min")
    assert result == expected

def test_resample_5min():
    data = [
        (1609459200000, 1.0), 
        (1609459260000, 2.0), 
        (1609459320000, 3.0)
    ]
    expected = [
        (1609459200000, 2.0)
    ]
    result = rust_resample.resample(data, "5min")
    assert result == expected

def test_resample_1h():
    data = [
        (1609459200000, 1.0), 
        (1609459260000, 2.0), 
        (1609459320000, 3.0)
    ]
    expected = [
        (1609459200000, 2.0)
    ]
    result = rust_resample.resample(data, "1h")
    assert result == expected