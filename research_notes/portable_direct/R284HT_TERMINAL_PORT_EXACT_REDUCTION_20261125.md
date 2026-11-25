# R284HT — Exact terminal-port reduction and effective high-deficit curvature

2026-11-25. Author proof and exact finite checks, NOT_REVIEWED. Independent continuation of the auxiliary binary-tag safe-word total-count observer, not native physical attribution or a full-K monotonicity proof. Frozen scientific input: 4615ee75b8864a47efa5c1d3e0493eb08a1844e5:research_notes/portable_direct/R284HS_BALANCED_CRITICAL_CURVATURE_20261125.md (definitions and previous eventual low/middle-deficit theorem). Current account entry blobs verified together at 0eab621d5e347a59c153ea1a1a0263645e974ccf; continuation protocol, portable protocol, P000 V5, ACTIVE worldview, joint preservation and residual constraints read on main. Own recovery r1-20261125-1800-own-recovery confirms original open RESEARCHER session MCP-8cd6c4fa26b9459d923ff73ba0082220, original registration SUCCEEDED and custody not revoked; RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Metadata only, no shared CLAIM. Owner inventory r1-20261125-1800-owner-inventory SUCCEEDED, fixed Source 63f55d53133320dc3874be442ccaa2b152024799, as_of 2026-11-25T09:59:46.765253Z, no LEASED entries (Source changed at completion, no live write authority). No other actor's task state changed.

## Results

Use M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n, zero elsewhere. C_g=sum_k M_n(k)M_m(g-k), A_g=C_g/[M_n(0)M_m(0)binom(g+3,3)], r_g=A_(g+1)/A_g. Let t=min(n,m), T=max(n,m), S=2(n+m+2), j=n+m-g.

1. Exact formula for T-1<=g<=n+m:
   C_g=R_g=binom(S,j)[4(g+2)^2-S]/[S(S-1)].
   For t>=1 and max(1,T-1)<=g<=n+m-2, r_g-r_(g+1)>1/(5S), regardless of capacity ratio. No asymptotic threshold in this terminal region.
2. For t>=2048, T<=2t, t/2<=g<=n+m-2, r_g-r_(g+1)>1/(56t). Explicit onset for the entire high-deficit band, including g below T-1.
3. Combined with frozen HS (author proof, not independent review), for sufficiently large t and T<=2t all valid 0<=g<=n+m-2 have r_g-r_(g+1)>1/(200t). The effective onset of the lower band remains unresolved; this does not prove complete K monotonicity.

## Proof: exact signed-extension identity and retained truncation residual

Set N=n+1, M=m+1, S=2(N+M). Let J count first-class objects in a uniform j-subset of S objects, with classes of sizes 2N and 2M. Write v=(1-J/N)(1-(j-J)/M). The true count divided by binom(S,j) is E[v 1_{J<=n, j-J<=m}]. The full signed extension is E[v]. By counting a specified sampled object or an ordered pair across classes, E J=j(2N)/S, E(j-J)=j(2M)/S, E[J(j-J)]=j(j-1)4NM/[S(S-1)]. Thus E v=1-4j/S+4j(j-1)/[S(S-1)]=[4(g+2)^2-S]/[S(S-1)]. If j<=t+1, the only omitted nonzero-support branches have J=N or j-J=M and therefore zero weight; the exact formula follows. In general 0<=j<=n+m=N+M-2, the two factors cannot both be negative. Every omitted term is nonpositive (zero on first forbidden layer). Therefore C_g=R_g+E_g where E_g>=0 is the exact negative signed-extension mass with its sign reversed. On the hypergeometric support both factors have magnitude <=1, hence
  0<=E_g/binom(S,j)<=Pr(J>N or j-J>M).
The signed extension is an algebraic auxiliary observer, not a cancellation of distinct positive physical branches. The true joint population remains available.

## Proof: rational ratio and its curvature

Where R_g>0 set b_g=j/(S-j+1), c_g=(g+1)/(g+4), a=S/4, d_g=((g+3)^2-a)/((g+2)^2-a). Then the ratio of the normalized signed extension is s_g=b_g c_g d_g. Whenever g+2>sqrt(a), d_g>1 and decreases strictly: the derivative of log(x^2-a) is 2x/(x^2-a), strictly decreasing for x>sqrt(a); the log of d is its integral over a unit interval.
For j>=2,
  b_g-b_(g+1)=(S+1)/[(S-j+1)(S-j+2)]>1/S,
  b_(g+1)/(b_g-b_(g+1))=(j-1)(S-j+1)/(S+1)<=j-1,
  c_(g+1)-c_g=3/[(g+4)(g+5)].
Consequently b_g c_g-b_(g+1)c_(g+1) >= (b_g-b_(g+1))c_g [1-3(j-1)/((g+1)(g+5))].
In the exact terminal band, j<=t+1<=g+2, so the bracket is at least (g+2)/(g+5). For g>=1, c_g times this bracket is >=1/5. R_g=C_g>0 implies g+2>sqrt(a). Multiplying by the decreasing positive d factors preserves the gap lower bound. This proves result 1.

For t>=50, T<=2t and g>=t/2, S<=7t, j<=3t-g<=5g, g>=25. Now 15g/((g+1)(g+5))<1/2 (equivalent to g^2-24g+5>0, true for g>=25). Also c_g>1/2. The numerator 4(g+2)^2-S>=t^2-7t>=t^2/2, so R_g>0, R_g/binom(S,j)>=1/98>1/100, and g+2>sqrt(a). Thus s_g-s_(g+1)>1/(4S)>=1/(28t). In this range a<= (g+2)^2/2 because S<=7t and g>=t/2, t>=50. It follows d_g<=1+2(2g+5)/(g+2)^2<2; b_g<=1, c_g<=1, hence s_g<2.

## Proof: exponentially paid truncation

For a hypergeometric count J, with p=2N/S, the factorial moments give E[(1+z)^J]=sum_l binom(j,l)(2N)_l/(S)_l z^l <=(1+p z)^j for z>=0 (falling factorials, each sampling factor <=p). Thus for h>=0, E exp[h(J-jp)] <= exp(j h^2/8): the second derivative of log(1-p+p exp(h)) is the variance of a Bernoulli variable and <=1/4, and subtracting ph makes value and first derivative zero at h=0. Markov with h=4b/j gives Pr(J-jp>=b)<=exp(-2b^2/j) for j>0. Same proof for the other class. The mean's distance to N equals N(g+2)/(N+M)>= (g+2)/3>=t/6; the analogous distance to M also satisfies that bound. Since j<=3t, each tail <=exp(-t/54). For j=0 there is no omitted mass. Hence throughout the high-deficit band
  0<=e_g=E_g/R_g<=200 exp(-t/54).
The exact true ratio is r_g=s_g(1+e_(g+1))/(1+e_g). Since e_g,e_(g+1) are nonnegative and <=the common bound, |r_g-s_g|<=400 exp(-t/54). Paying both consecutive ratios yields
  r_g-r_(g+1)>1/(28t)-800 exp(-t/54).
At t=2048, t/54>37, e>2 and 800*56*2048=91750400<2^37. Since t exp(-t/54) decreases for t>54, the last term is <1/(56t) for all t>=2048. This proves result 2. Combining with HS establishes result 3. Only the declared total-count and adjacent ratio observers descend through this reduction; arbitrary joint observables do not.

## Executed exact finite evidence

Python arbitrary precision integers and fractions; decimal display only. Independent computation of the original convolution and closed form, including capacity truncation. The following equivalent replay script enumerates precisely the executed cases (the actual run had one redundant conditional expression for m in the sample set, semantically identical).

```python
from math import comb
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def ports(n):
    return [((k+1)*comb(2*n+2,n-k))//(n+1) for k in range(n+1)]
def C(n,m,g):
    a,b=ports(n),ports(m)
    return sum(a[k]*b[g-k] for k in range(max(0,g-m),min(n,g)+1))
def R(n,m,g):
    S=2*(n+m+2); j=n+m-g
    return F(comb(S,j)*(4*(g+2)**2-S),S*(S-1))
def ratio(a,b,g): return F(b,a)*F(g+1,g+4)
exact=checks=nonzero=0; min_term=None; min_bal=None
for n in range(1,51):
    for m in range(n,51):
        S=2*(n+m+2); t=n
        c=[C(n,m,g) for g in range(n+m+1)]
        for g in range(m-1,n+m+1):
            assert c[g]==R(n,m,g); exact+=1
        for g in range(max(1,m-1),n+m-1):
            gap=ratio(c[g],c[g+1],g)-ratio(c[g+1],c[g+2],g+1)
            assert gap>F(1,5*S); checks+=1
            v=S*gap
            if min_term is None or v<min_term[0]: min_term=(v,n,m,g)
        if m<=2*n:
            for g in range((t+1)//2,n+m+1):
                res=c[g]-R(n,m,g)
                assert res>=0
                nonzero+=res>0
                if g<=n+m-2:
                    gap=ratio(c[g],c[g+1],g)-ratio(c[g+1],c[g+2],g+1)
                    if min_bal is None or t*gap<min_bal[0]: min_bal=(t*gap,n,m,g)
print(exact,checks,min_term,nonzero,min_bal)
for t in (256,2048,4096):
    for m in (t,3*t//2,2*t):
        for g in sorted({t//2,t,m-1,m,t+m-2}):
            c=[C(t,m,g+i) for i in range(3)]; r=[R(t,m,g+i) for i in range(3)]
            assert all(a>=b>0 for a,b in zip(c,r))
            gap=ratio(c[0],c[1],g)-ratio(c[1],c[2],g+1)
            rgap=ratio(r[0],r[1],g)-ratio(r[1],r[2],g+1)
            if t>=2048: assert gap>F(1,56*t)
            assert rgap>F(1,28*t)
            print(t,m,g,round(float(t*gap),8),round(float((c[0]-r[0])/r[0]),8))
```

Actual summary: 24650 exact terminal count identities, 22099 terminal curvature checks, min S*gap=339/344 at (n,m,g)=(1,4,3); 13132 strictly positive truncation residuals in the balanced high-deficit finite band; minimum observed t*gap in that finite band 79/780 at (1,2,1). 42 large-parameter sample comparisons (14 per t=256,2048,4096), all stated assertions passed. Selected output for m=2t:
|t|g|t*(r_g-r_(g+1))|
|--:|--:|--:|
|256|128|0.47284899|
|256|766|0.16623335|
|2048|1024|0.48741067|
|2048|6142|0.16661242|
|4096|2048|0.48859321|
|4096|12286|0.16663954|
The t=256,m=512,g=128 relative correction rounds to 0.00000007 at 8 decimal places; rounded zeros in other samples are not asserted to be exact zero. Finite experiments are checks, not the unbounded proof.

## Next

The balanced-port positive curvature is now eventual across its full support, and the high-deficit half has an explicit onset, with a genuinely threshold-free terminal identity. Seek effective lower-half onset or a direct discrete low/middle-deficit argument; use exact terminal reductions and signed residual rather than repeating critical asymptotics. Full K propagation remains open. Independent review and strict Activity observation audit outstanding.
