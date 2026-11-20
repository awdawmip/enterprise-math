import time,hashlib,json
from collections import Counter,defaultdict

def slots(p):
 d=defaultdict(list)
 for i in range(p):
  for j in range(p):
   for s in (-1,1):d[(1<<i)-s*(1<<j)].append((i,j,s))
 return {0:sorted((c,tuple(v)) for c,v in d.items() if c%2==0),1:sorted((c,tuple(v)) for c,v in d.items() if c%2==1)}

def mjoin(p,k,m):
 H=1<<(p-1);low=H+1;high=2*H-1
 s=slots(p); names=[]; sts=Counter()
 for t in range(1,2*k+1):
  left=s[1-t%2];right=s[t%2] # odd m requires C parity opposite to c; t odd=>c even,C odd
  d=2*t-k*m
  assert d%2
  mod=abs(d)
  tab=defaultdict(list)
  for C,Cs in right:tab[(k*C)%mod].append((C,Cs))
  sts['bucket_entries']+=len(right)
  sts['pair_naive']+=len(left)*len(right)
  for c,cs in left:
   possible=tab[((k+2)*c)%mod]
   sts['modular_bucket_probe']+=1
   for C,Cs in possible:
    sts['joined_pairs']+=1
    N=k*C-(k+2)*c
    assert N%d==0
    b=N//d
    if not(low<=b<=high):continue
    v=m*b+C-c
    if v%4!=2:continue
    a=v//2
    if not(low<=a<=high) or a==b:continue
    assert (k*a-t*b)==c and ((k+2)*a-(t+m)*b)==C
    sts['arithmetic_pairs']+=1
    ls=[(i,j) for i,j,sgn in cs if (((t*b+(1<<i))>>j)&1)==(sgn==1)]
    rs=[(i,j) for i,j,sgn in Cs if ((((t+m)*b+(1<<i))>>j)&1)==(sgn==1)]
    sts['slot_checks']+=len(cs)+len(Cs)
    for i,j in ls:
     for I,J in rs:
      assert (((k*a)^(1<<j))-(1<<i))==t*b
      assert ((((k+2)*a)^(1<<J))-(1<<I))==(t+m)*b
      names.append((a,b,t,t+m,i,j,I,J))
 names.sort()
 hashval=hashlib.sha256(''.join(','.join(map(str,x))+'\n' for x in names).encode()).hexdigest()
 return names,dict(sts),hashval

def baseline(p,k,m):
 H=1<<(p-1);low=H+1;high=2*H-1
 s=slots(p); names=[];stats=Counter()
 for t in range(1,2*k+1):
  left=s[1-t%2];right=s[t%2]
  d=2*t-k*m
  for c,cs in left:
   for C,Cs in right:
    stats['integer_divisions']+=1
    N=k*C-(k+2)*c
    if N%d:continue
    b=N//d
    if not(low<=b<=high):continue
    a2=m*b+C-c
    if a2%4!=2:continue
    a=a2//2
    if not(low<=a<=high) or a==b:continue
    ls=[(i,j) for i,j,sgn in cs if (((t*b+(1<<i))>>j)&1)==(sgn==1)]
    rs=[(i,j) for i,j,sgn in Cs if ((((t+m)*b+(1<<i))>>j)&1)==(sgn==1)]
    for i,j in ls:
     for I,J in rs:
      names.append((a,b,t,t+m,i,j,I,J))
 names.sort()
 return names,dict(stats)

def direct_small(p,k,m):
 H=1<<(p-1);lo=H+1;hi=2*H-1;out=Counter()
 for a in range(lo,hi+1,2):
  left=defaultdict(list);right=defaultdict(list)
  for i in range(p):
   for j in range(p):
    x=((k*a)^(1<<j))-(1<<i)
    y=(((k+2)*a)^(1<<j))-(1<<i)
    if x>0:left[x].append((i,j))
    if y>0:right[y].append((i,j))
  for x,li in left.items():
   for y,ri in right.items():
    diff=y-x
    if diff<=0 or diff%m:continue
    b=diff//m
    if b!=a and lo<=b<=hi and b%2 and x%b==0:
     t=x//b
     if t>=1:
      for i,j in li:
       for I,J in ri:out[(a,b,t,t+m,i,j,I,J)]+=1
 return out

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--small',action='store_true');args=parser.parse_args()
 cases=[]
 if args.small:
  for p in range(4,8):
   H=1<<(p-1)
   for k in range(1,H-2,2):
    for m in (1,3,5):
     got,_,_=mjoin(p,k,m)
     assert Counter(got)==direct_small(p,k,m),(p,k,m)
     cases.append({'p':p,'k':k,'m':m,'count':len(got)})
 out=[]
 expected={1:(442,614,'ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71'),3:(839,1286,'1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3'),5:(3,3,'c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b')}
 for m,(np,nw,eh) in expected.items():
  ta=time.perf_counter();named,counts,sha=mjoin(19,21,m);join_elapsed=time.perf_counter()-ta
  tb=time.perf_counter();base,basestats=baseline(19,21,m);base_elapsed=time.perf_counter()-tb
  assert named==base and len(named)==nw and len(set((a,b) for a,b,*_ in named))==np and sha==eh
  out.append({'m':m,'pairs':np,'named':nw,'sha256':sha,'join_counts':counts,'baseline_counts':basestats,'elapsed_seconds_one_run':{'modular_join':round(join_elapsed,6),'baseline':round(base_elapsed,6)}})
 result={'schema':'PREFIX968_R6_MODULAR_BUCKET_QUOTIENT_JOIN_V1','source_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','model':'auxiliary named XOR k,k+2; odd k, odd m, strict odd p-bit moduli','status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED','small_cases':cases,'q19_k21':out,'perf_caveat':'Single process, one run per method in same Python program; arithmetic counts are exact; runtime comparisons not controlled benchmark.'}
 with open('PREFIX968_R6_EXACT_RESULTS.json','w') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'small_cases':len(cases),'q19':out},indent=2))
