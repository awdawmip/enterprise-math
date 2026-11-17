# R259C — Labelled modular observability and effective p-adic denominator-loss periodicity

Date: 2026-11-18 (Asia/Shanghai). Research status: **AUTHOR_PROVED / EXACT_FINITE_STATE_VERIFICATION / NOT_REVIEWED**. Scientific input remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Inputs and inherited definitions

This result uses only the seven-source positive rational **auxiliary scalar** observer of R257/R258, not a native signed-port or three-dimensional-slice BRC equivalence. For each mask `m=0,...,62`, retain its separate label and source subset `D_m={0} ∪ {i+1: bit_i(m)=1}`. With the R257 coefficient functions and weights, write

`h_(m,k)(s) = W_popcount(m) rho_D^T P_D^k 1`, `k>=0`.

The source inputs and earlier proofs are pinned in R257 at commit `8a0b721455f00e8c5e50ff08831c12fea01c86e4`, R256 at `c7b15b956ec9fb996c5b72eaae06bed14399e234`, and R255B at `6c12b514474d865d3fb8efb940a1b100b14d9208`. Their prime-specific denominator theorems are used only in their stated domains.

## Relation to previously published R259

The earlier R259 research material (independent commit `d789f0e6907aa18a923830bd0036cf19d0d5ef3d`) already derives the much sharper **23-adic first-layer** periodicity bound: for `v_23(t)=-2` the post-transient period divides `12144`, and for `v_23(t)<=-3` it divides `22`. That result remains the preferred efficient 23-adic test. The present supplement gives a **general p-adic depth-r theorem for any prime**, plus independently recomputed *exact minimal full joint-state periods* for R256/R257/R258. It does not supersede that sharper R259 bound.

## Theorem A — exact joint modular observation criterion

Fix a rational parameter `s`, a positive integer `T` such that every scaled characteristic polynomial

`C_m(y)=T^d c_m(y/T) ∈ Z[y]`, `d=|D_m|`,

and a positive integer `J` such that the direct finite bases `H_(m,3),...,H_(m,d+2)` are integers, where `H_(m,k)=J T^k h_(m,k)`. Define `K>0` as the gcd of all these 249 integers. By Cayley–Hamilton, the sequences `q_(m,k)=H_(m,k)/K` are integral for every `k>=3`, and each satisfies the monic recurrence `C_m`. If additionally `K | J T^3` (hence `K | J T^k` for all `k>=3`), set `A_k=J T^k/K`.

Then the exact least common denominator of **all 63 reduced labelled rational outputs** is

`D_k=A_k/gcd(A_k,q_(0,k),...,q_(62,k))`.

In particular, for any prime `p` dividing `A_k`, an extra factor `p` cancels from the proposed common denominator `A_k` **if and only if all 63 labelled residues `q_(m,k) mod p` vanish simultaneously**. A single nonzero labelled residue certifies the full `p` exponent in `A_k`.

*Proof.* Each `H` satisfies `C_m`: substituting `h_k=H_k/(JT^k)` into `c_m` yields the monic integral recurrence with characteristic `C_m`. Its `d` integer starting values ensure integrality for all later indices. The gcd `K` divides the entire recurrence because it divides every starting value. Each output is `q_m/A_k`. Taking the least common multiple of denominators gives the displayed gcd identity by comparing the valuation at each prime. The modular equivalence follows at once. QED.

## Theorem B — effective finite-state periodicity at every fixed p-adic depth

For a prime `p` and integer `r>=1`, consider the ordered concatenation of the 63 recurrence windows

`X_k=((q_(m,k),...,q_(m,k+d_m-1)) mod p^r)_(m=0,...,62)`.

This is an exact deterministic linear transition on `(Z/p^r Z)^249`. Consequently the orbit is eventually periodic, with its first repeated state reached after at most `p^(249r)` distinct states. Both its preperiod and its period are determined by a finite state-orbit enumeration. The all-zero observation set `{k>=3: all_m q_(m,k) ≡0 mod p^r}` is therefore ultimately periodic.

The condition `p^r | A_k` is eventually constant as `v_p(A_k)=v_p(J/K)+k v_p(T)`: it is always false or eventually true. Hence the exact set of horizons at which **at least r powers of p cancel** from `A_k` is ultimately periodic, with an effective description. For `p|T`, the `p^r|A_k` prerequisite holds for all sufficiently large `k`. This asserts periodicity separately at each fixed finite `r`; it does not assert a uniform fixed period for the unbounded full valuation `v_p(gcd(A_k,q_0,...,q_62))`.

*Proof.* One step shifts each mask's length-`d_m` window and appends the integer-recursive next term modulo `p^r`. There are at most `p^(r sum_m d_m)=p^(249r)` states; pigeonhole plus determinism gives a preperiod followed by a cycle. The all-zero test is a function of state, and intersection with the eventually constant divisibility test for `A_k` preserves eventual periodicity. QED.

## R259C independently recomputed full labelled orbit certificates

The attached pure-standard-library script reconstructs `a,b,pi,rho` from exact rational inputs, all 63 characteristic polynomials, the 249 direct integer bases, `J`, and their gcd `K`. It then enumerates the **entire 249-coordinate joint state** modulo each indicated prime, stopping at the first repeated state. Assertions check the printed period, zero set, integrality and source constants.

| Parameter | p | First-repeat preperiod | Exact joint-state period | All-63-zero horizons in one cycle |
|---|---:|---:|---:|---|
| `s=67/169` (R256) | 13 | 0 | **2184** | `k=1093,2185` |
| `s=770/1973` (R257) | 23 | 0 | **528** | none |
| `s=866/2197` (R258) | 23 | 0 | **12144** | none |
| `s=866/2197` (R258) | 13 | 0 | **12** | none |

For R256, the zeros repeat exactly at `k ≡ 1 (mod 1092)` with `k>=3`, confirming the previously identified periodic 13-adic dip. For R257/R258 the full joint-state orbit supplies a second, independent **all-horizon nonvanishing** certificate in addition to the earlier one-mask geometric witnesses. The R258 23-adic joint-state period `12144` is a new finite-state invariant of this labelled observer.

Verification: `R259_exact_modular_observability.py` (Python `fractions.Fraction`, integer modular arithmetic, no floats) emits `R259_verification.json`. Four exact cycles covering `2184+528+12144+12=14868` joint-state observations were exhaustively visited, with all assertions passing. Reproduced locally on 2026-11-18. The SHA-256 of the generated JSON (including trailing newline) is `4672c9d7fbf2e055d94056178b2cdbbe81672eafd9435255a6e674323e134b4f`. Script SHA-256 is `0630a59d6ae90cfbfe48634a87357e9287cffe0081d9d929b81005f202e2dee2`.

## Mathematical scope and next research

The theorem is a general integer-linear-recurrence statement; the computed periods belong to the pinned seven-source rational auxiliary scalar model. Mathematical review is pending. The Source files are independent portable research materials and neither assert a formal CLAIM nor change P000, existing Task ownership, native BRC admission or earlier Result/Review records.

Next: leverage the modular state criterion to find an actual rational parameter with a 23-adic denominator dip, or prove a parameter-class obstruction. Seek provable short orbit bounds via labelled observable quotients rather than the general `p^249` bound. A separate open direction remains the continuous-real 270/403 two-mode approximation threshold.
