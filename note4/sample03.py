# sample03.py
number = input("数字を入力してください\n")
# 文字型のnumberを数値型に変換する
number = int(number)

if number >= 10 and number <= 100:
    print("変数numberは10以上、100以下の値です")
else:
    print("変数numberは10未満または、100より大きい値です")

print("終了しました")