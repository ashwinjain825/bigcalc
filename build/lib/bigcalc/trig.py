TRIG_ERRORS = {
    "TRIG00001": "Input angle must be a number",
    "TRIG00002": "Unit must be either 'deg' or 'rad'",
    "TRIG00003": "Accuracy must be a positive integer",
    "TRIG00004": "Tangent is undefined for this angle",
    "TRIG00005": "Cotangent is undefined for this angle",
    "TRIG00006": "Secant is undefined for this angle",
    "TRIG00007": "Cosecant is undefined for this angle",
    "TRIG00008": "Input must be in the range [-1, 1]",
    "TRIG00009": "Arccotangent is undefined for zero",
    "TRIG00010": "Input must not be zero",
    "TRIG00011": "Input must be a number"
}

PI = 3.141592653589793


def error(code):
    return {
        "error_code": code,
        "message": TRIG_ERRORS[code]
    }


def validate_angle(angle):
    if not isinstance(angle, (int, float)):
        return False, error("TRIG00001")
    return True, None


def validate_unit(unit):
    if unit not in ["deg", "rad"]:
        return False, error("TRIG00002")
    return True, None


def validate_accuracy(accuracy):
    if not isinstance(accuracy, int) or accuracy <= 0:
        return False, error("TRIG00003")
    return True, None


def validate_number(x):
    if not isinstance(x, (int, float)):
        return False, error("TRIG00011")
    return True, None


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def power(x, n):
    result = 1

    if n < 0:
        n = -n
        for _ in range(n):
            result *= x
        return 1 / result

    for _ in range(n):
        result *= x

    return result


def convert_to_radian(angle, unit):
    if unit == "deg":
        return angle * PI / 180
    return angle


def sin(angle, unit="deg", accuracy=10):
    valid, err = validate_angle(angle)
    if not valid:
        return err

    valid, err = validate_unit(unit)
    if not valid:
        return err

    valid, err = validate_accuracy(accuracy)
    if not valid:
        return err

    x = convert_to_radian(angle, unit)
    result = 0

    for i in range(accuracy):
        term = power(x, 2 * i + 1) / factorial(2 * i + 1)

        if i % 2 == 0:
            result += term
        else:
            result -= term

    return result


def cos(angle, unit="deg", accuracy=10):
    valid, err = validate_angle(angle)
    if not valid:
        return err

    valid, err = validate_unit(unit)
    if not valid:
        return err

    valid, err = validate_accuracy(accuracy)
    if not valid:
        return err

    x = convert_to_radian(angle, unit)
    result = 0

    for i in range(accuracy):
        term = power(x, 2 * i) / factorial(2 * i)

        if i % 2 == 0:
            result += term
        else:
            result -= term

    return result


def tan(angle, unit="deg", accuracy=10):
    sine = sin(angle, unit, accuracy)
    if isinstance(sine, dict):
        return sine

    cosine = cos(angle, unit, accuracy)
    if isinstance(cosine, dict):
        return cosine

    if abs(cosine) < 1e-10:
        return error("TRIG00004")

    return sine / cosine


def cot(angle, unit="deg", accuracy=10):
    sine = sin(angle, unit, accuracy)
    if isinstance(sine, dict):
        return sine

    cosine = cos(angle, unit, accuracy)
    if isinstance(cosine, dict):
        return cosine

    if abs(sine) < 1e-10:
        return error("TRIG00005")

    return cosine / sine


def sec(angle, unit="deg", accuracy=10):
    cosine = cos(angle, unit, accuracy)
    if isinstance(cosine, dict):
        return cosine

    if abs(cosine) < 1e-10:
        return error("TRIG00006")

    return 1 / cosine


def csc(angle, unit="deg", accuracy=10):
    sine = sin(angle, unit, accuracy)
    if isinstance(sine, dict):
        return sine

    if abs(sine) < 1e-10:
        return error("TRIG00007")

    return 1 / sine


def arcsin(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    valid, err = validate_accuracy(accuracy)
    if not valid:
        return err

    if x < -1 or x > 1:
        return error("TRIG00008")

    result = 0

    for n in range(accuracy):
        term = (
            factorial(2 * n)
            / (power(4, n) * power(factorial(n), 2))
        ) * power(x, 2 * n + 1) / (2 * n + 1)

        result += term

    return result


def arccos(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    if x < -1 or x > 1:
        return error("TRIG00008")

    value = arcsin(x, accuracy)
    if isinstance(value, dict):
        return value

    return PI / 2 - value


def arctan(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    valid, err = validate_accuracy(accuracy)
    if not valid:
        return err

    result = 0

    for n in range(accuracy):
        term = power(-1, n) * power(x, 2 * n + 1) / (2 * n + 1)
        result += term

    return result


def arccot(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    if x == 0:
        return error("TRIG00009")

    value = arctan(x, accuracy)
    if isinstance(value, dict):
        return value

    return PI / 2 - value


def arcsec(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    if x == 0:
        return error("TRIG00010")

    if -1 < x < 1:
        return error("TRIG00008")

    return arccos(1 / x, accuracy)


def arccsc(x, accuracy=10):
    valid, err = validate_number(x)
    if not valid:
        return err

    if x == 0:
        return error("TRIG00010")

    if -1 < x < 1:
        return error("TRIG00008")

    return arcsin(1 / x, accuracy)