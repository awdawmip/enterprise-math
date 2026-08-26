# Odd-sector lane-label Joukowski image theorem

Status: `FREE_RESEARCH_EXACT_TRANSVERSE_QUOTIENT / CLASSICAL_JOUKOWSKI_COMPONENT / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on the odd-sector central-fiber saturation theorem.

Only `s=3` is native Enterprise geometry; general odd `s` is the controlled shell allocator.

## 1. Central s-slot packet and the longitudinal hyperbola

For positive odd `s`, the central even-shell packet is

`P_(s,j)(m)=2s*m^2+2j*m+1`,

with lane labels

`j=-(s-1)/2,...,(s-1)/2`.

For an odd prime `q` with `q` not dividing `2s`, consider the same split-hyperbola coordinate used by the longitudinal theory:

`s*a*b=-1`.

Take

`a=m`.

For every nonzero `m mod q`, there is a unique hyperbola point because

`b=-1/(s*a)`.

Thus

`F_q^* ~= H_(s,-1)(F_q)`

through the first hyperbola coordinate.

## 2. Lane-label map

On the hyperbola,

`1=-s*a*b`.

Therefore

`P_(s,j)(a)`

`=2s*a^2+2j*a-s*a*b`

`=a*(2s*a+2j-s*b)`.

Since `a!=0`, lane `j` vanishes iff

`2s*a+2j-s*b=0`.

Hence the unique lane label associated to a hyperbola point is

`Lambda_s(a,b)=s*(b-2a)/2`.

Using `b=-1/(s*a)`, this becomes

`Lambda_s(a)`

`=-s*a-1/(2a)`

`=-s*(a+kappa/a)`,

where

`kappa=1/(2s)`.

Freeze:

`TRANSVERSE LANE DIVISIBILITY = JOUKOWSKI LANE-LABEL MAP ON THE SAME SPLIT HYPERBOLA`.

## 3. Exact root/lane equivalence

For every nonzero `a mod q`:

`P_(s,j)(a)=0`

iff

`j=Lambda_s(a)`.

Therefore the full central packet saturates every nonzero `m` class modulo `q` exactly when

`Im(Lambda_s) subseteq J_s`,

where

`J_s={-(s-1)/2,...,(s-1)/2}`

is the set of native lane labels reduced modulo `q`.

When `q>s`, the lane labels are distinct, so the number of roots of lane `j` is exactly the fiber size

`|Lambda_s^(-1)(j)|`.

Thus the previous Legendre root profile is the fiber-count profile of one Joukowski map.

## 4. Classical Joukowski image size

Consider

`J_kappa(a)=a+kappa/a`

on `F_q^*`.

The involution

`a -> kappa/a`

has:

- two fixed points iff `kappa` is a quadratic residue;
- no fixed point iff `kappa` is a nonresidue.

Every nonfixed orbit has size2, and each orbit gives one Joukowski value.

Therefore

`|Im J_kappa|=(q+Legendre(kappa,q))/2`.

Scaling by the nonzero factor `-s` does not change image size, so

`|Im Lambda_s|`

`=[q+Legendre(1/(2s),q)]/2`.

This is a classical Joukowski/inversion quotient count; no novelty is claimed for the count itself.

## 5. Structural saturation bound

For `q>s`, complete central-packet saturation requires

`Im Lambda_s subseteq J_s`.

Since `|J_s|=s`, necessarily

`[q+Legendre(1/(2s),q)]/2 <= s`.

Hence:

### residue branch

If

`Legendre(1/(2s),q)=+1`,

then

`q<=2s-1`.

### nonresidue branch

If

`Legendre(1/(2s),q)=-1`,

then

`q<=2s+1`.

This refines the generic root-slot bound `q<=2s+1` by explaining the two possible extremal cases through the ramification of the Joukowski involution.

## 6. Fiber multiplicities

The equation

`Lambda_s(a)=j`

is exactly

`2s*a^2+2j*a+1=0`.

Its discriminant is

`4(j^2-2s)`.

Therefore the fiber size is

`1+Legendre(j^2-2s,q)`.

This recovers the earlier root-profile formula

`omega_s(q)=sum_(j in J_s) |Lambda_s^(-1)(j)|`

`=s+sum_(j in J_s) Legendre(j^2-2s,q)`.

Thus the Legendre profile is not a separate construction; it is the ramification profile of the lane-label Joukowski map.

## 7. Native s=3, q=5: ramified extremal image collapse

Take

`s=3`, `q=5`.

Then

`kappa=1/6=1 mod5`

is a square.

Therefore

`|Im Lambda_3|=(5+1)/2=3=s`.

Directly,

`Im Lambda_3={-1,0,+1}=J_3`.

The Joukowski involution has two fixed points, so two image fibers have size1 and one has size2.

They are exactly:

- lane `-1`: size1;
- lane `0`: size2;
- lane `+1`: size1.

Thus the native mod5 root multiplicity

`1:2:1`

is the ramification profile of the extremal residue-branch Joukowski quotient at

`q=2s-1`.

## 8. Native s=3, q=7: unramified extremal image collapse

Take

`s=3`, `q=7`.

Then

`kappa=1/6=6 mod7`

is a nonresidue.

Therefore

`|Im Lambda_3|=(7-1)/2=3=s`.

Again

`Im Lambda_3={-1,0,+1}=J_3`.

The involution has no fixed point, so every fiber has size2.

Thus the mod7 multiplicity is

`2:2:2`.

This is the unramified extremal nonresidue-branch image collapse at

`q=2s+1`.

## 9. Native q=3 boundary

At q=3, the coefficient `s=3` vanishes, so the nonsingular hyperbola/Joukowski description degenerates.

The transverse packet still has the exact outer-lane pattern

`1:0:1`.

Hence the three factors of the native 105 gate now have a unified classification:

- `3`: coefficient-degenerate boundary;
- `5=2s-1`: ramified Joukowski image collapse onto all three native lanes;
- `7=2s+1`: unramified Joukowski image collapse onto all three native lanes.

## 10. A compact explanation of 105

For native `s=3`, the central-fiber gate is

`3*5*7`.

The factors can now be read as

`s`

`x (2s-1)`

`x (2s+1)`

because both extremal Joukowski branches saturate:

`105=3*5*7=3*(2*3-1)*(2*3+1)`.

This equality is special: general odd `s` need not have both `2s-1` and `2s+1` prime or saturating.

## 11. Relation to longitudinal hyperbola quotient

Two different quotient maps now live on the same split hyperbola:

1. the longitudinal `K_4` quotient, whose orbit count controls transparency/breaking;
2. the transverse lane-label Joukowski quotient, whose image/fiber profile controls which central packet lane is divisible.

For native q=5, both quotient mechanisms collapse maximally:

- the longitudinal K4 quotient has one class -> universal breaker;
- the transverse Joukowski image has exactly the three lane labels -> complete C3 saturation.

For native q=7:

- the longitudinal K4 quotient has two classes -> nonbreaker;
- the transverse Joukowski image still has exactly three lane labels -> complete C3 saturation.

This precisely separates why5 belongs to both longitudinal and transverse gate mechanisms, while7 belongs only to the transverse one.

## 12. Prior-art boundary

Joukowski maps, inversion quotients, Dickson polynomials and their value sets are classical.

The research-specific candidate is the fact that the odd-sector shell allocation selects this exact lane-label Joukowski map on the same hyperbola that independently carries the longitudinal tangent/cover quotient.