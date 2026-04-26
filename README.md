# bigcalc

**bigcalc** is an advanced mathematical Python library built without any external dependencies. It provides accurate implementations of trigonometric functions, matrix operations, and unit conversions — all computed from scratch using mathematical series and algorithms.

[![PyPI version](https://img.shields.io/pypi/v/bigcalc)](https://pypi.org/project/bigcalc/)
[![Python](https://img.shields.io/pypi/pyversions/bigcalc)](https://pypi.org/project/bigcalc/)
[![License: MIT](https://img.shields.io/pypi/l/bigcalc)](https://pypi.org/project/bigcalc/)

---

## Features

- **Trigonometry** — sin, cos, tan, cot, sec, csc and all inverse functions, computed via Taylor series with configurable accuracy
- **Matrix Operations** — addition, subtraction, multiplication, transpose, determinant, inverse, power, trace, and more
- **Unit Conversion** — 13 categories including length, weight, temperature, time, area, volume, speed, pressure, energy, power, storage, angle, and frequency
- **Zero dependencies** — pure Python, no NumPy or external packages required
- **Structured error handling** — every function returns a descriptive error dict on invalid input instead of raising exceptions

---

## Installation

```bash
pip install bigcalc
```

---

## Quick Start

```python
from bigcalc import trig, mat, convert

# Trigonometry
print(trig.sin(30))           # sin(30°) → ~0.5
print(trig.cos(0))            # cos(0°)  → 1.0
print(trig.arctan(1))         # arctan(1) in radians → ~0.785

# Matrix operations
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(mat.add(A, B))          # [[6, 8], [10, 12]]
print(mat.determinant(A))     # -2
print(mat.inverse(A))         # [[-2.0, 1.0], [1.5, -0.5]]

# Unit conversion
print(convert.length(1, "mile", "km"))        # 1.60934
print(convert.temperature(100, "C", "F"))     # 212.0
print(convert.storage(1, "GB", "MB"))         # 1024.0
```

---

## Modules

### `bigcalc.trig` — Trigonometry

All functions accept angles in degrees (`"deg"`) or radians (`"rad"`). The `accuracy` parameter controls Taylor series terms (default: `10`).

| Function | Description |
|---|---|
| `sin(angle, unit, accuracy)` | Sine |
| `cos(angle, unit, accuracy)` | Cosine |
| `tan(angle, unit, accuracy)` | Tangent |
| `cot(angle, unit, accuracy)` | Cotangent |
| `sec(angle, unit, accuracy)` | Secant |
| `csc(angle, unit, accuracy)` | Cosecant |
| `arcsin(x, accuracy)` | Inverse sine, input ∈ [-1, 1] |
| `arccos(x, accuracy)` | Inverse cosine, input ∈ [-1, 1] |
| `arctan(x, accuracy)` | Inverse tangent |
| `arccot(x, accuracy)` | Inverse cotangent, x ≠ 0 |
| `arcsec(x, accuracy)` | Inverse secant, \|x\| ≥ 1 |
| `arccsc(x, accuracy)` | Inverse cosecant, \|x\| ≥ 1 |

---

### `bigcalc.mat` — Matrix Operations

Matrices are represented as lists of lists, e.g. `[[1, 2], [3, 4]]`.

| Function | Description |
|---|---|
| `add(a, b)` | Element-wise addition |
| `sub(a, b)` | Element-wise subtraction |
| `multiply(a, b)` | Matrix multiplication |
| `scalar_multiply(a, k)` | Multiply all elements by scalar `k` |
| `divide(a, k)` | Divide all elements by scalar `k` |
| `transpose(a)` | Transpose rows and columns |
| `determinant(a)` | Determinant (square matrices only) |
| `inverse(a)` | Matrix inverse (square, non-singular) |
| `power(a, n)` | Matrix raised to integer power `n` |
| `trace(a)` | Sum of diagonal elements |
| `identity_matrix(n)` | Returns an n×n identity matrix |

---

### `bigcalc.convert` — Unit Conversion

All conversion functions follow the signature: `convert.<category>(value, from_unit, to_unit)`

| Category | Function | Supported Units |
|---|---|---|
| Length | `convert.length()` | `mm`, `cm`, `m`, `km`, `inch`, `ft`, `yard`, `mile` |
| Weight | `convert.weight()` | `mg`, `g`, `kg`, `ton`, `oz`, `lb` |
| Temperature | `convert.temperature()` | `C`, `F`, `K` |
| Time | `convert.time()` | `sec`, `min`, `hour`, `day`, `week`, `month`, `year` |
| Area | `convert.area()` | `mm2`, `cm2`, `m2`, `km2`, `acre`, `hectare` |
| Volume | `convert.volume()` | `mL`, `L`, `m3`, `gallon`, `cup` |
| Speed | `convert.speed()` | `m/s`, `km/h`, `mph` |
| Pressure | `convert.pressure()` | `Pa`, `kPa`, `bar`, `atm` |
| Energy | `convert.energy()` | `J`, `kJ`, `cal`, `kcal` |
| Power | `convert.power()` | `W`, `kW`, `hp` |
| Storage | `convert.storage()` | `bit`, `byte`, `KB`, `MB`, `GB`, `TB` |
| Angle | `convert.angle()` | `deg`, `rad` |
| Frequency | `convert.frequency()` | `Hz`, `kHz`, `MHz`, `GHz` |
| Force | `convert.force()` | `N`, `dyne` |

---

## Error Handling

Instead of raising exceptions, bigcalc returns a structured error dict when inputs are invalid:

```python
result = trig.sin("hello")
# → {"error_code": "TRIG00001", "message": "Input angle must be a number"}

result = convert.length(10, "m", "lightyear")
# → {"error_code": "CONV00003", "message": "To unit is invalid"}

result = mat.inverse([[1, 2], [2, 4]])
# → {"error_code": "MAT00011", "message": "Inverse does not exist (determinant is 0)"}
```

You can check for errors like this:

```python
result = trig.tan(90)
if isinstance(result, dict) and "error_code" in result:
    print("Error:", result["message"])
else:
    print("Result:", result)
```

---

## Requirements

- Python 3.7+
- No external dependencies

---

## Author

**Ashwin Jain** — [ashwinjain825@gmail.com](mailto:ashwinjain825@gmail.com)

---

## Links

- [PyPI](https://pypi.org/project/bigcalc/)
- [Documentation](./DOCUMENTATION.md)