#!/usr/bin/env python3
"""Exact Unit107: named-axis BRC update and raw-coordinate subset repair bound."""
import json
from itertools import product, combinations
from math import factorial
P=((0,5),(1,4),(2,3))

def packet(z):
 t=[z[i]*z[j] for i,j in P];s=sum(t)
 f=1
 for a in z:f*=factorial(abs(a))
 return (tuple((z[i]-z[j])%2 for i,j in P)+(sum(z)%3,),
         tuple(sorted(s-2*v for v in t)),sum(map(abs,z)),
         sum(v*v for v in z),f)

def B(z):
 n=sum(map(abs,z));f=1
 for v in z:f*=factorial(abs(v))
 return factorial(n)//f

def move(z,i,d):
 y=list(z);y[i]+=d;return tuple(y)

def after(z,i,d):
 n=sum(map(abs,z));b=B(z);a=abs(z[i]);v=abs(z[i]+d)
 num,den=(b*(n+1),a+1) if v==a+1 else (b*a,n)
 assert den>0 and num%den==0
 return num//den

checks=0
for z in product(range(-2,3),repeat=6):
 for i in range(6):
  for d in (-1,1):
   if after(z,i,d)!=B(move(z,i,d)):raise AssertionError(('recurrence',z,i,d))
   checks+=1
assert checks==187500

states=list(product((-1,0,1),repeat=6))
future={z:tuple(B(move(z,i,d)) for i in range(6) for d in (-1,1)) for z in states}
counts=[]
for n in range(7):
 good=0
 for S in combinations(range(6),n):
  seen={};ok=True
  for z in states:
   key=(packet(z),tuple(z[i] for i in S))
   if key in seen and seen[key]!=future[z]:ok=False;break
   seen[key]=future[z]
  good+=ok
 counts.append((n,good))
assert counts==[(0,0),(1,0),(2,0),(3,0),(4,0),(5,6),(6,1)]

witness=[]
for j in range(6):
 partner=next(v if u==j else u for u,v in P if j in (u,v))
 k=next(i for i in range(6) if i not in (j,partner))
 x=[0]*6;y=[0]*6;x[k]=y[k]=1;x[j]=3;y[j]=-3
 x=tuple(x);y=tuple(y)
 assert packet(x)==packet(y) and B(x)==B(y)==4
 assert (B(move(x,j,1)),B(move(y,j,1)))==(5,3)
 witness.append({'missing_axis':j,'other_axis':k,'plus':x,'minus':y,'next_B':[5,3]})

print(json.dumps({'schema':'X6_UNIT107_EXACT_COORDINATE_SUBSET_BOUND_V1',
 'scientific_pins':['59538f585d037d09ef687b28715c4bc1a3f9fe03',
                    'fd2bcff10ca6e147348b6c1236027fc0d2877df3'],
 'recurrence_checked_states':15625,'recurrence_checked_edges':checks,
 'cube_states':729,'sufficient_coordinate_subsets_by_size':counts,
 'global_missing_axis_witnesses':witness,
 'scope':'coordinate-subset supplements to P=(rho_J,q_orbit,L1,L2,F)',
 'native_R063_Helly_executed':False,
 'status':'AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED'},
 sort_keys=True,separators=(',',':')))
