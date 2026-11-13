#!/usr/bin/env python3
"""Exact phase endpoint benchmark for PREFIX-606 positive 16D kernel.
Measures optimized native48, positive16 stepwise, and two batch variants.
All output comparisons use exact Python integers.
"""
import json,runpy,time,random,statistics
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name('PREFIX606_R2_positive16_exact_checker.py')))
Q=m['Q'];N=m['N'];g=m['g'];phases=m['phases']
E,R00,Ra,Rb,T0,H=[m[k] for k in ('E','R00','Ra','Rb','T0','H')]

def sparse_rows(mat):
 return [[(j,int(mat[i,j])) for j in range(mat.cols) if mat[i,j]] for i in range(mat.rows)]
Erows=sparse_rows(E)
Rs=[sparse_rows(a) for a in (R00,Ra,Rb)]
Trows=sparse_rows(T0); assert all(len(x)==1 for x in Trows)
P=[None]*16;C=[None]*16
for i,row in enumerate(Trows):
 j,w=row[0];P[j]=i;C[j]=w
assert C[0]==3 and H[15,0]==1

def native_step(v,z):
 u=[0]*48
 for i,js in enumerate(N):
  if abs(phases[i][2]) in (5,6):continue
  if i==g:u[i]=sum(v[j] for j in js)
  else:u[i]=sum(((3+z) if j==g else 2)*v[j] for j in js)
 return u

def first2(v,b,a):
 out=[]
 for i in range(16):
  out.append(sum(w*v[j] for j,w in Rs[0][i])
          + a*sum(w*v[j] for j,w in Rs[1][i])
          + b*sum(w*v[j] for j,w in Rs[2][i]))
 return out

def output(u):
 return [sum(w*u[j] for j,w in row) for row in Erows]

def native(v,word):
 for z in word: v=native_step(v,z)
 return v

def tail_iter(v,word):
 u=first2(v,word[0],word[1])
 for z in word[2:]:
  u=[(w+(z if i==15 else 0))*u[j] for i,row in enumerate(Trows) for j,w in row]
 return output(u)

def class_transfer(word):
 """Make O(n+16) exact positive 16D monomial transfer from gates suffix."""
 m=len(word)
 residue_products=[1]*4
 for t,z in enumerate(word):residue_products[t%4]*=(z+3)
 out=[]
 for j in range(16):
  here=j
  cyc=[]
  for _ in range(4):cyc.append(here);here=P[here]
  assert here==j
  base=1
  for v in cyc:base*= 1 if v==0 else C[v]
  factor=pow(base,m//4)
  for v in cyc[:m%4]:factor*=1 if v==0 else C[v]
  if 0 in cyc:
   first=cyc.index(0)
   factor*=residue_products[first]
  target=j
  for _ in range(m%4):target=P[target]
  out.append((target,j,factor))
 return out

def tail_fast(v,word,transfer=None):
 u=first2(v,word[0],word[1]); new=[0]*16
 for i,j,factor in (transfer if transfer is not None else class_transfer(word[2:])):
  new[i]=factor*u[j]
 return output(new)

rng=random.Random(606)
lengths=(16,64,256)
counts=(1,20,100)
results=[]
for n in lengths:
 word=[rng.randrange(0,10) for _ in range(n)]
 data=[[rng.randrange(0,100) for _ in range(48)] for _ in range(max(counts))]
 tr=class_transfer(word[2:])
 assert len(tr)==16
 for count in counts:
  subset=data[:count]
  outn=[native(v,word) for v in subset]
  outi=[tail_iter(v,word) for v in subset]
  outf=[tail_fast(v,word,tr) for v in subset]
  assert outn==outi==outf, (n,count)
  timing={}
  for label,call in [('native48',lambda:[native(v,word) for v in subset]),
                     ('positive16_step',lambda:[tail_iter(v,word) for v in subset]),
                     ('positive16_batch_reused_transfer',lambda:[tail_fast(v,word,tr) for v in subset]),
                     ('positive16_batch_including_transfer',lambda:(lambda transfer:[tail_fast(v,word,transfer) for v in subset])(class_transfer(word[2:])))]:
   samples=[]
   for _ in range(5):
    t0=time.perf_counter_ns();ans=call();samples.append((time.perf_counter_ns()-t0)/1e6)
    assert ans==outn
   timing[label]=round(statistics.median(samples),4)
  results.append({'depth':n,'batch_size':count,'bit_length':max(abs(x).bit_length() for x in outn[-1]),
                  'timings_ms_5run_median':timing,'all_equal':True})
  print('depth',n,'batch',count,'bits',results[-1]['bit_length'],timing,flush=True)

# Also test gate-class transfer itself vs slow exact tail operator on random 16D states.
for n in (0,1,2,3,4,7,15,63):
 w=[rng.randrange(0,12) for _ in range(n)]
 tr=class_transfer(w)
 v=[rng.randrange(1,12) for _ in range(16)]
 end=[0]*16
 for i,j,f in tr:end[i]=f*v[j]
 for z in w:
  v=[(weight+(z if i==15 else 0))*v[j] for i,row in enumerate(Trows) for j,weight in row]
 assert end==v

ans={
 'schema':'PREFIX606B_R2_POSITIVE16_BATCH_EXACT_BENCH_V1',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'native_phase_model':'Q native-derived, 48 phases, fixed axes (1,1,1,1,0,0), variable gate >=0',
 'host':'Python integer / SymPy matrices only for precomputation, pure-Python integer timing; five run median',
 'comparison':'complete 48-phase endpoint output for every 48-phase input; randomized deterministic nonnegative inputs and gate words',
 'data':results,
 'cost_scope':'times exclude native STAR reconstruction and precomputation of six fixed factor matrices; two batch timings respectively exclude and include one shared gate-word transfer construction. Both include two-step input encoding and all 48 phase output coordinates per query.',
 'transfer_reuse':'O(n) four residue-class gate products and O(16) monomial transfer weights for each shared gate sequence',
 'status':'EXECUTED_EXACT_INTEGER_EXPERIMENT; independent performance review pending'}
Path(__file__).with_name('PREFIX606B_R2_positive16_batch_results.json').write_text(json.dumps(ans,indent=2)+'\n')
