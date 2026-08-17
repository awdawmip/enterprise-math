#!/usr/bin/env python3
from dataclasses import dataclass

LOCAL_DIR={"1":(0,1),"2":(-1,1),"3":(-1,0)}

@dataclass(frozen=True)
class SegmentState:
    O: tuple
    r: int
    sector: int
    phase: str
    a: int
    b: int
    z: int

def rot(p):
    a,b=p
    return (-b,a+b)

def rotk(p,k):
    a,b=p
    for _ in range(k%6):
        a,b=rot((a,b))
    return (a,b)

def add(p,q):
    return (p[0]+q[0],p[1]+q[1])

def anchor(O,r,sector=0):
    if not isinstance(r,int) or r<1:
        raise ValueError('r must be a positive integer')
    return SegmentState(tuple(O),r,sector%6,'L',r,0,-4)

def endpoint(S):
    return add(S.O,rotk((S.a,S.b),S.sector))

def translate(S,t):
    return SegmentState(add(S.O,tuple(t)),S.r,S.sector,S.phase,S.a,S.b,S.z)

def rotate_state(S,j=1):
    return SegmentState(rotk(S.O,j),S.r,(S.sector+j)%6,S.phase,S.a,S.b,S.z)

def _next_sector(S):
    return anchor(S.O,S.r,S.sector+1)

def tau(S):
    r,k,ph,a,b,z=S.r,S.sector,S.phase,S.a,S.b,S.z
    if ph=='L':
        d=a-b
        if d<1:
            raise ValueError('invalid L state')
        if d>1:
            if z>=0:
                symbol='1'
                z2=z-3*(a+2*b+3)
                a2,b2=a,b+1
            else:
                symbol='2'
                z2=z+3*(a-b-3)
                a2,b2=a-1,b+1
            if a2-b2==0:
                S2=SegmentState(S.O,r,k,'R',a2,b2,z2+9*b2+3)
            else:
                S2=SegmentState(S.O,r,k,'L',a2,b2,z2)
        else:
            symbol='2'
            sigma=z+9*b+3
            a2,b2=a-1,b+1
            if a2==0:
                S2=_next_sector(S)
            else:
                S2=SegmentState(S.O,r,k,'R',a2,b2,sigma)
    elif ph=='R':
        if not (0<a<=b):
            raise ValueError('invalid R state')
        if z>=0:
            symbol='2'
            z2=z+3*(a-b-2)
            a2,b2=a-1,b+1
        else:
            symbol='3'
            z2=z+3*(2*a+b-2)
            a2,b2=a-1,b
        if a2==0:
            S2=_next_sector(S)
        else:
            S2=SegmentState(S.O,r,k,'R',a2,b2,z2)
    else:
        raise ValueError('bad phase')
    return S2,symbol

def orbit(O,r):
    S0=anchor(O,r)
    S=S0
    states=[S]
    symbols=[]
    while True:
        S,c=tau(S)
        symbols.append(c)
        states.append(S)
        if S==S0:
            break
    return states,symbols

if __name__=='__main__':
    import json,sys
    r=int(sys.argv[1]) if len(sys.argv)>1 else 10
    states,symbols=orbit((0,0),r)
    print(json.dumps({"r":r,"turn_period":len(symbols),"endpoints":[endpoint(s) for s in states[:-1]],"symbols":"".join(symbols)},sort_keys=True))
