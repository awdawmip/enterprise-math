# EC49FTW — Nonaffine quadratic fiber deformation and a sharp stochastic-order threshold

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen inputs, type, and domain

This work postprocesses the external *price-prior observer* of the inherited BRC16943 optimal q140 discount. Frozen native scientific pin: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Native parent: EC49FTH PR #2774 @ `999bf1069403306b3813e0e390dae4435d7b4b8c` (AUTHOR_PROVED, NOT_REVIEWED). Immediate inherited price fiber: EC49FTV PR #2805 @ `9d75e96c7273bfcac61530d5401b0e5885cd4fd9` and EC49FTU PR #2801. No native Bellman rerun or P000 change occurs here.

External box: `a in [3/4,49/64], b in [7/16,57/128]`. Condition on high-gap `m=M in I=(1469/64,187/8)`, set `t=187/8-m in (0,T)`, `T=27/64`, upper discount `U=3/4`, lower conditional fiber `L(m)=(8m+173)/480`. The inherited *nonclipped* inverse is

`a(m,z)=(47-m)/945+(44/45)z`, `b(m,z)=1/27-m/54+(10/9)z`, `L(m)<z<U`.

The clipped fiber has `b(m)=(47-m)/54`, `x(m)=(740-m)/945` and `x(m)<a<49/64`. Its clipping curve is `a_c(b)=(77+6b)/105`. The inherited Jacobians are `16/945` for the nonclipped density and `1/54` for the clipped mass.

## Nonaffine joint-density family

For any `eta>=0`, let `q(a,b)=a-a_c(b)` and let

`h_eta^base(a,b)=(1+a+b)*(1+eta*q(a,b)^2)`.

The base density is strictly positive, smooth and correlated on the entire closed price box. On the continuous fiber,

`K_eta(m,z)=(16/945)*(1+a(m,z)+b(m,z))*(1+eta*[8(4z-3)/35]^2)`.

This deforms the *continuous kernel nonaffinely* in z. The positive quadratic multiplier depends only on z, so it retains the base kernel's strict TP2.

A fully explicit, strictly positive C-infinity clipped-only mass perturbation exists for every `lambda>=0`: let `phi(s)=0` for `s<=0`, and `phi(s)=exp(-1/s^2)` for `s>0`. Define `d(b)=49/64-a_c(b)>0`, `S(b)=int_0^{d(b)} phi(u)du>0`, `t(b)=54b-189/8>=0`. Then take, up to its finite positive normalization,

`h_{eta,lambda}=h_eta^base+54*lambda*t(b)*A_eta(t(b))*phi(q(a,b))/S(b)`.

Here `A_eta` is the positive explicit polynomial below. The added term vanishes identically on the nonclipped region `q<=0`; on the clipped fiber it adds *exactly* `lambda*t*A_eta(t)` to the atom mass after the `1/54` Jacobian, because the shape integral divided by S equals one. All functions are smooth through the clipping seam since phi is flat at zero. The overall density normalizer cancels from the conditional distribution.

## Exact masses and sharp theorem

Write `A_eta(t)=int_L^U K_eta(m,z) dz`, `B_eta(t)=(1/54)*int_{x(m)}^{49/64}h_eta^base(a,b(m)) da`. Exact integration yields

```text
A_eta(t)= t*(137265384375+135607500*t
            +eta*(10624320*t^2-31616*t^3)) / 221526014062500

B_eta(t)= (441-64*t)*(5838972720537600+50565847449600*t
            +eta*(103568717259-29177039808*t
                   +1924780032*t^2+18612224*t^3))
          / 8670060656386375680000

r_{eta,lambda}(m)= B_eta(t)/A_eta(t) + lambda*t.
```

**Theorem A (all nonnegative eta).** For every `eta>=0`, `lambda>=0`, the *entire* conditional family on `m in I` satisfies `m<m' => Z|M=m <=_st Z|M=m'` if and only if

```text
0 <= lambda <= Lambda(eta)
Lambda(eta)=8750*(5242065851199447*eta^2
       +464097831859863824000*eta
       +8116152181126391808000000)
       /[19683*(15916473*eta+1157352560000)^2].
```

**Proof.** The factor `1+a(m,z)+b(m,z)` is positive affine with negative m-coefficient and positive z-coefficient, so its mixed log derivative is strictly positive and its kernel strictly TP2. Multiplication by any positive z-only factor preserves strict TP2. With L(m) increasing and U fixed, the continuous normalized laws are stochastically increasing. The mixed law consists of that continuous component and a top atom at U of probability `r/(1+r)`. A mixture coupling shows that nondecreasing r is sufficient; the upper-tail event `Z=U` shows it is necessary.

For the curvature of the original atom ratio `R_eta=B_eta/A_eta`, put `a=221526014062500*A_eta`, `b=8670060656386375680000*B_eta`. With primes denoting differentiation in t, define

`N=b''*a^2-b*a''*a-2*b'*a*a'+2*b*(a')^2`.

Then `R_eta''(m)=(221526014062500/8670060656386375680000)*N/a^3`. The exact rational certificate expands `N=sum_{j=0}^3 eta^j N_j(t)` and converts `N_j((27/64)s)` to its full-degree Bernstein basis, `0<=s<=1`. Its complete coefficient sign profiles are:

| j | degree in t | positive Bernstein coefficients | zero | negative |
|---|---:|---:|---:|---:|
| 0 | 3 | 4 | 0 | 0 |
| 1 | 6 | 7 | 0 | 0 |
| 2 | 8 | 7 | 2 | 0 |
| 3 | 9 | 6 | 4 | 0 |

Every basis function is nonnegative, and the entire eta^0 coefficient is strictly positive, so `N>0` for all `0<=t<=T, eta>=0`. The polynomial `a>0` for `t>0`: the eta coefficient `t^2*(10624320-31616*t)` is nonnegative, and the constant part positive. Hence `R_eta''(m)>0` throughout I. Its derivative is therefore minimal at the left limit `m downarrow 1469/64` (`t uparrow 27/64`). Exact rational quotient differentiation gives the stated Lambda(eta). Since `dt/dm=-1`, the added atom mass changes `r'` by `-lambda`. Thus `r'` is nonnegative everywhere iff `lambda<=Lambda(eta)`. If lambda is larger, r decreases on a nonempty interior neighborhood of the left endpoint and the top-atom probability decreases, contradicting FOSD. QED.

**Theorem B (unique nonaffine repair transition at lambda=3).** Direct differentiation gives

```text
Lambda'(eta)=980000000*(42384250491004069407999*eta
       +2488962318606109896061456000)
       /[19683*(15916473*eta+1157352560000)^3] > 0
```

for every `eta>=0`, with `Lambda(0)=171167905504400/63545784776721` and `lim_{eta->infinity} Lambda(eta)=566272545654261250/61560189400614147`. For fixed `lambda=3`, there is exactly one positive critical `eta_*`, the positive root of

`30908950173645923529*eta^2+1885376222457017973760000*eta-8077734137777523206400000000=0`.

The exact rational bracket is `4019<eta_*<4020` (approx. `4019.54108034360`). Complete stochastic order fails for `0<=eta<eta_*` and holds for `eta>=eta_*`. This is a *monotone repair* path produced by a quadratic continuous-fiber deformation, in contrast to the affine-theta reentrant path in EC49FTV.

## Evidence and continuation

The standalone standard-library Fraction checker recomputes A/B polynomial numerator derivatives, all **30 exact** Bernstein coefficients (**24 positive and 6 zero**), the sharp Lambda rational polynomial identity, the lambda=3 rational bracket and positive-mass samples. Algebraic coefficient positivity together with the analytic TP2/mixed-law proof establishes the stated continuous quantifiers. Inherited native Bellman optimality remains an unreviewed author result; this proof is not independent Review, a formally claimed Result, or main integration.

Next: construct higher-degree nonaffine fibers with multiple extrema of Lambda; classify kernel deformations that lose TP2 but retain the mixed conditional order; separately study the inherited native `z<11/16` Bellman phase using the same frozen input.
