# Enhance any text with a single function

This is just a Python wrapper around the [uwuify](https://github.com/Daniel-Liu-c0deb0t/uwu/) Rust project.

Exposes a single function, `uwufy`:

```python

from uwufier import uwufy

# Prints "hewwo wowwd!"
print(uwufy("hello world!"))
```

# Building

Requires rust 1.51.0 or nightly. 

```bash
rustup override set nightly
python install -r requirements.txt
python setup.py bdist_wheel
pip install .
```