# BRC_CARRIER_ORDER_LADDER — higher-order precision carriers for the Xi saddle route

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`

Status:

`CARRIER_ORDER_EXPONENT_LADDER_DERIVED / LOG_DEPTH_LINEAR_REMAINDER / INERTIA_BRIDGE_OPEN / RH_NOT_CLOSED`

## 1. Input from the published cubic-wedge proof

Let `f=log a` be the analytic interpolation of the positive Xi coefficients, let

`tau=tau_k=-log(a_(k-1)a_(k+1)/a_k^2)`,

and let

`t=4 sqrt(r tau)`, `w=t/tau`.

The published certified bounds used here are

`1/(2k)<tau<4/k`

and, for every degree `d>=3`,

`|f^(d)(k)/d!| <= 2*80^d*tau^(d-1)`

after normalization by `tau`.

The centered logarithmic remainder has the exact expansion

`h(s)=sum_(d>=3) a_d P_d(s)`,

with

`P_d(s)=s^d-s` for odd `d`,
`P_d(s)=s^d-s^2` for even `d`.

The published comparison model keeps only the quadratic carrier and treats all `d>=3` as
perturbation. Its leading whitened remainder is what produces the `r^3/k` scale.

## 2. Degree-m carrier split

For an integer `m>=2`, define the retained carrier

`h_<=m(s)=sum_(3<=d<=m) a_d P_d(s)`

(with the empty sum for `m=2`) and the unresolved tail

`h_>m(s)=sum_(d>=m+1) a_d P_d(s)`.

Put

`d0=m+1`,
`d_odd=min{d>=d0:d odd}`,
`d_even=min{d>=d0:d even}`.

Repeating the weighted-algebra estimate degree by degree gives the exact tail bound

`||h_>m||_A <= MAIN_m + ODD_m + EVEN_m`,

where

`MAIN_m = (2/tau)*(80t)^d0/(1-80t)`,

`ODD_m = 2t*80^d_odd*tau^(d_odd-2)/(1-(80tau)^2)`,

`EVEN_m = 2t^2*80^d_even*tau^(d_even-3)/(1-(80tau)^2)`.

This is valid whenever `80t<1` and `80tau<1`; it is exactly the published nonlinear
majorant with the first unresolved degree moved from `3` to `m+1`.

Consequently

`||exp(h_>m)-1||_A <= exp(||h_>m||_A)-1`.

The only new requirement is that the retained degree-m comparison carrier must have its
inertia/sign certified nonperturbatively.

## 3. Fixed carrier order gives an exponent ladder

Let `d=d0=m+1`. The leading term has scale

`(1/tau)*(sqrt(r tau))^d
 = r^(d/2) tau^(d/2-1)`.

Since `tau=Theta(1/k)` in the certified curvature window, the dimensionless leading scale is

`r^(d/2) k^(1-d/2)`.

For a power-law tail `k=C r^p`, uniformity in `r` requires

`p >= d/(d-2)=(m+1)/(m-1)`.

Thus the carrier-order ladder is

| retained through degree m | first omitted d | natural power p=d/(d-2) |
|---:|---:|---:|
| 2 | 3 | 3 |
| 3 | 4 | 2 |
| 4 | 5 | 5/3 |
| 5 | 6 | 3/2 |
| 6 | 7 | 7/5 |
| 9 | 10 | 5/4 |

and

`p_m=1+2/(m-1) -> 1`.

This identifies the published cubic wedge as precisely the `m=2` member of a hierarchy of
possible precision carriers. The analytic tail does not privilege exponent `3` once higher
centered modes are retained rather than collapsed into one error term.

## 4. The linear critical scale needs only logarithmic carrier depth analytically

Now take

`k=C r`

and suppose `C>409600`. From `tau<4/k`,

`t<=8/sqrt(C)`

and hence

`rho:=80t <= 640/sqrt(C)<1`.

The leading unresolved tail satisfies, using also `tau>1/(2k)`,

`MAIN_m <= 4 C r * rho^(m+1)/(1-rho)`.

Therefore any choice

`m+1 >=
 log(4 C r/(epsilon(1-rho)))/(-log rho)`

makes the leading tail at most `epsilon`.

The odd/even centering corrections are controlled by the exact formulas of Section 2 and
carry additional positive powers of `tau`; for increasing `m` they decay still faster on a
linear wedge.

Hence, for fixed `C>409600`, an analytic remainder smaller than any fixed epsilon can be
obtained with

`boxed: m=O(log r)`.

This is an analytic statement about the **unresolved tail only**. It does not prove that the
retained degree-`m` comparison model has the required inertia.

## 5. Numerical scale illustration

Take `C=10^6`, so the conservative response ratio is `rho<=0.64`. At

`r=10^13`, `k=10^19`,

retaining centered modes through degree `m=108` makes the direct worst-case evaluation of the
Section-2 tail bound about `1.04e-2`; the centering correction terms are negligible on this
scale.

This is `EVIDENCE_ONLY` for scale intuition. The important theorem is the logarithmic-depth
bound above.

## 6. BRC interpretation

This produces a second refinement axis independent of branch width:

`quadratic carrier -> cubic carrier -> quartic carrier -> ...`

A low-order carrier is cheap but leaves a large future-support uncertainty (large perturbative
remainder). When the current `(r,k)` state enters a region where that carrier is unsafe, BRC
should **refine the carrier order on demand** instead of globally replacing the entire proof by
an infinite Taylor object.

For every finite `m`, the future tail is explicitly bounded. The unknown mathematical object is
therefore finite-dimensional:

`INERTIA_m(q,a_3,...,a_m)`.

No future refinement may forget these retained mode parameters if later sign propagation uses
them; doing so would violate `NO_RESURRECTION`.

## 7. The real hard bridge exposed by the ladder

The analytic continuation/saddle side is strong enough to support the entire ladder. The
missing theorem is:

`HIGHER_ORDER_INERTIA_BRIDGE`:

> certify the sign/inertia of the centered degree-m comparison block, uniformly in the
> Xi-admissible parameter box, with a mechanism stable as `m` grows (ideally up to
> logarithmic depth on `k=Cr`).

Potential representations include:

- a homotopy that adds centered modes one at a time and branches only at possible eigenvalue
  crossings;
- a finite feature-lift of the mixed polynomial kernel after row/column factors are removed;
- an exact higher-order deformation of the q-Pascal/Toda carrier.

Until such an inertia theorem exists, the exponent ladder is a route map, not a positivity
proof.

## 8. Classification

Proved/derived from the published certified coefficient bounds:

- exact degree-m unresolved-tail formula;
- fixed-order exponent ladder `(m+1)/(m-1)`;
- logarithmic carrier depth suffices to make the **analytic tail** small on a fixed linear wedge.

Open:

- higher-order comparison inertia;
- RH.

Final status: `RH_NOT_CLOSED`.
