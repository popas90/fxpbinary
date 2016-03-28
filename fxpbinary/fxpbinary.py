from math import floor, ceil, fmod, fabs


class TwosComplementInteger(object):
    pass
    # def __init__(self,  )


def _uint_to_bits(value):
    """Converts an integer value to a list of bits."""
    int_value = int(value)
    bits = []
    while int_value > 0:
        bits.insert(0, int_value % 2)
        int_value //= 2
    return bits


def _ufrac_to_bits(value):
    """Converts a fractional value to a list of bits"""
    frac_value = fmod(value, 1.0)
    bits = []
    while fmod(frac_value, 1.0) > 0:
        bits.insert(0, floor(frac_value * 2))
        frac_value = fmod(frac_value * 2, 1.0)
    return bits


class FxpNumber(object):
    """This class allows the creation of binary fixed-point numbers, especially
    for hardware emulation purposes. In general, a fixed-point looks like this:
    [ii..i],[ff..f], where each 'i' represents a bit in the integer part of the
    number and 'f' represents a bit in the fractional part. For representing
    signed numbers, two's complement is used, and the MSB becomes the sign bit:
    [sii..i],[ff..f]. Notice that when representing signed numbers, at least
    one bit must be assigned on the integer part of the number.
    """

    def __init__(self, numIntBits, numFracBits, val=0):
        self.integer_bits = []
        self.fractional_bits = []
        # self._value = val

    def _convert_to_twos_complement(value):
        sign = value < 0
        abs_value = fabs(value)
        frac_value = fmod(abs_value, 1.0)
        int_value = floor(abs_value)
        uint_bits = _uint_to_bits(int_value)
        ufrac_bits = _ufrac_to_bits(frac_value)
        
