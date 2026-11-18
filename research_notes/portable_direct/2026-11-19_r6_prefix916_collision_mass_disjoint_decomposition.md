# PREFIX-916 — Exact disjoint decomposition of named XOR collision-pair mass

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Status: AUTHOR_PROVED / EXACT_INTEGER_COMPUTED / SMALL_STATE_EXHAUSTIVE_AND_INDEPENDENT_PARAMETER_TRAVERSAL / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scientific dependencies: PREFIX-913 (signed dyadic two-named-flip collision identities); PREFIX-914 (existing strict-19-bit modulus coverage); PREFIX-915 (exact number of witnesses per fixed identity).
This is provenance-preserving BRC auxiliary two-port research, not an admitted X6-native time/triadic event model.

## 1. The counting problem

Let `N=2^p`, and fix two positive observer moduli `a,b`. A named flip trajectory is

```text
F_x^i = (x, x XOR 2^i),    0 <= x < N, 0 <= i < p,
Phi_(a,b)(u,v) = (u mod a,v mod b).
```

A **positive ordered-gap, high-source-first collision pair** is an unordered pair
`{F_x^i,F_y^j}` with `x<y` and `i>j`, whose two observed residues agree, and whose *terminal state gap*
`(y XOR 2^j)-(x XOR 2^i)` is **strictly positive**. Its trajectories and both source labels are retained. These conditions define a precise subset of all two-port collisions.

The earlier PREFIX-915 formula counted the number `M_p(A,i,j,eps,eta)` at a *single* signed-dyadic identity

```text
A = k*a,  B = ell*b,
A - B = eps*2^i - eta*2^j,
1 <= k,ell, 0 <= j < i < p, eps,eta in {-1,+1},
0 < A < N.
```

All sign choices are allowed. PREFIX-915 gives an exact count `M` even when the signed equation has no witnesses owing to terminal headroom.

## 2. Theorem 916-A — parameter fibers are pairwise disjoint

**Statement.** For fixed `(p,a,b)`, let `S_{k,ell,i,j,eps,eta}` be the set of labeled trajectory pairs `{F_x^i,F_(x+k*a)^j}` satisfying the stated signs and p-bit start bounds. As `(k,ell,i,j,eps,eta)` ranges over all positive integers `k,ell`, `0<=j<i<p` and signs satisfying the signed equation, the nonempty sets `S` are pairwise disjoint. Their union equals precisely the positive ordered-gap, high-source-first collision pairs. Therefore the exact total number is

```text
C_p(a,b)
 = sum_{k>=1, k*a<N} sum_{0<=j<i<p}
   sum_{eps,eta in {-1,+1}}
      [ B=k*a-eps*2^i+eta*2^j is >0 and divisible by b ]
      * M_p(k*a,i,j,eps,eta).                                    (1)
```

**Proof (uniqueness).** Every member of this class has exactly one ordering of its two trajectories by start: `x<y`, and exactly one ordering by named index: `i>j`. Therefore `A=y-x` and the source indices `(i,j)` are fixed by the labeled pair. Because the first observed residues coincide and `A>0`, `A=k*a` for a **unique** positive integer `k`. The XOR signs `eps` and `eta` are uniquely determined by the corresponding bit values of `x` and `y`. The terminal-state gap is then uniquely `B=A-eps*2^i+eta*2^j`; by hypothesis it is positive and divisible by `b`, so `ell=B/b` is a unique positive integer. Hence the entire parameter tuple is uniquely recoverable from the labeled trajectory pair; different tuples have no common members.

**Proof (completeness).** Conversely every pair in the defined class yields the unique parameters just described, so it is counted by precisely one `M_p` term in (1). Every pair in a term satisfies both observer modular equalities by PREFIX-915. Thus (1) is a disjoint union identity, not an inclusion-exclusion approximation. QED.

**Scope detail.** The high-source-first orientation is the declared class; low-source-first or nonpositive terminal-gap collisions may be analyzed separately. This choice does not collapse named sources or turn an auxiliary observer into native X6 event admission.

## 3. The exact multiplicity kernel

Use PREFIX-915's `M` with `A=k*a` and `L=N-A`:

```text
H=2^i, T=2^(i+1), q=L//T, t=L%T,
bi=(eps==-1), bj=(eta==-1),
u=clamp(t-bi*H,0,H),
G_j(z)=(z//2^(j+1))*2^j+max(0,z%2^(j+1)-2^j),
d=G_j(A+u)-G_j(A),
M=q*2^(i-1)+(d if bj else u-d).
```

Everything is exact integer arithmetic. As seen in PREFIX-915, the case `eps=+1` and `A<=2^i` has `M=2^(p-2)` regardless of `j` and `eta`. For the current single-observer count, the partition in theorem 916-A ensures that a pair is never counted twice across different signed equations.

## 4. Complete 32-bit arithmetic result for one strict-19-bit observer

Choose the already-established PREFIX-914 new covered modulus pair

```text
p=32, a=321651, b=440665, N=4294967296.
```

The complete integer algorithm iterates every positive `k` with `k*a<N`, every `0<=j<i<32` and four sign choices. It solves `ell*b=k*a-eps*2^i+eta*2^j`, retaining only positive divisible results and computing each exact `M`. Results:

| Exact classification | Count |
|---|---:|
| Signed parameter identities, including zero-witness solutions | 264 |
| Parameter identities with at least one labeled trajectory-pair witness | 263 |
| Largest single-identity witness count | 1,073,741,824 |
| **Distinct labeled trajectory-pair collisions in this declared class** | **196,960,748,158** |
| Independent terminal-gap-first calculation | **196,960,748,158** |

The independent traversal instead enumerates `ell*b<N` first and solves `k*a=ell*b+eps*2^i-eta*2^j`; it yields the same total and 263 positive identities. The absolute number of distinct *modulus pairs* covered by PREFIX-914 remains **7,795,676,346**, since this computation refines one already covered modulus pair.

An important phenomenon: this observer sits above the earlier total-capacity pigeonhole threshold `a*b>33*2^32`, so a global uniform-capacity lower bound supplies zero here, yet the named two-flip collision class has exact mass exceeding 196 billion. The distinction is the observer's nonuniform fibers and preservation of source labels.

## 5. Executable verification and reproducibility

- Source code: `research_notes/portable_direct/PREFIX916_R6_DISTINCT_LABEL_MASS.cpp`.
- Certificate: `research_notes/portable_direct/PREFIX916_R6_DISTINCT_LABEL_MASS_RESULTS.json`.
- Build and run: `g++ -std=gnu++17 -O3 -Wall -Wextra PREFIX916_R6_DISTINCT_LABEL_MASS.cpp -o p916 && ./p916`.
- The program uses exact 64-bit integers for intermediate gaps and unsigned 128-bit accumulation for total mass; no floats, random sampling, approximate residuals or external APIs are used.
- Small-state brute force directly iterates every `x<y`, every `i>j`, and both residue conditions, for **276** combinations of `2<=p<=7` and positive odd `a,b<=15` below `2^p`: **zero discrepancies** against the summed symbolic formula.
- An independent *terminal-gap-first* full p=32 parameter enumeration matches **196,960,748,158** and all 263 positive families. This is a second enumeration order, not a separate independent mathematical review.
- Verified locally executed source Git blob SHA-1: `0d956f39c6755b7e4888205a851112c558ea2e12`. The project source is stored on immutable GitHub main and can be recompiled directly.

The p32 total is exact relative to theorem 916-A and its finite parameter domain; 196 billion trajectory pairs were not individually materialized. The theorem supplies a proof that the integer sum counts them all.

## 6. Durable scientific frontier and authority

Next mathematical directions: (i) derive a useful distribution/invariant of exact observer collision multiplicity across modulus pairs; (ii) quantify the complementary classes with other source-index orders and signed endpoint gaps; (iii) use exact tail multiplicity to admit additional large multipliers while preserving all source labels and check full set-union de-duplication separately.

The user-selected P000, Heartbeat native X6 geometry/time, and immutable scientific input remain unchanged. No mathematical acceptance, Working Truth or formal Result is claimed.

Control observation: native X6 owner read request `r6-20261119-0431-owner-read-prefix915` succeeded as of 2026-11-18T20:35:54.748804+00:00 with `actor=null`, `claim_id=null`. An own native research session registration request `r6-20261119-0435-prefix915-own-session` ended `FAILED / SOURCE_TREE_BLOB_SIZE_INVALID`. Thus no authenticated Researcher-ID, research Activity, or live shared CLAIM was obtained by this run; original failure is retained for regular repair, and the mathematics is preserved through independent GitHub research notes.
