#!/usr/bin/env python3
"""R288 exact independent checks of one-step BRC negative-tail transfer.
Python standard-library integer arithmetic only. A finite test, not a universal proof.
"""
import hashlib
import json
from collections import defaultdict

N=8000
DP_N=160
A=[1,0,2,-1] # a(y)
D=[1,-4,4,-2,4,-4,1] # a(y)^2-4y


def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w: z[i+j]+=v*w
    return z


def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]


def times(p,q):
    a,b=p; c,d=q
    return add(mul(a,c),mul(mul(b,d),D)), add(mul(a,d),mul(b,c))


def numerator(sym,m):
    count = m+1 if sym=='+' else m-1
    z=([1],[0])
    for _ in range(count):z=times(z,(A,[-1]))
    b=([1,-2,0,1] if sym=='+' else [1,0,-2,1])
    P,Q=times(z,(b,[1]))
    return P, mul(Q,[1,0,0,-1]), count # sqrt D=(1-y^3)*g


def f_coeffs(size):
    # f_j = -[y^j] sqrt((1-3y+y^2)/(1+y+y^2))
    f=[-1,2,0,0]
    for n in range(3,size):
        z=(2*n-2)*f[n]+(n-1)*f[n-1]+(2*n-2)*f[n-2]-(n-3)*f[n-3]
        q,r=divmod(z,n+1)
        assert r==0,(n,r)
        f.append(q)
    return f


def exact_delta(sym,m,top,f):
    # Delta_m(x)=x^(m+2)*d_m(x^2), (1+y)d_m=(P+Q*(1-y^3)*g)/(2^(M+1)y^M).
    P,Q,M=numerator(sym,m)
    den=2**(M+1)
    prev_d=0; values=[]
    for j in range(top+1):
        t=j+M
        w=(P[t] if t<len(P) else 0)-sum(c*f[t-i] for i,c in enumerate(Q) if c and t>=i)
        w,r=divmod(w,den)
        assert r==0,(sym,m,j,r)
        d=w-prev_d
        values.append(d)
        prev_d=d
    return values


def make_v(size):
    h=[0]*(size+1)
    for n in range(1,size+1):
        h[n]=(n==4)+sum(c*h[n-i] for i,c in ((1,1),(2,2),(3,1),(4,1)) if n>=i)
        for shift,c in ((1,1),(2,2),(3,1)):
            t=n-shift
            if t>=0:h[n]+=c*sum(h[k]*h[t-k] for k in range(t+1))
    v=[(i==0)+(i==1)+h[i]+(h[i-1] if i else 0) for i in range(size+1)]
    return v


def direct_dp(top):
    edges={0:{0:(2,-1,-1),1:(2,1,-1)},1:{0:(0,-1,-1),1:(0,1,-1)},2:{0:(1,1,1),1:(2,1,-1)}}
    cur={(0,1,0,0):1}
    result=[{(1,0):1}]
    for n in range(1,top+1):
        nex=defaultdict(int)
        for (q,ep,k,was0),count in cur.items():
            for bit,(nq,eta,c) in edges[q].items():
                if bit==0 and was0:continue
                nex[(nq,ep*eta,eta*k+c,1-bit)]+=count
        cur=nex
        pop=defaultdict(int)
        for (q,ep,k,was0),count in cur.items():
            if q==0:pop[(ep,k)]+=count
        result.append(pop)
    return result


def main():
    f=f_coeffs(N+50)
    d13=exact_delta('+',13,N,f)
    d11=exact_delta('-',11,N,f)
    d12=exact_delta('+',12,8,f)
    d10=exact_delta('-',10,8,f)
    assert d12[5]==-56,(d12[:7])
    assert d10[4]==-5,(d10[:7])
    assert all(z>=0 for z in d13),"+13 finite negative"
    assert all(z>=0 for z in d11),"-11 finite negative"
    assert d13[:8]==[1,11,52,130,157,24,51,1270],d13[:8]
    assert d11[:8]==[1,8,26,39,16,5,191,718],d11[:8]
    v=make_v(90)
    assert v[:8]==[1,1,0,0,1,2,4,9]
    assert all(z>0 for z in v[4:])
    exact={('+',13):exact_delta('+',13,70,f),('+',14):exact_delta('+',14,70,f),('-',11):exact_delta('-',11,70,f),('-',12):exact_delta('-',12,70,f)}
    for sym,m in (('+',13),('-',11)):
        lo=exact[(sym,m)];hi=exact[(sym,m+1)]
        for j in range(70):
            assert hi[j]==sum(v[i]*lo[j-i] for i in range(j+1)),(sym,m,j)
    dp=direct_dp(DP_N)
    comparisons=0
    for sym,m in (('+',13),('+',14),('-',11),('-',12)):
        ds=exact_delta(sym,m,(DP_N-m-2)//2,f)
        for j,w in enumerate(ds):
            n=m+2+2*j
            e=1 if sym=='+' else -1
            direct=dp[n].get((e,-m),0)-dp[n].get((e,-m-2),0)
            assert w==direct,(sym,m,n,w,direct)
            comparisons+=1
    def digest(z):
        h=hashlib.sha256()
        for i,value in enumerate(z):
            h.update(f'{i}:{value}\n'.encode())
        return h.hexdigest()
    data={
        'status':'PASS','model':'ordered positive BRC auxiliary clean reset, six edges',
        'strictly_finite_verification':True,'math_infinite_identity':'Delta_(m+1)=u Delta_m from R283 exact Green expressions',
        'u':'x*(1+y)*(1+h(y)); h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2',
        'candidate_bases':{'plus_m':13,'minus_m':11},
        'necessary_lower_failures':{'Delta_plus_12_at_n24':d12[5],'Delta_minus_10_at_n20':d10[4]},
        'normalized_positive_prefixes':{'plus_m13':d13[:15],'minus_m11':d11[:15]},
        'checked_j_range':[0,N],
        'checked_path_length_range':[0,DP_N],
        'path_vs_algebra_comparisons':comparisons,
        'one_step_coefficient_crosscheck':{'pairs':2,'j_range':[0,69],'passed':True},
        'f_recurrence_truncation':N+50,
        'hash_of_normalized_coefficients':{'plus_m13':digest(d13),'minus_m11':digest(d11)},
        'unproved':'The two base series have nonnegative coefficients for every j>N; finite prefix does not establish that claim.'
    }
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
