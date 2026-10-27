#!/usr/bin/env python3
"""Original signed 12-term ordered-hex BRC auxiliary recurrence; R347 exact corank 302..310.
Reuses byte-verified R346 K/J recurrences; rebuilds H_300..H_311,
Q_301..Q_310, verifies R346 r301 digest. Auxiliary BRC, not native X6.
"""
from math import comb
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json, time

R345_ALL='5f897213f1bc399a6f649b7a9bb3932a1d670cbae4eb7baa98a08eee96c9b384'

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

R346_ALL = '0890ffe6433ce6a8edbcca77c94fd05e854628ef2ec4ffca7143d413c6cf6515'
R346_NEW = '242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484'

def run(R=310):
    assert R>=302
    start=time.monotonic()
    Hmax=R+1
    smax=3*Hmax+2
    lim=2*Hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):
            z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
        if s%100==0:print('source_B',s,'/',smax,flush=True)

    # Only compute dependent H rows for coranks 301..R; old rows are immutable evidence.
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
        assert len(ds)==r+1 and ds[-1]==6**r and all(x>0 for x in ds),(r,'H-invariant')
        H[r]=ds

    # Evaluate L_r=5^r H_r via its exact Newton basis.
    # At most 2R+2 positive nodes suffice for every Q_r needed below.
    vals={}
    for r,ds in H.items():
        scaled=[x*5**r for x in ds]
        assert all(x.denominator==1 for x in scaled),(r,'noninteger-L')
        vals[r]=eval_newton([int(x) for x in scaled],2*R+3)

    r301_only=sha256(); combined=sha256(); new=sha256()
    all_prev=0; new_count=0; bad=[]; new_row_digests=[]; minor_spotchecks=0
    full_rows=[]
    for r in range(301,R+1):
        qvals=[vals[r][i+1]*vals[r][i+2]-vals[r-1][i+2]*vals[r+1][i+1] for i in range(2*r+1)]
        # Cross-check the Q_r normalization against raw D minors, not only H differences.
        if r>=302:
            def raw_D(q,k):
                return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))
            for k in (1,2,3):
                q=r+k
                raw_minor=raw_D(q,k)*raw_D(q+1,k+1)-raw_D(q,k+1)*raw_D(q+1,k)
                normalized=Fraction(qvals[k-1]*5**(2*k+1),5**(2*r))
                assert raw_minor==normalized,(r,k,'minor-identity')
                minor_spotchecks+=1
        ds=forward_differences(qvals)
        assert len(ds)==2*r+1
        catalan_top=30**(2*r)*comb(2*r,r)//(r+1)
        assert ds[-1]==catalan_top,(r,'Catalan_top')
        row_hash=sha256()
        for i,x in enumerate(ds):
            assert type(x) is int
            line=f'{r},{i},{x}\n'.encode()
            combined.update(line);row_hash.update(line)
            if r==301:all_prev+=1
            if r==301:r301_only.update(line)
            if r>=302:new.update(line);new_count+=1
            if x<=0:bad.append((r,i,str(x)))
        if r>=302:
            new_row_digests.append({'r':r,'coefficient_count':len(ds),'all_strictly_positive':all(x>0 for x in ds),
                                    'nonpositive_indices':[i for i,x in enumerate(ds) if x<=0],
                                    'min_index':min(range(len(ds)),key=lambda i:ds[i]),
                                    'min_decimal_digits':len(str(min(ds))),
                                    'max_decimal_digits':len(str(max(ds))),
                                    'top_matches_catalan':ds[-1]==catalan_top,
                                    'sha256':row_hash.hexdigest(),
                                    'first_coefficient':str(ds[0]),
                                    'last_coefficient':str(ds[-1])})
            full_rows.extend((r,i,str(x)) for i,x in enumerate(ds))
        if r%50==0 or r>=301:print('row_Q',r,'/',R,flush=True)

    # Compare the only recomputed previous row exactly against the published R346 SHA.
    # R345 and r<=300 are not recomputed: inherited evidence is named separately.
    assert r301_only.hexdigest()==R346_NEW,('r301_digest_changed',r301_only.hexdigest())
    assert all_prev==603 and new_count==(R-301)*(R+303), (all_prev,new_count)
    assert not bad and minor_spotchecks==3*(R-301), ('nonpositive_or_spotcheck', bad[:10])

    out={
       'schema':'R347_EXACT_BRC_TP2_CORANK310_V1',
       'author_status':'AUTHOR_SIDE_EXACT_CONDITIONAL_R330_UNREVIEWED_NOT_ADMITTED',
       'source':'R346_verify.py, byte-verified sha256 b7a0e0be716cef2f5b1c6ec49b87c74084c38d379277ab26fbd9b9e0fab486a4; only H rows 300..311 recomputed',
       'model':'original signed 12 K/J term ordered-hex BRC auxiliary recurrence B_0=1+t',
       'R_max':R,'H_max':Hmax,'s_max':smax,'degree_limit':lim-1,
       'prior_r345_digest_inherited':R345_ALL,
       'prior_r346_digest_inherited':R346_ALL,
       'r301_only_digest':r301_only.hexdigest(),
       'recomputed_prior_r301_coefficients':all_prev,
       'new_rows':[302,R],'new_coefficient_count':new_count,
       'new_sha256':new.hexdigest(),
       'rows_301_to_R_sha256':combined.hexdigest(),
       'all_new_coefficients_strictly_positive':not bad,
       'direct_original_D_minor_spotchecks':minor_spotchecks,
       'nonpositive_positions':bad,
       'row_summaries':new_row_digests,
       'R330_load_bearing_unverified_dependency':'D_(r+u,u)=5^u H_r(u), deg H_r <= r for all u >=0',
       'unbounded_licence':'Newton basis coefficients positive + R330 imply Q_r(v)>0 for all v>=0 for 1<=r<=R',
       'proof_scope':'auxiliary signed BRC combinatorial coefficients, not native X6 dynamics',
       'arithmetic':'exact integer and Fraction, no floating-point sign approximation',
       'elapsed_seconds':round(time.monotonic()-start,2)
    }
    path=Path(__file__).with_name('R347_EVIDENCE.json')
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    raw=''.join(f'{r},{i},{x}\n' for r,i,x in full_rows)
    Path(__file__).with_name('R347_ALL_NEW_COEFFICIENTS.txt').write_text(raw)
    assert sha256(raw.encode()).hexdigest()==out['new_sha256']
    print('RESULT',json.dumps({k:out[k] for k in ['R_max','s_max','H_max','prior_r345_digest_inherited','prior_r346_digest_inherited','new_coefficient_count','new_sha256','rows_301_to_R_sha256','all_new_coefficients_strictly_positive','elapsed_seconds']},ensure_ascii=False),flush=True)
    return out

if __name__=='__main__':run()

