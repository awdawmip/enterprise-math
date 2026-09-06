# RH log2 -> log3 N=8 threshold-inertia diagnostic

Status: `TASK_RESEARCH / FLOATING FINITE-SECTION DIAGNOSTIC / NOT INTERVAL CERTIFIED / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil square-shell / log2->log3 / support-exact branch-sine Galerkin / threshold inertia`

## 0. Purpose and status boundary

This note pressure-tests the corrected reference block

`B_ref = B_prime + B_Cauchy/Carleman`

from `RH_ARCH_BOUNDARY_CARLEMAN_PRINCIPAL_DECOMPOSITION_20260906.md` in a natural support-exact finite section.

The calculation is deliberately classified as **floating diagnostic only**. In particular, one `eta=0.999` full-block eigenvalue lies at scale `4e-10`; its sign must not be promoted until all matrix entries and all analytic/discretization tails are rigorously enclosed.

The companion note

`RH_LOG2_LOG3_CARLEMAN_TAYLOR_TAIL_CERTIFICATE_20260906.md`

rigorously bounds only the regular-arch cross tail. It does not certify the diagonal archimedean matrices used here.

## 1. Support-exact four-branch basis

Put

`L2=log2`, `L3=log3`, `delta=log(3/2)`.

Retain four labelled support branches:

- `O_-=[-L2,0]`;
- `O_+=[0,L2]`;
- `S_-=[-L3,-L2]`;
- `S_+=[L2,L3]`.

On an interval `[a,a+ell]`, use the orthonormal Dirichlet sine basis

`phi_(a,ell,k)(x)=sqrt(2/ell) sin(k pi (x-a)/ell)`,

`k=1,...,N`.

For this diagnostic take

`N=8` per branch,

so the old block dimension is 16, shell block dimension is 16, and every threshold matrix has dimension 32.

This basis respects the exact branch supports. No parity/inversion recoalescence is performed.

## 2. Fourier transform used for the archimedean diagonal blocks

For

`alpha=k pi/ell`,

under

`f_hat(tau)=integral f(x) exp(-i tau x) dx`,

the basis transform is

`phi_hat(tau)`
`= sqrt(2/ell) exp(-i tau a)`
`  * alpha [1-(-1)^k exp(-i tau ell)]/(alpha^2-tau^2)`,

with the removable values at `tau=+/-alpha` understood by continuity.

The archimedean quadratic matrix was evaluated from

`(1/pi) integral_0^infinity`
`[Re psi(1/4+i tau/2)-log pi]`
`Re(phi_hat_i conjugate(phi_hat_j)) d tau`.

Floating Gauss-Legendre integrations were compared at frequency cutoffs `T=1500,2000,2500`. This is a convergence diagnostic, not a rigorous improper-integral enclosure.

## 3. Exact finite prime-power carrier in `H_log3`

For the complete `[-log3,log3]` finite section, prime-power translations satisfy

`log m <= 2 log3`,

so only

`m in {2,3,4,5,7,8,9}`

contribute.

For each such `m`, with

`w_m=Lambda(m)/sqrt(m)`, `s_m=log m`,

the real bilinear matrix contribution was assembled from the support-exact translation overlap as

`-w_m (R_(s_m)+R_(s_m)^T)`.

No prime-only absolute-value envelope was used.

## 4. Pole endpoint channels

On the unreduced two-sided basis define

`l_+(phi)=integral phi(x) exp(x/2) dx`,
`l_-(phi)=integral phi(x) exp(-x/2) dx`.

The pole matrix used here is

`P = l_+ l_-^T + l_- l_+^T`.

Its old-to-shell block has two nonzero singular values in this calculation,

approximately

`2.26700917`, `0.188547549`,

with the rest at floating zero. Thus the unreduced cross is numerically rank 2, matching the conservative BRC rank budget. A rank-1 statement requires a separately declared parity/inversion sector.

## 5. Direct x-space archimedean cross

For old-to-shell cross entries, the exact off-diagonal kernel

`K_inf(s)=-exp(-s/2)/(1-exp(-2s))`, `s>0`,

was integrated directly in x-space. This avoids the slow high-frequency cancellation that affects a truncated Fourier integral for adjacent supports.

The Cauchy principal block was separately computed from

`K_C(s)=-1/(2s)`.

At `N=8`, the singular values of the floating regular difference

`B_arch-B_Cauchy`

were approximately

`0.207358374`,
`0.0257849844`,
`2.77237e-4`,
`1.12e-5`,
`2.44e-7`,
`5.66e-8`,
`2.18e-10`,
`2.07e-11`,
`...`.

This rapid decay is consistent with the exact analyticity/Taylor-compressibility theorem; it is not itself the proof of that theorem.

Increasing the direct tensor Gauss rule from 128 to 160 and 160 to 192 points per interval changed the cross operator by approximately

`3.06e-10` and `7.27e-11`, respectively.

Again these are floating convergence differences, not certified quadrature errors.

## 6. Diagonal-block sanity values

At the `T=2000` archimedean frequency cutoff, after adding exact finite prime translations and the two pole channels, the floating minimum eigenvalues were approximately

`lambda_min(A_2) = 1.32e-9`,

`lambda_min(D_2) = 2.0846e-3`.

The first value is extremely small, as expected from the existing compact-window near-null observations. Its positivity here is not an interval certificate.

Changing the archimedean cutoff from `1500 -> 2000 -> 2500` changed the displayed minimum eigenvalues only slightly:

- old block: `1.31705e-9 -> 1.31723e-9 -> 1.31730e-9`;
- shell block: `0.002084596 -> 0.002084615 -> 0.002084622`.

This supports numerical consistency but does not bound the infinite-frequency remainder in Loewner order.

## 7. Threshold-inertia ablation table

For each cross choice `B`, form

`H_eta(B)=[[eta^2 A_2,B],[B^T,D_2]]`.

Using direct x-space arch cross and the `T=2000` diagonal blocks, strict floating signs gave:

| `eta` | full | prime only | prime + Cauchy | arch only | Cauchy only | pole only |
|---:|---:|---:|---:|---:|---:|---:|
| 0.9 | 8 | 8 | 8 | 4 | 4 | 2 |
| 0.99 | 6 | 6 | 6 | 4 | 4 | 2 |
| 0.999 | 5 | 5 | 5 | 4 | 4 | 2 |

These counts are numbers of negative eigenvalues of the 32x32 floating threshold matrices.

For all three tested thresholds, the integer count agrees among

`full`, `prime-only`, and `prime+Cauchy`.

This agreement is evidence only. In particular, it does **not** prove that the prime cross dominates in the infinite operator or even in this finite section under rigorous rounding.

## 8. Closest-to-zero eigenvalues

Representative full-block eigenvalues closest to zero were:

### `eta=0.9`

`+5.98e-10`,
`+5.74e-6`,
`+2.00e-5`,
`-1.94e-4`, ...

### `eta=0.99`

`+5.95e-10`,
`+3.03e-6`,
`-1.05e-5`,
`+6.98e-5`, ...

### `eta=0.999`

`-4.29e-10`,
`+8.62e-7`,
`+2.64e-6`,
`-5.04e-5`, ...

The last `eta=0.999` sign is the critical warning. A previous tolerance-based count using `eigenvalue<-1e-8` would report 4, whereas strict floating sign reports 5. The correct current status is

`ETA_0.999_NEAR_ZERO_SIGN = UNRESOLVED_BY_FLOATING_ARITHMETIC`.

## 9. Reference-block gaps are much healthier

For

`B_ref=B_prime+B_Cauchy`,

the closest absolute eigenvalue was approximately

- `7.23e-6` at `eta=0.9`;
- `2.33e-6` at `eta=0.99`;
- `4.71e-6` at `eta=0.999`.

These are many orders of magnitude larger than the rigorously bounded degree-50 regular-arch residual

`||R_50^reg|| < 1.622e-10`.

Therefore the regular-arch **tail itself** is no longer the obstacle to certifying the reference-block inertia. The finite Taylor block and pole channels should simply be included explicitly rather than paid as a rank uncertainty.

## 10. Cutoff sensitivity of the full near-zero signs

Repeating the same finite-section construction with diagonal archimedean frequency cutoffs `T=1500,2000,2500` left the strict floating inertia counts unchanged:

| `eta` | `T=1500` | `T=2000` | `T=2500` |
|---:|---:|---:|---:|
| 0.9 | 8 | 8 | 8 |
| 0.99 | 6 | 6 | 6 |
| 0.999 | 5 | 5 | 5 |

The closest full eigenvalue at `eta=0.999` moved approximately

`-4.34e-10 -> -4.29e-10 -> -4.28e-10`.

This stability is encouraging but remains non-rigorous because the cutoff error is not enclosed.

## 11. Main conclusion of the diagnostic

The computation supports three structural conclusions:

1. the corrected `prime+Cauchy` reference is numerically well conditioned relative to the exact regular-arch tail scale;
2. the full response count still matches the prime-only count at this finite resolution, but this should remain a hypothesis/ablation observation rather than a theorem;
3. the decisive remaining certification problem is now the **diagonal old/shell archimedean block**, especially the near-null old block, plus finite-section complement control.

The immediate proof program should therefore stop spending effort on tighter floating cross quadrature and instead construct a cutoff-free or rigorously interval-enclosed representation for the diagonal archimedean Gram matrices.

## 12. Hard boundaries

- `FLOATING COUNT AGREEMENT != CERTIFIED INERTIA`.
- `N=8 FINITE SECTION != INFINITE OPERATOR`.
- `T=2500 STABILITY != RIGOROUS TAIL BOUND`.
- The `eta=0.999` smallest full eigenvalue is explicitly too close to zero for ordinary floating sign to be treated as proof data.
- The degree-50 regular-arch tail certificate controls only that declared cross remainder.
- No statement at `eta=1` is obtained.
- No RH proof is claimed.
