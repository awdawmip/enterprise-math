# X6 R87 — Four-channel BRC: exact phase diagrams on six paired-precision rays

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: CONDITIONAL_SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Mode: independent portable observation study, no formal CLAIM or RESULT.

## Frozen model and antecedent

Use the four-channel positive-count BRC star-histogram readout with a shared unknown additive offset, maximum success degree four and integer difference a=(x,y,z), identified up to sign. It is an abstract conditional observer, not a native X6 signed triadic event or a time-dynamics experiment. Preserve the published task science pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, with current ACTIVE worldview and provenance rules separately read.

R86 antecedent: research_notes/portable_direct/2026-11-21_x6_r86_absolute_nine_core_full_port_profile.md. Its author-side all-lattice certificate gives for p>=125 and any positive w the exact formula η*(p,w)=min over S9 of F(a;w), where

\[
Z(a)=(0,2x+6y+12z,6x+24y+60z,14x+78y+252z),\quad
g_{ij}=|Z_i-Z_j|/2,\quad
F(a;w)=\max_{i<j} g_{ij}/(w_i+w_j).
\]

The nine exact q-labelled vectors are

| q | a |
|---:|---|
| 7 | (6,-4,1) |
| 10 | (9,-5,1) |
| 11 | (10,-5,1) |
| 16 | (15,-6,1) |
| 27 | (24,-14,3) |
| 39 | (36,-16,3) |
| 43 | (39,-20,4) |
| 49 | (45,-21,4) |
| 125 | (114,-56,11) |

## Theorem R87: all six paired rays

For a two-element heavy-channel set H in {1,2,3,4}, set w_i(t)=t for i in H, and w_i(t)=1 otherwise; t>0 and integer p>=125.

**Alternating pairs H={1,3} or H={2,4}.**

\[
\boxed{\eta^*_{p,4}(w_H(t))=\frac{1}{1+t}\quad(t>0).}
\]

The q=11 vector (10,-5,1) is the unique optimal direction at every t>0.

**Neighboring pairs H={1,2}, {1,4}, {2,3}, {3,4}.**

\[
\boxed{
\eta^*_{p,4}(w_H(t))=
\begin{cases}
6/(1+t),&0<t\le 1/11,\\
1/(2t),&1/11\le t\le1,\\
1/2,&1\le t\le11,\\
6/(1+t),&t\ge11.
\end{cases}}
\]

For 0<t<1/11 exactly two directions are optimal (low winners); for 1/11<t<11 only q=11 is optimal; for t>11 exactly two are optimal (high winners). Exactly three directions tie at each t=1/11 and t=11 (q=11 plus the corresponding two winners). At t=1, q=11 is unique.

| H | Low winners q | High winners q |
|---|---|---|
| {1,2} | 10,27 | 39,43 |
| {1,4} | 27,49 | 16,39 |
| {2,3} | 16,39 | 27,49 |
| {3,4} | 39,43 | 10,27 |

## Symbolic proof

For each H let L be its complementary two-channel pair. For any vector define h=g_{H1,H2}, ℓ=g_{L1,L2}, and m=max of the four cross-pair half-gaps. The full objective is

\[
F(a;w_H(t))=\max\{h/(2t),\,m/(1+t),\,\ell/2\}. \tag{R87-1}
\]

By exact substitution of the nine listed vectors into Z, the q=11 vector has (h,m,ℓ)=(0,1,0) on either alternating pair, and (1,1,1) on any neighboring pair. For all other eight directions, the cross-pair maximum m is at least 6 for each of the six H. These are 6×9 integer computations; every triple is stored in the accompanying certificate.

For alternating H, the q=11 objective equals 1/(1+t), while every other candidate is at least 6/(1+t), giving the formula and uniqueness.

For neighboring H, q=11 yields max{1/(2t),1/(1+t),1/2}=max{1/(2t),1/2}. The other candidates are at least 6/(1+t). At t<=1/11, precisely the two low winners in the table have (h=0,m=6,ℓ<=6), hence they realize 6/(1+t), since 6/(1+t)>=11/2>3. At t>=11, precisely the two high winners have (ℓ=0,m=6,h<=6), hence they realize 6/(1+t), since 6/(1+t)>=6/(2t). In between, q=11 is strictly better.

The exact crossings are 1/(2t)=6/(1+t) iff t=1/11, and 1/2=6/(1+t) iff t=11. At the first crossing, any further equal-cost non-q11 candidate would need m=6 and h<=1; only the two listed low winners satisfy h=0 with the necessary gap. At the second crossing, equality requires m=6 and ℓ<=1; only the two listed high winners have ℓ=0. Off those two boundaries the same exact gap table excludes additional winners. The claimed multiplicities follow.

## Verification, scope and next questions

Run with Python 3: python3 research_notes/portable_direct/x6_r87_pair_anisotropy_verify.py. The companion JSON records all six sets of nine (h,m,ℓ) triples, the witnesses and exact parameter checks. Local Python Fraction run on 2026-11-21: PASS for 6×70²=29,400 exact rational pair/parameter trials, with explicit boundary and winner-count assertions. The general real-t theorem follows from the symbolic finite gap inequalities, not numerical interpolation.

This conditional readout claim inherits R86's author-side nine-core all-lattice proof and has not received independent review. No physical/native X6 time law, lossless named Port decoder, future-operation-safe joint-event quotient, or completed R063 benchmark is asserted.

Next: classify multiway tie intersections in the full projective four-weight space; and separately construct an exact source-defined signed/triadic named-Port observer with a specified future-operation horizon, then establish fiber constancy or exhibit two future-distinguishable histories.
