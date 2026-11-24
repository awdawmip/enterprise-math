# R284HD — Eventual unique flexibility transition and integer rounding

2026-11-25. Author derivation, NOT_REVIEWED. Auxiliary four-phase binary-tag count model, no new physical attribution. Original own registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED, EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4; own recovery_status confirms original session open, metadata only, no runs or execution authorization. Previous inventory r284hc-20261125-0200-owner-read-v1 SUCCEEDED with no LEASED entries at its as-of time; current r284hd-20261125-0300-owner-read-v1 submitted; no shared CLAIM. Current normative entries read (GK main 518a214c5f864a0e9574ff5e304facb3fadb7ee8 entry blobs verified; EM control main 30909fe3d79e01650e191e733a40883491fbb47b, P000 V5 and companions, ACTIVE worldview, BRC, portable and continuation protocols). Frozen science: GU f14ef36840c37d78c1537c930f192fdb43d3b094 (blob 7be81184e98a89c982dc8ab87e3ee78f9341b4d5); HC 36e96070fd5f44cabe0713c9047fb751232f69bc, and HA/HB as pinned there. No repinning. All theorems here use the earlier author-proved GU uniform estimate and HC finite upper bound; independent review of the dependencies remains pending.

## 1. Results

Use integer u>=1 and 0<=q<u, H=u+2q+1, J=3u+q, S,P,Q the three exact safe-word counts, K=PQ(J+1)^2/(S^2 H). K^2 is the labeled four-edge cycle count ratio.

Theorem A: For every sufficiently large u, K(q+1,u)<K(q,u) for every adjacent integer q with q+1<=floor(u/(log u)^3). More generally the assertion holds eventually on every sequence with (q+1)log^2(u)/u -> 0. This is a growing unbounded wedge, not a fixed strip. Natural log used; changing base preserves the asymptotic scale.

Theorem B: For all sufficiently large integer u the full low-omission domain has exactly one sign transition across K=1, allowing at most one tied integer between a nonempty initial K>1 interval and a nonempty terminal K<1 interval. This does not require global K monotonicity. No effective numerical lower threshold on u is asserted.

Theorem C: Put h(u)=6 sqrt(u)-169/3. There is an absolute constant A>0 such that, for sufficiently large u, every integer q below h(u)-A log^2(u)/sqrt(u) has K>1, and every integer q above h(u)+A log^2(u)/sqrt(u) has K<1. Outside the exceptional set of u satisfying dist(h(u),Z)<=A log^2(u)/sqrt(u), the last strictly asymmetric-dominant integer is exactly floor(h(u)), with no tie. The count of exceptional u<=X is O(sqrt(X) log^2(X)), so the exact floor formula holds on a density-one set. In particular, for all sufficiently large perfect squares u=s^2, the last asymmetric-dominant q=6s-57 and first symmetric-dominant q=6s-56.

## 2. Proof of the growing monotone wedge

Reuse GU's uniform relative estimate at epsilon=1/2:
K(q,u)=T(q,u)(1+O(log^2(u)/u)), 0<=q<=u/2.
Set D=N-q=4u+2q+1=H+3u, L=J+1, p=H/D and beta=3u/D. Then
T = L^2 D/[H^2 B^2], B=q+1/(p beta)=q+D^2/(3uH).
Equivalently T=9u^2 L^2 D/(3u q H+D^2)^2, an exact rational surrogate, not the exact K.

Regard q as a real variable only for T. The prefactor L^2 D/H^2 is decreasing because its logarithmic derivative is 2/L+2/D-4/H<0 (H<L, H<D). On the interval 0<=q<=u/2, 1/4<=p<=1/2, so B<=q+16/3<q+6. Direct differentiation gives
B' = 1 + (2/(3u))(1-(3u/H)^2) >= 1-16/(3u) >= 1/2 for u>=11.
Hence d(log T)/dq <= -1/(q+6). Integration over one unit yields
log(T(q+1,u)/T(q,u)) <= -log((q+7)/(q+6)) <= -1/(q+7),
for q+1<=u/2. In particular T(q+1)/T(q)<=(q+6)/(q+7), exactly.

The uniform GU relative error implies |log K-log T| <= C log^2(u)/u for all sufficiently large u and this whole interval (use |log(1+x)|<=2|x| once |x|<=1/2). Consequently
log(K(q+1,u)/K(q,u)) <= -1/(q+7)+2C log^2(u)/u.
If (q+1)log^2(u)/u -> 0, the negative term strictly dominates; uniformly for q+1<=u/log^3(u) its magnitude is at least asymptotically log^3(u)/u. This proves Theorem A. It does not differentiate the error term or assume smooth interpolation of the integer counts.

## 3. Proof of unique transition

At q=0 the rational T has T/u -> 81/64, so K(0,u)>1 eventually. HC's strict finite bound K<144u/(q+5)^2 for u>=40 implies K<1 at every integer q with q+5>=12 sqrt(u). For large u the integer ceil(12 sqrt(u)-5) is strictly inside the monotone wedge of Theorem A. Thus K decreases strictly from above 1 to below 1 within that wedge, and every later q is below 1 by the independent HC bound. There is a single sign transition on the entire low-omission domain, with at most one equality; no statement of global monotonicity is needed. Theorem B follows.

## 4. Exact rounding except near integer resonance

GU's critical-window formula, uniform for bounded k=q-6 sqrt(u), is
K=1-(q-h(u))/(3 sqrt(u))+O(log^2(u)/u).
Thus within |q-h(u)|<=3, an absolute A (greater than 3 times the uniform error constant) guarantees the stated strict signs beyond distance A log^2(u)/sqrt(u). For large u the latter distance is <1/2, and the integer points just outside a fixed radius 1 on either side of h are within the monotone wedge. By Theorem A these signs extend to all earlier/later q in the wedge, and by HC to all remaining q beyond it. Hence if the distance to the nearest integer exceeds the error width, the two integers floor(h), ceil(h) straddle the transition strictly, and the last K>1 equals floor(h). The at-most-one ambiguous integer is preserved; no automatic rounding through a tie.

For the density estimate, partition u into blocks r^2<=u<(r+1)^2. The real h varies by exactly 6 on each block and has derivative 3/sqrt(u)>=3/(r+1). For r sufficiently large the exceptional condition implies distance to one of at most 8 integers <= C' log^2(r+1)/r. For each integer, the corresponding real u interval has length O(log^2(r+1)) by the mean value theorem and contains O(1+log^2(r+1)) integers. Summation over r<=sqrt(X) bounds exceptions by O(sqrt(X) log^2(X)). On perfect squares h=6s-56-1/3, distance 1/3, so all sufficiently large squares avoid the exception set. Exact asymptotic floor can be evaluated without floating point as (isqrt(324*u)-169)//3. This retains the integer observation; the unresolved exceptional u require a finer error analysis or exact count.

## 5. Actual finite checks (not a threshold proof)

Executed Python arbitrary precision: 16,359 exact rational surrogate adjacent comparisons for 11<=u<=256 and 0<=q<floor(u/2); all satisfied T(q+1)(q+7)<=T(q)(q+6). Six exact K counts using HA/HC moments at the two integers surrounding h:
u | floor(h) | K(floor(h)) | K(floor(h)+1)
256 | 39 | 3.345013977719362 | 3.174298653549773
1024 | 135 | 1.3701432291623878 | 1.3480987334213206
4096 | 327 | 1.089993658027979 | 1.0828494637447525
The adjacent decreases hold, but both points are above 1 for all these finite u. This explicitly illustrates that the eventual floor rule is not a claim for these sizes. No numeric onset or independent review was established.

Reproduce:
```python
from math import comb,isqrt
from fractions import Fraction

def moments(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        a.append(a[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return a

def conv(a,b,g):
    return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0

def counts(u,q):
    d=u-q;m=u+q;g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    Q=conv(A,B,d-1);S=Q+conv(A,B,d)+q*(conv(a,B,d)+conv(a,B,d-1))
    P=sum(comb(3,j)*conv(a,b,d+1-j) for j in range(4))
    return S,P,Q

def K(u,q):
    S,P,Q=counts(u,q)
    return Fraction(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))

def T(u,q):
    D=4*u+2*q+1;H=u+2*q+1;L=3*u+q+1
    return Fraction(9*u*u*L*L*D,(3*u*q*H+D*D)**2)

def center_floor(u):
    return (isqrt(324*u)-169)//3

if __name__=='__main__':
    n=0
    for u in range(11,257):
        for q in range(u//2):
            assert T(u,q+1)*(q+7)<=T(u,q)*(q+6)
            n+=1
    print('rational surrogate adjacent comparisons',n)
    for u in (256,1024,4096):
        q=center_floor(u)
        a,b=K(u,q),K(u,q+1)
        print(u,q,float(a),float(b),a>b)
```

## 6. Continuation

The mother problem of exact finite-u monotonicity for all q is still open; HB covers initial gaps 2..48, HC proves Q/S and W decreasing, HD adds an eventual low-q wedge and settles eventual single sign transition on the entire domain. Next investigate a sharper uniform GU expansion with O(1/u) or smaller controlled error, preferably a second-order critical expansion, to resolve the integer resonance set and obtain an effective onset. The middle-region monotonicity question remains separately useful. The compression T is a controlled total-count observer only; the original BRC joint port coordinates and path data are retained in source; no claim of state equivalence or physical transfer.