# BRC GCD Divisor-Lattice Quotient for Activation Blocks

Status: `RESEARCH FRONTIER / EXACT OPERATION-SAFE QUOTIENT + STATE-COMPRESSION POSITIVE RESULT + COMPUTATION-COMPRESSION GAP / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_ORDERING_ACTIVATION_WALL_RANDOM_ACCESS_FRONTIER_20260908.md`
Source snapshot before write: `main@5e14c45f46f91343f77e650f1beaee35516bdaf5`

## 0. Question

The parent frontier reduced boundary ordering to a factor-scale activation query and showed that generic random access lands on the classical square-root block-product frontier. The remaining BRC-specific question is whether the full modular block value is unnecessarily rich and can be replaced by a smaller state that still composes under giant jumps.

For this declared future operation, only divisibility by the hidden prime factors matters. This note identifies the exact minimal-looking algebraic quotient carried by gcd support and separates representation compression from algorithmic evaluation.

---

## 1. Exact divisor-lattice homomorphism

Let `N` be squarefree and define

`Phi_N(X)=gcd(X,N)`.

The codomain is the divisor lattice `Div(N)`. For all integers `X,Y`,

`Phi_N(XY)=lcm(Phi_N(X), Phi_N(Y))`.

Proof is primewise. For each prime `r|N`,

`r | XY`

iff

`r|X or r|Y`.

Thus the prime support of `gcd(XY,N)` is the union of the prime supports of `gcd(X,N)` and `gcd(Y,N)`, which is exactly their lcm because `N` is squarefree.

Freeze:

`(Z, multiplication) -> (Div(N), lcm)`

is an exact operation-safe quotient for every future computation that only multiplies blocks and finally asks gcd support against squarefree `N`.

For a semiprime `N=pq`, the exact quotient has only four semantic states:

`{1,p,q,N}`.

This is a genuine BRC compression theorem: the full residue of an arbitrarily large product modulo `N` is unnecessary for multiplicative continuation followed only by gcd observation.

---

## 2. Boolean quotient is sufficient in the one-factor zone

Define the unit-status observer

`U_N(X)=1[gcd(X,N)=1]`.

For every modulus `N`, not only squarefree ones,

`U_N(XY)=U_N(X) AND U_N(Y)`.

Equivalently nonunit status composes by Boolean OR.

In a threshold interval known a priori to lie below `q`, at most the prime `p` can appear. Therefore the richer distinction between `p` and `q` is unnecessary until the moment a proper gcd is actually returned.

For a public integer interval `I=[L+1,U]` with `U<q`, define

`P_I=prod_(n in I) n`.

If prior evidence guarantees `L<p`, then

- `gcd(P_I,N)=1` iff `p>U`;
- `gcd(P_I,N)=p` iff `L<p<=U`.

Thus the factor-threshold problem has an exact **one-bit sufficient carrier** before success.

This is the sharpest observer compression found so far on the collision/activation route.

---

## 3. Why three anonymous states are not globally composition-safe

One might try to compress semiprime gcds to the unlabeled statuses

`UNIT / PROPER / TOTAL`.

This is not closed under multiplication in general. If two child blocks are both `PROPER`, their hidden proper factors may be the same, in which case the parent remains `PROPER`, or different (`p` versus `q`), in which case the parent becomes `TOTAL`.

Therefore outside a certified one-factor zone, branch identity/provenance of the proper divisor cannot be discarded. The exact four-state divisor lattice is the safe quotient; a three-state unlabeled quotient loses the equality relation required by future lcm composition.

This is a direct instance of the BRC provenance rule:

`PROPER_SUPPORT_WITHOUT_FACTOR_IDENTITY` is not operation-safe under later block multiplication.

---

## 4. PCF4R first wall reduces to a consecutive interval product

Recall

`A_s = C(2s,s)^2 * C(3s,s)`.

Let `r` be prime and suppose `s<r/2`. Then every factor occurring in `C(2s,s)` is below `r`, so that component is an `r`-unit. Also

`C(3s,s)=prod_(j=1)^s (2s+j)/j`.

The denominators `j` are below `r` and hence are units. Therefore in the first-wall range

`r/3 <= s < r/2`,

the `r`-activation is carried exactly by the numerator interval

`{2s+1, 2s+2, ..., 3s}`.

For a semiprime `N=pq` with `s<p/2`, both hidden primes exceed `2s`, so the whole gcd state satisfies

`gcd(A_s,N)
 = gcd(prod_(n=2s+1)^(3s) n, N)`.

Thus the PCF4R activation wall is, at its first relevant transition, exactly a consecutive-interval factor-support query. The hypergeometric wrapper supplies a clean N-only recurrence, but it does not change the underlying threshold-product semantics.

This explains why generic acceleration lands so naturally on Strassen/Bostan-Gaudry-Schost block products.

---

## 5. Exact BRC block carrier

For any finite interval/block `I`, define

`D_N(I)=gcd(prod_(n in I) n, N)`.

For disjoint blocks, and in fact for arbitrary finite multisets,

`D_N(I union J)=lcm(D_N(I),D_N(J))`

when multiplicity is interpreted through the product and `N` is squarefree.

So a hierarchical product tree has an exact BRC reinterpretation:

- leaves: labeled public factors `n`;
- serial composition: integer multiplication;
- quotient/recoalescence: prime support against `N`;
- parent state: lcm of child divisor states;
- terminal success: a proper divisor state.

The full product residue is an implementation lift, not the mathematically minimal state for the declared observer.

---

## 6. Positive result and immediate barrier

The state complexity problem is therefore solved extremely strongly:

- global semiprime block state: four exact divisor-lattice values;
- certified one-factor zone: one Boolean bit until the factor is exposed.

But this does **not** solve the computational problem. To construct `D_N(I)` from only the interval endpoints and `N`, one still needs a mechanism that detects whether a hidden prime divisor lies in the interval. Computing a modular block product followed by gcd is the classical batching mechanism; recursively composing already-known child divisor states requires enough child evaluations to locate the hidden jump and gives no automatic speedup.

Freeze:

`STATE_COMPRESSION != EVALUATION_COMPRESSION`.

`CONSTANT-SIZE_SUFFICIENT_CARRIER != CONSTANT-TIME_CONSTRUCTOR`.

This distinction is the principal new conclusion of this round.

---

## 7. Adaptive interval search and cross-scale reuse

Suppose prior threshold queries have certified

`L < p <= U < q`.

A midpoint test needs only the block

`I=(L,M]`, `M=floor((L+U)/2)`,

not a fresh prefix from `1` to `M`. If the block is unit, update `L=M`; if proper, the factor has already been returned.

Thus adaptive order search can reuse negative-range provenance and reduce each new test to the as-yet-unresolved interval. The interval lengths halve geometrically, so any black-box block evaluator costing approximately `H^alpha` on width `H` has total adaptive cost dominated by the first unresolved width.

For the classical square-root block frontier `alpha=1/2`, this remains `Theta(sqrt(U-L))` up to logarithmic/multiplication factors. Reuse removes redundant prefix work but does not change the exponent when the initial bracket has width `Theta(p)`.

A true BRC gain therefore requires either:

1. an initial N-only bracket for `p` of sublinear width `o(p)`; or
2. a block divisor-state constructor asymptotically below square-root-in-width; or
3. a cross-scale certificate whose composition shrinks the unresolved width faster than ordinary threshold bisection without paying equivalent block work.

Fixed-bit RSA Challenge construction priors only reduce the initial width by a constant factor and hence do not alter this exponent.

---

## 8. Minimality boundary relative to the observer

The divisor-lattice quotient is sufficient for multiplication + gcd support, but no claim of formal categorical minimality is made over all encodings.

Within the declared semantics, however, two distinctions are provably necessary:

- `UNIT` must remain distinct from any state containing a prime divisor;
- outside a one-factor zone, proper-`p` and proper-`q` support cannot be merged if later block multiplication is allowed, because their self- and cross-products have different parent states.

Hence the unlabeled `UNIT/PROPER/TOTAL` quotient is too coarse, while the labeled prime-support lattice is operation-safe.

In a certified `U<q` zone, the `q` branch is unreachable, so Boolean unit/nonunit is adequate until success. This is an observer-relative quotient lease; widening the future interval past `q` invalidates it.

---

## 9. Revised smallest unresolved unit

The collision / ordering / valuation-wall chain has now reduced to:

> Given `N=pq` and a public interval `I=(L,U]` known to contain at most the least factor, construct the one-bit/proper-gcd state
> `D_N(I)=gcd(prod_(n in I)n,N)`
> with asymptotic work below the generic square-root-in-`|I|` block frontier, without first factoring `N` by another method.

This is no longer an information-recovery problem. The exact sufficient state has been identified. It is a **constructor complexity** problem.

Kill conditions:

- storing only gcd/divisor state but computing it via an unchanged classical block product is representation-only progress;
- ordinary product trees, multipoint evaluation, BSGS, accumulating remainder trees, or generic fast recurrence must be treated as baselines, not renamed as new BRC algorithms;
- any proposed local quotient must be checked for operation-safe composition under the exact future interval schedule.

Next attack: search for an algebraic jump law for `D_N(I)` itself (or a richer but sub-square-root-size repair state) rather than for the full product residue. If every such jump requires a lift of square-root block width, close this route as a precise BRC interpretation of classical deterministic small-factor search.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.