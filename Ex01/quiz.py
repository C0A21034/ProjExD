import random

def main():
    kotae = shutudai()
    kaito(kotae)

def shutudai():
    mondai = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]
    seikai = [["マスオ", "ますお"],["ワカメ", "わかめ"],["甥", "おい", "甥っ子", "おいっこ"]]
    print("問題.")
    a = random.randint(0,2)
    print(mondai[a])
    return seikai[a]
    

def kaito(kotae):
    a = input("答えるんだ：")
    if a in kotae:
        print("正解！！！！！！！！！！！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()