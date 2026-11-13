#!/usr/bin/env python3
"""R348: original signed twelve-term BRC K/J recurrence, new coranks 311..320.
Recomputes the R346 corank-301 and R347 corank-302..310 exact digests;
all claims concern only the auxiliary combinatorial model, not native X6.
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

def run(R=320):
    """Compute exactly the 10 NEW coranks 311..320; regress canonical R346 and R347."""
    assert R == 320
    start=time.monotonic()
    Hmax=R+1
    smax=3*Hmax+2
    lim=2*Hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1): z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    print('RECURSION B:',smax+1,'source-polynomials', 'seconds:',round(time.monotonic()-start,1),flush=True)
    # H_{r} is reconstructed from original signed recurrence at r+2 nodes,
    # so the finite degree test cannot silently use the lower-degree interpolation itself.
    H={}
    for r in range(300,Hmax+1):
        values=[]
        for u in range(r+2):
            q=r+u
            D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
            values.append(Fraction(D,5**u))
        ds=forward_differences(values)
        assert ds[-1]==0,(r,'finite-degree-check-failed')
        ds=ds[:-1]
        assert len(ds)==r+1 and ds[-1]==6**r and all(x>0 for x in ds),(r,'H-Newton-coefficients')
        H[r]=ds
    print('RECONSTRUCTED H:',len(H),'rows', 'seconds:',round(time.monotonic()-start,1),flush=True)
    vals={}
    for r,ds in H.items():
        scaled=[x*5**r for x in ds]
        assert all(x.denominator==1 for x in scaled),(r,'noninteger-L')
        vals[r]=eval_newton([int(x) for x in scaled],2*R+3)

    prior301=sha256(); prior302_310=sha256(); new311_320=sha256()
    all_301_320=sha256(); rows=[]; issues=[]; tests=0
    coeff_text=[]
    def raw_D(q,k):
        return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
    for r in range(301,R+1):
        qvals=[vals[r][i+1]*vals[r][i+2]-vals[r-1][i+2]*vals[r+1][i+1] for i in range(2*r+1)]
        ds=forward_differences(qvals)
        top=30**(2*r)*comb(2*r,r)//(r+1)
        assert ds[-1]==top,(r,'Catalan-check-failed')
        row_digest=sha256()
        for i,x in enumerate(ds):
            assert isinstance(x,int)
            line=f'{r},{i},{x}\n'.encode()
            row_digest.update(line); all_301_320.update(line)
            if r==301:prior301.update(line)
            elif 302<=r<=310:prior302_310.update(line)
            else:new311_320.update(line);coeff_text.append(line)
            if x<=0:issues.append((r,i,str(x)))
        if r>=311:
            for k in (1,2,3,4):
                q=r+k
                minor=raw_D(q,k)*raw_D(q+1,k+1)-raw_D(q,k+1)*raw_D(q+1,k)
                assert Fraction(minor)==Fraction(qvals[k-1]*5**(2*k+1),5**(2*r)),(r,k,'D-minor-normalization')
                tests+=1
            rows.append({'r':r,'count':len(ds),'nonpositive_count':sum(x<=0 for x in ds),
                         'min_index':min(range(len(ds)),key=lambda i:ds[i]),
                         'min_digits':len(str(min(ds))),
                         'first_digits':len(str(ds[0])), 'last_digits':len(str(ds[-1])),
                         'max_digits':len(str(max(ds))),
                         'sha256':row_digest.hexdigest(),
                         'highest_Catalan_exact':ds[-1]==top})
        print('Q',r,'computed','seconds',round(time.monotonic()-start,1),flush=True)
    assert prior301.hexdigest()=='242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484'
    assert prior302_310.hexdigest()=='912d07072d1e38d98b668ef03d615733104394392d077d3dc13a0e286c64a002'
    assert len(coeff_text)==6320
    assert tests==40 and not issues
    result={'schema':'R348_AUTHOR_SIDE_EXACT_TP2_CORANK320_V1',
            'model':'12 signed K/J ordered-hex BRC auxiliary recurrence B0=1+t',
            'R_max':R,'s_max':smax,'H_range':[300,Hmax],
            'finite_extra_degree_checks':len(H),'new_r_range':[311,R],
            'new_coefficient_count':len(coeff_text),'new_coefficient_nonpositive':len(issues),
            'new_coefficients_sha256':new311_320.hexdigest(),
            'prior_r301_digest_recomputed':prior301.hexdigest(),
            'prior_r302_310_digest_recomputed':prior302_310.hexdigest(),
            'raw_D_minor_identity_checks':tests,'Catalan_checks':10,
            'rows':rows,
            'R330_global_lemma':'Author-side universal algebraic proof supplied separately in R348_PROOF.zh-CN.md; independent review pending',
            'theorem_status':'AUTHOR_SIDE_PROVED_WITH_R348_R330_LEMMA_NOT_INDEPENDENTLY_REVIEWED',
            'arithmetic':'exact Python integers and Fraction, no floating point sign decisions',
            'elapsed_seconds':round(time.monotonic()-start,3)}
    loc=Path(__file__).parent
    (loc/'R348_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    (loc/'R348_NEW_COEFFICIENTS.txt').write_bytes(b''.join(coeff_text))
    print('RESULT',json.dumps({k:v for k,v in result.items() if k!='rows'},ensure_ascii=False),flush=True)
    return result

if __name__=='__main__':run()
