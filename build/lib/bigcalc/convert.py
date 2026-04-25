CONV_ERRORS = {
    "CONV00001": "Input value must be a number",
    "CONV00002": "From unit is invalid",
    "CONV00003": "To unit is invalid",
    "CONV00004": "Unsupported conversion",
    "CONV00005": "Temperature unit is invalid",
    "CONV00006": "Division by zero is not allowed"
}


def error(code):
    return {
        "error_code": code,
        "message": CONV_ERRORS[code]
    }


def validate_number(value):
    if not isinstance(value, (int, float)):
        return False, error("CONV00001")
    return True, None


def convert_by_base(value, from_unit, to_unit, units):
    valid, err = validate_number(value)
    if not valid:
        return err

    if from_unit not in units:
        return error("CONV00002")

    if to_unit not in units:
        return error("CONV00003")

    base_value = value * units[from_unit]
    result = base_value / units[to_unit]

    return result


def length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "ft": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }

    return convert_by_base(value, from_unit, to_unit, units)


def weight(value, from_unit, to_unit):
    units = {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1,
        "ton": 1000,
        "oz": 0.0283495,
        "lb": 0.453592
    }

    return convert_by_base(value, from_unit, to_unit, units)


def time(value, from_unit, to_unit):
    units = {
        "sec": 1,
        "min": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2592000,
        "year": 31536000
    }

    return convert_by_base(value, from_unit, to_unit, units)


def area(value, from_unit, to_unit):
    units = {
        "mm2": 0.000001,
        "cm2": 0.0001,
        "m2": 1,
        "km2": 1000000,
        "acre": 4046.86,
        "hectare": 10000
    }

    return convert_by_base(value, from_unit, to_unit, units)


def volume(value, from_unit, to_unit):
    units = {
        "mL": 0.001,
        "L": 1,
        "m3": 1000,
        "gallon": 3.78541,
        "cup": 0.236588
    }

    return convert_by_base(value, from_unit, to_unit, units)


def speed(value, from_unit, to_unit):
    units = {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704
    }

    return convert_by_base(value, from_unit, to_unit, units)


def pressure(value, from_unit, to_unit):
    units = {
        "Pa": 1,
        "kPa": 1000,
        "bar": 100000,
        "atm": 101325
    }

    return convert_by_base(value, from_unit, to_unit, units)


def energy(value, from_unit, to_unit):
    units = {
        "J": 1,
        "kJ": 1000,
        "cal": 4.184,
        "kcal": 4184
    }

    return convert_by_base(value, from_unit, to_unit, units)


def power(value, from_unit, to_unit):
    units = {
        "W": 1,
        "kW": 1000,
        "hp": 745.7
    }

    return convert_by_base(value, from_unit, to_unit, units)


def storage(value, from_unit, to_unit):
    units = {
        "bit": 0.125,
        "byte": 1,
        "KB": 1024,
        "MB": 1024 * 1024,
        "GB": 1024 * 1024 * 1024,
        "TB": 1024 * 1024 * 1024 * 1024
    }

    return convert_by_base(value, from_unit, to_unit, units)


def angle(value, from_unit, to_unit):
    units = {
        "deg": 1,
        "rad": 57.2958
    }

    return convert_by_base(value, from_unit, to_unit, units)


def frequency(value, from_unit, to_unit):
    units = {
        "Hz": 1,
        "kHz": 1000,
        "MHz": 1000000,
        "GHz": 1000000000
    }

    return convert_by_base(value, from_unit, to_unit, units)


def force(value, from_unit, to_unit):
    units = {
        "N": 1,
        "dyne": 0.00001
    }

    return convert_by_base(value, from_unit, to_unit, units)


def temperature(value, from_unit, to_unit):
    valid, err = validate_number(value)
    if not valid:
        return err

    valid_units = ["C", "F", "K"]

    if from_unit not in valid_units:
        return error("CONV00005")

    if to_unit not in valid_units:
        return error("CONV00005")

    if from_unit == to_unit:
        return value

    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5 / 9
    else:
        c = value - 273.15

    if to_unit == "C":
        return c
    elif to_unit == "F":
        return (c * 9 / 5) + 32
    else:
        return c + 273.15