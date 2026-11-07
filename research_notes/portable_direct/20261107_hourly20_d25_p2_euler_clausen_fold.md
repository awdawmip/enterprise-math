# D25 — Universal mod-p² Clausen–Euler truncation and CM first-digit source

2026-11-07; TASK_RESEARCH author-side; **PROVED POLYNOMIAL ALGEBRA / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-hourly-enterprise-math-20260923` is distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`. Consumed scientific material (not identity) from `05f75b399746c5b749e857e13c8b1bfccae658b1`, `822c7965917f8dfcc35d5d29cc7de6b9c0c9f105` and parallel onhour `3918433058fe75f0e46bf1f18d58998d5bf79a71`. Earlier CM0 first-digit and Hasse roots are explicit inherited hypotheses, not newly proved here.

## Theorem 1: universal polynomial congruences in Z_(p)[z]

Define
`A_<p(z)=sum_{n=0}^{p-1} [(1/2)_n(1/3)_n(2/3)_n/(n!)^3] z^n` and
`B_<p(z)=sum_{n=0}^{p-1} [(1/2)_n(1/4)_n(3/4)_n/(n!)^3] z^n`.

For every prime `p=6m+1>3`, let
`F_p(z)=sum_{n=0}^{2m} [(1/6)_n(1/3)_n/(n!)^2]z^n`. Then
`A_<p(z) = F_p(z)^2 (mod p^2)`, **coefficientwise**.

For every prime `p=8k+3>3`, let
`G_p(z)=sum_{n=0}^{3k+1} [(1/8)_n(3/8)_n/(n!)^2]z^n`. Then
`B_<p(z) = G_p(z)^2 (mod p^2)`, **coefficientwise**.

For every prime `p=8k+5`, let
`T_p(z)=sum_{n=0}^{3k+1} [(5/8)_n(7/8)_n/(n!)^2]z^n`. Then
`B_<p(z) = (1-z) T_p(z)^2 (mod p^2)`, **coefficientwise**.

**Proof.** Clausen's identity gives exact formal rational-series squares for both 3F2 functions. Euler's Gauss transformation rewrites the 2304 square as `(1-z)*2F1(5/8,7/8;1;z)^2`. For the A Gauss series the first p-dividing rising-factorial factors have zero-based indices `m` and `2m`. Every coefficient with degree greater than `2m` therefore has valuation at least two; the retained square has degree `4m<p`. For the p=8k+3 B Gauss series the corresponding first-hit indices are `k` and `3k+1`; the mod-p² retained square has degree `6k+2<p`. For p=8k+5 the Euler-transformed parameters (5/8,7/8) have the same first-hit indices `k,3k+1`; including `1-z`, its square has degree `6k+3<p`. Thus truncating the formal coefficient identities at degree <p loses nothing modulo p² in these three representations. No CM input is required for this polynomial theorem.

## Corollary 2: a unified finite-field B source

Modulo p, `F_p(z)=F_m^0(z)=sum_{n=0}^m binom(m,n)binom(2m,n)z^n`.
In **both** B cases `p=8k+3` and `p=8k+5`, the appropriate Gauss factor `G_p` or `T_p` reduces to the *same*
`H_k(z)=sum_{n=0}^k binom(k,n)binom(3k+1,n)z^n`.
Indeed, the Gauss upper parameters reduce to `(-k,-3k-1)` in either order.

The previously established CM0 source reports `F_m^0(1/2)=0 (mod p)` for target primes `p=13,19 (mod24)`, and the previously proved author-side CM/Hasse classification gives `H_k(1/9)=0 (mod p)` in those classes. **With these exact cited input roots**, Theorem 1 proves for every target prime
`A_p:=A_<p(1/2)=0 (mod p²)` and `B_p:=B_<p(1/9)=0 (mod p²)`.
This upgrades the earlier 301-prime observation to an algebraic derivation whose only external mathematical input is the specified CM root status.

## Theorem 3: exact weighted Frobenius leading digit on the B side

Put `D=z d/dz`, `V_p=(1+8D)B_<p(1/9)`, `chi_p=(-3/p)`.
By differentiating Theorem 1 modulo p², and using `G_p(1/9),T_p(1/9)=0 (mod p)` in the respective target classes,
`V_p/p=(16/9)[G_p(1/9)/p]H_k'(1/9) (mod p)` when `p=19 mod24`,
and `V_p/p=(128/81)[T_p(1/9)/p]H_k'(1/9) (mod p)` when `p=13 mod24`.

The Guo–Zudilin full-sum theorem (`V_p=p chi_p (mod p³)` for all primes p>3) thus gives **unconditional within its existing CM/Hasse root dependency**
`[G_p(1/9)/p]H_k'(1/9) = (9/16)chi_p (mod p)` for `p=19 mod24`,
`[T_p(1/9)/p]H_k'(1/9) = (81/128)chi_p (mod p)` for `p=13 mod24`.
Here `chi_p=1` for the frozen classes. The two class-specific coefficients preserve the Euler source factor, giving a typed BRC observable rather than a source-collapsed scalar.

On the A side, Theorem 1 likewise gives the exact conditional root-derived identity
`W_p/p=6[F_p(1/2)/p]F_p'(1/2) (mod p)`, where `W_p=(1+6D)A_<p(1/2)`. Proving its target value 1 for all primes remains a meaningful next D25 obligation; this relation is a sharper single-Gauss criterion.

## Finite execution and BRC method

The local standard-library checker `d25_p2_euler_clausen_fold_20261107.py` independently checked the **entire coefficient vector mod p²** for 25 A-primes, 13 B3-primes and 14 B5-primes (p<250), plus CM roots, unweighted p² vanishing, first weighted digit and both Gauss-product identities for **all 107 target primes p<3000** (53 in class 13, 54 in class 19). For p=13,19,37,43,67,373 it independently checked third-digit values against the full integer-binomial sum. Exact examples `(p,A_p/p² mod p,B_p/p² mod p)`: `(13,11,4)`, `(19,8,7)`, `(43,24,15)`, `(67,16,36)`, `(373,71,203)`; p² vanishing is sharp at these primes. No float computation and no native p373 H0/B0 benchmark was performed.

BRC reuse `COMPOSE_APPLIED`: indexed Gauss coefficient ports; first p-factor positions; Euler fold factor; Hasse zero; separately normalized `Q_p/p`, derivative and A/B source labels. The exact degree inequalities provide a safe scalar projection **through p² only**. For the p³ mother objective, retain both three-stratum coefficient lifts, signed Fricke sources and omitted carry ports.

**Next:** use the exact A/B p³ coefficient lifts and the new normalized Gauss digits to derive a p²-normalized finite-field formula for `(W_p-V_p)/p²`, then seek a WZ/Dwork identity valid for both target classes. The frozen mother objective `Delta_p-R_p=0 mod p` (equiv. `W_p=p mod p³`) remains OPEN.

**Native status observed 2026-11-07 11:25 UTC:** `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; Site `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. Old unknown requests `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13` and protected session/staging preserved. `REGISTER_PENDING` / `SYNC_DEBT`. No native claim/run/checkpoint, Result, review or acceptance inferred. Support `awdawmip/enterprise-math#1558`.

Sources: classical Euler and Clausen identities; Guo & Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, https://arxiv.org/abs/1803.01830; the existing CM/Hasse notes cited above.
