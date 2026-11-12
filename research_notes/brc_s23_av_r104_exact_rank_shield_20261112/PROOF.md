# R104 — Exact rank-shield equivalence for historical Top-k source versions

Date: 2026-11-12. Scope: finite rational directed circular-source auxiliary model. This is an author-side independent mathematical continuation of R103. Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34, unchanged. R103 source: d73d6848139953bf3c3f6e5640c6abf15c7b82f6 / research_notes/brc_s23_av_r103_persistent_overlay_out_equivalence_20261112/PROOF.md. Shared Task CLAIM and independent review remain separate native operations.

## Exact source model

A complete identity is u=(t,branch), ordered by descending lexicographic rank, with t and branch integral. Fix sigma=(j,x,a,b), integers j,a,b and rational x. At real parameter theta let s_u={x+(t-j)theta}, A={a theta}, B={b theta}, fractional parts in [0,1). A=B means an empty directed half-open arc. If A<B, eligibility M_u is A<=s_u<B; if A>B, it is (s_u>=A or s_u<B). Top_k(S,theta) is the descending sequence of up to k eligible complete identities in finite S.

For two terminal history versions F,G put C=F intersection G and Delta=F symmetric_difference G. The canonical net overlay construction from R103 can recover F,G without replaying the history.

## R104.1: pointwise necessary-and-sufficient rank-shield theorem

For every real theta, all finite F,G and k>=1:

Top_k(F,theta)=Top_k(G,theta)  IF AND ONLY IF

for every u in Delta with M_u(theta)=true, at least k eligible COMMON identities strictly outrank u:

count{v in C : v>u and M_v(theta)} >= k.

Proof (reverse): Every eligible discrepant identity has k common eligible identities above it, so no discrepant identity can occupy either Top-k list. Both lists consist of exactly the same ordered common eligible prefix.

Proof (forward): If two Top-k sequences are equal, every identity in that common output belongs to C, since a discrepant identity belongs to exactly one version. If the output has fewer than k identities, then any eligible discrepancy would extend the containing version's output, contradicting equality. If it contains k common identities, each eligible discrepancy must rank below all k of them, again giving the stated count. QED.

This is strictly stronger than R103's sufficient all-OUT symmetric-difference check: an eligible difference can be harmless when hidden below the kth eligible common rank.

## R104.2: exact rational interval certificate and witness

For a rational closed I=[L,U], it suffices to check, separately for each u in Delta, only u and its HIGHER common identities H_u={v in C:v>u}. If |H_u|<k, u must be OUT over I. Otherwise the exact condition is

for all theta in I: NOT M_u(theta) OR count{v in H_u : M_v(theta)}>=k.

The membership predicates may change only at the endpoints and at rational theta for which one of the six affine phases

a*theta, b*theta, (t-j)*theta+x, (t-j-a)*theta+x, (t-j-b)*theta+x, (a-b)*theta

is an integer (t ranges over relevant source times). Generate all such roots in I, check every root and a rational midpoint between successive roots. On open gaps the phase fractional parts and all comparisons have unchanged order; every M_u is therefore constant. This is an exact complete finite real-interval check including coincident endpoints, wrap-arounds, and empty A=B arcs.

A local failure gives an exact rational theta at which the two Top-k sequences differ by R104.1; the checker independently evaluates both lists to verify the witness.

A cheaper sufficient certificate may select k common higher-ranked identities which are independently certified IN over the WHOLE interval. This shields the discrepancy even when that discrepancy is IN; the certificate can be checked with the same exact single-source phase cuts. Certificates may vary on a finite rational interval partition. Failure to find a uniform shield invokes the complete local check, not an inequality claim.

## R104.3: active-difference example that OUT pruning cannot certify

Let sigma=(0,1/4,0,1), I=[1/2,3/4], k=3.
Let C={(0,10),(0,11),(0,12)} union {(t,0):1<=t<=40}, F=C union {(0,0)}, G=C.

For every theta in I, A=0, B=theta, and the four t=0 identities have s_u=1/4, so ALL FOUR are eligible throughout I. The three common identities (0,10),(0,11),(0,12) strictly outrank the discrepant (0,0); their individual IN certificates prove full Top-3 equality even though the discrepancy is active.

For this family the six-phase full-union baseline generates 186 exact cutpoints / 371 representatives. The uniform shield uses three stationary common identities, each requiring only the two interval endpoints, and zero additional joint-profile cutpoints. This is a comparison of exact structural operations, not a general speedup measurement. Replacing the low-ranked difference with a sufficiently high-ranked source destroys the shield and gives an exact rational mismatch witness.

## Actual code audit

The companion independently executable Python program uses fractions.Fraction and random seed 10420261112; it compares the complete reference six-phase interval classification with the local rank-shield algorithm, checking every unequal output witness by direct ranking.

Successful author execution: R104_PASS 240 7020 162 54 186 0.
- 240 random version pairs: 78 equal and 162 unequal; 162 exact rational witnesses.
- 7,020 pointwise full-cut representatives, plus 54 singleton/end-boundary cases.
- Total baseline cuts over random pairs: 3,630. Total local post-shortcut cuts across discrepant identities: 3,262. Different cost aggregations; no universal CPU claim.
- The active-difference family above: 43 common identities, 186 full cuts, three certified stationary shields and zero additional joint cuts.

Evidence: check_r104.py and verification_r104.json in this exact directory. The proof is author-side in its stated model; source persistence is not a mathematical promotion.

## R105 research problem

Construct a persistent rank-shield certificate index, keyed by observation signature, rational interval, k, common identity provenance and source-version membership. Study interval-cover composition of different common shields, certificate reuse across history DAG branches, and joint costs of OUT-only pruning, rank-shield evaluation, persistent net overlays and explicit function materialization. Account for proof-building cost, exact rational bit operations, retained memory, and mismatch witness recovery.