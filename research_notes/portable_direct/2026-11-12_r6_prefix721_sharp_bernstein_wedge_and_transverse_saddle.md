# PREFIX-721-R6 — a 71-fold wider Gamma transverse wedge and a local no-maximizer theorem

Date: 2026-11-12 Asia/Shanghai. Parent objective: PREFIX-675, immediate predecessor PREFIX-720. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. This is an **auxiliary two-parameter Gamma-clock BRC statistical observer**, not a claim about a native X6 spatial plane. Status: **AUTHOR_EXACT_INTEGER_RECOMPUTED / UNREVIEWED / NOT_ADMITTED**.

## Statement

On `D=[0,1/2]^2`, let `Y(p,z)=max(T_p,T_z)` be the two independent Gamma completion clocks with the original 189-level stopping-count distributions. Write
[
mu=E[Y],quad M_2=E[Y^2],quad W=M_2-mu^2,quad
f_t=W-tmu,quad V_q=q^2f_{1/q}.
]
Set `x0=11/96`, `r=1/14000000000`, and
[
J(p,z)=mu_p(M_2)_z-mu_z(M_2)_p=(z-p)K(p,z).
]
Then throughout the **entire closed square**
[
S_r={(p,z): |p-x_0|le r, |z-x_0|le r}subsetoperatorname{int}(D)
]
we have
[
oxed{K(p,z)>2,000,000}.
]
For `p<z`, this yields `J(p,z)>2,000,000(z-p)>0`; the sign reverses for `p>z`.

**Stronger conclusion:** For *every* real `t` (hence all real `q>0` in the corresponding Gamma objective), **no point in `S_r` is a local or global maximizer of `f_t` on `D`**. Non-diagonal interior points cannot be stationary; any diagonal interior stationary point has positive curvature in the anti-diagonal direction. This is a strict optimizer-free region, not merely a stationary-free off-diagonal wedge.

The explicit radius is `500/7 ≈ 71.4286` times the `10^-12` radius of PREFIX-720. It is a local theorem; the previously reported global-grid exclusion fraction is not adjusted without proving and checking non-overlap.

## Exact Gamma kernel and inherited identities

The exact Gamma survivor pair kernel is `C[n,m]=binom(n+m,n)/2^(n+m+1)`. With frozen survivor tails `s_n(p)` (`0<=n<=188`):
[
mu=sum_n(s_n(p)+s_n(z))-sum_{n,m}C_{nm}s_n(p)s_m(z),
]
[
M_2=2sum_n(n+1)(s_n(p)+s_n(z))
-sum_{n,m}(n+m+1)C_{nm}s_n(p)s_m(z).
]
PREFIX-720 derives the exact first/second-derivative integer numerators and the identities
[
J(z,p)=-J(p,z),qquad
K(p,z)=int_0^1 J_z(p,p+u(z-p))du.
]
Its frozen certificate at `x0=88/768` is recomputed here from all 189 rows and 9,529 nonzero survivor coefficients, with `L=768^188`, `Z=2^377`, `d=L^2Z`, and the exact integer definitions `P,Q,PP,QQ,C0,C1` of the companion checker:
[
J_z(x_0,x_0)=rac{P(QQ+C_1)-Q(PP+C_0)}{d^2}
>oxed{40,800,000}.
]
This strictly strengthens the `10,000,000` integer lower bound previously used. The exact numerator decimal SHA-256 after the full sign comparisons matches the earlier reproducer: `f9eab864317b8b68e16940ed539733265725445e8108de8c7075d4d18adc95d2`.

## New Bernstein derivative lemma

Each frozen tail is a Bernstein polynomial
[
s_n(p)=sum_{k=0}^n g_{n,k}inom nk p^k(1-p)^{n-k},qquad
0le g_{n,k}=v_{n,k}/inom nkle1 .
]
For every integer `r>=1`, finite differences obey
[
|Delta^r g_{n,k}|le2^{r-1}.
]
Indeed the positive and negative binomial-coefficient groups in the alternating finite difference each sum to `2^(r-1)`; with coefficients in `[0,1]`, their difference has that absolute bound. Therefore, for `1<=r<=3`,
[
|s_n^{(r)}(p)|le 2^{r-1}(n)_r
le rac{376^r}{2}quad(0le ple1, 0le nle188).
]
For pure derivatives, positive Gamma influence factors satisfy `0<=A_n<=1` and `0<=H_n<=2(n+1)`. For mixed derivatives, the nonnegative kernel has row sums
[
sum_m C_{nm}=1,qquad
sum_m(n+m+1)C_{nm}=2(n+1).
]
Thus, for any *positive-order* partial derivative of total order `1<=r<=3`,
[
|D^alphamu|lerac N2,376^r,qquad
|D^alpha M_2|lerac{N(N+1)}2,376^r,qquad N=189.
]
Both factors in each Leibniz term of `J_{zp}` and `J_{zz}` are positive-order moment derivatives; the sum of their derivative orders is four. The previous derivative bound can hence be quartered:
[
|J_{zp}|, |J_{zz}|le
2N^2(N+1)376^4.
]
For `(p,z)` in a radius-`r` square around `(x0,x0)`, the integral identity and the mean-value theorem imply
[
|K(p,z)-J_z(x_0,x_0)|le B r,quad
oxed{B=4N^2(N+1)376^4=542610983324712960}.
]
The exact integer inequality
[
40,800,000-rac{542610983324712960}{14000000000}
>2,000,000
]
establishes the announced uniform signed margin. More generally this proof gives `K>0` for every rational `0<r<40800000/B`, while remaining inside the parameter domain.

## Why the whole square has no local maxima

The exact first partials are
[
f_{t,p}=mu_pigl(R_p-2mu-tigr),quad
f_{t,z}=mu_zigl(R_z-2mu-tigr),
quad R_p=(M_2)_p/mu_p, R_z=(M_2)_z/mu_z,
]
with `mu_p,mu_z>0` on the interior. Hence any off-diagonal stationary point requires `J=0`, incompatible with the signed bound.

At a diagonal stationary point `(x,x)`, symmetry gives `R_p=R_z=2mu+t`, and the **exact Hessian identity**
[
left.rac{d^2}{ds^2}f_t(x+s,x-s)ight|_{s=0}
=2(f_{t,pp}-f_{t,pz})
=oxed{rac{2J_z(x,x)}{mu_p(x,x)}}>0 .
]
Thus a diagonal stationary point cannot be a local maximum either. Every point in `S_r` lies in the interior of `D`, so these two cases exclude all local and global maximizers in `S_r` for every real `t`.

This reveals a useful distinction from the PREFIX-719 diagonal restricted maximum: a point can maximize the *diagonal restriction* while still having positive transverse curvature in the full two-parameter domain.

## Explicit saddle example

At `x=x0`, let
[
t_0=(M_2)_p(x_0,x_0)/mu_p(x_0,x_0)-2mu(x_0,x_0),quad q_0=1/t_0.
]
The exact integer/rational checker proves `1/4<t0<1/3` and hence `3<q0<4`. This gives a genuine interior stationary point for `f_{t0}`. The same checker proves
[
280<mu_p(x_0,x_0)<300,quad
Theta'(x_0)<-100,quad J_z(x_0,x_0)>40,800,000.
]
Consequently the diagonal and anti-diagonal directional second derivatives for `f_{t0}` satisfy, respectively,
[
left.rac{d^2}{ds^2} f_{t_0}(x_0+s,x_0+s)ight|_0
=2mu_pTheta'<-56,000,
]
[
left.rac{d^2}{ds^2} f_{t_0}(x_0+s,x_0-s)ight|_0
=2J_z/mu_p>272,000.
]
This is an **exact rationally specified strict saddle** for the auxiliary objective, using `q0 in (3,4)`; the scaling to `V_{q0}` multiplies these curvatures by `q0^2>0`.

## Reproduction, evidence and continuation

Companion program: `PREFIX721_R6_SHARP_BERNSTEIN_WEDGE.py`, importing the existing frozen parent program `PREFIX720_R6_LOCAL_TRANSVERSALITY_CHECKER.py` from the same directory. It independently rebuilds the 189 survivor rows and exact Gamma derivatives, checks the original and strengthened integer signs, the Bernstein bound, the explicit radius, `t0`, and the two saddle curvatures. JSON: `PREFIX721_R6_RESULTS.json`. Local author run: `ALL_CHECKS_PASS PREFIX721-R6`; derived `floor(J_z)=40818717`.

Parent manuscript: [PREFIX-720](https://github.com/awdawmip/enterprise-math/blob/99f89db754940a747c02dee12f246b65d524959c/research_notes/portable_direct/2026-11-12_r6_prefix720_gamma_diagonal_transverse_wedge.md); parent code SHA-1 `c0c25c090ae5035853d1cd63a79bf6e2548be52a` at this research snapshot. The parent and this paper are author-level evidence; no independent reviewer or formal Result/Review has admitted either theorem.

**Next discriminating unit:** derive interval-specific Bernstein envelopes for `K(p,z)` over surviving `384x384` Gamma candidate cells. A single exact sign certificate can classify a genuine two-dimensional optimizer-free region; an exact nonpositive counterexample to `K>0` should instead be retained to locate its true boundary. Compare the resulting cells with the PREFIX-718 witness exclusion set before claiming any added area. Preserve the fixed 189-row science input and avoid duplicating active Owner claims.
