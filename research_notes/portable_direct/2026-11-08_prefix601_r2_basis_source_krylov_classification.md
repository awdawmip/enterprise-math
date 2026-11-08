# PREFIX-601-R2 — Complete 48-phase basis-source Krylov classification on native zero-weight BRC boundary

2026-11-08. Frozen original native X6-BRC science `f42f2906d77f24085c123f3ccfe9667d41caa96d`: 48 native phases, 96 bit-ports, 576 typed actions; current positive 48-tail `Q(z)=Q(0,z)` with axis weights `(1,1,1,1,0,0)`. Reuses PREFIX-599 and the uniform source of PREFIX-600. All statements below refer to the **48-dimensional post-first-step phase right-source basis vectors**, not arbitrary original bit-port inputs. No P000 changes.

## Exact result

For **every real z>=0**, let `e_j` be the j-th unit vector in the existing zero-based native 48-phase ordering and let `mu_j(t,z)` be the monic minimal polynomial annihilating `e_j` under `Q(z)`. The entire 48-vector basis partitions into five exact types:

| Type | Phase indices j | Sharp polynomial for z>=0, z!=1 | At z=1 |
| --- | --- | --- | --- |
| Zero | 1,3,5,7,13,15,17,19,25,27,29,31,37,39,41,43 | `t` (degree 1) | same |
| Base five | 0,2,6,12,16,18,24,28,30,36,38,42 | `t(t^4-16)` (degree 5) | same |
| Gated five | 4,14,26,40 | `t(t^4-(4z+12))` (degree 5) | `t(t^4-16)` |
| Base six | 9,10,21,22,33,34,45,46 | `t^2(t^4-16)` (degree 6) | same |
| Full ten | 8,11,20,23,32,35,44,47 | `t^2(t^4-16)(t^4-(4z+12))` (degree 10) | `t^2(t^4-16)` (degree 6) |

Thus for **z>=0,z!=1** there are exactly **16 degree-1, 16 degree-5, 8 degree-6 and 8 degree-10** phase basis sources. At **z=1** there are 16 degree-1, 16 degree-5 and 16 degree-6 basis sources.

## Proof: complete symbolic identity and minor certificates

Rebuild `Q(z)` from the original STAR triple phases and target `g=4`, following PREFIX-599's original native successor semantics. Form exact matrices `Q^k`, 0<=k<=10, over `Z[z]`. For **each of the 48 columns** in the table, compare all 48 coefficients of the associated polynomial matrix against zero: `Qe_j` for Zero, `(Q^5-16Q)e_j` for Base five, `(Q^5-(4z+12)Q)e_j` for Gated five, `(Q^6-16Q^2)e_j` for Base six and `(Q^10-(4z+28)Q^6+16(4z+12)Q^2)e_j` for Full ten. All 2304 checks in the finite complete 48-column classification hold identically. At `z=1`, check the stronger six-order identity for each Full ten column.

For sharpness, form Krylov matrix `K_j(d)=[e_j,Qe_j,...,Q^{d-1}e_j]`, of size 48xd, with d the claimed degree. For each of the 48 indices, select a d-row submatrix using exact pivot rows at z=0, then calculate its determinant **symbolically over Z[z]**. Every selected determinant is a nonzero integer times `(z+3)^a` for all classes except Full ten; those eight determinants are nonzero integers times `(z-1)^4(z+3)^b`. Exponents a,b are nonnegative integers and the checker stores the exact pivot rows and determinant for **each** j. Consequently all 48 selected minors are nonzero for all nonnegative real z except the explicitly treated z=1 Full-ten class. At z=1, separate exact six-column Krylov minors are nonzero for all eight affected inputs, with determinants among ±16384 and ±32768. Hence no smaller polynomial degree is possible for any individual basis source.

Representative exact lower minors (all other input minors explicitly provided in results JSON):

```
j=0  degree5:       +1024
j=4  gated degree5: -64*(z+3)^4
j=9  degree6:       -65536
j=8  degree10:      -34359738368*(z-1)^4*(z+3).
```

This verifies a complete finite basis domain and a universal real nonnegative gate parameter through algebraic factorization, rather than sampling gate values. The standalone `PREFIX601_R2_native_phase_basis_krylov_checker.py` reproduces the whole computation; its machine-readable output `PREFIX601_R2_native_phase_basis_krylov_results.json` contains all 48 basis certificates.

## Reuse and next question

For stationary z and a single phase-source e_j, calculate `t^n mod mu_j(t,z)` to jump exactly n steps, then linearly combine a maximum of 1/5/6/10 Krylov vectors. Phase identity matters: the four gated five-degree cases are not identical to the twelve ungated five-degree cases. A general nonnegative source that mixes phase types may need the least common multiple of the respective polynomials; proven per-source order does not automatically imply the same order for arbitrary mixtures.

Next: characterize mixed-input minimal Krylov orders and the exact injective/quotient interface from the native 96-port first-step input to the 48-phase tail, preserving typed gate source and all requested observations. Benchmark input, polynomial jump and output bit cost for the resulting admissible query families.

Evidence status: exact author-side proof and local SymPy checker executed successfully; independent Driver mathematical review, formal Native Result and canonical mathematical promotion pending. Research activity `RA-79CF6AC40EFDC108B48AC3A7` registered; no formal CLAIM.
