def celsius_to_fahrenheit(celsius: float) -> float:
    """將攝氏溫度轉換為華氏溫度"""
    if not isinstance(celsius, (int, float)):
        raise ValueError("輸入的溫度必須是數字")
    return celsius * 9/5 + 32

# 單元測試部分
import unittest
import random
class TestTemperatureConversion(unittest.TestCase):
    
    def test_positive_temp(self):
        """測試正數溫度轉換"""
        a = random.randint(1, 1000)
        b = random.randint(1, 10000)
        c =random.uniform(1, 1000)

        result = celsius_to_fahrenheit(a)
        print(f"1. 攝氏 {a} 度轉換為華氏: {result} 度")

        result = celsius_to_fahrenheit(b)
        print(f"2. 攝氏 {b} 度轉換為華氏: {result} 度")

        result = celsius_to_fahrenheit(c)
        print(f"3. 攝氏 {c} 度轉換為華氏: {result} 度")
      

    def test_negative_temp(self):
        """測試負數溫度轉換"""
        a = random.randint(-1000, -1)
        b = random.uniform(-1000, -1)
        result = celsius_to_fahrenheit(a)
        print(f"4. 攝氏 {a} 度轉換為華氏: {result} 度")
        result = celsius_to_fahrenheit(b)
        print(f"5. 攝氏 {b} 度轉換為華氏: {result} 度")

    def test_zero(self):
        """測試零度轉換"""
        result = celsius_to_fahrenheit(0)
        print(f"6. 攝氏 0 度轉換為華氏: {result} 度")

    def test_fractional_temp(self):
        """測試小數溫度"""
        a = random.random()
        result = celsius_to_fahrenheit(a)
        print(f"7. 攝氏 {a} 度轉換為華氏: {result} 度")


    def test_edge_cases(self):
        """測試極端邊界情況"""
        result = celsius_to_fahrenheit(1e6)
        print(f"8. 攝氏 1e6 度轉換為華氏: {result} 度")

        result = celsius_to_fahrenheit(-1e6)
        print(f"9. 攝氏 -1e6 度轉換為華氏: {result} 度")

# 執行測試
if __name__ == '__main__':
    unittest.main()


