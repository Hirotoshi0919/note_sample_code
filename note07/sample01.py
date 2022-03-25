# sample01.py
text = ""
count = 0
while text != "end":
    count = count + 1

    print("while文：" + str(count) + "回目のループです")
    text = input("何か文字を入力して下さい\n")
    print("「" + text + "」が入力されました")

print("while文を抜けました")
