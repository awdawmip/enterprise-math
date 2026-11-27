# PREFIX-1141: Full-observer bounded fibers beyond sparse annihilators

Date: 2026-11-28. Researcher: EM-DIRECT-780BBE / TASK_RESEARCH (own registration and managed-session metadata verified). Activity: RA-0ABD84561C86E53067DB0322. Direct continuation; no formal execution claim. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## 1. Frozen inputs and scope

Predecessor: 4a6cfd60a7540f380c09774b4045fcfd6aa8f0f2:research_notes/portable_direct/2026-11-28_r6_prefix1140_radial_reuse_sparse_normals.md. Frozen P000 V5: f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor archive PREFIX-1140-execution-evidence.zip SHA256 45738454cfb8b1826f4cdc617774a37b08d436e1dcadff5d738ee12c19b69ed7; all 134 manifest entries verified before computation. Replayed the predecessor sparse scan (109 directions, 9 cuts, 6 vertices, all 16 candidates excluded). No fresh native BRC moment or anchor inversion was performed. All conclusions about true anomalies inherit Stage46, the anchor certificate and affine-transfer hypotheses. The anchor exit confirmation remains pending.

Let Z=m+U[-1,1]^22 in the ten-dimensional observer space, U comprising the twelve shared columns C and ten independent error axes diag(e). The affine lift at (rho,c) is T=G(-aj*x,am*y-dj*x,0,...,0), x=rho-r0, y=c-u, G=10^125. Under the inherited certificate T belongs to Z. For a rational candidate (p/q,h/q), at L>=10^114 and q>=q0=544447235321021556325566186117974922693, the necessary parameter allowance is 0<=rho-p/q<=K/L^2 and 0<=h/q-c<=H/L, K=d_hi+800000/q0, H=2K. For any integer observer normal n put a=-G(n0*aj+n1*dj), b=G*n1*am, z=n.m, S=sum_j |n.U_j|, v=a(p/q-r0)+b(h/q-u)-z. Necessarily
v <= S+max(0,-a)K/L^2+max(0,b)H/L,
-v <= S+max(0,a)K/L^2+max(0,-b)H/L.
This is the zonotope support inequality with one-sided parameter payments. Since each payment decreases with L, a strict failure at L=10^114 excludes the relation throughout the stated tail.

## 2. Exact coordinate enumeration

Using the six-vertex polygon from PREFIX-1140, reoptimized the unimodular integer coordinates V against polygon edge slopes using rational LLL (five candidate bases including the old basis). At hypothetical Q=10^70 the estimated outer-loop count drops from 71292 to 153; this is a loop-count estimate, not a measured runtime and not a completed enumeration at that Q.

At Q=10^69 the complete coordinate box is [(0,0),(-1,0),(1,9)]; 8 points pass the linear inequalities but none has gcd(p,q)=1. At Q=2*10^69 the box is [(0,0),(-2,0),(1,18)]: 54 coordinate triples, 25 pass all linear inequalities including q bounds, 8 primitive relations. The sliced loop has only three outer pairs. Completeness follows by taking each linear coordinate extremum over q in [q0,Q] and the expanded convex parameter polygon: extrema occur at endpoints of q and vertices of the polygon. V has an exactly verified integer inverse, so no lattice points are omitted. The verifier also checks every edge support inequality and gcd. All eight primitive parameter points already belong to the unexpanded PREFIX-1140 polygon. Their smallest denominator before full-observer separation is 1041353783449749807341823845353839802680219216774460847640273680962923.

An independent implementation used original polygon edge normals plus coordinate axes rather than the expanded Minkowski hull. A standalone certificate uses outward grid cells of side 10^-140 enclosing the six original vertices, checks the same 54/25/8 counts with exact fractions, and has a separate exact check of the twelve original vertex coordinate enclosures in the execution evidence.

## 3. Complete annihilator quotient and its limit

The first six dominant columns have rank six. Let B be a full-rank 4-by-10 integer annihilator basis, so B*C_j=0 for j<6. The projected remaining sixteen generators span R^4. Every facet normal of their full-dimensional zonotope is perpendicular to three linearly independent generators: indeed a supporting face is the sum of its forced generator endpoints and the segments corresponding to zero dot products, and a facet has dimension three. Conversely a normal from such an independent triple supplies a valid support inequality. Enumerating all such normals, with both signs, therefore describes the entire quotient zonotope; pulling back gives every necessary inequality obtainable by annihilating the first six columns (with the signed parameter allowance handled separately). The actual enumeration: 560 triples, 525 nonzero, 345 distinct primitive directions up to sign. Two further active cuts produce ten polygon vertices, with unchanged marginal widths approximately 7.168522e-102 (rho) and 3.439906e-101 (c). All eight candidates survive these complete annihilator-direction tests with the inherited signed scale allowance at L=10^114.

The quotient intentionally loses the bounded coefficient ranges of the first six generators. Annihilation is sound for exclusion but is not equivalent to membership of the original bounded zonotope: it can permit a lift whose first six coefficients exceed one in magnitude. Repeating scans restricted to these annihilators cannot settle the eight candidates through the tested necessary inequalities. This motivates retaining the full bounded fiber instead of treating the leading columns as irrelevant.

## 4. Exact full-observer separation and feasibility witnesses

Choose invertible pivot columns indexed (zero-based) by [0,1,2,3,4,5,15,16,19,20]. For a fixed affine target, write U_P z_P = T-m-U_F z_F. Solve the pivots exactly as functions of the twelve free coordinates. Floating linear programming was used only to suggest a dual normal or feasible free coordinates, not to decide any claim. For a feasible witness, round free coordinates to integer multiples of 10^-12, solve the pivots exactly over Q, and verify all ten equalities and all twenty-two bounds.

For the smallest of the eight candidates, the full observer support certificate in the fixture has nonzero pairing with at least one of the first six columns. It violates a signed allowance inequality with exact ratio >105/100 (display approximation 1.0508841505091693). This excludes that candidate throughout L>=10^114, whereas every exact annihilator direction tested failed to exclude it.

For the remaining seven candidates, the exact rational certificates satisfy T(p/q-r0,h/q-u)=m+Uz and max_i|z_i|<0.88. The respective interior slack values (display approximations in increasing denominator order) are 0.12007469491245361, 0.2580928329939997, 0.37140987717230844, 0.46066463623107207, 0.5365776695055136, 0.6019324082920657, 0.6587883667064416. The standalone verifier asserts each slack >12/100 exactly. Thus no linear observer support inequality of this *same affine outer zonotope* can separate these seven points, even with zero parameter allowance. This is a precise information bottleneck for this model, not a certificate of nonlinear spectral feasibility, true BRC coefficient feasibility, joint realizability of independent error axes, or actual integer anomalies.

## 5. Conditional arithmetic improvement

For L>=10^114, under inherited Stage46 and existing certificates, every relevant genuine anomaly pair has b-a>=q>=
1165623432270214220404883113745300873367119564109373807481147732125067
(approximately 1.16562343227e69). The previous strict bound q>10^69 is improved. The first unexcluded dyadic three-anomaly window remains 8.461516400515182e132 (j=415 in 10^8*2^j). The close-pair first unexcluded window doubles from 1.109067877648326e138 to 2.218135755296652e138 (j=433), using q<=sqrt(L). Exact threshold:
2218135755296651887662731347314466962749149660300653260136383664491697046244500498431979524883311662477912968769122857463179326259200000000.
Consecutive integer endpoint unchanged at about 4.72478e43. Unbounded strict separation and B_fix,odd(32) remain open.

## 6. Reproduction and verification

The compact input and independent standard-library verifier are stored together in research_notes/portable_direct/prefix1141/:
- fixture1141.json, immutable commit fd5b29757feda778fdc120f85ecb32c1b67cb847, blob 053df074dea0a6f671c2434a0151fa4097032be4, SHA256 cb38649b5a98a767b9658c9792af8d21f66b1c2f9290d1e7160b6cc602b6481a.
- verify1141_compact.py, immutable commit 9514c30135e1d76bdb5581e2b4d1fccdaf491f3f, blob cc1b540240802a06d0f38fbef4bf03096c253030, SHA256 6d4fd9150f1e86f6a8aa6d3902b036d3094019c0031b68a46f272edd522fd55b.
Both were read back byte-for-byte. Download both into one directory and run python verify1141_compact.py. Actual execution completed with PASS: outward grid complete enumeration and exact full-observer certificates. The full execution evidence includes predecessor archive contents, extend1141.py, quotient1141.py, fiber1141.py, verify1141.py and compact verifier, their outputs and logs. Exact rational computations decide assertions; floating values are printed only for readability in the verifier.

## 7. Next question

Do not repeat the annihilator search on unchanged ten-observer inputs. Seven points have explicit interior witnesses even for the full affine outer model. Inspect the free-coordinate slack and original error axes, then use additional independent moment observations or tighter point-conditioned nonlinear/anchor constraints to exclude the smallest surviving candidate. A nonlinear shared-coefficient feasibility test involving d is another useful route, with the outer-model versus actual-coefficient distinction preserved. No formal task closure or independent review is asserted.

## 8. Operational provenance

Global governance immutable main c1b0e6c5cf46c81f30f99feff3104177583d54cf. Original own registration request r6-20261123-2358-session-start-own-v1 succeeded; managed session metadata recovered and nonrevoked. LEASED inventory request r6-20261128-0346-owner-read succeeded, fixed observation 2026-11-28 03:47:36.590644+08, Source dc4440436ec5f786af0c2a3eeb9359d10858bb53: 547 tasks, LEASED result empty, cursor null. This is a fixed observation, not live write authority. Independent direct work; no CLAIM or shared execution state change. Activity association is separate from mathematical review.
