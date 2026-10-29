#!/usr/bin/env python3
"""Independent exact signed BRC K/J-to-Newton-to-interior-TP2 certificate.

Reconstructs the signed 12-term source recurrence from scratch. All calculations
are arbitrary precision integers/Fraction. The statement valid for all k>=1
also needs R330's separate exact extraction/degree lemma (author-side).
"""
import argparse, hashlib, json, time
from fractions import Fraction
from math import comb
from pathlib import Path

R344_PRIOR_DIGEST = '6b3f762cada37f8b00a51541a2568d93633911d6839fe0fee9bcf2ebf85aa795'
R331_PRIOR_DIGEST = '81c190fa50e22dc8479cb337a374706ae300a877fc9c74aa7a9033c49d96cf09'

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def add(a,b,lim):
    z=[0]*min(lim,max(len(a),len(b)))
    for i,x in enumerate(a[:len(z)]):z[i]+=x
    for i,x in enumerate(b[:len(z)]):z[i]+=x
    return z

def mul(a,b,lim):
    z=[0]*min(lim,len(a)+len(b)-1)
    for i,x in enumerate(a[:len(z)]):
        if x:
            for j,y in enumerate(b[:len(z)-i]):
                if y:z[i+j]+=x*y
    return z

def monomial(n,coeff,shift):return ([0]*shift+[coeff*C(n,j) for j in range(n+1)]) if n>=0 else [0]

def K(i):
    d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2), -C(9,i-3))
    z=[0]
    for j,v in enumerate(d,1):
        if v:z=add(z,monomial(i+1-j,-v,i-1),30)
    return z

def J(s):
    z=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:z=add(z,monomial(n,v,s),30)
    return z

def differences(values):
    arr=list(values);out=[]
    while arr:
        out.append(arr[0]);arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    return out

def newton_values(coeffs,count):
    d=list(coeffs);out=[]
    for _ in range(count):
        out.append(d[0]);
        for j in range(len(d)-1):d[j]+=d[j+1]
    return out

def run(max_r, prior, r332, out):
    assert max_r>=256
    t=time.monotonic(); Hmax=max_r+1; smax=3*Hmax+2; qlimit=2*Hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(kk[i],B[s-i],qlimit),qlimit)
        B.append(z)
    print('SOURCE_DONE',smax,'seconds',round(time.monotonic()-t,2),flush=True)
    def H(r):
        values=[]
        for u in range(r+2):
            q=r+u
            D=sum((-1)**(u-v)*C(u,v)*2**(q-v)*B[q+v][q] for v in range(u+1))
            values.append(Fraction(D,5**u))
        ds=differences(values)
        assert ds[-1]==0, ('out of sample degree check',r)
        ds=ds[:-1]
        assert len(ds)==r+1 and ds[-1]==6**r and all(x>0 for x in ds), ('H source issue',r)
        return ds
    cs=[]
    for r in range(Hmax+1):
        cs.append(H(r))
        if r in (0,1,17,255,256,257,300,Hmax):print('H',r,'seconds',round(time.monotonic()-t,2),flush=True)
    if prior:
        old=json.loads(Path(prior).read_text())
        assert len(old['cases'])==257
        for r in range(257):
            assert [Fraction(x) for x in old['cases'][r]['newton_coefficients']]==cs[r],('R331 full case mismatch',r)
        inp=hashlib.sha256()
        for r in range(257):
            for i,v in enumerate(cs[r]):inp.update(f'{r},{i},{v.numerator}/{v.denominator}\n'.encode())
        assert inp.hexdigest()==R331_PRIOR_DIGEST
        print('R331 FULL_INPUT 33153 coefficients PASS',flush=True)
    if r332:
        earlier332=json.loads(Path(r332).read_text())
        checked=0
        for entry in earlier332['cases']:
            r=entry['r']
            if r>max_r:continue
            assert cs[r][0]==Fraction(entry['H_0'])
            assert cs[r][1]==Fraction(entry['DeltaH_0'])
            assert cs[r][-1]==Fraction(entry['Delta^rH_0'])
            assert Fraction(entry['last_extra_difference'])==0
            assert entry['min_coefficient_positive'] is True
            checked+=1
        assert checked==min(max_r,300)-256
        print('R332 prior summary',checked,'bands PASS',flush=True)
    # Integer Newton coefficients of L_r(v)=5^r H_r(v).
    vs=[]; need=2*max_r+3
    for r,co in enumerate(cs):
        scaled=[v*5**r for v in co]
        assert all(x.denominator==1 for x in scaled), ('nonintegral L coefficient',r)
        vs.append(newton_values([int(x) for x in scaled],need))
    dig_all=hashlib.sha256();dig_previous=hashlib.sha256();dig_new=hashlib.sha256()
    count_new=count_all=0; per_band=[]; samples={}
    for r in range(1,max_r+1):
        qv=[vs[r][v+1]*vs[r][v+2]-vs[r-1][v+2]*vs[r+1][v+1] for v in range(2*r+1)]
        ds=differences(qv)
        expected=30**(2*r)*(C(2*r,r)//(r+1))
        assert ds[-1]==expected,('Catalan check',r)
        bad=[i for i,x in enumerate(ds) if x<=0]
        if bad:
            print('NONPOSITIVE Q NEWTON',r, bad[:10],flush=True)
            raise AssertionError(('Q positive cone fails',r,bad[:10],str(ds[bad[0]])[:120]))
        rowhash=hashlib.sha256()
        for i,v in enumerate(ds):
            line=f'{r},{i},{v}\n'.encode()
            dig_all.update(line);rowhash.update(line);count_all+=1
            if r<=255: dig_previous.update(line)
            else:dig_new.update(line);count_new+=1
        per_band.append({'r':r,'positive':len(ds),'sha256':rowhash.hexdigest()})
        if r in (1,2,255,256,257,300,max_r):
            samples[str(r)]={'Q_r_0':str(ds[0]),'Delta_2r_Q_r_0':str(ds[-1])}
        if r%25==0:print('Q',r,'seconds',round(time.monotonic()-t,2),flush=True)
    assert dig_previous.hexdigest()==R344_PRIOR_DIGEST
    assert count_all==max_r*(max_r+2)
    assert count_new==(max_r+1)**2-256**2
    data={
        'schema':'R345_EXACT_BRC_INTERIOR_TP2_CORANK_EXTENSION_V1',
        'status':'EXACT_INTEGER_FRACTION_PASS',
        'model':'Original signed 12-term K/J ordered hexagonal BRC auxiliary model',
        'B_s_range':[0,smax],
        'source_coefficients_retained_degrees':[0,qlimit-1],
        'H_r_interval':[0,Hmax],
        'H_every_out_of_sample_r_plus_one_forward_difference_zero':True,
        'H_newton_all_strictly_positive_and_top_6_power':True,
        'R331_full_input_crosscheck': bool(prior),
        'R332_full_summary_257_300_crosscheck': bool(r332),
        'R344_prior_r_1_through_255_digest':dig_previous.hexdigest(),
        'new_corank_strips':[256,max_r],
        'total_corank_strips':[1,max_r],
        'new_Q_forward_differences_positive':count_new,
        'total_Q_forward_differences_positive':count_all,
        'all_newton_coefficients_positive':True,
        'catalan_top_coefficient_equalities':max_r,
        'new_coefficient_digest':dig_new.hexdigest(),
        'total_coefficient_digest':dig_all.hexdigest(),
        'canonical_digest_lines':'r,i,exact_decimal_Delta^i_Q_r(0) + newline',
        'per_r_sha256':per_band,
        'samples':samples,
        'infinite_scope':'All k>=1 and 1<=q-k<=max_r, conditional on R330 exact rational extraction and deg(H_r)<=r',
        'nonadjacent_scope':'All legal 1<=k<l<=q<p with p-k<=max_r+1',
        'proof_arithmetic':'Python int/Fraction; no floating point sign inference',
        'not_claimed':['Unbounded in both r and k','native X6 dynamics','independent Driver review','Source CLAIM or Result'],
    }
    Path(out).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('PASS',max_r,count_new,count_all,dig_new.hexdigest(),'seconds',round(time.monotonic()-t,2),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-r',type=int,default=300)
    parser.add_argument('--prior',help='optional full R331 artifact for all-33153-coefficient independent crosscheck')
    parser.add_argument('--r332',help='optional R332 summary for 44 band checks')
    parser.add_argument('--out',required=True)
    a=parser.parse_args()
    run(a.max_r,a.prior,a.r332,a.out)
