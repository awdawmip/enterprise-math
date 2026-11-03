#!/usr/bin/env python3
"""PREFIX-472: exact codebook-free rank/unrank for normalized X6 BRC base support.
Only Python 3 standard library, integers throughout; no GitHub or native writes.
"""
from math import comb, factorial

Q_NUM = (1, 2, 3, 4, 2)

def pbin(x, d):
    """Binomial polynomial (x choose d) on any integer x."""
    z = 1
    for i in range(d):
        z *= x-i
    return z // factorial(d)

def P(m):
    """Polynomial extension of [z^m] (1+2z^2)(1+z)^2/(1-z)^8."""
    return sum(a*pbin(m-h+7, 7) for h,a in enumerate(Q_NUM))

def diffs(f, deg):
    arr = [f(i) for i in range(deg+1)]
    out = []
    while arr:
        out.append(arr[0])
        arr = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
    return out

def newton_sum(coeffs, t):
    assert t >= 0
    return sum(a*comb(t, i+1) for i,a in enumerate(coeffs) if i+1 <= t)

def sm(n,k):
    assert n>=0 and k>=1
    return (n+k)//(k+1)

def M(n,k,s):
    return n if s==0 else n-1-(s-1)*(k+1)

def s_prefix(n,k,s):
    """# normalized states with special-step count < s, 0<=s<=smax+1."""
    if s==0: return 0
    seq = diffs(lambda j:P(n-1-j*(k+1)),7)
    return P(n)+newton_sum(seq,s-1)

def R(t):
    return (t+1)*(3*t+2)//2

def c5_poly(q):
    return (4*q**4+20*q*q+6)//3

def shell_poly(m,t):
    return R(t)*c5_poly(m-2*t)

def shell_prefix(m,t):
    """# states in shells T=0,...,t-1; t<=m//2+1."""
    assert m>=0 and 0<=t<=m//2+1
    ans=newton_sum(diffs(lambda u:shell_poly(m,u),6),t)
    if m%2==0 and t==m//2+1:
        ans-=R(m//2)  # c5(0)=1, its polynomial continuation is 2
    return ans

def c(j,q):
    if q<0: return 0
    if j==0: return int(q==0)
    return sum(comb(j,a)*comb(q-a+j-1,j-1) for a in range(min(j,q)+1))

def H(j,q):
    if q<0: return 0
    return sum(comb(j,a)*comb(q-a+j,j) for a in range(min(j,q)+1))

def prefix_signed(rem,j,v):
    """# j+1 dimensional vectors (v0,rest) of norm rem with v0<=v, integer ascending."""
    assert -rem<=v<=rem
    if v<0:
        return H(j,rem+v)
    return 2*H(j,rem-1)+c(j,rem)-H(j,rem-v-1)

def rank_vec(d,q):
    assert len(d)==5 and sum(map(abs,d))==q
    ans=0; rem=q
    for i,v in enumerate(d):
        assert -rem<=v<=rem
        if v>-rem:
            ans+=prefix_signed(rem,4-i,v-1)
        rem-=abs(v)
    assert rem==0
    return ans

def unrank_vec(q,idx):
    assert 0<=idx<c(5,q)
    d=[]; rem=q
    for i in range(5):
        j=4-i
        lo=-rem; hi=rem
        while lo<hi:
            v=(lo+hi)//2
            if prefix_signed(rem,j,v)>idx:hi=v
            else:lo=v+1
        v=lo
        below=prefix_signed(rem,j,v-1) if v>-rem else 0
        idx-=below
        d.append(v); rem-=abs(v)
    assert idx==0 and rem==0
    return tuple(d)

def tri_start(t,C):
    return C*(2*t+1)-C*(C-1)//2

def rank_tri(t,A,C):
    assert 0<=C<=t and 0<=A<=2*t-C
    return tri_start(t,C)+A

def unrank_tri(t,idx):
    assert 0<=idx<R(t)
    lo,hi=0,t+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if tri_start(t,mid)<=idx:lo=mid
        else:hi=mid
    return idx-tri_start(t,lo),lo

def count(n,k):
    return s_prefix(n,k,sm(n,k)+1)

def rank(n,k,s,d,A,C):
    assert 0<=s<=sm(n,k)
    m=M(n,k,s); q=sum(map(abs,d))
    assert m>=q and (m-q)%2==0
    t=(m-q)//2
    return s_prefix(n,k,s)+shell_prefix(m,t)+rank_vec(d,q)*R(t)+rank_tri(t,A,C)

def unrank(n,k,idx):
    total=count(n,k)
    assert 0<=idx<total
    lo,hi=0,sm(n,k)+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if s_prefix(n,k,mid)<=idx:lo=mid
        else:hi=mid
    s=lo; rest=idx-s_prefix(n,k,s); m=M(n,k,s)
    lo,hi=0,m//2+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if shell_prefix(m,mid)<=rest:lo=mid
        else:hi=mid
    t=lo; rest-=shell_prefix(m,t)
    q=m-2*t
    d=unrank_vec(q,rest//R(t))
    A,C=unrank_tri(t,rest%R(t))
    return (s,d,A,C)

def shell(q,dim=5):
    if dim==0:
        if q==0:yield ()
        return
    for v in range(-q,q+1):
        for rem in shell(q-abs(v),dim-1):
            yield (v,)+rem

def brute(n,k):
    """Independent direct lexicographic enumeration of the normalized set U_{n,k}."""
    idx=0
    for s in range(sm(n,k)+1):
        m=M(n,k,s)
        for t in range(m//2+1):
            q=m-2*t
            for d in shell(q):
                for C in range(t+1):
                    for A in range(2*t-C+1):
                        key=(s,d,A,C)
                        assert rank(n,k,*key)==idx,(n,k,idx,key)
                        assert unrank(n,k,idx)==key,(n,k,idx,key)
                        idx+=1
    assert idx==count(n,k),(n,k,idx,count(n,k))
    return idx

if __name__ == '__main__':
    for m in range(0,110):
        assert shell_prefix(m,m//2+1)==P(m),(m,shell_prefix(m,m//2+1),P(m))
        for q in range(0,11):
            assert c(5,q)==len(list(shell(q)))
    print('SHELL_POLYNOMIAL_PREFIX verified M=0..109; SHELL_VECTOR_COUNTS q=0..10')
    for k in (1,2,3,4):
        counts=[brute(n,k) for n in range(0,8)]
        print('EXHAUSTIVE RANK_UNRANK k=',k,'n=0..7 counts=',counts)
    assert count(8,2)==33797
    assert count(8,3)==33295
    for n,k in [(64,1),(256,2),(1024,3),(65536,2),(10**9,2),(10**9,1000000001)]:
        B=count(n,k)
        tests={0,1,B//5,B//2,(B*4)//5,B-2,B-1}
        for z in tests:
            if z<0 or z>=B:continue
            key=unrank(n,k,z)
            assert rank(n,k,*key)==z,(n,k,z)
        print('LARGE_EXACT', 'n=',n,'k=',k,'states_bits=',B.bit_length(),'samples=',len(tests),'PASS')
    print('ALL_CHECKS_PASS')
