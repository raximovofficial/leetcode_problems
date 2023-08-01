import decimal
class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.0
        ans = [decimal.Decimal.from_float(Kelvin),decimal.Decimal.from_float(Fahrenheit)]
        return ans

celsius = 36.50
a = Solution()
print(a.convertTemperature(celsius))