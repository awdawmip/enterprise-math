# X6 R133 — exact first-change radii on all 16 four-weight orthant rays

Date: 2026-11-23. **AUTHOR EXACT RATIONAL FINITE CERTIFICATE / LOCAL PYTHON REPLAY PASS / NOT INDEPENDENTLY REVIEWED.**

## Statement, scope and provenance

Continue R132 without changing the fixed scientific model. In the conditional four-positive-weight six-pair BRC observer on the selected 3-coordinate research slice, take physical integer Port `p=10`, signed triples modulo **sign only** (positive multiples remain distinct), and strict near-factor `3/2`. Let `h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, `g_ij(a)=|h_i-h_j|`, `s_ij(w)=w_i+w_j`, and `F_w(a)=max_(i<j) g_ij(a)/s_ij(w)`. Write `eta_10(w)=min_(0<q(a)<=10)F_w(a)` and `N_10(w)={a mod sign : q(a)<=10, 2F_w(a)<3eta_10(w)}`, with `q(a)=max(sum(a_i^+),sum((-a_i)^+))`.

The source-pinned R121 optimizer bank `B18` dominates all 1,935 physical Port-10 unoriented integer directions componentwise in the six-gap representation; R122's universal exclusion leaves `E20` (20 directions). This is the identical model studied by R131–R132 and is **not a native six-axis/time-evolution theorem**.

For a center `w0>0` and any sign vector `sigma in {-1,+1}^4`, define the *positive orthant ray* `w_sigma(t)_i=w0_i(1+sigma_i*t)` for `0<=t<1`. Let `tau_sigma=inf{t in [0,1): N_10(w_sigma(t)) != N_10(w0)}`, with symbol `none<1` when the set is empty. The following exact tables compute every first transition, including any transition occurring precisely at a strict boundary equality.

## Theorem — complete exact 16-ray first-change atlas

The entries are the **first** change radius `tau`; the integer in parentheses is the number of directions lost at that first change. No entering direction occurs at the first event in these 32 cases. A dash signifies the set is unchanged for every `0<=t<1`.

| Signs (A,B,C,D) | Center I: (136,8,176,185) | Center II: (722,465,240,48) |
|:--|:--|:--|
| ---- | — | — |
| ---+ | 119/489 (2) | 1/161 (2) |
| --+- | 43/1803 (1) | 1/641 (1) |
| --++ | 43/693 (1) | 1/721 (2) |
| -+-- | 9/329 (1) | — |
| -+-+ | 119/505 (2) | 1/161 (2) |
| -++- | 43/1883 (1) | 1/641 (1) |
| -+++ | 43/773 (1) | 1/721 (2) |
| +--- | 3/1091 (6) | — |
| +--+ | 81/2735 (1) | 39/167 (1) |
| +-+- | 3/1091 (6) | 39/391 (1) |
| +-++ | — | 13/173 (1) |
| ++-- | **1/369 (6)** | 9/71 (3) |
| ++-+ | 9/343 (1) | 1/7 (3) |
| +++- | **1/369 (6)** | — |
| ++++ | — | — |

In particular the minimum of the 16 first-change radii is `1/369` for center I (signs `++--` or `+++-`) and `1/721` for center II (`--++` or `-+++`). Thus R132's sharp *uniform centered relative L-infinity* radii reappear as the minima of this directional atlas. Several directions are much more stable: for example, center II is unchanged throughout `+---` and `+++-` up to `t<1`. This is an anisotropic refinement of R132, not a new optimizer definition or a claim that all possible non-radial chamber facets have been classified.

## Exhaustive rational certification — why finitely many points suffice for every real t

For `w_sigma(t)`, every pair capacity is an affine function `s_j(t)=alpha_j+beta_j*t>0` throughout `0<=t<1`. R121 and R122 give exactly
`eta_10(t)=min_(b in B18) max_k g_k(b)/s_k(t)`;
`N_10(t)={a in E20 : 2 max_j g_j(a)/s_j(t)<3eta_10(t)}`.

Membership in `N_10` is a Boolean combination of atomic rational inequalities. Each potentially changing atomic comparison has the form
`2*g_j(a)*s_k(t) ? 3*g_k(b)*s_j(t)` for some `a in E20`, `b in B18`, and `j,k in {01,02,03,12,13,23}`. Since its difference is affine in t, its sign is constant between consecutive roots. Comparisons identically equal for all t have constant sign and cause no omitted transition. Consequently, enumerating all roots in `(0,1)`, evaluating `N_10` at each root and at one exact rational midpoint of every intervening open interval, proves the entire continuum classification. In particular this catches an entering direction appearing *just after* an equality, even if the set has not changed at the equality itself.

The standalone Python verifier attached to this note regenerates the 1,935-direction lattice, proves B18 coverage and E20 exclusion by exact integer comparisons, enumerates all finite breakpoint candidates with `fractions.Fraction`, checks roots and midpoints, and asserts the 32 exact radii printed above. It prints the exact identities of the first exiting directions, not just their counts; no floating-point tolerance or sampled-continuum extrapolation is used. The local replay on 2026-11-23 returned `TABLE CERTIFICATE PASS` for both centers. This is author verification, not independent mathematical acceptance.

## Verified frozen sources and next step

- R121 optimizer: `enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`
- R122 exclusion: `enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`
- R132 proof and base sets: `enterprise-math@e297bc1c4f414223f2be0f569d1783d0e30e9711:research_notes/portable_direct/2026-11-23_r2_x6_r132_sharp_two_centered_relative_boxes.md`

Next question: classify the full *non-radial* connected stability chamber around each center in projective positive-weight space, including its irredundant facets and adjacent eight-/seven-direction regions. The first-exit atlas supplies a directional exact check for that future construction. Existing P000, native six-axis roles, frozen scientific source and formal Task/CLAIM/Result/Review authority are preserved.
