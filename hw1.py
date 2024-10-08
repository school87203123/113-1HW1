from typing import List 
    #從標準庫的 typing 模組中導入 List 類型。 

def countLetters(sentence: str) -> List[int]:
    # 定義一個名為 countLetters 的函數，參數是 sentence（類型為字串），返回值是整數列表。
    
    letterCount: List[int] = [0] * 26
        # 定義 letterCount 變數，其類型為整數列表，並初始化為 26 個 0，
        # 代表英文字母 a 到 z 的出現次數，初始值為 0。

    for char in sentence:
        # 使用 for 迴圈逐一檢查 sentence 中的每個字符。

        if char.isalpha():
             # 用 Python 內建方法 isalpha 檢查 char 是否為字母。
            index = ord(char) - ord('a')
                # 用 ord 函數將字符轉換為 ASCII 值，然後減去 'a' 的 ASCII 值
                # 得出該字母在字母表中的索引（a=0, b=1, ..., z=25）。
            letterCount[index] += 1 
                # 根據計算出的索引，將 letterCount 中對應字母的計數加 1。

    return letterCount 
    #回傳letterCount的值
pass 
    # `pass` 在這裡其實沒有實際作用，可以省略

def printLetterCount(letterCount: List[int]) -> None: 
    # 定義一個名為 printLetterCount 的函式，參數是 letterCount
    # 參數 letterCount 是一個長度為 26 的整數列表，表示各字母的出現次數
    # 該函式不返回任何值，只是將每個字母及其出現次數打印出來

    for i in range(26):
        # 使用 for 迴圈檢查 0 到 25 的索引，檢查字母 a ~ z
        if letterCount[i] > 0:
            # 如果 letterCount 中的第 i 個元素大於 0，說明該字母至少出現過一次
         print(f"{chr(i + ord('a'))}: {letterCount[i]}")
            # 將索引 i 對應的字母（使用 chr 函數將 i 加上 'a' 的 ASCII 值轉為字母） (就能打印出對應的字母)
            # 以及該字母的出現次數（letterCount[i]）打印出來
pass 
    # `pass` 在這裡其實沒有實際作用，可以省略


inputSentence: str = "this is an apple"
    # 定義 inputSentence 變數，類型為字串，內容為 "this is an apple" (可以任意改成你想要檢查的字串)
letterCount: List[int] = countLetters(inputSentence) 
    # 調用 countLetters 函式，將上面的inputSentence 作為參數，得到該句子中每個字母的出現次數
    # letterCount 是整數列表，表示各個字母的出現次數    
printLetterCount(letterCount)
    # 調用 printLetterCount 函式，將 letterCount 列表傳入
    # 以打印出句子中各字母的出現次數