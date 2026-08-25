# Native filament odd-curvature deformation master theorem

Status: `FREE_RESEARCH_EXACT_PARAMETERIZED_THEOREM_FAMILY / POST_AUDIT_V2_NARROWED / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Post-audit authority: `NATIVE_FILAMENT_COUPLED_SELECTION_POST_AUDIT_V2_STATEMENT_FREEZE_20260825.md`.

This note deforms the native coefficient `3` to an arbitrary positive odd curvature coefficient `B`. The actual Enterprise filament is the specialization `B=3`; values `B!=3` are a mathematical deformation family and are not claimed to be native Enterprise geometry.

## 1. Global odd-curvature filament

Let

`eps(r)=r mod 2` in `{0,1}`,

and for odd positive integer `B` define

`F_B(H,r)=H+(B*r^2+eps(r))/2`.

The numerator is always even, so `F_B(H,r)` is integer-valued.

Fix a start shell `R`, put

`chi=(-1)^R`,

`c=F_B(H,R)`.

Then every translated window value is exactly

`V_j=F_B(H,R+j)`

`=c+B*R*j+(B*j^2+chi*eps(j))/2`.

Thus the native `B=3` packet sits inside the one-parameter family

`quadratic drift + one C2 parity mode`.

## 2. Curvature and universal recurrence

For every `j`,

`V_j-2*V_(j+1)+V_(j+2)=B-chi*(-1)^j`.

Hence the two local curvatures are

`B-1` and `B+1`.

After centering by `B`, the curvature mode alternates by sign.

The whole sequence satisfies the `B`-independent fourth-order recurrence

`V_(j+4)-2*V_(j+3)+2*V_(j+1)-V_j=0`,

with characteristic polynomial

`(lambda-1)^3(lambda+1)`.

## 3. Exact finite-quotient cardinality

For modulus `M>=2`, let `C_(k,B)(M)` be the set of length-`k` residue words obtained from all integer `(H,R)`, with `k>=3`.

A word depends on `R` only through

`chi=(-1)^R`

and

`b=B*R mod M`.

Let

`g=gcd(B,M)`

and

`L_(B,M)=lcm(2,M/g)`.

### M>2

After fixing the intercept, the exact/minimal effective `R` period is

`L_(B,M)`.

The first three coordinates recover the effective state, and

`|C_(k,B)(M)|=M*L_(B,M)`.

### M=2

After fixing the intercept, the exact/minimal effective `R` period is `1`.

There are exactly two words:

- if `B=3 mod4`, the two constant words;
- if `B=1 mod4`, the two alternating words.

Thus

`|C_(k,B)(2)|=2`.

The count is independent of `k` once `k>=3`.

If `M|N` and both moduli are above the exceptional `M=2` collapse, reduction is surjective with uniform fibers. For a new prime `q` with `q∤B*M`, the fiber multiplier is `q^2`.

## 4. Fixed-chirality affine MDS sheet

Let `q` be prime with

`q>max(2,k-1)`

and `q∤B`.

Fix chirality `chi`. Subtract the curvature offset

`eta_j^(B,chi)=(B*j^2+chi*eps(j))/2`.

Then

`W_j=V_j-eta_j^(B,chi)=a+b*j`.

Hence each fixed-chirality sheet is an affine translate of the `[k,2,k-1]` Reed--Solomon code.

## 5. Exact zero-line concurrence formulas

For divisibility by an odd prime `q`, the `j`-th coordinate defines

`L_j: a+b*j+eta_j^(B,chi)=0`.

### 5.1 Same-parity triples

If three distinct same-parity indices remain slope-distinct modulo `q`, their determinant is a nonzero Vandermonde factor times `B/2`. Therefore such a triple is concurrent modulo `q^a` iff

`q^a | B`.

### 5.2 Mixed-parity triples

Let `u,v` be the same-parity pair, let `w` have opposite parity, and put `e=eps(u)=eps(v)`.

The exact determinant is

`(u-v)/2 * [B*(w-u)*(w-v)+chi*(1-2*e)]`.

Therefore the displayed obstruction is an iff criterion modulo `q^a` provided

`q∤(u-v)`.

Equivalently, in a length-`k` window the stronger hypothesis

`q>k-1`

automatically supplies the distinct-slope/unit condition for every distinct index triple.

Without this condition the obstruction alone is not an iff criterion.

## 6. Chirality-dependent dual-parabola form

For `e in {0,1}` define

`Q_e^(chi)(x)=x^2/(2B)-chi*e/2`.

The zero line at index `j` is tangent at `x=-Bj` to

`Q_(eps(j))^(chi)`.

The older chirality-independent pair `Q_0,Q_1` is valid without modification only for `chi=+1`.

## 7. Union discriminant across both chiralities

In the inherited regime

`q` odd, `q∤B`, `q>k-1`,

same-parity triples are generic and the mixed-parity union discriminant is

`mathfrak D_(k,B)=product_T (B^2*A_T^2-1)`,

where `A_T=(w-u)*(w-v)`.

Then

`q` changes the mixed tangent-arrangement intersection type for at least one chirality

iff

`q | mathfrak D_(k,B)`.

For fixed chirality, the exact q-adic persistence depth is

`max_T v_q(B*A_T+chi*(1-2*e_T))`.

Do not identify the two-chirality union-discriminant valuation with a fixed-chirality depth.

If one extends outside `q∤B`, same-parity triples and small-`k` existence conditions must be handled separately.

## 8. Exceptional-prime cutoff away from divisors of B

For `k>=5`, the maximum possible absolute mixed-parity distance product is

`M_k=(k-1)(k-3)` for even `k`,

`M_k=(k-2)(k-4)` for odd `k`.

Every such product is odd. Since `B` is odd, every obstruction `B*A_T +-1` is even.

Therefore any odd exceptional prime `q` not dividing `B` satisfies

`q <= (B*M_k+1)/2`.

For the native specialization `B=3`, this recovers the terminal bound `q<=53` at `k=8,9`.

## 9. Transparency formula for arbitrary B

For odd prime `q>3`, call `H mod q` transparent if no shell value is divisible by `q`.

If `q|B`,

`T_B(q)=q-2`.

If `q∤B`,

`T_B(q)=[q-3 + Legendre(B/q)+Legendre(-B/q)]/4`.

Hence for every `q>=7`,

`T_B(q)>0`.

No prime `q>=7` is a universal single-channel breaker anywhere in this family.

## 10. Complete q=5 phase diagram

Modulo `5`:

- `B=0 mod5`: `T_B(5)=3`;
- `B=+-1 mod5`: `T_B(5)=1`;
- `B=+-2 mod5`: `T_B(5)=0`.

Therefore

`5 is a universal breaker`

iff

`Legendre(B/5)=-1`.

This includes `B=3`.

## 11. Exact breaker-coprime capacity in the q=5 breaker phase

Assume `Legendre(B/5)=-1`.

The sequence modulo `5` has period `10` in `r`. Every period contains a zero, so every consecutive run of values coprime to `5` has length at most `9`.

The bound is sharp exactly in the two normalized tangency classes

`H=0,2 mod5`.

Thus

`MAX CONSECUTIVE 5-COPRIME RUN LENGTH = 9`.

### Scope guard

This is a divisibility/nonzero-run capacity, not an unrestricted prime-run theorem for arbitrary integer `(H,R)`.

The actual native typed-Cell theorem `MAX GLOBAL PRIME-INCIDENCE ISLAND SIZE = 9` is a separate stronger result from the parent native branch, using native domain/incidence/seam structure in addition to the breaker calculation.

## 12. Finite-wheel dichotomy

For every prime `q>=7`, at least one transparent class exists. By CRT, any finite collection of individually nonbreaking channels has a simultaneous transparent transverse class.

Consequently, after the base `2/3` selection:

- if `Legendre(B/5)=-1`, channel `5` breaks every long filament with breaker-coprime capacity `9`;
- otherwise, no finite collection of prime channels `q>=5` can break every filament.

## 13. Native interpretation

The Enterprise filament has `B=3`. Therefore

`three-sector shell geometry -> B=3`,

`Legendre(3/5)=-1`,

`-> channel 5 is the unique breaker above3`,

`-> breaker-coprime run capacity 9`.

Separately, the full native typed-Cell incidence theorem proves an actual prime-incidence island cap of `9`.

So the constants `5` and `9` are coupled, but the divisibility-capacity theorem and the actual-prime-incidence theorem remain logically distinct.

## 14. Nonuniform p-adic depth outside the native specialization

The native `B=3`, `k<=9` exceptional channels all heal by the second residue layer because every relevant obstruction has q-adic valuation one.

This is not universal in the deformation family.

Example: `B=49`, `k=5`, `q=5`, negative chirality has a mixed obstruction of 5-adic valuation two. Direct enumeration gives nonzero defect mod `5` and mod `25`, but zero defect mod `125`.

## 15. Boundary

The finite-field method, affine/MDS code theory, quadratic-character sums, CRT and arithmetic-arrangement language are classical.

No external novelty claim is made for those ingredients.

The research candidate is the exact coupled deformation law

`odd curvature coefficient B`

`-> quotient-code period`

`-> explicit arrangement discriminant / p-adic depth`

`-> Legendre(B/5) connectivity phase`

`-> sharp breaker-coprime 9-cap in the nonresidue phase`.

External novelty remains unresolved pending a separate independent literature review.
