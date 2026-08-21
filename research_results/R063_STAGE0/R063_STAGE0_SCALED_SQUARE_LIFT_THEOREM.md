# R063 Stage 0 — Scaled-square lift theorem

## Statement

Let `N=r^2` with `r>=1`. Define C3 from the integer factorization of `r` by enumerating divisors `k|r`, putting `h=r/k`, constructing Gaussian roots `m+nJ` of norm `h`, and retaining the canonical channels:

- axis channel: `h=1, (m,n)=(1,0)`;
- nondegenerate channel: `m>n>0`, `gcd(m,n)=1`, and `m,n` have opposite parity.

For each canonical channel form

`alpha = k(m+nJ)^2 = k(m^2-n^2) + 2kmn J`,

and retain both ordered nonnegative component orientations when distinct.

Then the deduplicated C3 output is exactly

`{(a,b) in N_0^2 : a^2+b^2=r^2}`.

## No-extra proof

Every generated channel satisfies

`[k(m^2-n^2)]^2 + (2kmn)^2 = k^2(m^2+n^2)^2 = r^2`.

Hence C3 produces no extra branch.

## Completeness proof

Take any nonnegative ordered solution `a^2+b^2=r^2`.

If one component is zero, the axis channel with `k=r,m=1,n=0`, followed by the ordered orientation rule, generates it.

Otherwise set `d=gcd(a,b)`. Prime valuations in `d^2 | r^2` imply `d|r`. Dividing by `d` gives a primitive integer Pythagorean triple. The classical primitive Pythagorean classification supplies unique `m>n>0`, `gcd(m,n)=1`, opposite parity, with

`r/d=m^2+n^2`

and the two primitive legs equal to `m^2-n^2` and `2mn` up to order. Therefore C3 visits `k=d`, reconstructs the branch, and its orientation rule restores the original ordered pair.

Thus C3 is complete for every square native norm, not only the central finite case.

## Evidence

- N=2500 exact equality against the post-freeze brute oracle: `True`.
- N=2500 extras: `0`.
- Regression `1<=r<=512` combined C3/C4 checker mismatch count: `0`.

Raw noncanonical scaled-square channels are retained as derivation provenance, but are quotiented before the component-root/trace branch is returned. This is why algebraic derivation multiplicity can exceed one without multiplying the native trace branch itself.
