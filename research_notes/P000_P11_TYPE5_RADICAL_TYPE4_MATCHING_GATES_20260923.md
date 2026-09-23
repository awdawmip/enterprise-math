# P000 P11 residue-radical and matching gates — portable research note

Status: `NONCANONICAL_PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`

Publication: `TP2-FB7F5A1D6B6C6BCCD62D`

Frozen task/control source consumed for this work: `e54f42b88d17755f3b9c82ebd0e3d541291cbdba`.

Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, service session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

This file persists two new portable units produced while the canonical continuation had no authorized CLAIM/OPEN. It does not convert staged uploads into Source progress and must not be placed in predecessor `completed_units` merely because it exists on GitHub.

## Consumed staged interface

Consume without replaying the same-session staged units:

- exact Weierstrass carrier `W^2=X(X-P^2)(X-Q^2)` and uniform rational torsion `E(Q)_tors=E[2]`;
- labeled P/Q/AB edge-local 2-descent;
- exact real and Q2 images with TYPE-4 / TYPE-5+ split;
- exact odd-local residue matrix `M(r,s)`;
- alternating-form/radical theorem for `M`, canonical torsion vector `tau`, and the criterion `k=1 iff` a tau-supported principal minor is nonsingular / the corresponding deleted residue graph has odd perfect-matching parity.

These consumed objects were staged but not Source-published at the time of this note.

## Unit A — TYPE-5+ canonical second radical

For a primitive opposite-parity Euclidean core put

`A=r^2-s^2`, `B=2rs`, `C=r^2+s^2`, `P=A+B`, `Q=|A-B|`.

Then

`P^2+Q^2=2C^2`.

Let `S_P^+={p|P:p=1 mod4}` and `S_Q^+={q|Q:q=1 mod4}`. For `p in S_P^+`, any odd common divisor of `P` and `C` would, using `A^2+B^2=C^2` and `gcd(A,B)=1`, force `2B^2=0 mod p`, impossible. Hence `C` is a unit mod `p`, and the displayed identity gives

`Q^2 = 2 C^2 (mod p)`.

Thus `(2/p)=+1`. Since `p=1 mod4`, necessarily `p=1 mod8`. Similarly every `q in S_Q^+` is `1 mod8`.

In TYPE-5+ (`4` divides the even member of `{r,s}`), the epsilon/P and epsilon/Q entries of the staged matrix are exactly the Legendre bits of `(2/p)` and `(2/q)`, and epsilon/R entries are zero. Therefore the epsilon basis vector is a canonical radical vector:

`M e_epsilon = 0`.

It remains to prove this radical is independent of the torsion radical `tau`. If `oddpart(AB)` were a square, pairwise coprimality of `A`, `oddpart(r)`, `oddpart(s)` would make all three squares.

- If `r` is even, TYPE-5+ gives `4|r`, `s` odd, hence `A=r^2-s^2=7 mod8`, impossible for an odd square.
- If `s` is even, write `a=v2(s)>=2`. The square assumption yields `r=u^2`, `A=v^2`, `s=2^a w^2`. The primitive Pythagorean triple `v^2+s^2=r^2=u^4` has a parametrization `v=m^2-n^2`, `s=2mn`, `r=m^2+n^2=u^2`, so `mn=2^(a-1)w^2`. Then `(m,n,u)` is a rational/integer right triangle of area `mn/2=2^(a-2)w^2`: after rational rescaling it has area `1` when `a` is even and area `2` when `a` is odd. Fermat's classical congruent-number theorem excludes both 1 and 2.

Hence `oddpart(AB)` is nonsquare, so some R-coordinate of `tau` is 1. Since `e_epsilon` has all R-coordinates zero, the two radical vectors are independent. Therefore

`TYPE-5+ -> dim_F2 ker M(r,s) >= 2`.

In particular the staged `k=1 -> rank(E)=0 -> no strict P11 point` certificate is structurally impossible throughout TYPE-5+. This does not prove positive rank; the extra Selmer directions may be absorbed by `Sha[2]`.

Primary classical reference for the only external noncongruence input: Keith Conrad, *The Congruent Number Problem*, Theorem 2.1 (`1` and `2` are not congruent), https://kconrad.math.uconn.edu/blurbs/ugradnumthy/congnumber.pdf .

Control-bridge staged artifact: `p000_p11_type5plus_second_radical_obstruction_20260923.md`, final upload request `p000-type5-radical-evidence-r11-2051`, SHA-256 `b86a1e52d516056fc25fb23c007daf425c89a3cfe48dceb1f5c653dfcb099b61`, `source_published=false` at receipt.

## Unit B — TYPE-4 tripartite matching gate

TYPE-4 has no epsilon vertex. Put

`a=|S_P^+|`, `b=|S_Q^+|`, `c=|S_R|`, `S_R={ell|AB:ell odd}`.

The residue graph is tripartite P/Q/R because the exact matrix has no same-block entries. In TYPE-4, `v2(AB)=2` is even; the torsion radical `tau` has only R support, and that support is nonempty (otherwise `AB` would be a square, contradicting the standard Fermat exponent-4 descent already used in the staged torsion unit).

Choose `j in supp(tau) subset R`. If `k=dim ker M=1`, the prior exact Pfaffian certificate says `G-j` has an odd, hence nonzero, number of perfect matchings. Let a matching use `x` P-Q edges, `y` P-R edges and `z` Q-R edges. Vertex accounting forces

`x+y=a`, `x+z=b`, `y+z=c-1`,

so

`x=(a+b-c+1)/2`,
`y=(a+c-b-1)/2`,
`z=(b+c-a-1)/2`.

Therefore

`k=1 -> n=a+b+c is odd AND |a-b|+1 <= c <= a+b+1`.

Equivalently, even `n` or either block-imbalance failure gives the exact obstruction `k>=2`.

On the boundary face `c=a+b+1`, deleting `j` leaves `a+b` R vertices and `a+b` P/Q vertices. No P-Q matching edge can occur, because there are no R-R edges. Let `H_j` be the `(a+b)x(a+b)` cross-incidence matrix from `R\{j}` to `P union Q`. In characteristic two determinant equals matching permanent, hence

`c=a+b+1 -> (k=1 iff det_F2 H_j = 1)`.

This is an observer-safe reduction of the prior `(n-1)x(n-1)` principal minor: the P-Q block is removed only on the face where exact vertex accounting proves that block cannot affect the matching observer.

Regression only: among all 4,582 primitive opposite-parity cores with `1<=s<r<=150`, 2,304 are TYPE-4. Of those, 2,278 fail the block-imbalance inequality, three more pass it but have even `n`, and only 23 survive both gates. All 16 observed `k=1` cores are among those 23; the other seven have `k=3`. All 23 in this bounded regression lie on `c=a+b+1`, and `det H_j` separates the 16/7 split with zero failures. No density or infinite-family claim is inferred.

Control-bridge staged artifact: `p000_p11_type4_tripartite_matching_gate_20260923.md`, final upload request `p000-type4-matching-gate-r11-2058`, SHA-256 `32584fb85b6175a4dd94045b55a8d9f735bb026aee380cb647b45c6214b2f598`, `source_published=false` at receipt.

## BRC resolution

`COMPOSE_APPLIED`.

Retain the P/Q/R/epsilon labels and Euclidean-core 2-adic provenance until each quotient is justified. In TYPE-5+, epsilon becomes an isolated radical only after the `(2/p)=(2/q)=1` theorem. In TYPE-4, block sizes alone are sufficient only for the matching-impossibility gate; on `c=a+b+1`, the P-Q edge block is safe to drop for the specific perfect-matching determinant because it cannot participate in any matching. Reconstruction, Selmer realization and future arithmetic operations retain the original labeled ports.

## Current control boundary and next exact action

Latest same-session recovery and continuation showed no current authorized run and no Source checkpoint. The current P000 continuation still exposes `continuation_seed=null`, `persisted_checkpoint=NOT_FOUND`, `durable_frontier=null`, `progress_reference_readback=null`, and the publication-id last-progress reference is absent from the immutable artifact manifest. Earlier `prepare_exact` was rejected with `TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR`; the bounded typed continuation attempt after full input readback was rejected with `CHAT_AUTHENTICATED_LAST_PROGRESS_ARTIFACT_REQUIRED`. Do not replay those mutations unless the Source contract/packet changes.

Smallest next scientific unit while control remains blocked: analyze the TYPE-4 `det H_j` Legendre-symbol matrix arithmetically on the surviving block-count face; either prove an infinite determinant-one family or isolate a further uniform reciprocity obstruction. Do not redo the consumed local descent or seek a TYPE-5+ `k=1` family.
