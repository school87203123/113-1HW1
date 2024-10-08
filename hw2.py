def reverse_number(N: int) -> int:
    # 檢查 N 是否在範圍內
    if N < 1 or N > 100000:
        return "輸入的數字不在範圍內"
    
    reversed_number = 0
    while N > 0:
        digit = N % 10  # 取出最後一位數字
        reversed_number = reversed_number * 10 + digit  # 將反轉的數字加上這一位
        N = N // 10  # 移除最後一位數字
    return reversed_number

# 主程式部分
N = int(input("請輸入一個正整數 (1 ≤ N ≤ 100000): "))
print(reverse_number(N))



