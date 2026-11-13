#!/usr/bin/env python3
"""R455 independently reimplemented exact Catalan-factor polynomial certificates.
No floats; compute positive-coefficient polynomials in u=k-k0 for each s.
Scientific source: r454/R454_PROOF.zh-CN.md immutable commit 5ee2a81... .
"""
from math import comb, factorial
import hashlib,json,sys,time

def add(*ps):
    z=[0]*max(map(len,ps))
    for p in ps:
        for i,a in enumerate(p):z[i]+=a
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def neg(a):return [-x for x in a]

def mul(a,b):
    if len(a)>len(b):a,b=b,a
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]+=x*y
    return out

def prod(factors):
    z=[1]
    for f in factors:z=mul(z,f)
    return z

def B_polynomial(s,k0,F):
    m=(s-1)//2
    E=prod(([2*(k0+1-s//2+j),2] for j in range(s)))
    O=prod(([2*k0+2*j+1,2] for j in range(s//2+1)))
    R=add(*([comb(s-1,2*q)*2**q*x for x in prod([[2*k0-2*h-1,2] for h in range(q,m)]+[[k0+1-d,1] for d in range(q)])] for q in range(m+1)))
    assert F%factorial(2*s)==0
    return [v*(F//factorial(2*s)) for v in prod([E,O,R])]

def C(n):return comb(2*n,n)//(n+1)

def H_signed(k,s):
    r=2*k+1
    if not 2<=s<=r:return 0
    d=r-s
    def cc(n,j):return comb(n,j) if 0<=j<=n else 0
    return comb(r+s,2*s)*sum(comb(d,q)*(cc(2*s,r-2*q)-cc(2*s,r-2*q-1)) for q in range(d+1))

def H_cat(k,s):
    r=2*k+1
    if not 2<=s<=r:return 0
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*C(k-q) for q in range((s-1)//2+1))

def check(s):
    t0=time.monotonic(); k0=(s+2)//2; F=factorial(2*(s+2))
    ps={t:B_polynomial(t,k0,F) for t in range(s-2,s+3)}
    a,b,c,d,e=(ps[t] for t in (s,s-1,s+1,s-2,s+2))
    p2=add(mul(a,a),neg(mul(b,c)))
    p2left=add(mul(b,b),neg(mul(d,a)))
    p2right=add(mul(c,c),neg(mul(a,e)))
    p3=add(mul(mul(a,a),a),neg([2*x for x in mul(mul(a,b),c)]),mul(d,mul(c,c)),mul(mul(b,b),e),neg(mul(d,mul(a,e))))
    assert len(p2)==4*s+1 and len(p3)==6*s+1
    assert mul(a,p3)==add(mul(p2,p2),neg(mul(p2left,p2right)))
    nonpos2=[i for i,x in enumerate(p2) if x<=0]
    nonpos3=[i for i,x in enumerate(p3) if x<=0]
    cross=[]
    for k in (k0,k0+1):
        for t in range(s-2,s+3):
            v=H_signed(k,t);w=H_cat(k,t)
            cross.append((k,t,int(v==w),int(v>=0)))
            assert v==w
            if k==k0:
                assert ps[t][0]*C(k)==F*v
    assert not nonpos2 and not nonpos3, {'s':s,'bad2':nonpos2[:3],'bad3':nonpos3[:3]}
    sha=hashlib.sha256()
    for row in (p2,p3):
        sha.update(len(row).to_bytes(2,'big'))
        for x in row:
            v=x.to_bytes((x.bit_length()+7)//8,'big')
            sha.update(len(v).to_bytes(4,'big'));sha.update(v)
    result={'s':s,'k0':k0,'min_r':2*k0+1,'degrees':[len(p2)-1,len(p3)-1],'checked_positive_coefficients':len(p2)+len(p3),'condensation_identity':'PASS','raw_Catalan_crosschecks':len(cross),'coefficients_sha256':sha.hexdigest(),'elapsed_s':round(time.monotonic()-t0,2)}
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 141
    hi=int(sys.argv[2]) if len(sys.argv)>2 else 141
    results=[]
    for s in range(lo,hi+1):results.append(check(s))
    evidence={'name':'R455_ExactSignedBRC','source':'R454 proof at commit 5ee2a81ccea8af95a92cae0bcbe008c04d1083f0','interval':[lo,hi],'status':'PASS','rows':results,'total_positive_coefficients':sum(x['checked_positive_coefficients'] for x in results),'crosschecks':sum(x['raw_Catalan_crosschecks'] for x in results)}
    with open('R455_EVIDENCE.json','w',encoding='utf-8') as f:json.dump(evidence,f,indent=2,ensure_ascii=False)
    print('R455_EXACT_PASS',evidence['total_positive_coefficients'],flush=True)
