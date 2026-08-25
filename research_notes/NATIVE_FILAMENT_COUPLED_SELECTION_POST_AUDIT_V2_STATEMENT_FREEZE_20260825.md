# Native filament coupled-selection theorem — post-audit V2 statement freeze

Status: `FREE_RESEARCH_INDEPENDENTLY_VERIFIED_WITH_NARROWING / V2_STATEMENT_AUTHORITY / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Independent audit: PR `#631`, return `research_returns/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_RETURN_20260825.md`, frozen verdict `PACKAGE_VERIFIED_WITH_NARROWING`.

This file is the authoritative statement layer for PR #627 after the independent blind audit. Where older #627 notes conflict with this file on C1, D1, D2, or the meaning of the sharp value `9`, this file controls.

## 1. Audit outcome

The blind audit independently reconstructed proofs/checks without reading PR #627 source proofs or package-specific checkers before freezing its return.

Rows A1--I all survived. Three rows require explicit narrowing:

- `C1`: special effective-period behavior at `M=2`;
- `D1`: chirality-dependent vertical shift in the dual-parabola formulation;
- `D2`: distinct-slope / q-adic-unit condition for the mixed-parity concurrence iff.

No row has `DEPENDENCY_GAP`. No row remains refuted after the narrowings below.

## 2. V2 finite-quotient statement

For positive odd `B` and `k>=3`, let

`F_B(H,r)=H+(B r^2+eps(r))/2`,

and let `C_(k,B)(M)` be the set of length-k residue words modulo `M` obtained from integer `(H,R)`.

Put

`L_(B,M)=lcm(2,M/gcd(B,M))`.

### M>2

After fixing the intercept, the exact/minimal effective `R` period is

`L_(B,M)`.

The exact code cardinality is

`|C_(k,B)(M)| = M L_(B,M)`.

### M=2

After fixing the intercept, the exact/minimal effective `R` period is

`1`, not `2`.

The total code cardinality remains

`|C_(k,B)(2)|=2`.

Thus the cardinality theorem survives unchanged; only the unqualified effective-period statement is narrowed.

## 3. V2 curvature and fixed-chirality affine sheet

For start shell `R`, put `chi=(-1)^R`, `c=F_B(H,R)` and `V_j=F_B(H,R+j)`.

Then

`V_j=c+B R j+(B j^2+chi eps(j))/2`.

The alternating second difference is

`V_j-2V_(j+1)+V_(j+2)=B-chi(-1)^j`,

and every trajectory satisfies

`V_(j+4)-2V_(j+3)+2V_(j+1)-V_j=0`.

For prime `q>max(2,k-1)` with `q∤B`, each fixed-chirality sheet becomes, after subtracting the curvature offset, the affine evaluation family

`(a+bj)_(j=0,...,k-1)`,

hence an affine `[k,2,k-1]` Reed--Solomon/MDS coset. The code classification is classical; the geometry-selected integer lock is the research-specific input.

## 4. V2 dual-parabola formulation

For `e in {0,1}` and chirality `chi`, define

`Q_e^(chi)(x)=x^2/(2B)-chi e/2`.

The zero line at index `j`,

`L_j: y=-j x-(B j^2+chi eps(j))/2`,

is the tangent at `x=-Bj` to

`Q_(eps(j))^(chi)`.

This is the uniform two-chirality formulation. The older unshifted pair `Q_0,Q_1` is valid without modification only on the `chi=+1` sheet.

## 5. V2 concurrence obstruction

Let `u,v` be same-parity indices with common parity `e`, and let `w` have the opposite parity.

The exact determinant is a unit scalar multiple of

`B(w-u)(w-v)+chi(1-2e)`

provided the same-parity slope difference is a q-adic unit.

Therefore the iff statement modulo `q^a` is:

if `q∤(u-v)`, then

`L_u,L_v,L_w` are concurrent modulo `q^a`

iff

`q^a | B(w-u)(w-v)+chi(1-2e)`.

For a length-k window, the stronger condition `q>k-1` automatically guarantees the required distinct-slope condition for all distinct indices.

Without this condition the obstruction alone is not an iff criterion; the blind audit produced an explicit `q=3` slope-collision counterexample.

## 6. V2 exceptional discriminant / depth

In the inherited regime `q` odd, `q∤B`, `q>k-1`, the two-chirality union discriminant remains exact:

`mathfrak D_(k,B)=product_T (B^2 A_T^2-1)`

up to inessential unit/sign conventions, where `A_T=(w-u)(w-v)` runs over mixed-parity triples.

Then

`q` changes the mixed tangent-arrangement intersection type for at least one chirality

iff

`q | mathfrak D_(k,B)`.

For fixed chirality, the q-adic persistence depth is the maximum valuation of the corresponding fixed-chirality obstruction

`B A_T+chi(1-2e_T)`.

Do not identify the two-chirality union discriminant valuation with a fixed-chirality persistence depth.

If one extends the theorem to `q|B`, same-parity triples and small-k existence conditions must be handled separately; this is outside the inherited D3 statement.

## 7. Breaker theorem survives exactly

For odd prime `q` define `tau_B(q)` as the number of transverse classes `H mod q` for which no shell value is divisible by `q`.

The exact formulas remain:

- if `q|B`, `tau_B(q)=q-2`;
- if `q∤B`,
  `tau_B(q)=[q-3+(B/q)+(-B/q)]/4`.

At `q=2`:

- `B=1 mod4` gives a breaker;
- `B=3 mod4` leaves one transparent class.

Hence universal breaker primes are contained in `{2,3,5}` and no `q>=7` is a universal breaker.

The first-breaker phase modulo 60 remains exact.

## 8. Exact meaning of the sharp capacities 1,5,9

For a universal breaker `q in {2,3,5}`, the breaker-coprime shell pattern has period `2q` and at least one killed residue in every period. The exact maximal consecutive breaker-coprime run capacities are

- breaker `2` -> `1`;
- breaker `3` -> `5`;
- breaker `5` -> `9`.

For breaker `5`, the extremal normalized transverse classes are exactly

`H=0,2 mod5`.

### Scope guard

These are **divisibility / breaker-coprime capacities**. They are not, by themselves, unconditional prime-run caps for the unrestricted integer family `F_B(H,r)`.

For example, the blind audit notes that allowing the breaker value itself and leaving the native shell domain can produce longer prime runs.

The actual native typed-Cell theorem

`MAX GLOBAL PRIME-INCIDENCE ISLAND SIZE = 9`

is a separate stronger theorem already established on the native `s=B=3` carrier using the full incidence/seam/domain analysis in the parent research branch. It is compatible with, but not deduced solely from, the breaker-coprime capacity statement.

## 9. Sector-count provenance survives

For the abstract odd-sector shell allocator with admissible side position,

`B=s`

exactly on the central filament.

For even sector count, the reflected central seam pair differs by `2h+1`, so two nonexceptional odd primes cannot occupy that reflected pair simultaneously.

For the native tri-sector specialization:

`sector count = mean filament curvature = normalized seven-Cell Poisson source = 3`.

Then `B=3` avoids breaker channels `2` and `3`, while `(3/5)=-1`, so the first universal breaker is `5` and the breaker-coprime capacity is `9`.

Among positive odd sector counts with a finite universal breaker, `s=3` is the smallest sector count attaining the latest possible finite first breaker `5`.

## 10. High-dimensional transparent-basin rows survive

The CRT product, extinction dimensions, fixed-B asymptotic, and profinite survivor statements were all independently verified at their stated strength, provided the primorial ultrametric is explicitly defined as in the audit return.

For no-break classes, every finite prime subsystem is integer-satisfiable; the all-prime compatible product exists profinitely; the diagonal ordinary-integer intersection is empty.

## 11. Control witness survives

The `B=15` twelve-value prime witness was independently regenerated and independently verified prime with a deterministic 64-bit Miller--Rabin basis.

Thus the native sharp-nine phenomenon is not a universal property of all quadratic-plus-parity filament families.

## 12. Prior-art / novelty status

The independent audit verifies statement strength, not external novelty.

Continue to treat as classical / non-novel ingredients:

- characteristic quasi-polynomials / arithmetic arrangement counting;
- coefficient monotonicity;
- Reed--Solomon/MDS theory;
- CRT;
- quadratic character sums / order-2 cyclotomy;
- Legendre transform and conic duality;
- standard product/profinite/Hausdorff methods.

The only external novelty candidate remains the exact coupled pipeline selected by the native geometry:

`sector allocation -> curvature scalar -> integer quotient code -> dual-parabola tangent/value geometry -> breaker/exception phase -> high-dimensional extinction-vs-survival`.

External novelty remains `UNRESOLVED` pending a separate independent literature audit.

## 13. Frozen verdict

`COUPLED_SELECTION_V2_STATEMENTS = INDEPENDENTLY_VERIFIED_WITH_NARROWING`.

`N1: M=2 EFFECTIVE PERIOD = 1`.

`N2: DUAL PARABOLA SHIFT IS CHIRALITY-DEPENDENT`.

`N3: MIXED CONCURRENCE IFF REQUIRES DISTINCT-SLOPE / UNIT CONDITION`.

`H: 9 IS BREAKER-COPRIME CAPACITY; NATIVE PRIME-INCIDENCE CAP9 REQUIRES THE SEPARATE GLOBAL NATIVE THEOREM`.
