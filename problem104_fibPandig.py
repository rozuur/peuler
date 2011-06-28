phi = 1.6180339887498949

x,y = 1,1
iid = 1
l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
mod = 1000000000
nine = mod/10

while y<nine:
    x,y,iid = y,x+y,iid+1

X = x
while iid<=2750:
    x,y,iid = y, (x+y), iid+1
    if x>= mod:
        x -= mod
    if y>= mod:
        y -= mod
    X = X*phi
    if X>nine*nine:
        X /= nine

while True:
    x,y,iid = y,(x+y),iid+1
    if x>= mod:
        x -= mod
    if y>= mod:
        y -= mod
    X = X*phi
    if X>nine*nine:
        X /= nine
    if x<nine:
        continue
    t = sorted( list(str(x)) )
    if t == l:
        s = str(X)[:10]
        if s[1] == '.':
            s = s[0]+s[2:]
        else:
            s = s[:9]
        s = sorted(s)
#        print iid,"".join(s) ,"...","".join(t)
        if s==l:
            print iid
            break
    
