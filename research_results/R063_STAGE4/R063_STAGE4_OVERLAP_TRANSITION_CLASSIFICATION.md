# R063 Stage 4 — Overlap Transition Classification

Status: `COMPLETE`

## 1. Strict additive maps

The local process label law is addition in `C4`. Every additive endomorphism is

`phi_m(x)=m x mod 4`, `m in {0,1,2,3}`.

The invertible unit-preserving maps are only

`x -> x` and `x -> -x` (`m=1,3`).

They all fix phase `0`.

Therefore a strict invertible transition cannot map a shared positive axis from local phase `0` to `1`, or from `1` to `0`.

For all three overlaps to have equal shared-axis phases one would need

`epsilon_12 != epsilon_23`,

`epsilon_23 != epsilon_31`,

`epsilon_31 != epsilon_12`,

which is impossible on a three-cycle.

Hence

`STRICT_C4_MONOID_OVERLAP_GLUE = NO_GO`.

## 2. Minimal affine survivor

Once the local phase orientation in each chart is frozen, the minimal choice-free map that matches the shared-axis phase while preserving all phase differences is the translation

`tau_k(x)=x+k mod 4`,

where `k = target_phase(shared_axis)-source_phase(shared_axis)`.

This is a torsor map, not a monoid homomorphism unless `k=0`.

The tensor defect is exact:

`tau_k(x) box tau_k(y) = tau_k(x box y) + k`.

Equivalently,

`(x+k)+(y+k) - ((x+y)+k) = k mod 4`.

So an affine transition is compatible with the process only as an **affine-monoidal transport with recorded defect**, not as a strict algebra isomorphism.

## 3. General affine automorphisms

The most general affine bijection of the `C4` torsor is

`F(x)=s x+k`, `s in {1,3}`.

Its tensor defect is still the constant `k`.

Allowing `s=3` introduces an extra phase inversion choice not forced by one shared-axis identification. Stage 4 therefore uses the pure-translation extension as the minimal transition, while separately checking that even the larger affine class cannot trivialize the loop.

## Verdict

- strict monoid gluing: `NO_GO`;
- affine torsor gluing: `EXACT WITH DEFECT`;
- route-independent affine trivialization: `NO_GO` by odd holonomy.
