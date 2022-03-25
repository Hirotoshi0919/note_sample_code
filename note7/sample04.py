# note_sample_code/note7/sample04.py
count = 0
while True:
    count = count + 1
    print("while文：" + str(count) + "回目のループです")
    text = input("何か文字を入力して下さい\n")

    if text != "end":
        print("「" + text + "」が入力されました")
        continue
    else:
        print("「" + text + "」が入力されました")
        break
print("while文を抜けました")