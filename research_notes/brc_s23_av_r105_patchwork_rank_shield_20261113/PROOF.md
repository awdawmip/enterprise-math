# R105 — Patchwork rank-shield certificates and edit-stable historical Top-k equivalence

Date: 2026-11-13 (Asia/Shanghai). Independent author-side continuation of [R104](https://github.com/awdawmip/enterprise-math/blob/869af6d9115bec00913af228cef7b9793b771cf3/research_notes/brc_s23_av_r104_exact_rank_shield_20261112/PROOF.md). Researcher: EM-DIRECT-EF19E1; Research Activity: RA-7B0A9D106EA9A31B8FE5A210. Scientific input remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Model and observer

This is the finite rational directed circular-source auxiliary model of R104, not a claim about unbridged native X6 dynamics. Complete source identities `u=(t,branch)` have integral components and descending lexicographic rank; all identity and provenance distinctions are retained. Fix `sigma=(j,x,a,b)`, where `j,a,b` are integers and `x` is rational. At real `theta`, write `s_u={x+(t-j)theta}`, `A={a theta}`, `B={b theta}`, with fractional parts in `[0,1)`. `M_u(theta)` holds when `A<B` and `A<=s_u<B`, or `A>B` and `s_u>=A or s_u<B`; `A=B` yields an empty directed half-open arc. For finite source sets `F,G`, `Top_k(S,theta)` is the ordered first `k` eligible complete identities. Set `C=F intersection G`, `Delta=F symmetric_difference G`, `k>=1`, and let `I=[L,U]` be a closed rational interval.

## R105.1 — Exact finite patchwork certificate (sound and complete)

An exact atomic decomposition of I comprises its rational critical points and the open gaps between consecutive points. For each discrepant `u in Delta` and each atom `J`, store one of:

- `OUT(u,J)`: `M_u(theta)` is false for every `theta in J`.
- `SHIELD(u,J,S)`: `S` is a set of at least `k` distinct identities belonging to `C`, every `v in S` ranks strictly above `u`, and each `M_v(theta)` is true for every `theta in J`.

**Theorem.** `Top_k(F,theta)=Top_k(G,theta)` for every real `theta in I` if and only if there exists a finite cover of I by such verified atoms for every `u in Delta`.

**Soundness.** A discrepant identity is either out or has `k` currently eligible common identities strictly above it; apply R104.1 at each `theta`. **Completeness.** The R104.2 six-affine-phase construction gives a finite partition for every `u` and its higher common sources: `a theta`, `b theta`, `(t-j)theta+x`, `(t-j-a)theta+x`, `(t-j-b)theta+x`, and `(a-b)theta` hitting integers, together with `L,U`. On each open gap, every relevant membership is constant; singleton boundary points are checked separately. If equality holds, R104.1 gives at least `k` higher eligible common identities on every atom where `u` is eligible; take any `k` of them, or all of them to preserve edit slack. QED.

For `K` distinct common critical points including interval endpoints, the partition has at most `2K-1` atoms, and at most `|Delta|(2K-1)` per-discrepancy certificate entries. A failing atom supplies a rational point (endpoint or rational midpoint) `theta_0`, a discrepant eligible `u`, and fewer than `k` eligible higher common identities; by R104.1 the two Top-k outputs differ there. This provides a complete exact mismatch certificate.

Atoms retain endpoint openness/closedness: a shield valid on `[L,c)` need not be valid at `c`.

## R105.2 — Transfer between versions and rank monotonicity

Suppose the above certificate was built for `F,G,k,sigma,I`. Let `F',G'` be new finite versions with the same observation signature and interval; write `Delta'=F' symmetric_difference G'` and `C'=F' intersection G'`. Assume `Delta' subseteq Delta`. For every `u in Delta'` and each old certificate atom where u is eligible, assume at least `k` recorded shield identities also belong to `C'`. Then

`Top_k(F',theta)=Top_k(G',theta)` for all real `theta in I`.

Proof: old OUT and IN membership certificates depend only on `(u,sigma,I)`, not source-version membership. The surviving guards are common to `F',G'`, eligible throughout their atoms, and higher than u. Apply R104.1 to the new pair. Additional common sources can only improve shielding. Every atom is retained, so exact endpoints and gaps are covered. QED.

If an atom originally lists `m>=k+r` guards, deleting or losing up to `r` of those guards from the new common set leaves a valid rank-k shield on that atom. This slack rule is sharp in the worst case: with exactly `k` active higher common guards, removing one may expose an active discrepancy into one Top-k output. A rank-`m` certificate is also valid for every `1<=k<=m` at the same source/version/observer scope.

**Persistence interface.** Each reusable certificate record retains exact `sigma`, rational atom endpoints and openness, `u`, guard full identities, `k`, the fixed frozen source provenance, and the verified point/gap membership evidence. New version nodes only need to validate the discrepancy subset, guard intersection and any newly introduced discrepancies. If this sufficient transfer check fails, recompute the affected atoms; a failed reuse check does not infer that the Top-k functions differ.

## R105.3 — Strictly useful patchwork example

Take `sigma=(j,x,a,b)=(0,1/4,0,1)`, `I=[2/5,4/5]`, `k=1`. Let
`u=(0,0)`, `C={(1,0),(2,0)}`, `F=C union {u}`, `G=C`.

For every `theta in I`, the discrepancy u is eligible since `A=0`, `B=theta`, and `s_u=1/4<theta`.

For `theta in [2/5,3/4)`, the higher common identity `(2,0)` is eligible: `s_2=2theta-3/4` lies in `[0,theta)`. At the exact boundary `theta=3/4`, it has `s_2=3/4=B` and becomes OUT. On `[3/4,4/5]`, `(1,0)` is eligible, with `s_1=theta-3/4` in `[0,theta)`.

Conversely `(1,0)` is OUT at `theta=2/5`, while `(2,0)` is OUT at `theta=3/4`. Thus no **single** common identity supplies a uniform whole-I shield, but the two precisely glued half-open/closed subintervals give a complete Top-1 equality certificate. An all-OUT test also fails since u is eligible throughout I.

## R105.4 — Edit-slack example

For `sigma=(0,1/4,0,1)`, `I=[1/2,2/3]`, `k=2`, take discrepancy `u=(0,0)`, and four higher common identities `(0,10),(0,11),(0,12),(0,13)`. They all remain eligible over I. Any two common deletions retain two guards and exact Top-2 equality. Deleting three common guards leaves one and exposes u into Top-2, for instance at `theta=1/2`. This realizes the stated sharp slack boundary.

## Exact verification and accounting

The accompanying `check_r105.py` uses Python `fractions.Fraction`, seeded random finite historical source pairs, six-affine-phase exact integer roots, all singleton boundary points and rational gap midpoints. It independently compares the certificate decision with direct full Top-k evaluation and validates every claimed mismatch witness. It also tests source-version certificate transfer, one-common-deletion reuse, the patchwork example and the slack example.

Author run: `R105_PASS 220 52 168 10330 109`. Breakdown: 220 random version pairs, 52 matching, 168 different with exact rational witnesses; 10,330 exact atomic representatives; 109 one-common-deletion transfers passing the sufficient retained-shield test. `verification_r105.json` contains the result and seed.

The finite randomized audit validates these tested cases; the universal statements above are proved by exact finite-partition arguments. No CPU/bit-complexity acceleration or independent mathematical admission is asserted.

## Next concrete question — R106

Maintain a DAG of interval-specific `OUT` and guard-IN certificates with split/merge operations. Establish a certified update cost in terms of changed source identities, affected atomic intervals, guard slack, bit length and retained version memory; compare against net-overlay and explicit materialization on both patchwork-friendly and adversarial histories. Preserve complete identity/provenance and rational witness recovery.

State: independent author-side material. `RS-S23-AV` exact current native task lookup returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`; no shared CLAIM/open or independent review is claimed.
