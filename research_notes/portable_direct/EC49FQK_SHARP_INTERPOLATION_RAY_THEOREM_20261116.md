# EC49FQK — sharp two-parameter BRC observation slab with an unbounded price ray

Date: 2026-11-16. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scientific predecessors: EC49FQI [PR #2539](https://github.com/awdawmip/enterprise-math/pull/2539) and EC49FQJ [PR #2542](https://github.com/awdawmip/enterprise-math/pull/2542).

## Statement and exact domain

The native BRC class identified by configuration 16943 contains 310 original configurations and 141 distinct **complete named-root cost profiles**. Its fixed observer palette consists of 144 complete-terminal scalar observations (physical indices 0–143) and 84 named-root scalar observations (indices 144–227). A correct adaptive strategy identifies the entire named-root profile. Terminal-only indistinguishability is retained as a genuine residual.

Let `m_i` be each profile's configuration multiplicity, `sum_i m_i=310`. Define the prior `p_lambda(i)=(1-lambda)/141+lambda*m_i/310`, where `0<=lambda<=1`. The per-observation prices are `r>0` for named-root observations and `t>0` for terminal observations; put `x=r/t`. The global optimum `V(lambda;r,t)` ranges over **all finite correct adaptive decision trees**, with no depth or first-observation restrictions.

**Theorem.** Set `alpha=155/1847` and `beta=620/3299`. For **every real** `alpha<=lambda<=beta` and `x>=1`,

```
V(lambda;r,t)/t =
  (1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310,  1<=x<=3;
  (1-lambda)*(4*x+296)/141 + lambda*(4*x+707)/310,  x>=3.
```

The two formulas meet at `x=3`. The **complete set of physically indexed optimal first observations** is

- `{32,34,140,142}` at the one corner `(lambda,x)=(alpha,1)`;
- `{16,23,140,142}` along the entire right boundary ray `lambda=beta, x>=1`;
- `{140,142}` at every other point of the above slab.

Both prior endpoints are **sharp for the common displayed formula on the full x>=1 ray**: for every `lambda<alpha`, at `x=1` a `q32`-first correct strategy costs strictly less; for every `lambda>beta`, at each `x>=1` a `q16`-first correct strategy costs strictly less. This is a sharp domain statement, not a full classification of neighboring phases outside this slab.

## Exact unrestricted Bellman proof

Frozen native input hashes: original master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; named-root cost CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. These source files and the complete reproducibility code are retained in the accompanying portable evidence archive; exact source reconstruction code was already published in EC49FQJ (#2542).

For each `lambda=a/b` use integer weights `W_i=310*(b-a)+141*a*m_i` with total `141*310*b`. For any candidate-set bitmask `S` the unrestricted exact Bellman recurrence is

```
B({i})=0;
B(S)=min_{q strictly splitting S} [ c(q)*W(S) + sum_z B(S intersect fiber(q,z)) ].
```

Every useful query strictly reduces the surviving candidate set. Thus this finite recurrence optimizes over arbitrary correct adaptive trees. All 228 physical observations are checked for forced-first cost, even when several share one of the 209 unique response partitions.

The four **load-bearing newly computed exact corner values** (set `t=1`) are:

| lambda | x | exact V/t | complete optimal first physical indices |
|---|---:|---:|---|
| 155/1847 | 1 | 7861/3694 | 32,34,140,142 |
| 155/1847 | 3 | 8111/3694 | 140,142 |
| 620/3299 | 1 | 7080/3299 | 16,23,140,142 |
| 620/3299 | 3 | 7290/3299 | 16,23,140,142 |

The original FQJ independently replayed full-population optimal trees starting with `q140` and `q142`. Their exact `(U_root,U_terminal;M_root,M_terminal)` count vectors are `(5,293;5,704)` in the first price regime and `(4,296;4,707)` in the second. These same trees are parameter-independent valid strategies. Each tree's normalized expectation is a **bilinear function of (lambda,x)**. Subtract the first-regime reference cost from any correct tree: the difference is bilinear, nonnegative at the four rectangle corners by the exact recurrence, and is a convex combination of those four values inside `[alpha,beta]×[1,3]`. Hence it is nonnegative throughout that continuum, while the reference trees attain zero. This proves the first piece for all real pairs.

## Infinite high-price extension

The 144 terminal responses jointly have 139 response fibers among the 141 complete profiles. Exactly two fibers are nonsingleton:

```
{(configuration 17928,m=1), (38165,m=1)};
{(configuration 24541,m=1), (38166,m=1)}.
```

For each of those four profiles, every correct distinguishing tree must use at least one named-root observation on its path, because no terminal query can distinguish either pair. Therefore every correct tree has `U_root>=4` and `M_root>=4`, i.e. under the interpolated prior the expected number of root observations is at least `4*((1-lambda)/141+lambda/310)`.

At `x=3`, the second regime's witness reaches global Bellman optimum with exactly four root observations in **both** population count conventions. Increasing `x` by any nonnegative real `h` increases the cost of **every** tree by at least `h*t*4*((1-lambda)/141+lambda/310)`; the witness attains equality. Thus the second formula holds globally for **all real x>=3**, with no finite upper cutoff.

## All optimal first queries and sharpness

The bilinear difference argument also applies to forced-first policies. An extra first query optimal at an interior parameter would have to be optimal at every rectangle corner with positive interpolation coefficient. The corner-set intersections leave `q140,q142` in the slab interior. At `lambda=alpha`, `q32,q34` appear only at `x=1`, because they are absent at the `x=3` endpoint. At `lambda=beta`, complete `q16`- and `q23`-first tree witnesses have the vectors `(5,295;5,685)` on `1<=x<=3` and `(4,298;4,688)` on `x>=3`. They achieve the reference optimum **exactly at lambda=beta** and the high-price witnesses meet the mandatory minimum four-root count; hence these extra first queries persist along the entire right boundary ray. Any optimum at `x>3` must already be optimal at `x=3` and use the minimum root count, so no other first queries appear there.

The `q32`-first tree at `x=1` has counts `(6,290;6,751)`, beating the first-regime reference whenever

```
Delta_lower = -2*(1-lambda)/141 + 48*lambda/310 < 0,
```

which is exactly `lambda<155/1847`. The `q16`-first alternatives have counts `(5,295;5,685)` on `1<=x<=3` and `(4,298;4,688)` on `x>=3`, so in either regime their excess over the reference is

```
Delta_upper = 2*(1-lambda)/141 - 19*lambda/310,
```

strictly negative when `lambda>620/3299`. These exact valid trees prove the stated sharp endpoint claims without extrapolating from finite price samples.

## Validation, provenance, next problem

A primary integer Bellman program and a distinct integer recurrence independently re-evaluated ten newly saved rational probes, exhaustively checked their 228 forced-first physical costs, and replayed the complete witness trees against all 141 profiles/310 configuration multiplicities. The four load-bearing corners, further x=2,4,5 controls, and a lambda=1/5 outside-region falsifier all passed. The complete archive includes the frozen original input, old and new machine certificates, original code, independent verification code, full native replay data, real logs and a SHA256 file manifest. Code and hash index are separately published in this PR. Local evidence archive SHA256: `b7208cf0af5349e572fe029d18ab68ba19bbe173e2119b8a1d5f697da5c54f83`.

This is an exact mathematical theorem **within the declared finite native BRC observation model**. It has author and independent-implementation checking; project-independent theorem review remains `NOT_REVIEWED`. No official Task CLAIM, Result, Review, P000 change or physical-world calibration is claimed.

**Next:** determine the adjacent phase curves for `lambda<alpha` at `x>1` and `lambda>beta`, retaining complete named-root residuals and physical-index first-action distinctions. Current exact Task lookup of `RS-EC49AS` returned `CANONICAL_REJECTED: unknown current immutable task publication`; independent portable research is the scope of this scientific file.
