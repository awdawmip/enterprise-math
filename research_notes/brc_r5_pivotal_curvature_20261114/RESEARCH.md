# Frozen R5: exact cut pivotality and curvature transition

**Research status:** author-side proof and exact finite calculation, NOT_REVIEWED. **Science pin:** awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. **Previous frontier:** Draft PR #2349 (all gap closures and interval optimization), Draft PR #2353 (the complete 2^28 center-count distribution), scientific head ba53c76f26fb03ee1ffc50de2b4bf77e3ab4e0f6. All assertions below concern only the derived one-dimensional integer-event radius-2 observer, not the native six-axis model or the 2,520-byte certificate performance experiment.

## Model and main result

The 15 frozen integer atoms generate 953 rational activation thresholds, 954 integer cumulative-event boundaries (total 1,065 events), and 29 consecutive blocks separated by 28 original gaps of length 3. Number the gaps 0,...,27. A subset C of these gaps is closed by shrinking its members from length 3 to 2. Let D(C) be the *minimum cardinality* of a set of centers selected from the resulting boundary coordinates covering all coordinates at distance at most 2.

For a uniformly random subset C of the *other* 27 cuts, let I_i = Pr[D(C)-D(C∪{i})=1]. The exact pivotal probabilities are:

| Gap i | I_i |
| ---: | ---: |
| 2, 3, 4 | 3/16 each |
| 5 | 7/16 |
| 6 | 9/16 |
| 8 | 17/32 |
| 9 | 15/32 |
| 10, 11 | 3/32 each |
| 12 | 19/32 |
| 13 | 13/32 |
| **16** | **1** |
| 25, 26, 27 | 1/4 each |
| 0, 1, 7, 14, 15, 17–24 | 0 |

Thus cut 16 is **pivotal in every one of the 134,217,728 configurations of other cuts**, and 13 cuts are never pivotal. The sum of the 28 probabilities is 11/2. A cut that is ineffective when closed alone may be pivotal after other cuts close.

Let F(p) = E[D(C)] when each of the 28 cuts independently closes with probability p. Then:

- F(0)=213; F(1/2)=13471/64; F(1)=207;
- F'(0)=-5; F'(1/2)=-11/2; F'(1)=-9;
- F''(0)=2 and F''(1/2)=-29/8.

By continuity of this finite polynomial, **F has a change in curvature** and is neither globally convex nor globally concave. There exists at least one zero of F'' strictly between 0 and 1/2; uniqueness is not asserted.

For all 378 distinct pairs of cuts, the averaged pair interaction is zero in 350 cases, positive in 11, and negative in 17. Particularly strong interactions: (5,6)=+7/8; (8,9)=+15/16 (redundant improvements); (12,13)=-13/16; and (25,26)=(25,27)=(26,27)=-1/2 (complementary improvements). The entire 28-cut pivotal count array and all 28 nonzero interactions are in EXACT_R5_PIVOTAL_CURVATURE.json.

## Theorem 1: a single length-3-to-2 gap closure improves D by only 0 or 1

For any strictly increasing integer point sequence with candidate centers restricted to point coordinates and radius 2, closing one designated gap from 3 to 2 while keeping other gaps fixed satisfies

0 ≤ D_open - D_closed ≤ 1.

**Proof.** Closing the gap shifts all points on one side one step towards the other side. Within-side distances remain unchanged and cross-gap distances cannot increase. Thus every old center-index set remains feasible, proving D_closed≤D_open.

Conversely take a minimum cover of the closed configuration and name the two points flanking the gap a,b=a+2. A cross-gap center can cover a point on the opposite side only for the exact boundary pair a,b: all other cross-gap pairs are separated by at least 3. After reopening the gap, the only potentially lost coverage is coverage of a by center b or of b by center a. If both a and b are centers, self-coverage ensures neither is lost; otherwise at most one boundary point can lose its covering relation. Adding that point as a center restores the cover. Therefore D_open≤D_closed+1. QED.

Theorem 1 makes the sum of all paired differences an *integer count of pivotal configurations*, not merely an expected decrease.

## Theorem 2: a finite interval first-moment transfer computes all pivotal counts

Write B=29 and let d(a,b) be the exact minimum number of centers in the **fully merged interval** consisting of original blocks a,...,b. Define S(a,b) to be the sum of D over all 2^(b-a) patterns of internal cut closure on that interval. For a≤b:

S(a,b) = Σ_(j=a)^b [ d(a,j) · 2^max(0,b-j-1) + 1_(j<b) S(j+1,b) ].

**Proof.** Any closure configuration has a unique *first maximal merged interval* [a,j]. If j<b, the following cut is open (length 3), and the remaining b-j-1 cuts may vary freely. There is no radius-2 coverage across an open cut, so the center count is d(a,j)+D(remainder). For j=b the remainder is empty. Summing all such unique decompositions gives the recurrence. QED.

Let T=S(0,B-1), and let A_i be the sum of D over the 2^(B-2) configurations with gap i forced **open**. Independence of the left and right sides of an open cut gives

A_i = 2^(B-i-2) S(0,i) + 2^i S(i+1,B-1).

The sum over configurations with i forced closed is T-A_i. Pairing configurations differing only at i and using Theorem 1 yields the *exact integer pivotal count*

P_i = 2 A_i - T,   I_i = P_i / 2^(B-2).

For the frozen R5 sequence, T=56,501,469,184 and 2^(B-2)=134,217,728. All 28 P_i are computed from the 435 interval costs with integer arithmetic; no enumeration of all 268,435,456 full-scale cut patterns is involved.

## Theorem 3: exact fair-background pair interactions

For i<j, let A_ij be the sum of D over configurations with **both** i and j forced open. Those configurations split into three independent segments [0,i], [i+1,j], [j+1,B-1]. Thus

A_ij = 2^(B-i-3) S(0,i) + 2^(B-j+i-2) S(i+1,j) + 2^(j-1) S(j+1,B-1).

For the same choices of all remaining cuts, define

Δ_ij = D(00) - D(10) - D(01) + D(11),

where 0 denotes open and 1 closed at the two specified cuts. Partition all full configurations into the four cut states, whose D-sums are respectively A_ij, A_j-A_ij, A_i-A_ij, and T-A_i-A_j+A_ij. Hence the fair-background mean is

E[Δ_ij] = [T + 4 A_ij - 2 A_i - 2 A_j] / 2^(B-3).

Positive effects indicate redundant benefit of closing both gaps; negative effects indicate complementarity. Both signs occur, so the set-function D is neither globally submodular nor globally supermodular for this finite instance.

The multilinear Bernoulli closure expectation F(p) satisfies

F'(p) = -Σ_i Pr_p[i is pivotal];
F''(p) = 2 Σ_(i<j) E_p[Δ_ij].

At p=1/2, the summed 378 interactions equal -29/16; hence F''(1/2)=-29/8. Independently differentiating the previously saved exact cut-count/center-count polynomial yields the same derivative, F''(0)=2 and F'(0)=-5.

## Verification and precise scope

The self-contained standard-library Python program VERIFY_R5_PIVOTAL_CURVATURE.py reconstructs the frozen atoms using exact fractions, builds the 435 interval costs, calculates every S(a,b), all 28 pivotal counts and 378 pair interactions, and independently checks the derivative identities against the complete closure-count histogram. The authored program was executed, returning PASS_EXACT_R5_PIVOTAL_AND_CURVATURE. A second exhaustive center-subset solver checks 117 small block configurations, 774 closure configurations and 270 pair interactions; direct tests on the full frozen points check 10,612 paired configurations having no more than two other closed gaps. For all 2^28 configurations the conclusion is covered by the exact finite transfer recurrence and the mathematical proof, **not** by brute-force enumeration.

This note does not assert new native X6 semantics, an asymptotic speedup, a formal Task-ID/CLAIM, an admitted Result, or independent review. The uploaded program/JSON need immutable GitHub readback to establish remote publication.

**Next:** compute higher-order cut-coalition effects or the fixed-budget-K nearest-center *total correction cost* over multiple gap closures while retaining explicit center-set witnesses and provenance. A separate native validation remains due for the original 2,520-byte seed / 28-coordinate / 8,192-prefix-query benchmark, including full preprocessing, precision and memory accounting.
