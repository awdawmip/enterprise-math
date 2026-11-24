# R5 — Partial named Set future-safety: exact hyperedge formula and state-family counts

Date: 2026-11-16 (Asia/Shanghai).
Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Provenance: previous R5 ring-of-triangles source-labelled common-library theorem and `r5_slack2_future_safe_star_20261116`, followed by `r5_named_set_homomorphic_slack_20261116`. This is an auxiliary integer indexed-center observer, not an assertion about native X6 spatial dynamics; P000 is unchanged.

## Problem

For n>=1, let X={0,1}^n with bitwise order and let h(x)=sum_{empty != A subset [n]} w_A product_{i in A}x_i, with finitely many coefficients w_A>=0 (rational or integer). Fix a set J of coordinates permitted in named Set_i(0/1) commands. Assume the same *common-source cost law* as the inherited ring model: a nonempty raw belief B may use a genuine source-labelled common library of size C+h(OR B), while the individual optimum for u is C+h(u). For general hypergraphs this common-source law is a stated premise; the algebraic future-safety result is conditional on it.

Write r=OR B and D(r,u)=supp(r) minus supp(u), for u in B. For a finite Set command word T put loss_T(r,u)=h(T(r))-h(T(u)).

## Theorem 1 — exact supremum over all future command words

For every r>=u, define D=D(r,u), E=supp(r) union (J minus D), and the integer or rational quantity

    Delta_J(r,u) = h(1_E) - h(1_(E minus D))
                 = sum_{A subset E, A intersects D} w_A.     (1)

Then

    max_{finite words T using only J} loss_T(r,u) = Delta_J(r,u).  (2)

The maximum is attained by the single word that sets every coordinate in J minus D to 1 and leaves coordinates in D untouched. No other commands are needed.

**Proof.** A finite sequence of named Set commands has the same concrete action as one simultaneous partial overwrite on a subset S of J. For any hyperedge A, its contribution to h(T(r))-h(T(u)) is either zero or w_A, since T(u)<=T(r). It contributes exactly w_A only when A is contained in supp(T(r)) and contains at least one coordinate where T(r) and T(u) still differ. The surviving differences belong to D minus S. Also supp(T(r)) is contained in E: coordinates outside supp(r) that may turn on belong to J minus D. Thus every contributing A lies in E and meets D, and positivity proves the upper bound Delta_J. Setting all coordinates of J minus D to 1 while leaving D unchanged makes supp(T(r))=E and supp(T(u))=E minus D, so every hyperedge counted in (1) contributes and the bound is attained. QED.

## Theorem 2 — exact partial-control future-safe criterion

For every nonempty B with r=OR B, every finite word of named controls in J has source slack at most s>=0 over *each possible underlying raw input* if and only if

    Delta_J(r,u) <= s for all u in B.                       (3)

Indeed OR(T(B))=T(OR B) since every named overwrite commutes with finite coordinatewise OR. Therefore the slack of the common source library following T is max_{u in B} loss_T(r,u). Taking max over T and u and invoking Theorem 1 yields (3).

For the k>=3 unit-weight cycle observer q(x)=sum_{i mod k}x_i x_{i+1}, (1) becomes the **number of cycle edges lying inside E and incident to D**. This yields a direct bitset certificate, no search over command histories. In particular J=all gives Delta_all(r,u)=number of cycle edges incident to D, because E=[k]; at budget s=2 that is <=2 exactly when |D|<=1. Thus Theorem 2 strictly extends the inherited all-coordinate radius-one-star theorem.

At J=empty it reduces to the present-time condition q(r)-q(u)<=s. If J grows, Delta_J(r,u) cannot decrease: future safety is monotone with respect to the allowed command repertoire.

## Theorem 3 — exact count of future-safe source beliefs

For a fixed r let F_r(J,s)={u<=r:Delta_J(r,u)<=s}. For S subset supp(r), put n_r(S)=|{u in F_r(J,s): supp(u) intersects S is empty}|. The number of nonempty future-safe belief families B with OR B=r is

    C_r(J,s)=sum_{S subset supp(r)} (-1)^|S| (2^n_r(S)-1). (4)

The total number is C(n,J,s)=sum_r C_r(J,s). The proof is inclusion-exclusion: count nonempty subfamilies of F_r that cover every coordinate in supp(r). This exact formula avoids enumeration of all 2^(2^n) raw belief families. When J=[k] and s=2, it recovers B_k=2*3^k-(k+2)*2^(k-1).

## An exact contrast witness

For k=6 set J={0}, r=42 (bits {1,3,5}) and u=0. The belief B={r,u} has OR r, and the unrestricted raw difference has three missing 1-bits. Still Delta_{J}(r,u)=2, so it is **future-safe for every command word using only node 0** at budget two. If all six nodes are controllable, Delta_all(r,u)=6, so this same belief is not safe. This is a real distinction between current observation, restricted future and arbitrary future.

## Reproducible exact checks

Run `node VERIFY_R5_PARTIAL_SET_FUTURE_SAFETY.js` (plain JS, integer and Boolean arithmetic only). The executed program exhaustively compared formula (2) with every partial overwrite for **all J, all comparable r>=u and k=3..6**, totaling 3,257,280 ring command evaluations. It separately tested all 3^7=2187 nonnegative weight assignments to seven nonempty hyperedges on three vertices, with 3,779,136 command evaluations. For k=3,4 all J, it enumerated 1,050,600 nonempty belief-family candidates and matched (4). It calculated C(k,J,2) for selected control patterns for k=3..7, including all-control recovery of the earlier closed form.

The general result follows from the proof; finite checks are reproducible regression evidence. No numerical solver or rounding assumptions are used; independent review is NOT_REVIEWED.

## Next question

Use (3) to reduce the candidate families in the exact dynamic controller program for partial J. Compute N_dyn(k,J,2) for a single named node and for two adjacent nodes and compare with the homomorphic projection bound. Test whether allowed control scope yields a provably smaller source-labelled controller with deterministic, transition-closed states; keep exact source-library identities. This unit does not assert an unrestricted full-control lower bound or canonical Task/CLAIM/Result acceptance.
