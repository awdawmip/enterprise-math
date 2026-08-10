# Prior art — R004 fractionless count/defect/exponent calculus

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

This note separates established mathematics from R004's project-specific use of those tools. The fact that a construction uses only integers does not make the underlying mathematics new.

## 1. Prime-exponent and valuation coordinates are established

Unique factorization identifies a positive integer with its finite prime-exponent word. Equivalently, the multiplicative monoid of positive integers is the free commutative monoid on the primes, and the multiplicative group of positive rationals is represented by finitely supported integer exponent words. Under these coordinates multiplication becomes exponent addition; divisibility becomes coordinatewise order; gcd/lcm become coordinatewise minimum/maximum.

The p-adic valuation is classical and satisfies

`v_p(xy)=v_p(x)+v_p(y)`

and

`v_p(x+y)>=min(v_p(x),v_p(y))`,

with equality when the two input valuations differ [SRC-EOM-PADIC-VALUATION]. R004 therefore does **not** claim valuation arithmetic, p-adic orders, non-Archimedean norms, or ultrametricity as inventions.

## 2. Tropical/min-plus algebra is established

Tropical geometry works over min-plus/max-plus semirings and has a mature literature [SRC-RICHTERGEbert-STURMFELS-THEOBALD-2003-TROPICAL]. Consequently R004 must not rename the off-diagonal valuation identity

`v_p(x+y)=min(v_p(x),v_p(y))`

as a new tropical arithmetic.

R004's narrower use is a **negative boundary**: valuation-only addition behaves min-plus when the input levels differ, but equal-level addition can have arbitrarily deep extra divisibility. That cancellation/carry boundary is then interpreted through the already-canonical P023/P024 question of which future operations descend to a coarse quotient.

## 3. Denominator clearing and projective count rays are elementary prior mathematics

Any finite rational probability vector can be multiplied by a common denominator to obtain a non-negative integer count vector. Dividing all counts by their gcd gives a unique primitive count representative of the same rational ray. Conversely every nonzero count vector defines a rational normalized distribution.

R004 therefore does not claim denominator clearing, homogeneous/projective count coordinates, cross multiplication, or determinant comparison of ratios as novel.

The project-specific choice is architectural: rational normalization is demoted to an **external view**, while integer counts and signed cross defects become the native finite state used by the current toys.

## 4. Bell/CHSH and convex separation are prior mathematics

Bell and CHSH theory, including local deterministic response tables and linear inequality certificates, are established prior work already mapped in the main R004 source corpus. Rewriting the same finite Bell target as an integer cone does not create a new Bell theorem.

R004 uses the elementary fact that if an integer linear functional is non-positive on every deterministic generator, it is non-positive on every non-negative integer combination of those generators. The selected target has a positive integer defect under one CHSH functional, yielding a denominator-free impossibility certificate. This is a representation choice and an application-specific certificate, not a novelty claim about convex duality or Bell polytopes.

## 5. Fraction-free exact linear algebra is established

Bareiss developed integer-preserving Gaussian elimination specifically to avoid unnecessary fraction growth in exact linear algebra [SRC-BAREISS-1968-FRACTION-FREE]. If Enterprise Math later needs larger exact linear constraint solvers, fraction-free/Bareiss-style elimination is therefore a natural **prior-art tool candidate**, not a new algorithmic invention.

R004 does not currently depend on Bareiss elimination for any theorem. The present Bell certificate is elementary enough to verify directly on sixteen generators.

## 6. Integer-valued polynomial/binomial coordinates are established

Integer-valued polynomial theory and binomial-coordinate methods are mature mathematics [SRC-CHABERT-2025-INTEGER-VALUED-POLYNOMIALS]. In particular, finite combinatorial counts written with binomial coefficients and finite differences are not Enterprise Math inventions.

R004's path crossover count

`Z(N,d)=binom(N-d+1,2)`

is therefore treated as elementary combinatorics. Its relevance is only that an apparently fractional macro share can be kept internally as an exact pair of integer counts and compared by cross multiplication.

## 7. R004-specific synthesis under test

The research-local proposal is the following layered interface:

`count ray -> integer defect functional -> exponent word -> operation-conditioned residue repair`.

Its intended semantics are:

- **count rays** for finite normalized/rational phenomena;
- **integer defects** for comparisons, Bell certificates, kill-test margins and monotonicity checks;
- **prime-exponent words** for multiplicative precision scales;
- **residue repair** only when a declared additive future language cannot descend through a valuation-only quotient.

The strongest new project-specific boundary is not a new p-adic theorem. It is the cross-surface conclusion that a valuation quotient can be extremely compact for multiplicative operations yet lose **all** compression under the universal additive-translation future language: at cap `K`, the future-safe closure has exactly `p^K` classes, equal to the full residue space modulo `p^K`.

That statement is an R004/P023/P024 specialization of established valuation and quotient mathematics. Historical novelty of the exact Enterprise Math packaging remains `NOVELTY_UNVERIFIED`.
