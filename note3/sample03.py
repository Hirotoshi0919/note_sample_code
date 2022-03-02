# sample03.py
number = input("数字を入力してください\n")
# 文字型のnumberを数値型に変換する
number = int(number)

if number == 1:
    print("変数numberは1と等しいです")
elif number == 2:
    print("変数numberは2と等しいです")
elif number == 100:
    print("変数numberは100と等しいです")
else:
    print("変数numberは1、2、100以外の値です")

print("終了しました")
