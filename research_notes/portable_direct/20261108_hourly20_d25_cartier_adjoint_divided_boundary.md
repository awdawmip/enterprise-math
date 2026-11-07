# D25 — Characteristic-p Cartier adjoint gauge and divided finite-boundary identity

Date: 2026-11-08 (Asia/Hong_Kong). Research lane: `chatgpt-research-hourly-enterprise-math-20260923`, distinct from `chatgpt-hourly-enterprise-math-20260921`.
Role: TASK_RESEARCH author-side portable, REGISTER_PENDING. Status: **algebraic proof / exact finite checks / UNREVIEWED / NOT_ADMITTED**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

This unit consumes the source-resolved reflected kernel and reciprocal Green defect (Research20 `47c8de70adfae20dd99a47eb804bb2dd72f87716`) and the separate on-hour lane's finite-adjoint and cutoff identities (current main `698f6bf033747ea7b2af46babb274b7a9f2689ac`, `81c998c1c846b925575b0f3e4f573a1ba21ec3f6`). The known formal adjoint itself is **predecessor input**, not newly claimed here. The new units are (I) complete rational/finite-field gauge classification and (II) a new cutoff `4m` Cartier-shifted exact **divided boundary** relation, with retained `(i,r,j)` source indices.

## 1. Common operator and new adjoint gauge

Let `D=t d/dt`, `a=18(1-2t)`,
[
L=(6D-1)(3D-1)-36tD^2=aD^2-9D+1,
]
and under the Laurent constant-term pairing `CT` let
[
L^*=(6D+1)(3D+1)-36D^2t
=aD^2+(9-72t)D+(1-36t).
]
For any characteristic different from 2 and 3 and any nonzero rational function `rho`, the operator identity `L^*(rho Y)=rho L Y` for **all** rational Laurent test functions `Y` is equivalent to
[
oxed{Dlogho=rac{4t-1}{2(1-2t)}=:q(t).}	ag{GAUGE}
]
The leading coefficients agree automatically. The first-derivative coefficient gives (GAUGE). Substitution in the zeroth-order coefficient gives the identity
[
a(Dq+q^2)+(9-72t)q-36t=0.
]
Over `Q(t)`, there is no nonzero rational `rho` satisfying (GAUGE): the necessary order at `t=0` is `-1/2`. On the quadratic cover the full family is
[
ho_{mathbb Q}=rac{c}{sqrt{t(1-2t)}}quad(c
e0).
]
In characteristic `p>3` prime, put
[
oxed{sigma_p(t)=[t(1-2t)]^{(p-1)/2}.}
]
It satisfies (GAUGE) in `F_p(t)` because `(p-1)/2=-1/2` in the field. Moreover **every** rational `F_p(t)` gauge is
[
oxed{ho(t)=sigma_p(t),phi(t^p),qquad
phiinmathbb F_p(t^p)^*.}	ag{CARTIER-GAUGE-CLASS}
]
Indeed `D(ho/sigma_p)=0` and the rational constants of `D` are precisely `F_p(t^p)`. This classification makes the Frobenius shift an explicit allowable branch operation rather than erasing it during a scalar observer readout.

## 2. New finite Cartier divided-boundary theorem (exact over Q)

Fix **any integer** `m>=1`, set `P=6m+1`, and define
[
w_i=2^{-i}{mchoose i}{2mchoose i},quad
W_m(t)=sum_{i=0}^{m}w_i t^{-i}.
]
Let `C_1=1/10` and `C_{r+1}/C_r=36r^2/((6r+5)(3r+2))`; take `N=4m`,
[
F_N(t)=sum_{r=1}^{N}C_rt^r,qquad
kappa_m=36N^2C_N,qquad
J=W_mDF_N-F_NDW_m.
]
The coefficient recurrence and reciprocal Gauss identity imply the **exact rational** equations
[
L F_N=t-kappa_m t^{4m+1},qquad
L W_m=-P(9D-2)W_m-P^2W_m.
]
Define the shifted Cartier weight
[
oxed{	au_m(t)=t^{-(3m+1)}(1-2t)^{3m}.}	ag{SHIFT}
]
The logarithmic derivative obeys an **exact rational** identity
[
D(a	au_m)=(-9-9P)	au_m.
]
Therefore the Green product rule yields the exact identity
[
oxed{
Digl(a	au_m Jigr)
=	au_m!left[tW_m-kappa_m t^{4m+1}W_m
+P{F_N(9D-2)W_m-9J}+P^2F_NW_might].
}	ag{CARTIER-FLUX}
]
Take Laurent constant terms. `CT(Df)=0`, `CT(t	au_mW_m)=(-2)^{3m}`, and `CT(	au_m t^{4m+1}W_m)=w_m`. Define a finite **source-resolved** index set
[
I_m={(i,r,j):0le ile m, 1le rle4m,0le jle3m, j=3m+1+i-r}.
]
Let `v_{irj}=w_iC_r(-2)^j {3mchoose j}`, retaining three independent source labels until the declared CT readout. Set
[
mathcal C_m=sum_{I_m}(18i+9r+2)v_{irj},
qquad
mathcal V_m=sum_{I_m}v_{irj}.
]
Since `CT(tau[F_N(9D-2)W_m-9J])=-mathcal C_m`, (CARTIER-FLUX) gives
[
oxed{
kappa_m w_m-(-2)^{3m}=-Pmathcal C_m+P^2mathcal V_m.
}	ag{DIVIDED-BOUNDARY-Q}
]
This is an **all-m exact identity in Q**, not a numerical conjecture. It is a different adjoint channel from the on-hour `m`-cutoff resonance: its Cartier shift uses `4m` exact coefficients and explicitly retains the characteristic-p boundary.

For every prime `p=6m+1>3`, the rational numbers `C_1,...,C_{4m}`, `w_i`, and `kappa_m` are p-integral. In the recurrence the first p-dividing denominator is the next `3r+2=2p` factor at `r=4m`, which enters `C_{4m+1}`, excluded here. Reducing (DIVIDED-BOUNDARY-Q) gives the unconditional arithmetic conclusions
[
oxed{kappa_mw_mequiv(-2)^{3m}pmod p,}
qquad
oxed{rac{kappa_mw_m-(-2)^{3m}}pequiv-mathcal C_mpmod p.}	ag{FIRST-DIGIT}
]
The quotient is well defined in `Z_(p)/p` by the first congruence.

## 3. Exact computation and observer distinction

A standalone Python standard-library checker verifies the all-m rational identity for `m=1,2,3,4,7`; the gauge conjugacy `L^*(sigma_p t^n)=sigma_p L(t^n)` for `n=-3,-1,0,1,4` and every one of the **80 primes** `7<=p<1000`, `p=1 mod6`; and both first/second-digit finite-ring checks for all those primes. Selected `(p,m,first_digit,V modp)`:
[
(13,2,2,9), (19,3,7,9), (43,7,5,1),(67,11,5,41), (373,62,266,36), (997,166,820,849).
]

The raw original frozen reflected `R_p` differs from this **new** Cartier boundary observer: `R_13=0` while the boundary digit is `2`; `R_19=12` while the boundary digit is `7`. Thus (FIRST-DIGIT) is a new valid second-digit source constraint, **not** the mother LIFT itself. It can serve as a discriminating intermediate identity for prospective Fricke/Cartier transfer operators. The full `(i,r,j)` fiber is retained for subsequent signed/cutoff-sensitive operations; `mathcal C_m` and `mathcal V_m` are declared observer quotients only.

## 4. Continuation and control

Frozen parent objective remains `Delta_p=((G_p/p)h-1)/p == original R_p (modp)` for `p=13,19 mod24`, using accepted D24 UR/JT0 as input. The next exact question: find, or distinguish through p=19 and 373, a source-preserving transfer from the Cartier `4m` boundary digit/volumetric fiber to the on-hour finite adjoint resonance `E_m` and the original Gauss ports `(ZH0-1)/p, SH0, ZH1, Phi_xx`. A candidate transfer must account for the separately observed `R_p - boundary_digit`, not set it to zero by choosing free lifts.

Native status/receipt in this run: `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Original requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` remain protected; current old session/claim/uploads cannot be conclusively projected. No session start, CLAIM, OPEN, Source native checkpoint, freeze, review, or native p373 experiment is asserted. Recovery support `#1558`; separate native p373 experiment `#1559`. Research activity native registration remains pending.

Research status: `AUTHOR_SIDE_PROVED_ALGEBRA / FINITE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED`.
