# D25 / SECOND-DIGIT-LIFT — Native supersingular slope-parity gate and a 2026 mixed-CM transfer falsifier

Date: 2026-10-27. Original Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). **AUTHOR-SIDE / EXACT CONDITIONAL NO-GO + EXECUTED INDEPENDENT INTEGER CERTIFICATES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED / LIFT_OPEN.**

Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`**, unchanged. This note consumes the already-proved E3 CM operator with square `-6`, signed two-column eigenbasis and prior source relation between the original weighted `W_p` and the D25 observer. The older eigenline-exchange/off-diagonal lemma and the earlier p^4 W counterexamples are **consumed, not credited as new**.

## 1. Prime splitting at the exact D25 target

For each prime `p ≡ 13,19 (mod 24)`, quadratic reciprocity gives

```
                      p≡13     p≡19
(-1/p)                 +1        -1
( 2/p)                 -1        -1
( 3/p)                 +1        -1
(-3/p)                 +1        +1
(-6/p)                 -1        -1
```

Thus these are **split** in `Q(sqrt(-3))` but **inert** in the CM field `Q(sqrt(-6))` of the *original* E3 degree-six endomorphism `vartheta²=-6`. In particular `T²=2` defines the unramified quadratic coefficient field over `Q_p`; `u²=-3` has a solution in `Q_p`, and for `theta=uT`, the unramified conjugation `sigma(T)=-T` sends `theta` to `-theta`. The previously proven signed CM eigenline-exchange result is therefore on the **opposite local splitting branch** from a split `j=0` unit-root construction. This is an exact character statement, not a native Frobenius measurement.

## 2. New exact parity obstruction at the original H0/B0 acceptance gate

**Lemma (rank-one unramified sigma-module parity).** Let `K/Q_p` be unramified quadratic with Frobenius `sigma` of order two, and let `L=K e` be one dimensional. If `F` is invertible sigma-semilinear with `F(e)=a e`, `a∈K×`, then

```
    F²(e) = a sigma(a) e;
    v_p(a sigma(a)) = 2 v_p(a) ∈ 2 Z.
```

Consequently **no rank-one sigma-stable K-isocrystal has `F²=p·unit`**, whose scalar valuation is odd. The proof uses only the valuation group `v_p(K×)=Z` of an unramified field and sigma-invariance of valuations. In particular it remains true when `a` is not integral.

**Conditional original-class consequence.** Suppose an authenticated comparison identifies the *entire* fixed original supersingular E3 crystalline/F-isocrystal with a proposed **rank-one sigma-stable H0/B0 module over the unramified quadratic coefficient field**, and the actual two-step Frobenius has scalar `p·unit` (e.g. the previously documented **conditional** unmodified `[+p]` branch `F²=pI`). These three assumptions are inconsistent. The evaluator must retain the actual rank-two/off-diagonal operator or explicitly reject/retype at least one premise of this comparison. This does **not** prohibit a rank-one object over a ramified extension, a quotient with another Frobenius, or an H0/B0 module not proved to represent the full original crystal.

This sharpens the pre-existing conditional ticket #1559 interface: its ordinary candidate norm `122102 mod 139129` has `122102 mod 373=131≠0`, hence is a p-unit. For any `eta∈K×`, `v_p(Norm(eta)·122102)` is **even**, never one. Therefore a rank-one comparison asserting both `F²=Norm(eta)·122102` and `F²=p·unit` fails already by valuation, before precision or signed Hesse/Green data. This is an **arithmetic acceptance discriminator**, not a native rank verdict; the native `[X]U`, rank and eta remain to be measured.

## 3. Newly located 2026 external result and a precise nontransfer theorem

External prior art: Alex Shvets, *Split-prime supercongruence at the mixed CM point (1/6, 1/3; 1)*, **arXiv:2605.19773, preprint submitted 2026-05-19**, https://arxiv.org/abs/2605.19773 . The abstract states for `A_n^mix=108^n[z^n] _2F1(1/6,1/3;1;z)^3`, for every split prime `p≥7, p≡1 mod3` and `m≥1`:
`A_(mp)^mix ≡ A_m^mix (mod p^4)`. At `m=1`, the polynomial definition gives `A_1^mix=18`, so **under that paper's stated theorem** `A_p^mix≡18 (mod p^4)` at every frozen D25 target prime.

The accepted D24 original weighted first-digit theorem supplies `W_p≡p (mod p²)` on the target classes, hence `W_p≡0 (mod p)`. Since `18` is a p-unit for p≥13, for any `v∈Z_p×`:

```
     v A_p^mix ≡ 18v != 0 ≡ W_p    (mod p).
```

**Transfer no-go (conditional only on the cited preprint's all-prime claim):** No **unit-only** normalization can identify the mixed `j=0` coefficient with the frozen original weighted-`216` observer, even at its first digit. Importing this split-prime p^4 tower to prove supersingular D25 LIFT or to fill the native H0/B0 observation therefore requires an independently proved **nonunit** period/crystalline/derivative transfer, including exact definition, rank and operator orientation. Neither equality of hypergeometric parameters in a nearby `2F1` nor a scalar norm is such a transfer.

Even the most basic *nonunit* candidate `(p/18)A_p^mix`, which equals `p` modulo `p^4` under the cited theorem, disagrees with the original `W_p` at precision `p^4`, by the exact negative witnesses below. This is a bounded explicit falsifier of **that specified candidate bridge**; it does not rule out other sourced nonunit bridges or refute the original p^3 conjecture.

## 4. Actually executed exact certificates and independent algorithms

A new standard-library Python checker `research_notes/portable_direct/d25_cm_split_mixed_transfer_parity_check_20261027.py` was executed in this turn. For every displayed prime, it computed the exact mixed coefficient `A_p^mix` in two genuinely different ways: (i) direct **integer triple convolution** of the scaled `2F1` coefficients and (ii) the independently published **order-two integer recurrence** recorded at OEIS A393983 (https://oeis.org/A393983). The resulting **full integers**, not only modular residues, agreed. The original `W_p` was independently computed by (iii) direct integer binomial terms with `216^{-n}` modulo `p^4` and (iv) its p-unit rational recurrence modulo `p^4`. Each character was computed by Euler's criterion; zero floating-point operations or p-divisible modular denominators.

| p | (-3/p) | (-6/p) | A_p^mix mod p^4 | W_p mod p^4 | (W_p-p)/p^3 mod p |
|--:|--:|--:|--:|--:|--:|
| 13 | +1 | -1 | 18 | 19786 | 9 |
| 19 | +1 | -1 | 18 | 82327 | 12 |
| 37 | +1 | -1 | 18 | 962444 | 19 |
| 43 | +1 | -1 | 18 | 1510676 | 19 |
| 373 | +1 | -1 | 18 | 11832087049 | 228 |

For all five displayed primes, the exact value `(p/18)A_p^mix mod p^4` is `p`; the discrepancy is **nonzero p³**. In particular at the fixed benchmark prime

```
     A_373^mix ≡ 18 (mod 373^4),
     W_373 ≡ 373 + 228·373³ (mod 373^4).
```

The five checks are finite certificates. The cited preprint's **all split primes** assertion is source-attributed, not independently re-proved here. The previously checked 9590-prime `W_p mod p³` study and prior p^4 negative examples are consumed; no new broad scan is claimed.

## 5. BRC carrier/observer, source boundary and canonical continuation

`BRC_REUSE=COMPOSE_APPLIED`: retain the prime branch (`(-3/p),(-6/p),(2/p)`), actual original CM field and p-adic slope, sigma orientation, rank, the labeled original weighted-`216` versus mixed `2F1^3` coefficient model, the normalization factor's valuation and the target modulus. The **smallest sufficient negative-transfer witness** is `(v_p(A_p^mix),v_p(W_p))=(0,≥1)`, plus the exact `p³` residual when the nonunit trial `p/18` is allowed. Dropping the model label, valuation or Frobenius direction would make a false direct-transfer claim. This algebra is an external/classical arithmetic auxiliary, **not** an unlicensed native P000 X6 or three-dimensional-slice theorem.

Research outcome: the unramified rank-one **slope-parity impossibility** is a complete exact conditional theorem; the split-vs-inert character proof is complete; the five-prime precision-boundary certificate is exact; the external all-prime mixed tower is stated with explicit 2026 source provenance and no invented original-E3 correspondence.

**Highest unfinished native unit:** the *unchanged* original-class fixed H0/B0 divided-power `[X]U mod 139129`, actual native module rank, semilinear Frobenius/orientation and eta through two digits, full signed odd Hesse/Green, original kappa, Delta−R, reproducible raw original-class source/version and independent review; existing support **awdawmip/enterprise-math#1559** remains **PENDING_OWNER / NATIVE_NOT_EXECUTED** at this turn's read, with no identified executor. The new exact parity test is an extra **conditional guard**, never a substitute result. Native executor route: accept #1559 via the authorized current Source owner/implementation maintainer, run the same original object, return native raw rank/operator before any rank-one normalization, then test this parity condition only if full crystalline comparison and p-slope premises are authenticated.

Control provenance: old own Research-lane request `research-onhour-20261027-0507-dispatch-r13` at `awdawmip/kimi-query-bridge#6576` had terminal `FAILED / TimeoutExpired`; historical #6575 recovery did not give Source claim. During this turn authenticated gateway 0.6.11 was Site-only, `research_authority_granted=false`, `executor_binding_configured=false`, and `remote_mathematical_compute` disabled. **No own Source CLAIM/open/run verified; no new control mutation or dispatch issued**. This GitHub artifact is author-side durable source, not canonical Source checkpoint or Result; session/claim/run = **NONE_VERIFIED**, new request = **NONE**. Prior source staging stays isolated. The frozen scientific source pin, ownership, scheduler and notification behavior are not modified.

**Next scientific action:** supply/locate the actual native H0/B0 fixed representative and legal executable path through #1559, and return `[X]U mod 139129` with full rank/operator evidence; independently attempt a mathematically legitimate signed/valuation-preserving transport to the original `W_p` only when real native/source data exist. Do not repeat the already completed Clausen triangle or p^4 W scan.
