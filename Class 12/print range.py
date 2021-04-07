def printr(l,u):
    if (l==u+1):
        return
    else:
        print(l)
        printr(l+1,u)
printr(1,10)
