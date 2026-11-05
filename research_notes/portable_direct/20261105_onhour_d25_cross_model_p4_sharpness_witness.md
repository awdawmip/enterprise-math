# D25 / LIFT — sharpness witness for the frozen signed 216–2304 p³ transport

**2026-11-05.** Author-only portable scientific result. **EXACT FINITE COUNTEREXAMPLE TO UNIFORM p⁴ EXTENSION / UNREVIEWED / NOT_ADMITTED.** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Native original-class p373 H0/B0 remains NOT_RUN under #1559.

## Target and discriminating question

Existing Source-aligned exact rational identity `(W_p-p)/p²=Delta_p-R_p` (under the original Clausen cutoff and UR) connects the frozen parent target to the weighted 216 sum at modulus p³. The existing signed 216/2304 author notes additionally study `W_p-V_p` at modulus p³, consuming the already published 2304 congruence of Guo–Zudilin. This unit asks a strictly narrower, falsifiable question: **can the uniform cross-model statement be strengthened to modulus p⁴ without an additional term?**

Use only original rational sums (all denominators p-units for p>3):

```text
W_p = Σ[k=0..p-1] (6k+1)*binom(2k,k)^2*binom(3k,k)/216^k
V_p = Σ[k=0..p-1] (8k+1)*binom(2k,k)^2*binom(4k,2k)/2304^k
```

## Exact p=13 certificate and theorem scope

Calculate in Z/(13⁴), with 13⁴=28561, from the original rational coefficients:

`W_13=19786`, `V_13=24180`, so `W_13-V_13=24167=11·13³ (mod 13⁴)`.

Hence `v_13(W_13-V_13)=3`. This **proves** the universal strengthening
`W_p ≡ V_p (mod p⁴)` for every p≡13 or 19 (mod 24) is false. The statement `W_p ≡ V_p (mod p³)` for every target prime is unaffected and remains the live proof obligation; a finite exact counterexample to its p⁴ strengthening is not itself a proof of p³ for all primes.

Keep both original half truncations and the weighted upper shells, with `X_shell=X_full-X_half`. At p=13 the original signed p⁴ residues are `W_half=24687`, `V_half=4407`, `W_shell=23660`, `V_shell=19773=9·13³`. The 2304 upper shell vanishes mod p³ but **does not** vanish mod p⁴. Consequently, a p⁴-level lift of the previously proved T_B=0 mod p cannot discard that shell. This is a different, separately observed source boundary, not a replacement for the frozen p³ interface.

## Source-preserving independent arithmetic

Two explicit integer algorithms are run by `d25_cross_model_p4_sharpness_checker_20261105.mjs`: (1) literal binomial coefficients and modular inverse powers; (2) independent hypergeometric-term recurrence. Their unweighted term updates are

`A_{k+1}/A_k = (2k+1)(3k+1)(3k+2) / [36(k+1)³]`

`B_{k+1}/B_k = (2k+1)(4k+1)(4k+3) / [288(k+1)³]`.

For k<p all (k+1) in used updates are units mod p⁴; no floating point and no p-division are performed. Both independent original sums and their half/full subdivisions must match exactly modulo p⁴. This is the executed output:

| p | W mod p⁴ | V mod p⁴ | (W−V)/p³ mod p | V_upper/p³ mod p |
|---:|---:|---:|---:|---:|
| 13 | 19786 | 24180 | 11 | 9 |
| 19 | 82327 | 41173 | 6 | 3 |
| 139 | 190679088 | 281990134 | 105 | 119 |
| 373 | 11832087049 | 5916043711 | 114 | 353 |

All four cases use the original target residue classes; p=13 alone supplies the exact counterexample. p373 is a second, original-sum **portable arithmetic** observation, not the native divided-power `[X]U` experiment.

## BRC and next frontier

**BRC=COMPOSE_APPLIED:** labeled residue classes p≡13,19 mod24; separate signed 216/2304 coefficient branches; half and upper shells; explicit p-adic valuation; final observer W−V/p³ retained. Replacing the signed pair by a positive sum, dropping B's shell at p⁴, or treating p373 ordinary sums as native Frobenius would lose required information.

The **next primary scientific unit remains** the all-target p³ cancellation from the accepted source port:
`D_center + S2_lower + (v_N/2^N) J_n = 0 (mod p)`.
The new witness prevents an unnecessarily stronger p⁴ hypothesis from entering a candidate terminal WZ transformation. Exact original-class fixed-373 H0/B0 `[X]U mod139129`, rank, semilinear Frobenius direction, normalization eta, signed kappa and independent reproduction remain PENDING_OWNER at issue #1559. This result does not substitute for that experimental acceptance.

Source/proof scope: finite exact integer certificate, no new universal supercongruence proof, no Source native CLAIM/run/checkpoint or mathematical acceptance attributed to this note. Prior accepted CM0/UR and previously published upper-jet/shell lemmas are **consumed, not recredited**.
