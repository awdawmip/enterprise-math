# 自作用近场核的直接认证：4.95 → 4.55，并推进 A3 家族到 0.191

Record-ID: `FINDING-EM-PDE-SELF-NEAR-KERNEL-20260910`
Status: `TESTING / ORDINARY_PROOF_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: 2026-09-10

## 0. Scope

This is a classical normalized three-torus result downstream of unchanged P000. It continues `FINDING-EM-PDE-SYMMETRIZED-SELF-ADVECTION-20260910`. No native-X6 dynamical derivation, optimal-constant claim, historical-priority claim, or arbitrary-data Navier–Stokes theorem is made.

The parent self-advection note proved

`||B(u,u)||_{Hdot^-1/2} <= 4.95 ||u||_{Hdot^1}^2`

by borrowing the ordered two-input near bound `7.4` and using the exact symmetrized far integral. The remaining obvious loss was therefore the near field itself.

## 1. Exact self near kernel

For output `k`, test vector `z in k^perp`, and `p+q=k`, define

`M_z=k z^T+z k^T`.

The diagonal self kernel is

`S_self(k,z)=(1/(4|k|)) sum ||P_p M_z P_q||_F^2/(|p|^2|q|^2)`.

To certify the near region `|p|<6 or |q|<6`, fix an integer output representative `k=(k0,k1,k2)` and choose the rational transverse basis

`t1=(k1,-k0,0)` (or `(1,0,0)` on the axis), `t2=k cross t1`.

For an arbitrary `z in k^perp`, the exact Frobenius numerator admits the rational form

`||P_p M_z P_q||_F^2=(A+D)|z|^2-C(p.z)^2`,

where, with `np=|p|^2`, `nq=|q|^2`, `nk=|k|^2`, `kp=k.p`, `kq=k.q`,

`A=nk-kp^2/np`, `D=nk-kq^2/nq`,

`C=[nk(np+nq)-(kp-kq)^2]/(np nq)`.

Equivalently, after division by the kernel denominator, every matrix entry in the `(t1,t2)` basis is rational. The only irrational factor is `|k|`; the checker replaces it by a rigorous rational lower bound and proves positive definiteness of

`(18/5)|k| G_k - R_k`

using the two diagonal inequalities and the exact determinant.

The union of near legs is counted without duplication: all `p` with `0<|p|<6` are included, and the swapped ordered branch is added only when the companion `q` is outside that near set.

## 2. Finite certification

The exact finite population is:

- 894 near lattice points `0<|p|<6`;
- 571 octahedral output representatives with `0<|k|<17`.

For all representatives, rational positive-definiteness verifies

`boxed: S_self,near(k,z) < 18/5 = 3.6`.

The largest diagonal readout is approximately `3.5465194223` at output class `(0,2,2)`, but this floating value is diagnostic only; acceptance uses exact Fraction arithmetic plus rational lower bounds for `sqrt(|k|^2)`.

The smallest certified relative diagonal and determinant margins are strictly positive and stored in the verification JSON.

## 3. Combine with the analytic far tail

The parent symmetrized-self result already proves, using the structured cube-average identity and the exact continuum integral `3pi^3/16`, that

`S_self,far < 17.09560069415452...`.

Therefore

`sup S_self < 3.6+17.09560069415452... = 20.69560069415452...`.

Since

`20.69560069415452... < (91/20)^2 = 20.7025`,

we obtain the strengthened diagonal estimate

`boxed: ||B(u,u)||_{Hdot^-1/2} <= (91/20)||u||_{Hdot^1}^2`.

Thus the certified quadratic self-advection constant is

`boxed: C_self = 4.55`.

The constant is valid, not claimed optimal.

As in the parent note, real polarization with a free scaling parameter gives the same constant for the symmetric bilinearization

`B_s(f,g)=[B(f,g)+B(g,f)]/2`,

while the genuinely ordered bilinear map still uses its separate constant.

## 4. Trajectory-space feedback constant

For the inherited critical trajectory norm with `c=3nu/4`,

`||B_s(f,g)||_Y <= [(91/20)/sqrt(2c)] ||f||_X||g||_X`.

The nonlinear fixed-point difference satisfies

`B(w,w)-B(z,z)=B_s(w-z,w+z)`.

Hence the feedback constant becomes

`alpha=L*(91/20)/sqrt(2c)`.

The background causal inverse bound `L` is unchanged; the improvement occurs only in the quadratic nonlinear feedback channel.

## 5. Executed A3 endpoint: a/nu = 0.191

Reuse the same rank-three two-shell A3/FCC shape and the same exact two causal responses, with all generated outputs retained. At `nu=1`, endpoint

`a=191/1000`,

the checker certifies the conservative rational bounds

- `L < 5427/1000 = 5.427`;
- `alpha < 2017/100 = 20.17`;
- `eta < 12241/1000000 = 0.012241`.

Choose

`r=123/5000 = 0.0246`.

Exact rational arithmetic gives

- `r-eta-alpha r^2 = 382307/2500000000 >0`;
- `2 alpha r = 248091/250000 <1`;
- equivalently `4 alpha eta <1` with positive margin.

An arbitrary smooth real mean-zero divergence-free initial perturbation of size

`||delta u0||_{Hdot^1/2} <= 3/100000 = 3e-5`

still leaves positive certified margin. By monotonicity of the inherited amplitude bounds, the endpoint controls every `0<=a<=0.191`.

Restoring viscosity scaling yields the restricted family

`boxed: 0<=a/nu<=0.191,  ||delta u0||_{Hdot^1/2}<=3e-5 nu`.

For these data, the inherited all-mode contraction theorem gives the full periodic NS solution in the stated trajectory ball. This is a sufficient family and open neighborhood, not arbitrary-data global regularity and not an optimal endpoint claim.

## 6. BRC interpretation

The improvement comes from retaining the ordered pair genealogy until the future operation is known to be the quadratic diagonal. At that point `p<->q` is a legal symmetric identification. The direct near-field matrix then preserves the common output direction instead of paying twice for two ordered observers.

This is a concrete operation-safe quotient: merging branches is valid for `Q(u)=B(u,u)` and its symmetric polarization, but not for the background ordered linearization.

## 7. Verification

Executed checks:

- exact 894-point near population and 571 output symmetry classes;
- exact rational generalized 2x2 matrix positivity;
- no PDE time sampling;
- inherited analytic all-frequency far tail;
- endpoint full-response defect and contraction inequalities;
- deterministic clean rerun.

Key local verification hashes before publication:

- `certify_selfnear.py`: generated in the current continuation package;
- `selfnear_verification.json`: exact Fraction certificate;
- `certify_family_0191.py`: exact endpoint checker;
- `family_0191_verification.json`: exact contraction margins.

The next mathematical unit is to decide whether the remaining far self kernel can itself be sharpened by keeping the sign of its Frobenius cross term, or whether improving the background causal inverse gives the larger return. Arbitrary-data NS regularity remains open.
