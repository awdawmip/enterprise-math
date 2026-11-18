# R762FD — Exact stationary 85-state BRC orbit quotient for q=9

Research date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECK_PASS / NOT_REVIEWED.

Research lineage: independent portable continuation of RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Earlier R762EM/EO/FA/FC are context; this elementary theorem has its own proof. P000 and six-dimensional signed X6 world are unchanged.

## Model and exact statement

Let q be any odd positive integer and G=(Z/qZ)^3. Keep six separate, positive, unit-weight, named BRC branches:

B = {(0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)}.

In Z[G] put P=1+X+Z+XY+YZ+XYZ, and write c_n(g)=[g]P^n for n>=0. All coordinates below are modulo q. For g=(x,y,z), define

\[
u_n(g)=(2x-n,\ n-2y,\ 2z-n),\qquad
\kappa(u)=\min_{\rm lex}\{\operatorname{sort}(u),\operatorname{sort}(-u)\}.
\]

Sorting uses the representatives 0,...,q-1. Multiplication by 2 is invertible modulo odd q, so u_n is a bijection of G.

**Theorem 1 (complete terminal recovery):** For all odd q and every n>=0, c_n(g) depends only on the key \(\kappa(u_n(g))\). The number of endpoint *orbit classes*, not necessarily different numerical coefficient values, is exactly

\[
\boxed{d_q=\tfrac12\left[\binom{q+2}{3}+\tfrac{q+1}{2}\right].}
\]

For q=9 the complete 729-integer terminal vector is reconstructed from 85 values and the explicit time-indexed decoder \(g\mapsto\kappa(u_n(g))\).

**Theorem 2 (stationary state evolution):** Define the six centered signed steps

\[
S=\{(-1,1,-1),(1,1,-1),(-1,1,1),(1,-1,-1),(-1,-1,1),(1,-1,1)\}.
\]

Let \(K_q\) be the set of keys and define the \(d_q\times d_q\) nonnegative integer matrix

\[
T_{k,\ell}=\#\{s\in S:\kappa(k-s)=\ell\},\quad k,\ell\in K_q.
\]

Let \(v_n(k)\) be the coefficient at any endpoint g whose key is k. Then the same time-independent matrix T gives

\[
\boxed{v_{n+1}=Tv_n,\qquad v_0(k)=\mathbf1_{k=(0,0,0)},\quad
c_n(g)=v_n(\kappa(u_n(g))).}
\]

At q=9 this is a fixed 85-state nonnegative integer BRC recurrence, with 405 nonzero matrix entries and 510 counted six-branch edges. The raw positive BRC system has 729 states and 4,374 counted edges per update.

**Corollary (no-extra-precision terminal period certificate):** If the candidate shift L is divisible by q, the decoders at n+L and n agree. For an equality or congruence between \(P^{n+L}\) and an integer scalar multiple of \(P^n\), checking one endpoint representative per orbit is equivalent to checking all q^3 endpoints. A q=9, 127-time-window comparison thus needs 127*85=10,795 coefficients instead of 127*729=92,583, saving 81,788 comparisons (644/729 or approximately 88.34%). The previously used recurrence and valuation hypotheses are not changed. This is a reduction in terminal comparisons, not a claim that the prior high-precision periodicity test was rerun.

## Proof

For a branch \(b=(b_x,b_y,b_z)\) define the centered step
\(s(b)=(2b_x-1,1-2b_y,2b_z-1)\).
The set of the six s(b) is precisely the set of sign triples in \(\{+1,-1\}^3\) with *not all signs equal*. The 12-element group \(S_3\times C_2\) of coordinate permutations and simultaneous negation acts on S by permutations of six distinct branch labels.

For every ordered word \(b_1,\ldots,b_n\), its endpoint is \(g=\sum b_j\), and
\(u_n(g)=\sum s(b_j)\). Applying one group element to all the centered steps gives a unique word in the six named branches with transformed centered endpoint and the same positive multiplicity. The inverse group element inverts this word map. This proves that all endpoints in one centered orbit have equal coefficients.

Under the coordinate-permutation group \(S_3\), a triple corresponds to a size-three multiset on q residues; there are \(\binom{q+2}{3}\). The involution induced by simultaneous negation fixes exactly \(\{0,0,0\}\) and the \((q-1)/2\) multisets \(\{0,a,-a\}\), since q is odd. Burnside's formula for negation on multisets gives
\(d_q=(\binom{q+2}{3}+(q+1)/2)/2\).
As \(u_n\) is bijective, the count is the exact number of terminal orbits.

The six-branch BRC convolution is
\(c_{n+1}(g')=\sum_{b\in B}c_n(g'-b)\).
The exact identity
\(u_n(g'-b)=u_{n+1}(g')-s(b)\)
gives the claimed matrix update. Its value is independent of the selected representative of the next orbit because every group element permutes S. This proves the well-defined *stationary* quotient for arbitrary orbit-constant input vectors, not just the observed powers of P; initialization proves the formula at all n.

If \(q\mid L\), then \(u_{n+L}(g)=u_n(g)-L(1,-1,1)=u_n(g)\) in G. The orbit partitions used to decode both endpoint vectors are identical, and an integer scalar preserves orbit constancy. Hence equality (or congruence in any integer modulus) on all representatives is equivalent to equality on all endpoints, proving the corollary.

## Observer boundary: explicit fixed-branch counterexample

The quotient is exact for positive whole-six-branch BRC counts and for operations descending through that observer. It **does not** identify branch-sensitive future paths or native signed Cell/Link/Port state.

For q=9 at n=1, g=(0,0,0) and h=(1,1,1) have the same orbit key. Append the same fixed, named X branch (1,0,0) to each word. At n=2 the corresponding endpoints (1,0,0) and (2,1,1) have *different* orbit keys. Thus a named single-branch update is not a function on the compressed keys; branch/provenance data must be retained for such operations. Positive BRC count symmetry is not signed native TRIADIC_CLOSURE_E.

## Exact validation

The accompanying Python checker runs the original six positive integer branch convolutions and the independently defined stationary compressed matrix, then compares **every** raw endpoint: q=3 for n=0..72 (1,971 comparisons), q=9 for n=0..90 (66,339), and q=27 for n=0..12 (255,879), totalling 324,189 exact coefficient comparisons. It also tests arbitrary orbit-constant initial vectors at every residue n mod q, proves computational mass consistency \(\sum_gc_n(g)=6^n\) on those finite ranges, checks the 85-state/405-nonzero q=9 matrix, and checks the named-branch non-descent witness. All checks passed using Python integers, no floating arithmetic. Universal mathematical scope follows from the branch-word bijection/Burnside proof, not from finite testing.

Run: python3 R762FD_Q9_SIX_BRANCH_ORBIT_VERIFY.py > R762FD_Q9_ORBIT_EVIDENCE.json

## Relationship, scope and next direction

This quotient gives a new exact 85-state stationary route for the same positive six-branch q=9 coefficient family studied by R762EM/EO/FA/FC. Its output at a *fixed raw endpoint* (for example the return moment at g=0) uses a time-dependent selection of orbit coordinates, so the reported 127-order scalar return recurrence and this 85-state representation are not contradictory. The quotient does not change the P000 six-axis ontology or the signed triadic event target.

Next: replace 729-coordinate comparisons by 85 representatives in one existing h=7/h=8 period certificate and measure the entire preprocessing, arithmetic, normalization, and decoding cost; seek a symmetry-adapted 3-adic recurrence for T; separately preserve the named-port and signed Cell/Link/Port transport open question.

Research-author proof and finite regression only. Independent scientific review: NOT_REVIEWED. Formal Result/Review/Source PROGRESS: not claimed.
