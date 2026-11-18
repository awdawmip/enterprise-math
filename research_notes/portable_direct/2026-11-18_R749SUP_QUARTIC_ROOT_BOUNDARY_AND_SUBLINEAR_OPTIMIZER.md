# R749SUP — A quartic-root boundary layer and a sublinear exact two-Port optimizer

Date: 2026-11-18 (Asia/Shanghai). Evidence: `AUTHOR_EXACT_NOT_REVIEWED`.
Scope: auxiliary labeled finite-positive-rational WBRC-T30–T32 two-Port feedback observer; native X6 Cell/Link/Port event admission remains separate.

## Immutable input and dependencies

- Frozen scientific input `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md`.
- The preceding R749SUN near-product competitor and its AM–GM deficit lemma: [R749SUN@63d7a974](https://github.com/awdawmip/enterprise-math/blob/63d7a97464f9516cbd5f3463540f30c1ebe5ecb4/research_notes/portable_direct/2026-11-18_R749SUN_UNIVERSAL_TWO_PORT_OPTIMAL_DEFECT_CLASSIFICATION.md).
- R749SUO in this research branch: complete optimal sign classification; **every** noncanonical labeled maximizer has `Q=+1` for `M>=116`, and a nearest-divisor optimization formula for its score and all ties.

As before, `ad-uv=1`, `1<=a,u,v,d<=M`, `tau=max(u,v)*ad`, `Q=u+v-a-d`, and `Opt(M)` includes all noncanonical named maximizers. Orient by `u=max(u,v)` when convenient.

## Theorem — every maximizer lies in an O(M^(1/4)) top-Port boundary layer

For every integer `M>=9999`, set

```
t = floor(sqrt(M+1)),     k=M+1-t^2,
j = 1 if k<=t, otherwise 2,
z = min{integer z>=0 : z(z+j)>=jt-k},
r=t-z, s=t+z+j, p=rs-1,
delta=M-p.
```

The pinned near-product construction proves `0<=delta<=2ceil(sqrt(t))+1` and gives the admissible determinant-one positive-unit competitor

```
(a,u,v,d)=(p-r,p,p-r-s+1,p-s),
W=p(p-r)(p-s).
```

**New conclusion:** for **each** `A in Opt(M)`, writing `u=max(u,v)`,

```
p<=u<=M,
0<=M-u<=delta<=2ceil(sqrt(t))+1=O(M^(1/4)).
```

In particular the maximizing product `n=u+1` belongs to the **explicit short integer interval** `p+1<=n<=M+1`.

### Proof: control the exact factor-product envelope

R749SUO proves `Q=+1` at every M in the present range, so the oriented factors `x=u-a>0`, `y=u-d>0` satisfy `xy=u+1`. Their arithmetic–geometric mean gives

```
tau=u*a*d <= H(u):=u*(u-sqrt(u+1))^2.
```

The competitor also has `rs=p+1`, hence its exact product deficiency from that continuous envelope is

```
H(p)-W=p^2*Delta,
Delta=(r+s)-2sqrt(rs)=(sqrt(s)-sqrt(r))^2.
```

Put `c=ceil(sqrt(t))`. Since `z<=c`, `s-r=2z+j<=2c+2`, `r=t-z>=t-c`, so

```
Delta=(s-r)^2/(sqrt(s)+sqrt(r))^2
     <=(c+1)^2/(t-c)
     <=(sqrt(t)+2)^2/(t-sqrt(t)-1)<2.
```

The final strict inequality is equivalent to `x^2-6x-6>0` for `x=sqrt(t)>=10`. Thus

```
W>H(p)-2p^2.                   (1)
```

From R749SUN Lemma 2, every maximizer has `u>=M-B` with `B=2t+6sqrt(t)+13`. For t>=100 the exact inequality `20B<M` follows from the positive polynomial `x^4-40x^2-120x-261>0` (x>=10). Therefore

```
u>=M-B>19M/20>=19p/20.
```

Also `p>=t^2-2sqrt(t)-4>=9976>2501`, whence `sqrt(p+1)<=p/50`. Differentiate the exact envelope:

```
H'(w)=3w^2-4w sqrt(w+1)-w^2/sqrt(w+1)+2w+1.
```

For any `19p/20<=w<=p`,

```
H'(w)>=3w^2-5w sqrt(w+1)
     >=3(19p/20)^2-5p sqrt(p+1)
     >=(1043/400)p^2>2p^2.          (2)
```

If a maximizer had `u<p`, integrality would give `p-u>=1`. The mean value theorem and (2) imply `H(p)-H(u)>2p^2`. But the maximizer satisfies `H(u)>=tau(A)>=W>H(p)-2p^2` by (1), contradiction. Therefore `u>=p`. The explicit bound on `delta=M-p` proves the result for **every** M>=9999. QED.

## Algorithm — O(M^(3/4)) arithmetic operations

For each integer M>=9999:

1. Construct the integer near-product witness `p` above (only integer square roots, additions and multiplications).
2. For `n=p+1,...,M+1` find the largest divisor `x_n<=floor(sqrt(n))` by trial division descending from `floor(sqrt(n))` to 2; let `y_n=n/x_n`. Ignore primes and infeasible pairs.
3. Evaluate `(n-1)(n-x_n-1)(n-y_n-1)`, maximize, and generate every labeled optimal matrix via the R749SUO factor/Port swaps.

The theorem proves that **all** optimal products n are inside this window; R749SUO proves that the closest pair maximizes score at fixed n. Its length is `delta+1=O(M^(1/4))`, and each factor search uses at most `O(sqrt(M))` trial divisions, hence

```
O(M^(3/4)) exact integer arithmetic operations,
O(1) auxiliary working memory excluding returned tied optimizers.
```

This bound counts integer operations; exact bit complexity includes `O(log M)`-bit arithmetic. The algorithm does not need a full divisor sieve, probabilistic factorization, floating-point approximation, or a native X6 event claim.

## Exact computational evidence and examples

`R749SUP_QUARTER_ROOT_CERT.py` independently constructs the full nearest-divisor prefix oracle and the short-window optimizer. It compares scores **and total labeled tie counts** for every M in `9999..25000`, a total of **15,002 integer scales**; all tests `PASS` using integer-exact computation. The largest witness gap `delta` observed is 25.

| M | p | optimal n | T*(M) | delta |
|---:|---:|---:|---:|---:|
| 9999 | 9989 | 10000 | 979,804,019,799 | 10 |
| 10000 | 9989 | 10000 | 979,804,019,799 | 11 |
| 25000 | 24989 | 25000 | 15,420,641,299,674 | 11 |

The universal bound is established by the preceding algebra; the finite regression tests the implementation.

## Next scientific frontier

Determine the sharp maximal offset `M-u`, including dependence on the local factorization of M+1 and the near-product competitor; investigate certified faster factor search for short intervals. For transfer into native X6, identify a source-pinned triadic Cell/Link/Port transition preserving named Port provenance, residual, resource permission and causal-time state under future operations. P000's six axes and native three-force closure are unchanged.

Research evidence `AUTHOR_EXACT_NOT_REVIEWED`. Historical R2 identity `EM-DIRECT-44C346` and Activity `RA-A16A5E663104EBDBA287C665` are provenance, not a new authenticated session or shared CLAIM.
