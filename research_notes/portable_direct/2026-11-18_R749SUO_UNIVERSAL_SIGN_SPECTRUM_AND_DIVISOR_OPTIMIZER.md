# R749SUO — Universal sign spectrum and divisor-sieve optimizer for labeled two-Port feedback

Date: 2026-11-18 (Asia/Shanghai). Evidence: `AUTHOR_EXACT_NOT_REVIEWED`.
Scope: **auxiliary** positive-rational WBRC-T30–T32 labeled two-Port feedback-bin observer. No native X6 event admission, shared Task CLAIM, Result, Review, or Foundation promotion.

## Source pins and provenance

- Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30–T32).
- Exact predecessor: [R749SUN](https://github.com/awdawmip/enterprise-math/blob/63d7a97464f9516cbd5f3463540f30c1ebe5ecb4/research_notes/portable_direct/2026-11-18_R749SUN_UNIVERSAL_TWO_PORT_OPTIMAL_DEFECT_CLASSIFICATION.md), source `63d7a97464f9516cbd5f3463540f30c1ebe5ecb4`. Reuses the complete finite R749SUK certificate at `0b292a4181f3729b2bda282cf35e6df2166531e5`.
- Current P000 and ACTIVE worldview remain intact: the rational two-Port matrix is a typed auxiliary observer, neither a native two-dimensional spatial plane nor primitive two-force balance. Native X6 triadic and causal permissions require their own typed bridge.

For each integer `M>=2`, define

```
U_M = {(a,u,v,d) in {1,...,M}^4 : a*d-u*v=1},
tau(a,u,v,d) = max(u,v)*a*d,
Q(a,u,v,d) = u+v-a-d.
```

The `Q=0` fiber is precisely the adjacent-diagonal canonical family (R749SUK), excluded below. Let `Opt(M)` be **all labeled noncanonical global maximizers** of `tau`, including ties.

## Theorem A — exact universal sign classification

Define

```
E_minus = {2,3,4,5,6,7,9,10,13,16,21,22,33,37,46,61,86,115}
E_tie   = {5,6,7,9}
E_two   = {58,93}
```

Then for **every integer M>=2** the full set of optimal defects is

```
{Q(A) : A in Opt(M)} =
  {-1,+1}  if M in E_tie,
  {-1}     if M in E_minus \ E_tie,
  {+2}     if M in E_two,
  {+1}     otherwise.
```

In particular, **Q(A)=+1 for every A in Opt(M) and every M>=116**. Exactly 18 integer scales have a negative optimum; four of these also have positive-unit ties.

### Infinite-range proof for every M>=9999

Use R749SUN's pinned and explicitly verified near-product competitor. Set `t=floor(sqrt(M+1))>=100` and `x=sqrt(t)>=10`. Orient each maximizer so `u=max(u,v)`, preserving both score and Q. Put

```
h=M-u,  R=M-a,  T=M-d,  S=h+R+T,
B=2t+6sqrt(t)+13.
```

R749SUN Lemmas 1–2, using its determinant-one near-product construction and AM–GM product comparison, establish `S<=B` and `u>=M-B`. Its Lemma 3 proves the prior universal `|Q|=1` in this range.

We now exclude `Q=-1`. The exact determinant identity is

```
(u-a)(u-d)=u*Q+1.
```

For `Q=-1`, since `u>=M-B>1`, the right side `1-u` is strictly negative. Exchange a,d if necessary and set `u-a=X>0` and `u-d=-Z<0`. Then `XZ=u-1`. Because `d=u+Z<=M`, `h>=Z`. Also `R=h+X` and `T=h-Z`, hence

```
S=3h+X-Z >= 2h+X >= 2sqrt(2hX) >= 2sqrt(2(u-1)).
```

The first bound uses `h>=Z`, the AM–GM bound applies to `2h+X`, and `hX>=ZX=u-1`. Squaring yields `B^2>=S^2>=8(u-1)>=8(M-B-1)`.

However `M>=t^2-1=x^4-1`, and the following **exact polynomial identity** holds:

```
8(x^4-2-(2x^2+6x+13))-(2x^2+6x+13)^2
 =4x^4-24x^3-104x^2-204x-289
 =4(x-10)^4+136(x-10)^3+1576(x-10)^2
  +6516(x-10)+3271 > 0       for x>=10.
```

Thus `B^2<8(M-B-1)`, a contradiction. This proves `Q!=-1`; combine with R749SUN's `|Q|=1` to conclude `Q=+1` for **every M>=9999**.

### Exact finite closure for M=2..10000

The companion C++17 certificate enumerates **every oriented** noncanonical determinant-one tuple with `1<=a,u,v,d<=10000`. For `u>=v`, the congruence `ad=1 (mod u)` implies `gcd(a,u)=1` and enumerates all admissible `d` via its modular inverse; the remaining entry is `v=(ad-1)/u`. The `u=1` case is handled directly. Off-diagonal transposition `u<->v` retains `tau` and `Q`, so orientation does not remove a sign or tied maximum.

Each tuple enters the bucket `L=max(a,u,d)` (the fourth entry `v<=u`). Prefix maxima over `M` therefore recover **all** labeled maxima. Every arithmetic operation is exact signed 64-bit integer arithmetic within the declared bound. A separately implemented `(a,d,u)` brute enumeration crosschecks all 119 scales `M=2..120`, including both score and complete Q set/tie count.

Observed exact `PASS`: 60,779,744 oriented noncanonical tuples; negative set `E_minus`, mixed-sign set `E_tie`, and `Q=2` set `E_two`. The finite range overlaps the analytic range at `M=9999,10000` and completes the universal theorem.

## Theorem B — nearest-divisor optimizer and **all labeled maximizers**

For any `M>=116`, Theorem A gives `Q=+1`. Orient `u=max(u,v)` and let `x=u-a`, `y=u-d`. Then `xy=u+1>0`. Both factors are positive: if both were negative, `a,d>u>=v` would imply `Q<0`. Set `n=xy=u+1`. Substitution gives the **complete inverse representation**

```
(a,u,v,d) = (n-x-1, n-1, n-x-y, n-y-1)
x,y>=2,  xy=n<=M+1,  n-x-y>=1.
```

Conversely every such factor pair defines a valid positive determinant-one `Q=+1` tuple: direct expansion gives `ad-uv=1`. Thus the parameterization is bijective for oriented named configurations.

At fixed `n=xy`, the score is

```
f(n,x,y)=(n-1)[(n-1)^2-(n-1)(x+y)+n].
```

Hence maximizing at fixed n is minimizing `x+y`. Among divisors `x<=sqrt(n)`, this is attained uniquely at the **largest divisor** `x_n` with `2<=x_n<=sqrt(n)`; let `y_n=n/x_n`. The closest-factor pair is feasible for every composite `n>=6`. Consequently

```
T*(M) = max over composite 6<=n<=M+1 of
        (n-1)*(n-x_n-1)*(n-y_n-1),      M>=116.
```

For every maximizing n, form the displayed tuple, exchange x_n and y_n if distinct (diagonal labels), and exchange u and v (directed Port labels). These are **all** labeled maxima. Their contribution is 2 configurations if `x_n=y_n`, otherwise 4; ties between distinct n add multiplicities.

A sieve computes all closest divisors for `n<=M+1`:

```
for x=2,...,floor(sqrt(M+1)):
    for n=x*x, x*x+x, ... <=M+1:
        x_n=x
```

Since x increases, the last assigned divisor is the closest one. Summed work is `O(M log M)` integer arithmetic operations and `O(M)` integer words; arbitrary-precision multiplication carries its separate `O(log M)`-bit operand cost. This replaces the general modular-inverse candidate search for all `M>=116`.

**Independent algorithm validation:** the same executable implements this divisor sieve and compares **both optimum score and total number of labeled maximizing matrices** against complete modular-inverse enumeration at all 9,885 scales `M=116..10000`; every test passed.

| M | maximizing n and factor pair | T*(M) | one oriented labeled maximizer |
|---:|---|---:|---|
| 116 | n=117, (9,13) | 1,278,436 | (107,116,95,103) |
| 120 | n=121, (11,11) | 1,425,720 | (109,120,99,109) |
| 10000 | n=10000, (100,100) | 979,804,019,799 | (9899,9999,9800,9899) |

## Reproducibility, evidence and unresolved interface

- The executable `R749SUO_SIGN_DIVISOR_CERT.cpp` compiles with `g++ -O3 -std=c++17` and runs without inputs (default M<=10000). Its exact output is `R749SUO_SIGN_DIVISOR_RESULTS.json`. No floating-point arithmetic enters the finite sign search, sieve scores, or comparisons.
- Proof scope: all integer M>=2 in the auxiliary labeled rational Port model. Current level `AUTHOR_EXACT_NOT_REVIEWED` (reproducible author proof and exact finite verification).
- The native X6 bridge remains a separate research question: identify a **source-pinned triadic Cell/Link/Port event**, verify resource permission and causal-time transition, and exhibit a future-context / labeled-provenance preserving observer map.
- Next number-theoretic question: characterize the maximizing products n and the gaps `M+1-n`, and seek sublinear certified optimization in specified regimes. Closest-divisor arithmetic is a new exact tool for this task.
- Historical R2 provenance `EM-DIRECT-44C346` / `RA-A16A5E663104EBDBA287C665`; this independent document does not assert a fresh native CLAIM or authenticated session.
