# sample02.py
number = input("数字を入力してください\n")
# 文字型のnumberを数値型に変換する
number = int(number)

if number == 1 or number == 2:
    print("変数numberは1または2と等しいです")
else:
    print("変数numberは1、2以外の値です")

print("終了しました")