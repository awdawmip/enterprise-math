#!/usr/bin/env python3
"""R357: exact signed twelve-term BRC Newton Q337 full certificate.

Uses archived immutable R346_verify.py for K/J polynomial arithmetic, not
an independent implementation of that engine.  Author-side computational
certificate only; the all-index inference depends on unreviewed R348 A1-A5.
"""
import sys, time, json
from pathlib import Path
from fractions import Fraction
from math import comb
from hashlib import sha256
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences,eval_newton
OLD_Q336='b00f2a797802649c9b07d31fdf5301c17e0a4e002892c6939a723da72ca20736'

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def run():
    start=time.monotonic(); rtarget=337; hmax=rtarget+1
    smax=3*hmax+2; lim=2*hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    assert [K(i)[0] for i in range(1,13)]==[2]+[0]*11
    assert [K(i)[1] if len(K(i))>1 else 0 for i in range(1,13)]==[3,-1]+[0]*10
    assert [K(i)[2] if len(K(i))>2 else 0 for i in range(1,13)]==[0,4,-8]+[0]*9
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    print('B_SOURCE',smax,'elapsed',round(time.monotonic()-start,3),flush=True)
    L={}; htop={}; hextra={}
    for r in range(rtarget-2,rtarget+2):
        vals=[Fraction(D(B,r+u,u),5**u) for u in range(r+2)]
        dif=forward_differences(vals)
        assert dif[-1]==0,('degree',r)
        dif=dif[:-1]
        assert all(x>0 for x in dif),('H_nonpositive',r)
        assert dif[-1]==6**r,('H_leading',r)
        scaled=[5**r*x for x in dif]
        assert all(x.denominator==1 for x in scaled)
        L[r]=eval_newton([int(x) for x in scaled],2*rtarget+3)
        htop[r]=str(dif[-1]);hextra[r]='0'
        print('H',r,'elapsed',round(time.monotonic()-start,3),flush=True)
    summaries=[]; complete=''
    for r in (rtarget-1,rtarget):
        vals=[L[r][u+1]*L[r][u+2]-L[r-1][u+2]*L[r+1][u+1] for u in range(2*r+1)]
        dif=forward_differences(vals)
        assert len(dif)==2*r+1
        assert all(isinstance(x,int) for x in dif)
        assert all(x>0 for x in dif),('nonpositive_Q',r)
        assert dif[-1]==30**(2*r)*comb(2*r,r)//(r+1),('Catalan',r)
        content=''.join(f'{r},{j},{x}\n' for j,x in enumerate(dif))
        sha=sha256(content.encode()).hexdigest()
        if r==336: assert sha==OLD_Q336,(sha,OLD_Q336)
        if r==337:
            assert Fraction(dif[-2], dif[-1])==Fraction(17*r+11,10),('next_to_top',r)
            assert Fraction(dif[-3], dif[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1)),('third_to_top',r)
            complete=content
            (BASE/'R357_Q337_FULL_COEFFICIENTS.txt').write_text(content)
            for k in range(1,9):
                q=r+k
                minor=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                expected=Fraction(vals[k-1]*5**(2*k+1),5**(2*r))
                assert Fraction(minor)==expected,('direct_minor',r,k)
                assert minor>0
        summaries.append({'r':r,'coefficients':len(dif),'sha256':sha,
                          'all_strict_positive':True,'negative_count':0,'zero_count':0,
                          'min_coefficient_index':min(range(len(dif)),key=lambda i:dif[i]),
                          'first_digits':len(str(dif[0])),'last_digits':len(str(dif[-1])),
                          'catalan_top':True})
        print('Q',r,sha,'elapsed',round(time.monotonic()-start,3),flush=True)
    evidence={'schema':'R357_BRC_CORANK337_V1','run_date':'2026-10-28',
              'classification':'AUTHOR_SIDE_EXACT_UNREVIEWED_NOT_ADMITTED',
              'scope':'signed twelve-term BRC auxiliary combinatorial recurrence',
              'direct_native_X6_transfer':False,'R348_A1_A5_extraction_independent_review':'PENDING',
              'smax':smax,'coefficient_t_range':[0,lim-1],'h_range':[rtarget-2,rtarget+1],
              'h_leading_verified':htop,'h_extra_degree_zero':hextra,
              'q336_regression':summaries[0],'q337_new':summaries[1],
              'top3_universal_ratios_r337_exact_recheck':True,
              'direct_D_minor_checks':8,'new_q337_coefficient_file':'R357_Q337_FULL_COEFFICIENTS.txt',
              'new_q337_file_sha256':sha256(complete.encode()).hexdigest(),
              'exact_integer_and_fraction':True,'float_sign_checks':False,
              'method':'R346 K/J signed recurrence + R351 D/H/Q Newton extraction',
              'elapsed_seconds':round(time.monotonic()-start,3)}
    (BASE/'R357_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print('RESULT',json.dumps(evidence,ensure_ascii=False),flush=True)
if __name__=='__main__':run()
