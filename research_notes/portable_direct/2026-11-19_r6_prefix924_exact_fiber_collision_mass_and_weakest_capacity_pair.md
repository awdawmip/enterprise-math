# PREFIX-924 — Exact marginal collision-mass lower bounds and the unique weakest strict-19-bit capacity pair

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6. Scientific status: **AUTHOR_PROVED / INTEGER_FINITE_ENUMERATION / SMALL_MODEL_DIRECT_CHECK / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED**.

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Direct preserved frontier: `research_notes/portable_direct/2026-11-19_r6_prefix923_sharp_bucket_capacity_and_highband_census.md` at `enterprise-math@9823959ad02bf3698c9d8f80abb519bd42e6fddf`.
Scope: the **auxiliary, named XOR zero-or-one-flip two-port observer**; this is not a claim of equivalence with native six-axis X6 dynamics.

## 1. Typed population and the exact mass carrier

Fix an integer `p>=1`, `N=2^p`, `t=p+1`. The named population contains the zero trace `Z_x=(x,x)` and `p` source-labeled flip traces `F_x^i=(x,x xor 2^i)` for every `0<=x<N` and `0<=i<p`. Distinct source labels always define distinct traces. The observer sends the trace endpoints to `(start mod a,end mod b)`, with positive integers `a,b`.

Let `c_(u,v)` be the number of **named traces** observed at residue pair `(u,v)` and let

```
C(p,a,b) = sum_(0<=u<a, 0<=v<b) binom(c_(u,v),2).
```

This is the actual unordered collision-pair mass. Its positive integer units count distinct *pairs of named traces*, not distinct modulus pairs or collided observer cells.

For an integer population `d>=0` distributed into `m>=1` bins define

```
q=floor(d/m), r=d mod m,
F_m(d)=(m-r)*binom(q,2)+r*binom(q+1,2)
      =m*q*(q-1)/2+r*q.
```

The exact integer function `F_m(d)` is the smallest possible number of unordered equal-bin pairs among all allocations of `d` distinguishable objects to `m` bins. Indeed, if bin occupancies differ by at least two, moving one object from the fuller to the emptier bin strictly decreases the sum of `binom(occupancy,2)`. Repeating yields the unique balanced occupancy multiset, proving the formula.

## 2. Exact dual marginal lower-bound theorem

Write

```
q_a=floor(N/a), r_a=N mod a,
q_b=floor(N/b), r_b=N mod b.
L(p,a,b) = r_a F_b(t*(q_a+1))+(a-r_a) F_b(t*q_a).
R(p,a,b) = r_b F_a(t*(q_b+1))+(b-r_b) F_a(t*q_b).
B(p,a,b) = max(L(p,a,b),R(p,a,b)).
```

**Theorem.** For all integers `p>=1` and positive `a,b`,

```
C(p,a,b) >= B(p,a,b).
```

Both `L` and `R` are sharp lower bounds using just their respective marginal fiber sizes, without claiming they are simultaneously attained by this XOR observer.

**Proof.** Each first-port residue class contains `q_a+1` starting states for exactly `r_a` residues, and `q_a` starting states for the other `a-r_a` residues. Every start supports exactly `t` distinct named traces. Within one such class, distribute these `t*q` traces over the `b` second-port residue values; their colliding pairs number at least `F_b(t*q)`. Summing disjoint first-port classes yields `C>=L`.

For the other direction, **each endpoint `y` has exactly `t` incoming named traces**: `Z_y` and `F_(y xor 2^i)^i` for each of the `p` bits. Partition endpoints by `y mod b`; their degree distribution is `t*(q_b+1)` on `r_b` classes and `t*q_b` on the rest. Applying the same balanced-bin lemma to the `a` first-port residues yields `C>=R`. Both bounds concern the same collision-pair set, so their maximum is valid.

**Corollary.** `B(p,a,b)>0` if and only if one of the two PREFIX-923 bucket-capacity inequalities fails:

```
b<t*ceil(N/a) OR a<t*ceil(N/b).
```

Thus the new carrier enriches the already certified Boolean collision-support set with an exact compulsory positive pair multiplicity. It does not replace the provenance-sensitive named-pair counter `C`.

## 3. Exact weakest-capacity classification in the strict 19-bit odd domain

Put `p=32, N=4294967296, t=33`, and

```
Q={262145,262147,...,524287}, |Q|=131072.
```

**Finite theorem.** In the full ordered domain `Q^2`, the minimum *positive* compulsory marginal collision mass is

```
min{ B(32,a,b) : (a,b) in Q^2, B(32,a,b)>0 } = 3.
```

Its **only** ordered minimizers are

```
(a,b)=(464773,304985) and (304985,464773).
```

This is a statement about the rigorous lower bound `B`, not about the minimum actual XOR collision mass `C`.

**Complete reduction.** Every `a in Q` is odd and `N` is a power of two, so `1<=r_a=N mod a<a`. Denote `d_0=33*floor(N/a)`, `d_1=d_0+33`. If `0<L(32,a,b)<=3` and `b<d_0`, then the `r_a` high-degree start fibers each overflow `b` by at least 34, forcing `L>3`; contradiction. Therefore `d_0<=b<d_1`. Because `d_0>=270336`, balancing these near-capacity degrees gives precisely `L=r_a*(d_1-b)`. Consequently `r_a<=3`, and `b=d_1-delta` for an integer `1<=delta<=floor(3/r_a)`. By swapping ports, the identical condition characterizes all possible cases `0<R<=3`.

An exhaustive 131072-element integer remainder scan gives exactly two values of `a in Q` with `1<=N mod a<=3`:

```
a=327685: floor(N/a)=13107, N mod a=1;
a=464773: floor(N/a)= 9241, N mod a=3.
```

The remainder claim may also be verified from divisors of `N-1`, `N-2`, `N-3`; the accompanying pure-Python reproducer enumerates every allowed `a` directly. The only possible oriented weak-capacity cases, along with their transposes, are:

| a | b | L | R | B |
|---:|---:|---:|---:|---:|
| 327685 | 432563 | 1 | 246345 | 246345 |
| 327685 | 432561 | 3 | 345635 | 345635 |
| 464773 | 304985 | 3 | 0 | **3** |

The symmetric pairs have `L,R` interchanged. These six ordered candidates exhaust any positive `B<=3` by the reduction. Exactly two realize `B=3` and none realize `B=1,2`. This proves the finite classification without scanning `17,179,869,184` observer pairs or silently omitting candidate families.

At the minimizer `(a,b)=(464773,304985)`: `N=9241*a+3`, `33*(9241+1)=304986=b+1`, hence the three extra starts in the largest first-port bucket force at least three unordered colliding trace pairs. The end-port capacity is not overfull (`R=0`). Also `a*b=141748793405>33*N=141733920768`; the global-cardinality test does not force this collision.

A **direct named XOR witness** independently demonstrates noninjectivity at this modulus pair:

```
F_0^7=(0,128), Z_3779069263=(3779069263,3779069263).
start gap 3779069263=8131*464773
end gap   3779069135=12391*304985.
```

Both states lie in `[0,2^32)`, and the two observed port residues agree. This particular witness certifies at least one actual collision; the theorem's `B=3` certifies at least three actual unordered named-trace pairs (not necessarily these three witness pairs explicitly enumerated).

## 4. Computation, provenance, and next question

Reproducer: `research_notes/portable_direct/PREFIX924_R6_FIBER_MASS_VERIFY.py` (Python 3 standard library only). It performs: exact `N mod a` over every `a in Q`; mathematically exhaustive generation of the at-most-three-mass candidate set; exact evaluation of all six oriented candidate pairs; an independent direct XOR witness divisibility check; and direct small-observer enumeration of `485` configurations for `p=1,...,5` checking `C>=B`.

The result uses **integer division and modular arithmetic only**. The proof of the universal inequality is human-complete; the uniqueness over `Q^2` uses the documented finite remainder scan. The program's explicit assertions are the finite certificate, not a formal proof assistant verdict.

Next local research question: quantify `C/B` in or near the weakest-capacity pair using the existing PREFIX-918/919 exact named-collision kernels, preserving individual start/end/source types, then decide whether compulsory marginal mass predicts actual collision concentration. The larger auxiliary injectivity question and native X6 dynamical correspondence stay as separately typed problems; the project mother question remains `B_fix,odd(32) in {19,20}`.
