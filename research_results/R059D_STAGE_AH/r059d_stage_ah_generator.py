#!/usr/bin/env python3

MIRROR={'1':'3','2':'2','3':'1'}
DIR={'1':(0,1),'2':(-1,1),'3':(-1,0)}

def generate_word(r:int)->str:
    if not isinstance(r,int) or r<0:
        raise ValueError('r must be a nonnegative integer')
    if r==0:
        return ''
    a,b=r,0
    rho=-4
    half=[]
    while a-b>1:
        if rho>=0:
            half.append('1')
            rho -= 3*(a+2*b+3)
            b += 1
        else:
            half.append('2')
            rho += 3*(a-b-3)
            a -= 1
            b += 1
    center='2' if a-b==1 else ''
    return ''.join(half)+center+''.join(MIRROR[c] for c in reversed(half))

def readouts(r:int,w:str):
    h=0;B=0
    n1=n2=n3=0
    a,b=r,0
    vertices=[(a,b)]
    for c in w:
        if c=='1':
            n1+=1;h+=1;b+=1
        elif c=='2':
            n2+=1;B+=h;a-=1;b+=1
        elif c=='3':
            n3+=1;B+=h;h-=1;a-=1
        else:
            raise ValueError('bad symbol')
        if h<0:
            raise AssertionError('non-Motzkin word')
        vertices.append((a,b))
    if h!=0 or (a,b)!=(0,r):
        raise AssertionError('bad endpoint')
    J=n1
    if n3!=J or n2!=r-J:
        raise AssertionError('bad symbol counts')
    return {'W':w,'B':B,'J':J,'D':2*r+1,'C':6*r+6*J,'V':1+3*r*(r+1)+6*B,'sector_vertices':vertices}

def rot(p):
    a,b=p
    return (-b,a+b)

def rotk(p,k):
    a,b=p
    for _ in range(k%6):
        a,b=rot((a,b))
    return (a,b)

def d6_boundary(sector_vertices):
    full=[]
    for k in range(6):
        z=[rotk(p,k) for p in sector_vertices]
        if k==0:
            full.extend(z)
        else:
            full.extend(z[1:])
    return full

def generate_enterprise_circle_N(r:int):
    w=generate_word(r)
    out=readouts(r,w)
    out['full_boundary']=d6_boundary(out['sector_vertices']) if r>0 else [(0,0)]
    return out

if __name__=='__main__':
    import json,sys
    r=int(sys.argv[1]) if len(sys.argv)>1 else 10
    print(json.dumps(generate_enterprise_circle_N(r),sort_keys=True))
