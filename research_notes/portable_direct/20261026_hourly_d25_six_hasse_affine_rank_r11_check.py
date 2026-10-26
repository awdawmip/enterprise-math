#!/usr/bin/env python3
"""p-local affine-(j,ell) Hasse-jet no-go checker; imports prior exact carrier.

Run next to 20261026_hourly_d25_six_hasse_cellwise_rank_r11_check.py.
Author-only, no native CM/Frobenius or independent review.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import importlib.util

prev = Path(__file__).with_name('20261026_hourly_d25_six_hasse_cellwise_rank_r11_check.py')
spec = importlib.util.spec_from_file_location('six_hasse_base',prev)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def det(a):
    x=[list(map(F,row)) for row in a]
    d=F(1)
    for k in range(len(x)):
        s=next((r for r in range(k,len(x)) if x[r][k]),None)
        assert s is not None
        if s!=k:
            x[k],x[s]=x[s],x[k]
            d=-d
        v=x[k][k]
        d*=v
        for r in range(k+1,len(x)):
            scale=x[r][k]/v
            for c in range(k+1,len(x)):
                x[r][c]-=scale*x[k][c]
            x[r][k]=F(0)
    return d


def augmented(row, idx):
    return list(row)+[idx*x for x in row]


def main():
    lo=[base.rational_low(j) for j in range(1,8)]
    hi=[base.rational_high(e) for e in range(1,8)]
    minor=lambda rows,inds:det([augmented(rows[j-1],j) for j in inds])
    LM1=minor(lo,[1,2,3,4,5,6]); LM2=minor(lo,[1,2,3,4,5,7])
    HM1=minor(hi,[1,2,3,4,5,6]); HM2=minor(hi,[1,2,3,4,5,7])
    assert LM1==F(6115090146751187,4933357406401147831073850100442726400)
    assert LM2==F(4067311166086063,1233339351600286957768462525110681600)
    assert HM1==F(365171593153733456612202247837761463284375552,
                   1317843520492196161221934377615738727453060628857421875)
    assert HM2==F(1623108928803144044357925191458383972711122628476928,
                   2270677331896066290689423480991358220869809790037059326171875)
    assert gcd(LM1.numerator,LM2.numerator)==49
    assert gcd(HM1.numerator,HM2.numerator)==2**13*3**51
    ps=[19]+[p for p in base.primes(997) if p>=31]+[8221]
    for p in ps:
        M=6 if p==19 else 7
        u=base.jets_mod_p(p)
        for j in range(1,M+1):
            assert [u[a][j] for a in range(3)] == [base.modfrac(v,p) for v in lo[j-1]],(p,j,'low')
            assert [u[b][p-j] for b in range(2,5)] == [base.modfrac(v,p) for v in hi[j-1]],(p,j,'high')
        if p==19:
            assert base.modfrac(LM1,p)*base.modfrac(HM1,p)%p!=0
        else:
            assert base.modfrac(LM1,p)!=0 or base.modfrac(LM2,p)!=0, p
            assert base.modfrac(HM1,p)!=0 or base.modfrac(HM2,p)!=0, p
        mat=[]
        for j in range(1,M+1):
            for ell in range(1,M+1):
                ports=[u[a][j]*u[b][p-ell]%p for a,b in base.PAIRS]
                mat.append(ports+[j*x%p for x in ports]+[ell*x%p for x in ports])
        assert base.rank_mod(mat,p)==18,(p,'affine-source-rank')
    p=13;u=base.jets_mod_p(p)
    rows=[]
    for j in range(1,5):
        for ell in range(1,5):
            ports=[u[a][j]*u[b][p-ell]%p for a,b in base.PAIRS]
            rows.append(ports+[j*x%p for x in ports]+[ell*x%p for x in ports])
    assert base.rank_mod(rows,p)==14
    assert base.modfrac(LM1,37)==0 and base.modfrac(LM2,37)!=0
    assert base.modfrac(HM1,109)==0 and base.modfrac(HM2,109)!=0
    print('PASS exact rational affine minors and gcd certificates')
    print('PASS',len(ps),'primes >=19 through 997 and 8221; 18 independent affine port columns')
    print('p=13 small 4x4 window affine rank=14, not covered')
    print('123456 minor exception p37 (low) and p109 (high); row7 repairs')


if __name__=='__main__':
    main()
