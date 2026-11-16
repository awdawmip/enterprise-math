#!/usr/bin/env python3
"""R419: exact signed BRC auxiliary Turan positive coefficient certificates.
Only integer polynomial arithmetic and Python stdlib. Doesn't claim native X6 transfer.
"""
import json,hashlib,sys
from math import comb
from pathlib import Path
LOW,HIGH=129,256

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if not v: continue
        for j,w in enumerate(b):out[i+j]+=v*w
    return out
def scale(a,n):return [n*x for x in a]
def sub(a,b):return add(a,scale(b,-1))
def horner(a,x):
    v=0
    for z in reversed(a):v=v*x+z
    return v
def cat(n):return comb(2*n,n)//(n+1)

def delta_raw(r,q):
    # Original signed coefficient [t^r](1-t)(1+t)^(2q)(1+t^2)^(r-q)
    acc=0
    for i in range(2*q+1):
        for bit in (0,1):
            d=r-i-bit
            if d>=0 and d%2==0 and d//2<=r-q:
                acc+=(-1 if bit else 1)*comb(2*q,i)*comb(r-q,d//2)
    return acc

def row_cert(s,eps,raw_check=True):
    assert s>=2 and eps in (0,1)
    r0=s+1+((s+1-eps)&1)
    m0=(r0-eps)//2; b0=m0-1+eps
    dmax=(s-1+eps)//2
    assert b0>=dmax
    numfac=[[b0-a+1,1] for a in range(dmax)]
    denfac=[[2*(2*(b0-a)-1),4] for a in range(dmax)]
    prefix=[[1]]
    for f in numfac: prefix.append(mul(prefix[-1],f))
    suffix=[None]*(dmax+1);suffix[dmax]=[1]
    for d in range(dmax-1,-1,-1):suffix[d]=mul(denfac[d],suffix[d+1])
    T=suffix[0]
    atoms=[mul(prefix[d],suffix[d]) for d in range(dmax+1)]
    N={}
    for q in (s-1,s,s+1):
        res=[0]*(dmax+1)
        for d in range(dmax+1):
            j=q-2+eps-2*d
            if 0<=j<q:
                weight=comb(q-1,j)*(1 << (q-1-j))
                atom=atoms[d]
                assert len(atom)==dmax+1
                for k,v in enumerate(atom):res[k]+=weight*v
        N[q]=res
    Ln=scale(mul([r0+s+1,2],[r0-s,2]),2*s*(2*s-1))
    Ld=scale(mul([r0+s,2],[r0-s+1,2]),(2*s+2)*(2*s+1))
    A=sub(mul(Ld,mul(N[s],N[s])),mul(Ln,mul(N[s-1],N[s+1])))
    B=mul(Ld,mul(T,T))
    assert len(A)==len(B)==2*dmax+3
    if not all(v>0 for v in A):
        bad=[i for i,v in enumerate(A) if v<=0]
        raise ValueError(('nonpositive numerator',s,eps,bad))
    assert all(v>0 for v in B)
    if raw_check:
        hs=[comb(r0+q,2*q)*delta_raw(r0,q) for q in (s-1,s,s+1)]
        D=hs[1]*hs[1]-hs[0]*hs[2]
        assert D>0 and B[0]*D==A[0]*(comb(r0+s,2*s)*cat(b0))**2
    digest=lambda a:hashlib.sha256(','.join(map(str,a)).encode()).hexdigest()
    return {'s':s,'epsilon':eps,'r0':r0,'b0':b0,'dmax':dmax,'A_degree':len(A)-1,'B_degree':len(B)-1,
            'A_coefficients_ascending':[str(v) for v in A],
            'B_coefficients_ascending':[str(v) for v in B],
            'A_sha256':digest(A),'B_sha256':digest(B),
            'positive_numerator_coefficients':len(A),
            'positive_denominator_coefficients':len(B),
            'boundary_crosscheck':raw_check}

def main():
    lo=int(sys.argv[1]) if len(sys.argv)>1 else LOW
    hi=int(sys.argv[2]) if len(sys.argv)>2 else HIGH
    rows=[]
    for s in range(lo,hi+1):
        for eps in (0,1):rows.append(row_cert(s,eps))
        if s%16==0:print('PROGRESS',s,flush=True)
    total=sum(row['positive_numerator_coefficients'] for row in rows)
    assert total==sum(2*s+4 for s in range(lo,hi+1))
    obj={'schema':'EM_R419_SIGNED_AUX_INTERVAL_CERT_V1','range':[lo,hi],
         'source':'R418 raw Catalan kernel polynomial method, exact integer reimplementation with prefix/suffix factoring',
         'proof_scope':'each fixed s within range and every integer r>=s+1; signed auxiliary combinatorial model only',
         'rows':rows}
    root=Path(__file__).resolve().parent
    path=root/f'R419_FULL_EVIDENCE_{lo}_{hi}.json'
    path.write_text(json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    summary={'schema':'EM_R419_PUBLISHABLE_SUMMARY_V1','s_min':lo,'s_max':hi,
             'bands':hi-lo+1,'parity_cases':len(rows),
             'positive_numerator_coefficients':total,'positive_denominator_coefficients':total,
             'boundary_raw_checks':len(rows),'raw_evidence_sha256':sha,'raw_evidence_bytes':path.stat().st_size,
             'case_digests':[{'s':r['s'],'epsilon':r['epsilon'],'r0':r['r0'],'degree':r['A_degree'],
                 'A_sha256':r['A_sha256'],'B_sha256':r['B_sha256']} for r in rows]}
    spath=root/f'R419_EVIDENCE_SUMMARY_{lo}_{hi}.json'
    spath.write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print('R419_EXACT_PASS',lo,hi,'bands',hi-lo+1,'parity_cases',len(rows),'A_positive',total,'B_positive',total,'raw_boundary_checks',len(rows))
    print('RAW_SHA256',sha)
    print('SUMMARY_SHA256',hashlib.sha256(spath.read_bytes()).hexdigest())
if __name__=='__main__':main()

