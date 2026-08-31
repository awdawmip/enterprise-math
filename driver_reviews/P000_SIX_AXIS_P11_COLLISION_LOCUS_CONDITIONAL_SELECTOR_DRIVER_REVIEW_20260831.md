# Driver Review — P000 six-axis P11 collision locus and conditional selector

Driver-ID: `EM-DVR-WLE3X6`

Result: `RR-C3E71A9D4B6052F88E21`  
Publication: `TP2-3DEA87F0F4ED366BEE03`  
Disposition: `REQUEST_REVISION / MATHEMATICAL_SCOPE_CORRECTION / PAIRABILITY_FILTER_MISSING`  
Destination: `FOLLOWUP_TASK / RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR / TP2-E899F20BC1B62973D07C`

## Verdict

Return the immutable Result for mathematical revision under the **same stable Task-ID**.

The Researcher correctly classifies the **combinatorial** `S3` equal-`P11` assignment pairs and correctly derives the Gram/Vandermonde quadratic resolvents, but the hard target asks for the exact two-orbit **admissible** `K/Gamma` fibre under the frozen integer-pairability gate. The submitted theorem equates the algebraic collision locus `C1 union C2` with the admissible two-state locus without filtering the alternate colliding assignment through pairability. That implication is false.

The revision is narrow. Preserve all validated algebraic collision/resolvent work, but replace the terminal one-bit law by the pairability-filtered law and add an exact regression for the missing case.

## Valid payload retained

1. On fully distinct sorted marginals with positive gaps
   `A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`,
   the only **combinatorial** equal-`P11` assignment pairs are:
   - `C1: AC=BD`, pair `132/213`;
   - `C2: AD=BC`, pair `231/312`.
2. Repeated-`H` or repeated-`T` strata are combinatorially `P11`-injective on distinct alignment orbits.
3. Simultaneous `C1+C2` forces `A=B` and `C=D`; the two combinatorial double levels remain distinct, so a three-state combinatorial fibre is impossible.
4. The submitted symmetric Gram/Vandermonde formulas are valid quadratics satisfied by every algebraic candidate `P21` and, dually, `P12` value. On a genuine two-admissible-orbit fibre they give exactly the two second-moment values.
5. The `P21/P12` numeric-root ordering relation is correctly `SAME` on `C1` and `OPPOSITE` on `C2` when both branches are admissible.
6. The pairable positive witnesses first occurring at root-box `B=6` for `C1` and `C2`, and their homogeneous scaling families, were independently reproduced.
7. Output scope is exact: five CLAIM-authorized files only; manifest Git blob SHA-1 pins match the fetched Return, checker, certificate and execution record.
8. Prior-mathematics attribution and all P000/Pfaffian/native-orientation firewalls are acceptable.

## Decisive falsifier

Use valid marginals

`H={-2,0,2}`, `T={-1,0,1}`.

They have

`A=B=2`, `C=D=1`,

so **both** submitted algebraic collision equations hold.

### Upper combinatorial double level: `P11=2`

The submitted `C1` pair is `132/213`.

`213` gives

`K_213={(-2,0),(0,-1),(2,1)}`,

with integer root pairs

`{-2,0}`, `{-1,1}`, `{1,1}`,

so it is admissible.

`132` gives

`K_132={(-2,-1),(0,1),(2,0)}`.

Here `(-2,-1)` has discriminant `8`, not a square, and `(0,1)` has negative discriminant. Hence the alternate colliding alignment is **not** admissible.

Therefore the admissible fibre at `P11=2` has size `1`, not `2`.

### Lower combinatorial double level: `P11=-2`

The submitted `C2` pair is `231/312`.

`312` gives

`K_312={(-2,1),(0,-1),(2,0)}`,

with integer root pairs

`{-1,-1}`, `{-1,1}`, `{0,2}`,

so it is admissible.

`231` gives

`K_231={(-2,0),(0,1),(2,-1)}`,

and is not admissible because `(0,1)` has negative discriminant and `(2,-1)` has discriminant `8`.

Therefore the admissible fibre at `P11=-2` also has size `1`.

This counterexample is entirely inside the frozen derived arithmetic interface and does not touch native orientation or Full-Cell semantics.

## Why the current checker misses it

The checker's core `fibres(H,T)` routine groups all six combinatorial matchings by `P11` and the main collision census asserts `has_double == bool(collision_classes(H,T))` **before applying the integer-pairability gate**. Pairability is used later only for positive root-box witnesses and scaling regression. Consequently the checker verifies the combinatorial collision theorem, not the taskbook's exact admissible-fibre theorem.

The current `0 bits off locus / 1 bit on locus` statement therefore overstates the side-information requirement on algebraic collision levels where only one colliding branch is pairable.

## Required revision

Generation 2 must freeze the distinction

`ALGEBRAIC_P11_COLLISION_LOCUS != ADMISSIBLE_TWO_ORBIT_LOCUS`.

At minimum it must:

1. retain `C1` and `C2` as the exact combinatorial equal-`P11` equations;
2. intersect each class with the frozen pairability gate for **both** colliding packets, giving a necessary-and-sufficient admissible two-orbit criterion;
3. express that criterion exactly, either as the six relevant discriminant-square/parity conditions or an equivalent simplified Diophantine form;
4. define the conditional selector from the **pairability-filtered** candidate set;
5. revise the information law to `log2 |admissible fibre(H,T,P11)|`: zero bits whenever only one admissible packet survives, including one-branch algebraic collisions, and one bit exactly when both colliding packets are admissible;
6. state the Gram/Vandermonde quadratic as an algebraic candidate resolvent and prove how pairability discards a nonadmissible root when only one branch survives;
7. add the `H={-2,0,2}`, `T={-1,0,1}`, `P11=+/-2` regression and a pairability-filtered exhaustive control;
8. preserve the validated `B=6` positive two-branch witnesses and same/opposite `P21/P12` branch relation on the genuine two-admissible-orbit locus;
9. create a fresh execution identity and **NEW Result-ID** under the superseding publication generation;
10. preserve all existing derived-only, Pfaffian-orientation, no-dimension-reduction, no-factorization and no-Full-Cell firewalls.

## Control consequence

The current Result is not rejected: most algebraic structure is retained. It is not accepted because its terminal theorem and checker identify the wrong locus for the taskbook's word `admissible` and therefore misstate the exact conditional information law.

Publish one Generation-2 revision under the same Task-ID. No native-orientation, signed-carrier, factorization, Full-Cell, or broader invariant-search successor is authorized.

Method harvest: `RESULT_ONLY`. No Working Truth, Foundation status, or canonical promotion is granted.
