# PREFIX-602-R2 — Common exact 16-dimensional native BRC tail under nonstationary gate parameters

2026-11-08. Author-side exact proof and executed verification; independent Driver review / canonical admission pending. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continuation of PREFIX-596 (96-port → positive 48-phase bridge), PREFIX-599 (zero-weight spectrum), PREFIX-601 (single-phase Krylov classes). P000 and ACTIVE worldview unchanged.

## Source, population, declared observer

Use the original 48 X6-BRC STAR phases from triples `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`, 96 source bit ports, and 576 individually tagged native actions, including the three original marked-gate branches. Work in the already-proved PREFIX-596 48-phase nonnegative tail with frozen six-axis weights `(1,1,1,1,0,0)`. The marked phase is `g=4` (zero-based), with original successors `N(i)`.

For `j in N(i)`, the tail matrix `Q(z)` has entry 0 when the row axis is 5 or 6, entry 1 at the marked row `i=g`, entry `3+z` when `j=g` and `i!=g`, and entry 2 otherwise. All other entries vanish. The scientific BRC positive regime has `z>=0`, changing arbitrarily between steps. The 16-state matrices below are *signed observable coordinates* for **all 48 phase outputs**, not a positive BRC replacement or a preservation theorem for individual historical path labels. The original source carrier retains the provenance.

## Theorem — fixed common 16-dimensional invariant subspace and two-step stabilization

Set `A=Q(1)`, `G=Q(2)-Q(1)` and `V=im(A^2)⊂Q^48`. Then `Q(z)=A+(z-1)G`, `rank(A^2)=16`, `rank(G)=1`, and `G^2=0`.

For every real `z`, `Q(z)V⊆V`. For every real `a,b`, `im(Q(a)Q(b))⊆V`. If `a,b!=-3`, `rank(Q(a)Q(b))=16`, hence its image **equals V**.

Consequently, for any nonnegative (nonstationary) gate sequence `z_1,...,z_n`, `n>=2`:
```text
im(Q(z_n)...Q(z_1)) = V
rank(Q(z_n)...Q(z_1)) = 16.
```
The common 16D image is independent of the gate sequence. The restricted map `Q(z)|_V` is invertible for all nonnegative z, so rank never drops further. Dimension 16 is therefore the exact minimum for any linear internal state that recovers the **entire 48-dimensional phase vector** for all initial phase vectors at/after the second transition. No claim is made about complete historical branch provenance or unrestricted six-axis weights.

## Constructive fixed encoder, 16-state dynamics, and full phase recovery

Use original zero-based ordering. Form `E` by taking columns
```text
C=[0,2,4,6,8,9,10,11,12,14,21,23,28,30,32,34]
```
of `A²`; its 16 columns are independent. Select output rows
```text
R=[0,1,2,3,4,5,6,7,16,17,18,19,24,25,26,27].
```
The 16×16 submatrix `E_R` is invertible. Define `K=E_R^{-1}P_R` (with `P_R` selecting rows R) and `T(z)=KQ(z)E`. Exact matrix identities give
```text
K E=I_16,      Q(z) E=E T(z).
```
For any original phase input `y_0`, after **two** transitions encode `w_2=KQ(z_2)Q(z_1)y_0`; then
```text
w_(n+1)=T(z_(n+1))w_n,   y_n=Ew_n,   n>=2.
```
This reconstructs all 48 phase coordinates exactly, including under nonstationary gates. The old PREFIX-596 96-port observation bridge remains necessary when individual native bit-port outputs are requested. `E` has 72 nonzero integer entries, `K` has 36 nonzero rational entries, and `T(z)` has 36 nonzero symbolic entries versus 96 nonzero positions of `Q(z)` at the stated positive gate/axis parameters. **T and K have negative coefficients.** These are signed linear coordinates, not a certified positive carrier and not an end-to-end speedup result.

On V the characteristic polynomial is
```text
det(t I_16 - T(z)) = (t^4 - 16)^3 (t^4 - 4z - 12).
det T(z) = 2^14 (z+3).
```
This is compatible with PREFIX-599's previously established `det(tI_48-Q(z))=t^32(t^4-16)^3(t^4-4z-12)` and identifies exactly the 16D nonzero spectral part.

## Exact proof and all-parameter certificate

1. Rebuild the 48 STAR successors and gate, form exact integer matrices `A,G`. Determine 16 independent columns of `A²` and 16 pivot rows. For the six full matrices `M∈{A²,AG,GA,G²,AE,GE}`, the supplied checker confirms **exactly** `E(KM)=M`, not merely special-value rank samples. Consequently `Q(z)E=ET(z)` for every real z, and `V` is common invariant.
2. Since `G²=0`, `Q(a)Q(b)=A²+(b-1)AG+(a-1)GA`. All three terms have image inside V, proving the two-step rank upper bound 16 universally.
3. Let `D(a,b)=det((Q(a)Q(b))[R,C])`. As `AG,GA` have rank one, D is degree ≤1 in **each** of a and b. Four exact integer values are `D(0,0)=-9·2^28`, `D(0,1)=D(1,0)=-12·2^28`, `D(1,1)=-16·2^28`. Bilinear interpolation proves `D(a,b)=-2^28(a+3)(b+3)` for **all real** a,b. This supplies the nonzero rank-16 minor for all nonnegative gate pairs.
4. `T(z)=T(1)+(z-1)H` with `H=KGE` rank one; its characteristic polynomial is affine in z. Full exact 16×16 characteristic polynomials at `z=0,1` match the displayed expression and imply it for **all** z. Its determinant is `2^14(z+3)` and is nonzero in the native nonnegative domain. Thus all later gates act invertibly on V, proving rank 16 for every product length ≥2.
5. The independent checker also compares **612 complete 48-phase outputs** for 51 integer initial phase vectors, 3 gate sequences of 6 nonstationary steps and all 4 post-transient steps, using exact SymPy arithmetic. Finite checks are regression evidence; the universal theorem follows from the algebraic rank-one and interpolation argument.

## Limitations, reuse, next question

`REUSE_APPLIED`: frozen original typed BRC phase-successor interface and the exact PREFIX-596 port bridge. `COMPOSE_APPLIED`: PREFIX-599 spectral result. `EXTEND_EXISTING_TOOL`: PREFIX-601 initial-vector recurrence machinery. No classical π, trigonometric, Taylor/Padé/Cayley or matrix-exponential computations. Positive provenance and native path-history observers are retained by the original carrier; only the declared 48-phase future linear observer factors through the new 16D coordinate.

Next: test whether `V∩R_{≥0}^{48}` admits a common nonnegative 16-state generating cone for every `z>=0`, or prove a precise obstruction; benchmark input conversion, signed intermediate bit lengths, 16-state core, and full 96-port output recovery against the optimized 48-state/96-port code. Preserve the positive and path-labelled original carrier until a provenance-safe equivalence certificate exists.

Evidence: `PREFIX602_R2_stable16_native_BRC_checker.py` (standalone executable exact reconstruction, fixed pivot selection, all-parameter matrix checks and 612 regressions), `PREFIX602_R2_stable16_native_BRC_results.json` (actual executed certificate). This is author-side research publication only; no native CLAIM, Result, Driver review, Foundation admission or deployment is inferred.