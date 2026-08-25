# Native Filament Post-audit Hyperbola/Joukowski — Independent Replication Return

Task-ID: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Researcher-ID: `EM-POSTHJ-EE1141`

Date: `2026-08-25`

Owner branch: `audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825`

Math-source branch tip at blind-read start: `9c99b131f3e1af67be6521ecfb977ab6ef00cbaa`

Taskbook blob: `0e461007e74be40ee0bc783fb0273cb96ece1866`

Blind packet blob: `6ce9ea10f02fded1959c55a1b78044ada434360f`

Independent checker:

`research_checks/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_CHECKER_20260825.py`

Checker SHA256:

`03cd9a185dab0eacdf65b927a9c4c629d764d6289959b99c4524f187b230d52d`

## 1. Independence attestation

I generated the fresh identity `EM-POSTHJ-EE1141` for this replication.

Before freezing this return I read only the taskbook and its single allowed statement-only blind packet as mathematical inputs. I did not read PR #627, branch `research/native-filament-generalization-theorem-package-20260824`, any withheld source proof/checker, any package-specific file containing the prohibited names, or originating-researcher proof-correctness opinions. I did not use audit #631 as a proof source. Account-level bootstrap/operating instructions were read only as execution-control metadata and supplied no mathematics.

The checker was written independently from the blind statements and uses only the Python standard library.

## 2. Executive verdict

The post-audit layer is mathematically strong, but it is **not exact as written in every semantic bridge**.

The core algebraic claims H1a/H1b/H1c, H2a/H2c/H2d, J1, J2, and C1 survive independent derivation. Two statement-strength corrections are required:

1. **H1 bridge correction.** The dual-overlap variety is the full split hyperbola, but distinct-slope tangent concurrence does not realize the full hyperbola. After quotienting concurrence triples by simultaneous translation of `(u,v,w)`, it realizes the hyperbola with the diagonal points `a=b` removed. Those omitted points exist exactly when `C_i/B` is a square in the field. Without the translation quotient there is also an extra affine-line parameter, so the two spaces are dimensionally different.
2. **C2 semantic correction.** The three displayed `C3` lane formulas follow exactly by specializing the packet's lane polynomial to `s=3, j=-1,0,1`, and `3*M_9=105` is an exact integer identity. But the blind packet does not define any extra native “slot-unfolding” structure or give data from which one can prove that two appearances of the integer `105` have a stronger common provenance/mechanism. Only the exact algebraic coincidence is independently certified.

There is also a finite-field notation/domain cleanup in H2: if `q` is intended to range over all odd prime powers, the character in H2c must be the quadratic character `chi_q` of `F_q`; if the symbol is literally the Legendre symbol `(./q)`, restrict H2 to odd prime `q`.

Accordingly the global outcome is:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`

and the requested hard target is met.

## 3. Verdict matrix

| Group | Verdict | Independent result |
|---|---|---|
| H1 | `VERIFIED_WITH_NARROWING` | H1a/H1b/H1c are exact. The final “same full torsor” bridge is too strong under `u != v`; tangent concurrence modulo common translation is `H_(B,C_i) \ Delta_i`, not always all of `H_(B,C_i)`. |
| H2 | `VERIFIED_WITH_NARROWING` | Counting/orbit claims are exact. For arbitrary odd `F_q`, write the quadratic character `chi_q`; literal Legendre notation requires odd prime `q`. H2b also needs the H1 shift relation `C=2(d_0-d_1)` (or an explicit choice of such shifts). |
| J1 | `VERIFIED_EXACT` | `Lambda_s` is exactly the quotient of `F_q^*` by the involution `a -> c/a`, `c=(2s)^(-1)`, and the image-size/saturation statements follow. |
| J2 | `VERIFIED_EXACT` | Independent second-moment derivation gives `q_-(s) | 75` and `q_+(s) | 21` under saturation, forcing `(s,q)=(3,5)` and `(3,7)` respectively; existence at `s=3` is checked directly. |
| C1 | `VERIFIED_EXACT` | Both boundary equations are exactly equivalent to `q_b=s+2`; with `s>=3` odd and the stated bound `q_b<=5`, only `(s,q_b,k_*)=(3,5,9)` remains. Arithmetic `35,105,106=2*53` is exact. |
| C2 | `VERIFIED_WITH_NARROWING` | The `s=3` lane specialization gives the three displayed polynomials exactly and the two `105` values coincide numerically. Any stronger claim of shared native provenance/mechanism is not derivable from the blind packet. |

## 4. H1 — independent derivation and minimal failure mode

Assume throughout this section:

- `K` is a field;
- `char(K) != 2`;
- `B in K^*`;
- `d_i != d_(1-i)`;
- `C_i=2(d_i-d_(1-i))`, hence `C_i != 0`.

### H1a: tangent concurrence

For

`Q_i(x)=x^2/(2B)-d_i`,

the tangent at `x=-Bu` is indeed

`T_(i,u): y=-u x-Bu^2/2-d_i`.

For `u != v`, intersect `T_(i,u)` and `T_(i,v)`. Their unique intersection is

`X=-B(u+v)/2`,
`Y=Buv/2-d_i`.

Substituting `(X,Y)` into `T_(1-i,w)` gives

`Buv-2d_i = B(wu+wv-w^2)-2d_(1-i)`,

or equivalently

`B(w-u)(w-v)=2(d_i-d_(1-i))=C_i`.

Thus H1a is exact.

Because `C_i != 0`, any concurrent solution also has `w != u` and `w != v`.

### H1b: negative algebraic Legendre dual

Completing the square in

`p x-Q_i(x)`

gives the algebraic stationary dual

`Q_i^*(p)=Bp^2/2+d_i`.

Hence the negative dual map is

`L_i(p)=-Bp^2/2-d_i`.

A common value `L_i(x)=L_(1-i)(y)` is equivalent to

`-Bx^2/2-d_i=-By^2/2-d_(1-i)`,

hence exactly

`B(y^2-x^2)=C_i`.

Thus H1b is exact.

### H1c: split-hyperbola isomorphism

Define

`Phi(x,y)=(a,b)=(y-x,y+x)`.

Then

`ab=(y-x)(y+x)=y^2-x^2`,

so

`B(y^2-x^2)=C_i  <=>  Bab=C_i`.

Since `char(K) != 2`, the inverse is

`x=(b-a)/2`,
`y=(a+b)/2`.

Therefore H1c is exact: the dual-overlap representation variety is isomorphic to

`H_(B,C_i)={(a,b):Bab=C_i}`.

### The overstrong bridge

Let the distinct-slope concurrence configuration space be

`X_i={(u,v,w): u!=v, B(w-u)(w-v)=C_i}`.

Map

`pi(u,v,w)=(a,b)=(w-u,w-v)`.

The simultaneous translation action

`t.(u,v,w)=(u+t,v+t,w+t)`

preserves `pi`, and every fiber of `pi` is one such affine translation orbit.

But

`u!=v  <=>  w-u != w-v  <=>  a!=b`.

Thus `pi` induces

`X_i / G_a  ~=  H_(B,C_i) \ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

So:

- the **dual-overlap side** is all of `H_(B,C_i)`;
- the **distinct-tangent side modulo translation** is `H_(B,C_i)` minus its diagonal points;
- before quotienting by translation, the tangent-concurrence space has one extra affine parameter.

The diagonal is empty over `K` exactly when `C_i/B` has no square root in `K`. Only in that case does the distinct-tangent quotient recover the full `K`-point hyperbola.

#### Concrete minimal counterexample to the unqualified “same full torsor” sentence

Take

`K=Q`, `B=1`, `d_i=1/2`, `d_(1-i)=0`.

Then `C_i=1`.

The dual-overlap pair

`(x,y)=(0,1)`

has common negative-dual value

`-1/2`

and maps under `Phi` to

`(a,b)=(1,1)`,

which lies on `ab=1`.

If this point came from tangent differences, then

`w-u=1=w-v`,

forcing `u=v`, contrary to H1a's distinctness hypothesis.

This is a concrete counterexample to the **unqualified final equivalence sentence**, not to H1a/H1b/H1c themselves.

## 5. H2 — independent finite-field orbit calculation

Use an odd finite field `F_q`, `B,C != 0`.

For literal Legendre-symbol wording below, take `q` prime. For an arbitrary odd prime power replace every Legendre symbol by the unique quadratic character `chi_q` of `F_q`.

Let

`R={(x,y):B(y^2-x^2)=C}`.

### H2a

The same invertible linear map

`(x,y)->(a,b)=(y-x,y+x)`

identifies `R` with

`Bab=C`.

For every `a in F_q^*` there is a unique

`b=C/(Ba)`.

Therefore

`|R|=q-1`.

This proof works for every odd prime power.

### H2b

To speak of “common dual values”, retain or choose shifts with

`C=2(d_0-d_1)`,

which is always possible in odd characteristic.

A common value determines `x^2` and `y^2` uniquely. Conversely, changing the sign of either coordinate does not change that value. Hence two points of `R` have the same common dual value exactly when they lie in the same orbit of

`G={+/-1}^2`.

Zero coordinates merely reduce orbit size and cause no failure of the quotient. Therefore the common-value set is in bijection with `R/G`.

### H2c: Burnside count

Let `chi` denote the quadratic character.

- Identity fixes all `q-1` points.
- `(-1,+1)` fixes exactly the points with `x=0`, so its fixed-point count is `1+chi(C/B)=1+chi(BC)`.
- `(+1,-1)` fixes exactly the points with `y=0`, so its fixed-point count is `1+chi(-C/B)=1+chi(-BC)`.
- `(-1,-1)` would require `x=y=0`, impossible because `C != 0`.

Burnside gives

`|R/G| = [q+1+chi(BC)+chi(-BC)]/4`.

For odd prime `q` this is exactly H2c with Legendre symbols.

### H2d without the character formula

If `|R/G|=1`, all `q-1` points of `R` lie in a single `G`-orbit.

Every `G`-orbit has size at most `4`, hence

`q-1<=4`,

so

`q<=5`.

This is the requested orbit-capacity proof and does not use H2c.

Small cases from H2c:

- `q=3`: the quotient always has size `1`;
- `q=5`: it has size `1` exactly when `chi(BC)=-1`, and size `2` when `chi(BC)=+1`.

No converse “every q<=5 is automatically a universal breaker” is being asserted.

## 6. J1 — exact Joukowski quotient

Assume:

- `s>=3` is odd;
- `q` is an odd prime;
- `q` does not divide `2s`;
- `a in F_q^*`.

For

`P_(s,j)(m)=2s m^2+2jm+1`,

the condition `P_(s,j)(a)=0 mod q` gives

`2ja=-(2sa^2+1)`,

hence

`j=-sa-1/(2a)=Lambda_s(a)`.

Set

`c=(2s)^(-1) in F_q^*`.

Then

`Lambda_s(a)=-s(a+c/a)`.

Thus it is a generalized Joukowski map, scaled by `-s`.

Define the involution

`tau(a)=c/a`.

Directly,

`Lambda_s(tau(a))=Lambda_s(a)`.

Conversely, if `Lambda_s(a)=Lambda_s(b)`, then

`(a-b)(-s+1/(2ab))=0`,

so either

`a=b`

or

`ab=c`,

i.e. `b=tau(a)`.

Therefore the fibers are exactly the `tau`-orbits; this is an exact quotient description, not merely an analogy.

The fixed points satisfy

`a^2=c`.

Their number is

`1+Legendre(c,q)`.

Hence the orbit count, and therefore the image size, is

`|Im Lambda_s|`
`=[(q-1)+(1+Legendre(c,q))]/2`
`=[q+Legendre(1/(2s),q)]/2`.

This proves J1b.

Finally, a nonzero residue `a` is hit by at least one central lane iff

`Lambda_s(a) in J_s (mod q)`.

Therefore all nonzero residues are hit iff

`Im Lambda_s subseteq J_s (mod q)`.

If the residue set of `J_s` and the image have equal cardinality, containment is equality. This proves J1c.

## 7. J2 — independent extremal uniqueness proof

No source second-moment identity was used.

### J2a: lower extremal `q=2s-1`

Assume `s>=3` odd and `q=2s-1` prime.

Then `q≡1 (mod 4)` and

`2s≡1 (mod q)`,

so

`Lambda_s(a)=-(a+a^(-1))/2`.

Also

`c=(2s)^(-1)=1`.

The involution is `a->a^(-1)`, with fixed points `a=+/-1`. Therefore

`|Im Lambda_s|=(q+1)/2=s`.

Because `J_s` has exactly `s` distinct residues modulo `q`, saturation forces

`Im Lambda_s=J_s`.

Write

`n=(s-1)/2=(q-1)/4`,

so

`J_s={-n,...,n}`.

For `q>3`,

`sum_(a!=0) a^2 = sum_(a!=0) a^(-2)=0`.

Therefore

`sum_(a!=0) Lambda_s(a)^2 = -1/2  (mod q)`.

Every nonfixed image value has two preimages. The two fixed inputs `+/-1` map to `-1,+1`, respectively. Hence, if `Im Lambda_s=J_s`,

`-1/2 = 2 sum_(j=-n)^n j^2 - 2`.

Thus

`4 sum_(j=-n)^n j^2 = 3 (mod q)`.

Using

`sum_(j=-n)^n j^2 = n(n+1)(2n+1)/3`,

we get

`4n(n+1)(2n+1)=9 (mod q)`.

Since `n=(q-1)/4`, equivalently `n=-1/4 (mod q)`, the left side is `-3/8`, so

`-3/8=9 (mod q)`,

which gives

`q | 75`.

The prime `q` is at least `5` and satisfies `q≡1 (mod 4)`, hence

`q=5`.

Then `s=(q+1)/2=3`.

Direct existence check at `s=3,q=5`:

`Im Lambda_3={0,1,4}=J_3 (mod 5)`.

Therefore J2a is exact.

### J2b: upper extremal `q=2s+1`

Assume `q=2s+1` prime.

Then `q≡3 (mod 4)` and

`2s≡-1 (mod q)`,

so

`Lambda_s(a)=(a-a^(-1))/2`.

Now

`c=(2s)^(-1)=-1`.

Since `q≡3 (mod 4)`, `-1` is nonsquare, so the involution

`a->-a^(-1)`

has no fixed points. Thus

`|Im Lambda_s|=(q-1)/2=s`.

Again saturation forces `Im Lambda_s=J_s`.

Put

`n=(s-1)/2=(q-3)/4`.

This time

`sum_(a!=0) Lambda_s(a)^2 = 1/2 (mod q)`.

Every image value has exactly two preimages, so saturation gives

`1/2 = 2 sum_(j=-n)^n j^2`,

hence

`4 sum_(j=-n)^n j^2 = 1 (mod q)`,

and therefore

`4n(n+1)(2n+1)=3 (mod q)`.

With `n=-3/4 (mod q)`, the left side is `3/8`, giving

`3/8=3 (mod q)`,

so

`q | 21`.

Here `q>=7` is prime and `q≡3 (mod 4)`, hence

`q=7`.

Then `s=(q-1)/2=3`.

Direct existence check at `s=3,q=7`:

`Im Lambda_3={0,1,6}=J_3 (mod 7)`.

Therefore J2b is exact.

### J2c

Both extremal boundaries are saturated at `s=3`, and each side separately forces `s=3`.

Thus `s=3` is the unique nontrivial odd-sector parameter saturating both prime extremal boundaries.

## 8. C1 — exact closure algebra

Let the stated breaker-coprime capacity be

`k_*=2q_b-1`.

Then

`k_*-4=2q_b-5`,
`k_*-2=2q_b-3`.

The equations

`k_*-4=2s-1`,
`k_*-2=2s+1`

both reduce to

`2q_b=2s+4`,

hence exactly

`q_b=s+2`.

Conversely `q_b=s+2` makes both equations true, so C1a is an equivalence.

For a nontrivial odd sector, `s>=3`. If the independently established breaker bound `q_b<=5` applies, then

`q_b=s+2>=5`.

Therefore

`q_b=5`,
`s=3`,
`k_*=2*5-1=9`.

This proves C1b as the stated conditional closure theorem.

At this point

`M_9=(9-4)(9-2)=5*7=35`,

`3*M_9=105`,

and

`3*M_9+1=106=2*53`.

So the terminal odd prime factor is exactly `53`.

### No prime-run promotion

The integer `9` here is only the breaker-coprime capacity `k_*=2q_b-1` in this closure theorem.

Nothing in H1/H2/J1/J2/C1 proves:

- nine unrestricted consecutive prime values;
- an unrestricted prime-run theorem of length nine;
- equality with the separate typed-Cell prime-incidence island cap mentioned as outside the packet.

The checker and this return make no such promotion.

## 9. C2 — exact algebra, narrowed semantics

From J1,

`P_(s,j)(m)=2sm^2+2jm+1`.

At `s=3`,

`J_3={-1,0,1}`,

so the three lane polynomials are exactly

`P_(3,-1)(m)=6m^2-2m+1`,
`P_(3,0)(m)=6m^2+1`,
`P_(3,1)(m)=6m^2+2m+1`.

Thus, **if “native C3 slot-unfolding” means the `s=3` central packet with its three lane slots `j=-1,0,1`**, C2a is exact. The middle lane is the displayed central filament value.

C2b has one part that is fully certified:

`3*M_9=3*35=105`.

Therefore the closure extremum and any independently defined gate whose exact value is `105` coincide as integers.

The blind packet, however, gives no independent definition/derivation of the phrase “native 105 bouquet gate” beyond naming its value, and supplies no invariant that would prove a stronger genealogical statement such as “the two occurrences arise from one previously defined mechanism”. Equality of integers alone does not establish provenance.

The independently justified wording is therefore:

> In the `s=3` closure, the longitudinal extremum `3*M_9` equals the stated native bouquet-gate integer `105` exactly; this replication certifies exact numerical/algebraic coincidence, not an additional causal or structural identification absent from the blind packet.

## 10. Boundary and accidental-equivalence audit

### Characteristic `2`

The exclusions are essential.

For H1/H2, `Phi` has determinant `-2`, so it ceases to be invertible. Also `-1=+1`, so the four-element sign action collapses.

Explicitly in `F_2`, with `B=C=1`,

`R={(x,y):y^2-x^2=1}`

has two points, while `q-1=1`. Thus H2a does not extend to `q=2`.

For J1, division by `2a` is unavailable; in fact the lane polynomial reduces to `1 mod 2`, so the stated lane-hit rewrite cannot hold.

### Vanishing `B` or `C`

- H1 requires `B != 0` even to define `Q_i`.
- Distinct shifts plus `char(K)!=2` ensure `C_i!=0`.
- In H2, if `B=0,C!=0`, `R` is empty, not of size `q-1`.
- If `C=0`, then `y^2=x^2`; for odd `q` this is the union `y=x` and `y=-x` with `2q-1` points. The checker confirms counts `9,13,25` for `q=5,7,13`.

Thus `B*C!=0` is essential.

### Slope collisions

The only collision relevant to the H1 bridge is `u=v`, equivalently `a=b`. This is precisely the diagonal deletion described in Section 4.

Since `C_i!=0`, concurrence itself automatically prevents `w=u` or `w=v`.

### Divisors of `s`

J1's `q∤2s` hypothesis is essential.

If an odd prime `q` divides `s`, the formula

`c=(2s)^(-1)`

does not exist, so the involution/image-size proof cannot even be stated. The lane-hit map itself reduces to

`Lambda_s(a)=-1/(2a)`,

which is a bijection of `F_q^*` and has image size `q-1`, qualitatively different from the claimed quotient formula.

The pressure checker explicitly exercised the `q|s` cases for odd `s<=15`.

### Small `s`

The nontrivial cutoff `s>=3` matters.

At the excluded value `s=1`, the upper extremal is `q_+=3`, and the single lane `j=0` does saturate the nonzero residues modulo `3`. Therefore extending J2c to `s=1` would be false.

### Nonprime `2s+/-1`

J2 is a finite-field prime-characteristic theorem and assumes the integer `2s+/-1` itself is prime. A composite modulus is not silently promoted to a finite field.

As a pressure test only, the checker also tested the raw polynomial congruence modulo every composite lower/upper boundary produced by odd `3<=s<=101`:

- lower composite boundaries tested: `29`;
- upper composite boundaries tested: `27`;
- observed complete saturations: none.

This is computational pressure only, not an extension of J2 to composite moduli.

## 11. Independent finite pressure-test log

Checker invocation:

`python3 research_checks/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_CHECKER_20260825.py`

Result:

`INDEPENDENT_CHECKER_PASS`

Key log:

- H1 over `F_5`: `8,000` distinct-slope concurrence triples tested; H1a/H1b/H1c finite identities passed.
- H1 over `F_7`: `74,088` distinct-slope concurrence triples tested; H1a/H1b/H1c finite identities passed.
- H1 rational narrowing counterexample: common dual value `-1/2`, `Phi=(1,1)` on the hyperbola diagonal, impossible with `u!=v`.
- H2 `q=5`: all `16` pairs `(B,C) in (F_5^*)^2` checked.
- H2 `q=7`: all `36` pairs checked.
- H2 `q=13`: all `144` pairs checked.
- H2 `q=53`: all `2,704` pairs checked.
- Every H2 case passed `|R|=q-1`, Burnside orbit count, and exact dual-value-fiber/orbit identification.
- J1: all `167` valid pairs with odd `s<=15`, prime `q<=101`, `q∤2s` passed the image-size formula and saturation equivalence.
- J2: among `21` lower-prime extremals through `s<=101`, only `(s,q)=(3,5)` saturated.
- J2: among `23` upper-prime extremals through `s<=101`, only `(s,q)=(3,7)` saturated.
- Composite raw-boundary pressure: `29` lower and `27` upper composite moduli, no saturation observed.
- Boundary checks: explicit `q=2` H2 failure, `C=0` count change, and excluded `s=1,q=3` saturation all confirmed.
- C1/C2 arithmetic: unique bounded solution `(3,5,9)`, `M_9=35`, `3*M_9=105`, `106=2*53`.

The computational tests are corroboration only. H1/H2/J1/J2/C1 conclusions above have independent exact derivations.

## 12. Exact final theorem wording after narrowing

### Theorem A — split-hyperbola duality and distinct-tangent bridge

Let `K` be a field with `char(K)!=2`, let `B in K^*`, let `d_0!=d_1`, and put `C_i=2(d_i-d_(1-i))`.

1. For `u!=v`, the tangents `T_(i,u),T_(i,v),T_(1-i,w)` are concurrent iff
   `B(w-u)(w-v)=C_i`.
2. Common values of the negative algebraic Legendre-dual maps
   `L_i(t)=-Bt^2/2-d_i`
   are represented exactly by
   `B(y^2-x^2)=C_i`.
3. `Phi(x,y)=(y-x,y+x)` is an isomorphism from this dual-overlap variety to
   `H_(B,C_i)={(a,b):Bab=C_i}`.
4. If `X_i` is the concurrence configuration space with `u!=v`, simultaneous additive translation of `(u,v,w)` is free and
   `X_i/G_a ~= H_(B,C_i)\Delta_i`,
   where `Delta_i={(a,a):Ba^2=C_i}`.
   Hence the distinct-tangent quotient equals the full split hyperbola iff `Delta_i(K)` is empty. If repeated tangents are allowed, the deleted diagonal is restored.

### Theorem B — finite-field sign quotient

Let `F_q` be a finite field of odd cardinality, let `B,C in F_q^*`, and let `chi_q` be its quadratic character. Then

`|R|=q-1`

for

`R={(x,y):B(y^2-x^2)=C}`,

and

`|R/{+/-1}^2|`
`=[q+1+chi_q(BC)+chi_q(-BC)]/4`.

When `C=2(d_0-d_1)`, the quotient is canonically the common negative-dual-value set for those two shifts.

If this quotient has one orbit, then `q<=5`, by orbit capacity alone.

For odd prime `q`, `chi_q` may be written as the Legendre symbol.

### Theorem C — central-lane Joukowski quotient and extremal uniqueness

Let `s>=3` be odd and let `q` be an odd prime with `q∤2s`. Put

`Lambda_s(a)=-sa-1/(2a)`, `a in F_q^*`.

With `c=(2s)^(-1)`, `Lambda_s` is exactly the quotient map for the involution

`a -> c/a`,

and

`|Im Lambda_s|=[q+Legendre(c,q)]/2`.

The central packet saturates every nonzero residue modulo `q` iff

`Im Lambda_s subseteq J_s (mod q)`.

If `2s-1` is prime and the lower extremal saturates, then `(s,q)=(3,5)`. If `2s+1` is prime and the upper extremal saturates, then `(s,q)=(3,7)`. Both saturations actually occur at `s=3`; hence `s=3` is the unique nontrivial odd-sector parameter saturating both prime extremal boundaries.

### Theorem D — bounded boundary closure

Assume an odd universal breaker `q_b` has exact breaker-coprime capacity

`k_*=2q_b-1`

and satisfies the independently established bound `q_b<=5`.

For nontrivial odd `s>=3`, simultaneous closure

`k_*-4=2s-1`,
`k_*-2=2s+1`

is equivalent to `q_b=s+2`, and therefore uniquely yields

`(s,q_b,k_*)=(3,5,9)`.

At this solution

`M_9=35`,
`3M_9=105`,
`3M_9+1=106=2*53`.

This is a breaker-coprime capacity theorem only, not an unrestricted prime-run theorem.

### Corollary E — `s=3` lane arithmetic

Under the explicit identification of the native `C3` slot-unfolding with the `s=3` central lane set `j=-1,0,1`, its three lane values are exactly

`6m^2-2m+1`,
`6m^2+1`,
`6m^2+2m+1`.

Also `3M_9=105`; hence the longitudinal closure extremum equals the stated `105` bouquet-gate integer exactly. No stronger provenance/mechanism identification is certified by this blind replication.

## 13. Final hard-target verdict

`HARD_TARGET_MET = YES`

`FINAL_OUTCOME = POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`

The source package should **not** be promoted verbatim without the H1 bridge correction and the C2/H2 wording cleanups above.

Per the taskbook stop rule, this return freezes the independent result. No withheld #627 proof/checker or prohibited source branch was read.
