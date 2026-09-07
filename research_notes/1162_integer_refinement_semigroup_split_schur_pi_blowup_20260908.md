# #1162 — integer refinement semigroup, split–Schur duality, and pi as an identity blow-up calibration

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-integer-refinement-semigroup-split-schur-pi-blowup-20260908
At: 2026-09-08T00:50:00+08:00
Parents:
- `research_notes/1162_alias_fiber_resolvent_brc_20260907.md`
- `research_notes/1162_q_chain_markov_gauge_stabilization_20260908.md`
- `research_notes/1162_physical_schur_pi_free_determinant_20260908.md`

## 1. Discrete refinement semigroup replaces a continuous scale generator

Let P_q act on phase observables by

(P_q f)(theta)=sum_(r=0)^(q-1) p_r(theta) f((theta+r)/q),

with exact positive alias probabilities

p_r(theta)=sin^2(pi theta)/[q^2 sin^2(pi(theta+r)/q)].

The gauge form

p_r=(1/q^2) g((theta+r)/q)/g(theta),

g(theta)=csc^2(pi theta),

makes path composition telescope. Therefore for all integers p,q>=2,

P_p P_q=P_(pq)=P_q P_p.

This is the native finite refinement semigroup. No N derivative or continuous scale interpolation is required.

For the boundary label observable

H_(s,a)(theta)=E[sgn(L+theta)^a |L+theta|^(2-s)],

one has simultaneously for every integer q>=2,

P_q H_(s,a)=q^(s-2) H_(s,a).

Thus q -> q^(s-2) is the multiplicative eigencharacter of the integer refinement semigroup. The Basel exponent s=2 is the unique real exponent for which this eigencharacter is trivial for every q:

P_q H_(2,a)=H_(2,a).

For a=0, H_(2,0)=1 identically.

Earlier continuous-scale-generator / half-integer-Jordan statements remain valid only in their declared analytic/asymptotic readout models. They are not required as the native refinement language after the user's resolution-stability correction.

## 2. Split–Schur duality

For positive probe u, the fine Fourier aliases of one coarse mode obey

sum_(r=0)^(q-1) 1/[lambda_(qN,k+rN)+u]
=
Z_(q,N)(u)/[lambda_(N,k)+u_(q,N)(u)].

The same right-hand side is obtained in physical space by retaining every q-th vertex and Schur-eliminating the q-1 hidden vertices between ports:

Schur(A_(qN)+uI)
=
[q/Z_(q,N)(u)] [A_N+u_(q,N)(u)I].

Therefore Fourier alias summation and physical Schur elimination are dual descriptions of the same exact finite coarse-graining operation.

At u=0 on nonzero fibers, Z=1 and inverse spectral mass is exactly lossless. The zero mode remains singular and is tracked separately by the zero-fiber residual mass.

## 3. Root-of-unity finite carrier and DFT proof

With omega_N=exp(2pi i/N), finite inverse masses can be written

x_(N,k)=1/[N^2 |1-omega_N^k|^2].

For child z_r=omega_(qN)^(k+rN), z_r^q=omega_N^k,

p_r=x_child/x_parent
=|(1/q) sum_(j=0)^(q-1) z_r^j|^2.

Finite DFT Parseval gives sum p_r=1. The DFT/Fejer/spectral-leakage identity is classical; the present use is to expose the exact positive branch carrier and its observer leases.

## 4. Pi is absent from finite refinement and enters at the identity blow-up

The finite root-of-unity, Schur, determinant and integer-refinement identities need no primitive pi value once roots of unity / finite cyclic rotation are the declared implementation carrier.

Classical Euclidean circle calibration enters at the local blow-up

M |1-omega_M^n| -> 2pi |n|.

Thus

pi=(1/2) lim_(M->infinity) M |1-omega_M|

is the conversion constant between one finite rotation chord defect and the continuum tangent/frequency coordinate.

For Basel, the finite algebra supplies the rational invariant

lim Tr'(A_N^(-1))=1/12

under circumference-one normalization. The classical blow-up spectrum supplies eigenvalues `(2pi n)^2`, hence

1/12=2/(2pi)^2 zeta(2),

so zeta(2)=pi^2/6.

This cleanly types the ingredients:
- `1/12`: finite discrete/refinement invariant;
- `2pi`: N3/classical identity blow-up calibration;
- factor 2: positive/negative continuum alias pair.

## 5. BRC observer meaning

The finite relation has two dual safe collapses:
- Fourier side: sum child inverse masses when only the coarse inverse-mass observer is required;
- physical side: Schur-eliminate hidden vertices when only port dynamics is required.

For richer future observers, retain richer carriers: alias labels for arithmetic moments, determinant coefficients / hidden loop-zeta factors for absolute spectral invariants.

This is direct application of the BRC future-language/observer lease rather than post-hoc recovery by differentiation.

## 6. Prior-art boundary

Classical components include DFT Parseval/Fejer spectral leakage, Doob h-transforms, Schur complements, Chebyshev/continuant spectral decimation, and Fourier proofs of Basel. Targeted search found direct prior art for DFT/Parseval Basel proofs and broad Schur/spectral-decimation machinery.

No historical-first claim is made. Candidate project synthesis remains the rough-observer organization: alias split probability + physical port collapse + observer-factorization uniqueness + discrete semigroup eigencharacter, all after explicitly rejecting microscopic differentiation as a default native observable.

## 7. Next

1. construct exact finite endpoint-orientation quotients for odd characters at s=2;
2. sharpen labeled finite character estimators using periodic cancellation;
3. explore the two-parameter mass-moment/label-moment phase around the unique neutral point (alpha,s)=(1,2) using finite inequalities only.
