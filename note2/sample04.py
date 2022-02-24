# sample04.py

# 1. input関数で数（文字型）を入力してもらう
number = input("数を入力してください\n")
# 2. 数を数値型に変換する
number = int(number)
# 3. 計算する（今回は数を2倍にします）
answer = number * 2
# 4. 計算結果を表示する
print("計算結果は" + str(answer) + "です")