# BRC E3 Selector — Hidden Factor Character / Lift Reduction

Status: `RESEARCH NOTE / EXACT LOCAL REDUCTIONS + TARGETED FINITE SHADOW COLLISION / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Researcher-ID: `EM-DIRECT-7K3Q`
Parent: `research_notes/BRC_E3_LOCAL_RESIDUE_CEILING_AND_VALUATION_SELECTOR_20260908.md`
Source snapshot immediately before write: `main@c07e4b3b7780bbd9ab11abc5bf9f2f7a262ba562`

## 0. Purpose

The parent note classifies the complete factor-blind fixed-local ceiling for

`E3 = 2(p+q)^2-6N`.

This continuation asks what the **first residue beyond that ceiling actually means**.

The answer is sharper than “one more hidden energy bit”:

> the first free E3 digit is an individual-factor local character or principal-unit lift that multiplication into `N=pq` has erased.

This converts the surviving BRC target from generic residue prediction into a hidden-factor orbit-selection problem.

Define

`P(N)=2(N^2-N+1)`,

`D=P(N)-E3=2(p^2-1)(q^2-1)`.

The first free digit at a prime `ell` is a normalized digit of `D` just beyond the forced local valuation floor.

## 1. Prime-modulus orbit identity

For an odd prime `ell` not dividing `N`, write `n=N mod ell` and let a possible factor residue be `x`, with the other factor residue `n/x`.

If

`(x+n/x)^2=(z+n/z)^2 mod ell`,

then either

`x+n/x = z+n/z`,

which gives

`z=x or z=n/x`,

or

`x+n/x = -(z+n/z)`,

which gives

`z=-x or z=-n/x`.

Hence `S^2 mod ell` identifies exactly the hidden factor-residue orbit

`{x, n/x, -x, -n/x}`.

Equivalently, once `N mod ell` is fixed, an extra `E3 mod ell` value is not an unrelated energy statistic: it is exactly partial recovery of the factor residue modulo `ell`, up to swap and simultaneous sign.

This is the conceptual meaning of the local orbit count in the RSA-270 synthesis.

## 2. First 2-adic free bit is a fixed-base quadratic-residuosity bit

Assume

`N=1 or 7 mod8`.

The parent note proves that `E3` is factor-blindly fixed mod128 but not mod256. Define

`d2 = D/128 mod2`.

Because

`D = 2(p^2-1)(q^2-1)`, 

we have

`d2 = ((p^2-1)/8) * ((q^2-1)/8) mod2`.

For an odd prime `r`,

`(r^2-1)/8` is odd iff `r=3 or5 mod8`,

which is exactly iff the Legendre symbol `(2/r)=-1`.

Since `N=1 or7 mod8`, the two factors lie in the same `(2/r)` class. Therefore

`d2 = (1-(2/p))/2 = (1-(2/q))/2`.

So:

- `d2=0` iff `(2/p)=(2/q)=+1`;
- `d2=1` iff `(2/p)=(2/q)=-1`.

The public Jacobi symbol is `(+1)` in both cases. Thus the next E3 bit decides whether the fixed base `2`, known to have Jacobi symbol `+1`, is a quadratic residue modulo **both** hidden prime factors or a nonresidue modulo both.

By CRT:

`d2=0` iff the congruence `x^2=2 mod N` is locally solvable at both prime factors.

This is a fixed-base quadratic-residuosity decision problem, not a new species of collision statistic.

Important boundary: this interpretation does not prove that deciding this fixed-base bit is equivalent to factoring. It does show that any claimed cheap BRC evaluator for the first 2-adic E3 lift must be compared against the classical quadratic-residuosity problem rather than only against residue-table baselines.

### Favorable public class `N=3 or5 mod8`

Here `(2/N)=-1`, so exactly one factor has `(2/r)=+1` and the other has `-1`. The factor-blind E3 floor is already mod256.

The first free bit at mod512 refines the `+1` factor from its `+-1 mod8` class into its next mod16 lift. This is a deeper individual 2-adic character/lift, again erased by the product residue.

## 3. First 3-adic lift is hidden factor membership in the cube subgroup mod9

Write the two factor residues modulo 9 as

`p = eps*(1+3a)`,

`q = eta*(1+3b)`,

where `eps,eta in {+1,-1}` and `a,b in F_3`.

Then

`(p^2-1)/3 = 2a mod3`,

`(q^2-1)/3 = 2b mod3`.

Therefore the first normalized 3-adic defect digit is

`d3 := D/9 mod3 = 2ab mod3`.

The public residue `N mod9` determines both

`eps*eta`

and

`a+b mod3`.

Consequently, if both `a,b` are nonzero, their product `ab` — and hence the nonzero value of `d3` — is already public. The only hidden decision is whether one of `a,b` is zero.

Thus:

`d3=0` iff `p=+-1 mod9` or `q=+-1 mod9`.

The subgroup `{+-1}` is exactly the cube subgroup of `(Z/9Z)^*`. So the first mod27 E3 lift is a binary decision about whether one hidden factor lies in that subgroup. If neither does, the unique nonzero ternary digit is forced by `N mod9`.

This explains why every unit `N mod27` has exactly two local `S^2` values despite the next digit being ternary.

## 4. First 5-adic lift is the hidden principal-unit digit of one factor

Assume `(N/5)=-1`, so `N=2 or3 mod5`.

Exactly one factor lies in the `+-1 mod5` class. Call it `p_A` and write

`p_A = eps*(1+5t) mod25`,

with `eps in {+1,-1}` and `t in F_5`.

The other factor lies in the `+-2 mod5` class, so its square minus one is

`q^2-1 = 3 mod5`.

Also

`(p_A^2-1)/5 = 2t mod5`.

Hence

`d5 := D/5 mod5`

satisfies

`d5 = 2 * (2t) * 3 = 2t mod5`.

Therefore

`t = 3 d5 mod5`,

and the hidden factor lift is recovered as

`p_A = +-(1+15 d5) mod25`.

So the five possible `E3 mod25` lifts are not merely five energy buckets. They are exactly the five principal-unit lifts of the hidden factor that is already known only to lie in `+-1 mod5`, modulo the unavoidable sign symmetry.

This is why a Boolean valuation test `v5(D)>=2` is insufficient: it recognizes only `t=0`. The full first 5-adic E3 digit recovers a genuine base-5 factor-residue digit.

For RSA-270, whose public class has `N mod5=2`, any improvement beyond the current `E3 mod5760` ceiling through the 5-adic channel must therefore recover this hidden factor lift.

## 5. Operator-level consequence: pure modular ring circuits are dead

Suppose a proposed N-only E3 residue evaluator is built only from fixed modular ring operations on `N`:

`+,-,*,fixed powers`,

and inverses of values already certified as units, followed by reduction modulo a fixed `M`.

Then the output factors through `N mod M`.

The fixed-local ceiling theorem therefore kills the evaluator immediately once the target digit lies beyond the singleton ceiling. It cannot select an individual-factor orbit because no such distinction exists in its input quotient.

Hence any surviving BRC selector must contain a **non-congruence-stable operation before final reduction**, such as:

- floor / integer-square-root / carry information;
- an exact comparison or threshold;
- gcd with `N`;
- multiplicative order / exponent-valuation behavior modulo `N`;
- another provenance-bearing operation that does not descend to the public `N mod M` quotient.

This does not make such an operator useful automatically. It only identifies the minimum semantic type required to escape the fixed-local no-go.

The project root/remainder states `J_m=floor(sqrt(mN))`, `R_m=mN-J_m^2` are therefore at least of the correct nonlocal type, because the low bits of `J_m` can depend on high bits of `N`. The question is whether they preserve the required **individual-factor character**, not whether they contain more information than `N` in an extensional sense.

## 6. Targeted m=1,3 shadow collision on the first free 2-adic bit

A finite exact search over genuine prime semiprimes produced a balanced collision tailored to the selector above:

`N_A = 23,987,401 = 4721 * 5081`,

`N_B = 23,987,657 = 4787 * 5011`.

The factor ratios are approximately `1.0763` and `1.0468`.

For both integers:

`N mod256 = 201`,

`J_1 = floor(sqrt(N)) = 4897`,

`J_3 = floor(sqrt(3N)) = 8483`.

Their exact remainders differ only by multiples of 256:

- `R_1(N_A)=6792`, `R_1(N_B)=7048=6792+256`;
- `R_3(N_A)=914`, `R_3(N_B)=1682=914+3*256`.

Hence the enriched low-bit signature is identical:

`(N,J1,R1,J3,R3) mod256 = (201,33,136,35,146)`.

Yet their first free selector bits are opposite:

- `N_A`: `v2(D)=10`, so `d2=0` and `E3=18 mod256`;
- `N_B`: `v2(D)=7`, so `d2=1` and `E3=146 mod256`.

The public baseline is the same:

`P(N)=18 mod256` for the shared class `N=201 mod256`.

Thus the second energy differs by exactly 128, the unique first-free bit.

This strengthens the earlier mod127 m=1,3 collision in the precise direction now required:

> even the enriched `(N,J1,R1,J3,R3) mod256` compression fails exactly on the first hidden quadratic-residuosity / E3 selector bit, and the failure occurs for near-balanced prime semiprimes.

This is a finite collision witness for that declared compressed observer, not a lower bound against full exact `N` or against richer pre-compression BRC provenance.

## 7. Revised BRC target

The collision-energy program should no longer ask generically for

`E3 mod M`.

The correct target is now:

`N -> hidden factor orbit character/lift`.

In order of diagnostic economy:

1. on `N=1,7 mod8`, test whether a new pre-compression BRC observer predicts the fixed-base quadratic-residuosity bit `d2` exactly;
2. on mod9, test the binary hidden cube-subgroup membership selector underlying `d3`;
3. on `N/5=-1`, test the full five-way principal-unit digit `d5`, not just a zero/nonzero valuation flag;
4. only after one of these survives exact collision tests should larger prime moduli be attempted, because for `ell>=7` selecting `E3 mod ell` is already partial factor-residue recovery among multiple prime-field orbits.

Kill conditions remain strict:

- if the observer factors through public fixed-local residue data, reject as residue facade;
- if same observer signature admits opposite selector labels, reject deterministic recovery by that observer;
- if the evaluator uses gcd/order machinery that already isolates a factor orbit by a classical route, classify it as a classical reduction rather than a new collision-energy primitive;
- if only statistical correlation survives, keep it as reconnaissance, not an exact leak.

## 8. Current verdict

The first-free E3 digits are now semantically identified:

- 2-adic unfavorable class -> individual Legendre-symbol / quadratic-residuosity bit;
- 3-adic first lift -> hidden cube-subgroup membership mod9;
- 5-adic nonresidue class -> hidden principal-unit factor digit mod25.

Therefore the remaining BRC problem is not “find another modular identity.” It is:

> construct, from N-visible pre-compression BRC operations, an individual-factor local character/lift selector that multiplication into N has erased, and do so without paying the classical factor-isolation cost.

The current low-bit m=1,3 root/remainder compression does not meet that requirement.