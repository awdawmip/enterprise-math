# 无散角度格点界与临界反馈常数改进

Record-ID: `FINDING-EM-PDE-ANGULAR-CONSTANT-BARRIER-20260910`
Status: `TESTING / ORDINARY_PROOF_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: 2026-09-10

## Scope

This is a classical three-torus result downstream of unchanged P000. It does not derive native X6 dynamics and does not prove arbitrary-data Navier–Stokes regularity.

For normalized `T^3=(R/2pi Z)^3`, let `B(f,g)=P((f.grad)g)`, with `f` mean-zero and divergence-free. Fourier incompressibility gives, for `k=p+q`,

`|fhat(p).q|=|fhat(p).k| <= |p cross k|/|p| |fhat(p)|`.

Hence

`||B(f,g)||_{Hdot^-1/2}^2 <= (sup_k S_perp(k)) ||f||_{Hdot^1}^2 ||g||_{Hdot^1}^2`,

where

`S_perp(k)=sum_(p!=0,k) |p cross k|^2/(|k||p|^4|k-p|^2)`.

The sum is split disjointly into `|p|<6`, `|k-p|<6` with the first leg not already counted, and the remaining far region. The finite near region uses 894 lattice points and 487 octahedral output classes, with exact rational acceptance. The large-output near part is bounded using cubic tensor symmetry. The far region is covered analytically by unit-cube comparison and the exact Riesz integral `int_R3 dx/(|x|^2|k-x|^2)=pi^3/|k|`.

The resulting certified bound is

`sup_k S_perp(k) < (159/20)^2`,

so

`||P((f.grad)g)||_{Hdot^-1/2} <= (159/20)||f||_{Hdot^1}||g||_{Hdot^1}`.

Thus the previous valid constant 9.503 can be replaced by 7.95 in this interface. The constant is effective, not claimed sharp.

## Consequence for the A3 certificate

Using the same two causal responses and the same all-mode inverse/contraction interface, the specified rank-three A3/FCC family passes the complete NS certificate at amplitude `a=0.16`, and uniformly for `0<=a/nu<=0.165` with arbitrary smooth real divergence-free mean-zero initial perturbation bounded by `1e-5 nu` in `Hdot^1/2`. This is a restricted sufficient family, not an arbitrary-data theorem.

## BRC boundary

The improvement is legal because branch identity and polarization are retained through the incompressibility identity before applying a positive majorant. The angular zero here is classical collinearity suppression; it is not identified with the separate equal-shell 120-degree/helical cancellation.

## Verification provenance

Original locally verified package SHA256 records:
- note: `2babce33b1f6f90b05a133435380883ed8dbdafbdc1d3073f1c88fe9930c7839`
- angular checker: `40d41ab035fd4be7b6c271f3cb0144c9a4c2042e4268940c96613c240de89a50`
- family checker: `3baea8c9d1dd908e20b4b85b0539ed7687a0efe114d63acaedeabd7a77bcdf6e`

The finite checks are not independent review or proof-assistant formalization.
