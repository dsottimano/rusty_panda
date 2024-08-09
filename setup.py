from setuptools import setup, find_packages
from setuptools_rust import RustExtension, Binding

setup(
    name="rust_resample",
    version="0.1.0",
    rust_extensions=[RustExtension("rust_resample.rust_resample", "Cargo.toml", binding=Binding.PyO3)],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)