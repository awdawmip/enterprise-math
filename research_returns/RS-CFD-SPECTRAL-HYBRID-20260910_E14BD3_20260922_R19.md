# CFD continuation R19: sharp Source=0 RK4 viscous lower bound

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-RK4MIN-E14BD3`  
Claim: `CLM-CFD-E14BD3-20260922-0049-R19`  
Activity: `RA-CFDRK4MIN-E14BD3-20260922`  
State: `CONTINUATION_REQUIRED / EXACT FINITE RK4 SHARP-MINIMUM CERTIFICATE / NO NATIVE-HOST CLAIM`

## Frontier consumed without replay

This unit consumes R18 at `a1aea28fa0d854241ea357d16c4e0b1aff85da5b` without replaying its 4,220 SOS checks, 87,500 semilinear decompositions, or support-loss/cancellation cases. R18 established, for Source=0 and one unmasked retained Fourier mode under classical fixed-step RK4,

`R(-x)=1-x+x^2/2-x^3/6+x^4/24`, `x=h nu |k|^2>=0`,

and used the simple uniform bound `R(-x)>=1/4` to obtain a conservative nonlinear no-loss certificate.

The separate trajectory-verifier line is not claimed or modified here. The frozen R15/6D3A91 native benchmark manifest is unchanged.

A fresh capability probe in this execution environment again found `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, and `pyfftw` unavailable, with no `mpicc`, `mpicxx`, or `mpirun`. No native spectralDNS/shenfun/MPI/FFTW run is claimed.

## New exact result 1: the global lower bound is strictly larger than 1/4 and can be made sharp

Let

`p(x)=R(-x)=1-x+x^2/2-x^3/6+x^4/24`.

Then

`p'(x)=q(x)/6`, where `q(x)=x^3-3x^2+6x-6`.

The derivative of `q` has the exact form

`q'(x)=3((x-1)^2+1)>0`

for every real `x`. Therefore `q` is strictly increasing. Since `q(0)=-6` and `q(x)->+infinity`, it has a unique positive zero `x_*`, and `p` decreases before `x_*` and increases after `x_*`. Thus `x_*` is the unique global minimizer of `p` on `[0,infinity)`.

There is a second exact identity,

`24 p(x)-x^4=-4 q(x)`.

At the minimizer `q(x_*)=0`, hence the exact sharp global minimum is

`mu = p(x_*) = x_*^4/24`.

A rational isolation check gives

`1596071/1000000 < x_* < 1596072/1000000`,

so `x_*` is approximately `1.5960716379833215`.

Equivalently, the real Cardano root can be written

`x_*=1+cuberoot(1+sqrt(2))+cuberoot(1-sqrt(2))`,

using real cube roots.

## New exact result 2: an algebraic certificate for the sharp constant

Eliminating `x_*` between `q(x_*)=0` and `mu=x_*^4/24` yields

`32 mu^3 - 12 mu^2 + 12 mu - 3 = 0`.

The checker verifies the stronger polynomial factor identity

`r(x^4/24)=q(x)(x^6-3x^4+36)(x^3+3x^2+6x+6)/432`,

where `r(mu)=32mu^3-12mu^2+12mu-3`.

Moreover,

`r'(mu)=96(mu-1/8)^2+21/2>0`

for all real `mu`, so `r` has exactly one real zero. Exact rational signs isolate it as

`54078953/200000000 < mu < 135197383/500000000`,

that is,

`0.270394765 < mu < 0.270394766`.

High-precision evaluation is approximately

`mu = 0.2703947652051846079624596133831109...`.

Thus R18's convenient uniform lower bound `1/4=0.25` was valid but not sharp. The exact sharp constant is about `8.157906082%` larger. Even without algebraic-number arithmetic, the rational value

`mu_safe = 54078953/200000000 = 0.270394765`

is a certified implementation-safe lower bound and improves the old `1/4` threshold by more than `8.157906%`.

## Consequence for the Source=0 nonlinear no-loss certificate

R18 gave the exact semilinear RK4 decomposition

`u_{n+1,k}=R(-x)u_{n,k}+C_k`

with

`C_k=h(b1 N_1+b2 N_2+b3 N_3+b4 N_4)`.

Its strongest mode-specific gate remains unchanged:

`h sum_j |b_j| ||N_j|| < R(-x)||u_{n,k}||  =>  u_{n+1,k} != 0`.

R19 improves only the *uniform* Source=0 substitute used when one does not want to evaluate the mode-specific `R(-x)`:

`h sum_j |b_j| ||N_j|| < mu ||u_{n,k}||  =>  u_{n+1,k} != 0`.

For rational-only fail-closed code, the slightly conservative but certified rule is

`h sum_j |b_j| ||N_j|| < (54078953/200000000)||u_{n,k}||`.

This is strictly stronger than R18's `1/4` gate while remaining uniform over every `x=h nu |k|^2>=0`.

Sharpness matters: no larger universal constant can replace `mu`, because the pure homogeneous RK4 factor actually attains `mu` at `x=x_*`. This does **not** establish support monotonicity in nonlinear Navier-Stokes; it only reduces the region in which a Source=0 support-loss event could plausibly be attributed to nonlinear cancellation.

## Executable verification

`research_checks/RS_CFD_SPECTRAL_HYBRID_E14BD3_R19.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic for the proof obligations. It verifies:

- exact polynomial coefficients for `q'(x)=3((x-1)^2+1)`;
- exact identity `24R(-x)-x^4=-4q(x)`;
- exact elimination/factor identity producing `32mu^3-12mu^2+12mu-3`;
- exact root-isolating signs for both `x_*` and `mu`;
- strict positivity of the derivatives of `q` and `r`;
- strict certified improvement over `1/4`;
- 12,001 rational grid transcription checks;
- 42,504 finite scalar no-loss witnesses under the strengthened rational uniform gate.

`python -m py_compile` passes. The checker SHA-256 is
`66c9db37ceaf05ec3a20be8976bb41d96e7470329bda26199892bd2942598485`.

The machine-readable result is
`research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_E14BD3_R19/sharp_rk4_certificate.json`.

The finite grid/witness loops are regression checks, not the continuum proof. The continuum statement follows from the exact polynomial identities, strict derivative positivity, and rational root isolation.

## Native-run implication and boundary

For the next provisioned pinned-host run, R18's per-mode diagnostic should continue to record the actual `R(-x_k)` because that is stronger than any uniform constant. R19 adds a useful fail-closed cross-check: an unmasked Source=0 mode cannot be lost by an exact semilinear RK4 step if the recorded nonlinear correction bound is below `mu_safe ||u_n||`. A support-loss event below that margin points away from mathematical nonlinear cancellation and toward instrumentation error, masking/Nyquist action, or floating implementation effects; it is not itself proof of which alternative occurred.

This is an exact finite classical-RK4/spectral-mode result only. It is not a native spectralDNS benchmark, not evidence of speedup or slowdown, not a generic CFD or industrial acceleration claim, not a continuous-PDE theorem, and not independent final acceptance. It does not justify `M=0` from a support-saturation snapshot and does not alter the frozen benchmark protocol.

## Smallest unresolved unit

The parent task still requires the provisioned pinned spectralDNS/shenfun/MPI/FFTW host run and independent trajectory review. Execute the frozen native benchmark unchanged. For any Source=0 support-loss event, retain the R18 mode-level cancellation diagnostics and additionally compare the observed nonlinear correction against the R19 sharp/uniform lower-bound certificate. Keep any permanent-dense latch in its separately predeclared diagnostic arm. Return the immutable native checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910`; do not mark the parent task DONE before native-host evidence and independent review.
