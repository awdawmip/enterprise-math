# D25 — global CM-sign simplification and direct 216/2304 comparison at the live third digit

Date 2026-11-09 Asia/Hong_Kong. Author-side TASK_RESEARCH; logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. **EXACT CHARACTER/COEFFICIENT REDUCTION + SOURCE-BACKED EQUIVALENCE; FINITE CHECK EXECUTED; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

## I. One additional precise, all-prime character identity

Consume the original D25 E3 CM identification, already proved source-side/author-side: `E3((2-sqrt(2))/4)` has CM by the order of discriminant -24, in imaginary quadratic field `Q(sqrt(-6))`. For every good odd prime p>3, Deuring's CM splitting criterion classifies this model as ordinary exactly when `(-6/p)=+1` and supersingular exactly when `(-6/p)=-1`. The published `sgn` in Babei–Roy–Swisher–Tobin–Tu (2025), Theorem 2.1, is +1 for ordinary and -1 for supersingular. Thus on this **specific original curve**, not an arbitrary CM curve,
```
sgn_p = (-6/p).
```
With lambda=1/2, the published coefficient of p in their numerical conjectural equation (6.8) has the exact elementary character simplification
```
sgn_p * ((1-lambda)/p)
  = (-6/p)*(2/p)
  = (-12/p)
  = (-3/p).
```
This follows from multiplicativity of the Legendre symbol and `4` being a square modulo every p>3. No p-dependent orientation is invented. The residue classes modulo 24 split:
```
class p mod24       1  5  7 11 13 17 19 23
(-6/p), sgn          +  +  +  +  -  -  -  -
(2/p)                +  -  +  -  -  +  -  +
(-3/p), product      +  -  +  -  +  -  +  -
```
Consequently, the full proposed *global* mod-p^3 strengthening in published equation (6.8) reads, with its actual original cutoff and coefficients:
```
W_p  ?=  p*(-3/p)  (mod p^3), p>3.
```
The frozen task only requires the two classes 13/19, where `(-3/p)=+1`. The other classes are contextual predictions, not added formal task scope.

## II. Equivalence to an independently proved 2304 series

Guo and Zudilin, *A q-microscope for supercongruences*, arXiv:1803.01830, prove for every p>3 that the *full* 2304 weighted truncation
```
V_p = sum_{n=0}^{p-1} (8n+1)*binom(4n,2n)*binom(2n,n)^2 / 2304^n
```
satisfies
```
V_p = p*(-3/p) (mod p^3).
```
Thus, **using this established theorem**, the published conjectural d=3, lambda=1/2 assertion has the exact logical equivalence
```
[all good p>3] W_p ?= p*(-3/p) modp^3
  <=> [all good p>3] W_p ?= V_p modp^3.
```
At original target p=13,19 mod24 this is a new *published-source-aligned equivalence of conjectural proof targets*:
```
frozen Delta_p-R_p=0 modp
  <=> W_p=p modp^3
  <=> W_p=V_p modp^3 .
```
The first equivalence is the existing proved frozen signed-cutoff Clausen identity, never a replacement for the original `R_p`. The second uses the Guo–Zudilin proved full-truncation theorem. Neither equivalence proves the unestablished W-to-V congruence. The previously explored stronger author-only mod-p^4 `W_p-2V_p+p*(-3/p)` candidate is an additional, distinctly typed conjecture; do not report it as a published theorem or recredit its scans.

This sharply identifies the missing third digit at a comparison level where both sums have **known exact source definitions and full p-1 truncation**, with a potential common q/WZ transformation route; no geometric coordinate or native `[X]U` can be inferred from the scalar equality alone.

## III. Executed independent cross-model falsification cases

On 2026-11-09 ran exact Python 3 standard-library integers. `W_p` evaluated by the rising-factorial modular recurrence; `V_p` evaluated independently with exact `comb(4n,2n) comb(2n,n)^2` and modular inverse 2304, both at full n=0,...,p-1:
```
p   chi(-3)   W_p modp^3     V_p modp^3     W-V modp^3
5    -1            120             120          0
7    +1              7               7          0
11   -1           1320            1320          0
13   +1             13              13          0
17   -1           4896            4896          0
19   +1             19              19          0
23   -1          12144           12144          0
29   -1          24360           24360          0
31   +1             31              31          0
41   -1          68880           68880          0
47   -1         103776          103776          0
71   -1         357840          357840          0
97   +1             97              97          0
157  +1            157             157          0
163  +1            163             163          0
```
These 15 cases validate the **new direct pairing of two public series representations**, not the unproved general statement. The project had already performed a broader previous p^4 scan, which is consumed rather than counted as fresh discovery. Exact code/results of this small pairing can be reproduced from the two explicitly stated binomial recurrences and Python stdlib (no external native evaluator).

## IV. Current authority, unresolved experiment and next discriminating action

Prior exact source crosswalk and executed separate F6 check: `research_notes/portable_direct/20261109_onhour_d25_published_conjecture_6_8_exact_source_crosswalk.md`. Public sources: https://arxiv.org/abs/2408.08844 (2025 v3, §6 (6.8), Thm.2.1, Sec.1.1) and https://arxiv.org/abs/1803.01830 (Guo–Zudilin original proven 2304 full p-1 supercongruence).

**Current strongest author-only mathematical result:** proved all-prime sign simplification plus published-source target equivalence; 15 finite crosschecks. **Formal D25 LIFT still OPEN**: no all-prime W=V proof and no refutation. The native same-original-class fixed H0/B0 benchmark remains #1559 OPEN / PENDING_OWNER, `[X]U mod139129`, actual module/rank/eta and odd signed Green/Hesse kappa, original Delta-R and independent native reproducer NOT_RUN. Never replace that original-class deliverable by a W/V pair or a synthetic Frobenius.

Historical own Researcher registration `EM-ENTERPRISE-4DEB43` / `MCP-ecbfd1c046864bb3bff1a2e04c87d207` / activity `RA-9553E027FD14223807511263`, but recovery currently returns `SESSION_CAPABILITY_REQUIRED`; no winning CLAIM or run, no Source-native checkpoint, no review. No maintenance-lane credentials were used.

**Next exact scientific discriminant:** for legitimate permitted portable math, attempt an exact finite-sum q/WZ transformation or p-adic factorial valuation identity for `W_p-V_p modp^3`, preserving the full cutoffs; the original p373 H0/B0 executor support still needs actual authorized owner and raw native experiment. No fabricated new Task/claim, acceptance, native benchmark or scheduling change.

BRC/source tags: `COMPOSE_APPLIED` retains full signed characters, two original term families and independent truncation definitions. The quotient `W=V modp^3` is a candidate at this precision, not permission to discard the original `Q/R` or full rank operator.
