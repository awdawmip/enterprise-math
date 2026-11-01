# D25/LIFT GH-96 — reflected-tail stationary root and nonliftable p-adic cancellation

Date: 2026-10-29. Author context: TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`. Classification: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` / D25/LIFT/JT2 stays OPEN. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. This is not a Source CLAIM, authorized run, checkpoint, Result or independent review.

## Source-labelled definitions

Reuse GH-93 exact p-local adjoint lift and GH-95 reflected-tail exception, preserving the earlier author-only evidence status. For prime `p=4d+3>=7` let `R=Z_(p)`; distinguish the original coefficients `c_i` from reflected coefficients `h_j`:
`h_0=1`, `h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)]`, `0<=j<d`.
With `theta=z d/dz`, define `U_d(z)=sum_(j=0)^d h_j z^j`,
`H_d=(8theta+5)U_d`, and
`R_p(z)=sum_(j=0)^d (8j+5)h_j z^(d+1+j)/(d+1+j)`.
Every denominator is a p-local unit. Here `H_d` denotes the reflected Laurent observer, **not** the elliptic Hasse invariant; `R_p` is not the original GH-3 target `T=(8theta+1)S`.

## Theorem GH-96a: stationary root and nonliftability

**Unconditional over the stated coefficient definitions:**
`theta R_p=z^(d+1)H_d` and `R_p'=z^d H_d`, exactly over `Z_(p)[z]`.
If `a in F_p^*` satisfies `H_d(a)=0` and `H_d'(a)!=0`, then
`R_p'(a)=0`, `R_p''(a)=a^d H_d'(a)!=0`.
Hence `R_p(a)=0` iff `a` is a root of multiplicity **exactly two** of `R_p mod p`. This is the reflected primitive's critical-height condition, not an original-source target condition.

If the integer lift `a0` has `R_p(a0)=p*u mod p^2`, with `u!=0 mod p`, then `R_p(a0+p*t)=p*u mod p^2` for **every** integer `t`, because `R_p'(a0)=0 mod p). Therefore the mod-p double root cannot lift to any root modulo `p^2` above `a`, even when `H_d` has its ordinary unique Hensel root there.

Proof: differentiate the finite sum termwise and apply the second derivative test; apply Taylor's formula modulo `p^2`. No CM identity, any unproved GH-3 vanishing, or division by a vanishing observer is used.

## Theorem GH-96b: sharp valuation filtration of the GH-93 correction

For GH-93's two-source signed concomitants, write `Delta=W-W_naive` and original terminal coefficient `c_d in Z_(p)^*`. GH-93's exact p-local source identity says
`Delta=c_d(-3p/2+3p^2/4-p^3/8)*R_p - p^3*h_d*(2p+7)*M_p/8`,
where `M_p` is the distinct original-source primitive. At any p-local specialization (especially `z=9`):
- If `v_p(R_p)=0`, then **`v_p(Delta)=1`**.
- If `v_p(R_p)=1`, then **`v_p(Delta)=2`**.
- If `v_p(R_p)>=2`, then **`v_p(Delta)>=3`**, with possible higher-order cancellations not classified.

Proof: the coefficient multiplying `R_p` has exact p-valuation 1 (`p>=7`, `c_d` a unit, `-3/2` a unit), while the distinct second term has valuation at least 3. This strengthens GH-95's mod-`p^2` equivalence by one precise digit, retaining original/reflected provenance. It **does not** imply `T_(p,9)=0 mod p^2`.

## Independently computed p=3347 witness

For `p=3347`, `d=836`, `p^2=11202409`, `p^3=37494462923`, the companion program evaluates all source recurrences and two independent concomitant reconstructions using integer modular arithmetic:

| Quantity | Exact modular value |
|---|---:|
| `c_d mod p`, `h_d mod p` | `2034`, `1200` |
| `R_p(9) mod p^2` | `3969542 = 3347*1186` |
| `H_d(9) mod p^2` | `9863609 = 3347*2947` |
| `H_d'(9) mod p`, `theta H_d(9) mod p` | `299`, `2691` |
| `R_p'(9) mod p`, `R_p''(9) mod p` | `0`, `2331` |
| Unique `H_d` root modulo `p^2` above 9 | `9+3347*2117=7085608` |
| `H_d(7085608) mod p^2` | `0` |
| `R_p(7085608) mod p^2` | `3969542` (nonzero) |
| `W(9) mod p^3` | `15038887963` |
| `W_naive(9) mod p^3` | `19284600974` |
| `Delta(9) mod p^3` | `33248749912=3347^2*2968` |

The unique reflected-`H` root shift is `t=-2947/299=2117 mod3347`. The independently evaluated `W` uses ordered GH-84 concomitants and source jets, while `W_naive` uses a separate original/reflected double convolution. Their difference satisfies the GH-93 correction modulo `p^3`. Thus `v_p(Delta(9))=2` **exactly**: the exceptional second-digit agreement fails at the third digit.

The p-adic second-jet identity
`R_p(9+pt) = R_p(9)+pt R_p'(9)+(pt)^2 R_p''(9)/2 (mod p^3)`
also passed a direct check at `t=2117`: `R_p(9) mod p^3=24279589845`, `R_p'(9)/p mod p=2098`, `R_p''(9)/2 mod p=2839`, `t*2098+t^2*2839=1672 mod3347`, and `R_p(7085608) mod p^3=5515554770`. The original `T_(3347,9)` remains `4659024 != 0 mod3347^2` by the separately labelled GH-95 original-source computation.

## Validation, BRC and continuation

Executed local Python standard-library exact modular checker `d25_gh96_stationary_tail_padic_obstruction_check.py` (SHA256 of executed file `8aa722eefeb47086d8c23fb777096f09cff8c16d8027f81af06b01fe01c2696f`), with both `PASS_GH96_INDEPENDENT_SOURCE_RECURRENCE_AND_OBSERVERS` and `PASS_GH96_DOUBLE_MODP_ROOT_NONLIFTABILITY_AND_EXACT_P2_DEFECT`. Exact arithmetic checks a stated finite witness; the universal assertions are deduced algebraically as above, conditional only on explicitly named GH-93 for the `Delta` law. No native experiment or formal review was performed.

BRC decision `COMPOSE_APPLIED` to existing two-source p-adic signed-jet carrier. Population `(p, original index i, reflected index j, z)`; operations ordered convolution, theta differentiation, modular lifting; observers labelled `T,R,H,H',W-W_naive` and p-valuations. A mod-p critical zero and mod-`p^2` signed correction agreement erase a nonzero third-digit residual. These are external arithmetic charts; P000's six native axes, native 120° right angle and separate time remain unchanged.

**Next exact question:** identify a finite-field trace, character-sum or noncircular WZ boundary that predicts `R_p(9) mod p` zero *without scanning*, and explain the isolated prime 3347 at its precise source observer. Separately use GH-92's signed eigenport to prove original `T_(p,9)=0 mod p`, without transferring the reflected-root property to the original source. GH-83 Laurent `B_0L`, GH-20/21 second-digit moments, W/S, Hasse ports, R23/R36 and native p=373 remain distinct. Current actual task session/claim/run/request and predecessor data must be recovered canonically under #1558, not inferred from this portable note or moved into the maintenance conversation.