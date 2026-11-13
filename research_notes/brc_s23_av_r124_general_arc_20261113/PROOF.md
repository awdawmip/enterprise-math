# R124 — Four-integer joint S23 oracle without endpoint pre-atomization

Date: 2026-11-13. Author-side auxiliary proof and exact finite tests. Predecessor: R123 source commit `c5e7cb5aaa31be2d12f261c9efd6db9e5563fc9c`. Frozen scientific input remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. P000/native X6 and original source provenance are unmodified. This is **not** native Cell/Link/Port event permission or independently reviewed mathematics.

## Statement

For rational `x,l,h` with `l<h`, integers `N,d,j,a,c`, and `m>=2`, take the original S23 directed half-open auxiliary observer
[
M_t(	heta)=mathbf1{operatorname{frac}(x+(t-j)	heta)in[operatorname{frac}(a	heta),operatorname{frac}(c	heta))_{m directed}}.
]
Coincident endpoints define the **empty** directed arc. Let the new times be `t_i=N+i*d`, `0<=i<m`. On the open rational parameter interval `J=(l,h)`, for every prescribed bit word `b in {0,1}^m`, joint attainability is exactly equivalent to the union of finitely many **mixed rational-linear systems with only four integer variables** `n,k,p,q` and one real `theta`. No pre-splitting at the potentially numerous integer crossings of `a theta`, `c theta`, `(a-c)theta` is necessary.

The construction admits arbitrarily signed integers, `a=c`, `d=0`, wrapped arcs, zero-width subsegments, and parameter points where the endpoints coincide. A singleton parameter atom is evaluated directly.

## Construction and proof

Put `Y_i=x+(N+i*d-j)theta`, `D=d theta`, `alpha=a theta-p`, `gamma=c theta-q`, and `z_i=Y_i-(n+i k+w_i)`. Enumerate lift vectors in the standard finite vocabulary
[
P_m={(lfloor alpha_0+ietafloor)_{i=0}^{m-1}:0lealpha_0,eta<1}.
]
The prior R121-LIT source attributes the exact finite Sturmian count `|P_m|=1+sum_{r=1}^{m-1}(m-r)phi(r)=Theta(m^3)`. Alternatively enumerate the self-contained larger set of all prefix sums of `m-1` binary increments, retaining only actual feasible systems.

For each `w`, impose simultaneous constraints:
[
l<	heta<h,quad ple a	heta<p+1,quad qle c	heta<q+1,
]
[
nle Y_0<n+1,quad kle d	heta<k+1,quad 0le z_i<1quad (0le i<m).
]
Select exactly one of `alpha<gamma`, `alpha>gamma`, or `alpha=gamma`. For each requested bit `b_i`, choose one allowed fractional-phase segment and impose `L_i(theta)<=z_i<U_i(theta)`:

| Endpoint order | bit 1 | bit 0 |
| --- | --- | --- |
| `alpha<gamma` | `[alpha,gamma)` | `[0,alpha)` OR `[gamma,1)` |
| `alpha>gamma` | `[alpha,1)` OR `[0,gamma)` | `[gamma,alpha)` |
| `alpha=gamma` | impossible | `[0,1)` |

All conditions are rational-affine in `theta,n,k,p,q`. Strict upper and weak lower segment endpoints remain exactly as prescribed.

**Completeness.** A genuine `theta` gives the true floors `p=floor(a theta)`, `q=floor(c theta)`, `n=floor(Y_0)`, `k=floor(d theta)`. With `alpha_0=Y_0-n` and `beta=d theta-k`, the identity
[
lfloor Y_ifloor=n+i k+lflooralpha_0+ietafloor
]
proves that one enumerated `w` gives `z_i=frac(Y_i)`. Exactly one order branch and an allowed phase segment represent each actual bit. **Soundness.** Conversely, the four floor inequalities force the intended floor variables and the `0<=z_i<1` inequalities force `n+i k+w_i=floor(Y_i)`. The selected segment exactly expresses the original directed arc bit, including phase equality. Therefore every feasible system yields one genuine *joint* rational-phase witness; it does not combine separately attainable bits. QED.

## Complexity

For each `w`, endpoint order and segment selection, there are `O(m)` affine inequalities. Fourier–Motzkin elimination of the **one real** `theta`, retaining strictness when either paired bound is strict, gives `O(m^2)` rational-linear inequalities in the **four integers** `n,k,p,q`. Clearing denominators and shifting integer strict inequalities by one produces an ordinary fixed-dimensional integer linear feasibility instance. Its coefficient bit lengths and floor bounds remain polynomial in the original rational input size. Fixed-four-variable integer programming therefore has polynomial binary-input complexity by the classical theorem of H. W. Lenstra Jr. (1983), *Mathematics of Operations Research* 8(4), 538–548, DOI `10.1287/moor.8.4.538`. The integer solution gives a rational `theta` by exact interval intersection; when the permitted intersection is a weak singleton, take that singleton instead of a midpoint.

At most `3*2^m*|P_m|=O(2^m*m^3)` instances are needed for **one prescribed** bit word; all signatures can be enumerated with at most another `2^m` factor. For *fixed m* this gives polynomial bit complexity in the lengths of `N,d,a,c,j,x,l,h`; notably no factor linear in `|a|,|c|,|N|,|d|`. Previous historical atom construction, ranking-tree maintenance, full-output size and native-X6 permission are separate and not subsumed. If endpoint floors and order are already fixed, substituting `p,q` recovers the earlier two-integer R121–R123 construction.

## Verification

A stand-alone Python 3 `fractions.Fraction` tester implements bounded exhaustive `p,q,n,k` floor search for **small inputs**, all three endpoint orders, all binary-prefix lift candidates and exact affine `theta` interval intersections. Independently, a complete finite phase-cut enumerator cuts on integer crossings of `a theta,c theta,(a-c)theta,Y_i,Y_i-a theta,Y_i-c theta`, tests every interior cut point and rational open-gap midpoint using the original literal predicate, and compares sets of attained signatures.

Executed `R124_GENERAL_ARC_LATTICE_PASS` with seed 12420261113: **201 cases**, **1,082** attained signatures and **1,082** independent rational witness checks, including 28 cases `a=c`, 80 negative `d`, 22 zero `d`, and 63 cases with `m=4`. Four further **positive** floor-identity certificates use signed 121-digit `N` and 95-digit `d` without full phase atomization. Testing fixed the initially discovered branch-collapsing bug: multiple feasible phase segments sharing a partial bit prefix must **not** be deduplicated before later bits. Regression: `x=3/2; (N,d,j,a,c)=(-1,3,0,1,3); J=(-1,4/3); m=3`, where `110` occurs at both `theta=-1/4` and `3/4`.

The finite test validates the lift construction and half-open boundaries; **it does not implement or benchmark Lenstra's fixed-dimensional algorithm**, so no measured asymptotic speedup is claimed. The complete locally executed Python source has SHA-256 `f81bfcaf893cf33160e9670a2f80601e107b0ffab412a1c1f86068f781d48e1c` and its exact output JSON has SHA-256 `7f3cc08d0b04c3e6e672e72174aebd786fc0607bcf249dca33b98ed917fef643`. Full source and raw test evidence are preserved in the accompanying local research archive; source persistence to this GitHub branch is separately tracked, not inferred from these hashes.

## Next

Implement and verify an actual exact four-variable feasibility solver (not float MILP); compare total preprocessing, word enumeration, integer bit cost, witness recovery and historical root costs against endpoint pre-atomization + R123. Try to remove one endpoint-floor integer in useful signed special cases without discarding branch/provenance information. Independent mathematical review, native admissibility and formal CLAIM remain separate.
