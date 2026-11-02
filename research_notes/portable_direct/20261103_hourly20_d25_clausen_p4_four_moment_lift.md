# D25 | Four-moment finite Clausen lift one precision digit beyond H4

2026-11-03, Asia/Hong_Kong. **AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Logical Research lane `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance and on-hour lanes. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Frozen mother `Delta_p-R_p=0 (mod p)` for `p mod24 in {13,19}` remains open.

## Exact source and new observer

For every prime `p=6r+1>=7`, work in `Z_(p)`, put `theta=z d/dz`, `z0=1/2`, and define

`c_k=(1/6)_k(1/3)_k/(k!)^2`, `G_p(z)=sum_{k=0}^{p-1}c_k z^k`;

`a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3`, `F_p(z)=sum_{k=0}^{p-1}a_k z^k`.

The exact formal Clausen identity supplies `[z^n]G_infty(z)^2=a_n` for `n<p`. Therefore the finite polynomial difference is precisely

`D_p(z)=F_p(z)-G_p(z)^2=-sum_{0<=i,j<p, i+j>=p} c_i c_j z^(i+j)`.

The inherited H4 result evaluated `([(1+6theta)D_p](1/2))/p^2` modulo `p`. The **new** observer is its next precision digit:

`E_p^[2]=([(1+6theta)D_p](1/2))/p^2 (mod p^2)`.

## L1 — General p^2 high-edge reflection

Define `U_p=c_(p-1)/p^2` (a p-unit, retained **mod p^2**),

`A_s=(s!)^2/[(11/6)_s(5/3)_s]` and

`H_s=sum_{t=0}^{s-1}(1/(t+11/6)+1/(t+5/3)-2/(t+1))`, with `H_0=0`.

All stated denominators are p-units for `0<=s<=2r-1`. Then for all these `s`:

`c_(p-1-s)/p^2 = U_p A_s (1+p H_s) (mod p^2)`. **[L1, proved]**

Proof: the exact backward quotient is `c_(n-1)/c_n=n^2/[(n-5/6)(n-2/3)]`. At `n=p-1-t`, it is

`(t+1)^2/[(t+11/6)(t+5/3)] * (1-p/(t+1))^2 /[(1-p/(t+11/6))(1-p/(t+5/3))]`.

Expand the last factor modulo `p^2`, and multiply the `s` ratios. The inherited U1 theorem at EM commit `e3e3e054b2abd05a585a950a32ce6544f405b057` supplies `U_p=1/10 (mod p)`, but **not** its new `p^2` digit.

## L2 — Four-prefix complete reconstruction

For `1<=i<=2r`, define

`Lambda_i=sum_{s<i}2^s A_s`, `Gamma_i=sum_{s<i}s 2^s A_s`,

`Lhat_i=sum_{s<i}2^s A_s H_s`, `Ghat_i=sum_{s<i}s 2^s A_s H_s`,

all modulo `p^2`. Put `B_i=(6i-5)Lambda_i-6Gamma_i`, `K_i=(6i-5)Lhat_i-6Ghat_i`. Then

`E_p^[2] = -2 U_p 2^(-(p-1)) sum_{i=1}^{2r} c_i 2^(-i)[ B_i + p(K_i+6Lambda_i)] (mod p^2)`. **[L2, proved for all p=6r+1>=7]**

Proof: `v_p(c_i)` is exactly `0,1,2` on `[0,r],[r+1,2r],[2r+1,p-1]`. Every pair `i+j>=p` includes one high index because `4r<p`. High/high pairs have valuation `>=4` and hence vanish in `D_p/p^2 (mod p^2)`. The other ordered pairs occur twice and are precisely `1<=i<=2r`, `j=p-1-s`, `0<=s<i`. Their original Euler weight is `6(i+j)+1=(6i-5)-6s+6p` and `2^(-(i+j))=2^(-i)2^(-(p-1))2^s`. Substitute L1 and collect `s^0,s^1,H_s,s H_s` plus the `+6p` source. This proves L2 without collapsing any unordered or signed source pair.

Modulo `p`, the mid band and new corrections vanish, `c_i=binom(r,i)binom(2r,i)` for `i<=r`, `U_p=1/10`, `2^(-(p-1))=1`; L2 reduces **exactly** to inherited H4.

## L3 — Typed source ports and strict precision-loss witness

With common factor `T=-2U_p 2^(-(p-1))`, L2 splits into four `mod p^2` ports:

`P_LH=T sum_{i=1}^r c_i2^(-i)B_i`;

`P_MH=T sum_{i=r+1}^{2r} c_i2^(-i)B_i`;

`P_H=T p sum_{i=1}^r c_i2^(-i)K_i`;

`P_W=T p sum_{i=1}^r c_i2^(-i)6Lambda_i`.

These exhaust `E_p^[2]`. The low/high port itself retains the full p^2 unit digits of `c_i,U_p` and the factor `2^(-(p-1))`. The mid/high, reflected-harmonic, and original Euler `6p` correction ports are separately labeled.

The exact integer certificate at `p=373` is

`U_373=63895=112+171*373 (mod 139129)`;

`(P_LH,P_MH,P_H,P_W)=(130727,80568,18277,121971) (mod 139129)`;

`E_373^[2]=73285=177+196*373 (mod 139129)`;

`E_373^[2]-P_LH=81687=219*373 (mod 139129)`.

Thus the lifted first (low/high) port alone loses a provably nonzero exact signed contribution to this specified observation. At `p=13`, `E_13^[2]=65=5*13 (mod 169)`, despite its original leading digit `E_13=0 (mod 13)`.

## Exact verification, scope and continuation

An actually executed standard-library Python checker computes the original independent 3F2 and 2F1 finite coefficient recurrences modulo `p^4`, forms `[(1+6theta)(F-G^2)](1/2)`, divides by `p^2`, and independently reconstructs the same value from four prefixes and high-edge reflection. **148 of 148 primes** `7<=p<=2000, p=1(mod 6)` passed direct-vs-reconstructed, individual high-edge spot checks, and all four-port sum assertions. Reproducible full checker, results JSON, execution log and SHA256 manifest are included in the current-turn archive `enterprise_math_D25_clausen_p4_four_moments_20261103.zip`; these finite checks are supplementary to the algebraic proof. Both direct scalar and prefix methods use `O(p)` modular operations, with p-adic bit complexity accounted separately.

BRC status: **COMPOSE_APPLIED**, retaining ordered index-pair source, three valuation bands, four exact prefix moments, the signed Euler/Fermat observers, and precision-typed projection proof. No native H0/B0 computation or native X6 interpretation is asserted.

**Next smallest unfinished scientific unit:** derive the `mod p^3` version of this defect using high/high pairs of valuation 4, one additional low/high unit digit and one extra mid/high unit digit; compare with the previously derived Gauss/Hensel third-carry mechanisms. In parallel, the universal target-class `12*j*h=1(mod p)` and the original frozen Delta-R relation remain mathematically open. Native p=373 H0/B0 support continues under #1559.

**Control boundary read this run:** Gateway 0.6.11: `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, active-job quota `5/5`. Same-lane #6637 is earlier successful read-only recovery; #6638 is definitively failed continuation; both receipts were inspected, neither replayed. Session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` is **historical recovery evidence only**, not current ownership. Two neutral staging archives are protected. No new native CLAIM, authorized OPEN, Source checkpoint, freeze, review or admission. Existing control-support owner path is #1558.
