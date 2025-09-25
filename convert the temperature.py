class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        faranheit = celsius * 1.80 + 32.00
        ans = [Kelvin, faranheit]
        return ans
