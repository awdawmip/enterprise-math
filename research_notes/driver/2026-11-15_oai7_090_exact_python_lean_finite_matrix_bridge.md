# OAI7-090 — exact Python–Lean finite-matrix identity (source-level proof)

**Driver source/semantic audit, 2026-11-15** · Contributor: EM-DVR-DEBB5E (RESEARCH_DRIVER). External mathematical/software authorship belongs to `openai/math`. This is a **bounded algebraic comparison of the ideal real matrices** in the frozen external tree, not an execution receipt, a Lean formalization, a new Researcher CLAIM, or a native Result acceptance.

## Pinned inputs and the question

External frozen revision: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

- Python `preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`, blob `23768a5c2d88e100399bb5c4347447e86a7160cb`: `Pfull`, `PJ`, `makecol`, `M`, `Waves.loS`, `Ll`, and `approx`.
- Lean `lean/OAI/Analysis/Triangular/Basic.lean`, blob `0aa100fe19f4f25972904eed987233aa10f5199e`: `atomFactor`, `atomPolynomial`, `cAtomPolynomial`, `dAtomPolynomial`, `cShiftPolynomial`, `cCoefficient`, `dCoefficient`, `finiteColumn`, `jetMultiplier`, `jet`, `fullJetMatrix`, and `R`.
- Lean `lean/OAI/Analysis/Triangular/Certificate/AtomicMatrix.lean`, blob `df3cd4517bd13dd35943d5f55aeab284767b93b7`: `RValue := Construction.R` and `literalR_mem`.
- Lean `lean/OAI/Analysis/Triangular/Construction/FiniteAssembly.lean`, blob `bd83d7b12efd69e0a9854f028469bdb98aebefb0`: independent use of `R i j = jet H H ... (finiteColumn (j+2))`.

**Claim.** Replace the Python interval operations by their exact underlying real/complex operations and its interval `Pi` by exact `π`, preserving the code's column and row ordering. Let `A_exact` be the 20×20 real matrix obtained by evaluating `[row[2:] for row in Ll.loS(M)]`. Then for every `i,j : Fin 20`,

`A_exact[i,j] = OAI.AtomicTriangular.Construction.R i j`.

This is an equality of defined real matrices, not an assertion that the *computed interval object* is literally a real number or that its outward enclosure passed on this run.

## 1. Fourier coefficient identity — the missing normalization step

Put `κ=π/36`, `e_a=exp(iπ a/18)`, and let the 15-element residue inventory be

`S=(0,1,3,4,7,9,12,13,16,19,21,25,27,28,31)`.

Define the degree-30 polynomial

`F(z)=∏_{a∈S}(-e_a+2z-e_a^{-1}z²)=∑_{k=0}^{30}p_k z^k`,

and `P_j=p_{15+j}` for `j=0,...,15`. Python creates exactly these coefficients via `Pfull` and `PJ=Pfull[15:]`. Lean `atomFactor` and `atomPolynomial` give the same polynomial because `phase(a)=e_a` and `phase(-a)=e_a^{-1}`.

Fix `a∈S`; write `F_a=∏_{b≠a}(-e_b+2z-e_b^{-1}z²)`. Since `-e_a+2z-e_a^{-1}z²=-e_a^{-1}(z-e_a)²`, the Lean polynomial coefficients obey

`cShift_a(z) = 4κ² z F_a(z) = -4κ² e_a z F(z)/(z-e_a)²`

and

`dAtom_a(z) = iκ(e_a-e_a^{-1}z²)F_a(z) = iκ (z+e_a)F(z)/(z-e_a)`.

The rational expressions are **polynomial identities after clearing denominators**. For extracting their high coefficients, use the formal Laurent expansions at infinity (no analytic convergence assumption):

`e_a z/(z-e_a)²=∑_{r≥1}r e_a^r z^{-r}` and
`(z+e_a)/(z-e_a)=1+2∑_{r≥1}e_a^r z^{-r}`.

Consequently, for each `j=0,...,15`,

`cCoefficient(a,15+j) = -4κ²∑_{r=1}^{15-j} r e_a^r P_{j+r}`,

`dCoefficient(a,15+j) = iκ(P_j+2∑_{r=1}^{15-j} e_a^r P_{j+r})`.

These are **precisely** Python `makecol(j,a)`'s two entries before the `(2 if j else 1)` folding factor: Python's `yj=Pi/36` tends to `κ`, and `ph((l-j)*a)` is `e_a^{l-j}`.

Every polynomial factor `-e_a+2z-e_a^{-1}z²` is conjugate-reciprocal; so are `cShift_a` (with a zero at degrees 0 and 30) and `dAtom_a`. Therefore the coefficient at degree `15-j` is the conjugate of its degree-`15+j` coefficient. The full degree-`0,...,30` Fourier sum thus equals the positive-frequency sum with factor 2 at `j>0` and factor 1 at `j=0`, **after taking real parts**. This proves the Python `makecol` folding, not just a numerical resemblance.

## 2. Nodes, jets, and the 20×20 submatrix

Python sets `L=[0,1,3,4,7,9,12,13,16,19,21]`, `f=L[1:]`, and constructs 22 columns `M[j]=[makecol(j,n) for n in L]` (each node has a `c,d` pair). Lean's `finiteColumn col` uses exactly the same `cCoefficient,dCoefficient` pairs in the same order. The first two Python columns are the `n=0` pair.

Python `Ll=Waves(H,H)` with `H=27/50`. Its `loS(M)` loops over `n∈f` in this order, emitting the two rows
`-(1/Q(n)) Re Σ_t λ(H,t)e^{iπζ(H,H,t)n} M[t,*]` and
`(1/Q(n)) Re Σ_t λ(H,t)e^{iπζ(H,H,t)n}(D(n)-iπζ(H,H,t)) M[t,*]`.

Lean `jetMultiplier H H n d (frequency j)` is exactly these expressions: `d=0` multiplies by `-1`; `d=1` by `D(n)-iπζ`. Crucially, `t=(j-15)/18` varies **with every Fourier term**; it must not be replaced by a constant frequency.

The Python `Q(n)` and `D(n)` are also identical to Lean's exact `Q n`, `D n`: their positive-frequency sums give half the full even/odd wave-derivative real parts, hence Python's denominators `Q` and `3Q` match Lean's `Q` and `6Q` after conjugate pairing. The parameters `h=17/50`, `H=27/50`, `b=√3/2`, and `κ=π/36` coincide.

Finally Lean defines `fullJetMatrix(i,col)=jet (if col=22 then h else H) H (finiteNode(i/2)) (i%2) (finiteColumn col)`, and `Construction.R(i,j)=fullJetMatrix(i,j+2)`. Python `A=[row[2:] for row in Ll.loS(M)]` removes exactly the node-0 pair. So row `i=2m+d` and column `j=2q+s` of `A_exact` correspond to Lean node `f[m]`, derivative `d∈{0,1}`, column node `f[q]` and `c/d` type `s∈{0,1}`. **No row/column permutation, transposition, scaling, or sign reversal is needed.** Note Python's variable `R` names the residue *list*, not Lean's matrix `R`.

This completes the source-level algebraic identification of the **entire** 20×20 ideal matrix, strengthening the previous partial matching of dimension, signs, inverse thresholds and Lean `RValue=R`.

## 3. Verification and admission boundary

- **Established by exact source algebra:** polynomial coefficient identity, conjugate folding, exact Q/D normalization, row and column indexing, and `A_exact=Construction.R`.
- **Not established by this audit:** successful execution of the original Python 60-digit outward interval program with all assertions enabled, whether the particular interval implementation encloses its ideal `A_exact` throughout the complete checker, equality of every separate finite-bound table with the Lean rational enclosures, a pinned Lean build and transitive axiom audit, or the paper's analytic propagation/energy theorem.
- **Research/ownership:** This is a non-claiming RESEARCH_DRIVER contribution to source correspondence. The independent formal OAI7-090 Researcher Task is not satisfied or claimed by this analysis. Existing Lean/Python and paper authors retain attribution; no new Native Result or JT2/OAI mother-objective completion is inferred.

Prior related project notes: `research_notes/driver/2026-11-14_oai7_090_python_lean_evidence_crosswalk.md` and `research_notes/driver/2026-11-15_oai7_090_lean_density_matrix_source_audit.md`. Next independent verification should run unmodified `python3 -I verification/check_certificate.py` from the article directory with assertions enabled, build the pinned Lean modules, inspect `#print axioms` for the intended theorems, and compare its interval/rational table enclosures to the already-identified exact matrix. These execution steps require actual run outputs before any new claim.
