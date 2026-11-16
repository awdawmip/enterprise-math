# R203 — Exact four-dimensional orbit-affine minimum for the binary two-step suffix observer

Date: 2026-11-16. Status: AUTHOR_PROVED / EXHAUSTIVE_GF2_CHECKED / NOT_REVIEWED.
Frozen scientific input: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Builds on R201@b2f62925 and R202@f721c4b4. Applies only to the finite source/event observation quotient; P000, X6's six axes, native path and branch provenance remain unchanged.

## Theorem R203 (sharp missing power-alphabet case)

Let T_{2,2} be the monoid of binary words truncated to their final two letters. Its seven elements are

    ε, 0, 1, 00, 01, 10, 11.

The minimum dimension of a faithful affine representation over F_2 whose orbit from **one starting state** separates these seven elements is **exactly 4**.

**Proof — lower bound.** Any such orbit in dimension <=2 contains at most four points. Suppose it exists in dimension 3, with event transformations f_0,f_1 in Aff(F_2^3) and a separating point p. Write p_0=f_0(p), p_1=f_1(p), p_ij=f_j(f_i(p)). These seven points are distinct.

Let M be the linear part of f_0. The suffix identities give

    f_0(p_00)=f_0(p_10)=p_00,
    f_0(p_01)=f_0(p_11)=p_10.

Therefore d_0=p_00+p_10 and d_1=p_01+p_11 (addition in F_2^3) are nonzero vectors in ker M. Also f_0(p)=p_0, f_0(p_0)=p_00 and f_0(p_1)=p_10 are **three different values**. An affine map of rank <=1 over F_2 has an image of size <=2, so rank M>=2. In dimension 3, dim ker M<=1; since d_0 and d_1 are nonzero kernel vectors, they must coincide, and dim ker M=1.

It follows that

    p_00+p_10=p_01+p_11,
    p_00+p_10+p_01+p_11=0.

Four distinct points in F_2^3 with zero vector sum form an affine plane P of four points (a translate of a two-dimensional vector subspace H). The nonzero vector d_0 lies in H and ker M=span(d_0). Since the seven orbit points are distinct, p,p_0,p_1 are outside P. F_2^3 has exactly two H-cosets, so all three lie in the other affine plane P' parallel to P.

But f_0 maps P' into an affine line with exactly two points: its two-dimensional direction H is mapped by M with one-dimensional kernel ker M contained in H. This contradicts the three distinct values f_0(p)=p_0, f_0(p_0)=p_00 and f_0(p_1)=p_10. Hence D=3 is impossible.

**Proof — upper bound.** R201/R202's two-register binary shift with distinct **nonzero** two-bit letter codes γ(0)=01 and γ(1)=10 has four F_2 coordinates and recovers every word in T_{2,2} from its orbit of zero. Therefore D_min=4. QED.

## Why this result is not a mere state-count bound

There are only seven states, so information capacity alone asks for ceil(log_2 7)=3 bits. R203 proves that the **affine update plus a single separating orbit** needs a fourth coordinate. By contrast, R202-C represents all seven elements by seven distinct affine **transformations** on just 2 coordinates using the codes γ(0)=0, γ(1)=1, if the observer can read the entire map instead of a single orbit point. Hence three distinct resource notions remain separate: optimal arbitrary state code (3 bits), action-faithful affine dimension (at most 2 here), and single-orbit-separating affine dimension (exactly 4).

This sharpens R202's power-alphabet interval for (q,a,L)=(2,2,2). It does not assert a general minimum for every q^r alphabet or for the source-plus-tail joint observer.

## Independent finite certificate

\`R203_binary_power_suffix_affine_minimal_check.py\` enumerates all P(7,6)=5,040 injective assignments of p_0,p_1,p_00,p_01,p_10,p_11 to six distinct nonzero points of F_2^3, after translating the initial orbit point p to zero. For each assignment, it tests whether an affine f_0 or f_1 agrees with the complete declared suffix-transition table on all seven states. A basis of three independent state differences fixes the candidate affine map uniquely and the remaining four constraints test consistency.

Observed exact counts: 5,040 assignments, 0 affine-consistent f_0, 0 affine-consistent f_1, 0 jointly consistent pairs. The exhaustive result is supplemental to the human proof; it does not depend on sampling, floating point, ordinary trigonometry or physical calibration. \`R203_verification.json\` records the outcome. Independent mathematical review and native package BRC integration remain pending.

## Next scientific frontier

- Determine orbit-separating affine minima for a=q^r and L>=2 beyond the first binary case.
- Determine the minimum full paired R200 source+tail action dimension, potentially sharing source and tail registers.
- Execute R201's pinned native BRC EffectHistogram integration probe; compare full action map storage, orbit reads, optimal nonlinear state codes and conversion costs.

Control: independent portable research, no formal Task CLAIM, Result, independent Review or P000 alteration.
