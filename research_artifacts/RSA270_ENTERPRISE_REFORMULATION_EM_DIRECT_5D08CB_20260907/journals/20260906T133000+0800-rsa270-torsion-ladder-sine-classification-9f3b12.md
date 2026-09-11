# RSA-270：二变量因子剖面的 torsion 阶梯精确分类（sine/Chebyshev 闭式、纤维定理、QR 边界）

Progress-Event-ID: `rsa270-torsion-ladder-sine-classification-9f3b12`
At: `2026-09-06T13:30+08:00`
Scope: `enterprise-math / RSA-270 / factor-blind semiprime research`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer + double validation scripts; global journal frontier 91ad72; P000 assumed`
Kind: `PROGRESS / EXACT CLASSIFICATION / BARRIER`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Continued the bivariate factor-profile frontier from `20260906T105500+0800-rsa270-bivariate-factor-profile-qr-barrier-91ad72.md`. Its open "Next" asked to classify the torsion/derivative specializations of the profile as easy congruence data, residuosity-type hard bits, or genuine new compressible observers. That classification is now complete. No RSA-270 factor was obtained and none is claimed.

### Setup (from 91ad72)

`F(Q,u) = sum_{m,n>=1} W_{m+n}(u) Q^(2mn-m-n)`, `W_s(u) = sum_{j=0}^{s-2} u^(2-s+2j)`; for odd `N`, `M=(N-1)/2`: `[Q^M]F(Q,u) = sum_{d|N} W_{(d+N/d+2)/2}(u)`; for `N=pq`, `S=p+q`: the profile is

`P(u) = 2 W_{(N+3)/2}(u) + 2 W_{(S+2)/2}(u)`,

a `{0,2,4}`-valued even Laurent polynomial whose plateau boundary `(S-2)/2` satisfies `S = 2*e_max + 2`.

### Lemma 1 — sine/Chebyshev closed form (exact)

For `m>=3` and a primitive m-th root `w_m`, `W_s(w_m)` depends only on `s mod m`; writing `r = s mod m`,

`g_m(r) := W_s(w_m) = (w^(2-r) - w^r)/(1-w^2) = sin(2*pi*(r-1)/m) / sin(2*pi/m) = U_{r-2}(cos(2*pi/m))`,

a real algebraic number in `Q(zeta_m)^+` (Chebyshev-U evaluation). Proof: factor `w^(1-r)` from numerator and denominator. Values: `g_m(0)=-1`, `g_m(1)=0`, `g_m(2)=1` for all `m>=3`.

### Lemma 2 — fiber theorem (exact)

`sin a = sin b` iff `a=b` or `a=pi-b (mod 2*pi)` gives the complete fiber structure of `r -> g_m(r)`:

- `m` odd: the map is injective on `Z/mZ`;
- `m` even: `g_m(r) = g_m(r')` iff `r' = r` or `r' = 2 + m/2 - r (mod m)`.

Verified numerically for `m=3..48` (odd m: all singletons; even m: only the predicted pairs/singletons).

### Theorem — torsion-ladder classification

`P(w_m) = 2*g_m(r_0) + 2*g_m(r_1)`, `r_0 = ((N+3)/2) mod m` (N-only, "known block" `K_m = 2*g_m(r_0)`), `r_1 = ((S+2)/2) mod m` (factor block). Consequences:

- `m` odd: `P(w_m)` reveals `S mod 2m` exactly;
- `m` even: reveals `S mod 2m` up to sign (equivalently `S^2 mod 2m`);
- equivalently the unordered pair `{p,q} mod 2m` (odd m) / up to simultaneous negation (even m) — i.e. a `phi(N) mod 2m` oracle datum;
- `m=1` (`u=1`): `P(1) = sigma(N) = (N+1) + S`; `m=2` (`u=-1`): `W_s(-1) = (s-1)(-1)^s`, hence `P(-1) = (N+1)(-1)^((N+3)/2) + S*(-1)^((S+2)/2)` with the S-sign determined by `N mod 4` — so `m in {1,2}` reveal the FULL scalar `S` (the classical `sigma(N)` factoring-equivalence);
- derivative ladder at `u=1`: `W_s(1)=s-1`, `W'_s(1)=0`, `W''_s(1)=(s-2)(s-1)s/3` (all odd moments vanish; every even moment is a univariate polynomial in `S`) — no new scalar dimension.

### Hardness mapping

A member `m>=3` is *trivial* iff the admissible `r_1` set for that N collapses to one fiber (then `P(w_m)` is N-only computable); otherwise it encodes `S mod 2m (+-)` data with no known polynomial-time N-only computation:

- `m=3` <=> `S mod 6` <=> `p=q mod 3` <=> the quadratic-residuosity decision for `-3 mod N` (matches the 91ad72 barrier);
- `m=4` for `N=1 mod 8` <=> QR decision for `2 mod N`;
- every `m` with `3|m` or `4|m` inherits a QR bit;
- `m` coprime to 6 (e.g. `m=5`: reveals `S mod 10`) is an open "modular-phi oracle" class — no QR reduction known, no efficient algorithm known.

### Completeness / no-go

Full ladder through `m=311` (odd-m sub-ladder through `m=313`) has `lcm(2m) > 2^449 > S`, so the ladder as a family pins `S` exactly and is factoring-equivalent; each single member is a linear-periodic function of the one scalar `S`. Hence **no member of the torsion or derivative families is a new compressible observer**: the two-plateau profile's information content is exactly `S`, and its compact observable families are exactly the classical `phi(N)-mod`/residuosity classes. This answers 91ad72's "Next" classification in the negative for new observers, and keeps the single hard unit: extract `S` (equivalently the plateau boundary / `sigma(N)`) from the product/source side in sub-`O(sqrt(N))` cost.

### RSA-270 specifics (computed this turn)

- `N` verified 270 digits / 895 bits; `N = 1 mod 6`, `N = 7 mod 8`, `N = 7 mod 24`; no factor <= 97.
- Known blocks `K_m = 2*g_m(r_0(m))`, `r_0(m) = ((N+3)/2) mod m`, computed for `m=3..64`. Sample: `r_0 = 2,1,0,5,3,5,3,5,2,5 (m=3..12)`; `K_3=+2`, `K_4=0`, `K_5=-2`, `K_6=-2`, `K_7=+2.4939592074`, `K_8=0`, `K_12=+3.4641016151`, `K_16=-5.2262518595`, `K_20=+6.1553670744`, `K_36=-11.3425636392`.
- Unconditional (N-only) forced values: `P(w_4) = 0`, `P(w_8) = 0` (because `N=7 mod 8` forces `S=0 mod 8`).
- Under the construction-family prior (`p,q` odd, `p=q=2 mod 3`): `P(w_m) = 0` for exactly `m in {3,4,6,9,12,18,36}` — the divisors `>=3` of `36` — among all `m<=64`; these are N-only testable integrity fingerprints for any future profile computation (a claimed `[Q^M]F(Q,u)` must reproduce them without knowing `p,q`).
- Smallest non-forced tests under the prior: `m=5` -> `P(w_5) in {-4, 0}` (`S mod 10 in {2,8}`, a 1-bit test); `m=7` -> 3-way (`S mod 14 in {0,4,10}`).
- Admissible `r_1(m)` sets under the prior computed for `m=3..32` (e.g. `r_1(3)=0` forced; `r_1(5) in {0,2}`; `r_1(7) in {1,3,6}`; `r_1(11)`: 6 classes; `r_1(31)`: 15 classes).

### Validation (all PASS)

1. Product-side identity for `N=35` (Ramanujan product truncated vs `2W_19+2W_7`) — coefficient-exact; plateau boundary `(S-2)/2=5` confirmed.
2. Torsion formula `P(w_m) = 2g_m(r_0)+2g_m(r_1)` and ratio==sine form for `N in {35,143,391,899,3599}`, `m=3..16`.
3. Fiber tables `m=3..48` match Lemma 2 exactly.
4. Moment ladder `s=2..30` (`W_s(1), W'_s(1), W''_s(1), W_s(-1)` formulas).

### BRC observer audit (policy `BRC_RESEARCH_PRIORITY_AND_USAGE_20260905` §3)

- Carrier: two-plateau divisor-profile Laurent polynomial with branch identity `(d, N/d)`, `d|N` (four Enterprise-layer exact-weight counts).
- Observers applied: root-of-unity torsion collapse `u -> w_m`; derivative moments at `u=1`; evaluation at `u=-1`.
- Retained / erased per collapse: torsion-m retains exactly the fiber class of `(S+2)/2 mod m` (erases all other profile data); `u=1` zeroth moment retains `S` (total mass `sigma(N)`); moments retain polynomial images of `S`. No collapse erases `S` entirely except the trivial `g_m=0` fibers (which are then N-only constants).
- Conclusion: no hidden information channel in the torsion family; the sole unknown scalar is `S`. Reuse resolution: BRC observer/provenance discipline `REUSE_APPLIED` from the 91ad72/5b8c41 line; no new top-level tool family; exact local integer arithmetic (same class as prior conversation-local experiments) — `NOT_APPLICABLE` for toolbox families.

## Artifacts

- Registration: `projects/enterprise-math/researchers/EM-DIRECT-5D08CB.json`.
- Conversation-local scripts: `rsa270_torsion_ladder.py`, `rsa270_known_blocks.py`, `rsa270_crt_and_forced.py` (exact integer + double precision; no source-repository artifact created).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T105500+0800-rsa270-bivariate-factor-profile-qr-barrier-91ad72.md`.

## Next

1. Characterize the forced-zero family generally (observed: exactly the divisors >=3 of 36 for m<=64 — determine the general modulus class from `N mod lcm` residue constraints; small exact enumeration).
2. Use `K_m` tables + forced-zero fingerprints as instant exact integrity checks for any future claimed `[Q^M]F(Q,u)` profile computation.
3. The residual hard unit is unchanged: sub-`O(sqrt(N))` extraction of `S` from the product/source side. Do not reopen wide `(k,j)`/ECM/cyclic-ring search (per 68d4a1/91ad72); resume immediately if Eric Lu's RSA-260 method or authenticated RSA DSP generation provenance is published.
