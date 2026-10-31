#!/usr/bin/env python3
"""R418: exact certificate for 98 infinite signed auxiliary Turan bands, 31 <= s <= 128.

Run: python r418_interval_certificate.py
Output: R418_INTERVAL_EVIDENCE.json, R418_INTERVAL_MANIFEST.json
Pure standard library; no floating point is used in any model computation.
"""
from math import comb
import hashlib, json
from pathlib import Path
LOW,HIGH=31,128

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out
def product(items):
    v=[1]
    for item in items:v=mul(v,item)
    return v
def scale(a,n):return [n*x for x in a]
def sub(a,b):return add(a,scale(b,-1))
def horner(a,x):
    v=0
    for z in reversed(a):v=v*x+z
    return v
def cat(n):return comb(2*n,n)//(n+1)

def coefficient_raw(r,q):
    # [t^r](1-t)(1+t)^(2q)(1+t^2)^(r-q)
    acc=0
    for i in range(2*q+1):
        for bit in (0,1):
            d=r-i-bit
            if d>=0 and d%2==0 and d//2<=r-q:
                acc+=(-1)**bit*comb(2*q,i)*comb(r-q,d//2)
    return acc

def certificate(s,eps):
    assert s>=2 and eps in (0,1)
    r0=s+1+((s+1-eps)&1) # smallest r>=s+1 with r%2==eps
    m0=(r0-eps)//2; b0=m0-1+eps
    dmax=(s-1+eps)//2
    assert b0>=dmax
    denominator_factors=[[2*(2*(b0-a)-1),4] for a in range(dmax)]
    numerator_factors=[[b0-a+1,1] for a in range(dmax)]
    T=product(denominator_factors)
    N={}
    for q in (s-1,s,s+1):
        coeff=[0]
        for j in range(q):
            if (eps-q+j)%2:continue
            d=(q-j-2+eps)//2
            if d<0:continue
            assert d<=dmax
            atom=product(numerator_factors[:d]+denominator_factors[d:])
            coeff=add(coeff,scale(atom,comb(q-1,j)*2**(q-1-j)))
        N[q]=coeff
    Ln=scale(mul([r0+s+1,2],[r0-s,2]),2*s*(2*s-1))
    Ld=scale(mul([r0+s,2],[r0-s+1,2]),(2*s+2)*(2*s+1))
    A=sub(mul(Ld,mul(N[s],N[s])),mul(Ln,mul(N[s-1],N[s+1])))
    B=mul(Ld,mul(T,T))
    assert len(A)==len(B)==2*dmax+3
    assert all(v>0 for v in A) and all(v>0 for v in B),('nonpositive coefficient',s,eps)
    # One boundary exact model cross-check per parity, in addition to independent verifier.
    hs=[comb(r0+q,2*q)*coefficient_raw(r0,q) for q in (s-1,s,s+1)]
    D=hs[1]**2-hs[0]*hs[2]
    C=cat(m0-1+eps)
    assert D>0 and B[0]*D==A[0]*(comb(r0+s,2*s)*C)**2
    def digest(a):return hashlib.sha256(','.join(map(str,a)).encode()).hexdigest()
    row={'s':s,'epsilon':eps,'r0':r0,'b0':b0,'dmax':dmax,
         'A_degree':len(A)-1,'B_degree':len(B)-1,
         'A_positive_count':len(A),'B_positive_count':len(B),
         'A_min':str(min(A)), 'B_min':str(min(B)),
         'A_coefficients_ascending':[str(v) for v in A],
         'B_coefficients_ascending':[str(v) for v in B],
         'A_sha256':digest(A),'B_sha256':digest(B),
         'boundary_D':str(D),'boundary_crosscheck':True}
    return row

def main():
    out=[]
    for s in range(LOW,HIGH+1):
        for eps in (0,1):out.append(certificate(s,eps))
    assert len(out)==2*(HIGH-LOW+1)
    ac=sum(t['A_positive_count'] for t in out)
    bc=sum(t['B_positive_count'] for t in out)
    assert ac==bc==sum(2*s+4 for s in range(LOW,HIGH+1))==15974
    root=Path(__file__).parent
    full={'schema':'EM_R418_SIGNED_AUX_INTERVAL_EXACT_CERTIFICATE_V1',
          'domain':{'s_min':LOW,'s_max':HIGH,'r_lower_bound_rule':'integer r>=s+1'},
          'source':'R416 Catalan kernel; R417 raw polynomial method; R418 generalized finite-degree lemma',
          'algorithm':'Exact raw integer polynomial assembly, both r parities, all A/B coefficients strictly positive',
          'rows':out}
    full_path=root/'R418_INTERVAL_EVIDENCE.json'
    full_path.write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest={'schema':'EM_R418_INTERVAL_SUMMARY_V1','s_min':LOW,'s_max':HIGH,
        'n_bands':HIGH-LOW+1,'n_parity_cases':len(out),
        'positive_numerator_coefficients':ac,'positive_denominator_coefficients':bc,
        'boundary_raw_checks':len(out),'full_evidence_sha256':hashlib.sha256(full_path.read_bytes()).hexdigest(),
        'rows':[{'s':r['s'],'epsilon':r['epsilon'],'r0':r['r0'],'A_degree':r['A_degree'],
                 'B_degree':r['B_degree'],'A_sha256':r['A_sha256'],'B_sha256':r['B_sha256']}
                for r in out]}
    summary_path=root/'R418_INTERVAL_MANIFEST.json'
    summary_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R418_INTERVAL_EXACT_PASS',LOW,HIGH,'bands',HIGH-LOW+1,'parity_cases',len(out),
          'A_pos',ac,'B_pos',bc,'boundary_checks',len(out))
    print('R418_FULL_EVIDENCE_SHA256',manifest['full_evidence_sha256'])
    print('R418_SUMMARY_SHA256',hashlib.sha256(summary_path.read_bytes()).hexdigest())
    print('FULL_EVIDENCE_BYTES',full_path.stat().st_size)

if __name__=='__main__':main()
