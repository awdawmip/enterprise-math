#!/usr/bin/env python3
"""Original signed 12-term ordered-hex BRC auxiliary recurrence; extend R345 by r=301.
Independent local implementation of the R345 exact coefficient route, with
complete previous-prefix digest checks and no native X6/physical assertion.
"""
from math import comb
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json, time

R345_ALL='5f897213f1bc399a6f649b7a9bb3932a1d670cbae4eb7baa98a08eee96c9b384'
R345_NEW='5835f388f9a78bbcde8bff10a4ff5bfa85364794a8658084efb48526d5fbb136'

def C(n,k): return comb(n,k) if 0 <= k <= n else 0

def add(a,b,lim):
    z=[0]*min(lim,max(len(a),len(b)))
    for i,x in enumerate(a[:len(z)]): z[i]+=x
    for i,x in enumerate(b[:len(z)]): z[i]+=x
    return z

def mul(a,b,lim):
    z=[0]*min(lim,len(a)+len(b)-1)
    for i,x in enumerate(a[:len(z)]):
        if x:
            for j,y in enumerate(b[:len(z)-i]):
                if y: z[i+j]+=x*y
    return z

def monomial(n,coef,shift):
    return [0]*shift + [coef*C(n,j) for j in range(n+1)] if n>=0 else [0]

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=[0]
    for j,v in enumerate(ds,1):
        if v: z=add(z,monomial(i+1-j,-v,i-1),30)
    return z

def J(s):
    z=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v: z=add(z,monomial(n,v,s),30)
    return z

def forward_differences(values):
    a=list(values);d=[]
    while a:
        d.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return d

def eval_newton(d,count):
    d=list(d);ans=[]
    for _ in range(count):
        ans.append(d[0])
        for j in range(len(d)-1):d[j]+=d[j+1]
    return ans

def run(R=301):
    start=time.monotonic(); Hmax=R+1; smax=3*Hmax+2; lim=2*Hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1): z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
        if s%100==0:print('B_source',s,'of',smax,'sec',round(time.monotonic()-start,1),flush=True)
    H=[]
    for r in range(Hmax+1):
        v=[]
        for u in range(r+2):
            q=r+u
            D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
            v.append(Fraction(D,5**u))
        ds=forward_differences(v)
        assert ds[-1]==0,(r,'degree-exception')
        ds=ds[:-1]
        assert len(ds)==r+1 and ds[-1]==6**r and all(x>0 for x in ds)
        H.append(ds)
        if r%50==0 or r>=300:print('H',r,'sec',round(time.monotonic()-start,1),flush=True)
    vals=[]
    for r,ds in enumerate(H):
        scaled=[x*5**r for x in ds]
        assert all(x.denominator==1 for x in scaled),(r,'noninteger-L')
        vals.append(eval_newton([int(x) for x in scaled],2*R+3))
    prior=sha256();old_new=sha256();new=sha256();allsha=sha256()
    old_count=0;new_count=0; bad=[]; R301=None
    for r in range(1,R+1):
        v=[vals[r][i+1]*vals[r][i+2]-vals[r-1][i+2]*vals[r+1][i+1] for i in range(2*r+1)]
        ds=forward_differences(v)
        top=30**(2*r)*comb(2*r,r)//(r+1)
        assert ds[-1]==top,(r,'Catalan')
        for i,x in enumerate(ds):
            line=f'{r},{i},{x}\n'.encode();allsha.update(line)
            if r<=300:
                prior.update(line);old_count+=1
                if r>=256:old_new.update(line)
            else:
                new.update(line);new_count+=1
            if x<=0:bad.append((r,i,str(x)))
        if r==301:
            R301={'r':r,'num_coefficients':len(ds),'all_positive':all(x>0 for x in ds),
                  'negative_or_zero_positions':[(i,str(x)) for i,x in enumerate(ds) if x<=0],
                  'min_coefficient_index':min(range(len(ds)),key=lambda i: ds[i]),
                  'min_coefficient':str(min(ds)),
                  'constant':str(ds[0]),'highest':str(ds[-1]),
                  'sha256':sha256(''.join(f'{r},{i},{x}\n' for i,x in enumerate(ds)).encode()).hexdigest(),
                  'first_values':[str(x) for x in ds[:8]],'last_values':[str(x) for x in ds[-8:]]}
        if r%50==0 or r>=300:print('Q',r,'sec',round(time.monotonic()-start,1),flush=True)
    assert prior.hexdigest()==R345_ALL,('prior-mismatch',prior.hexdigest())
    assert old_new.hexdigest()==R345_NEW,('prior-r256_300-mismatch',old_new.hexdigest())
    assert old_count==90600 and new_count==603
    result={'schema':'R346_EXACT_BRC_TP2_R301_V1','status':'EXACT_INTEGER_FRACTION_RECOMPUTATION',
            'source':'R345_VERIFY.py at GitHub commit 5e043110d76e7a61fa561cc4776ea16870439a15',
            'source_model':'12 signed K/J recurrence, B_0=1+t, no signed-tail erasure',
            's_max':smax,'degree_limit':lim-1,'H_max':Hmax,'H_newton_positive_through':Hmax,
            'R330_dependency':'Assume D_{r+u,u}=5^u H_r(u) and deg H_r<=r for all nonnegative integers',
            'H_r_plus_one_finite_check_through':Hmax,
            'r345_digest_recomputed':prior.hexdigest(),'r345_new_digest_recomputed':old_new.hexdigest(),
            'r345_verified_coefficient_count':old_count,'new_r301_coefficient_count':new_count,
            'r301':R301,'new_digest':new.hexdigest(),'all_digest':allsha.hexdigest(),
            'violations':bad[:30],'violations_count':len(bad),
            'arithmetic':'Python integers, fractions only, no floating-point sign comparison',
            'scientific_licence':'BRC auxiliary combinatorial model only; no native X6 physical dynamics conclusion',
            'elapsed_seconds':round(time.monotonic()-start,2)}
    out=Path(__file__).with_name('R346_EVIDENCE.json');out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('RESULT',json.dumps({k:result[k] for k in ['s_max','H_max','r345_digest_recomputed','r345_verified_coefficient_count','new_r301_coefficient_count','r301','violations_count','elapsed_seconds']},ensure_ascii=False),flush=True)
    return result

if __name__=='__main__':run()
