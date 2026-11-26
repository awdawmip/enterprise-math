# R284IZ — Joint denominator height compression and exact prime-local carry optimizer
2026-11-27. Author proof and executed exact finite tests; NOT_REVIEWED. Auxiliary binary-tag joint-count observer, no spatial/dynamics promotion. Frozen input IY@5ce97ab5f9362a860b735028975420c0b19b5fe2:research_notes/portable_direct/R284IY_BUDGET_PRIME_LIFT_AND_BOUNDARY_20261127.md (blob 63b8137d6b80c7d723cce7a2d7e2e61935ae0bba), including its frozen IX definitions and IU height lineage. P000 V5, ACTIVE worldview, joint observer and heartbeat companion, current portable and research-method contracts consulted. Own existing registration recovered; RA-B82240E8488EF5A1DA5186C4. Owner inventory request r1-20261127-0204-owner was RUNNING at proof/publication preparation; this is an independent continuation of own portable line, no shared task, claim, result or owner mutation. All V,Q,A,E are retained.

## 1. Exact common denominator with factorial compression
Use q>=64, 1<=d<=2sqrt(q), integers; u=q+d, m=2q+d, l=d-k. R_n(j)=product_{i=0}^{j-1}(n-i)/(n+i+3), w0=(k+1)(l+1)R_u(k)R_m(l), w1=(k+1)l R_u(k)R_m(l-1) (zero for l=0), v=(u-k)(u+k+2)/(2u(2u+1)). V=sum w0, Q=sum w1, A=sum v(w0+w1),
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)].
Z=qA+Q+V, Y=qK=q(4q+3d+1)^2(A+E)Q/[(3q+d+1)Z^2], F=Y-32/3.

Define B=2u(2u+1)(4m+2), C_n=binom(n+d+2,d), L= lcm_{0<=j<=d} binom(d,j), D=B C_u C_m L^2. Then DV,DQ,DA,DE are integers. Proof: R_n(j)=binom(n,j)/binom(n+j+2,j) and C_n binom(d,j)=binom(n+j+2,j)binom(n+d+2,d-j), by factorial cancellation. Hence each reduced denominator of R_n(j) divides C_n L. Apply to both full and shifted fibers and the exact E; the latter includes only R_u(d) and exterior factors dividing B. No observation is deleted. Also D divides IU's old Dold=B product_{i=0}^{d-1}(u+i+3)(m+i+3), since L divides d! (every binomial divides d!).

For each prime p, Legendre's formula gives v_p(binom(d,j)) as the sum over p^a<=d of floor(d/p^a)-floor(j/p^a)-floor((d-j)/p^a), each 0 or 1. Thus L divides lcm(1,...,d) and log L=O(d). Elementary proof of the latter: for power of two N, each prime power in (N/2,N] contributes a prime factor to binom(N,N/2) (by the same floor formula). At most one power of a given prime lies in that half-open interval. Consequently log lcm(1,...,N)-log lcm(1,...,N/2)<=N log 2. Sum dyadically and round d up to a power of two <2d, giving log L<=4d log 2. This argument does not require a prime number theorem.

## 2. Sharper nonzero real residual certificate and precision cap
S=binom(d+3,3)+binom(d+2,3)=(d+1)(d+2)(2d+3)/6. Since 0<R<=1, 0<=v<1 (use (u-k)(u+k+2)<=(u+1)^2<2u(2u+1) for u>=64), V+Q<=S by elementary convolution of (k+1)(l+1) and (k+1)l. Hence 0<Z<=(q+1)S.
Writing V,Q,A,E with denominator D in the exact joint ratio gives
F = [3q(4q+3d+1)^2 (D(A+E))(DQ)-32(3q+d+1)(DZ)^2]/[3(3q+d+1)(DZ)^2].
Its numerator is an integer and the denominator positive. Therefore F=0 or |F|>=1/H with
H=3(3q+d+1)[D(q+1)S]^2.
For an enclosure of F, width strictly below 1/H, containing zero, implies exact equality; this is an exact bound and need not form H explicitly if a certified upper bound for its bit length is used. Using n+d+2<=3q for n=u,m, d<=2sqrt(q), q>=64, C_n<=(3eq/d)^d, log L=O(d), B=O(q^3), we get log H<=4d log(q/d)+O(d+log q) uniformly. On d=s sqrt(q)+O(1), fixed 0<s<=2, this is 2d log q+O_s(d+log q). IU's published sufficient cap (4d+16)log(10q) has leading term 4d log q. Thus the leading sufficient worst-case precision cap is halved on the critical scale, not a claim about actual minimal precision, runtime, or polynomial-in-log q separation. For the exact H above, ceil(log2 H)+1 suffices as an enclosure width exponent. Computing C_n,L or H exactly can still cost at least its output length; this is a height theorem, not a fast global factorization algorithm.

## 3. Joint prime-local minimal common denominator via a five-bit carry state
Define J=lcm of the reduced denominators of every unweighted product R_u(k)R_m(l) with k+l=d or d-1 and nonnegative k,l. This is an exact minimal common denominator for that declared family of product readouts, not for every weighted aggregate. R_u(d) is one member, so D_J=B J also clears V,Q,A,E. D_J divides D. The joint denominator can be computed locally at any supplied prime without enumerating the O(d) branches.

For fixed prime p and s in {d,d-1}, use base-p digits of k,l with k+l=s. At a digit position track five bits (c,a,b,x,y): incoming carry for k+l, carries for (u+2)+k and (m+2)+l, borrows for u-k and m-l. Kummer's carry formula, or Legendre's formula summed by digit differences, gives
-v_p(R_u(k)R_m(l)) = (# addition carries a,b) - (# subtraction borrows x,y).
Indeed R_n(j)=binom(n,j)/binom(n+j+2,j), binom(n,j) counts borrows subtracting j from n, binom(n+j+2,j) counts carries adding j to n+2. Include all digits through a width W with p^W>m+d+2. Initial and terminal five bits are all zero: k+l=s and k,l<=d<=u,m ensure no final borrow, and sums fit this width.

For a proposed next state (c',a',b',x',y'), the digits K,L obey K+L=s_i+p c'-c. The allowed K range starts [0,p-1]; intersect with K>=p-(u+2)_i-a if a'=1 or K<=p-1-(u+2)_i-a if a'=0, and K>=u_i-x+1 if x'=1 or K<=u_i-x if x'=0. Similarly L with m,b,y. A pair exists iff both resulting integer intervals are nonempty and the prescribed sum lies between the sum of lower endpoints and the sum of upper endpoints. Thus a transition has an O(1) feasibility test independent of p and adds score a'+b'-x'-y'. Max-plus DP over the 32 states gives the exact maximum at the terminal zero state, separately for each s. Induction over digits gives all feasible prefixes and their maximal score; feasibility and future scores depend only on the retained state, so maximum compression is exact for this observer/horizon. Conversely each feasible transition admits an integer digit pair, and terminal paths decode to actual allowed k,l. The exponent of p in J is the maximum of zero and the two terminal scores. This preserves shared sum carries rather than optimizing the two branches independently.

There are O(log_p(m+d+2)) digit layers, at most 32^2 transitions per layer; digit extraction and all interval and score operations have polynomial bit cost in log q+log p. No scan over k, l, or p digit values. The local algorithm assumes a supplied prime; it neither discovers all relevant primes nor reconstructs the full huge J in polynomial input length. It computes denominator exponents for unweighted products, not cancellation among sums, so it is a safe common-denominator certificate and a new local arithmetic resource, not a claim of the exact valuation of Y.

## 4. Executed evidence
Exact Python Fraction/integer calculations. All 1990 pairs q=64..160, d=1..isqrt(4q) checked, plus five specified larger cases. Dold/D/D_J bit lengths:
q=10000,d=97: 2723/1972/1645; H=4022 bits, actual reduced F denominator 2977 bits.
q=100000,d=306: 10529/7211/6056; H=14522 bits, actual F denominator 10924 bits.
q=1000000,d=968: 39624/25958/22457; H=52035 bits, actual F denominator 40738 bits.
q=100000000,d=100: 5500/4722/4375; H=9563 bits, actual F denominator 7996 bits.
q=10^30,d=100: 20336/19558/19166; H=39454 bits, actual F denominator 35109 bits.
For 1990 cases median D/Dold bit-length ratio 0.8634146341463415, min 0.7494199535962877, max 1 (bit length ratios, not numerical denominator ratios).
Prime-local DP: 2240 exact comparisons to independently enumerated rational products (40 pairs, 28 primes, 2 totals). All pass.
At q=10^60,d=968081516889092505839243780672, p=(2,3,5,7,11,101,1009), J exponents=(78,50,37,26,24,16,7).
At q=10^100,d=10^50, same primes, exponents=(95,69,17,56,36,21,12). These two large inputs used the carry DP only, not full branch enumeration or real Y evaluation. No timing claim.
Reproduction code below, executed locally (Python, SymPy only for small-prime list):
```python
from math import comb, lcm, prod, isqrt
from fractions import Fraction as F
from statistics import median

def R(n,d):
    a=[F(1)]
    for i in range(d): a.append(a[-1]*F(n-i,n+i+3))
    return a

def calc(q,d):
    u=q+d; m=2*q+d
    r,s=R(u,d),R(m,d)
    V=Q=A=F(0)
    for k in range(d+1):
        l=d-k
        w0=(k+1)*(l+1)*r[k]*s[l]
        w1=(k+1)*l*r[k]*s[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=w0;Q+=w1;A+=v*(w0+w1)
    E=r[d]*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V
    Y=q*(4*q+3*d+1)**2*(A+E)*Q/((3*q+d+1)*Z**2)
    B=2*u*(2*u+1)*(4*m+2)
    L=lcm(*(comb(d,j) for j in range(d+1)))
    D=B*comb(u+d+2,d)*comb(m+d+2,d)*L**2
    Dold=B*prod((u+i+3)*(m+i+3) for i in range(d))
    J=lcm(*((r[k]*s[d-k]).denominator for k in range(d+1)), *((r[k]*s[d-1-k]).denominator for k in range(d)))
    Dj=B*J
    for n,arr in [(u,r),(m,s)]:
        C=comb(n+d+2,d)
        for j,x in enumerate(arr):
            assert x==F(comb(n,j),comb(n+j+2,j))
            assert (C*L)%x.denominator==0
    assert lcm(*range(1,d+1))%L==0
    assert Dold%D==0 and D%Dj==0
    for h in (V,Q,A,E):
        assert (D*h).denominator==1 and (Dj*h).denominator==1
    S=comb(d+3,3)+comb(d+2,3)
    assert 0<Z<=(q+1)*S
    f=Y-F(32,3)
    H=3*(3*q+d+1)*(D*(q+1)*S)**2
    Hactual=3*(3*q+d+1)*int(D*Z)**2
    assert Hactual<=H and Hactual%f.denominator==0
    assert not f or abs(f)*H>=1
    return Dold.bit_length(),D.bit_length(),Dj.bit_length(),H.bit_length(),f.denominator.bit_length()

def exponent_dp(q,d,p,s):
    u=q+d; m=2*q+d
    top=m+d+2
    width=0
    while top: width+=1;top//=p
    state={(0,0,0,0,0):0}
    from itertools import product
    states=list(product((0,1),repeat=5))
    def interval(n,a,c,b,co,bo):
        lo,hi=0,p-1
        if co:lo=max(lo,p-a-c)
        else:hi=min(hi,p-1-a-c)
        if bo:lo=max(lo,n-b+1)
        else:hi=min(hi,n-b)
        return lo,hi
    for i in range(width):
        sd=s%p; ud=u%p;md=m%p
        if i==0: ua,ma=u+2,m+2
        ad,bd=ua%p,ma%p
        nxt={}
        for (c,a,b,x,y),val in state.items():
            for co,ao,bo,xo,yo in states:
                total=sd+p*co-c
                lo,hi=interval(ud,ad,a,x,ao,xo)
                lo2,hi2=interval(md,bd,b,y,bo,yo)
                if lo<=hi and lo2<=hi2 and lo+lo2<=total<=hi+hi2:
                    key=(co,ao,bo,xo,yo);score=val+ao+bo-xo-yo
                    nxt[key]=max(nxt.get(key,-10**9),score)
        state=nxt
        s//=p;u//=p;m//=p;ua//=p;ma//=p
    return state[(0,0,0,0,0)]

def vp(n,p):
    v=0
    while n%p==0:n//=p;v+=1
    return v

if __name__=='__main__':
    cases=0; ratios=[]
    for q in range(64,161):
        for d in range(1,isqrt(4*q)+1):
            a,b,c,h,f=calc(q,d);cases+=1;ratios.append(b/a)
    print('exhaustive',cases,'median Dnew/Dold bits',median(ratios),'min',min(ratios),'max',max(ratios))
    for q,d in [(10**4,97),(10**5,306),(10**6,968),(10**8,100),(10**30,100)]:
        print(q,d,*calc(q,d))
    from sympy import primerange
    import random
    rng=random.Random(284)
    num=0
    for q,d in [(64,1),(64,16),(101,19),(1000,63),(10**6,968)]+[(q:=rng.randrange(64,10000),rng.randrange(1,isqrt(4*q)+1)) for _ in range(35)]:
        r=R(q+d,d);t=R(2*q+d,d)
        for p in list(primerange(2,100))+[101,1009,10007]:
            for s in (d,d-1):
                a=max(vp((r[k]*t[s-k]).denominator,p)-vp((r[k]*t[s-k]).numerator,p) for k in range(s+1))
                b=exponent_dp(q,d,p,s)
                assert a==b,(q,d,p,s,a,b)
                num+=1
    print('DP comparisons',num)
    for q,d in [(10**60,968081516889092505839243780672),(10**100,10**50)]:
        print('huge local exponents',q,d,[(p,max(0,exponent_dp(q,d,p,d),exponent_dp(q,d,p,d-1))) for p in (2,3,5,7,11,101,1009)])
```

Next: use the joint carry optimizer to locate and classify high-pole fibers with witnesses, then retain their leading joint residues to resolve cancellation in V,Q,A,E and Z. Investigate whether the prime-local denominator compression yields a smaller aggregate height or a modular equality certificate in previously uncovered ranges; global inverse-polynomial separation, complete equality exclusion, worst-case polylog sign complexity remain open. No independent review or formal task completion asserted.
