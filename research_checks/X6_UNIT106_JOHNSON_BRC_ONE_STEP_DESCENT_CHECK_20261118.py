#!/usr/bin/env python3
"""Unit106: exact named signed-axis transition obstruction for Johnson/BRC observation.
Scientific pins P000 V5 59538f585d037d09ef687b28715c4bc1a3f9fe03;
historical Johnson fd2bcff10ca6e147348b6c1236027fc0d2877df3.
"""
import json
from collections import defaultdict
from itertools import product
from math import factorial
PAIRS=((0,5),(1,4),(2,3))
FACT=tuple(factorial(i) for i in range(9))

def ck(ok,msg):
    if not ok:raise AssertionError(msg)
def packet(x):
    t=tuple(x[i]*x[j] for i,j in PAIRS); S=sum(t)
    rho=tuple((x[i]-x[j])%2 for i,j in PAIRS)+(sum(x)%3,)
    q=tuple(sorted(S-2*a for a in t))
    l1=sum(abs(a) for a in x)
    l2=sum(a*a for a in x)
    F=1
    for a in x:F*=FACT[abs(a)]
    return rho,q,l1,l2,F

def B(x):
    n=sum(abs(a) for a in x)
    d=1
    for a in x:d*=FACT[abs(a)]
    return FACT[n]//d

def step(x,i,eps):
    a=list(x);a[i]+=eps;return tuple(a)

A=(-1,-1,-1,-1,-1,1)
C=(-1,-1,-1,-1,1,-1)
ck(packet(A)==packet(C),'pre-step packet mismatch')
ck(packet(A)==((0,0,0,2),(-1,-1,3),6,6,1),'packet expected values')
ck(B(A)==B(C)==720,'pre-step B mismatch')
ck(B(step(A,4,-1))==2520,'first following multiplicity')
ck(B(step(C,4,-1))==120,'second following multiplicity')

groups=defaultdict(list)
for x in product((-1,0,1),repeat=6):
    groups[packet(x)].append(x)
ck(len(groups)==94,'unexpected number of observation packets')
ck(all(len({B(z) for z in states})==1 for states in groups.values()),'base B not conserved')
conflicting=0
conflicting_packets=set()
for packet_key,states in groups.items():
    for i in range(6):
        for eps in (-1,1):
            m={B(step(z,i,eps)) for z in states}
            if len(m)>1:
                conflicting+=1
                conflicting_packets.add(packet_key)
ck(conflicting==1032 and len(conflicting_packets)==93,'one-step failure totals')
print(json.dumps({
  'schema':'X6_UNIT106_JOHNSON_BRC_ONE_STEP_DESCENT_V1',
  'frozen_p000':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
  'historical_johnson':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
  'base_domain':'{-1,0,1}^6',
  'base_states':729,'distinct_base_packets':len(groups),
  'base_packets_have_constant_Bmin':True,
  'tested_packet_named_signed_operations':len(groups)*12,
  'operations_with_ambiguous_next_Bmin':conflicting,
  'ambiguous_base_packets':len(conflicting_packets),
  'witness':{
    'a':list(A),'b':list(C),
    'equal_packet':{'rho_J':[0,0,0,2],'q_orbit':[-1,-1,3],'l1':6,'l2':6,'F':1},
    'before_Bmin':[720,720],
    'named_step':{'axis_zero_based':4,'direction':-1},
    'after_Bmin':[2520,120]
  },
  'scope':'finite exhaustive signed states with global explicit one-step impossibility witness',
  'original_native_R063_Helly_executed':False,
  'status':'AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED'
},sort_keys=True,separators=(',',':')))
