# Native Enterprise C3 fold: projective prime-sieve uniformization

Status: `FREE_RESEARCH_EXACT_REPRESENTATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_SHELL_FIBER_COORDINATE_20260823.md`

## 1. Centered C3 fiber

For shell-fiber coordinate `(r,t)`, let

`c=N(r,t,1)=B_r+t+r`,

where `B_r=3r(r-1)/2+1`.

The three pre-collapse integer labels are exactly

`c-r`, `c`, `c+r`.

Thus a fully bright C3 prime fiber is a three-term prime arithmetic progression whose common difference is the native shell index `r`.

## 2. Projective q-readout

Fix a prime `q`. Whenever `(c,r)` is not `(0,0) mod q`, define the projective readout

`Pi_q(r,t)=[c:r] in P^1(F_q)`.

If `q does not divide r`, use affine slope

`z=c/r mod q`.

Then one of the three C3 entries is divisible by q exactly when

`z in {-1,0,+1}`.

Therefore the three bad affine directions are independent of shell and side position:

`FORBIDDEN_PROJECTIVE_SLOPES = {-1,0,+1}`.

This uniformizes the varying congruences of all shells into one fixed three-point mask.

## 3. Resonant shells are projective infinity

If `q|r` but `q does not divide c`, then

`[c:r]=[1:0]=infinity`.

All three labels are congruent to `c mod q`, so they simultaneously avoid q.

If `q|r` and `q|c`, all three labels are divisible by q and the pair `(c,r)` has no projective point; this is a killed fiber.

Thus for a fixed prime q, a shell divisible by q moves every surviving C3 fiber to the same safe projective point at infinity.

This is the projective form of the local root collapse:

- `q not divide r`: three forbidden t-residues, surviving fraction `(q-3)/q` for q>3;
- `q | r`: one forbidden t-residue, surviving fraction `(q-1)/q`.

The relative enhancement is exactly

`((q-1)/q)/((q-3)/q)=(q-1)/(q-3)`.

Hence the native primorial shell resonance ladder is a repeated projective-infinity recoalescence across small-prime readouts.

## 4. The universal 6-shell gate becomes geometric

For `q=2`, the three formal bad slopes `-1,0,+1` collapse to the two affine points of `F_2`, so every finite affine slope is forbidden. The only surviving projective point is infinity. Therefore a non-exceptional fully-prime C3 fiber requires

`2|r`.

For `q=3`, the three bad slopes are exactly all three affine points of `F_3`; again only infinity survives. Therefore

`3|r`.

Together:

`FULL_C3_PRIME_FIBER => 6|r`.

So the universal shell quantization is equivalent to saying that the q=2 and q=3 projective sieve skies force every fully bright fiber to infinity.

## 5. Midpoint curve inside the projective sieve

For the equal-coordinate midpoint `t=r/2`,

`c=(3r^2+2)/2`.

When q is odd and q does not divide r, its affine projective slope is

`z=(3r^2+2)/(2r)`.

The midpoint is killed when this slope equals one of `-1,0,+1`, equivalently when one of

`3r^2-2r+2`, `3r^2+2`, `3r^2+2r+2`

vanishes modulo q.

For q=3,5,7 the nonzero r-residues are completely covered, so a fully bright midpoint must satisfy q|r. Therefore the midpoint is forced to projective infinity simultaneously for q=2,3,5,7:

`FULL_BRIGHT_MIDPOINT => 210|r`.

At those shells all three midpoint labels recoalesce to `1 mod 210`.

For q>7, degree/root-slot bounds prevent complete nonzero-r coverage, so finite safe projective slopes survive. This is the exact transition from saturated recoalescence to branching survivor basins.

## 6. Projective survivor law

For q>3 and q not dividing r, a fully bright fiber obeys the universal shell-independent condition

`c/r not in {-1,0,+1} mod q`.

Thus the raw `(r,t)` sieve can be viewed through a projective normalization in which every prime q imposes the same three-hole affine mask. Shell factors q|r are singular/resonant events that send survivors to infinity and collapse those three holes into one killed t-class.

This yields the native interpretation

`SMALL PRIME FACTOR OF SHELL r`

`-> PROJECTIVE INFINITY RECOALESCENCE`

`-> THREE LOCAL OBSTRUCTIONS COLLAPSE TO ONE`

`-> C3 PRIME RESONANCE ENHANCEMENT`.

## 7. Finite scale check

In the exact full-bright census through `r<=5000`, there are 3919 fully-prime C3 fibers.

For several primes q and only fibers with `q not divide r`, the normalized affine slope `c/r mod q` never occupies `-1,0,+1`, as required. The surviving slope counts are already close to uniform on the allowed classes at this scale; for example:

- q=5: allowed slopes 2,3 occur 1310 and 1270 times;
- q=7: allowed slopes 2,3,4,5 occur 782,795,739,805 times.

This near-uniformity is only a finite diagnostic. The exact result is the three-point projective exclusion and infinity-recoalescence law.

## 8. Boundary

Projective lines over finite fields and local prime-tuple sieves are classical mathematics. No novelty claim is made for those objects themselves.

The research-specific content is the derivation chain from the native Enterprise shell allocation:

`(a,b,c), min=0`

`-> exact shell-fiber coordinate (r,t,sigma)`

`-> C3 fold (r,t)`

`-> centered fiber (c-r,c,c+r)`

`-> projective readout [c:r]`

`-> universal forbidden directions {-1,0,+1}`

`-> shell factors as projective-infinity recoalescence`.
