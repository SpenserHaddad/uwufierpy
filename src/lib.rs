use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use uwuifier::uwuify_str_sse;

#[pyfunction]
fn uwufy(s: String) -> PyResult<String> {
    Ok(uwuify_str_sse(&s))
}

#[pymodule]
fn uwupy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(uwufy, m)?)?;
    Ok(())
}