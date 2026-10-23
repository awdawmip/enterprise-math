#!/usr/bin/env python3
"""C270 four-shared exact 852-leaf proof for C195/H168 positive-rational 79-node auxiliary.
Author-level mathematical certificate, not native GF(2)-BRC, not independent Driver-reviewed.
Integer masses, nonnegative convex affine envelopes, four-variable multiaffine 16-corner minima.
All inputs and binary splitting trees embedded; requires Python standard library only.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
I=(5,50,55,56);J=tuple(j for j in range(79) if j not in I)
Z=F(141421356237309504880,10**20)
Q=2**128;H=2**166;A=F(6912*50000**2,17**2)
assert len(U)==79 and all(U[j]<U[j+1] for j in range(78))
B={}
for j in J:
    v=F(Q)*A/H/((2-U[j]**2)*(3-U[j]**2))**3
    for p in range(79):
        if p!=j:v*=(Z-U[p])/abs(U[j]-U[p])
    B[j]=v.numerator//v.denominator
    assert B[j]>0

def fac(j,p,t):
    return (Z-t)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-t)

def affine(j,p,lo,hi):
    s=(lo+hi)/2
    val=fac(j,p,s)
    slope=val*(-1/(Z-s)-1/(s-U[j]))
    x=val+slope*(lo-s);y=val+slope*(hi-s)
    if x>=0 and y>=0:return x,y
    e=lo if j>p else hi
    return fac(j,p,e),fac(j,p,e)

def mov(k,lo,hi):
    d=I.index(k);t=(lo[d]+hi[d])/2
    val=F(Q)*A/H/((2-t*t)*(3-t*t))**3
    slope=6*t/(2-t*t)+6*t/(3-t*t)
    for j in J:
        val*=(Z-U[j])/abs(t-U[j]);slope-=1/(t-U[j])
    for p in I:
        if p==k:continue
        dd=I.index(p);e=lo[dd] if p<k else hi[dd]
        val*=(Z-e)/abs(t-e);slope-=1/(t-e)
    e=lo[d] if slope>=0 else hi[d]
    return max(F(0),val*(1+slope*(e-t)))

def bound4(lo,hi):
    fixed=[F(0) for _ in range(16)]
    for j in J:
        corners=[affine(j,p,lo[d],hi[d]) for d,p in enumerate(I)]
        for n in range(16):
            term=F(B[j])
            for d in range(4):term*=corners[d][(n>>(3-d))&1]
            fixed[n]+=term
    return min(fixed)+sum((mov(k,lo,hi) for k in I),F(0))

ROOTS={
    '18_ALL':(('2/271','34/49','60/77','19/24'),('6/409','28/39','72/91','41/51'),507,3160132858209827601324667317753066,"22a3a2a3a30a0aa000111aaa1aaaa0aa33a2a2aa2233a0a0aa3000111aa0aa1aaaa0a0aa000111aa0aa10aaa111aaa1aa0111aaa1aa111aaa1aa00111aaa1aaa0a10a1aa1aa330a0aa000111aa0aa1aaaa0a0aa3000111aa00aaa10aaa111aaa1aa0111aaa1aa111aaa1aa00111aaa1aaa0a10a1aa1aa000111aa00aaa100aaaa111aa1aa1aa0111aa1aa1aa111aa1aa1aa00111aa1aa1aa111aaa1aa0a10a1aa1aa323000111aaa1aaaa0aa000111aa0aa10aaa111aaa1aa0111aaa1aa111aaa1aa00aa0a10a1aa1aa3000111aaa1aaaa0aa000111aa00aaa10aaa111aaa1aa0111aaa1aa111aaa1aa00111aaa1aaa0a10a1aa1aa23000111aa00aaa100aaaa111aa1aa1aa0111aa1aa1aa111aa1aa1aa00111aaa1aa111aaa1aa0a10a1aa1aa000111a0aa00aaa100aaa1aa111aa1a0aa11aaa0111aa11aa12aa2aa112aaaa111aa11aa12aaa112aaaa00111aa1aa11aaa111aaa1aa0a10a1aa10aaa3000111aa00aaa100aaaa111aa1aa11aaa0111aa1aa11aaa111aa1aa11aaa00111aa1aa1aa111aaa1aa0a10a1aa10aaa000111a0aa00aaa100aaa1aa111aa11aa0a12aa2aa110a2aaaa0111aa11a2aa121a2aa21a2aa1a2a0aa22aa22a0aa20a1aa0a1aa1121aa12aaaaa111aa11a2aa121aa21aa1a2aa22aa22aa21aa1aa1121aa12aaaaa00111aa11aa12aa2aa112aaaa111aa1aa1aa0a10a1aa10aaa"),
    '21_22':(('1/105','7/10','53/68','13/16'),('3/205','18/25','21/26','23/28'),345,1010974601248244513663243410561557,"310303011222aa2aa22aaa222aa22aa22aaa22aaa1222aa22aa2aa22aaa222aa2aa2aa11222aa2aa2aa222aa22aa22aaa22aaa1222aa22aa2aa22aaa222aa2aa2aa011222aaa2aa222aa2aa2aa1222aaa2aa222aaa2aa11222aaa2aa222aa2aa2aa1222aaa2aa222aaa2aa3011222aa2aa2aa222aa22aa2aa22aaa1222aa2aa22aaa222aa2aa2aa11222aa2aa2aa222aa2aa2aa1222aa2aa2aa222aaa2aa011222aaa2aa222aaa2aa1222aaa2aa222aaa2aa1122aa2aa222aaa2aa1222aaa2aa22aa2aa3001122aaa22aaa122aaa22aaa1122aaa22aaa122aaa22aaa01122aaa22aaa122aaa22aaa1122aaa22aaa122aaa22aaa22aaa03031122aa2aa222aaa2aa1222aaa2aa22aa2aa1122aaa22aa2aa122aaa22aaa311a22aa2aa122aa2aaaa3011a22aaa122aaaaaa0a3311aa1aaaa130103022aa2aa22aa2aa022aaa22aaa3022aa2aaaaa01aa0aa013aaa0a0aa1aa3122aaa12aaa2aa")
}

def check(name,first=0,last=None):
    x,y,count,expected_margin,tree=ROOTS[name]
    lo=tuple(F(t) for t in x);hi=tuple(F(t) for t in y)
    for d,p in enumerate(I):assert U[p-1]<lo[d]<=hi[d]<U[p+1]
    assert hi[2]<lo[3] and hi[3]<Z
    last=count if last is None else last
    assert 0<=first<last<=count
    cursor=[0];leaves=[0];splits=[0];minimum=[None]
    def walk(a,b):
        t=tree[cursor[0]];cursor[0]+=1
        if t=='a':
            k=leaves[0];leaves[0]+=1
            if first<=k<last:
                v=bound4(a,b);margin=v.numerator//v.denominator-Q
                assert margin>0,(name,k,margin)
                minimum[0]=margin if minimum[0] is None else min(minimum[0],margin)
            return
        d=int(t);assert 0<=d<4
        mid=(a[d]+b[d])/2
        assert a[d]<mid<b[d]
        left=list(b);left[d]=mid;right=list(a);right[d]=mid
        splits[0]+=1
        walk(a,tuple(left));walk(tuple(right),b)
    walk(lo,hi)
    assert cursor[0]==len(tree) and leaves[0]==count and splits[0]==count-1
    if first==0 and last==count:assert minimum[0]==expected_margin
    print('C270_STANDALONE_EXACT_PASS',name,first,last,'margin',minimum[0])

if __name__=='__main__':
    import sys
    if len(sys.argv)==1:
        for name in ROOTS:check(name)
    else:
        check(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 0,int(sys.argv[3]) if len(sys.argv)>3 else None)
