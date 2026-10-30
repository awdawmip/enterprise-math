# D25 / SECOND-DIGIT-LIFT — Gauss cutoff source transport in the second Hensel-root digit

2026-10-30 19:00+08:00 · **AUTHOR-SIDE / EXACT CONDITIONAL-INPUT THEOREM / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING**.

Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923`, distinct from the maintenance lane `chatgpt-hourly-enterprise-math-20260921`. Parent: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**. P000/ACTIVE residual-faithful worldview unchanged. This note does not claim native Source claim/Result/review or original H0/B0 experiment.

## Consumed, not re-proved

The 2026-10-26 source-port proof (commit `2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be`) establishes the exact original Clausen scalar port, including the frozen signed reflected cutoff `R_p`. The 2026-10-30 Gauss–Hensel note (commit `9b7f98937214f7dcf2f125dd1c0d773c4b036126`) establishes the simple Hensel zero of the **full** Gauss truncation at `z_0=1/2`, its signed root-residual transport `6g^2(d-d^*)/p`, and the all-prime equivalence to the original LIFT under existing frozen CM0/UR input. The earlier two-factor cutoff factorial formula is reused, not credited as a new theorem. This turn only proves the missing **low/full Hensel-root comparison** and executes the independently checkable source-digit certificate.

## Exact objects and coefficients

For each prime `p=6m+1`, `p ≡ 13 or 19 (mod 24)`, work over `Z_(p)`. Define

```text
c_n = (1/6)_n (1/3)_n/(n!)^2,
G_full(z) = sum_{n=0}^{p-1} c_n z^n,
G_low(z)  = sum_{n=0}^{2m} c_n z^n,
T_p(z)    = G_full(z)-G_low(z),
z_0       = 1/2,
g_p       = G_full'(z_0) mod p = G_low'(z_0) mod p != 0.
```

The last nonzero assertion is the **consumed** simple-zero CM0 antecedent. It is not inferred from numerical samples. The two rising factorials each have exactly one p-factor when `2m<n<p`; every `n!` is a p-unit. Therefore

```text
c_n/p^2 ≡ (-1)^m m!(2m)!(n-m-1)!(n-2m-1)!/[18(n!)^2] (mod p),
                  2m+1 <= n <= p-1.
```

The quotient is formed in `Z_(p)` **before** reduction. Define the source-labeled high-tail digit

```text
F_p = T_p(1/2)/p^2 (mod p)
    = [(-1)^m m!(2m)!/18] *
      sum_{n=2m+1}^{p-1} (n-m-1)!(n-2m-1)!/[(n!)^2 2^n] (mod p).    (1)
```

The factor `1/18` is the two separate p-zero factors `p/6` and `p/3`. All denominator factors are p-units. In BRC terms, `F_p` is **not** an unlabelled remainder: the ordered indices `n>2m`, the valuation-2 carrier and its original Gauss source are retained.

## New full-prime cutoff-to-root transport theorem

Let `zeta_full` and `zeta_low` be the respective unique Hensel zeros of `G_full` and `G_low` in `Z_p` satisfying `zeta ≡ z_0 (mod p)`. Define `d_full=(z_0-zeta_full)/p` and `d_low=(z_0-zeta_low)/p`. Then **for every prime in the declared two infinite target classes**,

```text
(zeta_full-zeta_low)/p^2 ≡ -F_p * g_p^(-1) (mod p),                (2)
(d_full-d_low)/p ≡ F_p * g_p^(-1) (mod p).                        (3)
```

**Proof.** Both polynomials have the same mod-p value and mod-p derivative at `z_0`, and `T_p(z)` is pointwise divisible by `p^2` for every `z in Z_p`. By Hensel uniqueness their roots coincide modulo `p^2`. Since `zeta_low-z_0` lies in `pZ_p`, the integral polynomial `T_p/p^2` satisfies
`T_p(zeta_low) ≡ T_p(z_0) ≡ p^2 F_p (mod p^3)`.
Writing `delta=zeta_full-zeta_low in p^2 Z_p`, Taylor expansion gives
`0=G_full(zeta_full) ≡ T_p(zeta_low)+delta*G_full'(zeta_low) ≡ p^2F_p+delta*g_p (mod p^3)`.
The derivative is a unit. Divide by `p^2` and solve, proving (2). The definitions of `d` give (3). This uses no claim about a Frobenius/eta native operator or universal LIFT vanishing.

## Signed original-observer interface and nonzero obstruction

Reuse the original, frozen `d^*=g^{-2}/6+p(R_p g^{-2}/6-g^{-4}/54)` (mod `p^2`) and `6g_p^2(d_full-d^*)/p` from the Gauss–Hensel source. If the **same** target `d^*` is evaluated on `d_low` merely as a formal truncated-coordinate comparator, then its difference from the actual full-coordinate expression is

```text
6g_p^2 * [(d_full-d_low)/p] ≡ 6g_p F_p (mod p).                 (4)
```

Here the full-coordinate term agrees with the original `Delta_p-R_p` by the existing source proof. The **low-coordinate term is not declared an original Delta/R observer**, because the signed Clausen cutoff and original A-model have not been redefined. Equation (4) is a precise correction that must be carried when changing the full Gauss polynomial to the smaller `n<=2m` polynomial at precision `p^3`. Dropping it is not generally observer-safe.

## Executed exact certificates

The standalone checker `d25_onhour_gauss_tail_hensel_transport_20261030.py` was run with Python standard library only, exit zero and terminal marker `PASS_D25_EXACT_GAUSS_TAIL_HENSEL_ROOT_TRANSPORT`. For **all 166 target primes `13<=p<5000`, `p≡13,19 mod24`**, it:
- builds the original `c_n2^{-n}` by p-unit modular recurrence modulo `p^3`;
- computes `F_p` a second time by the independent factorial expression (1);
- finds both actual Hensel roots by Newton digits, evaluates each zero modulo `p^3`, checks (2), (3) and (4);
- preserves source/resolution labels; no floating point or unexecuted test counted.

Exact representative modular data, in order `(p,F_p,g_p,zeta_low,zeta_full,(zeta_full-zeta_low)/p^2,6g_pF_p)`:

```text
( 13,   8,   1,     1801,      449,   5,   9)
( 19,  10,   2,     6603,     4798,  14,   6)
( 37,   8,  11,    31099,    39313,   6,  10)
( 43,   7,  40,    45129,    22941,  31,   3)
(211, 130,  84,  3574446,  8649840, 114, 110)
(373, 252, 215, 33701856, 18815053, 266, 197)
(157,   0, 118,   767809,   767809,   0,   0)
```

The `p=373` full root `18815053 (mod 373^3)` independently agrees with the previous original Gauss–Hensel source. **A crucial negative control is `p=157`: the tail digit vanishes there.** In this checked finite interval it was the only `F_p=0` target, which is *not* a global classification. Thus (4) is an exact signed correction but is not asserted nonzero for every prime.

## Unfinished frontier and authorization

This is a new **conditional-on-consumed-CM0 full-prime algebraic theorem**, not a proof that `Delta_p-R_p=0` for the original infinite target classes. Next precise **mathematical** action: compare the signed high-tail digit `F_p` to the frozen source `R_p` and the lower-root second Hensel digit **without** equating independent source carriers. A full LIFT proof still requires a genuinely new uniform p-adic transformation/CM deformation controlling their joint sum.

The higher-priority **native** requirement remains GitHub issue #1559 (OPEN on 2026-10-30): original-class fixed p373 H0/B0 divided-power `[X]U mod139129`, actual semilinear Frobenius and eta, native module rank, odd signed Green/Hesse, kappa, independent replication. No ordinary scalar tail/root computation supplies that experiment. Owner/executor currently unconfirmed; responsible path is the actual authorized canonical Source owner or designated native compute maintainer, with reproducible original-class raw output and independently checked native operator readback as acceptance.

This client Site on 2026-10-30 reported `research_authority_granted=false`, `write_relay_enabled=false`, `upstream_auth_mode=static_machine_readonly`. Previously recovered same-lane Researcher session `MCP-de3e5bafb24f43f4a5e6285e7601676a` had no own active run/claim or Source authority; neutral archived staging remains separate. No role-bound control write, new CLAIM, Source checkpoint, review or Result is asserted. The author-side GitHub note/checker are evidence only, not the formal Source frontier. Preserve original request IDs and resume lawful native continuation once the Site-scoped backend permission is actually configured. Do not pause the existing research automation.
