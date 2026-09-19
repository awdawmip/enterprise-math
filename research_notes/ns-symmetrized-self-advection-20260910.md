# 对称化自作用常数：把完整 NS 二次反馈从 6.45 降到 4.95

Record-ID: `FINDING-EM-PDE-SYMMETRIZED-SELF-ADVECTION-20260910`
Status: `TESTING / ORDINARY_PROOF_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: 2026-09-10

## Scope

This is a classical periodic Navier–Stokes result downstream of unchanged P000. It does not derive native X6 dynamics and does not claim arbitrary-data regularity or an optimal constant.

Let `B(f,g)=P((f.grad)g)` and `B_s(f,g)=[B(f,g)+B(g,f)]/2`. The parent result supplies the ordered two-input constant 6.45. The nonlinear fixed-point feedback, however, uses the quadratic diagonal `Q(u)=B(u,u)` and hence the symmetric polarization `B_s`, so the `p<->q` branch pairing can be retained before taking a positive majorant.

## Symmetrized Fourier kernel

For a real divergence-free field `u` and `k=p+q`,

`Bhat(u,u)(k)=(i/2)P_k sum[(uhat(p).k)uhat(q)+(uhat(q).k)uhat(p)]`.

Fix a real unit output test vector `z in k^perp`, and put `M_z=k z^T+z k^T`. For `a=uhat(p) in p^perp`, `b=uhat(q) in q^perp`,

`|z.Bhat_pair| <= (1/2)||P_p M_z P_q||_F |a||b|`.

Thus the positive diagonal kernel is

`S_self(k,z)=(1/(4|k|)) sum_(p+q=k) ||P_p M_z P_q||_F^2/(|p|^2|q|^2)`.

The quadratic map obeys

`||B(u,u)||_{Hdot^-1/2}^2 <= (sup_(k,z) S_self(k,z)) ||u||_{Hdot^1}^4`.

## Near and far bounds

Writing

`P_p M_z P_q=(P_p k)(P_q z)^T+(P_p z)(P_q k)^T`,

the Frobenius parallelogram inequality and `p<->q` relabelling imply that the self near kernel is bounded by the already certified ordered-polarization near kernel. Hence

`S_self,near < 37/5`.

For the far region rotate coordinates so `k=K e3`, `z=e1`, `p=(x,y,zeta)`, `q=(-x,-y,K-zeta)`. Then

`||P_p M_z P_q||_F^2=N/(|p|^2|q|^2)`

with

`N=K^2[K^2x^2+K^2y^2-4Kx^2zeta-2Ky^2zeta+2x^2y^2+4x^2zeta^2+2y^4+2y^2zeta^2]`.

Its Laplacian has the positive form

`Delta N=4K^2[3(zeta-K/2)^2+3x^2+8y^2+K^2/4]`.

The centered unit-cube average is exactly

`int_Qp N = N(p)+Delta N(p)/24+29K^2/360 >= N(p)`.

After the same denominator comparison used by the coupled-polarization parent, the continuum self kernel is

`int_R3 N/(4|k||p|^4|q|^4) dp = 3 pi^3/16`,

exactly one half of the corresponding ordered-polarization continuum positive kernel. Therefore

`S_self,far < 17.09560069415452...`.

Combining near and far,

`sup S_self < 24.49560069415452... < (99/20)^2`.

### Theorem A

For real mean-zero divergence-free periodic `u`,

`||B(u,u)||_{Hdot^-1/2} <= (99/20)||u||_{Hdot^1}^2`.

The constant 4.95 is effective, not claimed optimal. With the unitary Fourier transform on `R^3`, the analogous diagonal constant is `sqrt(6)/16`.

## Symmetric bilinear extension

A quadratic norm bound on a real Hilbert space polarizes with no loss. For any `t>0`,

`B_s(f,g)=[Q(f+t g)-Q(f-t g)]/(4t)`.

Thus

`||B_s(f,g)|| <= C/(2t)(||f||^2+t^2||g||^2)`.

Optimizing `t=||f||/||g||` gives

`||B_s(f,g)||_{Hdot^-1/2} <= (99/20)||f||_{Hdot^1}||g||_{Hdot^1}`

for real divergence-free fields. This does not replace 6.45 for a genuinely ordered `B(f,g)`; the gain is licensed only when the future operation factors through the symmetric quadratic map.

## Trajectory-space consequence

For the inherited trajectory norm

`||h||_X^2=sup_t[||h(t)||_{Hdot^1/2}^2+c int_0^t||h||_{Hdot^3/2}^2 ds]`, `c=3nu/4`,

and `Y=L2_t Hdot^-1/2`, the parent identity `int H D <= ||h||_X^4/(2c)` yields

`||B_s(f,g)||_Y <= [(99/20)/sqrt(2c)]||f||_X||g||_X`.

Since

`B(w,w)-B(z,z)=B_s(w-z,w+z)`,

the nonlinear contraction uses

`alpha=L*(99/20)/sqrt(2c)`

instead of the ordered 6.45 constant. The background causal inverse `L` itself is unchanged.

## A3 endpoint

Reusing the same exact rank-three two-shell A3/FCC reference and the two causal responses, with all generated outputs retained, the checker certifies at `nu=1`, `a=3/16`:

- `L < 1311/250 = 5.244`;
- `alpha < 106/5 = 21.2`;
- `eta < 589/50000 = 0.01178`.

Taking `r=47/2000=0.0235`, exact rational arithmetic gives

- `4 alpha eta <= 0.998944 <1`;
- `r-eta-alpha r^2 = 123/10000000 >0`;
- `2 alpha r = 2491/2500 <1`.

An arbitrary smooth real divergence-free mean-zero initial perturbation of `Hdot^1/2` size at most `1/500000` still leaves positive margin. By monotonicity of the inherited amplitude bounds, this yields the viscosity-scaled restricted family

`0<=a/nu<=3/16`, `||delta u0||_{Hdot^1/2}<=2e-6 nu`.

This is a sufficient neighborhood, not arbitrary-data global regularity.

## BRC boundary

Ordered `B(f,g)` and the quadratic diagonal `Q(u)=B(u,u)` are different observer contracts. The diagonal permits `p<->q` branch pairing before compression; the background linearization generally does not. Prematurely merging ordered branches would be invalid, while refusing to merge them in the quadratic map overpays the nonlinear feedback constant.

Next target: certify the self near kernel directly rather than bounding it by the ordered near kernel, and compare that gain with improvements to the background inverse.
