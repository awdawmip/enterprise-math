# PREFIX-1084 — Exact signed tail closure and a computable global negative-tail certificate

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED.
Independent R6 continuation of PREFIX-1083. Own session metadata recovered for MCP-f6d93209fc8e4c5bb2c3b44f69a47174 / EM-DIRECT-780BBE / TASK_RESEARCH, Activity RA-0ABD84561C86E53067DB0322. Current owner inventory request r6-20261125-1852-owner-read was RUNNING at the last observation before this note; no new CLAIM or shared Task mutation. Registration metadata does not grant Task authority.
Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; unchanged Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full paired Cell, signed phase, ports and ordered multiplicity are retained. All x, CT and Haar/character variables below are auxiliary readouts of the inherited paired BRC, not native spatial or time coordinates.

Parents:
- 9c37e17bb751d6ce506762884e349e8bc20f2d7f:research_notes/portable_direct/2026-11-25_r6_prefix1083_finite_two_bin_certificate.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md
- inherited exact residual transport from PREFIX-1077/1078.

## 1. Exact signed tail from r observations, with no infinite terminal scan

Let m>=0, r>=1, M=m+r, k>=3 be integers and D_m(k)>0. Put x=SB/36, c0=1/(4*36^8). For integer U>=1 let the grouped signed tail be
    S_U = sum_(u>=U) binom(u+r-1,r-1) D_M(k+u)/D_m(k).
The exact identity is
    S_U = [sum_(j=0)^(r-1) binom(U+j-1,j) D_(m+j)(k+U)]/D_m(k).
Proof: D_i(Q+1)=D_i(Q)-D_(i+1)(Q). For r=1 use the telescoping transport identity. For r>1, summation by parts with c_u=binom(u+r-1,r-1) gives c_U D_(M-1)(k+U) plus sum_(u>U)(c_u-c_(u-1))D_(M-1)(k+u), divided by D_m(k). Since c_u-c_(u-1)=binom(u+r-2,r-2), this is the (r-1)-layer tail at U plus binom(U+r-2,r-1) D_(M-1)(k+U)/D_m(k). Induction proves the formula; the boundary at infinity vanishes by the inherited fixed-index positive-tail asymptotic (alternatively the absolute estimate below). It gives an exact rational signed tail, not a bound on absolute or negative tail by itself. Its term count does not depend on an upper terminal cutoff, although computing each D can still cost substantial resources.

## 2. Newton separation of the parameter-dependent paired carrier

In PREFIX-1082, D_M(0)=c0 CT[K(M+8)x^M], and D_M(Q)=sum_(l=0)^Q (-1)^l binom(Q,l) D_(M+l)(0). Freezing K at M inside the Q-th difference would be incorrect: its coefficients depend cubically on n. Let sigma swap axes 0 and 1 (z->c^(-1), c->z^(-1), S,B unchanged), Kbar=(K+sigma K)/2, and P_d(M)=Delta_n^d Kbar evaluated at n=M+8. Radial CT invariance gives exactly the same observation with Kbar. The finite Newton expansion, since deg_n K<=3, gives
    D_M(Q)=c0 sum_(d=0)^min(3,Q) (-1)^d binom(Q,d)
                    CT[P_d(M) x^(M+d)(1-x)^(Q-d)].
Proof: Kbar(M+8+l)=sum_d binom(l,d)P_d(M). Substitute and use binom(Q,l)binom(l,d)=binom(Q,d)binom(Q-d,l-d), followed by the binomial theorem. No derivatives, root rounding or replacement of the native carrier are required.

Exact Laurent expansion of 2*Kbar has 84 nonzero monomials S^a B^b z^v c^w and every a+b>=6 (the original K has 66). This is the radial exchange cancellation in PREFIX-1073/1075, now retained in an integer coefficient observer. Let P_d(M)=sum p_(a,b,v,w) S^a B^b z^v c^w, with rational p, and define
    L_d(M)=c0 sum |p_(a,b,v,w)| 6^(a+b).
On the unit characters, |S|=|B|<=6 and |z|=|c|=1, so c0|P_d(M)|<=L_d(M) x^3. For the positive radial moment R(i,Q)=CT[x^i(1-x)^Q], this yields the rigorous bound
    |D_M(Q)| <= sum_(d=0)^min(3,Q) L_d(M) binom(Q,d) R(M+d+3,Q-d).
The loss of signed cancellation in the coefficient l1 bound is explicit. It is an error envelope only; no native state or signed observation is replaced.

## 3. A finite rational certificate for the complete unscanned tail

For U>=4, define
    A_U = 1/D_m(k) *
      sum_(d=0)^3 sum_(e=0)^d L_d(M) binom(k,d-e) binom(r+e-1,e)
      * sum_(j=0)^(r+e-1) binom(U-e+j-1,j)
          R(m+d-e+3+j,k+U-d).
Then
    sum_(u>=U) binom(u+r-1,r-1)|D_M(k+u)|/D_m(k) <= A_U,
    0 <= N_tail(U) <= (A_U-S_U)/2.
Here N_tail(U) sums the actual negative parts of the grouped law. The second bound is the exact relation negative part=(absolute value-signed value)/2 combined with the first.

Proof of the finite expression: apply the bound in section 2. Expand binom(k+u,d)=sum_e binom(k,d-e)binom(u,e), use binom(u+r-1,r-1)binom(u,e)=binom(r+e-1,e)binom(u+r-1,r+e-1), and set v=u-e. For h>=1, V>=1 and 0<x<=1,
    x^h sum_(v>=V) binom(v+h-1,h-1)(1-x)^v
      =(1-x)^V sum_(j=0)^(h-1) binom(V+j-1,j)x^j.
This negative-binomial tail identity follows from the geometric series and induction on h (or from the event that fewer than h successes have occurred before the V-th failure in Bernoulli trials). Use h=r+e, V=U-e, multiply by x^(M+d+3-h)(1-x)^(k+e-d), and apply CT/integration. All exponents are nonnegative; the formula extends to x=0 by its limit and the full integrand has vanishing factor x^(m+d-e+3). Nonnegative summation permits Tonelli, and the integrated bound is finite. No assumption of a global ordinary signed spectral density is needed. There are at most sum_(d=0)^3 sum_(e=0)^d (r+e)=10r+10 radial terms before deduplication. R is exactly rational from the six-axis zero-shift CT table and the same integer difference recurrence as PREFIX-1082.

For fixed m,k,r, A_U is nonincreasing and tends to zero: it is the exact sum of the nonnegative envelopes over u>=U, whose total is finite by the same NB kernel identity. In fact, the inherited bounded zero-edge radial density (PREFIX-1073/1075, p_1 continuous) gives R(i,Q)=O_i(Q^(-i-1)) as Q->infinity for fixed i, by splitting a fixed zero neighborhood and its exponentially small complement. Each term above is O(U^(-m-d+e-4)), hence A_U=O_(m,k,r)(U^(-m-4)). The decay is a fixed-parameter statement, not a uniform resource bound when r or k grows. It supplies a convergent global negative-tail certificate without first locating p or the final negative index.

If N_fin is the exact negative mass of 0<=u<U, the full mass satisfies
    N_fin <= N_full <= N_fin+(A_U-S_U)/2.
Consequently the distance from the full signed normalized law to the probability simplex lies between 2N_fin and 2N_fin+A_U-S_U. This upgrades the finite-only lower bound in PREFIX-1083 to a finite, computable, two-sided global bound. If a nonempty selected set of negative bins has exact retained mass R0 and omitted known finite mass B0, the total variation error of its normalized negative-mass approximation is between B0/(R0+B0) and (B0+(A_U-S_U)/2)/(R0+B0+(A_U-S_U)/2). Thus one can certify adaptive truncation against a requested tolerance when the bound is small enough, without an assumption about the number of later sign changes. It cannot certify strict absence of negative tail merely from a small positive upper bound.

## 4. Exact executed checks and a quantitative limitation

The actual local Python/SymPy run used the unchanged parent 66-term polynomial and eight shift classes, N=380, checked first eight A_m, and verified the exchange symmetrization in ten CT values. All 48 exact Newton expansion comparisons (M=0..5,Q=0..7) passed. For (m,r,k)=(0,1,115),(0,3,150),(0,5,205), U=4,5,10,20,40,80,120, verified exact differences S_U-S_V against direct finite grouped signed sums, A_U-A_V >= corresponding direct absolute sums, and (A_U-S_U)/2-(A_V-S_V)/2 >= direct negative sums. 18 finite intervals, 348 grouped bins including overlaps across different parameter choices. Each comparison used Fraction arithmetic; no classical trig/pi numerical evaluation or native kernel re-enumeration.

r | k | U | S_U (rounded) | A_U (rounded) | upper negative tail (rounded)
1 | 115 | 4 | 1.0580544810 | 443137.5649 | 221568.2534
1 | 115 | 120 | .2046283407 | 33461.68434 | 16730.73986
3 | 150 | 4 | 1.0002059568 | 524045.9555 | 262022.4776
3 | 150 | 120 | .6364859094 | 249806.7715 | 124903.0675
5 | 205 | 4 | 1.000000008384 | 751464.5133 | 375731.7567
5 | 205 | 120 | .9222119606 | 659478.6490 | 329738.8634

For M=1 the four exact L_d are 34493507/629856,469861/17496,1207/162,8/9; for M=3 they are 73016315/629856,746125/17496,1495/162,8/9; for M=5 they are 132549875/629856,1084597/17496,1783/162,8/9. Exact rational output digest (decimal-string Fraction records described below): d1a3b16da01c462e8a1a7d0b1c23d82bede9fe94b5ac3abd15246f5a5572ffc0.

Important negative result: although the bound is finite and converges eventually, this coefficient-l1 envelope is very loose (upper bounds ~10^4--10^5 here), so it does NOT yet certify practical two-bin compression for the tested windows. The signed tail can exceed one in a signed law. Cancellation of the joint carrier before absolute bounding is the important remaining computational objective. No measured runtime/precision reduction is claimed.

## 5. Reproduction

Run PREFIX-1082 section 4 through the construction of A, changing Nmax=1200 to Nmax=380. The original digest assertions concern a different triangle and are not executed. Its coefficients/tables and K are reused unchanged. The following suffix reproduces the new exact checks and the rational digest. The integer tables in the actual run were built with Jmax=N+12 (rather than parent N+10); either covers all accessed indices.

```python
from fractions import Fraction as F
N=Nmax
K2=sy.expand(K+K.xreplace({z:1/c,c:1/z}))
def coeffs(K):
    out=defaultdict(lambda:0)
    for term in K.as_ordered_terms():
        powers=term.as_powers_dict()
        key=tuple(int(powers.get(v,0)) for v in (S,B,z,c))
        out[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
    return {k:sy.Poly(sy.expand(v),n) for k,v in out.items() if sy.expand(v)!=0}
sym=coeffs(K2)
assert len(coeff)==66 and len(sym)==84
assert all(u+v>=6 for u,v,a,b in sym)
assert {canonical((-a,b,0,0,0,0)) for u,v,a,b in sym}<=ks
def ct(power,pol,at):
    val=0
    for (u,v,a,b),p in pol.items():
        d=(-a,b,0,0,0,0); j=power+u-sum(max(x,0) for x in d)
        assert j==power+v-sum(max(-x,0) for x in d)
        if j>=0: val+=int(p.eval(at))*tables[canonical(d)][j]
    return val
assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
assert all(ct(m,sym,m+8)==2*A[m] for m in range(10))
C=tables[(0,0,0,0,0,0)][:N+1]
rows={m:[] for m in range(8)}; pos={i:[] for i in range(3,12)}
cur=A[:]; rad=C[:]
for Q in range(N+1):
    for m in rows:
        if m<len(cur): rows[m].append(cur[m])
    for i in pos:
        if i<len(rad): pos[i].append(rad[i]); assert rad[i]>=0
    cur=[36*cur[i]-cur[i+1] for i in range(len(cur)-1)]
    rad=[36*rad[i]-rad[i+1] for i in range(len(rad)-1)]
def D(m,Q): return F(rows[m][Q],4*36**(8+m+Q))
def R(i,Q): return F(pos[i][Q],36**(i+Q))
def coeffbound(M,d):
    return F(sum(abs(sum((-1)**(d-j)*comb(d,j)*int(p.eval(M+8+j))
                         for j in range(d+1)))*6**(u+v)
                 for (u,v,a,b),p in sym.items()),8*36**8)
for M in range(6):
    for Q in range(8):
        got=F(0)
        for d in range(min(3,Q)+1):
            val=sum((-1)**(d-j+v)*comb(d,j)*comb(Q-d,v)*
                    F(ct(M+d+v,sym,M+8+j),36**(M+d+v))
                    for j in range(d+1) for v in range(Q-d+1))
            got+=(-1)**d*comb(Q,d)*val/F(8*36**8)
        assert got==D(M,Q)
exact=[]; count=0
for r,k in [(1,115),(3,150),(5,205)]:
    m=0; M=r; den=D(m,k); assert den>0
    L=[coeffbound(M,d) for d in range(4)]
    def tail(U):
        Q=k+U
        a=sum(comb(U+j-1,j)*D(m+j,Q) for j in range(r))/den
        b=sum(L[d]*comb(k,d-e)*comb(r+e-1,e)*comb(U-e+j-1,j)*
              R(m+d-e+3+j,Q-d) for d in range(4) for e in range(d+1)
              for j in range(r+e))/den
        assert b>=abs(a)
        return a,b,(b-a)/2
    us=[u for u in [4,5,10,20,40,80,120] if k+u+r+6<=N]
    for U,V in zip(us,us[1:]):
        a,b,neg=tail(U); a2,b2,neg2=tail(V)
        finite=[comb(u+r-1,r-1)*D(M,k+u)/den for u in range(U,V)]
        assert a-a2==sum(finite)
        assert b-b2>=sum(abs(x) for x in finite)
        assert neg-neg2>=sum(max(0,-x) for x in finite)
        count+=len(finite)
    for U in [us[0],us[-1]]:
        a,b,neg=tail(U)
        exact.append([r,k,U,[str(x) for x in L],str(a),str(b),str(neg)])
assert count==348
digest=hashlib.sha256(json.dumps(exact,separators=(',',':')).encode()).hexdigest()
assert digest=='d1a3b16da01c462e8a1a7d0b1c23d82bede9fe94b5ac3abd15246f5a5572ffc0'
```

## 6. Next

Sharpen the global envelope before absolute values by exploiting exact radial exchange averaging beyond a single swap and the inherited effective density's certified positive zero-edge contribution. A rigorous spectral p,d enclosure or a cheaply certified slope envelope for PREFIX-1083 remains open. Use exact signed tail identity for global mass bookkeeping; distinguish a mathematically convergent but loose certificate from a practical precision guarantee. Mother objective B_fix,odd(32) remains open. No formal checker or independent review was executed.
