# R749SPV — An exact unimodular 22-counter provenance codec for both minimal Walsh alphabets

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Research mode:** independent portable TASK_RESEARCH; no shared X6 execution claim. **Frozen scientific source:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Dependencies:** R749SPR (complete optimal-center polytope, PR #2457), R749SPT (IDP, PR #2464), R749SPU (two 26-letter universal alphabets and provenance exponent 22, PR #2467). All imported mathematical results are author-reported and await independent review.

## 1. Model and exact question

Use the frozen auxiliary signed 16-atom Walsh model
`p(t,s,h,u,v,w,z)[k]=(1+t chi_3(k)+s chi_12(k)+h chi_15(k)+u chi_1(k)+v chi_2(k)+w chi_4(k)+z chi_8(k))/16`,
where `chi_m(k)=(-1)^popcount(k&m)`, `0<=k<16`. At `(t,s)=(1/10,1/2)`, the complete calibrated minimax-center polytope `K` has the eight integral facets recorded in R749SPR, with `rho=rho_cal=9/20`. Each source letter `a=(H,U,V) in K intersect Z^3` denotes the complete signed law `q_a=p(1/10,1/2,H/10,U/10,V/10,0,0)`.

R749SPU identified two minimum universal source alphabets `A_zero=F union {(0,0,0)}` and `A_shift=F union {(-1,0,0)}`, both of size 26; `F` is the 25-letter set forced by unique two-letter sums. Here `n` is the *number of selected labeled source letters*, with unordered multiplicities `c_a>=0` and `sum c_a=n`. The averaging observer produces `X=sum c_a a in Z^3`, and the averaged probability center is `q_(X/n)`. The problem is to recover the exact multiset counts from the observer `(n,X)` plus a small residual.

## 2. Main theorem — 22 explicit counts and a division-free inverse

Both minimal alphabets contain the same four **forced** anchor letters, in the following fixed order:
```text
a0=(-2,-1, 1)     a1=(-2, 0, 0)
a2=(-1,-2, 1)     a3=(-1,-1, 1)
```
Their augmented count/moment column matrix is
```text
        a0 a1 a2 a3
count    1  1  1  1
H       -2 -2 -1 -1
U       -1  0 -2 -1
V        1  0  1  1
```
and has determinant **-1**. Consequently these columns constitute an integral unimodular basis of `Z^4`.

**Theorem.** For either minimum alphabet `A`, any integer `n>=0` and any observed `X=(H_total,U_total,V_total) in Z^3`, the list of 22 nonanchor source multiplicities uniquely and exactly determines all 26 source multiplicities, if a valid nonnegative source multiset with that residual exists. The reconstruction uses integer additions/subtractions only, and is linear time in the fixed alphabet size.

**Explicit decoder.** Let `r_b=c_b` for the 22 letters `b in A\{a0,a1,a2,a3}`. Subtract their contribution:
```text
N = n - sum_b r_b
(H,U,V) = X - sum_b r_b * b
c[a0] = -H + V - 2N
c[a1] =  N - V
c[a2] = -U - V
c[a3] = 2N + H + U + V
```
Accept exactly when these four integers and the 22 supplied residual counts are nonnegative and the reconstructed total and moment equal `(n,X)`; otherwise report that the proposed residual does not encode a valid source multiset. In particular, no divisibility tests or rational rounding are needed.

**Proof.** After subtracting the 22 stored contributions, the remaining four counts `x,y,z,w` satisfy `N=x+y+z+w`, `H=-2x-2y-z-w`, `U=-x-2z-w`, `V=x+z+w`. Therefore `y=N-V`, `z=-U-V`, `x=-H+V-2N`, and `w=2N+H+U+V`. These expressions solve all four original equations identically and are unique; their integral form also proves the determinant-one lattice property. Every actual source multiset yields nonnegative reconstructed counts, and every accepted residual yields exactly that multiset. This statement holds for all n as a pure integer fiber theorem; full coverage of every point of `nK` for n>=2 uses the imported R749SPT/R749SPU theorems separately.

A concrete collision illustrates the information preserved: `(-2,-1,1)+(-2,1,-1)=(-2,0,0)+(-2,0,0)=(-4,0,0)`. These two positive source multisets have the same averaged full signed Walsh law. The 22-count residual distinguishes them without altering the signed readout.

## 3. Storage optimality relative to the declared readout

Each residual count is in `[0,n]`, so a direct fixed-width residual uses at most `22*ceil(log2(n+1))` bits, given that `n,X` and the chosen alphabet are already available to the decoder. The inverse is linear in the 26-source alphabet size (and O(log n) integer bit length per count).

R749SPU established the sharp worst-fiber growth `max_X M_A(n,X)=Theta(n^22)` for both alphabets, where the fiber counts unordered nonnegative source-multiplicity vectors compatible with `(n,X)`. Thus any exact worst-case residual distinguishing source multisets **within a known readout fiber** requires `22 log2(n)+O(1)` bits. The explicit 22-counter code attains the optimal leading coefficient. The bit bound describes provenance recovery; it does not assert a native X6 operation or a measured optimized hardware codec. The source multiset must be retained when the future operation depends on provenance; projection to `X` alone is not source-faithful.

One may optionally enumerate valid 22-count residual tuples for the known readout and encode their rank in `ceil(log2 M_A(n,X))` bits, obtaining a theoretical fiber-optimal enumerative code; its enumeration cost is not bounded here.

## 4. Exact finite experiment — the two alphabets exchange the maximum-fiber ordering

The companion pure-integer Python program constructs K from the exact eight R749SPR halfspaces, recomputes P and the forced 25 types from unique second-grid pair sums, and verifies both 26-letter alphabets contain the unimodular anchors. It enumerates **every unordered source multiset** at n=2,3,4,5 for both alphabets. For each, it computes `(n,X)`, retains the 22 nonanchor counts, decodes them and checks all 26 recovered counts for exact equality; it independently compares the number of attained readouts against R749SPS's Ehrhart formula.

| n | Source multisets per alphabet | Distinct readouts | max fiber, A_zero | max fiber, A_shift | unique readouts, A_zero / A_shift |
|---|---:|---:|---:|---:|---:|
| 2 | 351 | 179 | 7 | 7 | 87 / 83 |
| 3 | 3,276 | 531 | 29 | 34 | 88 / 86 |
| 4 | 23,751 | 1,181 | 154 | 144 | 110 / 108 |
| 5 | 142,506 | 2,221 | 595 | 586 | 136 / 134 |

The maximum-fiber ordering **reverses between n=3 and n=4**: `A_shift` has the larger maximum at n=3, while `A_zero` has the larger one at n=4 and n=5. These are complete finite facts for the stated levels, not an asymptotic ordering claim. Total: **339,768 source multisets** exhaustively decoded across the two alphabets for n=2..5. The program output is `PASS` with exact Python integers and no floating-point tolerance.

## 5. Scope, evidence, next question

This is an explicit effective strengthening of R749SPU's existential provenance index: a single common unimodular four-letter set gives a simple, fully constructive inverse for both minimum alphabets. The exact codec itself requires only the verified membership of the four anchors; claims about full nK coverage and asymptotic lower bounds inherit the cited author-reported theorems. No original Source Task/CLAIM/Result/Review status is changed by the auxiliary model derivation. The signed 16-atom law, positive source multiplicities, and source identity remain separate typed carriers. No native Heartbeat World X6/V29/V39 operator transfer is asserted.

**Reproduction:** Run `python3 R749SPV_WALSH_UNIMODULAR_PROVENANCE_CODEC_CERT.py > R749SPV_WALSH_UNIMODULAR_PROVENANCE_CODEC_RESULTS.json` using standard-library Python. The JSON records the exact anchor indices, two alphabets, count statistics and all-level decoder success. Author check: `PASS`; independent mathematical review: pending.

**Next scientific problem:** derive a rational generating-function or chamber theorem for the difference `M_{A_zero}(n,X)-M_{A_shift}(n,X)`, and determine whether the finite maximum-fiber reversal persists, oscillates, or eventually stabilizes. A separate research direction is the exact native signed/branch-preserving lift of the 22-count residual.
