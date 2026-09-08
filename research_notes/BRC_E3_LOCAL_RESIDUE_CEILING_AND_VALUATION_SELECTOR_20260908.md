# BRC E3 Fixed-Local Residue Ceiling and First-Free Selector

Status: `RESEARCH NOTE / EXACT ELEMENTARY LOCAL CLASSIFICATION + SELECTOR REDUCTION / NOT FOUNDATION / NO FACTORIZATION SPEEDUP CLAIM`
Date: `2026-09-08`
Researcher-ID: `EM-DIRECT-7K3Q`
Parent notes:
- `research_notes/BRC_MULTIPLIER_COLLISION_ENERGY_TRACE_20260908.md`
- `research_notes/RSA270_BRC_COLLISION_ACTIVATION_PHASE_SYNTHESIS_20260908.md`
Source snapshot immediately before write: `main@e992bcd6fac9d962304ef462f62c6489a9561faa`

## 0. Purpose

The collision-energy route has already collapsed to

`E3 = 2 S^2 - 6 N`, where `S=p+q`, `N=pq`.

Hence any exact extra residue of `E3` is an extra residue of `S^2`, and enough independent residue information would eventually recover `S` and factor `N`.

The previous frontier established the universal RSA-type congruence

`S^2 = (N+1)^2 mod 576`

and, for RSA-270 specifically, the stronger factor-blind local residue

`S^2 mod 2880`, equivalently `E3 mod 5760`.

This note closes the entire **fixed-local factor-blind residue** route, not merely the particular moduli already tested. It also identifies the exact first factor-sensitive digit that any surviving BRC observer would have to select.

Scope boundary:

- this is a classification of information determined solely by fixed local factor-blind congruence classes;
- it is **not** a no-go theorem for arbitrary algorithms using the full integer `N`;
- it does **not** rule out adaptive moduli, gcd/order effects, valuation-triggered factor isolation, or a genuinely factor-sensitive BRC orbit selector.

## 1. Local hidden-energy fiber

For a modulus `m` and a unit `n mod m`, define the factor-blind local `S^2` fiber

`F_m(n) = { (x + n*x^{-1})^2 mod m : x in (Z/mZ)^* }`.

This is exactly the set of `S^2 mod m` values compatible with the public local product `pq=n mod m` when the individual factor residue is hidden.

The key identity is

`(x + y)^2 - (xy + 1)^2 = -(x^2-1)(y^2-1)`.

With `xy=n`, this becomes

`S^2 - (n+1)^2 = -(x^2-1)(y^2-1)`.

Therefore local singleton behavior is a valuation problem for the two defects `x^2-1` and `y^2-1`.

Under CRT, the fibers factor exactly across coprime prime powers. Consequently a composite modulus gives a singleton if and only if every prime-power projection gives a singleton. There is no hidden cross-prime rescue available inside the fixed-local model.

## 2. Exact 2-adic ceiling

Assume `n` is odd.

For every odd `x`,

`v2(x^2-1) >= 3`.

More precisely:

- `v2(x^2-1)=3` iff `x=3 or 5 mod 8`;
- `v2(x^2-1)>=4` iff `x=1 or 7 mod 8`.

Hence every factor pair gives

`S^2 = (n+1)^2 mod 64`.

The next bit depends only on the public class `n mod 8`.

### 2.1 Favorable classes `n=3,5 mod 8`

Let

`A={1,7} mod8`, `B={3,5} mod8`.

If `n in B`, every factorization `xy=n mod8` has one factor in `A` and one in `B`, because `A*B=B` while `A*A=B*B=A`.

Thus one defect has valuation at least 4 and the other exactly 3, giving

`v2((x^2-1)(y^2-1)) >= 7`.

Therefore

`S^2 = (n+1)^2 mod 128`

for every factor pair.

This cannot lift uniformly to mod 256. Choose `y=7 mod256`, for which

`v2(y^2-1)=4`.

Set `x=n*y^{-1} mod256`. Since `n in B`, `x mod8` lies in `B`, so

`v2(x^2-1)=3`.

The defect product then has exact valuation 7. The baseline choice `x=1`, `y=n` has zero defect. Hence the fiber is non-singleton mod256.

So for `n=3,5 mod8`, the exact factor-blind 2-adic ceiling for `S^2` is `2^7`.

### 2.2 Unfavorable classes `n=1,7 mod 8`

Now `n in A`. Since `B*B=A`, one can choose both factor residues in `B`, making both defect valuations exactly 3. The defect product then has exact valuation 6, while the baseline `x=1` has zero defect.

Therefore the fiber is already non-singleton mod128.

So for `n=1,7 mod8`, the exact factor-blind 2-adic ceiling for `S^2` is only `2^6`.

### 2.3 2-adic summary

Define

`delta_2(n)=1` if `n=3,5 mod8`, else `0`.

Then the maximal factor-blind 2-power determining `S^2` is

`2^(6+delta_2(n))`.

Finite exact enumeration agrees:

- mod64: every odd `n` has one `S^2` orbit;
- mod128: exactly the classes `n=3,5 mod8` are singleton;
- mod256: no odd `n` is singleton.

The proof above, not the enumeration, establishes the ceiling.

## 3. Exact 3-adic ceiling

For every unit `x mod3`,

`x^2=1 mod3`.

Thus both factor defects are divisible by 3 and

`S^2 = (n+1)^2 mod9`

for every `n` coprime to 3.

The congruence cannot lift uniformly to mod27.

Modulo 9, the four unit classes

`B={2,4,5,7}`

have exact valuation

`v3(x^2-1)=1`.

Moreover `B*B` covers every unit class mod9. Therefore for every unit `n mod27` one can choose `x mod27` with `x mod9 in B` such that `y=n*x^{-1}` also lies in `B mod9`. Both defects then have exact 3-adic valuation 1, so their product has exact valuation 2. Again the baseline `x=1` has zero defect.

Hence:

- `F_9(n)` is singleton for every unit `n`;
- `F_27(n)` is non-singleton for every unit `n`.

In fact exact finite enumeration shows every unit `n mod27` has exactly two `S^2` values. Thus the first 3-adic lift is a genuine binary orbit choice even though it lives in a ternary digit.

The maximal factor-blind 3-power determining `S^2` is therefore exactly `3^2`.

## 4. Exact 5-adic ceiling

Modulo 5, split the units into

`A={1,4}={+-1}`, `B={2,3}={+-2}`.

For `x in A`, `5 | x^2-1`. For `x in B`, `x^2-1` is a unit mod5.

### 4.1 `n` a quadratic nonresidue mod5

If `n in {2,3}`, every factorization `xy=n mod5` has one factor in `A` and one in `B`. Hence one defect is divisible by 5 and

`S^2=(n+1)^2 mod5`.

This does not lift uniformly to mod25. Take `y=6`, for which

`v5(y^2-1)=1`.

Let `x=n*y^{-1} mod25`. Then `x mod5 in B`, so `v5(x^2-1)=0`. The defect product has exact valuation 1, while the baseline again has zero defect.

Thus a nonresidue `n` contributes exactly one free factor-blind power of 5 and no more.

### 4.2 `n` a quadratic residue mod5

If `n in {1,4}`, choose both factor residues in `B`, whose product lies in `A`. Both defects are units mod5, so the fiber is already non-singleton mod5.

Therefore define

`delta_5(n)=1` iff `(n/5)=-1`, otherwise `0`.

The maximal factor-blind 5-power determining `S^2` is `5^delta_5(n)`.

Finite enumeration agrees:

- mod5: singleton exactly for `n=2,3`;
- mod25: no unit `n` is singleton.

## 5. No fixed-local contribution from primes ell >= 7

The parent RSA-270 synthesis established the exact prime-modulus orbit count

`c_ell(n) = (ell+1+chi(n)+chi(-n))/4`

for odd prime `ell` not dividing `n`.

For every `ell>=7`, this count is at least 2. Hence no such prime contributes even one fixed-local factor-blind `S^2` digit.

This closes all new-prime searches in the fixed-local residue model. Trying `ell=7,11,13,...` cannot create a singleton that was merely missed by previous finite scans.

## 6. Complete fixed-local ceiling theorem

Assume `gcd(N,30)=1` and the hidden factors are odd primes above 5. Define

`delta_2(N)=1` iff `N=3 or 5 mod8`, else `0`,

and

`delta_5(N)=1` iff `(N/5)=-1`, else `0`.

Then the maximal modulus in the divisibility lattice for which `S^2 mod M` is uniquely determined by factor-blind fixed-local product information is

`M_S(N) = 2^(6+delta_2(N)) * 3^2 * 5^delta_5(N)`

or equivalently

`M_S(N) = 576 * 2^delta_2(N) * 5^delta_5(N)`.

On this maximal modulus,

`S^2 = (N+1)^2 mod M_S(N)`.

Since

`E3 = 2S^2-6N`,

the corresponding maximal fixed-local collision-energy modulus is

`M_E(N)=2 M_S(N)`,

and

`E3 = 2(N^2-N+1) mod M_E(N)`.

The four possible `E3` ceilings are therefore:

| public local class | maximal fixed-local `E3` modulus |
|---|---:|
| no extra 2-bit, no mod5 | 1152 |
| extra 2-bit only | 2304 |
| mod5 only | 5760 |
| extra 2-bit and mod5 | 11520 |

No fixed-local deterministic `E3` residue can be enlarged by adjoining another prime-power digit: at the first excluded prime-power layer the factor-blind local fiber contains at least two admissible `S^2` orbits.

By CRT the prime-power ambiguities combine independently, so a composite modulus cannot repair a failed local singleton.

For a statement restricted to genuine prime semiprimes rather than arbitrary unit factor residues, Dirichlet's theorem supplies infinitely many primes in every admissible reduced residue class. Thus the local ambiguity is not an artifact of allowing nonprime factor representatives. This still only proves a no-go for functions of the fixed local residue data, not for a full-`N` algorithm.

## 7. RSA-270 ceiling becomes exact, not empirical

The synthesis records

`N mod5=2`,

so `delta_5=1`.

It also records

`S^2=1984 mod2880`.

Since `1984=0 mod64` and `(N+1)^2` has that same residue, the RSA-270 public class is `N=7 mod8`, hence `delta_2=0`.

Therefore the theorem gives exactly

`M_S(RSA270)=2880`,

`M_E(RSA270)=5760`.

So the previously observed failure to lift at `2^7`, `3^3`, and `5^2` is not merely a collection of local witnesses: it is the special case of the complete fixed-local ceiling.

The already recorded residue

`E3=2486 mod5760`

is therefore the **maximum possible collision-energy information obtainable from this factor-blind fixed-local congruence mechanism** for RSA-270.

Any further progress must use a factor-sensitive selector.

## 8. Normalize the remaining problem: the collision defect

Define the public baseline polynomial

`P(N)=2(N^2-N+1)`.

Then

`D := P(N)-E3`

satisfies the exact factorization identity

`D = 2((N+1)^2-S^2)`

`  = 2(p^2-1)(q^2-1)`

`  = 2(p-1)(p+1)(q-1)(q+1)`.

Thus every universal residue facade is exactly a **forced lower bound on local valuations of D**.

For any prime `ell`,

`E3=P(N) mod ell^k`

iff

`v_ell(D)>=k`.

The next residue beyond the fixed-local ceiling is therefore not an unspecified `E3` mystery. It is the first **normalized factor-sensitive defect digit** beyond the forced valuation floor.

This is the sharper target for an N-only BRC observer.

## 9. First-free selector digits

### 9.1 2-adic selector

If `N=1 or 7 mod8`, the forced `E3` floor is mod `2^7=128`. Define

`d_2 = D/128 mod2`.

Then `d_2` is the entire next bit `E3 mod256`.

For these public classes, factor residues split into two hidden orbit types:

- both factors `=3 or5 mod8`: `v2(D)=7`, so `d_2=1`;
- both factors `=1 or7 mod8`: `v2(D)>=9`, so `d_2=0`.

There is no `v2(D)=8` case here. The selector is exactly an individual-factor 2-adic orbit bit erased by multiplication into `N`.

If instead `N=3 or5 mod8`, the forced floor is one bit higher, `E3 mod256`. The first free bit is

`d_2 = D/256 mod2`,

which distinguishes whether the unique factor lying in the `+-1 mod8` class has the next 2-adic defect lift.

### 9.2 3-adic selector

The forced floor is `E3 mod9`. Define

`d_3=D/9 mod3`.

For each fixed public `N mod27`, the local `S^2` fiber has exactly two values. Equivalently the allowed `d_3` set is `{0,c_N}` for one public nonzero `c_N mod3`.

Thus one binary orbit decision — baseline versus nonbaseline — selects the whole first 3-adic lift.

The zero orbit is characterized by

`v3(D)>=3`,

while the nonzero orbit has `v3(D)=2`.

### 9.3 5-adic selector

When `(N/5)=-1`, the forced floor is `E3 mod5`. Define

`d_5=D/5 mod5`.

Here the next local fiber at mod25 has five possible values. Hence a single valuation predicate

`v5(D)>=2`

only recognizes the distinguished zero digit; it does **not** recover the four possible nonzero digits.

For RSA-270, therefore, a complete lift from `E3 mod5760` through the next 5-adic layer requires a genuine base-5 orbit digit, not merely one Boolean valuation wall.

This is an important distinction from the 2-adic first lift and from the two-orbit 3-adic first lift.

## 10. The existing mod256 shadow collision is exactly a first-free-selector no-go

The parent energy note gave the two prime semiprimes

`19519 = 131*149`,

`156479 = 167*937`,

with identical compressed mod256 shadow

`(N, J1, R1, phase)=(63,139,198,2)`

but

`E3=6 mod256`

versus

`E3=134 mod256`.

For the shared public residue `N=63 mod256`,

`P(N)=2(N^2-N+1)=134 mod256`.

Therefore the second example is on the baseline orbit while the first differs by exactly 128.

Indeed:

- for `131*149`, both factors are in the `3,5 mod8` orbit and `v2(D)=7`;
- for `167*937`, both factors are in the `1,7 mod8` orbit and `v2(D)>=9`.

So the previous counterexample is stronger than a generic `E3` mismatch:

> the current `(N,J1,R1,phase) mod256` compression fails **exactly on the first unforced 2-adic collision-energy bit**.

This sharply localizes the information loss. Any successor observer must preserve more pre-compression provenance than that shadow.

## 11. Classical-method novelty firewall

The normalized defect has

`D=2(p-1)(p+1)(q-1)(q+1)`.

Hence local selectors are statements about whether an individual hidden factor lies near `+1` or `-1` in a prime-power modulus.

That is immediately adjacent to classical group-order machinery:

- `p-1` smoothness/order tests;
- Lucas / `p+1` style tests;
- gcd extraction when a public exponent/order expression vanishes modulo one factor but not the other;
- ordinary local factor-residue sieving.

Therefore a BRC construction that appears to reveal `d_ell` must be audited against these classical mechanisms before any novelty claim.

The existing admitted activation-wall tool `t1.nonly_valuation_wall_gcd_extractor` already shows that a factor-sensitive Boolean wall can exist without yielding a new asymptotic primitive. A selector is interesting only if its constructor is genuinely cheaper than the classical factor-threshold/order work it replaces.

Freeze:

`ORBIT_SELECTOR != FACTORIZATION SPEEDUP`.

`SMALL OBSERVER STATE != SMALL CONSTRUCTOR`.

`NEW E3 DIGIT != NEW METHOD` unless the construction cost and classical reduction audit both survive.

## 12. Revised experimental target for m=1,3

Do not scan larger multiplier horizons or new fixed moduli.

For every candidate N-visible BRC observer derived from the **pre-compression** `m=1,3` state, test it against the exact first-free labels:

- `d_2` at the first excluded 2-adic layer;
- baseline/nonbaseline `d_3` at mod27;
- the full five-way `d_5` at mod25 when `(N/5)=-1`.

Required controls:

1. condition on the full public local residue needed for the label (`N mod256/512`, `N mod27`, `N mod25` as applicable), so a candidate cannot win by relearning a public congruence;
2. preserve raw/pre-compression BRC provenance and record exactly which operation generated the candidate invariant;
3. demand exact within-signature consistency first; a single same-signature/different-label collision kills deterministic recovery by that observer;
4. use held-out semiprimes across magnitude bands only after exact collision checks;
5. treat correlation or classification accuracy as reconnaissance, not a theorem;
6. if a candidate succeeds, reduce it algebraically against `D=2(p^2-1)(q^2-1)` and against standard gcd/order methods before continuing.

The most economical immediate test is the 2-adic unfavorable class because the target is one bit and the existing mod256 counterexample already provides a regression pair.

## 13. Research closure reached in this note

The fixed-local CRT accumulation program is now closed completely:

- no new odd prime `ell>=7` can help factor-blindly;
- the 2-adic contribution stops at `2^6` or `2^7` according to `N mod8`;
- the 3-adic contribution stops exactly at `3^2`;
- the 5-adic contribution is either absent or exactly one digit according to `(N/5)`;
- CRT creates no hidden cross-prime singleton.

For RSA-270 the exact ceiling is `E3 mod5760`.

The surviving collision-energy question is therefore strictly narrower:

> Can an N-visible BRC operation preserve or construct an individual-factor orbit selector for the first normalized defect digit `d_ell`, without collapsing to classical factor-threshold/order/gcd work?

That is the next hard unit. Larger `K`, additional second moments, and further fixed-local residue sweeps are no longer justified.