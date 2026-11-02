
class Calculator(object):
    _instance = None

    # Number names in English, German, Spanish, Russian, Chinese
    _NAMES = {
        # English
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        # German
        'null': 0, 'ein': 1, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4,
        'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9,
        # Spanish
        'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
        'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9,
        # Russian (Cyrillic)
        'ноль': 0, 'нуль': 0, 'один': 1, 'одна': 1, 'два': 2, 'две': 2,
        'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
        'семь': 7, 'восемь': 8, 'девять': 9,
        # Chinese
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
        '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
    }

    # Latin numeral values (two-char pairs checked before single chars)
    _LATIN_PAIRS = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    _LATIN_SINGLE = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def _from_latin(self, s):
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in self._LATIN_PAIRS:
                result += self._LATIN_PAIRS[s[i:i+2]]
                i += 2
            else:
                result += self._LATIN_SINGLE[s[i]]
                i += 1
        return result

    def _to_number(self, x):
        if isinstance(x, (int, float)):
            return x
        s = str(x).strip()
        # Try integer
        try:
            return int(s)
        except ValueError:
            pass
        # Try float
        try:
            return float(s)
        except ValueError:
            pass
        # Try name lookup (case-insensitive for Latin scripts)
        if s in self._NAMES:
            return self._NAMES[s]
        if s.lower() in self._NAMES:
            return self._NAMES[s.lower()]
        # Try Latin numerals (all chars must be valid Latin numeral chars)
        upper = s.upper()
        if upper and all(c in 'IVXLCDM' for c in upper):
            return self._from_latin(upper)
        raise ValueError(f"Cannot convert '{x}' to a number")

    def add(self, a, b):
        return self._to_number(a) + self._to_number(b)

    def sub(self, a, b):
        return self._to_number(a) - self._to_number(b)

    def mul(self, a, b):
        return self._to_number(a) * self._to_number(b)

    def div(self, a, b):
        return self._to_number(a) / self._to_number(b)

    def factorize(self, n):
        n = int(self._to_number(n))
        if n <= 1:
            return []
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
