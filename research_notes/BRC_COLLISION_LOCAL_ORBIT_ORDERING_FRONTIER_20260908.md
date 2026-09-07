# BRC Collision Local-Orbit Ceiling and Boundary-Ordering Comparator

Status: `RESEARCH FRONTIER / EXACT FINITE-FIELD QUOTIENT + RSA270 LOCAL RESIDUE LIFT + ORDERING-ORACLE REDUCTION + SCOPED ORIENTATION-LOSS NO-GO / NO FACTORIZATION SPEEDUP CLAIM`
Date: `2026-09-08`
Parent:
- `research_notes/BRC_MULTIPLIER_BOUNDARY_COLLISION_SPECTRUM_20260908.md`
- `research_notes/BRC_MULTIPLIER_COLLISION_ENERGY_TRACE_20260908.md`
Source snapshot at start: `main@3b0ffb055e74f39f5d140a47b8ceb0ed5e1f1293`

## 0. Question and BRC typing

Let `N=pq` with distinct odd primes `p<q`, put `S=p+q`, `g=q-p`, and retain the three-boundary collision energy

`E3 = p^2+q^2+(q-p)^2 = 2*S^2-6*N = 2*(N+g^2)`.

The previous frontier isolated the only open route as an `N`-visible evaluator that exposes more of `E3` than the fixed universal residue shadow.

This continuation separates two observer classes:

1. **local modular quotient** — reduce the hidden factor residues modulo a fixed modulus and ask what value of `S^2`, `g^2`, or `E3` survives without choosing a factor branch;
2. **archimedean boundary ordering** — retain only the order between two labeled hidden boundaries, not their values.

The first admits an exact local ceiling. The second is much stronger: one order bit is an exact factor-ratio comparison bit. Current square-gap BRC loses precisely that orientation bit because it squares the signed imbalance.

No positive Weighted-BRC mass identification is used. The adequate carrier is labeled factor-split provenance until the declared quotient is proved safe.

---

## 1. Prime-field product fiber and the exact `S^2` orbit quotient

Fix an odd prime `ell` with `ell` not dividing `N`, and write

`n = N mod ell`.

A local factor branch is represented by any `a in F_ell^*`, with

`b=n/a`.

The hidden squared factor-sum residue on that branch is

`Y(a)=(a+n/a)^2`.

Two branches have the same `Y` exactly when

`b in {a, n/a, -a, -n/a}`.

Indeed, if

`b+n/b = a+n/a`,

then

`(b-a)(ab-n)=0`;

and if

`b+n/b = -(a+n/a)`,

then

`(a+b)(ab+n)=0`.

Thus `Y` is precisely the orbit quotient of `F_ell^*` by the Klein four action

`a -> a`, `a -> n/a`, `a -> -a`, `a -> -n/a`.

Burnside gives the exact number of distinct `S^2` residues compatible with the N-only product fiber:

`c_ell(n) = (ell+1+chi(n)+chi(-n))/4`,

where `chi` is the Legendre symbol modulo `ell`.

Because `g^2=(b-a)^2=Y-4n` and `E3=2Y-6n`, the same orbit count applies to the possible `g^2` and `E3` residues modulo every odd `ell`.

This is an exact observer statement: `N mod ell` fixes the product fiber, while selecting one of the `c_ell(n)` orbits is additional factor-residue provenance.

---

## 2. Consequence: only `ell=3` and the special `ell=5` case can collapse to one free residue

If `ell == 3 mod 4`, then `chi(-n)=-chi(n)` and

`c_ell(n)=(ell+1)/4`.

If `ell == 1 mod 4`, then

`c_ell(n)=(ell+1+2*chi(n))/4`.

Hence:

- `ell=3`: one `S^2` orbit;
- `ell=5`: one orbit exactly when `N` is a quadratic nonresidue modulo 5;
- every prime `ell>=7`: at least two distinct `S^2`/`E3` orbits remain.

So no fixed prime modulus `ell>=7` can yield a unique hidden collision-energy residue from the product residue alone. Any such unique output must include an additional orbit selector, i.e. factor-sensitive provenance.

This is stronger than saying a particular residue heuristic failed: it exactly counts the quotient fibers left after local product collapse.

---

## 3. RSA-270 gets one genuine extra free local factor: `5`

For RSA-270,

`N mod 5 = 2`,

which is a quadratic nonresidue modulo 5. Therefore the `ell=5` quotient has one orbit and

`S^2 == 4 (mod 5)`.

For odd prime factors above 3, the parent result already gives

`S^2 == (N+1)^2 (mod 576)`.

For the actual RSA-270 integer these combine to

`S^2 == 1984 (mod 2880)`,

`g^2=S^2-4N == 36 (mod 2880)`,

and therefore

`E3=2(N+g^2) == 2486 (mod 5760)`.

So the previous universal `576` wall was not the exact RSA-270 local wall: the concrete residue `N mod 5=2` supplies one additional N-only prime-field collapse.

This is still classical local arithmetic, not a new factoring mechanism.

### Interaction with the RSA Challenge `e=3` construction-family prior

The durable RSA-270 checkpoint conditionally carries `p==q==2 (mod 3)`, from which the existing line derived

`S == 16 (mod 72)`.

Combining that with the new free `mod 5` information gives

`S mod 360 in {88,232}`.

Thus the new local collapse contributes a small constant amount of additional information under the same prior; it does not alter the exponential-scale search conclusion.

---

## 4. Prime-power maximality for the current RSA-270 residue classes

The local singleton does not continue indefinitely up prime powers.

For RSA-270:

### 2-adic next lift fails

`N == 55 (mod 128)`.

Two unit factor-residue branches are

`(a,b)=(1,55)` and `(3,61)`,

both having product `55 mod 128`, but

`(a+b)^2 == 64` and `0 (mod 128)` respectively.

Thus the free `2^6` information does not uniquely lift to `2^7`.

### 3-adic next lift fails even under `p,q==2 mod3`

`N == 19 (mod 27)`.

The two branches

`(2,23)` and `(8,26)`

both have both coordinates `2 mod3`, both multiply to `19 mod27`, but give

`S^2 == 4` and `22 (mod27)`.

Thus the conditional Challenge residue prior does not uniquely lift the free `3^2` information to `3^3`.

### 5-adic next lift fails

`N == 7 (mod25)`.

Already the unit branches produce five distinct `S^2 mod25` values; for example

`(1,7) -> 14`, `(2,16) -> 24`, `(3,19) -> 9`, `(4,8) -> 19`, `(11,12) -> 4`.

Therefore the concrete local singleton stops at `5^1`.

Scoped conclusion for fixed residue-only product-fiber observers on RSA-270:

`FREE_UNIQUE_SQUARED_SUM_MODULUS = 2^6 * 3^2 * 5 = 2880`.

This is a local observer ceiling, not a lower bound against nonlocal magnitude/order algorithms.

---

## 5. Enriching the fixed local shadow with `m=7` root/remainder residues still does not select the orbit

A finite exact collision witness sharpens the current `N/J/R` shadow boundary.

The semiprimes

`43823 = 13*3371`

and

`3097 = 19*163`

both satisfy `N==3 mod7` and have the identical compressed BRC tuple

`(N, J_1,R_1,J_3,R_3,J_7,R_7) mod7`

`=(3,6,2,5,5,0,0)`,

where `J_m=floor(sqrt(mN))`, `R_m=mN-J_m^2`.

But their hidden squared sums differ:

`(13+3371)^2 == 2 (mod7)`,

`(19+163)^2 == 0 (mod7)`.

So adding the same-prime multiplier state `m=7` to the low residue shadow does not provide an exact local orbit selector. This is a finite counterexample for the declared compression only, not a universal lower bound against every use of full integer root trajectories.

---

## 6. Boundary-ordering comparator theorem

The modular route is locally exhausted, but boundary **ordering** is much stronger.

Let

`A=(S-2)/2`.

For positive integers `u,v`, the pure odd-split boundaries satisfy

`L_(2u+1,1)=A+u*p`,

`L_(1,2v+1)=A+v*q`.

Therefore exactly

`L_(2u+1,1) < L_(1,2v+1)`

iff

`u*p < v*q`

iff

`u/v < q/p`.

Thus one cross-multiplier boundary-order bit is one exact rational comparison bit for the hidden factor ratio.

This is an oracle reduction, not yet an evaluator.

---

## 7. The same order bit is an exact threshold bit of the three-boundary energy

Put

`R=q/p>1`.

Then

`S^2/N = R+2+1/R`.

The right side is strictly increasing for `R>1`. For a meaningful threshold `u/v>1`,

`R>u/v`

iff

`S^2 > N*(u+v)^2/(u*v)`.

Using `E3=2*S^2-6*N`, this is equivalently the integer comparison

`u*v*E3 > 2*N*(u^2-u*v+v^2)`.

So the two formerly separate attack objects are identical at the one-bit level:

`BOUNDARY_ORDER_BIT = ARCHIMEDEAN_THRESHOLD_BIT_OF_E3`.

The modular route asks for residues of `E3`; the ordering route asks whether `E3` lies above chosen rational thresholds.

---

## 8. Why a poly-bit ordering evaluator would be a genuine break

Suppose an evaluator answers the ordering query for arbitrary `u,v` with cost polynomial in the bit lengths of `N,u,v`.

Assume only a constant factor-ratio bound `1<R<C`, as in the RSA Challenge equal-length-prime regime. Binary search on rational thresholds determines `R` to interval width below `1/sqrt(N)` in `O(log N)` queries.

Since

`p(R)=sqrt(N/R)`

has derivative magnitude at most `sqrt(N)/2` on `R>=1`, such an interval confines `p` to width below `1/2`. The unique integer candidate is then checked by division into `N`.

The queried numerators and denominators need only `O(log N)` bits even though their numerical values eventually reach factor scale.

Therefore:

`POLY-BIT BOUNDARY_ORDER_ORACLE -> POLYNOMIAL-TIME FACTORIZATION`.

This explains why the order bit is a sharper target than exact collision counting: the needed output is only one bit per query, but it is already factor-complete under adaptive interrogation.

---

## 9. Exact orientation loss of the current square-gap factor bridge

For one split `(a,b)`, the factor-bearing difference-of-squares representation is

`x=(a*p+b*q)/2`,

`y=(a*p-b*q)/2`,

with

`x^2-a*b*N = y^2 = (a*p-b*q)^2/4`.

Every current observer that retains only

- the square completion gap `y^2`,
- `|y|`,
- a square-residue test of `y^2`, or
- a nearest-square scalar cost

is invariant under

`a*p-b*q -> -(a*p-b*q)`.

But the factor-ratio comparison

`a/b ? q/p`

is exactly the sign of `a*p-b*q`.

Hence the present square-gap BRC bridge is **orientation-blind by construction**. It can measure closeness to the balancing ridge, but it cannot say which side of that ridge the split lies on without retaining additional labeled cross-branch information.

Freeze:

`SQUARED_GAP_PROXIMITY != BOUNDARY_ORDER_ORIENTATION`.

This is the precise observer-loss reason that a minimum-gap strategy can correlate with balance yet fail to yield an exact binary-search comparator.

---

## 10. Common-offset balancing does not automatically repair the bootstrap

One can encode the same comparison using two branches with a large common odd baseline:

`(a+2u,b)` and `(a,b+2v)`.

Their hidden boundary difference is still exactly

`u*p-v*q`,

so common offsets can make the two multiplier splits individually close to the balancing ridge while preserving the desired threshold bit.

For a split ratio `z=a/b`, its exact factor-bearing endpoint sits above the geometric root by

`Delta(z,b) = (b*p/2)*(sqrt(z)-sqrt(R))^2`.

For `z=R+epsilon` in a fixed bounded ratio band,

`Delta = Theta(b*p*epsilon^2)`.

If a current ratio estimate has error `delta`, and a common denominator/baseline scale `b` is chosen so the two comparison splits perturb the estimate by `Theta(1/b)`, then the best balance of the two terms occurs at

`b = Theta(1/|delta|)`,

and the resulting local factor-bearing offset scale is

`Delta_min = Theta(p*|delta|)`.

Therefore realizing the order bit by ordinary local square-gap scanning does not bootstrap cheaply: to make the local scan polylogarithmic, the ratio must already be known to essentially `1/p` precision, which is already enough for factor recovery.

This is a scoped cost law for this local-scan realization only. It is not a lower bound on all possible cross-branch BRC operators and not a general deterministic factoring lower bound.

---

## 11. Revised attack surface

The collision program is now split cleanly:

### Closed as a primary route

- larger exact-collision horizons;
- more second moments across `K`;
- fixed local prime-modulus attempts to obtain a unique `E3` residue beyond the exact product-fiber quotient;
- independent square-gap/minimum-gap scalars as a substitute for orientation.

### Retained

1. **Local regression baseline:** RSA-270 has the exact free residue
   `E3 == 2486 mod5760`.
2. **Hard local selector problem:** for every `ell>=7`, identify which of the `c_ell(N)` factor-residue orbits is real. This is additional factor-sensitive information, not a free product collapse.
3. **Strongest new theoretical target:** construct an N-visible **cross-branch order/orientation operator** that evaluates
   `sign(u*p-v*q)` without first locating either factor-bearing boundary or recovering a square-gap witness.
4. **Kill condition:** if every candidate cross-branch operator factors through independent squared gaps, absolute imbalances, fixed local residues, or an explicit factor/divisor selection, classify it as orientation-erasing or factorization-equivalent and stop.

The new target is deliberately one bit wide. A successful cheap evaluator would be enough; exact boundary reconstruction is unnecessary.

No Foundation promotion, Working Truth promotion, or factorization-complexity improvement is claimed.