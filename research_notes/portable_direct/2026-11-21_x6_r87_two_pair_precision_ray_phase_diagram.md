# X6 R87 — Paired BRC precision rays: optimal value and full-lattice tie multiplicity

Date: 2026-11-21 (Asia/Shanghai).
Status: SYMBOLIC_AUTHOR_PROOF + EXHAUSTIVE_EXACT_INTEGER_AUTHOR_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED.
Independent portable study only; no Task CLAIM, PROGRESS, Result or Review. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.

**Correction to initial R87 paper:** The first draft correctly computed the minimum using the R86 sufficient nine-vector core, but mistakenly identified ties *within this core* as all-lattice tie multiplicities. The original immutable commit remains historic. A complete all-lattice check and R86's finite-reduction bound establish the corrected counts **3, 7, 1, 7, 3**; other, non-core integer vectors can tie with the nine-core winners.

## Observer and theorem

This is the conditional degree-four positive-count BRC star-histogram, with a common unknown additive offset, not a signed native P000 triadic/heartbeat observer. For nonzero integer difference a=(x,y,z) modulo whole-vector negation, define

\[
q(a)=\max(x^++y^++z^+,(-x)^++(-y)^++(-z)^+), \quad
Z(a)=(0,2x+6y+12z,6x+24y+60z,14x+78y+252z),
\]
\[
g_{ij}(a)=|Z_i-Z_j|/2,\quad
F(a;w)=\max_{i<j}\frac{g_{ij}(a)}{w_i+w_j},\quad
\eta^*_{p,4}(w)=\min_{\substack{a\ne0\\q(a)\le p}}F(a;w).
\]

Fix any integer p≥125 and any real t>0. Pick a two-element heavy-channel set H⊂{1,2,3,4}, set w_i=t for i∈H and w_i=1 for the complementary light pair L.

**Alternating heavy pairs H={1,3} or {2,4}:**
\[
\boxed{\eta^*_{p,4}(w_H(t))=1/(1+t),\quad M_H(t)=1\quad(t>0).}
\]
Here M counts *all* global minimizing unoriented integer differences in the full lattice. The unique minimizer is (10,-5,1).

**Neighboring heavy pairs H={1,2},{1,4},{2,3},{3,4}:**
\[
\boxed{\eta^*_{p,4}(w_H(t))=
\begin{cases}
6/(1+t),&0<t\le1/11,\\
1/(2t),&1/11\le t\le1,\\
1/2,&1\le t\le11,\\
6/(1+t),&t\ge11.
\end{cases}}
\]
\[
\boxed{M_H(t)=
\begin{cases}
3,&0<t<1/11,\\
7,&t=1/11,\\
1,&1/11<t<11,\\
7,&t=11,\\
3,&t>11.
\end{cases}}
\]
The central unique minimizer is (10,-5,1). The three extreme open-ray co-minimizers are:

| H | 0<t<1/11 | t>11 |
|---|---|---|
| 12 | (9,-5,1), (15,-9,2), (24,-14,3) | (36,-16,3), (39,-20,4), (75,-36,7) |
| 14 | (24,-14,3), (45,-21,4), (69,-35,7) | (15,-6,1), (21,-10,2), (36,-16,3) |
| 23 | (15,-6,1), (21,-10,2), (36,-16,3) | (24,-14,3), (45,-21,4), (69,-35,7) |
| 34 | (36,-16,3), (39,-20,4), (75,-36,7) | (9,-5,1), (15,-9,2), (24,-14,3) |

The exact seven-element tie sets on both walls are fully enumerated in the companion certificate. All co-minimizers satisfy q≤82, hence are eligible for every p≥125.

## Proof of the optimum values

For each H, let
\[
h=g_{H_1H_2},\qquad \ell=g_{L_1L_2},\qquad
m=\max_{i\in H,j\in L}g_{ij}.
\]
Then exactly
\[
F(a;w_H(t))=\max\{h/(2t),\,m/(1+t),\,\ell/2\}. \tag{R87-1}
\]

R86 (2026-11-21_x6_r86_absolute_nine_core_full_port_profile.md) gives an author-proved, all-lattice equality of the minimum with the minimum over the nine fixed integer differences of q 7,10,11,16,27,39,43,49,125 whenever p≥125. For a=(10,-5,1), direct exact substitution gives (h,m,ell)=(0,1,0) on alternating H and (1,1,1) on neighboring H. Each of the other **eight core** differences has m≥6 for each H. On neighboring H, two core differences have h=0,m=6,ell≤6 and two have ell=0,m=6,h≤6; their q labels for low/high t are H12 (10,27)/(39,43); H14 (27,49)/(16,39); H23 (16,39)/(27,49); H34 (39,43)/(10,27). Thus the exact minimum among the core is
\[
\min\{\max(1/(2t),1/2),\,6/(1+t)\}
\]
for neighboring H, yielding the piecewise formula. The alternating minimum equals 1/(1+t). R86's all-lattice sufficiency transfers these minimum **values** to every integer difference direction. It does *not* identify all equal-cost noncore directions, which is the purpose of the next argument.

## Global tie certification by integer inequalities

R86's exact moment-inverse bound gives, for every a and positive w,
\[
q(a)\le F(a;w)
\left[\frac{181}{12}(w_1+w_2)+\frac{41}{6}(w_1+w_3)+\frac{11}{12}(w_1+w_4)\right]. \tag{R87-2}
\]
On each paired-weight ray the bracket is K_H t+B_H. The exact coefficients and bound maxima are

| H | K_H | B_H | sup_{t>0} eta*(t)(K_H t+B_H) |
|---|---:|---:|---:|
| 12 | 455/12 | 31/4 | 455/2 |
| 13 | 89/3 | 16 | 89/3 |
| 14 | 95/4 | 263/12 | 285/2 |
| 23 | 263/12 | 95/4 | 285/2 |
| 24 | 16 | 89/3 | 89/3 |
| 34 | 31/4 | 455/12 | 455/2 |

These maxima follow by evaluating the exact linear-fractional function on the intervals separated by 1/11, 1 and 11 (and at 0 and infinity); each branch is monotonic or constant. Hence any co-minimizing integer direction has q≤floor(455/2)=227.

A fresh C++17 exact-integer enumeration exhausts **21,492,159** unoriented nonzero directions with q≤234. This includes every possible co-minimizer for any t. In every case the equality conditions on (h,m,ell) reduce to the following finite integer predicates, checked over the whole enumerated domain:

| H class | Parameter regime | Exact/sufficient integer predicate | Enumerated count |
|---|---|---|---:|
| Alternating | 0<t<1 | h=0,m≤1,ell≤1 | 1 |
| Alternating | t=1 | h≤1,m≤1,ell≤1 | 1 |
| Alternating | t>1 | ell=0,m≤1,h≤1 | 1 |
| Neighboring | 0<t<1/11 | h=0,m=6,ell≤11 | 3 |
| Neighboring | t=1/11 | h≤1,m≤6,ell≤11 | 7 |
| Neighboring | 1/11<t<1 | h≤1,m≤5,ell≤10 | 1 |
| Neighboring | t=1 | h≤1,m≤1,ell≤1 | 1 |
| Neighboring | 1<t<11 | h≤10,m≤5,ell≤1 | 1 |
| Neighboring | t=11 | h≤11,m≤6,ell≤1 | 7 |
| Neighboring | t>11 | ell=0,m=6,h≤11 | 3 |

On the two **interior open** neighboring intervals the stated predicates are necessary *supersets*, not claimed if-and-only-if: they each contain the known global minimizer and exactly one vector. All other predicates are equivalent to optimum equality within the stated regime. At the two extremes integrality forces h=0 or ell=0, and m=6 by the exact cost; at wall t=1/11 or 11 the three inequalities are directly equivalent to equality because the global minimum is already known. The exhaustive integer sets prove the total multiplicities for all positive real t. Their actual maximum q is 82, so each exists for p≥125.

## Reproducibility, boundary, continuation

- Core-value checker: x6_r87_pair_anisotropy_verify.py and JSON; 29,400 exact Fraction parameter trials (nine-core, *not* global tie proof).
- Full lattice checker: x6_r87_full_lattice_ties_verify.cpp, build with g++ -O3 -std=c++17 and execute. It enumerates q≤234 with exact signed integer moments, normalizes sign, asserts total count 21,492,159, all 6 paired-class counts and q≤82 of every equality candidate.
- Complete full-lattice results: x6_r87_full_lattice_ties_results.json, including every seven-way wall tie.
- R86 proof/source is inherited at its exact author-certificate status; current R87 remains NOT_INDEPENDENTLY_REVIEWED.

The result concerns a conditional positive-count observer only. No native physical X6 dynamics law, future-operation-safe signed triadic projection, or completed R063 benchmark is claimed. Next problems: classify maximal multiplicity and simultaneous tie-wall intersections for arbitrary four positive channel weights; independently test a source-defined named-Port whole-triadic time observer for fiber constancy or exhibit a future-distinguishing witness.
