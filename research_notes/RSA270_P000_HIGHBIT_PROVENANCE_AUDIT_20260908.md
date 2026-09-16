# RSA-270 continuation: reconstruct and split the old P000 prior into documented and statistical components

Status: `RESEARCH NOTE / PROVENANCE REPAIR + EXACT CONDITIONAL INTERVAL / HEURISTIC PRIOR BOUNDARY`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T03:02:00+08:00`  
Parent: PR #1331 salvage of external PR #1330.

No RSA-270 factor is obtained.

## 1. Why this note exists

The external #1330 package repeatedly invoked an undefined/unpinned `P000` prior. The independent salvage had already separated the documented modulo-3 condition from unpinned assumptions. A new 2026 construction-family study makes it possible to identify the origin of the old numerical factor-ratio band with high confidence.

The correct provenance must nevertheless distinguish:

- **documented historical generation metadata**;
- **strong post hoc construction-family signature**;
- **mathematical consequences conditional on the latter**.

## 2. Documented hard metadata: H2

The original RSA Factoring Challenge list states that the decimal-labelled challenge numbers were products of two randomly chosen primes of approximately the same length, both congruent to 2 modulo 3, tested probabilistically, and generated using RSA Data Security's RSA DSP hardware.

Primary archive:

`https://www.ontko.com/pub/rayo/primes/rsa_fact.html`

Thus for RSA-270:

`H2: p ≡ q ≡ 2 (mod3)`

is a documented public generation condition and may be used as a hard premise when explicitly cited.

The archive does **not** specify a random seed, candidate increment schedule, PRNG, exact prime interval, or a top-two-bits rule.

## 3. 2026 statistical construction-family signature: binary prefix 11

A 2026 forensic analysis of 22 solved formal RSA Challenge moduli (44 factors) reports that all retained factors begin with binary prefix `11`. The authors use matched Monte Carlo controls and find the all-11 pattern highly atypical under their size/label baseline.

Source:

`Forensic Construction-Family Signatures in Solved RSA Challenge Moduli: High-Bit Conditioning, Residue Constraints, and Factor-Balance Patterns`, Information 17(9):847 (2026).

Crucially, that paper itself classifies this as a **construction-family signature**. It states that the observed factors cannot distinguish explicit top-bit setting from an equivalent upper-quarter prime interval or a pair-level acceptance rule, and that the surviving historical record does not identify the original RSA DSP source-code path, seed, sieve state, increment strategy or retry history.

Therefore define the statistical/conditional premise

`H11: both RSA-270 prime factors begin with binary prefix 11`.

`H11` is empirically supported by all solved Challenge samples studied, but it is **not documented hard metadata for RSA-270** and must not be silently folded into H2.

## 4. Exact RSA-270 interval under H11

RSA-270 has bit length 895.

The 2026 high-bit observation implies `bitlen(N)=bitlen(p)+bitlen(q)` for a pair whose two mantissas are at least 3/2. With approximately balanced factor allocation and `p<q`, the bit lengths are then

`bitlen(p)=447`, `bitlen(q)=448`.

Binary prefix `11` gives

`3*2^445 <= p < 2^447`,

`3*2^446 <= q < 2^448`.

Combining with `q=N/p` gives the exact conditional p interval

`L=max(3*2^445, ceil(N/(2^448-1)))`,

`U=min(2^447-1, floor(N/(3*2^446)))`.

For RSA-270 this is

`L = 320715617581214341111314865514099764376089683625186303450744913502165637206860039767069510326536326120529070218606479154225002140482006`,

`U = 363419362147803445274661903944002267176820680343659030140745099590319644056698961663095525356881782780381260803133088966767300814307327`.

The interval width is about

`W ~= 2^443.9108`.

Relative to `sqrt(N)`,

`W/sqrt(N) ~= 0.08844777`.

So H11 supplies about

`log2(sqrt(N)/W) ~= 3.4990 bits`

of interval information beyond a full sqrt-scale search interval.

## 5. The old P000 ratio band is exactly the H11 interval

Since `q/p=N/p^2`, the extremal ratio values over `[L,U]` are

`N/U^2 ~= 1.7649891612036819`,

`N/L^2 ~= 2.26630286911909`.

Therefore H11 yields exactly

`1.7649891612... <= q/p <= 2.2663028691...`.

This numerically matches the unexplained old #1330/P000 band

`q/p in [1.765,2.266]`.

Hence the old P000 ratio prior can now be reconstructed as the consequence of an **H11-style high-bit construction assumption**, not of H2 alone.

This is a provenance repair, not a proof that RSA-270 satisfies H11.

## 6. Consequences for old claims

Claims that depend only on H2 remain hard-condition results once sourced to the original Challenge record. Examples include the H2 mod-72 residue fiber and the level-9 `{8,8}` versus `{2,5}` split.

Claims using the ratio band must be relabelled `CONDITIONAL ON H11`, including statements such as:

- the exact numerical `q/p` interval above;
- l=2 being the closest small integer to the V-function vertex throughout that band;
- any numerical bound on `y(2)=|2p-q|` derived from that ratio band;
- any search-window prioritization justified by the same band.

They are useful heuristics/conditional geometry, not unconditional RSA-270 theorems.

## 7. Limited algorithmic value even if H11 is true

The interval narrowing is only about 3.50 bits.

In a partial-factor Coppersmith formulation, if a residue `p mod M` is already known, one can center the remaining arithmetic-progression index inside the conditional interval and apply the standard small-root theorem modulo the unknown divisor p. The relevant unknown-index width scales like `W/M` (or half that after centering), rather than `sqrt(N)/M`.

Thus an exact H11 premise would lower the required recovered low-residue information by only about 3.5 bits, up to constant/centering effects. In a pure ternary tower this corresponds to only a few `log2(3)`-bit lift levels, not a qualitative change from the e≈141 Coppersmith handoff.

Because H11 is statistical rather than documented, no exact new stopping exponent is promoted here. The robust hard-condition cutoff remains the previously proved `2*3^141 > N^(1/4)` scale.

## 8. Generator source audit

A targeted search of surviving RSA DSP / Motorola DSP56000 material found implementation descriptions of large-integer modular arithmetic and RSA acceleration, including the Dusse--Kaliski cryptographic library, but no preserved source establishing the Challenge prime candidate seed, PRNG, increment/sieve path or explicit top-two-bit rule.

The 2026 forensic paper reaches the same source boundary: the high-bit pattern supports a family-level construction restriction but not implementation-level attribution.

Disposition:

`RSA_DSP_EXTRA_GENERATOR_SECRET -> NOT PUBLICLY PINNED / DO NOT USE AS HARD PREMISE`.

## 9. Updated assumption map

Use the following split going forward:

- `H2_DOCUMENTED`: `p,q ≡ 2 mod3` — hard public metadata;
- `H_BALANCE_DOCUMENTED`: primes approximately same length — qualitative public metadata;
- `H11_STATISTICAL`: both factors prefix `11` — strong solved-sample signature, conditional only;
- `H_EXACT_GENERATOR`: seed/PRNG/candidate schedule — unavailable.

This map replaces the opaque `P000 assumed` wording for the RSA-270 salvage line.
