use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use pyo3::wrap_pyfunction;
use std::collections::HashMap;
use std::time::Duration;

#[pyfunction]
fn resample(data: Vec<(i64, f64)>, rule: &str) -> PyResult<Vec<(i64, f64)>> {
    let duration = match rule {
        "1min" => Duration::from_secs(60),
        "5min" => Duration::from_secs(300),
        "1h" => Duration::from_secs(3600),
        _ => return Err(PyValueError::new_err("Unsupported rule")),
    };

    let mut resampled: HashMap<i64, (f64, usize)> = HashMap::new();

    for (timestamp, value) in data {
        let bucket = (timestamp / duration.as_millis() as i64) * duration.as_millis() as i64;
        let entry = resampled.entry(bucket).or_insert((0.0, 0));
        entry.0 += value;
        entry.1 += 1;
    }

    let mut result: Vec<(i64, f64)> = resampled
        .into_iter()
        .map(|(bucket, (sum, count))| (bucket, sum / count as f64))
        .collect();

    result.sort_by_key(|k| k.0);

    Ok(result)
}

#[pymodule]
fn rust_resample(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(resample, m)?)?;
    Ok(())
}