# R284GH — high-omission sharp capacity extends to q >= 4u-1

Date: 2026-11-24 Asia/Shanghai. Author-proved with exact rational branch coverage, NOT independently reviewed. Informed portable TASK_RESEARCH. Same frozen four-phase fixed binary tag model and sources as R284GG. P000 unchanged; no formal CLAIM.

## Main result

For all integers u>=1 and q>=4u-1,

    n_min(q,u)=4q+8u+2.

This strengthens the R284GG threshold q>=4u+1 by two full integer omission layers, for every u. In particular q=7,u=2 requires 46 bits; q=11,u=3 requires 70; q=15,u=4 requires 94. The existing all-q>=2 result for u=1 remains separate.

## 1. Exact two-heavy necessity on the larger domain

Reuse the identical six disjunctions, source-incidence definitions, width inequality and three nonheavy cases from R284GG. Replace only q>=4u+1 by q>=4u-1. The new real relaxation still has no solution.

Adaptive branching on the six disjunctions generated 165,167,165 exact Farkas leaves for nonheavy pairs (3,5),(3,6),(5,6), respectively, total 497. All multipliers were checked using exact Fraction arithmetic; all children of every selected disjunction were covered. The new certificate data has 39353 uncompressed bytes and SHA256 d07f329fad0c969b0fa5622f27056cf67eee8637601b71b2e1d2e79315bd603f. The locally executed generator and checker returned these three counts. The packaged standard-library verifier reuses the R284GG source and branch checker; its embedded data is identical to the local certificate data and its immutable source was separately read back. Neither q nor u has an upper cutoff.

Thus any hypothetical correct histogram of total <=4q+8u+1 has at least two types in {3,5,6} with x_p>=2q+2u. This is the exact same conclusion as R284GG under the weaker q condition.

## 2. Extend the R284GF obstruction

Write n=4q+k with k<=8u+1, using nonconstant width after harmless removal of constants. Let two heavy sizes be 2q+a,2q+b, with a,b>=2u, and let R=k-a-b be the total residual mass outside them. Hence R<=4u+1 and R-q<=2.

For any collection of disjoint residual groups of total size M, their total overflow beyond q is at most (M-q)_+. This follows because either no group overflows or the overflowing groups subtract at least one q. Use the exact R284GE requirement sum_e (N_e-q)_+ >= q+4u+1.

Case {3,6}. On edges 0 and 1 exactly one of the chosen heavy types changes, and its last-change group is a singleton. Other groups have total mass <=R. Their overflow is at most 2. Consequently a,b>=4u-1, hence R<=3<=q. With no residual group overflow the same edge constraints now imply a,b>=4u+1. This contradicts a+b+R<=8u+1.

Cases {3,5} and {5,6}. Use a for the nonalternating heavy offset and b for alternating type 5. On the two edges on which only the alternating heavy changes, its source group includes distinct residual types r_1,r_2 (types 1 and 4 for {3,5}; types 2 and 7 for {5,6}). Here r_i denotes the multiplicity, not the type label. The remaining changing groups have total mass <=R-r_i. Therefore GE implies, for each i,

    b + max(r_i,R-q) >= 4u+1.

Indeed the heavy group contributes q+b+r_i and the rest at most (R-r_i-q)_+.

First prove b>=2u+1. If b<=4u-2, then 4u+1-b>=3>R-q, so both r_i>=4u+1-b. Since they are distinct residual types, R>=2(4u+1-b). Thus k>=a+8u+2-b, giving b>=a+1>=2u+1. If b>=4u-1, the conclusion follows directly because u>=1.

We now have R<=4u and R-q<=1. Consider opposite phases (0,2), which differ in the nonalternating heavy type but agree in type 5. Its differing mass is at most 2q+k-b <=2q+6u <=3q+2u+1. A four-vertex cut is impossible. If a=2u, no two-vertex cut can work: the chosen nonalternating heavy size is exactly 2q+2u and any residual type has mass <=4u<2q+2u+1. The only possible separating cut is then a three-vertex cut with sum >=3q+2u+1, which forces equality in the previous chain. In particular q=4u-1, k=8u+1, b=2u+1, R=4u. The two r_i inequalities force both distinct residual types to have mass >=2u, because R-q<=1<2u. A three-vertex cut contains just two incident types. To reach the threshold it must include the nonalternating heavy (residual mass alone is too small), and it must include all residual mass in the one remaining type. This contradicts the two distinct positive residual types. Hence a>=2u+1.

Finally b cannot equal 2u+1: then R<=4u-1<=q, so the two r_i inequalities require r_1+r_2>=4u>R. We conclude b>=2u+2 and R<=4u-2<=q.

The R284GF diagonal-prefix witness applies: choose the edge on which both heavy types change (0->1 for {3,5}, 1->2 for {5,6}). Their four phase projections are all distinct binary pairs. The positive thresholds are

    T_a=a+R-2u=k-b-2u <=4u-1,
    T_b=b+R-2u=k-a-2u <=4u.

Thus both lie in [1,q+1], with q>=R. Along any attempted order, the first heavy threshold reached produces the forbidden third-phase read by the exact R284GF source-slot witness. All two-heavy cases are excluded. This proves the strict width lower bound at q>=4u-1. The matching R284FE two-group Gray construction has width 4q+8u+2, completing the theorem.

## 3. New frontier

At q>=4u-2 the same real-relaxation search (not an exact integer counterexample search) found feasible nonheavy solutions; for example u=3/2, q=4 and (x1,...,x7)=(0,0,10,0,9,10,0) in the (3,6) nonheavy branch, with n=29. These values satisfy the real-relaxed width, thresholds, and six disjunctions, but u is not an integer. This marks a failure of that real relaxation rather than a counterexample to physical capacity. Next: inspect integer-only branches at q=4u-2 and improve the diagonal witness or find exact physical nonheavy examples. Do not assume the threshold is sharp.

## Sources and evidence

- R284GG theorem: 32c7e5c164557424558fc6128503d17e232e7dad:research_notes/portable_direct/R284GG_ALL_U_HIGH_OMISSION_SHARP_CAPACITY_20261124.md
- R284GG complete certificate checker: 1d92030a09b96f41661247bc2bae837ed8ff1899:research_notes/portable_direct/R284GG_exact_general_u_certificate.py
- R284GH new complete certificate data: 837120a0cdaa2b0a683ff49e936b0671d395f589:research_notes/portable_direct/R284GH_q4u_minus1_certificate.py; run beside the pinned GG checker, with assertions enabled.
- R284GE exact no-rollback; R284GF diagonal-prefix lemma; R284FE constructive upper bound: immutable refs as listed in GG. These are auxiliary Boolean residual observer results, not a native geometric claim or change to P000.
