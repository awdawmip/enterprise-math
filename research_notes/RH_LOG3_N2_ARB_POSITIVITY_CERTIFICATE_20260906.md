# RH `H_log3` N=2 four-branch sine finite-subspace positivity certificate

Status: `TASK_RESEARCH / VERIFIED FINITE-SUBSPACE ARB CERTIFICATE / NOT FULL H_LOG3 POSITIVITY / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil form / H_log3 / four labelled support branches / first two Dirichlet-sine modes per branch / rigorous ball arithmetic`

## 0. Certified statement

Let `V_2` be the 8-dimensional real subspace of `H_log3` spanned by the first two Dirichlet-sine modes on each of the four labelled intervals

- `S_-=[-log3,-log2]`,
- `O_-=[-log2,0]`,
- `O_+=[0,log2]`,
- `S_+=[log2,log3]`.

For the Riemann-Weil quadratic form with the current project normalization, the complete Gram matrix on `V_2` is **positive definite**.

This is a rigorous finite-dimensional certificate. It does not state positivity on all of `H_log3`, does not close the Galerkin complement, and does not prove RH.

## 1. Exact positive archimedean series

From `RH_ARCH_PHYSICAL_TRANSLATION_DIRICHLET_FORM_20260906.md`,

`h_inf(t)=h0+2 integral_0^infinity w(r)(1-cos(tr)) dr`,

where

`w(r)=exp(-r/2)/(1-exp(-2r))`

and

`h0=psi(1/4)-log pi=-gamma-pi/2-3log2-log pi`.

Expand

`w(r)=sum_(n>=0) exp[-(2n+1/2)r]`.

For any finite orthonormal basis with translation-overlap matrix `R(r)`, define

`J_c = integral_0^infinity exp(-cr)[2I-R(r)-R(r)^T] dr`.

Because

`2I-R(r)-R(r)^T`

is the Gram matrix of the translated differences `T_r phi_j-phi_j`,

`boxed: J_c >= 0}`

for every `c>0`.

Therefore the exact archimedean Gram matrix is

`boxed: A_arch=h0 I+sum_(n>=0) J_(2n+1/2)}`.

Every finite partial sum is a Loewner lower bound for the complete archimedean matrix.

## 2. Closed-form Laplace overlap: no quadrature and no frequency cutoff

Write

`L_c(i,j)=integral_0^infinity exp(-cr)<phi_i,T_r phi_j> dr`.

Then

`J_c=2I/c-L_c-L_c^T`.

For the four disjoint branch intervals, every entry of `L_c` has an elementary closed form.

### Distinct ordered intervals

If the support of `phi_i` lies entirely to the left of the support of `phi_j`, then

`L_c(i,j)`
`= [integral phi_i(x) exp(cx) dx]`
`  [integral phi_j(y) exp(-cy) dy]`.

The reverse ordered entry is zero.

For a sine mode on `[a,a+ell]`, with `alpha=k pi/ell`,

`integral phi_k(x) exp(cx) dx`
`= sqrt(2/ell) exp(ca) alpha`
`  [1-(-1)^k exp(c ell)]/(c^2+alpha^2)`.

### Same interval

The triangular one-sided overlap is reduced by elementary integration of

`sin(alpha u) sin(beta(u+r))`

to the closed form implemented in

`scripts/rh_log3_n2_arb_certificate.py`.

Thus the certificate contains no numerical integration and no truncation of a frequency integral.

## 3. Exact finite arithmetic and pole blocks

On `H_log3`, the support geometry makes the prime-power contribution finite. The only nonzero von-Mangoldt translations satisfy `m<=9`:

`m in {2,3,4,5,7,8,9}`.

Each translation overlap is evaluated with Arb, while every support max/min decision is made by exact rational comparison in multiplicative coordinates. The basis interval endpoints are

`{1/3,1/2,1,2,3}`

before taking logarithms, and the shift is multiplication/division by the integer prime power `m`. Therefore no floating-point branch decision enters the certificate.

The unreduced two-sided pole contribution retains both endpoint channels

`l_+(f)=integral f(x) exp(x/2) dx`,
`l_-(f)=integral f(x) exp(-x/2) dx`,

and is assembled as

`P=l_+l_-^T+l_-l_+^T`.

No parity/inversion rank-one collapse is assumed.

## 4. Certified lower matrix

Take

`K=1000`

and define

`M_1000`
`= h0 I + sum_(n=0)^999 J_(2n+1/2)`
`  + M_prime + M_pole`.

The complete `V_2` Weil Gram matrix satisfies

`M_full = M_1000 + sum_(n>=1000) J_(2n+1/2)`.

Since every omitted `J_c` is positive semidefinite,

`boxed: M_full >= M_1000}`.

It therefore suffices to certify `M_1000>0`.

## 5. Arb interval LDL^T certificate

Production backend:

- GitHub Actions workflow: `.github/workflows/rh-log3-n2-arb-cert.yml`;
- certificate script: `scripts/rh_log3_n2_arb_certificate.py`;
- Python: `3.13.15` on Ubuntu 24.04 runner;
- `python-flint==0.9.0`;
- Arb working precision: `256 bits`;
- series cutoff: `K=1000`;
- workflow run: `34021625738`;
- job: `101455156783`;
- source head: `1d6afc5ae427dd62f216a42f4f64d1e92ab47769`.

The interval `LDL^T` pivots were:

| pivot | Arb midpoint | Arb radius |
|---:|---:|---:|
| 0 | `0.1236920816464326083949419181146212286691` | `1.10211342786e-74` |
| 1 | `0.6971253657764818005981802779994816126957` | `1.01587894875e-74` |
| 2 | `0.002631372766014514289746622760099253695627` | `1.90713480677e-74` |
| 3 | `0.008904026851692624055194818228418384119191` | `7.08950693426e-74` |
| 4 | `0.001508208806089498345829329071373875873034` | `6.16683550591e-74` |
| 5 | `2.840019350630616513170650322677642388568e-5` | `2.24203031044e-72` |
| 6 | `0.002349565912955672273597200915334453228481` | `3.22429850851e-70` |
| 7 | `0.001368950271229023026771025463450140044630` | `1.35260214779e-68` |

Every pivot ball lies strictly in `(0,infinity)`. Therefore the finite lower matrix `M_1000` is rigorously positive definite by `LDL^T`/Sylvester inertia.

Because the omitted series tail is positive semidefinite,

`boxed: M_full|_(V_2) > 0}`.

The CI log explicitly returned:

`CERTIFIED: all 8 Arb LDL^T pivots are strictly positive.`

and then applied the PSD-tail theorem step.

## 6. What has advanced relative to the previous floating diagnostics

Previous work had floating positivity at `eta=1` for larger finite sections but margins too small to trust. This certificate changes the status of one concrete unit:

`N=2 FOUR-BRANCH H_LOG3 FINITE SUBSPACE`
`FROM FLOATING POSITIVITY`
`TO RIGOROUS CUTOFF-FREE ARB POSITIVITY`.

The key reason this became possible was not merely higher precision. It was the structural rewrite

`INFINITE DIGAMMA INTEGRAL`
`-> POSITIVE CLOSED-FORM MATRIX SERIES`
`-> FINITE LOWER MATRIX + PSD OMITTED TAIL`.

The uncomputed archimedean tail requires no absolute-error estimate at all for the positivity direction.

## 7. BRC / observer-preservation interpretation

- four branch identities are retained throughout;
- prime shifts retain exact support provenance;
- the two pole channels are not prematurely recoalesced;
- the infinite archimedean observer is compressed only through a one-sided order certificate: the omitted directions are proved PSD for the declared positivity operation.

This is an operation-safe quotient/certificate, not information erasure by convenience.

## 8. Smallest unresolved unit

The next finite-dimensional target is the same construction with

`N=8` modes per branch (`32 x 32`).

Because the complete `N=8` floating margin is near `10^-12`, two questions must be answered before blindly increasing `K`:

1. how large a positive-series cutoff `K` is needed before the lower matrix itself becomes positive;
2. whether an ordering/pivot strategy or symmetry-preserving block factorization gives a numerically robust Arb certificate without sacrificing branch provenance.

Even a successful `N=8` certificate would remain finite-dimensional. The major analytical blocker after finite certification is a Galerkin-complement theorem that controls every mode outside the retained sine subspace.

## 9. Hard boundaries

- `V_2 POSITIVITY != H_LOG3 POSITIVITY`.
- `FINITE GALERKIN CERTIFICATE != RH`.
- No claim is made that `K=1000` is minimal or asymptotically efficient.
- The positive-series tail argument is one-sided and applies to the declared archimedean component; prime/pole terms are already included exactly in the finite matrix.
- No conclusion about all future square-shell steps follows automatically from this first finite certificate.

## Provenance

- Mathematical predecessors:
  - `research_notes/RH_ARCH_PHYSICAL_TRANSLATION_DIRICHLET_FORM_20260906.md`;
  - `research_notes/RH_SINE_BASIS_ARCH_DIAGONAL_TAIL_INERTIA_CERTIFICATE_20260906.md`;
  - `research_notes/RH_LOG2_LOG3_N8_THRESHOLD_INERTIA_DIAGNOSTIC_20260906.md`.
- Production certificate source: `scripts/rh_log3_n2_arb_certificate.py`.
- Production CI: workflow run `34021625738`, job `101455156783`.
- Certificate source commit: `1d6afc5ae427dd62f216a42f4f64d1e92ab47769`.
- Researcher-ID: `EM-DIRECT-7C1A42`.
