use pyo3::prelude::*;
use serde::{Serialize, Deserialize};

#[pyclass]
#[derive(Default, Debug, Serialize, Deserialize, Clone)]
struct ClassA {
    #[pyo3(get,set)]
    x : usize,
}

#[pymethods]
impl ClassA {
    #[new]
    fn new() -> Self {
        ClassA::default()
    }
}

#[pyclass]
#[derive(Default, Debug, Serialize, Deserialize)]
struct ClassB {
    #[pyo3(get,set)]
    a : ClassA,
}

#[pymethods]
impl ClassB {
    #[new]
    fn new() -> Self {
        ClassB { a : ClassA::default() }
    }

    fn workaround(&mut self, x : usize) {
        self.a.x = x;
    }
}


/* this works but cannot derive Serialize/Deserialize traits */
#[pyclass]
#[derive(Debug, Clone)]
struct ClassB2 {
    #[pyo3(get,set)]
    a : Py<ClassA>,
}

#[pymethods]
impl ClassB2 {
    #[new]
    fn new(py : Python) -> Self {
        ClassB2 { a : Py::new(py, ClassA::default()).unwrap(), }
    }
}

#[pymodule]
/// implement ta in rust
fn libreproducer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<ClassA>()?;
    m.add_class::<ClassB>()?;
    m.add_class::<ClassB2>()?;

    Ok(())
}
