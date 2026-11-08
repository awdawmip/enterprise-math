# D25 — Original E3 Frobenius sign versus the quartic-only semilinear port

Date: 2026-11-08 (Asia/Hong_Kong). **TASK_RESEARCH AUTHOR-SIDE: conditional exact theorem / discriminating p=19 counterexample / exact arithmetic 77 target primes ≤2000 / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical onhour research lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance `chatgpt-hourly-enterprise-math-20260921` excluded.

## Actual question and consumed results

The 2026-11-08 author-side two-port result [semilinear conjugate gauge/parity](20261108_onhour_d25_cm_semilinear_conjugate_gauge_parity.md) constructs, from the **original E3 coefficient pair** `A_p B_p^{CM}=1` in `k=F_p[s]/(s²−2)`, a coefficient-compatible, *auxiliary* σ-semilinear matrix `M=[[0,−pσ(A_p)],[B_p^{CM},0]]` over `R₂=(Z/p²)[s]/(s²−2)`. It proves `M σ(M)=−pI`. It also proves the quartic coordinate factor δ satisfies `N(δ)=δσ(δ)=−1` for `p≡13 mod24`, and `N(δ)=+1` for `p≡19 mod24`.

Independently, the existing 2026-10-26 [uniform original E3 geometric q-Frobenius sign theorem](../portable_direct/20261026_onhour_d25_uniform_E3_q_frobenius_sign_CM_three_torsion.md), author-side and not Source-admitted, proves under its existing CM/supersingular identification that the *unmodified* original curve
[
E_3(t): y^2+xy+(t/27)y=x^3,quad t=(2-s)/4,quad s^2=2
]
has geometric `q=p²` Frobenius `π_q=[+p]` for the two target residue classes. It uses its rational order-3 point `(0,0)` to fix the sign. We **consume** these two separate prior source results; do not identify the auxiliary σ-operator with native H0/B0 or claim to reprove geometry.

Question: can a **basis-gauge transformation alone**, or the **specified quartic scalar δ alone**, turn that auxiliary `−p` square into the required `+p` geometric-square sign in *both* target classes?

## Exact sign-compatibility theorem and p=19 falsifier

Let `p>3`, `p≡13 or 19 (mod24)`, and `R₂,σ,M` be as above with `Mσ(M)=−pI mod p²`.

**(1) No gauge can change the square sign.** For any `C∈GL₂(R₂)`, the σ-semilinear basis change `M'=C⁻¹Mσ(C)` satisfies
[
M'σ(M')=C^{-1}Mσ(M)C=-pIpmod{p^2}.
]
This covers diagonal rescalings of the two CM eigenlines. Thus, **if the original geometric identification requires `+pI` in that specific σ-semilinear square**, a basis normalization by itself cannot provide it in either residue class.

**(2) A scalar *operator* twist changes the norm, unlike a gauge.** Let `r∈R₂^×`, interpreted as changing the σ-semilinear operator `Φ_r=rΦ`, not as changing basis. Then
[
(rM)σ(rM)=N(r)(-p)Ipmod{p^2}.
]
Consequently exact sign compatibility modulo `p²` is **equivalent to**
[
oxed{N(ar r)=-1quad	ext{in }mathbb F_p^	imes.}
]
The condition is only on reduction modulo p because the matrix square contains p.

**(3) The already specified quartic factor δ alone passes the sign test only in the 13-class.** The consumed parity formula gives
[
(delta M)σ(delta M)equiv
egin{cases}
+pI,&pequiv13pmod{24},\\
-pI,&pequiv19pmod{24}.
end{cases}
]
For **p=19**, the existing original-E3 coefficient inputs are `A=11+16s`, `B^{CM}=18+17s`, `δ=3s`. In `R₂=(Z/361)[s]/(s²−2)`, the auxiliary matrix has upper entry `152+304s` and lower entry `18+17s`; `Mσ(M)=342I`, and the quartic-only matrix remains `(δM)σ(δM)=342I`, whereas the consumed unmodified geometric sign is `+19I`. **This is an exact counterexample to the specified quartic-only/gauge-only comparison mechanism at p=19, not a counterexample to LIFT/JT2 or to the existence of another geometric transport.**

**(4) An explicit class-dependent *algebraic sign-correcting scalar* exists, with nonunique choices.** Since `N(1+s)=1−2=−1`, define
[
ho_p=egin{cases}
delta_p,&pequiv13pmod{24},\\
(1+s)delta_p,&pequiv19pmod{24}.
end{cases}
]
Then `N(ρ_p)≡−1 modp`, so `(ρ_pM)σ(ρ_pM)=+pI modp²` for both classes. This is an **abstract coefficient-field correction**, not a certified coordinate change or a map of the genuine E3 geometry. All mod-p sign-compatible `r` form the coset `(1+s)ker(N:k^×→F_p^×)`; the kernel has `p+1` elements. Hence even the corrected square sign does not select a unique original-class normalization.

## Exact arithmetic and the next native observer

The runnable [checker](d25_original_e3_sign_compatible_twist_check_20261108.py) computes quadratic-ring multiplication, σ-semilinear matrix squares and class-dependent factors using **integer modular arithmetic**, without floating precision or native simulation. It checks the correction at each of the **77** primes `p≤2000`, `p≡13,19 mod24`, and cross-checks the *actual previously computed original-E3 coefficient pair* at `p=19,373`:

| original E3 coefficient port | p=19 | p=373 |
|---|---:|---:|
| `A_p` | `11+16s` | `349+48s` |
| `B_p^{CM}` | `18+17s` | `131+262s` |
| `δ_p` | `3s` | `269` |
| `ρ_p` | `6+3s` | `269` |
| raw auxiliary square mod p² | `342I=-19I` | `138756I=-373I` |
| quartic-only square mod p² | `342I` | `373I` |
| class-corrected auxiliary square mod p² | `19I` | `373I` |

The checker passed all 77 coefficient-ring sign checks and both original-E3 input cross-checks. The universal theorem is algebraic, not inferred from the finite window.

**BRC typed observer:** retain (original geometric `π_{p²}`, auxiliary σ-semilinear `Φ`, chosen E3 source branch, quartic δ, actual operator scalar twist r, eigenbasis gauge C, and matrix-square sign) as distinct provenance/operations. The scalar norm readout is only a necessary **sign** test for a declared comparison; it cannot identify the native divided-power `[X]U`. The quadratic coefficient ring is an external arithmetic carrier, not a native X6 plane or two-dimensional slice. P000 and ACTIVE worldview unchanged.

## Actual unfinished experiment and handoff

Issue [#1559](https://github.com/awdawmip/enterprise-math/issues/1559) still needs an authorized executor for the **same-original-class p=373 H0/B0 native divided-power [X]U mod 139129**, rank, native operator and σ-direction, η/source normalization, signed odd Hesse/Green κ, original `Δ−R`, plus independent reproducibility (then p=19). Once native source identifies the operator and Frobenius transport, apply the gauge-vs-operator-twist sign discriminator; **do not change original acceptance conditions or count this correction as an execution**.

Parent `Δ_p−R_p=0 modp` / `W_p=p modp³` remains OPEN. No new CLAIM, Result, review or native checkpoint. Existing exact request `onhour11-20261106-1400-exact-research-lane-continuation` retained; read/reconcile on 2026-11-08 returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Local Site phase `CONFIGURED_NOT_LIVE_VERIFIED`; `research_authority_granted=false`. No native role identity or completed upload inferred. Next action: authorized #1559 executor measures authentic original observer and checks actual Frobenius/gauge/twist relation, first p=373, then p=19.
