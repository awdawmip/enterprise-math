#!/usr/bin/env python3
"""Exact rational certificate for S23/AV linear word complexity.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Only standard-library integer/Fraction operations; no floats or OCR.
"""
from fractions import Fraction
B=79
Q=10**24

def log_interval(p,q,n):
    x=Fraction(p-q,p+q)
    power=x
    low=Fraction(0)
    for j in range(n):
        low+=2*power/(2*j+1)
        power*=x*x
    return low,low+2*power/((2*n+1)*(1-x*x))

def cert_alpha(n=160):
    l7,u7=log_interval(7,1,n)
    l107,u107=log_interval(10,7,n)
    dl=79*l7-431*u107
    du=79*u7-431*l107
    nl=2074774*l107-380295*u7
    nu=2074774*u107-380295*l7
    assert 0<dl<du and 0<nl<nu
    lo,hi=nl/du,nu/dl
    assert Fraction(1,2)<lo<hi<Fraction(2,3)
    p=(lo*Q).__floor__()
    assert p==(hi*Q).__floor__(), 'insufficient decimal enclosure'
    assert Fraction(p,Q)<lo<hi<Fraction(p+1,Q)
    return p

def t_bounds(p,m):
    """For j>=1, t_j={-79j alpha}, certified in [lo,hi] / Q."""
    out=[]
    for j in range(1,m+1):
        n=B*j*p//Q
        assert n==B*j*(p+1)//Q
        low=(n+1)*Q-B*j*(p+1)
        high=(n+1)*Q-B*j*p
        assert 0<low<high<Q
        out.append((j,low,high))
    return out

def sym(t2,c,j,p):
    """t2 is numerator of t in units of 1/(2Q), x=(c+t)/B."""
    lo=(2*Q*c+t2+2*B*j*p)//(2*Q)%B
    hi=(2*Q*c+t2+2*B*j*(p+1))//(2*Q)%B
    assert lo==hi,(t2,c,j,'uncertified')
    return lo

def block(t2,c,m,p):
    return tuple(sym(t2,c,j,p) for j in range(m))

def check(m,p):
    arr=t_bounds(p,m)
    old=sorted([(0,0,0)]+arr[:-1]+[(m+1,Q,Q)],key=lambda x:x[1]+x[2])
    assert len(old)==m+1
    assert all(old[s][2]<old[s+1][1] for s in range(m))
    words=set()
    for c in range(B):
        for s in range(m):
            w=block(old[s][2]+old[s+1][1],c,m,p)
            assert w not in words
            words.add(w)
    assert len(words)==B*m
    tlo,thi=arr[-1][1:]
    spots=[s for s in range(m) if old[s][2]<tlo and thi<old[s+1][1]]
    assert len(spots)==1
    s=spots[0]
    right_special=set()
    for c in range(B):
        xleft=old[s][2]+tlo
        xright=thi+old[s+1][1]
        wleft=block(xleft,c,m,p)
        wright=block(xright,c,m,p)
        assert wleft==wright
        a=sym(xleft,c,m,p)
        b=sym(xright,c,m,p)
        assert (b-a)%B==1
        right_special.add(wleft)
    assert len(right_special)==B
    left=old[s]
    right=old[s+1]
    left_low=tlo-left[2]
    left_high=thi-left[1]
    right_low=right[1]-thi
    right_high=right[2]-tlo
    err_low=min(left_low,right_low)
    err_high=min(left_high,right_high)
    assert 0<err_low<=err_high<Q
    return len(words),len(right_special),s,err_low,err_high

if __name__=='__main__':
    p=cert_alpha()
    print('ALPHA_CERTIFIED_DECIMAL_BRACKET',f'{p}/{Q}',f'{p+1}/{Q}',flush=True)
    for m in [1,2,3,4,8,16,32,64,128]:
        total,special,s,el,eh=check(m,p)
        print('PASS_ROTATION_WORDS',f'm={m}',f'distinct={total}',f'right_special={special}',f'split_slot={s}',f'optimal_error_interval=[{el}/{Q},{eh}/{Q}]',flush=True)
    print('PASS_EXACT_S23_AV_LINEAR_COMPLEXITY_FINITE_CERTS',flush=True)
