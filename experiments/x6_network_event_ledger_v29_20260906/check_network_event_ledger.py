#!/usr/bin/env python3
"""Exact finite checks for X6 upper V29 network event ledger."""
from __future__ import annotations

from copy import deepcopy
from itertools import product

P=4
CELLS=('x','y')

def zero_matrix(): return [[0]*P for _ in range(P)]
def zero_vec(): return [0]*P

def fresh():
    return {c:{'M':zero_matrix(),'rin':zero_vec(),'rout':zero_vec()} for c in CELLS}

def row(M): return [sum(r) for r in M]
def col(M): return [sum(M[i][j] for i in range(P)) for j in range(P)]

def derived(L,c):
    M=L[c]['M']; rin=L[c]['rin']; rout=L[c]['rout']
    I=[row(M)[i]+rin[i] for i in range(P)]
    O=[col(M)[i]+rout[i] for i in range(P)]
    Om=[[M[i][j]-M[j][i] for j in range(P)] for i in range(P)]
    u=[I[i]-O[i] for i in range(P)]
    rhs=[sum(Om[i])+rin[i]-rout[i] for i in range(P)]
    assert u==rhs
    assert all(v>=0 for v in I+O+rin+rout)
    assert all(v>=0 for r in M for v in r)
    return I,O,Om,u

def charge(L):
    return sum(sum(derived(L,c)[3]) for c in CELLS)

def passage(L,c,a,b):
    L[c]['M'][a][b]+=1

def transfer(L,x,a,y,b):
    L[x]['rout'][a]+=1
    L[y]['rin'][b]+=1

def snapshot(L):
    return tuple(
        (c,tuple(tuple(r) for r in L[c]['M']),tuple(L[c]['rin']),tuple(L[c]['rout']))
        for c in CELLS
    )

# Primitive increment laws.
L=fresh(); q0=charge(L)
passage(L,'x',0,1)
_,_,Om,u=derived(L,'x')
assert u==[1,-1,0,0]
assert Om[0][1]==1 and Om[1][0]==-1
assert charge(L)==q0

L=fresh(); q0=charge(L)
transfer(L,'x',2,'y',3)
assert derived(L,'x')[3]==[0,0,-1,0]
assert derived(L,'y')[3]==[0,0,0,1]
assert charge(L)==q0

# A nontrivial mixed closed-network history remains exactly conservative.
L=fresh()
events=(
    ('P','x',0,1),
    ('P','x',1,2),
    ('T','x',2,'y',0),
    ('P','y',0,3),
    ('T','y',3,'x',1),
    ('P','x',1,0),
)
for ev in events:
    if ev[0]=='P': passage(L,*ev[1:])
    else: transfer(L,*ev[1:])
    assert charge(L)==0
    for c in CELLS: derived(L,c)

# Cumulative ledger is multiset/order blind: all permutations of three
# additive event occurrences reach one exact count endpoint.
base_events=(('P','x',0,1),('P','x',1,0),('T','x',2,'y',3))
from itertools import permutations
ends=set()
for word in permutations(base_events):
    L=fresh()
    for ev in word:
        if ev[0]=='P': passage(L,*ev[1:])
        else: transfer(L,*ev[1:])
    ends.add(snapshot(L))
    assert charge(L)==0
assert len(ends)==1

# Exhaustive short-word conservation over a small event alphabet.
alphabet=(
    ('P','x',0,1),('P','x',1,0),
    ('P','y',2,3),('P','y',3,2),
    ('T','x',0,'y',1),('T','y',1,'x',0),
)
words=0
for n in range(5):
    for word in product(alphabet, repeat=n):
        L=fresh()
        for ev in word:
            if ev[0]=='P': passage(L,*ev[1:])
            else: transfer(L,*ev[1:])
        assert charge(L)==0
        for c in CELLS: derived(L,c)
        words+=1

print('PASS_X6_NETWORK_EVENT_LEDGER_V29')
print('exhaustive_words_checked',words)
print('closed_network_charge_invariant',True)
print('cumulative_ledger_order_blind_for_fixed_multiset',True)
print('stored_counts_nonnegative',True)
