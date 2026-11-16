#!/usr/bin/env python3
"""R421 signed BRC auxiliary Turan exact integer certificates.
Extends R420 r420_dual_boundary.py at immutable d4659e227a1a1a5fd0f35db5476ba1b87ec915c2.
No native X6 physics execution or floating point sign check.
"""
import argparse,hashlib,json,time
from math import comb
from pathlib import Path

def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        if c:
            for j,v in enumerate(b):out[i+j]+=c*v
    return out

def poly_prod(*seq):
    result=[1]
    for a in seq:result=poly_mul(result,a)
    return result

def horizontal(h,m):
    n=m-h;q0=3+h;L=n+1
    pre=[[1]]
    for d in range(L):pre.append(poly_mul(pre[-1],[q0-d,1]))
    suf=[None]*(L+1);suf[L]=[1]
    for d in range(L-1,-1,-1):suf[d]=poly_mul([q0+d+1,1],suf[d+1])
    atoms=[poly_mul(pre[d],suf[d]) for d in range(L+1)]
    N=[0]*(L+1)
    for k in range(n+1):
        d1=abs(n-2*k);d2=abs(n-2*k-1);co=comb(n,k)
        if co:
            for j in range(L+1):N[j]+=co*(atoms[d1][j]-atoms[d2][j])
    return N,suf[0]

def certificate(m,save_full=False):
    Nm,Qm=horizontal(-1,m);N0,Q0=horizontal(0,m);Np,Qp=horizontal(1,m)
    f1=poly_prod([4,1],[4,1],[m+6,2]);f2=poly_prod([3,1],[3,1],[m+7,2])
    a=poly_prod(f1,N0,N0,Qm,Qp)
    b=poly_prod(f2,Nm,Np,Q0,Q0)
    P=[(m+1)*u-m*v for u,v in zip(a,b)]
    while len(P)>1 and P[-1]==0:P.pop()
    B=poly_prod(f1,Q0,Q0,Qm,Qp)
    count_neg=sum(z<=0 for z in P)
    assert count_neg==0,(m,count_neg)
    assert len(P)==4*m+6,(m,len(P),4*m+6)
    assert all(z>0 for z in B)
    obj={'m':m,'degree':len(P)-1,'coefficient_count':len(P),'nonpositive':count_neg,
         'coeff_digest_sha256':hashlib.sha256(','.join(map(str,P)).encode()).hexdigest(),
         'minimum_coefficient':str(min(P)),
         'constant_term':str(P[0]),'leading_term':str(P[-1]),
         'denominator_degree':len(B)-1}
    if save_full:obj.update({'coefficients':[str(z) for z in P],
        'N':[[str(x) for x in Ns] for Ns in (Nm,N0,Np)],
        'Q':[[str(x) for x in Qs] for Qs in (Qm,Q0,Qp)]})
    return obj

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--low',type=int,default=193)
    ap.add_argument('--high',type=int,default=256)
    ap.add_argument('--full',action='store_true')
    ns=ap.parse_args();rows=[];start=time.monotonic()
    for m in range(ns.low,ns.high+1):
        result=certificate(m,save_full=ns.full);rows.append(result)
        print('R421_CERT',m,'deg',result['degree'],'positive',result['coefficient_count'],
              'elapsed',round(time.monotonic()-start,2),flush=True)
    raw={'schema':'R421_DUAL_BRC_EXACT_V1','author_side':'UNREVIEWED_NOT_ADMITTED',
         'm_range':[ns.low,ns.high],'s_lower':3,
         'source':['R420@d4659e227a1a1a5fd0f35db5476ba1b87ec915c2',
                   'GLOBAL@d310c5f090bd5883e89df4c5827468959073541b',
                   'EM_MAIN@e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66'],
         'rows':rows}
    target=Path(__file__).with_name(f'R421_EVIDENCE_{ns.low}_{ns.high}.json')
    target.write_text(json.dumps(raw,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print('R421_EXACT_PASS',ns.low,ns.high,'bands',len(rows),
          'positive_coefficients',sum(r['coefficient_count'] for r in rows),
          'sha256',hashlib.sha256(target.read_bytes()).hexdigest(),
          'size',target.stat().st_size,flush=True)
if __name__=='__main__':main()
