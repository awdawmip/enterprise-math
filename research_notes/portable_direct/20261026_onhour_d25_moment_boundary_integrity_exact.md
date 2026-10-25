# D25/LIFT — exact rank-p moment telescoper and original W scalar independent regression

2026-10-26 (Asia/Hong_Kong). **TASK_RESEARCH portable author evidence ONLY: AUTHOR EXACT DERIVATION / FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** No current native CLAIM/open/run, Source-native checkpoint, Result, review, accepted theorem, formal proof, or native benchmark is asserted.

- Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`.
- Frozen science source pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (not modified by this evidence).
- Real Research lane logical ID: \`chatgpt-research-onhour-enterprise-math-20260923\`; maintenance is separate and not claimed/operated.
- Unchanged source goal: prove or refute \`Delta_p=(G_p h-1)/p = R_p (mod p)\` for every prime \`p=13,19 (mod 24)\`; frozen D24 first digit/UR stays complete.

## Exact original-scalar cross-check

Preserve all terms in the originally defined finite hypergeometric scalar
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}.
\]
For each integer n>=0, the following is an **exact rational identity**:
\[
\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=216^{-n}\binom{2n}{n}^2\binom{3n}{n}.
\]
Proof: \((1/2)_n=(2n)!/(4^n n!)\) and
\((1/3)_n(2/3)_n=(3n)!/(27^n n!)\); cancel factorials.

Two **independent executed** exact-modular implementations were used: (A) original Pochhammer recurrence
\[
u_n/u_{n-1}=(2n-1)(3n-2)(3n-1)/(36n^3)
\]
and (B) stripped integer factorial and binomial p-valuation implementation of the RHS. Both retain all ranks n<p, including high valuation ranks.

Observed **548/548 primes 5<=p<=4000**: A=B modulo p^3. Among them **139/139 target primes** p=13 or 19 (mod24) have W_p=p mod p^3. Other 409 primes fit the stronger exploratory character pattern W_p=p*(-3/p) mod p^3. Extra trial-division-primality-verified anchors p=19963,100003,100069 give W_p=p mod p^3; p=100019 gives W_p=-p mod p^3. All extra anchors passed A=B. **These are exact finite falsifier/regression results only, NOT an all-prime proof or the native Source benchmark.**

## Exact finite moment-boundary telescoper (all integers and all suitable primes)

Consume the previously established Clausen coefficients
\[
r_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2},\qquad
S_j=\sum_{n=0}^{p-1}n^j r_n\ \ (j=0,1,2).
\]
For every n>=0, the rational ratio is
\[
r_{n+1}/r_n=\frac{(6n+1)(3n+1)}{36(n+1)^2}.
\]
Let \(G_n=36n^2r_n\). A *rankwise exact finite telescoper* is
\[
(18n^2-9n-1)r_n=G_n-G_{n+1}.
\]
Summing n=0,...,p-1 yields the exact rational identity
\[
\boxed{18S_2-9S_1-S_0=-36p^2r_p.}\tag{1}
\]
Equivalently, for \(\theta=z\,d/dz\) and \(F(z)=\sum_{n=0}^{p-1}r_nz^n\), the **exact inhomogeneous polynomial differential equation** is
\[
[\theta^2-\tfrac z2(\theta+\tfrac16)(\theta+\tfrac13)]F=-p^2r_pz^p.
\]
It is NOT legitimate to homogenize this after truncation and silently delete the rank-p boundary.

For primes \(p=6m+1\ge7\), independently recover the known coefficient \(r_p\equiv36^{-1}\pmod p\): in the product \(\prod_{j=0}^{p-1}(6j+1)\prod_{j=0}^{p-1}(3j+1)\), extract the unique p-factor in each product at j=m and j=2m; the two remaining nonzero residue permutations both multiply to \((p-1)!\). Cancel the two extracted p-factors with \((p!)^2\), retaining the unit denominator \(36^p\equiv36\pmod p\).

Therefore the **proved all-prime** third-digit observer certificate is
\[
\boxed{18S_2-9S_1-S_0\equiv-p^2\pmod{p^3}\qquad(p=6m+1\text{ prime},p\ge7).}\tag{2}
\]
Examples: p=13 defect=2028 mod 2197, p=19 defect=6498 mod 6859, p=100003 defect=1000080002100018 mod 1000090002700027. Verified independently for all **271 p=1(mod6), p<=4000** plus extra p=19963,100003,100069.

**BRC/observer use**: signed, rank-labeled rational and p-valuation carrier; theta and truncation are permitted future operations. Retain (S0,S1,S2,rank-p boundary); a positive-mass histogram or the pair (S0,S1) lacks the required signed third-digit relation. This is only a typed scalar observer within the fixed Heartbeat native X6 project, not a change to P000/worldview or a claim about 6D dynamics. Signed boundary of \`definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json\` and \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\` applied.

## Remaining genuine D25 obligation and provenance

The original frozen Source-native LIFT target is \((G_ph-1)/p-R_p\), **not** automatically identical to any author-selected numerical observer. The bridge from (2) and the verified W finite evidence to the frozen \(\Phi_{xx}\)/derivative/Frobenius port must be extracted and proved at exactly the frozen source interface. The all-prime joint cancellation, original native experiment, Resource/Claim ownership, formal Result and independent review remain NOT DONE.

Current service reads: gateway 0.6.11; Site read scope but no Researcher write authority; exact original request receipt IDs from last author-side handoff returned scoped \`CONTROL_REQUEST_NOT_FOUND\` (this does not prove no Source effect); recovery_status not available as a typed direct tool. Support issues \`awdawmip/enterprise-math#1539\`, \`#1558\`. No native write/claim/open/dispatch/benchmark was attempted. No scheduler/notification settings touched.

**Prior verified author frontier**: \`9713f10774d8c0a64c64fb2bd9888bec5679f40d\`, \`research_notes/portable_direct/20261025_onhour_d25_clausen_three_band_local_jet_joint.md\`. **Next exact research act**: source-pin the accepted definition of (G_p,h,Phi_xx,R_p), identify the full derivative-observer map for (1), and construct a signed simultaneous telescoper or an exact target counterexample. Avoid repeating D24 UR, existing Clausen cutoff, reflected jet or rank-p coefficient proof. Preserve original request IDs; reconcile before new role-bound actions.

Reproducible execution program and output were generated in the user artifact \`d25_moment_boundary_integrity_20261026.zip\` (not part of a native executed experiment). This note is a **neutral author evidence archive**, not a Source-native checkpoint or task publication.
