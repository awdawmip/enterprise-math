# PREFIX-599-R2 — Exact minimal-polynomial classification at the zero-weight boundary

Date: 2026-11-08. Status: author-side exact proof and executed symbolic verification, independent Driver review pending.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Previous inputs: PREFIX-595/596 positive 48-tail construction, PREFIX-598U3 full `(w,z)` characteristic-polynomial theorem. P000 and ACTIVE worldview remain unchanged.

## Model

Retain native four STAR triples `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`, 48 phases, original 96 bit-ports and 576 labelled native actions including all three gated branches. The 48-dimensional post-first-step matrix is the existing exact native observation carrier, not a new spatial ontology.

Fix axis weights `(1,1,1,1,w,w)` at `w=0`; call the 48x48 tail matrix `A_z=Q(0,z)`. Its original native phase successor list is `N(i)`, gate target `g=4` (zero-based), and source row axis `a(i)`. For `j∈N(i)`,
- `Q_ij=x_{a(i)}` if `i=g`;
- `Q_ij=2*x_{a(i)}` if `i!=g,j!=g`;
- `Q_ig=(3+z)*x_{a(i)}` if `i!=g,g∈N(i)`.
All remaining entries vanish. For the positive native BRC carrier use `z>=0`; the algebraic statements below hold over all real `z`.

## Theorem: complete zero-weight boundary classification

For every real `z`,

```text
det(t I_48-A_z)=t^32*(t^4-16)^3*(t^4-4z-12).
```

The sharp minimal polynomial is

```text
  z =  1:  mu(t)=t^2*(t^4-16),                    degree 6
  z = -3:  mu(t)=t^5*(t^4-16),                    degree 9
  other z: mu(t)=t^2*(t^4-16)*(t^4-4z-12),       degree 10
```

Also `rank(A_z)=32` for `z != -3`, and `rank(A_{-3})=31`. For the native nonnegative gate `z>=0`, the complete classification is degree 6 at `z=1` and degree 10 at every other gate weight.

## Proof

**Characteristic polynomial.** All gate-dependent entries lie in a single target column, so the determinant is affine in `z`. Direct exact integer calculations at `z=0` and `z=1` give the displayed characteristic formula at both points. Two-node interpolation proves it for every `z`.

**Universal annihilator.** Construct `A_z` from the original 48 native phase successors. Multiplication over `Z[z]` yields the polynomial matrix identity

```text
A_z^10 - (4z+28)*A_z^6 + 16*(4z+12)*A_z^2 = 0,
```

equivalently `A_z^2*(A_z^4-16I)*(A_z^4-(4z+12)I)=0`. All 2304 entries expand identically to zero in the executed symbolic certificate.

**Rank and zero Jordan exponent.** Exactly 32 source rows can be nonzero. The 32×32 submatrix with zero-based indices

```text
rows=(0,1,2,3,4,5,6,7,12,13,14,15,16,17,18,19,
      24,25,26,27,28,29,30,31,36,37,38,39,40,41,42,43)
cols=(0,2,4,6,8,9,10,11,12,14,16,18,20,21,22,23,
      24,26,28,30,32,33,34,35,36,38,40,42,44,45,46,47)
```

has exact determinant `7044820107264*(z+3)`. Thus rank equals 32 for every `z!=-3`; at `z=-3` direct exact elimination gives rank 31. For `z!=-3`, zero has algebraic multiplicity 32 but geometric multiplicity 16. Its minimal-polynomial exponent is therefore at least two; the universal annihilator bounds it above by two.

**Generic gate.** When `z` differs from 1 and -3, the polynomials `t`, `t^4-16` and `t^4-4z-12` are pairwise coprime. The characteristic polynomial forces both quartics to occur in the minimal polynomial; the rank argument forces the double-zero factor. Hence the universal degree-ten annihilator is sharp.

**At z=1.** Exact matrix multiplication shows `A_1^2*(A_1^4-16I)=0`. The characteristic factors and the rank argument force all factors of this degree-six annihilator. Hence the sharp degree is six.

**At z=-3.** Exact multiplication shows `A_{-3}^5*(A_{-3}^4-16I)=0`, while the explicit nonzero entry

```text
[A_{-3}^4*(A_{-3}^4-16I)]_(4,8)=-128
```

forces zero exponent at least five. The characteristic polynomial forces the nonzero factor `t^4-16`. Hence the sharp degree is nine.

All steps use exact symbolic integer/rational arithmetic. The proposition is a matrix algebra theorem on the frozen native BRC observation carrier, not a claim of a physical time law.

## Evidence, use and next question

The executable `PREFIX599_R2_zero_weight_minpoly_checker.py` reconstructs the STAR graph, verifies both 48x48 characteristic polynomials, the full formal matrix identity, the stated 32x32 determinant, ranks, special annihilators, and the nonzero lower-bound witness. Its executed output is `PREFIX599_R2_zero_weight_minpoly_results.json`. All assertions pass.

Immediate use: at stationary zero two-class weight, exact tail jump `A_z^n v` reduces modulo a degree-six recurrence when `z=1`, and a degree-ten recurrence otherwise for nonnegative `z`. First-step encoding and full original 96-port output restoration remain governed by the previously established carrier interfaces. Next: extend collision classification in `(w,z)` with attention to the independently developed PREFIX-601 parity factorization, and measure complete endpoint/bit complexity.

No formal Task CLAIM, native Result, independent review or theorem promotion was made here.
