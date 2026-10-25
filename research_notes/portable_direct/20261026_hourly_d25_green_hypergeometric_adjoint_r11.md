# D25/LIFT — hypergeometric Green kernel, adjoint duality, and nonvanishing Abel residue

**Date:** 2026-10-26. **Parent Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. **Publication:** `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Status:** `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`. These are finite-field algebraic results on the corrected Clausen middle-rank port; not a native Source checkpoint, not a Result/review, not the original CM experiment, and not the all-prime D25/LIFT proof.

**Consumed predecessor:** `research_notes/portable_direct/20261026_hourly_d25_middle_rank_factorial_wz_kernel.md` at Git commit `0e8eda0b046aafd500c082fab9f1e22e3d8e6451`, particularly its Theorems E/F. Its factorial identities and signed middle-rank formula are inputs, **not** newly credited research.

## Precise arithmetic object

Let `p=6m+1 >= 7` be prime, and work in `F_p`. Put `L=m+1`, `U=2m`. Use the *corrected denominator* Jacobi/Clausen Taylor source coefficients

```
a_j = (-1)^(m+j+1) m! (j-m-1)! (2m)! / ((2m-j)! (j!)^2),  L <= j <= U,
h_l = 2 m! (2m)! ((l-1)!)^2 / ((l+m)! (l+2m)!),        1 <= l <= U.
```

All displayed factorial denominators and factors of 2, 3, 6 and 216 are units modulo p. Define signed rank carriers

```
g_l = 2^l h_l,  v_j = 2^(-j) a_j (L <= j <= U), v_j=0 outside [L,U],
K_j = sum_{l=1}^j (6(j-l)+1) g_l, K_0=0.
```

The already-established middle-rank observer is precisely

[
\boxed{\; S_p:={1\over p}\bigl({Q_p\over p^2}\bigr)_{\!\mathrm{middle}}
       =-{1\over216}\sum_{j=L}^{U}v_jK_j\quad (\bmod p).\;}\tag{1}
]

Here `Q_p` remains the **original ordered signed** Clausen reflection tail. Equation (1) is only the prior finite-field middle-port identity; no identification with the whole CM target is assumed.

## Theorem G — exact causal Green and hypergeometric port (new)

Use the rational lift of `g` defined by the same initial value and ratio,

[
g_1={4\over(m+1)(2m+1)},\qquad
{g_{j+1}\over g_j}={2j^2\over(j+m+1)(j+2m+1)}.\tag{2}
]

For a formal variable `z`, introduce

[
G(z)=\sum_{j\ge1}g_jz^j,\qquad K(z)=\sum_{j\ge1}K_jz^j.
]

Then, *over* `Q(m)[[z]]` (and coefficientwise mod p up to degree U),

[
\boxed{G(z)=\frac{4z}{(m+1)(2m+1)}
{}_3F_2\!\left(\begin{matrix}1,1,1\\m+2,2m+2\end{matrix};2z\right),}
\tag{3}
]

[
\boxed{(1-z)^2K(z)=(1+5z)G(z).}\tag{4}
]

Writing `theta=z d/dz`, the source sequence satisfies the exact third-order homogeneous hypergeometric differential equation

[
\boxed{\bigl[(\theta-1)(\theta+m)(\theta+2m)-2z\theta^3\bigr]G(z)=0.}\tag{5}
]

Consequently the *signed rank convolution* itself has the explicit gauge-conjugated equation

[
\boxed{
\bigl[(\theta-1)(\theta+m)(\theta+2m)-2z\theta^3\bigr]
\left(\frac{(1-z)^2}{1+5z}K(z)\right)=0.}\tag{6}
]

These equations identify a concrete holonomic interface for creative telescoping; (6) does not by itself certify the all-target-prime D25 congruence.

**Proof.** From (2),

[
g_{n+1}=g_1\,{2^n(n!)^2\over(m+2)_n(2m+2)_n}.
]

The defining coefficient of `{}_3F_2(1,1,1;m+2,2m+2;2z)` is `2^n(n!)^2/((m+2)_n(2m+2)_n)`, proving (3). The convolution kernel `6r+1` has generating series

[
\sum_{r\ge0}(6r+1)z^r=\frac{1+5z}{(1-z)^2},
]

which proves (4). The standard hypergeometric coefficient recurrence yields
`[theta(theta+m+1)(theta+2m+1)-2z(theta+1)^3]({}_3F_2)=0`.
Multiplication by `z` shifts `theta` to `theta-1`, yielding (5); substitute (4) for (6). For fixed prime p, only the coefficients `1 <= j <= U` are identified with the **original** corrected Taylor source. Rational continuation past that range is an algebraic aid, not a Source/CM assertion. QED.

Equivalently, for `2<=j<=U`, the coefficientwise, denominator-safe recurrence is

[
\boxed{K_j-2K_{j-1}+K_{j-2}=g_j+5g_{j-1}.}\tag{7}
]

Thus two cumulative moments in the predecessor's Theorem F can be replaced by the scalar sequence `K` with exact finite-memory source forcing, without discarding the signed rank information.

## Theorem G' — adjoint/backward WZ entry (new)

Put `q_{U+1}=q_{U+2}=0` and for `j=U,U-1,...,1` define

[
\boxed{q_j=2q_{j+1}-q_{j+2}+v_j+5v_{j+1}.}\tag{8}
]

Then

[
q_\ell=\sum_{j=\max(L,\ell)}^U(6(j-\ell)+1)v_j
quad\text{and}\quad
\boxed{S_p=-{1\over216}\sum_{\ell=1}^Ug_\ell q_\ell.}\tag{9}
]

**Proof.** Equations (8) and terminal data solve the backward second-difference equation whose Green kernel is `6r+1`. Interchanging the finite signed double sum in (1) gives (9) exactly. This is a genuinely two-sided observer pairing: the forward `K` carries `g`, and the backward `q` carries `v`, with no absolute-value or support projection. QED.

## Theorem H — outer-rank quadratic antidifference and surviving residual (new)

The corrected middle-jet outer coefficients obey

[
{v_{j+1}\over v_j}={(j-m)(j-2m)\over2(j+1)^2}\quad (L\le j<U).
]

Extend `v_{U+1}=0`, and let `B_j=j^2v_j`, `W_j=j^2+3mj-2m^2`. Then

[
\boxed{B_{j+1}-B_j=-\tfrac12 W_jv_j,}\tag{10}
]
and therefore
[
\boxed{\sum_{j=L}^UW_jv_j=2L^2v_L.}\tag{11}
]

Multiplying by the *actual future observer* `K_j` and applying finite Abel summation gives the stronger, source-faithful identity

[
\boxed{
\sum_{j=L}^UW_jv_jK_j=
2L^2v_LK_L+
2\sum_{j=L+1}^U j^2v_j(K_j-K_{j-1}).
}\tag{12}
]

The second term is an **explicit signed bulk residual**; it cannot be deleted merely because the unweighted sum (11) telescopes.

**Proof.** The ratio gives
`B_(j+1)=((j-m)(j-2m)/2) v_j`, so subtraction yields (10). The factor `(U-2m)` makes `B_(U+1)=0` and summing proves (11). For (12), sum `-2(B_(j+1)-B_j)K_j` by parts, keeping both the lower boundary and the change in `K`. QED.

**Exact information-loss witness.** For `p=13,m=2,L=3,U=4`,

```
(g_1,g_2,g_3,g_4)=(2,11,4,8) mod 13
(v_3,v_4)=(11,9) mod 13
(K_3,K_4)=(3,9) mod 13
left side of (12) = 8 mod 13
boundary term = 9 mod 13
bulk residual = 12 mod 13 (nonzero)
```

Thus even a correct one-rank WZ antidifference is **not** an endpoint-only certificate after coupling to the original signed reflection observer. This witness is scoped to equation (12), not a disproof of any different combined Clausen/CM telescoper.

## Independent exact computation and scope

The accompanying stdlib verifier `20261026_hourly_d25_green_hypergeometric_adjoint_r11_check.py` checks factorial vs recurrence `h`, forward Green vs direct inner double sum, coefficientwise hypergeometric operator, backward Green vs direct dual sum, outer-rank ratio/quadratic antidifference, Abel residual, and equality of all three middle-rank observers. **80 primes** `p=6m+1, 7<=p<=997` passed. Sample middle-port residues:
`p=7 -> 4; 13 -> 2; 19 -> 2; 31 -> 9; 373 -> 157; 997 -> 550`.
A mathematical universal statement rests on the algebraic proofs above, not on finite tests; this is author verification only.

**BRC:** `COMPOSE_APPLIED` on the finite signed/source-labeled rank carrier `(a_j,h_l,v_j,g_l,K_j,q_l)`, with the exact future contraction `S_p` and the Abel residual preserved. The Green quotient is proved within the specified observer and precision; it does not promote positive-weight BRC to cancellation, does not establish a native six-axis transfer and does not change P000.

## Continuation and control separation

**Completed portable units:** (i) hypergeometric/third-order Green port with explicit adjoint recurrence; (ii) outer middle-jet quadratic telescope with nonzero signed Abel residue and 80-prime author verification. **Do not recredit** the predecessor factorial identities or the earlier corrected `p^4` bridge.

**Exact next mathematics:** seek an operator syzygy/creative-telescoping certificate linking (6), the outer middle-jet ratio, and the full corrected Clausen differential operator at `z=1/2`; use both (9) and the obstruction/residual (12). Any reduction must keep the original sign, boundary, denominator correction and unchanged source pin. The hard all-target-prime congruence and authentic same-class `H_0/B_0`, `[X]U mod p^2`, Frobenius normalization and `kappa` mapping remain unresolved; native CM remains `NOT_RUN`.

**Control:** one fresh direct Gateway D25 `em_control_continuation` read this turn failed at `INVALID_ARGUMENT / CONTROL_QUOTA` (no successful packet). The earlier cross-epoch claimant/checkpoint predecessor mismatch remains a *previously sourced* support issue, not reverified as repaired. No live winning claim, authorized open/resume, native checkpoint, independent review, session transition, activity registration, or frozen Result is claimed for this portable work. Research lane logical ID remains as declared `chatgpt-research-hourly-enterprise-math-20260923`; maintenance lane `chatgpt-hourly-enterprise-math-20260921` is not used for role-bound operations. `REGISTER_PENDING / NATIVE_ADMISSION_PENDING` until current Source permits lawful bound continuation. Scheduler, notifications and frozen source pin were not changed.
