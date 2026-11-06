#!/usr/bin/env python3
"""PREFIX-535 exact rooted parity minimality certificate.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor PREFIX-534: Delta(t)P_s(t) polynomial of t-degree <=22.
Pure Python 3 stdlib; no floating-point/trigonometry.
"""
from collections import Counter,defaultdict
from json import dump

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(j,c):return tuple((-1 if c>0 else 1)*x for x in STARS[j] if x!=abs(c))
PHASES=tuple((j,p,sg*x) for j in range(4) for x in STARS[j] for sg in (-1,1) for p in near(j,sg*x))
INDEX={x:i for i,x in enumerate(PHASES)}
assert len(INDEX)==48
def successors(s):
 j,p,c=s;k=next(k for k in range(4) if k!=j and abs(c) in STARS[k])
 return tuple(INDEX[x] for x in ([(j,c,d) for d in near(j,c) if d!=p]+[(k,c,d) for d in near(k,c)]))
NEXT=tuple(successors(s) for s in PHASES)
assert all(len(row)==3 for row in NEXT)
T=INDEX[(0,1,-3)]
sig=lambda i:(1 if PHASES[i][2]>0 else -1) if abs(PHASES[i][2])==1 else 0
flag=lambda i:int(abs(PHASES[i][2])==1)
BACK=[]
for i in range(48):
 weights=Counter()
 for mid in NEXT[i]:
  if T in NEXT[mid]:weights[flag(i)+2*flag(mid)+flag(T)]+=1
 BACK.append(weights)
assert sum(map(lambda x:sum(x.values()),BACK))==9

def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def mul(a,b,p):
 r=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%p
 return trim(r)
def sub(a,b,p):
 return trim([((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])
def rem(a,b,p):
 a=trim(a[:]);b=trim(b[:]);inv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  sh=len(a)-len(b);c=a[-1]*inv%p
  for i in range(len(b)):a[i+sh]=(a[i+sh]-c*b[i])%p
  trim(a)
 return a
def gcd(a,b,p):
 a=trim(a[:]);b=trim(b[:])
 while b!=[0]:a,b=b,rem(a,b,p)
 inv=pow(a[-1],-1,p)
 return [x*inv%p for x in a]

def denominator(q,z,p):
 E=[1,-4,-(192+480*q),-(2304+8064*q+2304*q*q),-(82944*q+62208*q*q),-746496*q*q]
 D1=[1,8,-48*q]
 D2=[1,0,16*(4+2*q),-64*(12*q+4*q*q),2304*q*q]
 F=mul([x%p for x in D1],[x%p for x in D2],p)
 K=[0,0,20*q,160*q*q+368*q,2560*q*q+5120*q,
 -27648*q**3+16384*q*q+27648*q,
 -73728*q**4-774144*q**3-485376*q*q+147456*q,
 -1400832*q**4-9732096*q**3-3833856*q*q,
 7077888*q**5-8847360*q**4-58392576*q**3-31850496*q*q,
 127401984*q**5+445906944*q**4-191102976*q**3,
 573308928*q**5+5733089280*q**4,-20639121408*q**5]
 d=sub(mul([x%p for x in E],F,p),[((z-1)*x)%p for x in K],p)
 assert len(d)==12 and d[0]==1 and d[-1]!=0
 return d

def evaluate(v,z,mod):
 d=denominator(v*v,z,mod)
 vp={k:pow(v,k,mod) for k in range(-2,5)}
 R=[([vp[-abs(sig(i)-initial)] for i in range(48)],0) for initial in (-1,0,1)]
 seq=[[] for _ in range(48)]
 for depth in range(23):
  for i in range(48):seq[i].append(R[sig(i)+1][0][i])
  if depth==22:break
  nr=[]
  for row,g in R:
   f=[]
   for i in range(48):
    x=sum(2*vp[flag(i)+flag(j)]*row[j] for j in NEXT[i])
    x+=sum(n*vp[k]*g for k,n in BACK[i].items())
    f.append(x%mod)
   nr.append((f,(z-1)*row[T]%mod))
  R=nr
 out=[]
 for i in range(48):
  n=[sum(d[j]*seq[i][depth-2*j] for j in range(depth//2+1))%mod for depth in range(23)]
  even=trim(n[::2]);odd=trim(n[1::2])
  ge=gcd(even,d,mod);go=gcd(odd,d,mod)
  assert ge==[1] and go==[1],PHASES[i]
  out.append({'root':list(PHASES[i]),'even_deg':len(even)-1,'odd_deg':len(odd)-1,
              'even_gcd_deg':len(ge)-1,'odd_gcd_deg':len(go)-1,
              'even_coefficients':even,'odd_coefficients':odd})
 assert Counter(x['even_deg'] for x in out)==Counter({10:45,11:3})
 assert Counter(x['odd_deg'] for x in out)==Counter({10:48})
 assert [x['root'] for x in out if x['even_deg']==11]==[[0,-6,1],[1,-4,1],[1,-5,1]]
 return d,seq,out

def independent_dp(v,z,mod,seq):
 comparisons=0;maxkeys=0;sample=[]
 for root in range(48):
  dp={(root,False,0,0):1}
  for depth in range(8):
   weighted=0;total=0
   for (end,prior_inner,k,h),count in dp.items():
    correction=abs(sig(end)-sig(root))
    assert k>=correction and (k-correction)%2==0
    weighted+=count*v**(k-correction)*z**h
    total+=count
   assert total==6**depth
   assert weighted%mod==seq[root][depth]
   comparisons+=1;maxkeys=max(maxkeys,len(dp))
   if root==0:sample.append(str(weighted))
   if depth==7:break
   nxt=defaultdict(int)
   for (end,prior_inner,k,h),count in dp.items():
    for dest in NEXT[end]:
     kk=k+flag(end)+flag(dest)
     for inner in (False,True):
      hit=int(prior_inner and inner and dest==T)
      nxt[(dest,inner,kk,h+hit)]+=count
   dp=nxt
 return {'roots':48,'depths':'0..7','root_depth_comparisons':comparisons,
         'max_state_keys_per_root':maxkeys,
         'first_root':list(PHASES[0]),'weighted_counts':sample}

results=[]
for p,v,z in ((1000000007,2,3),(998244353,3,2)):
 d,seq,out=evaluate(v,z,p)
 result={'modulus':p,'v':v,'q':v*v,'z':z,'denominator_u_degree':len(d)-1,
    'denominator_coefficients_ascending_u':d,
    'all_48_even_gcd_one':all(x['even_gcd_deg']==0 for x in out),
    'all_48_odd_gcd_one':all(x['odd_gcd_deg']==0 for x in out),
    'even_numerator_degrees':dict(Counter(x['even_deg'] for x in out)),
    'odd_numerator_degrees':dict(Counter(x['odd_deg'] for x in out)),
    'special_even_roots':[x['root'] for x in out if x['even_deg']==11],
    'example_first_root':out[0]}
 if p==1000000007:result['independent_native_forward_dp']=independent_dp(v,z,p,seq)
 results.append(result)

out={'status':'ALL_CHECKS_PASS','line':'PREFIX-535',
     'science_pin':'enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'prior_all_length_identity':'PREFIX-534: D(t^2)P_s polynomial of t-degree <=22',
     'theorem':'For all 48 roots the even/odd series each have generic minimal eventual recurrence order 11 over Q(q,z)',
     'specializations':results,'unreviewed':True,
     'next_question':'Benchmark parity-11 exact coefficient production versus 49-linear/51-deterministic native systems with endpoint BRC and provenance costs.'}
with open('PREFIX535_EXACT_EXECUTION.json','w',encoding='utf-8') as fh:
 dump(out,fh,indent=2,ensure_ascii=False)
print('ALL_CHECKS_PASS, 48 roots, 96 parity gcd tests per prime, 2 primes, 384 independent native comparisons')
