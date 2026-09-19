# 角度张量尾部、连续极限与改进周期常数

Record-ID: `FINDING-EM-PDE-TENSOR-TAIL-CONTINUUM-20260910`
Status: `TESTING / ORDINARY_PROOF_AND EXACT FINITE CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: 2026-09-10

## Main result

Continue the classical normalized three-torus estimate for

`S_perp(k)=sum |p cross k|^2/(|k||p|^4|k-p|^2)`.

Instead of discarding the angular numerator on the far lattice, use the exact unit-cube average

`int_Qp |x cross k|^2 dx = |p cross k|^2 + |k|^2/6`.

Together with denominator comparison on cubes, this retains the transverse quadratic structure through the lattice-to-continuum step. The exact tensor integral is

`int_R3 (I-xx^T/|x|^2)/(|x|^2|k-x|^2) dx = (pi^3/(4|k|))(3I-ee^T)`, `e=k/|k|`,

and therefore

`int_R3 |x cross k|^2/(|k||x|^4|k-x|^2) dx = pi^3/2`.

This cuts the certified far contribution relative to the scalar comparison and yields

`sup_k S_perp(k) < (1339/200)^2`,

hence the valid periodic estimate

`||P((f.grad)g)||_{Hdot^-1/2} <= 6.695 ||f||_{Hdot^1}||g||_{Hdot^1}`

for mean-zero divergence-free first input `f`.

For the unitary Fourier transform on `R^3`, the same calculation gives the whole-space constant `1/4` in the corresponding bilinear inequality. The whole-space constant is not substituted directly into the periodic theorem.

## High-frequency limit

The same positive lattice kernel satisfies

`S_perp(k) -> pi^3/2` as `|k|->infinity` through integer frequencies.

The proof is a genuine Riemann-sum argument with the singular neighborhoods of `0` and `k` and the spatial tail controlled separately. This shows a structural limit of the positive angular majorant: even after retaining incompressibility angle, the majorant does not decay to zero at high frequency. Further gains require more phase/polarization structure or a sharper propagation estimate.

## A3 consequence

Reusing the same all-mode causal inverse and exact two-response A3 calculation, the certified family extends uniformly to `0<=a/nu<=0.172`, with arbitrary smooth real divergence-free mean-zero off-family perturbation bounded by `5e-5 nu` in `Hdot^1/2`. The endpoint uses an all-time trajectory radius `0.019 nu`.

This is a restricted sufficient family, not arbitrary-data global regularity.

## Verification provenance

Original local package hashes:
- note: `0e51df2092e195f078b30a7b60c506c07f4392e51151541cd192317c2ef534e7`
- tensor-tail checker: `177122b5bc570f5221df781f683391728a7612c6a4af7222eb2c956f2d655750`
- family checker: `fdfa85cc36515edc80ae747366f18a4a2885f106d486475975477b127b846313`

No finite computation is used as a substitute for the analytic infinite-tail or high-frequency-limit argument.
