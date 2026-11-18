# EC49DL — uniform native-X6/BRC saturation of nonzero return fibre +2E1

Date 2026-11-01. Status **PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**. Independent mathematical review and native Research-Activity/Result admission remain pending. This study concerns the exact positive-BRC path observer, not physical dynamics, signed interference, or a three-dimensional slice.

## Fixed inputs and exact semantics

GLOBAL_KNOWLEDGE_V1 canonical main 529a3dfc7f127bd262e0b0571696a5ae2735d200 (verified this research run); Enterprise Math canonical main f1e437bcd8fae1135b671780b8f7a64006f7f1ff; previous research frontier PR #1730 head 93f5c20d61f3876923b9d080a6de778876bd8800 (EC49DK). P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc was checked against the global P000 startup projection. ACTIVE worldview unchanged.

All primitive steps are literal ordered signed X6 directions ±E1,...,±E6. The complete prefix endpoint is D=(2,0,0,0,0,0). The future-operation alphabet is a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), where each tuple names an ordered sequence of *primitive signed axis steps*; concatenating operations never erases boundaries relevant to adjacent primitive A/B tags. Ordered labels A=(+E1,+E2), B=(+E2,+E1) are evaluated across the entire prefix+future concatenation, including the seam. Joint tags 0=neither, 1=B only, 2=A only, 3=both. For each future word of exactly h operations, or collectively depths 1..h, keep only suffixes with displacement -D. One output coordinate is provided for each suffix, final tag and instrument (Wx,Wy,count). The two strictly positive BRC channels multiply weights x_i,y_i for positive +Ei primitives, and weight 1 for negative steps; count is 1 per literal path. Compare all prefix rows by exact linear rank over Q for rational parameters, and over R for real parameters. No Boolean support/count interchange occurs.

Reference weights: x=(2,3,1,2,3,4), y=(5,7,3,5,7,9)=2x+1. The theorem actually covers *all* positive affine parameters

    x_i>0, alpha>0, beta>0, y_i=alpha*x_i+beta, x_1 != x_2.

There is no assumption restricting the other four weights. All signed-X6 paths remain valid despite the certificate's use of only the first two axes. This is not a claim of a native two-dimensional plane.

## Theorem: exact local saturation and minimality for any horizon

For every finite integer h>=2, with the *same* prefix length n=8 and endpoint D=2E1:

    rank O_{=h} = 15  if h is even;
    rank O_{=h} = 18  if h is odd;
    rank O_{1..h} = 18 for either parity.

For this whole affine-positive stratum, 8 is the *earliest even primitive prefix length* that attains the displayed relevant full rank, separately for each exact-depth and cumulative observer. These are LOCAL fibre statements, not global n_sat(h) across all displacement fibres.

### Upper bounds by explicit future histories

For prefix p, let F00,F01,F10,F11 indicate its complete own A/B label. Let pA be the indicator of "no A in p, and p ends +E1"; pB similarly "no B in p, and p ends +E2". Each whole future operation ends negative. Thus there are no adjacent A/B seams across two future operations. The one prefix/future seam can create A only when the first future operation is d and p ends +E1, or B only when it is c and p ends +E2. Hence every future final-tag indicator factors through (F00,F01,F10,F11,pA,pB). Since returning suffix weights multiply the prefix instruments by suffix-specific constants, rank<=6*3=18 for every h and both languages.

For D=+2E1, future-return condition requires #a=#e+1 and #b=0. If h is even, #c+#d is strictly positive and odd; every suffix then internally contains at least one A or B. The final tag factors through five functions (1, noB=F00+F10, noA=F00+F01, pA,pB), so rank<=5*3=15 for exact even h. Odd exact h and cumulative h have rank<=18.

### Literal 18-path, six-history construction

The included EC49DL_WITNESS.json lists 18 distinct, complete length-eight primitive signed X6 paths whose actual endpoints all equal (2,0,0,0,0,0). They are not abstract history placeholders. Six successive blocks of three paths realize history columns

    H0 = F00       H1 = F01      H2 = F10
    H3 = F11       H4 = F00+pA   H5 = F00+pB.

Within each block the number of positive +E1 steps is k=2,3,4 (and positive +E2 steps are 5-k). All 18 rows therefore have instrument triples

    T_k = (x1^k*x2^(5-k), y1^k*y2^(5-k), 1),  k=2,3,4.

The exact three-row determinant is

    det(T2,T3,T4)
      = x1^2*x2*y1^2*y2*(y1*x2-x1*y2)*(x2-x1)*(y2-y1)
      = alpha*beta*x1^2*x2*y1^2*y2*(x2-x1)^3.

The last expression is nonzero for *every* parameter in the declared positive stratum, proving six independent BRC/count directions, three in each of six independent ordered-history blocks. At the reference parameter this determinant is +4200.

Returning h=2 operation words are precisely ac,ad,ca,da; the full future label map on the six history features has rank five. The exact h=3 suffixes include aae,aea,eaa, and the label map has rank six. The cumulative 1..2 language adds a, and its label map has rank six. All three maps have explicit selected suffix/tag coordinates in EC49DL_WITNESS.json, where each label block is multiplied by the three separate instruments. By block-factorization and the nonzero determinant above, the selected integer observer minors achieve respectively 15,18,18. The frozen checker actually recomputes all full concatenations and exact Bareiss determinants (not a simulated semantic label placement).

For the reference integer parameters the complete selected minors are:

    exact h=2 (15x15): +533756191302432000000000000000
    exact h=3 (18x18): -86468502990993984000000000000000000000000
    cumulative h=2 (18x18): -242066299910400000000000000.

All are nonzero, and their precise row/column definitions are in the JSON witness.

### Universal h lift

The complete two-operation suffix ae has zero displacement, begins negative and ends negative, and introduces no new A or B. For any selected returning suffix w, w(ae)^k preserves its final tag on *every* prefix and preserves total displacement; its three BRC/count coordinates are multiplied respectively by x1^(2k), y1^(2k), 1. Thus each three-instrument determinant block scales by (x1^2*y1^2)^k. The selected even base minor contains five blocks and the odd base contains six. Therefore

    det_even(2+2k) = (x1^2*y1^2)^(5k) * det_even(2);
    det_odd(3+2k) = (x1^2*y1^2)^(6k) * det_odd(3).

These nonzero identities hold for *all* integer k>=0, not merely tested finite windows. Every cumulative 1..h observer with h>=2 contains the original cumulative 1..2 coordinate family; hence it retains rank 18.

### Parameter-uniform obstruction before n=8

A prefix with full endpoint D=2E1 must have even primitive length. Let n=2(m+1). Exactly m primitive negative steps have multiset N; the positive multiset equals N plus two +E1 steps. This parametrizes *all* possible paths of the fibre without omitted words.

At n=6, m=2. Split all literal paths according to whether N includes E2. If it does, N={E2,Ej}; the three-instrument row scalar triple is (x1^2*x2*xj, y1^2*y2*yj,1), which lies in one common at-most-two-dimensional affine-weight subspace as j varies, since yj=alpha*xj+beta. Across at most six possible history features, this part has rank<=12. If N excludes E2, there is no positive +E2 and therefore no internal A/B; its history is in span(F00,pA). Modulo the same two-dimensional instrument subspace, these paths contribute <=2 further directions. Thus the *entire* full six-feature instrument matrix at n=6 has rank<=14 for all parameters in the stated affine family, independent of the other four weights. At n=4, m=1, if N=E2 one fixed instrument triple times at most six history features contributes <=6; for N!=E2 the history is in span(F00,pA) and the affine instrument variation spans at most two directions, contributing <=4; hence n=4 rank<=10. At n=2 there is exactly one possible path (+E1,+E1); at n=0 no such endpoint exists. Odd prefix lengths have no such endpoint. Therefore n<8 cannot attain either 15 or 18. This proof extends the early-shortening obstruction to *all* strictly positive affine x1!=x2 parameters, rather than inferring it from a single numerically tested weight point.

## Executed exact reproducibility

The independent standard-library checker VERIFY_EC49DL.py reads EC49DL_WITNESS.json, rebuilds each primitive prefix and suffix, computes all six signed displacement fields, A/B including seam, every positive X/Y product and count. Its exact fraction-free integer determinants have nonzero residues modulo both 1000003 and 1000033. It enumerates all 1+64+4665=4730 prefix words at lengths 2,4,6 (rank over Python fractions.Fraction equals respectively 1,8,14 at the reference weight), cross-checks whole-fibre BRC aggregate weights and multiplicities against the reused exact original native_signed_brc.py kernel, and rebuilds extended matrices for h=2..9 with exact determinant scaling. Actual result: PASS; source values captured in EC49DL_EXECUTED.json. Finite tests validate implementation and local short-length exhaustive coverage; universal h and parameter claims follow from the algebraic arguments above.

The checker and witness are independently recomputable without previous full checkout. The native kernel is copied unchanged from EC49DK's prior original evidence, used here only for independent aggregate cross-check. The prior provenance is retained rather than treating source reuse as mathematical novelty.

## Scope, authority and next work

This is an author-side constructive proof and finite exact check of the declared observer. The only canonical mathematical claim is the *conditional mathematical proposition stated here*, not a formal Enterprise Math Result, Driver-reviewed theorem, physical event evolution, or GLOBAL_KNOWLEDGE-worldview change. Native status and active owner have not been confirmed by a live native Source receipt in this portable run; no CLAIM/review/admission is asserted.

Next EC49DM: take the different displacement D=+2E2 with its own ordered seam asymmetry and derive a local saturation/obstruction, and separately classify the x1=x2 exceptional affine stratum at D=+2E1. Reuse these six-feature/BRC tools without importing symmetry that the five actual future operations do not possess.

