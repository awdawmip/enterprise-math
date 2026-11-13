# R5 — Exact maximum K_{2,3} circuit word length 15 in a fixed lawful Blackwell fiber

Date: 2026-11-11 Asia/Shanghai. Status: author-side proof and executed exact-rational checker; independent Source review pending.

## Frozen scientific model

Frozen scientific pins (unchanged): Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. This is the auxiliary P/Q–BRC Blackwell model of PRs #2017, #2021, #2026, #2032, embedded as a restricted research observer of P000/native X6, not a replacement ontology.

There are 30 allowed arcs: every (i,j) for i=0,...,6 and j in J={1,2,3,5}, plus (0,0),(6,6). The 21-row observer C records target marginals, source marginals and source first ratio moments. Ratios are r_i=R_i/20 for R=(2,10,15,20,25,30,38). The rational witness E0 of PR #2017, immutable WITNESS.txt blob f9e3671e12604bc29ee2cc07ffc59724bafacc90, has 30 strictly positive masses and minimum

$$m=\frac{196521}{33975844}>0.$$

Its source/target parameter pair satisfies the original five equalities and 26 capacity slacks. All constructions keep that physical pair fixed. The kernel of C has dimension 15 (PR #2021 and the verification attached).

For j<k in J and a<b<c in {0,...,6}, define the integer-normalized K_{2,3} circuit H(j,k;a,b,c) with entries at source j of (R_b-R_c,R_c-R_a,R_a-R_b) on targets a,b,c, their negatives at source k, and all other entries zero. Every H lies in ker C and has exactly six nonzero arcs. There are 6*35=210 such types. This is exactly 20 times the normalization in PR #2032, preserving scalar word length.

For nonzero h in ker C, define L(h) as the least number of these 210 types with **arbitrary real scalar coefficients** whose sum equals h.

## Theorem A — sharp universal and generic length

$$\boxed{\max_{0\ne h\in\ker C} L(h)=15.}$$

Moreover L(h)=15 for Lebesgue-almost every sufficiently small physically feasible signed perturbation, and this includes rational perturbations with both E0+h and E0-h strictly positive.

**Proof.** For j in {2,3,5}, k in {1,...,5}, set B_{jk}=H(1,j;0,k,6). In the 15 repair-coordinate locations h_{k'j'}, these 15 columns form minus 36 times the identity matrix. By PR #2021 these coordinates parameterize ker C, so the 15 circuits B form a basis and L(h)<=15 for every residual.

For any choice of up to 14 circuit types, their span is a proper linear subspace of the 15-dimensional ker C. The union over the finitely many such choices is measure zero and has empty interior. Its complement consists exactly of vectors with L(h)=15. Since E0 is strictly positive on all arcs, the physical coupling fiber has an open 15-dimensional neighborhood at E0, and that complement intersects it in a full-measure set. The proper spans have rational coefficients, so rational vectors outside their finite union are dense as well. QED.

### Fully explicit rational length-15 certificate

Index the basis B_0,...,B_14 in lexicographic (j,k) order and set

$$K=14!\,36^{14}=535356848614986537570569237299200,$$
$$T=K+2=535356848614986537570569237299202,$$
$$\boxed{h_*=\sum_{i=0}^{14}T^i B_i.}$$

For any of the 210 circuits H, its coordinates in this basis satisfy x_{jk}=-H_{kj}/36. Therefore A=36x is an integer column with each entry of magnitude at most 36.

Suppose some collection of at most 14 circuit columns has rank r<=14. Take r linearly independent columns, select r independent rows, and one more row among the 15. Cofactors of these r+1 rows give a nonzero integer row c annihilating those columns, with

$$\max_i|c_i|\le r!36^r\le K.$$

When r=0, a standard basis row works. If h_* belonged to their span, its basis coordinates (1,T,...,T^14) would obey sum(c_i*T^i)=0. Let d be the largest index with c_d nonzero. As c_d is a nonzero integer and T-1>K,

$$\left|\sum_{i<d}c_i T^i\right|
\le K\frac{T^d-1}{T-1}<T^d\le |c_d|T^d.$$

This contradicts cancellation of the leading term. Thus h_* is outside the span of every collection of at most 14 circuits and L(h_*)=15. Its 15-term expansion above is exact.

Every basis circuit has coordinate magnitude at most 36. Hence ||h_*||_infty <= 540*T^14. For the explicit rational perturbation size

$$\boxed{\varepsilon_*=\frac{m}{1080\,T^{14}}}$$

both E0+eps*h_* and E0-eps*h_* retain every arc mass >=m/2>0 and satisfy precisely the same 21 observed values. Thus they satisfy the same original physical constraints. The exact checker also finds support(h_*)=28. This final support count is not used to deduce the length-15 lower bound.

## Theorem B — a small exact length-five witness

Define

$$\begin{aligned}
h_5={}&H(1,2;0,1,2)+H(1,2;3,4,5)\\
&+H(3,5;0,1,2)+H(3,5;3,4,5)\\
&+\frac1{100}H(1,3;4,5,6).
\end{aligned}$$

The first four six-arc supports are pairwise disjoint, covering all 24 arcs from J to targets 0,...,5. The last circuit adds exactly two previously zero arcs, (6,1),(6,3). All its other nonzero coefficients have magnitude <=36/100, smaller than the smallest nonzero integer magnitude of the first four circuits (5). Therefore support(h_5)=26. Any sum of four six-arc circuits has support <=24, while the displayed expression uses five; hence L(h_5)=5. Since ||h_5||_infty<37, choosing eps_5=m/100 makes both E0+eps_5*h_5 and E0-eps_5*h_5 strictly positive and physically lawful.

## BRC interpretation, checks and next research question

In this frozen observer interface, 21 marginal/moment readouts erase a 15-dimensional port-resolved difference. Keeping the 15 repair coordinates permits exact recovery of the full 30-arc coupling. The sparse 210-circuit dictionary supplies constructive decompositions, but almost every invisible residual requires 15 atoms. The 18 incident rays of one particular 14-arc vertex in PR #2032, all requiring at most two atoms, display a special one-sided tangent-cone structure rather than a global word-length bound.

Exact static carrier: labeled signed arc masses retaining source/target ports and joint provenance. Observer: 21 marginal/first-moment values. Allowed future action: reconstruct full coupling with repair coordinates, or perturb within the fixed physical fiber. No unproved quotient to native X6 dynamics is used.

The companion executable VERIFY_CIRCUIT_WORD_LENGTH.py (and local EXACT_OUTPUT.txt) checks the frozen physical witness, all 210 circuits, the independence of the 15 explicit basis circuits, exact reconstruction of each of the 210 types, the root-avoidance lemma's integer input bounds, the 26- and 28-supported witnesses, and positivity/readout preservation for both rational perturbation pairs. The generic measure argument and integer-minor argument are proved above and are not reduced to a finite random experiment.

**Next discriminating question:** examine actual tangent edge rays at the other 1774 vertices of the pinned 1775-vertex radius-four graph ball for minimal word length 3 or more. In parallel, seek an exact global lower bound of 14 positive arcs for this fixed physical fiber.

Publication is author-side evidence and a continuation frontier, not an admitted Source Result, independent review, or task CLAIM.
