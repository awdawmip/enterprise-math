#!/usr/bin/env python3
"""Signed X6 / two positive BRC channels / four ordered A-B tags.
Finite regression for EC49DA uniform analytic boundary theorem. Python 3 stdlib.
"""
from itertools import combinations
P=1000003
W0=(2,3,3,2,1,1); W1=(3,2,3,2,1,1)
G={0:('1111','3111','2311'),1:('3211','2111','3221'),
   2:('1112','1122','3112'),3:('1211','2121','3121')}

def tag(p):
    pairs=set(zip(p,p[1:]))
    return 2*int((1,2) in pairs)+int((2,1) in pairs)

def end(p):
    z=[0]*6
    for x in p:z[abs(x)-1]+=1 if x>0 else -1
    return tuple(z)

def brc(p):
    a=b=1
    for x in p:
        if x>0:a*=W0[x-1];b*=W1[x-1]
    return a,b,1

def det(M):
    A=[[v%P for v in row] for row in M];d=1;n=len(A)
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];d=-d
        q=A[j][j];d=d*q%P;inv=pow(q,-1,P)
        for i in range(j+1,n):
            c=A[i][j]*inv%P
            if c:
                for m in range(j+1,n):A[i][m]=(A[i][m]-c*A[j][m])%P
    return d%P

def witness(h,s,v):
    # Return complete native paths for all |s|+v=h boundary endpoints.
    out=[];u=abs(s)
    if s<=0:
        for lab in range(4):
            for word in G[lab]:
                g=tuple(map(int,word))
                out.append((lab,(-1,)*(2*u)+g+tuple(-x for x in g)+(2,)*(2*v)))
        future=(3,1,1,-3)*u+(-2,-2)*v
    elif v==0:
        for lab in range(4):
            for word in G[lab]:
                g=tuple(map(int,word))
                out.append((lab,g+tuple(-x for x in g)+(1,)*(2*h)))
        future=(-1,-1)*h
    else:
        A=(1,)*(2*u);B=(2,)*(2*v)
        for lab in range(4):
            for var in range(3):
                x=(1,-1) if var==1 else ()
                y=(2,-2) if var==2 else ()
                f=(3,-3)*(4-int(var!=0))
                if lab==0:p=A+x+f+B+y
                elif lab==1:p=B[:-1]+y+B[-1:]+A+x+f
                elif lab==2:p=A[:-1]+x+A[-1:]+B+y+f
                else:p=A[:-2]+x+A[-2:-1]+B[:-1]+(1,2)+y+f
                out.append((lab,p))
        future=(-1,-1)*u+(-2,-2)*v
    return out,future

def check(h,s,v):
    assert abs(s)+v==h and v>=0
    paths,future=witness(h,s,v)
    target=(2*s,2*v,0,0,0,0)
    assert len(paths)==12 and end(future)==tuple(-x for x in target)
    assert all(len(p)==2*h+8 and end(p)==target and tag(p+future)==lab
               for lab,p in paths)
    M=[[brc(p+future)[c] if tag(p+future)==lab else 0 for _,p in paths]
       for lab in range(4) for c in range(3)]
    d=det(M);assert d!=0,(h,s,v)
    if s<=0:
        u=-s;f0=3**(2*v)*12**u;f1=2**(2*v)*27**u
        assert d==(-216**4*(f0*f1)**4)%P
    if s==h:
        assert d==(-216**4*6**(8*h))%P
    return d

def main():
    residues=[]
    for h in range(1,31):
        for v in range(h+1):
            u=h-v
            residues.append(check(h,-u,v))
            if u>0:residues.append(check(h,+u,v))
    # Exhaust all permutations of e and b for negative-edge h<=8.
    checks=0
    for h in range(1,9):
        for v in range(h+1):
            u=h-v
            paths,_=witness(h,-u,v)
            for pos in combinations(range(h),u):
                slots=set(pos)
                future=tuple(x for k in range(h) for x in
                    ((3,1,1,-3) if k in slots else (-2,-2)))
                for lab,p in paths:
                    a,b,_=brc(p);assert tag(p+future)==lab
                    assert brc(p+future)==(a*12**u,b*27**u,1)
                    checks+=1
    import json
    print(json.dumps({'status':'PASS','h_range':'1..30','boundary_fibers':len(residues),
       'nonzero_12x12_mod_1000003':len(residues),
       'all_suffix_permutation_path_checks_h_le_8':checks,
       'min_mod':min(residues),'max_mod':max(residues)},sort_keys=True))
if __name__=='__main__':main()
