# EC49FQM — Full high-price prior continuum and two exact new price slices

**Date:** 2026-11-16. **Scientific status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Predecessor:** EC49FQL [PR #2548](https://github.com/awdawmip/enterprise-math/pull/2548), with original input and conclusion retained. This document is independent portable research, not a canonical Task/CLAIM/Result or review.

## Model, cost surfaces and complete query domain

The native BRC class represented by configuration 16943 contains 310 original configurations and 141 distinguishable named-root profiles; all 228 physical scalar queries are available (144 terminal observations indexed 0–143, 84 named-root observations indexed 144–227; 209 distinct response partitions). The exact identification goal is to determine each complete named-root profile. Each query used must split the candidate set; all finite adaptive strategies are allowed.

The original configuration multiplicity of profile i is m_i, with sum m_i=310. Let

`p_lambda(i)=(1-lambda)/141 + lambda*m_i/310`, 0<=lambda<=1,

and prices r,t>0, x=r/t. Set v(lambda,x)=V(lambda;r,t)/t. Define beta=620/3299 and gamma(x)=310(3-x)/(7557-169x), 1<=x<=3. Five exact feasible native-tree cost surfaces are

```text
A      = (1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310
B      = (1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310
C      = (1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310
Bhigh  = (1-lambda)*(4*x+296)/141 + lambda*(4*x+707)/310
Chigh  = (1-lambda)*(4*x+298)/141 + lambda*(4*x+688)/310
```

The native q-first witnesses for A,B,C,Bhigh,Chigh are respectively q32/q34, q140/q142, q16/q23, q140/q142, q16/q23. The complete 141-profile/310-configuration replay gives their summed observation count vectors (U_root,U_terminal; M_root,M_terminal), respectively (6,290;6,751), (5,293;5,704), (5,295;5,685), (4,296;4,707), (4,298;4,688).

## Theorem 1 — full high-price ray, every real prior

For **all** real lambda in [0,1] and x>=3, the unrestricted global optimum is

```text
v(lambda,x) = min(Bhigh,Chigh)
            = Bhigh  for 0<=lambda<=620/3299
              Chigh  for 620/3299<=lambda<=1.
```

All optimal *physical first-query indices* (not merely query types) are:

| Prior | x>=3 |
|---|---|
| lambda=0 | {32,34,140,142} |
| 0<lambda<beta | {140,142} |
| lambda=beta | {16,23,140,142} |
| beta<lambda<1 | {16,23} |
| lambda=1 | {16,23,59,88} |

**Proof.** A complete exact integer Bellman recurrence over the 141-state finite domain, 209 query partitions and all 228 physical first actions gives at x=3:

```text
lambda=0:       value 308/141,    first={32,34,140,142}
lambda=620/3299:value 7290/3299, first={16,23,140,142}
lambda=1:       value 70/31,      first={16,23,59,88}.
```

At fixed price x, the expected cost of every fixed correct native tree is affine in lambda. The same Bhigh tree attains the exact Bellman minima at lambda=0 and lambda=beta; the same Chigh tree attains both lambda=beta and lambda=1. The gap between any competitor and the respective witness is affine and nonnegative at the two endpoints, hence nonnegative throughout each full real-prior interval. This proves both cost pieces at x=3. At an interior lambda, any additional optimal-first tree would also be optimal at both endpoints, restricting its first index to the intersection of their first sets; the listed witness trees attain each surviving index.

The terminal joint response has 139 fibers, exactly two nonsingleton disjoint doublets; the four profiles have original multiplicity one. A correct tree must use at least one named-root query along **each** of those four paths, yielding U_root>=4 and M_root>=4. Every stated high-price witness, including q32/q34 at lambda=0 and q59/q88 at lambda=1, attains the corresponding minimum of four root visits. When x grows from 3, every feasible tree's additional cost is at least (x-3)*4*((1-lambda)/141+lambda/310), attained by these trees. This proves optimality and all first sets on x>=3. QED.

## Theorem 2 — unbounded high-prior strip

For **all** real beta<=lambda<=1 and x>=1,

```text
v(lambda,x) = C(lambda,x)      for 1<=x<=3
              Chigh(lambda,x)  for x>=3.
```

On 1<=x<3 the full physical first sets are:

| Parameters | First observations |
|---|---|
| lambda=beta | {16,23,140,142} |
| beta<lambda<1 | {16,23} |
| lambda=1, x=1 | {16,23,124,131} |
| lambda=1, 1<x<3 | {16,23} |

At x>=3 use Theorem 1. **Proof.** At four corners (lambda,x)=(beta,1),(beta,3),(1,1),(1,3), the complete Bellman minima are achieved by the *same fixed* q16 native witness with count vector (5,295;5,685). The cost gap of every competitor relative to q16 is bilinear in (lambda,x), and is the convex interpolation of four nonnegative corner values. It remains nonnegative everywhere in [beta,1]x[1,3]. Q23 has the identical vector. Complete first sets follow by intersection at relative interiors and exact boundary Bellman sets. At x=3 the alternate Chigh witness has identical cost and minimum root count, proving the infinite extension by Theorem 1. QED.

This extends the earlier [155/1847,beta] common slab from EC49FQK on its upper-prior side all the way to lambda=1 for x>=1.

## Theorem 3 — full-prior optimum at x=3/2 and x=5/2

For **each** x in {3/2,5/2}, for **all real** lambda in [0,1],

```text
v(lambda,x) = min(A(lambda,x),B(lambda,x),C(lambda,x)).
```

All physically indexed optimal first observations are exactly:

| Prior | Optimal surface | Complete first indices |
|---|---|---|
| 0<=lambda<gamma(x) | A | {32,34} |
| lambda=gamma(x) | A=B | {32,34,140,142} |
| gamma(x)<lambda<beta | B | {140,142} |
| lambda=beta | B=C | {16,23,140,142} |
| beta<lambda<=1 | C | {16,23} |

The new exact first transitions are gamma(3/2)=310/4869 and gamma(5/2)=310/14269. Both transitions are sharp because

```text
A-B = (1-lambda)*(x-3)/141 + lambda*(x+47)/310,
C-B = 2*(1-lambda)/141 - 19*lambda/310.
```

**Proof.** For each of the two prices, independently recompute four complete integer-Bellman values at lambda=0,gamma(x),beta,1. The independently computed first indices equal the endpoint rows. On each interval bounded by these anchors, a fixed exact native q-first tree achieves the endpoint optimum; the expected cost gap for any competing tree is affine in lambda, nonnegative at both endpoints, hence nonnegative throughout. Optimal first indices in open intervals must be in both endpoint sets, and every surviving index has a complete replayed optimal tree. Exact tie trees establish the listed boundary sets. QED.

### New two-parameter certified rectangles

The same full native witnesses and the bilinear four-corner inequality also certify:

- A is globally optimal on 0<=lambda<=310/14269 and 3/2<=x<=5/2.
- B is globally optimal on 310/4869<=lambda<=620/3299 and 3/2<=x<=5/2.
- C is globally optimal on beta<=lambda<=1 and 1<=x<=3 (Theorem 2).

The proofs use only the exact four corners of each rectangle and bilinear interpolation of every competitor cost gap. The B-rectangle extends the older global B slab down in lambda from 155/1847 to 310/4869 over this price window.

## Exact finite verification, sources, and remaining frontier

Frozen input SHA256:
- original master `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- native root-cost table `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Thirteen newly regenerated unrestricted rational Bellman anchor certificates: eight at x=3/2 and x=5/2, plus five x=1/3 corner checks. An independent dynamic program rebuilds all 209 response partitions and **all 228 physical first actions**, replays the 141-state/310-configuration q-first trees, checks exactly two terminal-invisible doublets, and matches each optimum and complete first set. All rational calculations are exact. Evidence archive contains full frozen inputs, machine certificates, two solver implementations, exact tree replay, logs and SHA256 per-file manifest. No Lean check or independent mathematical review is claimed.

**Open:** In the remaining low-prior corridor 0<lambda<310/4869, 1<x<3, determine whether the candidate equality curve lambda=gamma(x) is globally sharp for every real x or whether another native strategy cuts below the candidate A/B lower envelope. The two new complete transverse slices certify exactness at x=3/2 and x=5/2; earlier x=1,2 results and this note provide additional anchors. Avoid extrapolating finite rational slices to the entire curved boundary without a proof.
