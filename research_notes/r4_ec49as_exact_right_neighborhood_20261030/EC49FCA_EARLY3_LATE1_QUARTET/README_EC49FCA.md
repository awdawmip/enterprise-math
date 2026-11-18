# EC49FCA — Exact three-early/one-late four-slot rigidity of the 158-edge signed-X6 witness

2026-11-06; author-side exact finite result, pending independent Driver mathematical review.

## Statement and frozen inputs
Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Reuse the original nine-state DFA, BRC full positive cache keys and native signed six-axis primitive-prefix expansion from EC49FBY `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`. The explicit 158-edge 24-word witness is EC49FBU `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`. Fix H2/H3 paths `fe,ge,feg,gef`. H4/H5 use `L=(4,2,1,0,0,0)`; H6–H9 use `M=(7,3,2,0,0,0)`.

Each of the ten early H4–H6 positions and ten later H7–H9 positions has a fixed horizon and required terminal observation signature. For any one of the `C(10,3)·10=1200` groups comprising exactly three early positions and one later position, replace those four words by arbitrary valid words matching their exact individual horizon, cache key and DFA signature, leaving all other twenty witness words fixed.

**Theorem (finite restricted exact optimum).** Each of these 1200 groups has optimal signed primitive-prefix-union cost **158**. The pinned witness attains the value.

## Proof and exhaustive computer certificate
For each slot set I, let R be the set of signed primitive prefixes supplied by the twenty unchanged paths. Let K=158−|R|, and for any candidate w set D(w)=B(w)\R, where B(w) comprises every nonempty prefix of the full native signed-axis expansion. A strict improvement requires `|D(w1) ∪ D(w2) ∪ D(w3) ∪ D(w4)| < K`. Hence a candidate whose residual has >=K elements, a pair already having >=K in its union, or a triple already having >=K, cannot participate in a strict improvement. Duplicate residual sets may be collapsed exactly, since the objective depends only on their union. The supplied finite verifier exhausts every remaining fourth candidate; none improves 158. Thus the pinned 158-edge witness is optimal in each stated four-exchange family.

The frozen EC49FBY generator exhaustively enumerates the finite positive BRC multiplicity solutions and the nine-state DFA terminal signatures. Exact native X6 primitive-prefix information and path order are preserved. This is a restricted local statement for the specified cache-key schedule and fixed twenty words.

## Executed results and independent crosscheck
Two standard-library Python implementations ran over all 1200 families on 2026-11-06: integer bitsets for exact prefix unions and a separate implementation using plain sets of tuples of signed primitive steps. Results agreed **for every group**, including the fourth-candidate evaluation count and optimum.

- 1200 families; each optimum 158; zero improvements.
- 12,617,337,600 raw candidate quadruples across all groups.
- 246,160,070 Cartesian products of individually eligible distinct residual masks (before pair/triple pruning).
- 23,658 filtered pairs and 200,924 filtered triples excluded by monotonic bound.
- 1,306,868 exact fourth-candidate unions evaluated.

`SUMMARY_EC49FCA.json` records totals. Run `python3 EC49FCA_EARLY3_LATE1_QUARTET/VERIFY_EC49FCA.py` to generate the full 1200-group `EXACT_REPORT_EC49FCA.json`, and `python3 EC49FCA_EARLY3_LATE1_QUARTET/VERIFY_DIRECT_EC49FCA.py` for the independently represented signed-prefix cost. Both import the immutable scientific generator from sibling EC49FBY, and require Python standard library only.

## Next question
The four-slot domain has `C(20,4)=4845` groups: 210 all-early (EC49FBZ), 1200 three-early/one-late (this work), and **3435** with two or fewer early positions. Continue exact search among these 3435 families, and evaluate alternative cache-key schedules against the mother nine-window objective. Favor exact lower-bound certificates, prefix residual dominance and 157-edge witnesses if found.

Author-side GitHub publication does not change formal CLAIM, Result/Review or P000; those follow current Source controls.
