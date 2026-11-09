#!/usr/bin/env python3
"""PREFIX619 reproducible exact X6-BRC 48/8/4 algorithm experiment.
Frozen source: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
No trigonometry, matrix exponential or non-BRC science surrogate.
"""
from fractions import Fraction as F
from statistics import median
from time import perf_counter_ns
import json,platform,sys
from pathlib import Path
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
PH=tuple((a,p,s*c) for a in range(4) for c in STAR[a] for s in(-1,1) for p in near(a,s*c))
I={p:i for i,p in enumerate(PH)}
def succ(i):
 a,p,c=PH[i]; b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
 return [I[x] for x in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
E=[(i,j) for i in range(48) if abs(PH[i][2]) not in(5,6) for j in succ(i)]
assert len(PH)==48 and I[(0,1,-3)]==4 and len(E)==96
HC=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB=({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})
def out(c,w):
 y=[F(0)]*48
 for j,inds in enumerate(HC):
  for i in inds:y[i]+=c[j]
 for j,inds in enumerate(HB):
  for i,k in inds.items():y[i]+=k*w[j]
 return y
def Qstep(x,g):
 y=[F(0)]*48
 for i,j in E:y[i]+=(F(1) if i==4 else (g+3 if j==4 else F(2)))*x[j]
 return y
def initial():
 a,b,lam=F(1),F(2),F(3,2)
 d=[F(0)]*48
 for i in(4,11,14,32):d[i]=lam
 c=[lam*v for v in(0,0,4,4)]
 w=[lam*v for v in(b+3,a+3,F(1),F(1,2))]
 x=Qstep(Qstep(d,a),b)
 assert x==out(c,w)
 return x,c,w
def native(word):
 x,_,_=initial()
 for g in word:x=Qstep(x,g)
 return x
def eight(word):
 _,c,w=initial()
 for g in word:
  c=[2*c[3],2*c[0],2*c[1],2*c[2]]
  w=[4*(g+3)*w[3],w[0],w[1],w[2]]
 return out(c,w)
def products(word):
 _,c,w=initial()
 f=[F(1)]*4
 for t,g in enumerate(word,1):f[t%4]*=4*(g+3)
 n=len(word)
 return out([2**n*c[(j-n)%4] for j in range(4)],
            [w[(j-n)%4]*f[(n-j)%4] for j in range(4)])
def gates(n,kind):
 if kind=='integers':return [F((13*j*j+7*j+3)%11) for j in range(n)]
 if kind=='rationals':return [F((11*j*j+5*j+1)%7,(3*j+1)%5+1) for j in range(n)]
 return [F(0)]*n
def timed(fn,word,r):
 clocks=[];last=None
 for _ in range(r):
  t=perf_counter_ns();last=fn(word);clocks.append(perf_counter_ns()-t)
 return int(median(clocks)),last
def main():
 cases=[]
 for kind in ('integers','rationals','zero'):
  for n in (0,4,16,64,256,1024):
   if kind=='rationals' and n==1024:continue
   word=gates(n,kind);r=3 if n>=256 else 5
   ts={};os={}
   for name,fn in (('native48',native),('positive8',eight),('four_products',products)):
    ts[name],os[name]=timed(fn,word,r)
   assert os['native48']==os['positive8']==os['four_products']
   x=os['native48']
   assert sum(bool(v) for v in x)==14
   cases.append({'kind':kind,'n':n,'repetitions':r,'median_ns':ts,
    'output_max_bits':max(max(v.numerator.bit_length(),v.denominator.bit_length()) for v in x),
    'exact_48_component_equality':True,'nonzero_phases':14})
 for n in (4,16,64,256):assert (16**(n//4)).bit_length()==n+1
 data={'schema':'PREFIX619_R2_EXACT_COST_V1','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'probe':[4,11,14,32],'calibration':{'a':'1','b':'2','lambda':'3/2'},
  'native_nonzero_entries':96,'reconstruction_H_nonzero_entries':24,
  'eight_state_transition_nonzero_entries':8,'case_count':len(cases),
  'environment':{'python':sys.version.split()[0],'platform':platform.platform()},
  'cases':cases,'status':'AUTHOR_SIDE_EXACT_CHECKS_PASS; INDEPENDENT_REVIEW_PENDING'}
 Path(__file__).with_name('PREFIX619_R2_exact_cost_results.json').write_text(json.dumps(data,indent=2)+'\n')
 print('PASS',len(cases),'exact cases; 48 phase outputs all equal')
if __name__=='__main__':main()
