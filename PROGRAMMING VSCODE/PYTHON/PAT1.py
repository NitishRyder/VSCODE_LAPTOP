nig=int(input())
rent=int(input())
gst=0
ba=0
if rent<1000:
    gst=0
    ba=nig*rent
    print(int(ba))
elif rent>=1000 and rent<=2499:
    gst=rent*0.12
    rent=rent+gst
    ba=nig*rent
    print(int(ba))
elif rent>=2500 and rent<=7499:
    gst=rent*0.18
    rent+=gst
    ba=nig*rent
    print(int(ba))
else:
    gst=rent*0.28
    rent+=gst
    ba=nig*rent
    print(ba)