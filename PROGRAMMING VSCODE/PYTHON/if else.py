print('enter score')
score=int(input())
if score>=40:
    print('you have good score')
else:
    print('your have bad score')
    print('enter your total score')
    total_score=int(input())
    if total_score>=40:
        print('you are good batsman')
    else:
        if total_score>=30:
            print('you are average')
        else:
            print('you are bad batsman')            