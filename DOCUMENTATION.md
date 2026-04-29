# bigcalc Documentation

**Version:** 0.1.0  
**Author:** Ashwin Jain  
**PyPI:** https://pypi.org/project/bigcalc/

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Package Structure](#package-structure)
4. [Error Handling](#error-handling)
5. [Module: trig](#module-trig)
6. [Module: mat](#module-mat)
7. [Module: convert](#module-convert)
8. [Error Code Reference](#error-code-reference)

---

## Overview

`bigcalc` is a pure Python mathematical library with zero external dependencies. It implements trigonometric functions via Taylor series expansion, matrix operations via standard linear algebra algorithms, and unit conversions via a base-unit ratio system.

All functions use structured error returns instead of raising exceptions, making them safe to use in pipelines without try/except blocks.

---

## Installation

```bash
pip install bigcalc
```

**Requirements:** Python 3.7 or higher. No dependencies.

---

## Package Structure

```
bigcalc/
├── __init__.py       # Exposes trig, mat, convert
├── trig.py           # Trigonometric functions
├── mat.py            # Matrix operations
└── convert.py        # Unit conversions
```

Import the submodules directly:

```python
from bigcalc import trig, mat, convert
```

---

## Error Handling

Every function in `bigcalc` returns a **plain Python value** on success, or an **error dictionary** on failure. No exceptions are raised for invalid inputs.

### Error Dict Format

```python
{
    "error_code": "TRIG00001",
    "message": "Input angle must be a number"
}
```

### Checking for Errors

```python
result = trig.sin("abc")

if isinstance(result, dict) and "error_code" in result:
    print(f"[{result['error_code']}] {result['message']}")
else:
    print(result)
```

---

## Module: `trig`

```python
from bigcalc import trig
```

Implements trigonometric and inverse trigonometric functions from scratch using Taylor series. No `math` module is used internally.

### Constants

| Name | Value |
|---|---|
| `trig.PI` | `3.141592653589793` |

---

### `trig.sin(angle, unit="deg", accuracy=10)`

Returns the sine of an angle.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `angle` | int / float | required | The input angle |
| `unit` | str | `"deg"` | `"deg"` for degrees, `"rad"` for radians |
| `accuracy` | int | `10` | Number of Taylor series terms (higher = more precise) |

**Returns:** `float` or error dict

**Examples:**
```python
trig.sin(30)              # → 0.49999999...  (~0.5)
trig.sin(90)              # → 1.0
trig.sin(1.5708, "rad")   # → 1.0 (π/2 radians)
trig.sin(30, accuracy=20) # → more precise result
```

---

### `trig.cos(angle, unit="deg", accuracy=10)`

Returns the cosine of an angle.

**Parameters:** Same as `sin`.

**Returns:** `float` or error dict

**Examples:**
```python
trig.cos(0)    # → 1.0
trig.cos(60)   # → ~0.5
trig.cos(180)  # → ~-1.0
```

---

### `trig.tan(angle, unit="deg", accuracy=10)`

Returns the tangent of an angle. Returns an error for angles where cosine ≈ 0 (i.e., 90°, 270°).

**Returns:** `float` or error dict

**Examples:**
```python
trig.tan(45)   # → ~1.0
trig.tan(90)   # → {"error_code": "TRIG00004", "message": "Tangent is undefined for this angle"}
```

---

### `trig.cot(angle, unit="deg", accuracy=10)`

Returns the cotangent (cos/sin). Returns an error where sine ≈ 0 (i.e., 0°, 180°).

**Returns:** `float` or error dict

---

### `trig.sec(angle, unit="deg", accuracy=10)`

Returns the secant (1/cos). Returns an error where cosine ≈ 0.

**Returns:** `float` or error dict

---

### `trig.csc(angle, unit="deg", accuracy=10)`

Returns the cosecant (1/sin). Returns an error where sine ≈ 0.

**Returns:** `float` or error dict

---

### `trig.arcsin(x, accuracy=10)`

Returns the inverse sine in radians. Input must be in [-1, 1].

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `x` | int / float | required | Input value, must be in [-1, 1] |
| `accuracy` | int | `10` | Taylor series terms |

**Returns:** `float` (radians) or error dict

**Examples:**
```python
trig.arcsin(0.5)   # → ~0.5236 (π/6)
trig.arcsin(1)     # → ~1.5708 (π/2)
trig.arcsin(2)     # → {"error_code": "TRIG00008", ...}
```

---

### `trig.arccos(x, accuracy=10)`

Returns the inverse cosine in radians. Input must be in [-1, 1].

**Returns:** `float` (radians) or error dict

**Examples:**
```python
trig.arccos(1)    # → ~0.0
trig.arccos(0)    # → ~1.5708 (π/2)
trig.arccos(0.5)  # → ~1.0472 (π/3)
```

---

### `trig.arctan(x, accuracy=10)`

Returns the inverse tangent in radians.

**Note:** Uses Taylor series which converges slowly for |x| > 1. For high accuracy on large inputs, increase `accuracy`.

**Returns:** `float` (radians) or error dict

**Examples:**
```python
trig.arctan(1)    # → ~0.7854 (π/4)
trig.arctan(0)    # → 0.0
```

---

### `trig.arccot(x, accuracy=10)`

Returns the inverse cotangent in radians. `x` must not be zero.

**Returns:** `float` (radians) or error dict

---

### `trig.arcsec(x, accuracy=10)`

Returns the inverse secant in radians. Requires |x| ≥ 1.

**Returns:** `float` (radians) or error dict

---

### `trig.arccsc(x, accuracy=10)`

Returns the inverse cosecant in radians. Requires |x| ≥ 1.

**Returns:** `float` (radians) or error dict

---

## Module: `mat`

```python
from bigcalc import mat
```

Implements matrix operations on standard Python lists of lists. All matrices are validated on every call.

### Matrix Format

A matrix is a non-empty list of lists where all rows have equal length and all elements are `int` or `float`:

```python
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```

---

### `mat.add(a, b)`

Returns element-wise sum of two matrices. Both matrices must have identical dimensions.

**Returns:** `Matrix` or error dict

```python
mat.add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# → [[6, 8], [10, 12]]
```

---

### `mat.sub(a, b)`

Returns element-wise difference `a - b`. Both matrices must have identical dimensions.

**Returns:** `Matrix` or error dict

```python
mat.sub([[5, 6], [7, 8]], [[1, 2], [3, 4]])
# → [[4, 4], [4, 4]]
```

---

### `mat.multiply(a, b)`

Returns the matrix product of `a` and `b`. Columns of `a` must equal rows of `b`.

**Returns:** `Matrix` or error dict

```python
mat.multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# → [[19, 22], [43, 50]]
```

---

### `mat.scalar_multiply(a, k)`

Multiplies every element in the matrix by scalar `k`.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `a` | Matrix | Input matrix |
| `k` | int / float | Scalar multiplier |

**Returns:** `Matrix` or error dict

```python
mat.scalar_multiply([[1, 2], [3, 4]], 3)
# → [[3, 6], [9, 12]]
```

---

### `mat.divide(a, k)`

Divides every element by scalar `k`. Returns error if `k == 0`.

**Returns:** `Matrix` or error dict

```python
mat.divide([[4, 8], [12, 16]], 4)
# → [[1.0, 2.0], [3.0, 4.0]]
```

---

### `mat.transpose(a)`

Returns the transpose of the matrix (rows become columns).

**Returns:** `Matrix` or error dict

```python
mat.transpose([[1, 2, 3], [4, 5, 6]])
# → [[1, 4], [2, 5], [3, 6]]
```

---

### `mat.determinant(a)`

Returns the determinant of a square matrix. Uses recursive cofactor expansion.

**Returns:** `float` or error dict

```python
mat.determinant([[1, 2], [3, 4]])   # → -2
mat.determinant([[2, 0], [0, 3]])   # → 6
```

---

### `mat.inverse(a)`

Returns the inverse of a square, non-singular matrix. Uses Gauss-Jordan elimination.

Returns an error if the matrix is not square or has determinant 0.

**Returns:** `Matrix` or error dict

```python
mat.inverse([[1, 2], [3, 4]])
# → [[-2.0, 1.0], [1.5, -0.5]]

mat.inverse([[1, 2], [2, 4]])
# → {"error_code": "MAT00011", "message": "Inverse does not exist (determinant is 0)"}
```

---

### `mat.power(a, n)`

Raises a square matrix to a non-negative integer power `n`. `n=0` returns the identity matrix.

**Returns:** `Matrix` or error dict

```python
mat.power([[1, 2], [3, 4]], 2)
# → [[7, 10], [15, 22]]

mat.power([[1, 2], [3, 4]], 0)
# → [[1.0, 0.0], [0.0, 1.0]]  (identity)
```

---

### `mat.trace(a)`

Returns the sum of the diagonal elements of a square matrix.

**Returns:** `float` or error dict

```python
mat.trace([[1, 2], [3, 4]])   # → 5
mat.trace([[5, 0, 0], [0, 3, 0], [0, 0, 2]])  # → 10
```

---

### `mat.identity_matrix(n)`

Returns an `n × n` identity matrix (1s on diagonal, 0s elsewhere).

**Returns:** `Matrix`

```python
mat.identity_matrix(3)
# → [[1.0, 0.0, 0.0],
#    [0.0, 1.0, 0.0],
#    [0.0, 0.0, 1.0]]
```

---

## Module: `convert`

```python
from bigcalc import convert
```

All conversion functions share the same signature:

```python
convert.<category>(value, from_unit, to_unit)
```

All non-temperature conversions use a shared base-unit ratio system internally. Temperature is handled separately with explicit formulas.

---

### `convert.length(value, from_unit, to_unit)`

**Supported units:** `mm`, `cm`, `m`, `km`, `inch`, `ft`, `yard`, `mile`

```python
convert.length(1, "mile", "km")      # → 1.60934
convert.length(100, "cm", "m")       # → 1.0
convert.length(12, "inch", "ft")     # → 1.0
```

---

### `convert.weight(value, from_unit, to_unit)`

**Supported units:** `mg`, `g`, `kg`, `ton`, `oz`, `lb`

```python
convert.weight(1, "kg", "lb")        # → 2.20462...
convert.weight(16, "oz", "lb")       # → 1.0
```

---

### `convert.temperature(value, from_unit, to_unit)`

**Supported units:** `C` (Celsius), `F` (Fahrenheit), `K` (Kelvin)

Unlike other conversions, temperature uses offset formulas rather than ratios.

```python
convert.temperature(0, "C", "F")     # → 32.0
convert.temperature(100, "C", "F")   # → 212.0
convert.temperature(0, "C", "K")     # → 273.15
convert.temperature(98.6, "F", "C")  # → 37.0
```

---

### `convert.time(value, from_unit, to_unit)`

**Supported units:** `sec`, `min`, `hour`, `day`, `week`, `month`, `year`

> **Note:** `month` is approximated as 30 days (2,592,000 seconds). `year` is approximated as 365 days.

```python
convert.time(1, "hour", "min")       # → 60.0
convert.time(1, "day", "sec")        # → 86400.0
convert.time(2, "week", "day")       # → 14.0
```

---

### `convert.area(value, from_unit, to_unit)`

**Supported units:** `mm2`, `cm2`, `m2`, `km2`, `acre`, `hectare`

```python
convert.area(1, "hectare", "acre")   # → 2.47105...
convert.area(1, "km2", "m2")         # → 1000000.0
```

---

### `convert.volume(value, from_unit, to_unit)`

**Supported units:** `mL`, `L`, `m3`, `gallon`, `cup`

```python
convert.volume(1, "L", "mL")         # → 1000.0
convert.volume(1, "gallon", "L")     # → 3.78541
```

---

### `convert.speed(value, from_unit, to_unit)`

**Supported units:** `m/s`, `km/h`, `mph`

```python
convert.speed(1, "m/s", "km/h")      # → 3.6...
convert.speed(60, "mph", "km/h")     # → 96.56...
```

---

### `convert.pressure(value, from_unit, to_unit)`

**Supported units:** `Pa`, `kPa`, `bar`, `atm`

```python
convert.pressure(1, "atm", "Pa")     # → 101325.0
convert.pressure(1, "bar", "atm")    # → 0.98692...
```

---

### `convert.energy(value, from_unit, to_unit)`

**Supported units:** `J`, `kJ`, `cal`, `kcal`

```python
convert.energy(1, "kcal", "J")       # → 4184.0
convert.energy(1, "kJ", "cal")       # → 239.005...
```

---

### `convert.power(value, from_unit, to_unit)`

**Supported units:** `W`, `kW`, `hp`

```python
convert.power(1, "hp", "W")          # → 745.7
convert.power(1000, "W", "kW")       # → 1.0
```

---

### `convert.storage(value, from_unit, to_unit)`

**Supported units:** `bit`, `byte`, `KB`, `MB`, `GB`, `TB`

Uses binary (base-2) prefixes: 1 KB = 1024 bytes.

```python
convert.storage(1, "GB", "MB")       # → 1024.0
convert.storage(1, "TB", "GB")       # → 1024.0
convert.storage(8, "bit", "byte")    # → 1.0
```

---

### `convert.angle(value, from_unit, to_unit)`

**Supported units:** `deg`, `rad`

```python
convert.angle(180, "deg", "rad")     # → 3.14159...
convert.angle(1, "rad", "deg")       # → 57.2958
```

---

### `convert.frequency(value, from_unit, to_unit)`

**Supported units:** `Hz`, `kHz`, `MHz`, `GHz`

```python
convert.frequency(1, "GHz", "MHz")   # → 1000.0
convert.frequency(2400, "MHz", "GHz") # → 2.4
```

---

### `convert.force(value, from_unit, to_unit)`

**Supported units:** `N`, `dyne`

```python
convert.force(1, "N", "dyne")        # → 100000.0
```

### `bigcalc.about` — Get About this Library

This module provides a function to retrieve information about the bigcalc library, including version, author, and description.

| Function | Description |
|---|---|
| `about.name()` | Returns the name of lib |
| `about.version()` | Returns the current version of bigcalc |
| `about.author()` | Returns the author's name and contact information |
| `about.author_email()` | Returns the author's email address |
| `about.description()` | Returns a brief description of bigcalc |
| `about.python_requires()` | Returns the minimum required Python version |

---

## Error Code Reference

### Trig Errors (`trig.py`)

| Code | Message |
|---|---|
| TRIG00001 | Input angle must be a number |
| TRIG00002 | Unit must be either 'deg' or 'rad' |
| TRIG00003 | Accuracy must be a positive integer |
| TRIG00004 | Tangent is undefined for this angle |
| TRIG00005 | Cotangent is undefined for this angle |
| TRIG00006 | Secant is undefined for this angle |
| TRIG00007 | Cosecant is undefined for this angle |
| TRIG00008 | Input must be in the range [-1, 1] |
| TRIG00009 | Arccotangent is undefined for zero |
| TRIG00010 | Input must not be zero |
| TRIG00011 | Input must be a number |

### Matrix Errors (`mat.py`)

| Code | Message |
|---|---|
| MAT00001 | Matrix must be a non-empty list |
| MAT00002 | Matrix must be a 2D list |
| MAT00003 | Matrix rows cannot be empty |
| MAT00004 | All rows must have same number of columns |
| MAT00005 | Matrix elements must be numbers |
| MAT00006 | Addition requires both matrices to have same dimensions |
| MAT00007 | Subtraction requires both matrices to have same dimensions |
| MAT00008 | Multiplication not possible: columns of first matrix must equal rows of second matrix |
| MAT00009 | Trace is only defined for square matrices |
| MAT00010 | Inverse exists only for square matrices |
| MAT00011 | Inverse does not exist (determinant is 0) |
| MAT00012 | Division by zero is not allowed |
| MAT00013 | Determinant is only defined for square matrices |
| MAT00014 | Power must be a non-negative integer |
| MAT00015 | Row index out of range |
| MAT00016 | Column index out of range |
| MAT00017 | Scalar value must be a number |

### Conversion Errors (`convert.py`)

| Code | Message |
|---|---|
| CONV00001 | Input value must be a number |
| CONV00002 | From unit is invalid |
| CONV00003 | To unit is invalid |
| CONV00004 | Unsupported conversion |
| CONV00005 | Temperature unit is invalid |
| CONV00006 | Division by zero is not allowed |