# R5: a new one-bridge, exact 14-edge Blackwell chart transverse to the saturated Phi face

Date: 2026-11-09 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Research input, provenance, and relation to the mother objective

Frozen model: seven LR nodes with r=(1/10,1/2,3/4,1,5/4,3/2,19/10), source FULL_HIST, target seedless F, g=b. Immutable source evidence:
- PR #1859 (mass map, physical constraints, 21 Blackwell equations, the saturated dual Phi and 17-edge face), f63a0250714f2445e8b406754b85f26d983ec3a6.
- PR #1861 (full fixed-marginal polytope, unique maximal atlas-escape vertex), 54f4abcb13b7453a29e66ed3421cbafa017e9e27.
- PR #1866 (fiber geometry), 7a2c8c48873499a3c998d5587ff9dbf4b32a14c3.
Frozen scientific input pins remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Applicable behavioral rules were read independently. The seven-node mass map is a typed statistical observer, not the native X6 spatial basis.

The mother question is whether every legally feasible g=b physical strategy pair with nonnegative Blackwell transport admits a coupling with <=14 positive edges, or whether a true >=15-edge physical witness exists. This note supplies a new *transverse* exact continuous 14-edge chart, complementing prior charts restricted to Phi=0.

## Theorem: a physically lawful transverse real interval of 14-edge certificates

Fix the previously verified source and target physical flow tuples (g,a,b,u,v,w,z):

    X0=(999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)
    Y =(1,2002911/10904720,26095487/40892700,
         442758619/6542832000,11037627/68154500,
         394502727/2180944000,2002911/109047200).

For each real e define X(e)=X0+e*(0,0,0,0,0,0,1). Set

    H = 17774559/17507527960.

For EVERY real e in [0,H], X(e) is a lawful g=b FULL_HIST source strategy; Y remains a lawful seedless-F target; and their two stopping times agree exactly:

    T_P=T_Q=(17609/6000,33857/12000).

For EVERY real e in [0,H], there is an exact nonnegative Blackwell transport E(e) on the following 14 candidate edges (target index i, source index j), with mass on each listed edge given by A_e+e*D_e:

| (i,j) | A_e | D_e |
|---|---:|---:|
| (0,0) | 33553/432000 | -247/1620 |
| (0,1) | 3997/432000 | 3211/14580 |
| (3,1) | 3997/540000 | -22477/36450 |
| (5,1) | 0 | 3211/8100 |
| (0,2) | 510479933/29442744000 | -247/3645 |
| (2,2) | 2893155797/8178540000 | 494/2025 |
| (3,2) | 6636239129/147213720000 | -3211/18225 |
| (2,3) | 222511289/4089270000 | -494/2025 |
| (3,3) | 318755011/3680343000 | 3211/4050 |
| (4,3) | 222511289/4089270000 | -494/2025 |
| (4,5) | 172449787/1363090000 | 494/2025 |
| (5,5) | 219439/545236000 | -3211/8100 |
| (6,5) | 172449787/2180944000 | 247/1620 |
| (6,6) | 38053/432000 | -247/1620 |

All unlisted edges are identically zero. All 21 exact conditions hold:

    sum_j E(i,j) = mu_i = M(Y)_i,  for each i=0,...,6;
    sum_i E(i,j) = nu_j(e) = M(X(e))_j,  for each j=0,...,6;
    sum_i r_i E(i,j) = r_j nu_j(e),  for each j=0,...,6.

There are exactly 14 strictly positive E entries when 0<e<H, and exactly 13 at e=0 and e=H. At the left endpoint only (5,1) is zero; at the right endpoint only (5,5) is zero.

The interval is maximal FOR THIS SPECIFIED AFFINE TRANSPORT CHART within e>=0, since

    E_(5,5)(e)=219439/545236000 - (3211/8100)e

becomes negative when e>H; H is less than the physical cap 1/120.

## Exact Phi one-edge bridge

Recall the old nonnegative 30-edge dual price Phi whose pairing with the fixed pair was zero:

    Phi(mu,nu)=(23/5)(mu_0-nu_0)+3(mu_1-nu_1)
               +2(mu_2-nu_2)+(mu_3-nu_3).

For this lawful physical family,

    Phi(M(Y),M(X(e))) = (3211/8100)e = E_(5,1)(e).

Exactly ONE of the listed edges has strictly positive Phi price: (5,1) has price +1. Each other listed edge has zero price. Hence the new (5,1) bridge carries the complete departure from the formerly saturated Phi=0 support face. The nonnegative 14-edge chart varies in a genuine marginal-observer direction (Phi>0 for e>0), rather than only along a fixed-statistical-fiber kernel.

The old 16-edge atlas S from PR #1859 also gives an exact, *not optimized over E*, escape mass for this particular chart:

    epsilon_S(E(e)) =
       8555233477/73606860000 - (51623/72900)e.

At e=0 this is the fixed-marginal maximum-gap 13-edge vertex from PR #1861; the escaped mass decreases linearly along the transverse chart. For e=1/1000, one obtains a 14-positive-edge certificate with

    Phi = 3211/8100000,
    epsilon_S = 71744989993/621057881250.

## Proof of the full real interval

1. X(e) retains g=b. All 13 explicit FULL_HIST capacity slacks are affine in e; at e=0 they are nonnegative and at e=H they are nonnegative (verified exactly by the self-contained checker). Thus they hold throughout [0,H] by convexity. Target Y is unchanged and seedless F (g=1,z=a/10); its capacity slacks are nonnegative. Both stopping times are independent of the changed z and already equal at e=0.

2. The source mass map M is affine in the seven physical flow variables. The coupling entries E(e) are affine. Therefore every mass/likelihood-ratio equation above is an affine identity in e. The verifier checks all 21 equations at e=0 and e=H using exact rational arithmetic. Hence all equations hold for every real e in [0,H]. Source/target masses are nonnegative and normalized by their capacity equations.

3. Every table entry is affine in e. It suffices to check nonnegativity at the two endpoints, done by exact rational comparisons in VERIFY.py. The only zero at e=0 is (5,1), and the only zero at e=H is (5,5); all remaining entries are strictly positive at both endpoints. All 14 entries are strictly positive on 0<e<H. Their total count is therefore exactly as stated, for all real e.

4. Direct exact substitution into Phi, with the old edge-price table, gives Phi=(3211/8100)e. On listed edges, the only positive-price edge (5,1) has mass precisely Phi; all other prices vanish. Summing the four selected out-of-atlas edge weights gives the stated affine escape cost.

Each step is a rational identity or linear inequality; no floating-point optimization is needed for the published certificate. SciPy was used only in route discovery, then eliminated from the proof/verification path. The independent checker uses Python stdlib Fraction for both physical boundaries, all transport equations and the selected example.

## Scope and next scientific action

This is a positive-width physically lawful one-parameter transverse chart of 14-edge Blackwell certificates. It extends the collection of verified local constructions towards the all-physical 14-versus-15 objective. It is not a proof of the universal 14-edge bound and supplies no 15-edge necessity witness.

Next: vary one more independent physical-flow parameter while respecting the two time constraints and g=b; solve the exact 14-edge chart equations in two parameters and determine the positivity chamber, or discover a new bridge edge when the current (5,5) bound is reached. Continue rigorous tests of all-physical coverage and 15-edge necessity. Preserve source/target identity, frozen scientific pins, and unadmitted author-side status. Native task owner/CLAIM/Result/review require live, separately authorized receipts.
