def moved(n,fromtower,totower,auxtower):
    if n==1:
        print("move disk",n,"from",fromtower,"to",totower)
    else:
        moved(n-1,fromtower,auxtower,totower)
        print("move disk",n,"from",fromtower,"to",totower)
        moved(n-1,auxtower,totower,fromtower)

moved(int(input()),'A','B','C')
