# PREFIX-276: Toeplitz extension disks and infinite rational C4-source witnesses for future-sensitive BRC observations

**Status:** Author-side exact mathematical derivation and independent finite rational C4 path-pair checks. Not a verified native heartbeat evolution, formal Result, Stage46 source-import test, or independent Driver review.

## Typed question

For an explicit Stage50 complete-history finite source packet `f=Σ a_j|jqC>`, put `Z=Σ|a_j|²`, `c_r=Σ conj(a_{j+r})a_j/Z`, `c_{-r}=conj(c_r)`, `c_0=1`. Its documented two-input C4 detector reads `p_external(r,p)=5/18*(1-Re(i^p c_r))`. Here `j` indexes source/history loads; neither loop degree nor `r` is physical heartbeat time. The native X6+time/P000 scope is unchanged.

**Theorem (one-step formal Gram completion).** Let `H>=1`, and suppose the Toeplitz Hermitian matrix `T_H=(c_{j-i})_{0<=i,j<=H}` is positive definite. Write `J={1,...,H}`, `B=T_{H+1}[J,J]`, `u=T_{H+1}[J,0]`, `v=T_{H+1}[J,H+1]`; all three are determined by `c_0,...,c_H`. Define `z*=u* B^{-1}v` and `rho=1-u*B^{-1}u>0`. Then the extended Toeplitz matrix `T_{H+1}` is positive semidefinite precisely for `|c_{H+1}-z*|<=rho`. The proof takes the Schur complement of `B`: the remaining 2-by-2 matrix has offdiagonal `c_{H+1}-z*`, and its two equal diagonal entries are `rho`. Equality of the diagonals follows because both adjacent `(H+1)`-square principal blocks equal `T_H`. The 2-by-2 PSD criterion completes the proof. This is a finite Gram extension theorem, not a statement that every disk point has a prescribed finite-packet physical realization. Singular `T_H` requires a separate generalized Schur complement.

At `H=1`, the disk is `|c_2-c_1²|<=1-|c_1|²`. For `c_1=i/2`, its center is `-1/4`, radius `3/4`; hence `-1<=Re(c_2)<=1/2` and the declared C4 readout obeys `5/36<=p_external(2,0)<=5/9` at the formal PSD-extension level.

**Concrete future-sensitive counterexample.** Take unnormalized C4 packets `f_A=|0>-i|1>` (`Z_A=2`) and `f_B=2|0>-i|1>-|2>` (`Z_B=6`). Exact ordered-pair character sums yield `c_1(A)=c_1(B)=i/2`, `c_2(A)=0`, `c_2(B)=-1/3`. All four `r=1` detector values coincide: `(5/18,5/12,5/18,5/36)`. At `r=2`, packet A has four values `(5/18,5/18,5/18,5/18)`, whereas B has `(10/27,5/18,5/27,5/18)`. These are distinct preparations, not identical complete native states. Both moment triples satisfy the disk and give strictly positive Toeplitz determinants `1/2` and `5/9`.

**Infinite rational family.** For each rational `t`, let `a=2/(1+t²)`, `b=-(t-1)²/(1+t²)` and `f_t=a|0>-i|1>+b|2>`. The rational-circle identity `(a-1)²+(b+1)²=1` gives `Z=a²+1+b²=2(a-b)`. Consequently `c_1(f_t)=i/2` for every `t`, whereas `c_2(f_t)=-(t-1)²/[(1+t²)(t²-2t+3)]`. This rational function is nonconstant, hence takes infinitely many values on the rationals. Explicit finite C4 packets thus retain infinitely many distinct future signatures invisible to all four `r=1` settings.

## Verification and source scope

`verify_prefix276.py` encodes each load with positive rational amplitude and an independent phase label modulo 4; all relevant ordered source pairs are multiplied before character summation and normalization. Exactly 89 distinct rational parameter values and their `r=0,1,2`, `p=0..3` external readouts were checked; the A/B witnesses, completion-disk certificates, and 11 distinct `t=1/n` next moments passed. All arithmetic is exact fractions/Gaussian rationals, no floating point, trig, ordinary propagator, or claimed native `H_n` step. The original Stage46 package import remains unperformed.

Source: `awdawmip/enterprise-math@dd2b53a45433d9662f9e37af7a2d828926da3d00:research_notes/HEARTBEAT50_INTERFERENCE_KERNEL_20260923_6DD798.md` (Git blob `0f4ec78225cfc799a267ca6b96d9f994422f8ad2`). The core `src/enterprise_math/brc_weighted_recurrent.py` handles positive total mass and cannot substitute for C4 path-pair interference. `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` records `fixed_heartbeat_program=null`; its separate heartbeat-instant companion requires but does not specify a native `model_law_id` update.

Classical provenance: Toeplitz positive-definite extension and Schur prediction theory predate this note; see NIST DLMF §18.33 and I. Gohberg, I. Koltracht, D. Xiao, *SIAM J. Matrix Anal. Appl.* 15 (1994), 1290–1309, DOI 10.1137/0615087. This note claims a new **project-scoped BRC application and finite rational witness family**, not invention of the Schur complement or classical moment theory.

Next: locate a native-legal `r=2` controller and Stage46 import with source, Cell/Port, field, boundary, history and independent time correspondence; obtain an actual native stdout certificate or formally delimit the missing bridge. Preserve `NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION` and `NOT_ADMITTED` until verified.
