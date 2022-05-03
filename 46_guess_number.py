import random

while True :
    print('快樂猜數字遊戲！')
    max_num = input('請輸入欲猜測之最大數字')
    min_num = input('請輸入欲猜測之最小數字')
    if max_num.isdigit() and min_num.isdigit():
        min_num = int(min_num)
        max_num = int(max_num)
        ans = random.randint(min_num , max_num)
        print('開始遊戲！')
        break
    else :
        print('請只輸入數字喔！')

frequency = 0

while True :
    guess = input('請輸入數字:')
    if guess.isdigit():
        guess = int(guess)
        frequency = frequency + 1
        if guess == ans :
            print('恭喜你完成遊戲！')
            print('你一共猜了',frequency,'次')
            break
        else :
            print('猜錯瞜！')
            if guess < ans :
                print('答案比你猜的還要大喔')
            else :
                print('答案比你猜的還要小喔')
    else :
        print('請只輸入數字喔！')
