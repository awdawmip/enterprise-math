# S23/AV exact saturation plateau N(71)=...=N(79)=439, N(80)=443

Date 2026-11-07; Status AUTHOR_SIDE_FINITE_EXACT_PROOF, independent review pending. Same frozen source and experiment as PROOF.md at ea1f338cdda0b1d183465d42e3a16cef5e068987.

**Theorem.** For the exact minimal future-sign observer defined in PROOF.md,

    N(h)=439 for every integer h in {71,72,...,79},
    N(80)=443.

The already established h=71 proof gave the strict lower bound N(71)>=439, since no prefix likelihood of length <=438 lies in (10^60/7^71,1). The future threshold sets T_h are nested: if h1<=h2 then T_h1 is a subset of T_h2. Thus achieving full interval occupancy for h2 implies full occupancy for every h1<=h2, giving N(h1)<=N(h2). A prefix can be padded by label 3 without changing its likelihood, so N(h) is well-defined and the saturation persists.

For the plateau upper bound, the companion VERIFY_PLATEAU.py exhaustively enumerates all M_79=binom(81,2)=3240 distinct rational thresholds and every nontrivial count-state (k,ell) with k+ell<=439. Exact Fraction comparisons show all 3241 open intervals occupied, i.e. N(79)<=439. Combining with monotonicity and N(71)>=439 gives N(h)=439 for all integers 71..79.

At h=80, the threshold set has M_80=binom(82,2)=3321 distinct points. Exact Fraction enumeration at prefix length 442 yields precisely one empty open interval, whose bounding thresholds come from suffix-count pairs (i,j)=(0,67) and (11,69): (7^-67, 10^11/7^80). At prefix length 443 all 3322 open intervals are occupied. Therefore N(80)>442 and N(80)<=443, yielding N(80)=443.

The exact verifier uses Python integers and fractions.Fraction, no floating-point comparisons; the complete executed stdout is RUN_PLATEAU.txt. These are exact finite results in the fixed lawful two-point auxiliary experiment, not the original minimax reconstruction or the six-source mother model. They add a ten-horizon structural plateau and a fresh jump at 80 to the already proved first deviation at h=71.

**Next:** identify the continued-fraction/rational-gap mechanism behind these plateaux and find a general exact or bounded formula for N(h). The full-lawful delta4 and source/time-aware mother bridge remain independent open research units.
