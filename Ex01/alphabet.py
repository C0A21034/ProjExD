import random
from re import I
a = 10
b = 2
x = list()
saidai = 5
kaisuu = 0

def main():
    for i in range(saidai):
        kotae = alphabet()
        kekka = kaitou(kotae)
        if kekka == True:
            break
        
def alphabet():
    al = [chr(c+65) for c in range(26)]
    x = random.sample(al, a)
    print("対象文字")
    print(x)

    z = random.sample(x,b)
    ##print("欠損文字")
    ##print(z)

    for i in range(b):
        x.remove(z[i])
    random.shuffle(x)
    print("表示文字")
    print(x)
    return z

def kaitou(kotae):
    q = int(input("欠損文字はいくつあるでしょうか？:"))
    if q == b:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        for i in range(saidai):
            r = input("一つ目の文字を入力してください")
            s = input("二つ目の文字を入力してください")
            if r in kotae and s in kotae:
                print("正解です！！！！！！！！")
                return True
            else:
                print("不正解です。またチャレンジしてください")
                if i == saidai-1:
                    return True
    else:
        print("不正解です。またチャレンジしてください")


if __name__ == "__main__":
    main()