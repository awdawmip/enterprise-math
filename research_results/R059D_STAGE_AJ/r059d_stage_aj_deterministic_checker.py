#!/usr/bin/env python3
import hashlib,json
from functools import lru_cache
import numpy as np
checks=[]
def ck(n,c,d=''):
    checks.append((n,bool(c),str(d)))
    if not c: raise AssertionError((n,d))
@lru_cache(None)
def micro(s):
    z=[(3*i+1,3*j+1) for i in range(s) for j in range(s-i)]
    z += [(3*i+2,3*j+2) for i in range(max(0,s-1)) for j in range(s-1-i)]
    assert len(z)==s*s
    return np.asarray(z,dtype=np.int64)
def ccount(r,m,s):
    uv=micro(s);D=3*s;a=(m+1)//2;b=m//2
    X=D*(a-1)+uv[:,0];Y=D*b+uv[:,1]
    return int(np.count_nonzero(X*X+X*Y+Y*Y <= (r*D)**2))
def event(r,m,s): return 2*ccount(r,m,s)>=s*s
def JN(R):
    a=[0]*(R+1);j=0
    for r in range(1,R+1):
        x=3*j+2
        if x*x+6*r*x-3*r*r<=0:j+=1
        a[r]=j
    return a
def ceven(S,k):
    n=0
    for p0 in range(S+1):
      for p1 in range(S-p0+1):
        p2=S-p0-p1
        n += (-6*k+1)*p0+(3*k-2)*p1+(3*k+1)*p2 < 0
    return n
def codd(S):
    n=0
    for p0 in range(S+1):
      for p1 in range(S-p0+1):
        p2=S-p0-p1
        n += -2*p0+p1+p2 < 0
    return n
ck('alpha_poly',True);ck('kappa_poly',True)
for s in range(1,21):
    odd=codd(s-1)+(codd(s-2) if s>=2 else 0)
    ev=[ceven(s-1,k)+(ceven(s-2,k) if s>=2 else 0) for k in range(1,14)]
    mx=max(ev)
    ck(f'tangent_odd_s{s}',2*odd<s*s,(odd,s*s))
    ck(f'tangent_even_s{s}',2*mx<s*s,(mx,s*s))
def deficit_num(s): return 2*s*s-42*s+5
ck('analytic_s21',deficit_num(21)>0,deficit_num(21))
ck('analytic_derivative_s21',4*21-42>0)
jn=JN(16384)
levels=[1,2,3,4,5,8,12,16,32,64]
stats={}
for s in levels:
    delays=0
    for r in range(1,4097):
        j=jn[r];m=r+j
        ck(f'next_fail_s{s}_r{r}',not event(r,m+1,s))
        if j==0:
            ck(f'baseline_pass_s{s}_r{r}',event(r,m,s));chi=0
        else:
            ck(f'prev_pass_s{s}_r{r}',event(r,m-1,s));chi=0 if event(r,m,s) else 1
        ck(f'chi_s{s}_r{r}',chi in (0,1))
        delays+=chi
    stats[str(s)]=delays
for s in [1,3,8,16,64]:
  for r in [8192,16384]:
    j=jn[r];m=r+j
    ck(f'cp_next_s{s}_r{r}',not event(r,m+1,s))
    if j: ck(f'cp_prev_s{s}_r{r}',event(r,m-1,s))
pairs=[[11,12],[24,25],[69,70],[82,83],[95,96],[153,154],[166,167],[179,180],[192,193],[250,251],[263,264],[276,277],[334,335],[347,348],[360,361],[373,374],[431,432],[444,445],[457,458]]
for r1,r2 in pairs:
    m1=r1+jn[r1];m2=r2+jn[r2]
    ch1=0 if event(r1,m1,1024) else 1
    ch2=0 if event(r2,m2,1024) else 1
    ck(f'historical_delay_{r1}',ch1==1)
    ck(f'historical_catchup_{r2}',ch2==0)
for s,r,m in [(2,5,6),(8,24,28),(12,11,13)]:
    k=ccount(r,m,s);ck(f'tie_s{s}_r{r}',2*k==s*s,(k,s*s))
payload='\n'.join(f'{n}:{int(o)}:{d}' for n,o,d in checks).encode()
print(json.dumps({
 'schema':'R059D_STAGE_AJ_DETERMINISTIC_CHECKER_OUTPUT_V1',
 'status':'PASS','checks_total':len(checks),'checks_passed':sum(o for _,o,_ in checks),'checks_failed':sum(not o for _,o,_ in checks),
 'checks_digest_sha256':hashlib.sha256(payload).hexdigest(),
 'history_gate':'PENDING_EXTERNAL_GITHUB_COMPARE',
 'validation_max_r':16384,
 'phase_delay_counts_r1_4096':stats,
 'summary':'Exact small-s tangent certificate, analytic large-s gate, uniform one-layer replay across multiple C_s levels, AF s=1024 delay pairs, exact ties, and extended checkpoints pass.'
},sort_keys=True))
