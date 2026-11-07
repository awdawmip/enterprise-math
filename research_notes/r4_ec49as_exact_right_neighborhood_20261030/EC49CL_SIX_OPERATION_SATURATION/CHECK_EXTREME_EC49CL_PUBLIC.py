"""Independent standalone exact extreme-fiber witness for EC49CL; executed 2026-10-31."""
from math import prod
P=1000003
W=((2,3,3,2,1,1),(3,2,3,2,1,1))

def det_mod(a):
    a=[[v%P for v in row] for row in a];d=1
    for j in range(len(a)):
        r=next((i for i in range(j,len(a)) if a[i][j]),None)
        if r is None:return 0
        if r!=j:a[j],a[r]=a[r],a[j];d=-d
        t=a[j][j];d=d*t%P;iv=pow(t,-1,P)
        for i in range(j+1,len(a)):
            f=a[i][j]*iv%P
            for k in range(j+1,len(a)):
                a[i][k]=(a[i][k]-f*a[j][k])%P
            a[i][j]=0
    return d%P

def label(p):
    return 2*any(x==1 and y==2 for x,y in zip(p,p[1:]))+any(x==2 and y==1 for x,y in zip(p,p[1:]))

def extreme(primary):
    other=3-primary;b=(primary,)*12
    pairs=((3,-3),(primary,-primary),(other,-other))
    result=[]
    for tag in range(4):
        for pair in pairs:
            if primary==1:
                if tag==0:
                    if pair==(3,-3):seq=b+(3,-3,-2,2)
                    elif pair==(1,-1):seq=b+(-2,2,-1,1)
                    else:seq=b+(-2,2,-2,2)
                elif tag==1:seq=(2,)+b+(-2,)+pair
                elif tag==2:seq=b+(2,-2)+pair
                else:seq=b[:6]+(2,)+b[6:]+(-2,)+pair
            else:
                if tag==0:
                    if pair==(3,-3):seq=b+(3,-3,-1,1)
                    elif pair==(2,-2):seq=b+(-2,2,-1,1)
                    else:seq=b+(-1,1,-1,1)
                elif tag==1:seq=b+(1,-1)+pair
                elif tag==2:seq=(1,)+b+(-1,)+pair
                else:seq=b[:6]+(1,)+b[6:]+(-1,)+pair
            assert len(seq)==16 and label(seq)==tag
            assert sum(a==primary for a in seq)-sum(a==-primary for a in seq)==12
            assert sum(a==other for a in seq)==sum(a==-other for a in seq)
            result.append(seq)
    return result

def check(primary):
    suffix=(-primary,)*12
    paths=extreme(primary)
    mat=[]
    for tag in range(4):
        for ch in range(3):
            row=[]
            for path in paths:
                full=path+suffix
                weights=prod(W[ch][x-1] for x in full if x>0) if ch<2 else 1
                row.append(weights if label(full)==tag else 0)
            mat.append(row)
    return det_mod(mat)

if __name__=='__main__':
    for ax in (1,2):
        x=check(ax)
        print('extreme E'+str(ax),'det mod',P,'=',x)
        assert x==390243
    print('EC49CL exact independent 12x12 extreme witnesses PASS')
