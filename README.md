# rust_resample

`rust_resample` is a Rust package with Python bindings that provides a fast and efficient resampling function similar to pandas' `resample` method.

## Prerequisites

To install and use the `rust_resample` package, you will need to have Rust installed on your system. If you don't have Rust installed, you can install it using `rustup`, the Rust toolchain installer. Run the following command:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Follow the on-screen instructions to complete the installation. After installation, ensure that the `cargo` command is available in your terminal by running:

```sh
cargo --version
```

Additionally, you will need to install `setuptools-rust` which is required to build the Rust extension:

```sh
pip install setuptools-rust
```

## Building and Installing the Package

Create a virtual environment:
   ```sh
   python -m venv rust_resample_env
   ```

Activate the virtual environment:
   
   On Unix or MacOS:
   ```sh
   source rust_resample_env/bin/activate
   ```

Navigate to the root directory of your project (where `setup.py` is located) and run:

```sh
pip install .
```

This command will build the Rust extension and install the `rust_resample` package.

## Usage

Here's an example of how to use the `rust_resample` package (also, just run python example.py):

```python
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
```

## Tests

Run pytest in the directory

