#!/usr/bin/env python3
"""Independent signed-coefficient and polynomial check of R421 full JSON evidence.
No imports from the generator; infinite s conclusion is from the exact polynomial
identity + complete P coefficients, not just finite point checks.
"""
import sys,json,hashlib
from math import comb
from pathlib import Path

def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0

def signed_delta(r,q):
    n=r-q
    return sum(comb(n,k)*(choose(2*q,r-2*k)-choose(2*q,r-2*k-1))
               for k in range(n+1))

def polyeval(coefficients,x):
    value=0
    for a in reversed(coefficients):value=value*x+int(a)
    return value

def main():
    cnt={'bands':0,'strict_positive_p_coefficients':0,'direct_delta':0,
         'turan_cross_products':0,'leading_coefficient_checks':0}
    all_m=[]
    for filename in sys.argv[1:]:
        data=json.loads(Path(filename).read_text())
        assert data['schema']=='R421_DUAL_BRC_EXACT_V1'
        lo,hi=data['m_range'];assert len(data['rows'])==hi-lo+1
        for row in data['rows']:
            m=row['m'];all_m.append(m);A=row['coefficients']
            assert len(A)==4*m+6 and row['degree']==4*m+5
            assert int(A[-1])==2**(2*m+1)
            cnt['leading_coefficient_checks']+=1
            assert row['nonpositive']==0 and all(int(c)>0 for c in A)
            assert hashlib.sha256(','.join(A).encode()).hexdigest()==row['coeff_digest_sha256']
            cnt['bands']+=1;cnt['strict_positive_p_coefficients']+=len(A)
            for s in (3,5,17,257,1024):
                r=s+m;vals=[]
                for h in (-1,0,1):
                    q=s+h;d=signed_delta(r,q)
                    vals.append(comb(r+q,2*q)*d)
                    assert d*polyeval(row['Q'][h+1],s-3)==comb(2*q,q)*polyeval(row['N'][h+1],s-3),(m,s,h)
                    cnt['direct_delta']+=1
                D=vals[1]**2-vals[0]*vals[2]
                W=comb(r+s,2*s)*comb(2*s,s)
                Qm,Q0,Qp=[polyeval(z,s-3) for z in row['Q']]
                den=(m+1)*(s+1)**2*(2*s+m)*Q0**2*Qm*Qp
                assert D*den==W*W*polyeval(A,s-3),(m,s)
                assert D>0,(m,s)
                cnt['turan_cross_products']+=1
        print('R421_VERIFIED',filename,'rows',len(data['rows']),
              'file_sha256',hashlib.sha256(Path(filename).read_bytes()).hexdigest(),flush=True)
    assert all_m==list(range(193,257)),(len(all_m),all_m[:3],all_m[-3:])
    print('R421_INDEPENDENT_PASS',json.dumps(cnt,sort_keys=True),flush=True)
if __name__=='__main__':main()
