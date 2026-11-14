#!/usr/bin/env python3
"""R5 universal one-swap recourse for cut 27 (K214-291) and cut 25 (K223-291).
Frozen scientific input 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Exact integer DAG, enumerate all globally-optimal local path patterns.
Running Python standard library: python VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py > OUT.json
"""
import json
from collections import Counter
from fractions import Fraction
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF=10**15

def frozen():
 p={3:set(),12:set(),15:set()};n=k=mask=0
 for t in range(1,1<<15):
  bit=t&-t;i=bit.bit_length()-1;mask^=bit;sgn=1 if mask&bit else -1
  n+=sgn*W[i];k+=sgn*K0[i]
  if n>=3 and k%36==0 and k//36 in p:p[k//36].add(n)
 e=Counter(Fraction(v,q) for q,vals in p.items() for v in vals)
 x=[0]
 for v in sorted(e):x.append(x[-1]+e[v])
 cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
 assert len(x)==954 and len(cuts)==28
 return x,cuts

def close(x,cuts,mask):
 active={cuts[i] for i in range(len(cuts)) if mask>>i&1};out=[];shift=0
 for j,v in enumerate(x):
  out.append(v-shift)
  if j in active:shift+=1
 return out

def graph(z):
 n=len(z);inc=[[] for _ in z];out=[[] for _ in z];pref=[INF]*n;tail=[INF]*n
 for j in range(n):
  if z[j]-z[0]<=2:pref[j]=sum(z[j]-z[t] for t in range(j))
  if z[-1]-z[j]<=2:tail[j]=sum(z[t]-z[j] for t in range(j+1,n))
  for i in range(j-1,-1,-1):
   if z[j]-z[i]>7:break
   mid=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
   if max(mid,default=0)<=2:
    w=sum(mid);inc[j].append((i,w));out[i].append((j,w))
 return inc,out,pref,tail

def paths_dp(z,max_k=291):
 inc,out,pref,tail=graph(z);n=len(z)
 C=[pref]
 for m in range(1,max_k):
  prior=C[-1];C.append([min((prior[i]+w for i,w in inc[j]),default=INF) for j in range(n)])
 D=[tail]
 for m in range(1,max_k):
  prior=D[-1];D.append([min((w+prior[q] for q,w in out[j]),default=INF) for j in range(n)])
 J=[min(C[k-1][j]+tail[j] for j in range(n)) for k in range(1,max_k+1)]
 return out,C,D,J

def patterns(dp,k,i,rad=9):
 out,C,D,J=dp;l=i-rad;r=i+rad;best=J[k-1]
 pats=set();seen=set();nodes=set()
 def walk(t,j,P):
  nodes.add((t,j))
  if t>=k:return
  for q,w in out[j]:
   if C[t][q]!=C[t-1][j]+w or C[t][q]+D[k-t-1][q]!=best:continue
   if q>r:pats.add(P)
   else:walk(t+1,q,P+(q,))
 for t in range(1,k):
  for j in range(max(0,l-7),l):
   if C[t-1][j]+D[k-t][j]==best:
    seen.add((t,j));walk(t,j,())
 return pats,len(seen),len(nodes)

def repair(P,new,old,i):
 chosen=set(P);events=range(i-6,i+8)
 def cost(z,S):
  ds=[min((abs(z[t]-z[j]) for j in S),default=INF) for t in events]
  return max(ds),sum(ds)
 orig=cost(new,chosen)
 if orig[0]>2:return -1,None
 if cost(old,chosen)==orig:return 0,None
 for p in chosen:
  if not i-4<=p<=i+5:continue
  for q in range(i-4,i+6):
   if q in chosen:continue
   T=(chosen-{p})|{q}
   if cost(old,T)==orig:return 1,(p,q)
 return 2,None


def main():
    x,cuts=frozen()
    intervals=[(214,221,[3,8,9,10,27],[27]),
               (222,222,[27],[27]),
               (223,291,[25,27],[25,27])]
    records=[]; total_patterns=0
    for lo,hi,bits,measured in intervals:
        z={mask:close(x,cuts,sum((1<<bit) for j,bit in enumerate(bits) if mask>>j&1))
           for mask in range(1<<len(bits))}
        for mask in range(1,1<<len(bits)):
            if not any(mask>>bits.index(bit)&1 for bit in measured):continue
            dp=paths_dp(z[mask],hi)
            for bit in measured:
                flag=1<<bits.index(bit)
                if not mask&flag:continue
                for K in range(lo,hi+1):
                    pats,starts,nodes=patterns(dp,K,cuts[bit])
                    assert pats and starts and nodes
                    old=mask^flag
                    categories=Counter();swap_types=Counter()
                    for p in pats:
                        count,swap=repair(p,z[mask],z[old],cuts[bit])
                        assert count in (0,1), (K,bit,mask,p,count)
                        categories[count]+=1
                        if swap:swap_types[f'{swap[0]}->{swap[1]}']+=1
                    assert categories[1]>0, (K,bit,mask)
                    total_patterns+=len(pats)
                    records.append({'K':K,'cut':bit,'new_mask':mask,'old_mask':old,
                                    'patterns':len(pats),'already_old':categories[0],
                                    'one_swap':categories[1],'start_states':starts,
                                    'visited_states':nodes,'swap_types':dict(sorted(swap_types.items()))})
    assert len(records)==405, len(records)
    assert total_patterns==sum(row['patterns'] for row in records)
    counts=Counter(r['cut'] for r in records)
    assert counts==Counter({27:267,25:138}), counts
    assert all(r['one_swap']>0 for r in records)
    print(json.dumps({'status':'PASS_EXACT_R5_LOW_BUDGET_ONE_SWAP','scientific_input_commit':
      '435e77af0d180eac32bd1f9c4c464bc4010b7551',
      'model':'954-event derived indexed-center one-dimensional radius-2 observer',
      'cut_positions':{'25':cuts[25],'27':cuts[27]},'budget_scope':[214,291],
      'R_27_K214_to_291':1,'R_25_K223_to_291':1,
      'transitions':len(records),'total_patterns':total_patterns,
      'records':records,'independent_review':'NOT_REVIEWED'},
      ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__': main()
