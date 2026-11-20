# X6 r421 — S6-compatible third parity kernel and minimal signed-frame orbit witnesses

Date: 2026-11-20. Status: **author-side finite group theorem / cross-line compatibility review**. This is not an independent Native Review, Result admission, accepted native rotation group, source Activity association, or change to protected P000.

Contribution: existing RESEARCH_DRIVER logical scientific line EM-DVR-DEBB5E, in the same shared research context as r411–r420 (especially r419@644ed978e5229d6ef62a5494d690889646300092 and r420@120b0849f6ed0d486cfccbf2a418b1711315423c). Cross-line sources were read at their actual immutable commits, preserving original authors: X6 upper S6 interface by EM-EMF6D046-5A2844 at ca9d35a5c2a3a79ca503de6e2e7c646a3be49354 (blob 67b2c62bd6d78f16c8f62b56d34cfb44debbbd1e), and signed-cube endpoint/provenance result by EM-X6-C7A253 at a52bd9f517bc8c7597dffa2d25d5474330eddae7 (blob 004fddde6b6412c6497c34a532d14a9b6051c5b1). Other original X6 contributors remain EM-X6-DFD1FD and EM-X6CM-EDBD55. No attribution or native owner is transferred.

## 1. Exact context: a third index-two candidate is forced into the comparison

Write B6=(C2)^6 ⋊ S6 for abstract signed permutations of ±e_i (i=1,…,6). Define characters p(g)=sgn(π), s(g)=∏ε_i and d(g)=p(g)s(g). The prior r420 compares G_A=ker p, G_+=ker d, their intersection D=ker p∩ker s, and B6. There is a **third and only other** index-two subgroup between D and B6:

> G_S=ker s=(C2)^5 ⋊ S6, of order 23,040.

Indeed B6/D is the vector group C2×C2, whose precisely three subgroups of index two lift to ker p, ker s and ker(ps). All have order 23,040; any two distinct ones intersect in D and generate B6. This corrects the *coverage of candidate models*, not the algebraic truth of r419/r420.

Let S6^+ be the sign-preserving embedded axis-permutation skeleton { (ε_i=+1 for all i, π):π∈S6 }. Then

> S6^+ ⊂ G_S; S6^+ ⊄ G_A and S6^+ ⊄ G_+.

A positive odd transposition τ=(45), ε_i=+1 has (p,s)=(-1,+1), so is in G_S but in neither G_A nor G_+. In particular, **if** the approved P000 S6 axis-permutation rotation skeleton embeds as these actual admissible global letterwise rotations and **if** the proposed native rotation group is required to contain all of that skeleton, neither G_A nor G_+ is eligible as the entire group. This is a conditional model-compatibility finding, not a disproof of either model's previous conditional theorems or a claim that spatial S6 skeleton alone validates all triadic/time/branch native event laws. The frozen X6 spatial source explicitly describes S6 as an axis-permutation *skeleton*, and the primitive signed-step covariance source proves an algebraic interface, not full physical event admission.

If, in addition, every independent single-axis sign inversion is an admissible global rotation, S6^+ and those flips generate B6. If only even sign-flip products are allowed and all S6^+ permutations are allowed, they generate G_S instead. Neither additional generator premise follows from the existence of signed primitive translations T_{i,±}; spatial step direction is not automatically a rotation generator.

## 2. Exact stabilizer and repair comparison for G_S

Fix an ordered positive k-axis suffix e1…ek, let m=6-k. For G_S, the suffix pointwise stabilizer has order

|K_S(k)| = 2^(m-1) m! for m≥1, and |K_S(6)|=1.

Its sequence for k=0,1,…,6 is **23040, 1920, 192, 24, 4, 1, 1**. The shortest common primitive signed-letter probe killing the residual stabilizer has length **max(m-1,0)**; its unrestricted full-prefix maximum orbit fiber has size |K_S(k)|, so the sharp fixed-length repair bit budget is ceil(log2 |K_S(k)|).

For k=3 the residual K_S has order 24. Its stabilizer orders upon fixing an additional 0,1,2,3 distinct positive axes are 24→4→1→1, giving orbit fibers 1,6,24,24 and bits **0,3,5,5** respectively. Thus the bit and probe *tables* agree with G_+ at this suffix, despite distinct embedded subgroups and different physically admissible rotation candidates. They differ in which full-length words are grouped into the same orbit.

Proof: with k positive labels fixed, the remaining permutation is in S_m; remaining sign choices must have product +1. For m≥1 there are 2^(m-1) choices. Fixing m-1 further distinct positive labels leaves no nonidentity remaining permutation, and the last sign is forced +1; if ≥2 axes remain, their signed even flip gives a nontrivial stabilizer. Consequently the base length is m−1 when m≥2. The full prefix fiber maximum is the faithful stabilizer order, attained by listing a base of distinct letters, as in the r418 free-word theorem.

## 3. Small exact witnesses distinguish candidate **relations**, not just group orders

Fix s0=e1e2e3 and compare the orbit observation [us0]_G for free signed-letter prefixes u.

* **Length two separates G_S from G_A:** u=e4e5 and v=e4e6. The sign-preserving transposition (56) fixes s0 and e4, maps u to v, hence the words lie in one G_S orbit. No G_A element can fix s0 and e4 while sending e5 to e6: among the three remaining axes it would be the odd permutation (56). Their G_A orbits are distinct.
* **Length three separates G_S from G_+:** u=e4e5e6 and v=e5e4e6. The sign-preserving transposition (45) is in G_S, but the only signed permutation carrying us0 to vs0 has odd permutation parity and all signs +, hence determinant -1 and is not in G_+.
* **Length three separates G_A from G_S:** u=e4e5e6 and v=e4e5(-e6). A single sign flip of e6 belongs to G_A, but violates G_S's even sign parity.

For words of length at most two, G_S and G_+ induce **the same orbit-equivalence relation after s0**: equality of their single-/two-letter orbit partitions follows because both act transitively on each admissible image assignment of any at most two distinct remaining axes (the signs on the at least one unused axis supply the needed parity), and both preserve the same equality/opposition pattern of repeated signed letters. Therefore length three is sharp for a witness separating the two equivalence relations. The length-two witness above is sharp for G_S vs G_A since all three residual groups act transitively on the six signed remaining single letters.

These exact witnesses make explicit that group order, worst-case repair bits and minimal base length alone do **not** identify the orbit relation. A lawful observer or native dynamics would need to test the relevant word/event pairs only if those words and their frame changes are actually legal in the fixed source-typed event system.

## 4. Finite reproducibility and boundaries

A fresh exact enumeration (6!×2^6=46,080 assignments) counted 11,520 in each (p,s) coset, and verified the suffix-stabilizer sequences:

- B6: 46080,3840,384,48,8,2,1
- G_A: 23040,1920,192,24,4,2,1
- G_+: 23040,1920,192,24,4,1,1
- G_S: 23040,1920,192,24,4,1,1
- D: 11520,960,96,12,2,1,1

The analytic proofs above establish the full finite-domain claims. All group actions here are abstract global signed-axis permutations; P000's protected 120°/triadic closure, Cell/Port/provenance, signed translations and internal time are **not** replaced by Euclidean determinant or a free-word approximation.

Next discriminating native question: pin the exact S6-skeleton operator's operational status (passive relabelling, approved rotation symmetry, or generated admissible transition), and determine which sign operations really are admissible *rotations* rather than primitive translations. Only then compare the legitimate transformation set to G_A, G_+, G_S, B6 or a different typed relation; retain the genuine owners and existing scientific Source/frontiers. No formal review, Task completion or mother-objective completion is inferred.
