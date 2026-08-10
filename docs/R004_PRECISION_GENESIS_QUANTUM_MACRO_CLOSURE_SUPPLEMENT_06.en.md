# R004 precision genesis — Supplement 06: fractionless count defects, exponent coordinates, and valuation repair

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_05.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

This supplement responds to a structural problem exposed by the previous R004 continuation: normalized fractions such as `eta`, Bell total-variation costs, or macro pair fractions had begun to appear as if they were primitive quantities. The present result is that they do not need to be primitive.

The stronger conclusion is **not** that every calculation should be forced into one exponent coordinate. Different future languages have different safe coarse states. The emerging native interface is layered:

`integer count ray -> integer defect functional -> prime-exponent word -> operation-conditioned residue repair`.

Conventional fractions remain useful at external scientific interfaces, but the current R004 mathematics can keep its internal state finite and integer-first.

## 1. Rational normalization can be demoted to a count-ray view

Let

`q=(q_1,...,q_m)`

be a finite rational probability vector. Clear all denominators with one positive integer `L`. Then

`c_i=L q_i`

are non-negative integers and

`sum_i c_i=L`.

Conversely every nonzero integer count vector `c` defines the rational normalized view

`q_i=c_i/sum_j c_j`.

Two count vectors define the same normalized view exactly when all cross products agree:

`c_i sum(d) = d_i sum(c)` for every `i`.

Dividing all entries by their gcd gives a unique primitive integer representative of the same ray.

Therefore rational finite distributions may be carried internally as

\[
\boxed{[c_1:\cdots:c_m]}
\]

with integer counts rather than as a tuple of fractions.

This is elementary denominator clearing/projective count mathematics, not a new Enterprise Math theorem.

## 2. Comparison becomes an integer cross defect

For two normalized parts conventionally written `a/b` and `c/d`, define the signed integer

\[
\boxed{\Delta=ad-cb.}
\]

Then

- `Delta=0` iff the two normalized quantities are equal;
- `Delta>0` iff the first is larger;
- `Delta<0` iff the second is larger.

No division is needed.

Under independent positive replication of the two count states, `Delta` is multiplied by a positive integer, so its sign and zero/nonzero status are invariant. This makes the cross defect a natural internal proof object even when a fraction remains the preferred external display.

## 3. Integer linear defect functionals unify kill tests

More generally, let a finite count state be

`z in N_0^m`

and let

`h in Z^m`.

Define

\[
\boxed{\Delta_h(z)=h\cdot z.}
\]

Replicating all counts by `k>0` gives

`Delta_h(kz)=k Delta_h(z)`.

Hence sign, exact zero, and half-space membership are independent of normalization.

This single object covers several R004 cases:

- Bell/CHSH separating certificates;
- experimental lower-bound margins;
- cross-multiplied comparisons of macro count words;
- future finite linear constraints where only the sign or vanishing defect matters.

### Integer-cone consequence

If `g_1,...,g_r` are deterministic integer generators and

`Delta_h(g_i)<=0`

for every generator, then every non-negative integer combination

`z=sum_i w_i g_i`

also satisfies

`Delta_h(z)<=0`.

Therefore a target `t` with

`Delta_h(t)>0`

has an exact integer impossibility certificate: it is outside the generator cone/monoid. This is elementary linearity/convex-semigroup mathematics, not a new separation theorem.

## 4. Bell no longer needs a primitive probability fraction

For one deterministic local response table

`lambda=(A_0,A_1,B_0,B_1)`,

define its five-coordinate integer generator

\[
g_\lambda=(A_0B_0,A_0B_1,A_1B_0,A_1B_1,1).
\]

For the existing exact R004 target, the four setting correlation numerators and common count mass are

\[
\boxed{t=(-12,-12,-16,16,20).}
\]

Choose the integer functional

\[
\boxed{h=(-1,-1,-1,+1,-2).}
\]

For all sixteen local deterministic generators,

`h dot g_lambda` is either `0` or `-4`.

But

\[
\boxed{h\cdot t=16>0.}
\]

Thus the target is separated from the setting-independent local count cone by the **integer Bell defect 16**. The normalized statement `|S|=14/5>2` is only one external rendering of this same finite obstruction.

Bell/CHSH mathematics remains prior art. The R004 change is representational: the primitive executable witness can be the integer cone certificate rather than a rational expectation value.

## 5. Measurement dependence becomes seed-transfer cost

Let two equal-total latent count rows be `u` and `v`. Define the **seed-transfer defect**

\[
T(u,v)=\sum_i\max(u_i-v_i,0).
\]

Equal total mass implies the positive and negative excesses are equal, so `T` is exactly the minimum number of count atoms that must be reassigned to transform one row into the other. It is equal to half the ordinary `L1` distance, but no division is required to compute it.

For four CHSH setting-conditioned latent rows, let

`T=max_(s,t) T(mu_s,mu_t)`.

If the common setting mass is `W` and the integer CHSH numerator is `N`, define the Bell excess

\[
\boxed{B=|N|-2W.}
\]

The previously derived relaxed measurement-independence inequality becomes the entirely integer statement

\[
\boxed{B\le6T.}
\]

For the explicit R004 denominator-60 witness:

\[
W=60,\qquad N=-168,\qquad B=48,
\]

and **every one of the six pairs** of setting rows has

\[
\boxed{T=8.}
\]

Hence

\[
\boxed{B=6T=48.}
\]

The earlier number `2/15` is the normalized external view `T/W=8/60`. The fraction is no longer needed as the native sharp statement.

## 6. Record overlap becomes an integer two-cell state

For threshold-record resolution `d` and alternative separation `delta`, define

\[
A=\max(d-\delta,0),
\qquad
S=\min(d,\delta).
\]

Then

\[
\boxed{A+S=d.}
\]

`A` is the number of environment states producing the same record and `S` the number producing separated records. The conventional overlap

`eta=A/d`

is an external normalized view.

If an experiment supplies a rational lower threshold `q/s`, compare it through the integer margin

\[
\boxed{K=sA-qd.}
\]

`K>=0` means the finite count state can reach the threshold; `K<0` excludes it under the declared multiplicative visibility model.

For the representative `9/100` Pedalino lower endpoint, the internal test is simply

\[
\boxed{K=100A-9d.}
\]

No decimal or fraction is required inside the model.

## 7. Macro crossover also stays as a count word

For path `P_N` and record resolution `d`, retain the two integers

\[
Z(N,d)=\#\{\text{unordered pairs with zero overlap}\},
\]

\[
O(N,d)=\#\{\text{unordered pairs with positive overlap}\}.
\]

For `N>d`,

\[
\boxed{Z(N,d)=\binom{N-d+1}{2}},
\]

and

`Z+O=binom(N,2)`.

The conventional zero-overlap fraction is only the external view `Z/(Z+O)`.

Its monotonicity can be checked without division by the integer cross defect

\[
\boxed{
G_N
=Z(N+1,d)T_N-Z(N,d)T_{N+1}
\ge0,
}
\]

where `T_N=binom(N,2)`. Thus even a statement normally phrased as monotonic growth of a ratio can remain an integer theorem.

Binomial-coordinate counting is established prior mathematics [SRC-CHABERT-2025-INTEGER-VALUED-POLYNOMIALS].

## 8. P005 scale multiplication linearizes exactly in exponent space

For a positive scale factor

\[
\lambda=\prod_p p^{a_p},
\]

define its finite-support exponent word

\[
\boxed{\nu(\lambda)=(a_p)_p.}
\]

Unique factorization gives the exact correspondences

\[
\nu(\lambda\mu)=\nu(\lambda)+\nu(\mu),
\]

\[
\nu(\gcd(\lambda,\mu))=\min(\nu(\lambda),\nu(\mu)),
\]

\[
\nu(\operatorname{lcm}(\lambda,\mu))=\max(\nu(\lambda),\nu(\mu)),
\]

where min/max are coordinatewise.

Therefore the P005 positive-integer scale lattice can be represented without logarithms as a finite-support integer lattice/monoid.

### Rank and total depth separate

Define

\[
\boxed{D(\lambda)=\omega(\lambda)=\#\{p:a_p>0\}}
\]

and

\[
\boxed{H(\lambda)=\Omega(\lambda)=\sum_p a_p.}
\]

`D` counts active prime axes; `H` counts total prime-step depth. They are distinct finite resources.

In the global divisibility Hasse graph where one edge multiplies or divides by one prime,

\[
\boxed{
d_H(\lambda,\mu)
=\sum_p|a_p-b_p|.
}
\]

Equivalently, with `g=gcd(lambda,mu)`,

\[
d_H(\lambda,\mu)
=\Omega(\lambda/g)+\Omega(\mu/g).
\]

For the equal-exponent candidate `lambda=P^a` with squarefree rank `D`,

`H(lambda)=D a`,

which matches the opposite-corner diameter of the corresponding exponent divisor grid.

All of these identities are standard unique-factorization arithmetic; R004's contribution is their use as a native precision coordinate interface.

## 9. Positive rational multiplicative quantities can also be exponent words

For a positive rational number `r=a/b`, define

\[
\boxed{
\nu(r)=\nu(a)-\nu(b)\in\bigoplus_p\mathbb Z.
}
\]

Thus the external fraction `2/15` has the exact Laurent exponent word

`{2:+1, 3:-1, 5:-1}`.

This shows that even when a normalized multiplicative quantity must be retained exactly, the slash is not fundamental.

However this representation is **not** a reason to force additive physics into exponent coordinates. Addition exposes a sharp failure boundary.

## 10. Valuation-only addition is safe off the diagonal

Fix a prime `p`. Classical p-adic valuation satisfies [SRC-EOM-PADIC-VALUATION]

\[
\nu_p(x+y)\ge\min(\nu_p(x),\nu_p(y)).
\]

If the two input levels differ, equality is forced:

\[
\boxed{
\nu_p(x)\ne\nu_p(y)
\Longrightarrow
\nu_p(x+y)=\min(\nu_p(x),\nu_p(y)).
}
\]

Thus a valuation-only coarse state is exactly sufficient for addition **off the equal-level diagonal**.

This resembles min-plus/tropical arithmetic, which is established prior mathematics [SRC-RICHTERGEbert-STURMFELS-THEOBALD-2003-TROPICAL]. R004 does not claim invention of the min rule.

## 11. Equal-level valuation carry is unbounded

The diagonal is fundamentally different.

Fix any prime `p`, base level `k>=0`, and desired extra depth `m>=1`. Let

\[
x=p^k,
\qquad
y=p^k(p^m-1).
\]

Then

\[
\nu_p(x)=\nu_p(y)=k,
\]

but

\[
\boxed{
\nu_p(x+y)=k+m.
}
\]

Since `m` is arbitrary, no bounded carry rule depending only on the two equal valuation levels can determine the sum level.

This is the exponent-calculus analogue of a P018 carry event: discarded unit/residue information can propagate arbitrarily far upward in valuation depth.

## 12. Finite cap K admits an exact residue repair

Define the capped observation

\[
q_K(x)=\min(\nu_p(x),K),
\]

with multiples of `p^K` and zero placed in level `K`.

For an uncapped level `a<K`, write

\[
x=p^a u,
\qquad p\nmid u.
\]

Retain the normalized unit residue

\[
\boxed{
uu=u\bmod p^{K-a}.}
\]

The repaired state is

\[
\boxed{\sigma_{p,K}(x)=(a,\nuu).}
\]

For level `K`, use one terminal marker.

This signature is equivalent to the residue `x mod p^K`, but factorized into an exponent level plus only the unit detail required at that level. Two repaired signatures can be added entirely by integer modular arithmetic, and the result determines the capped valuation of the sum exactly.

## 13. The unit-residue repair is sharp for arbitrary partners

At fixed level `a<K`, there are exactly

\[
\boxed{
\varphi(p^{K-a})
=(p-1)p^{K-a-1}
}
\]

possible normalized unit residues.

No two distinct unit residues can be merged if the future language contains arbitrary additive partners.

Indeed, let `u` and `u'` be two distinct units modulo

`M=p^{K-a}`.

Choose the unit partner

\[
v\equiv-u\pmod M.
\]

Then

`u+v` is divisible by `M`,

while

`u'+v` is not, because `u'!=u mod M`.

After restoring the common factor `p^a`, the first sum reaches capped level `K` and the second does not. Therefore the two unit residues have different future signatures.

So the unit-residue classes are not arbitrary implementation detail; they are forced by the declared all-partner additive language.

## 14. Universal translations destroy all valuation compression

The class counts telescope:

\[
1+\sum_{a=0}^{K-1}\varphi(p^{K-a})
=1+\sum_{h=1}^{K}\varphi(p^h)
=\boxed{p^K}.
\]

There is an even shorter future-signature proof.

Work on residues modulo `p^K`. If

`x != x' mod p^K`,

choose the translation

\[
t\equiv-x\pmod{p^K}.
\]

Then

\[
q_K(x+t)=K,
\]

whereas

\[
q_K(x'+t)<K.
\]

Therefore the family of all additive translations separates every residue. The coarsest quotient safe for that complete translation language is exact residue equality modulo `p^K`.

Hence

\[
\boxed{
\text{valuation-only }(K+1)\text{-class compression}
\xrightarrow{\text{all translations}}
p^K\text{ exact residue classes}.
}
\]

This is the strongest negative result of the supplement.

### Interpretation

Exponent/valuation coordinates are not a universal replacement for remainder information. They are operation-relative:

- multiplication, divisibility, gcd/lcm: exponent coordinates are native;
- addition with unequal valuation levels: exponent levels suffice;
- addition on equal levels: carry depends on unit detail;
- universal additive translation language: the future-safe repair restores the full residue state.

This is exactly the type of operation-conditioned precision boundary P023/P024 were built to express.

## 15. Fraction-free exact linear algebra is a tool route, not a novelty claim

If later R004 constraints become large systems of exact linear equations/inequalities, introducing ordinary rational Gaussian elimination would be unnecessary. Bareiss's integer-preserving elimination is established prior art for fraction-free exact linear algebra [SRC-BAREISS-1968-FRACTION-FREE].

R004 does not need that machinery for the present Bell certificate, but the prior-art lesson is important: exact constraint solving can remain integer-first without pretending that fraction-free elimination was invented here.

## 16. Independent executable pressure test

Before documentation/promotion, the new formulas were independently checked with exact integer enumeration:

- **10,000** scale pairs `1..100 x 1..100` for product-to-sum, gcd-to-min, lcm-to-max and Hasse-distance identities;
- **2,970** path `(N,d)` cases for non-negative normalized-growth cross defects;
- all **16** local deterministic Bell generators, with integer dual defects only `0` or `-4`, while the target defect is `+16`;
- all six pairs of the explicit setting-dependent Bell witness have seed-transfer defect exactly `8`;
- **414,620** capped p-adic residue-pair additions for `p in {2,3,5}`, `K=1..4`, all reproduced exactly by the repaired `(level,unit residue)` signature;
- **930** residues across the same bounded prime/cap families for which universal-translation future signatures were checked injective.

These are bounded executable checks and do not replace the ordinary proofs above. A fresh full-repository CI pass is not claimed merely from these independent checks.

## 17. Revised R004 arithmetic architecture

The main conclusion is not “fractions are forbidden.” It is more precise:

### Native finite layer

Use

\[
\boxed{
\text{Count} + \text{Defect} + \text{Exponent} + \text{Repair}
}
\]

as the internal state language whenever the declared operations permit it.

### External interface layer

Convert to fractions, percentages, real-valued expectations, conventional visibility, TV distance or other normalized scientific quantities only when communicating with an external theory/experiment whose published observable is stated that way.

### Operation-safety rule

No compressed coordinate is globally privileged. The legal representation is determined by the future operation language:

- count rays are sufficient for finite rational normalization;
- integer defect functionals are sufficient for homogeneous inequalities/certificates;
- exponent words are sufficient for multiplicative scale algebra;
- residue repair is required when addition/cancellation makes valuation-only states unsafe.

This is more compatible with Enterprise Math than replacing one universal real-number coordinate by one universal exponent coordinate.

## 18. Foundation feedback candidate

The reusable cross-route finding is:

> **A native finite coordinate should be selected by its safe future-operation family, not by aesthetic preference for scalar, fraction, exponent, or residue form.**

R004 supplies one sharp specialization:

- valuation level is a legal coarse state for multiplicative/min-max operations;
- it is partially legal for addition off the equal-level diagonal;
- it is not safe for universal additive translation;
- the exact repair under the universal translation language is the full residue modulo `p^K`.

This should be relayed to P018/P023/P024/Foundation as a `CONSUME/TEST` result. It is not yet a request to replace the existing Foundation primitive state by valuation vectors, because the same theorem proves that doing so globally would be wrong.
