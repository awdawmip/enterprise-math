# D25 / H40 dual Clausen ports: new prime-power valuation strata

Date: 2026-11-11. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Status: **AUTHOR_SIDE / FINITE_EXACT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.
Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Task/publication: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT` / `TP2-B6F4FC938FF94941C1B7`.
Frozen scientific source: `c47e13e4aba0e006366f989d6334d443f6333ae3` (not repinned).
The named two-port input is from the distinct H40 2026-11-11 composite-CRT author note `research_notes/portable_direct/2026-11-11_h40_d25_composite_crt_two_port_author_portable.md`; original authorship is retained. This note supplies NEW finite prime-power observations rather than recrediting H40's all-integer CRT lemma or its 2001-case scan.

## Exact objects and finite theorem

For integer `m>=0`, `e in {0,1}`, `N=6m+1+4e>=5`, let

```
c_k = 2^(m-k) binom(m,k) binom(2m+e,k)  (0<=k<=m)
U = sum_k c_k
V = sum_k (1-6e+12k)c_k
```

These are **labeled original finite Clausen ports**, not the native H0/B0 `[X]U` operator and not the original W216 weighted sum.

**Exact exhaustive result on a specified finite prime-power domain:**
For every prime `5<=p<=167`, every integer `r>=1` such that `p^r<=2,000,000`, and the unique `(m,e)` such that `p^r=6m+1+4e`, all of the following were verified by exact integer modular arithmetic.

Write `chi=(-6/p)`, with `v_p(0 mod p^r)` recorded as the truncated value `r`:

* If `chi=+1` (p mod 24 in 1,5,7,11), `v_p(U mod p^r)=0` and `V=0 mod p^r`.
* If `chi=-1` (p mod 24 in 13,17,19,23), the truncated valuations are exactly `v_p(U)=ceil(r/2)`, `v_p(V)=floor(r/2)`.

Consequently `UV=0 mod p^r` in every case of the declared finite domain. There are **37 primes and 124 distinct prime-power cases**: 65 with chi=+1, 59 with chi=-1. Exactly **60** cases have `m>1000` and lie outside H40's earlier m<=1000 scan. **52** cases with m<=300 were independently re-evaluated using Python `math.comb` big integers, and agree with the p-adic modular recurrence; all tests passed.

The observed two-class valuation law for *arbitrary* primes and exponents is a **new conjectural extension**, not a proved unbounded theorem.

Representative complete modular certificates:

| p^r | e | m | U mod p^r | V mod p^r | truncated (v_p U, v_p V) |
| ---: | ---: | ---: | ---: | ---: | :---: |
| 5^9=1953125 | 1 | 325520 | 1423641 | 0 | (0,9) |
| 11^6=1771561 | 0 | 295260 | 583188 | 0 | (0,6) |
| 13^5=371293 | 0 | 61882 | 96668 | 117793 | (3,2) |
| 17^5=1419857 | 1 | 236642 | 9826 | 590716 | (3,2) |
| 37^4=1874161 | 0 | 312360 | 1026750 | 1701667 | (2,2) |

## Exact proof of finite checkability

The coefficient ratio holds as an identity in rational integers, with each `c_k` an actual integer:

```
c_0=2^m
c_(k+1)/c_k = (m-k)(2m+e-k)/(2(k+1)^2).
```

At a fixed p^r, store `c_k=p^v u` where u is a p-unit mod p^r. Strip the p-powers from numerator and denominator *before* modular division. The remaining denominator `2*((k+1)/p^v_p(k+1))^2` is a unit because p>3; update `v` by the exact exponent difference. Thus every modular `c_k`, U and V is computed with only exact integer operations. The program asserts all intermediate c_k have nonnegative p-adic valuation, checks `UV%N==0`, and checks the displayed strata case by case. An independent `math.comb` computation validates 52 smaller cases.

Local raw 124-record JSON generated with SHA-256
`a9d5f63d42452f9452ce342b178a671167c8cae6e8ce78d829f251ac8e2a7a10`.
The JSON bytes are a local research artifact; **the companion GitHub program regenerates the complete 124-record certificate**.

## BRC relevance and next precise scientific question

The joint typed observable `(p,r,chi,v_p(U),v_p(V),U mod p^r,V mod p^r)` preserves named-port and prime-power information which the scalar `UV mod p^r` erases. This is a concrete BRC observer stratification, with actual finite evidence in both ordinary and inert `D=-24` arithmetic classes.

Next local mathematics: prove or find an exact counterexample to the all-prime-power valuation law, with particular attention to `chi=-1` where U and V split powers ceil/floor; use a p-adic Dwork/CM recurrence only after verifying that it truly represents the same two integer ports. H40's original universal `N|UV` conjecture remains a distinct higher target.

**Native parent remains NOT_RUN:** the frozen same-original-class H0/B0 divided-power `[X]U mod139129` at p=373, true module rank, semilinear Frobenius direction/basis eta, odd signed Green/Hesse kappa, original Delta-R and independent replica. Existing source support issue #1559 remains the execution-owner path. The present finite dual-port strata are *not* a native experiment, authorized Task CLAIM, Source checkpoint, Result or independent review.

## Control/source boundary

Last exact Source task read `onhour-20261111-nexttask-read-1900` returned `SUCCEEDED` at Source `2d258707eb0e68509e79b3bb0b676398dabeb9cf` (as-of 2026-11-11T11:06:02Z): `HANDOFF_READY/NEEDS_DISPATCH`, no active owner, canonical typed predecessor continuation with unchanged high frontier. The prior bridge `recovery_status` #6759 recovered only its old `REGISTRATION_FAILED` session, no winning CLAIM/open. This report is independent GitHub author-side material; no role-bound mutation has been attempted and the maintenance logical conversation has not been used.

## Additional exact Jacobi-jet representation (all integers m, e)

The classical binomial definition of Jacobi polynomials gives the **exact** identity, not a prime-power observation,

```
P(x) = P_m^(0,m+e)(x)
     = sum_(k=0)^m binom(m,k)binom(2m+e,k)
         ((x-1)/2)^k ((x+1)/2)^(m-k).
U = P(3).
4 P'(3) = m U + sum_(k=0)^m k c_k.
V = 48 P'(3) + (3+2e-2N)P(3).
```

This is proved termwise: at x=3, the summand is c_k and its derivative is (m+k)c_k/4. Since N=6m+1+4e, the last equality follows from V=(1-6e)U+12 sum k c_k. Therefore modulo *any* N of this form,

```
U V ≡ P_m^(0,m+e)(3) * [48 P_m^(0,m+e)'(3)
                          +(3+2e)P_m^(0,m+e)(3)] (mod N).
```

This is a precise, same-named-port **Jacobi value/derivative reduction** of the H40 composite conjecture. It retains the prime-power BRC coordinates when evaluated over Z/p^r. SymPy's standard Jacobi definition independently matched all 12 exact integer pairs (m=1..6, e=0,1); the displayed equations are also proved by the binomial formula. The next analytical direction is to study the p-adic divisibility of this Jacobi value and its stated derivative combination, including the observed inert ceil/floor split. No ordinary JET2/native-crystal identification follows from this algebra alone.
