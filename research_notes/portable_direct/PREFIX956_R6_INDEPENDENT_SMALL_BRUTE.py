#!/usr/bin/env python3
"""Independent direct-XOR validator for PREFIX956 two-core dyadic sieve."""
from collections import Counter
import json
checked=Counter(); sample=[]
for p in range(4,8):
 H=1<<(p-1)
 Q=list(range(H+1,2*H,2))
 for k in range(1,H-1,2):
  for a in Q:
   channels=[]
   for core in (k,k+2):
    ka=core*a
    witness=[]
    for i in range(p):
     for j in range(p):
      n=(ka^(1<<j))-(1<<i)
      if n>0:
       witness.append((n,i,j,(1<<i)-(1-2*((ka>>j)&1))*(1<<j)))
    channels.append(witness)
   for b in Q:
    A=[(n//b,i,j,c) for n,i,j,c in channels[0] if n%b==0]
    B=[(n//b,i,j,C) for n,i,j,C in channels[1] if n%b==0]
    for t,i,j,c in A:
     for T,I,J,C in B:
      m=T-t;delta=C-c
      checked['joint_witness_combinations']+=1
      assert delta==2*a-m*b
      if m&1:
       assert delta&1
       assert (c&1)==(1-(t&1)) and (C&1)==(t&1)
      else:
       assert delta%4==(0 if (m&2) else 2)
      d=2*t-k*m
      if d:
       na=t*C-T*c
       nb=k*C-(k+2)*c
       assert na==d*a and nb==d*b
       vd=(abs(d)&-abs(d)).bit_length()-1
       assert na%(1<<(vd+1))==(1<<vd)
       assert nb%(1<<(vd+1))==(1<<vd)
      if m>=5:
       assert a>b
      if m==0:
       assert a<1.5*H
      checked['p'+str(p)]+=1
      if len(sample)<10:sample.append({'p':p,'k':k,'a':a,'b':b,'t':t,'T':T,'i':i,'j':j,'I':I,'J':J,'m':m})
res={'tested_p':[4,5,6,7],'odd_adjacent_k_range':'1<=k<=2^(p-1)-3, k odd','all_moduli_Q_p':True,'joint_witness_count':checked['joint_witness_combinations'],'counts_by_p':{str(p):checked['p'+str(p)] for p in range(4,8)},'sample':sample}
open('PREFIX956_R6_SMALL_BRUTE_RESULTS.json','w').write(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='sample'},indent=2))
