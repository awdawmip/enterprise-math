#!/usr/bin/env python3
"""Exact author-side verification for hereditary Hall-flow absorption.
Proof of all-future decay is the theorem in the adjoining note, not enumeration.
"""
from fractions import Fraction
from itertools import product
from math import prod

W = ((1,665,1,333),(333,333,1,333),(1,1,1,997))
E = ((0,1),(1,2),(1,3),(2,3))
D = tuple(sum(i in e for e in E) for i in range(4))
SE = tuple(tuple(sum(W[a][i] for i in edge) for edge in E) for a in range(3))
CODE = {'0':0,'2':1,'3':2}

def atom(c):
    a = tuple(prod(W[t][i]**c[t] for t in range(3)) for i in range(4))
    b = tuple(prod(SE[t][j]**c[t] for t in range(3)) for j in range(4))
    return a,b

def occupancy(c):
    if sum(c)==0: return Fraction(0)
    a,b=atom(c)
    return Fraction(sum(b)-sum(D[i]*a[i] for i in range(4)),1000**sum(c))

def hall_rows(c):
    a,b=atom(c)
    for t in range(3):
        for mask in range(1,16):
            s={i for i in range(4) if mask&(1<<i)}
            cap=sum((1000-SE[t][j])*b[j] for j,e in enumerate(E) if s.intersection(e))
            dem=sum(D[i]*(1000-W[t][i])*a[i] for i in s)
            yield t,mask,cap-dem

def certified(c):
    return sum(c)>=2 and all(h>=0 for _,_,h in hall_rows(c))

def count_vectors(n):
    for x in range(n+1):
        for y in range(n-x+1):
            yield (x,y,n-x-y)

def history(word):
    c=[0,0,0]; old=peak=positive=Fraction(0)
    for letter in word:
        c[CODE[letter]]+=1
        now=occupancy(c)
        positive+=max(now-old,Fraction(0))
        peak=max(peak,now)
        old=now
    return tuple(c), old, peak, positive-peak

def independent_dp(word):
    mass=[0]*16; mass[0]=1
    for ch in word:
        nxt=[0]*16
        for mask in range(16):
            for i in range(4):
                nxt[mask|(1<<i)]+=mass[mask]*W[CODE[ch]][i]
        mass=nxt
    return Fraction(sum(mass[(1<<i)|(1<<j)] for i,j in E),1000**len(word))

def check():
    checks=0
    for n in range(9):
        for v in product('023',repeat=n):
            w=''.join(v)
            assert history(w)[1]==independent_dp(w),(n,w)
            checks+=1
    assert checks==9841
    safe=[]
    for n in range(2,7):
        for c in count_vectors(n):
            if certified(c):safe.append(c)
    assert safe==[(5,1,0)],safe
    first=(5,1,0); second=(0,10,0)
    min_first=[min((r for r in hall_rows(first) if r[0]==a),key=lambda r:r[2]) for a in range(3)]
    min_second=[min((r for r in hall_rows(second) if r[0]==a),key=lambda r:r[2]) for a in range(3)]
    assert [(r[1],r[2]) for r in min_first]==[
        (8,424379378457307386),(1,29146864489438065633),(8,1313328551379700394)]
    assert [(r[1],r[2]) for r in min_second]==[
        (4,17276854195127393442251774002),
        (4,23012769787909688065079363634),
        (4,17276854195127393442251774002)]
    successors=set()
    for n in range(5):
        for v in product(range(3),repeat=n):
            c=tuple(first[i]+v.count(i) for i in range(3))
            assert certified(c)
            successors.add(c)
    assert len(successors)==35
    h1=history('000002');h2=history('2222222222')
    assert h1[0]==first and h2[0]==second and h1[3]==h2[3]==0
    assert h1[1]==Fraction(41196163577218241,62500000000000000)
    assert h1[2]==Fraction(21447980969247,25000000000000)
    assert h2[1]==Fraction(4283967567856868870526585801,125000000000000000000000000000)
    assert h2[2]==Fraction(55611,125000)
    suffixes=0
    for n in range(6):
        for v in product('023',repeat=n):
            s=''.join(v)
            assert history('000002'+s)[3]==history('2222222222'+s)[3]==0
            suffixes+=1
    assert suffixes==364
    print('PASS 9841 mask recurrence; 80 count vectors; 3600 Hall cuts; 35 successor counts; 364 suffix pairs')
    print('strict Hall cut minima:',min_first,min_second)
    print('witness residuals:',h1[3],h2[3])

if __name__=='__main__':
    check()
