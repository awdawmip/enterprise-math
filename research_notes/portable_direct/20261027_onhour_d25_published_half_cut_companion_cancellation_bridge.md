# D25 SECOND-DIGIT-LIFT — theorem-backed companion half-cut and original high-band precision reduction

**Observed:** 2026-10-27, Research-onhour TASK_RESEARCH.
**Scope/status:** EXACT DERIVED CERTIFICATE / 8 EXECUTED FINITE CROSSCHECKS / AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0_B0_NOT_EXECUTED.
**Mother:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
**Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (not rebased).
**Logical Research conversation:** chatgpt-research-onhour-enterprise-math-20260923; NOT CONTROL_PLANE_MAINTENANCE.

## Directly consumed science and corrected external theorem scope

The accepted D24 UR/JT0 first digit and the earlier source-aligned D25 scalar interface give, for target primes p ≡ 13 or 19 (mod 24),

    Delta_p - R_p ≡ (W_p-p)/p² (mod p),  W_p ≡ p (mod p²),

where w_n=(6n+1)(2n)!(3n)!/((n!)^5 216^n) and W_p=sum(n=0..p-1) w_n.
The old author bridge to S_p and its nonzero Wilson gap E_p (commit dffe386cee25fb9c650d4aa46ff6f501c3745e8a) are consumed and NOT recredited.

**Material previously omitted part of the published source:** Guo and Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358; arXiv:1803.01830, abstract and Theorem 1.1 (q→1), explicitly prove **BOTH** of

    S(p-1) ≡ p * (-3/p) (mod p³),
    S((p-1)/2) ≡ p * (-3/p) (mod p³),

for all primes p>3, with the SAME weighted original companion summand

    s_n=(8n+1)(4n)!/((n!)^4 2304^n),  S(N)=sum(n=0..N) s_n.

Source: https://arxiv.org/abs/1803.01830 ; original author PDF https://math.ecnu.edu.cn/~jwguo/maths/q-congruence03q.pdf .
The previous D25 bridge note cited only full truncation. This finding CONSUMES rather than newly proves the half-truncation supercongruence. Target primes are p≡1 mod3 and have (-3/p)=+1.

## Proved all-target exact reduction: remove the complete high companion band as a SUM, not termwise

Write p=6m+1, set q=floor((3p-1)/4), and define

    V_p = sum(n=0..3m) (w_n-s_n),
    H_p = sum(n=3m+1..4m)
            (6n+1) (2n-p)! (3n-p)! / ((n!)^5 216^n)  in F_p.

**Exact derived theorem for EVERY target prime**:

    V_p ∈ p² Z_(p),
    (W_p-p)/p² ≡ V_p/p² + H_p (mod p).                   (HC-BRIDGE)

Therefore at the original frozen source interface,

    Delta_p - R_p ≡ V_p/p² + H_p (mod p),
    LIFT  iff  V_p/p² ≡ -H_p (mod p) for all target p.

This last equality remains OPEN as an all-prime proof; HC-BRIDGE is an unconditional equivalence that is smaller in precision/range than the previously used full two-model bridge.

**Proof (without assuming LIFT):**

1. Guo–Zudilin's two distinct published supercongruences imply
   sum(n=3m+1..p-1) s_n ≡ 0 (mod p³). This is a signed *collective* cancellation: many summands have exact valuation two and do NOT vanish separately.
2. Exact factorial valuation for n≤p-1 gives v_p((2n)!(3n)!/(n!)^5)=floor(2n/p)+floor(3n/p). In n>4m both floors total at least 3, so w_n≡0 (mod p³). For 3m+1≤n≤4m, both floors equal 1 and the signed weight 6n+1 is a p-unit, giving valuation exactly two.
3. Wilson's theorem yields (2n)!/p≡-(2n-p)! and (3n)!/p≡-(3n-p)! (mod p); their signs multiply to +1. Thus w_n/p² equals the summand H_p modulo p for precisely this high band.
4. Split W into n≤3m, 3m+1..4m, and n>4m; replace p by the *published half companion* S(3m) modulo p³. The displayed HC-BRIDGE follows.
5. Accepted first-digit W≡p (mod p²), the high original band is divisible by p², and S(3m)≡p (mod p²); hence V_p is divisible by p². Division is legitimate in Z_(p); no unproved second-digit cancellation is used.

**Precision/range accounting:** previous exact two-model bridge retained n≤4m in the joint p³ prefix and an explicit nonzero companion tail at 4m<n≤q. The new certificate retains paired w_n-s_n only at n≤3m=(p-1)/2; n=3m+1..4m needs *prime-field only* H_p, while **all s_n for n>3m are eliminated collectively by the independently published full-versus-half theorem**. In particular, at p=373 the expensive paired prefix contracts from 249 to 187 terms; 62 remaining W terms are computed in F_373, and no companion n>186 has to be numerically transported. This is a precise decrease in p-adic precision and observer support; it does not assert that a whole all-prime proof has been completed.

## Nonzero earlier gap is preserved and explained, not silently discarded

For p=373: m=62, 3m=186, 4m=248, q=279, p²=139129, p³=51895117.

    V_373             = 14886803 = 107 * 139129  (mod 51895117),
    p² H_373          = 37008314 = 266 * 139129  (mod 51895117),
    V_373 + p² H_373 = 51895117 ≡ 0               (mod 51895117).

The preceding Wilson-tail theorem found a genuinely nonzero gap:

    sum(n=249..279) s_n = 39095249 = 281*p² (mod p³).

The newly separated *inside* high-companion band gives

    sum(n=187..248) s_n = 12799868 = 92*p² (mod p³),

and 92+281=373≡0 (mod 373). Thus Guo–Zudilin's half-cut removes the **entire signed high companion band by a proved cancellation**, not by the false claim that its Wilson gap vanishes. This is an explicit BRC COMPOSE_APPLIED operation: label/valuation/high-band provenance survives until the proved collective observer allows compression.

## Reproducible exact arithmetic and source/ownership limits

Deterministic standard-library integer checker, executed for all eight selected target primes p=13,19,37,43,61,67,211,373:

    research_notes/portable_direct/d25_companion_half_cut_strict_bridge_checker_20261027.py
    initial source commit e65f89a8e7f157aa1c5d3a8a1b08dcb4e120f17d

Each case computed the full original W and full/half original S through exact binomial coefficients modulo p³, checked the direct high W band against an independently computed Wilson F_p factorial formula, checked high S=0 and each vanished term after q, verified V/p² and the structural identity, and inspected the p373 nonzero-gap split. All eight executions passed. Rows (p, m, 3m, 4m, q, V/p² modp, H modp, residual, high_S_modp³):

    (13,2,6,8,9,3,10,0,0)
    (19,3,9,12,14,10,9,0,0)
    (37,6,18,24,27,17,20,0,0)
    (43,7,21,28,32,8,35,0,0)
    (61,10,30,40,45,44,17,0,0)
    (67,11,33,44,50,9,58,0,0)
    (211,35,105,140,158,9,202,0,0)
    (373,62,186,248,279,107,266,0,0)

SHA-256 of JSON-serialized list of lists (separators(",",":")):
906c1683c3f0b08e42596a8711613e00fe721cd9525404f33264c5bd9c4408c1.

**Proof/source distinction:** the all-prime companion high-band vanishing is a corollary of already published Guo–Zudilin full AND half congruences. The HC-BRIDGE is the newly derived precise combination with the frozen original D25 scalar interface and Wilson high-band formula. The eight direct residual zeros are **finite tests only**, not universal proof. This is external ordinary hypergeometric arithmetic, not a proof about P000's native X6/three-dimensional-slice dynamics and NOT an original-class H0/B0 native execution.

**Unresolved original scientific/experimental frontier:** Prove for every target p that V_p/p²+H_p=0, OR supply a genuine counterexample; independently execute the **same-original-class** H0/B0 divided-power benchmark at p=373, including [X]U mod139129, module rank, semilinear Frobenius direction and two-digit eta, signed odd Hesse/Green readout, original kappa and Delta-R, and raw reproducer. Current support is https://github.com/awdawmip/enterprise-math/issues/1559 PENDING_OWNER / NOT_EXECUTED; no authorized executor is asserted. No new Task dispatch, scheduler, hosted Action or alternate benchmark is created.

**Control continuation (actual 06:00 Research lane only):** read-only recovery issue https://github.com/awdawmip/kimi-query-bridge/issues/6581 matched SUCCEEDED, returned a local ACTIVE session projection MCP-de3e5bafb24f43f4a5e6285e7601676a with source_authority_verified=false, prior_contribution_ids=[] (old declared EM-DIRECT-B63A06 not inherited), no pending request/own winning claim/open run; preserved neutral staging SD-d7c23e7984c2ddaac60a remains unmerged. Exact own D25 continuation issue https://github.com/awdawmip/kimi-query-bridge/issues/6582 returned REJECTED / PREREQUISITE_NOT_SUCCEEDED. Existing older dispatch #6576 ended FAILED / TimeoutExpired, not NO_DISPATCH. Control repair is https://github.com/awdawmip/enterprise-math/issues/1539. No authorized session/claim/run or Source-native checkpoint could be asserted; no historical mutation was replayed. Treat this GitHub note as **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**, pending canonical activity/Source intake and independent review.

**Next exact action:** the lawful continuation path must first resolve #1539 and own Research identity/prior contributions, then consume this immutable author certificate under exact Source continuation and consider its strict half-cut precision reduction without reopening accepted D24 UR. Mathematically, the next unresolved dependency is a uniform proof or counterexample for the low-prefix divided digit versus H_p; no extra Wilson gap computation is needed. The native H0/B0 task remains highest experimental priority. Preserve frozen source pin; Research and maintenance identities remain distinct.
