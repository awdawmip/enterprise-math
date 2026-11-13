# R763 — Perfect BRC frame residual survives every solvable group observer

Date: 2026-11-13 Asia/Shanghai. Scientific line R760 (PR #2225), with independent, contemporary R761 (#2231) and R762 (#2235) signed-triad candidates. Parent task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Frozen input remains awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

## Exact candidate and scope

Choose m of the six native X6 axes, 2 <= m <= 6. Their ordered signed step words form the free group F_m on generators x_1,...,x_m. A word preserves native step order and provenance; no P000 primitive force event is inferred. An m=2 subword is not a native two-dimensional plane.

Use R759/R760's declared **auxiliary internal frame**: phi:F_m -> S_(m+1), where phi(x_i)=phi(x_i^-1)=(0 i). Label 0 is an auxiliary frame label, not a seventh spatial axis. Products follow right-to-left permutation composition; the chronological frame H(w)=phi(w)^-1 has the corresponding left-coset form.

A solvable group observer is any group homomorphism theta:F_m -> Q into a solvable group Q with finite derived length r >= 1. Q need not be finite. This includes every finite iterated extension by abelian groups and any finite direct product of nilpotent group observers, but not arbitrary nonlinear algorithms, non-solvable observers or the full untruncated Magnus series.

## Main theorem (every solvable-observer fiber, exact dichotomy)

Let 4 <= m <= 6 and n=m+1, so 5 <= n <= 7. For every solvable group observer theta:F_m -> Q, let K=ker theta. Then

(1) phi(K) contains A_n and is exactly one of A_n, S_n.

(2) For every u in F_m, the exact rooted-frame set on the observation fiber is

    { phi(v) : theta(v)=theta(u) } = phi(u) phi(K).

Thus every observation fiber contains at least n!/2 distinct frames. It contains exactly the n!/2-element parity coset if sign composed with phi factors through theta(F_m), and all n! frames otherwise. In particular no solvable group quotient is sufficient to reconstruct the complete auxiliary frame.

(3) The exact worst-case fixed-code frame-repair requirements are:

| X6 axes m | auxiliary frame | parity-retaining states | minimum bits | parity-losing states | minimum bits |
|---:|---|---:|---:|---:|---:|
| 4 | S5 | 60 | 6 | 120 | 7 |
| 5 | S6 | 360 | 9 | 720 | 10 |
| 6 | S7 | 2520 | 12 | 5040 | 13 |

For this group-homomorphic observer class, the cutoff at four axes is sharp. At m=2,3 the full S3/S4 frame image is itself solvable, and theta=phi is a solvable observer that determines the frame completely.

### Proof

Define the derived series G^(0)=G and G^(k+1)=[G^(k),G^(k)]. Star transpositions generate S_n, so phi(F_m)=S_n and phi(F_m^(k)) = S_n^(k) for every k.

The commutator subgroup S_n' equals A_n: sign annihilates all commutators; [ (0 i), (0 j) ] is a nonidentity three-cycle; its conjugates generate all 3-cycles, which generate A_n.

For n>=5, A_n is perfect. A direct identity, with [a,b]=aba^-1b^-1, is

    [ (0 1 3), (0 2 4) ] = (0 1 2).

Both factors are even. Every 3-cycle is an A_n-conjugate of this 3-cycle: choose a relabeling permutation and, if necessary, change its parity by interchanging the two unused labels. Hence [A_n,A_n] contains all 3-cycles, so A_n'=A_n.

Consequently phi(F_m^(k))=A_n for every k>=1. Since Q has derived length r, theta(F_m^(r)) is trivial and F_m^(r) is a subgroup of K. Therefore A_n <= phi(K). As A_n has index two in S_n, the image phi(K) must be either A_n or S_n. The fiber theta^-1(theta(u)) is uK, giving its exact frame image by applying phi. The kernel K lies inside ker(sign o phi) precisely when the parity character descends to theta(F_m), proving the two cases. Their cardinalities give the exact frame-only fixed-code bounds.

For m=2,3, the groups S3 and S4 are solvable, so theta=phi provides the stated counterexamples to extending the universal theorem to smaller supports. QED.

## Constructive witnesses at all derived depths

For distinct axes i,j define W_1(i,j)=[x_i,x_j], where the bracket is the group commutator. Then W_1(i,j) lies in F_m' and phi(W_1(i,j))=(0 i j).

For r>=2, choose distinct k,l outside {i,j} from the remaining axes, possible whenever m>=4, and recursively set

    W_r(i,j) = [ W_(r-1)(i,k), W_(r-1)(j,l) ].

Then W_r(i,j) lies in F_m^(r) and

    phi(W_r(i,j))=[ (0 i k), (0 j l) ]=(0 i j).

Its raw unreduced signed-step length is exactly 4^r. This gives a concrete nonidentity-frame word annihilated by every solvable observer of derived length at most r. Every conjugate in F_m of W_r also lies in F_m^(r); its frames realize the conjugate three-cycles. R763_SOLVABLE_FRAME_VERIFY.py checks depths r=1,2,3,4 (lengths 4,16,64,256) for m=4,5,6.

These witness words are spatial Cell-return loops; for r>=2 they also have zero signed projected area, because F_m'' is contained in gamma_4(F_m). They have no automatic TRIADIC_CLOSURE_E force-event, V29 PASS or native V39 interpretation.

## Independent finite verification

Exact standard-library Python checks enumerate S_n and A_n for n=3..7, test sign parity and the derived alternating subgroup, and confirm the above commutator identity. The results are 6/3/1 for n=3, 24/12/4 for n=4, 120/60/60 for n=5, 720/360/360 for n=6, and 5040/2520/2520 for n=7 (S_n, A_n, A_n'). The constructive W_r recursion is checked at four levels on each of m=4,5,6. The proof, not a finite enumeration, establishes the all-solvable-group quantifier.

## Scientific consequence and next interface

R760 established an alternating residual for every fixed finite Magnus signature. The present theorem identifies a stronger structural cause: the perfect alternating subgroup survives *all solvable group-homomorphic path observers*, irrespective of their size or finite derived length.

R761 and R762 separately investigate candidate signed triadic-Port incidence, A6 orientation and overlap commutators; those are not a validated native TRIADIC_CLOSURE_E/V39 map. The next discriminating question is whether the **actual P000-admitted primitive triadic event** and its V29/V39 transport generate a perfect residual group or only a solvable quotient. Such an interface requires a typed, source-preserving Cell/Link/Port incidence and update construction. Until then the theorem is exact in the auxiliary path model. P000, the six native axes, 120-degree PERP_E, frozen science and branch provenance remain unchanged.

This author-side research paper makes no claim of live task CLAIM, formal Source Result, independent Driver review or Foundation promotion.
