# 双输入无散偏振耦合与共同输出矩阵界

Record-ID: `FINDING-EM-PDE-COUPLED-POLARIZATION-20260910`
Status: `TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: 2026-09-10

## Main result

For the classical normalized three-torus, let both inputs `f,g` be real mean-zero divergence-free fields and `B(f,g)=P((f.grad)g)`.

For each output `k` and test vector `z in k^perp`, retain both input solenoidality constraints before applying Cauchy--Schwarz. This yields the positive operator kernel

`T(k)=sum_(p+q=k) [|p cross k|^2/(|k||p|^4|q|^2)] P_k P_q P_k`.

Then

`||B(f,g)||_{Hdot^-1/2}^2 <= (sup_k lambda_max(T(k))) ||f||_{Hdot^1}^2||g||_{Hdot^1}^2`.

The previous scalar angular kernel satisfies

`S_perp(k)P_k-T(k) = sum weights * (P_k q)(P_k q)^T/|q|^2 >=0`,

so the matrix keeps common-output polarization information that the scalar majorant discards.

## Lattice-to-continuum step

For `k=K e3`, `z=e1`, the far numerator is

`N(x)=|x cross k|^2 |(k-x) cross z|^2`.

Its centered unit-cube average satisfies `N(p)<=int_Qp N(x)dx`; the proof uses the exact positive Laplacian plus the positive fourth-order remainder, not a false pointwise comparison.

The continuum integral is

`int_R3 |x cross k|^2 |(k-x) cross z|^2/(|k||x|^4|k-x|^4) dx = 3 pi^3/8`.

Using exact rational finite matrix checks on 571 octahedral output classes plus analytic all-frequency tails gives

`sup_k lambda_max(T(k)) < 6.45^2`.

Hence

`||B(f,g)||_{Hdot^-1/2(T3)} <= 6.45 ||f||_{Hdot^1}||g||_{Hdot^1}`

for two divergence-free inputs. The constant is effective, not claimed optimal.

For unitary Fourier transform on `R^3`, the corresponding constant is `sqrt(3)/8`.

## A3 consequence

Reusing the existing all-mode inverse and exact causal responses, the specified A3/FCC family is certified for:
- `0<=a/nu<=0.174` with arbitrary smooth divergence-free mean-zero initial perturbation at most `5e-5 nu` in `Hdot^1/2`, trajectory radius `0.020 nu`;
- `0<=a/nu<=0.175` with perturbation at most `2e-6 nu`, trajectory radius `0.0203 nu`.

The second endpoint does not inherit the larger perturbation radius of the first.

## BRC boundary

The gain is not a per-branch projection contraction: `||P_k P_q||` can equal one. The reduction appears only after all branches are constrained to the same output direction. Branch identities, polarization and phase therefore remain live until this common-output operation is formed.

## Verification provenance

Original local verified hashes:
- note: `5e2d348ec1d416b7b41c4c937ca8777a17b4ca9b86a970ccbc3b220c00bc4a21`
- checker: `9ed03b1f3aff165f7a624ed58518d1ac89ae5f21042b7fd22d2cfdf147104368`
- family checker: `fe01b0b0d77c68806e68242be2ab4d484e59f3c6cdc3f9bfaa72e94796d82568`

The matrix high-frequency limit is nonzero, so this positive majorant alone does not solve arbitrary-data Navier--Stokes regularity.
