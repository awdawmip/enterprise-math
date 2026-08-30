# Research Return — Add/Mul Bridge A6: Finite-Field Gauss / Jacobi Spectrum

- Task: `RS-ADDMUL-GAUSS-ADDITIVE-MULTIPLICATIVE-SPECTRUM`
- Publication: `TP2-4DB8E710150A47A5F9D8`
- Researcher: `EM-AMSPEC-A6-7C41D2`
- Owner: `research/addmul-gauss-additive-multiplicative-spectrum`
- Execution branch: `research/addmul-gauss-spectrum-em-amspec-a6-7c41d2`
- Frozen taskbook: `research_tasks/ADDMUL_GAUSS_ADDITIVE_MULTIPLICATIVE_SPECTRUM_20260830.md@sha1:471f2c7ebe29680453c4ae2cf968c064c76b8fdf`
- Terminal verdict: `INVERTIBLE_TYPED_SPECTRAL_TRANSFORM_CLASSIFIED`
- Hard target: `FINITE_FIELD_ADDITIVE_MULTIPLICATIVE_SPECTRAL_BRIDGE_CLASSIFIED`
- Hard-target status: **SATISFIED at the finite `F_p` typed-linear level; natural convolution-algebra intertwining is obstructed.**

## 1. Executive result

For every prime `p`, the additive and multiplicative character systems do form an exact finite bridge, but only after the zero element is typed explicitly.

The sharp classification is:

1. **Correlation probe — YES.** Gauss sums are the transition coefficients between multiplicative characters and additive Fourier frequencies; Jacobi sums are the cross-structure constants for additive convolution of multiplicative-character states.
2. **Invertible typed transform — YES.** The unit-character space has dimension `p-1`; after adjoining the zero atom `delta_0`, the basis
   `B_x0={delta_0} union {chi_j : j in Z/(p-1)}`
   has dimension `p`, and its additive Fourier transition matrix is invertible for every prime `p`.
3. **Natural algebra isomorphism — NO.** On the unit sector, the Gauss transform does not intertwine multiplicative convolution with additive-convolution Fourier multiplication. This is an operation-level obstruction, not a rank failure.

Thus the correct Enterprise residue is not “Gauss sums magically identify addition and multiplication.” It is:

> **zero-completed invertible coordinate bridge + sparse Jacobi cross-law + exact zero-resonance defect + explicit non-intertwining guard.**

No claim of mathematical novelty is made for the classical Gauss/Jacobi identities themselves. The task contribution is the exact strength classification, zero-typing, operation audit, and finite Enterprise interface.

## 2. Frozen conventions

Let

- `K=F_p`,
- `U=F_p^x`, `m=p-1`,
- `g` a primitive root of `U`,
- `zeta=exp(2 pi i/p)`, `eta=exp(2 pi i/m)` when `m>1`.

Additive characters are

`psi_t(x)=zeta^(t x)`, `t in K`.

Multiplicative characters are

`chi_j(g^r)=eta^(j r)`, `j in Z/m`,

and are extended to `K` by `chi_j(0)=0`. Write `epsilon=chi_0` for the trivial unit character, also zero at `0`, and let `delta_0` be the point mass at `0`.

Use the unnormalised additive Fourier transform

`F_+(f)(t)=sum_{x in K} f(x) psi_{-t}(x)`,

with inversion

`f(x)=(1/p) sum_{t in K} F_+(f)(t) psi_t(x)`.

Define the Gauss sums

`G_j=sum_{x in U} chi_j(x) psi_1(x)`.

In particular `G_0=-1`.

## 3. The zero-completed multiplicative basis is the exact missing type

### Theorem A — orthogonal completion

`B_x0={delta_0, chi_0, ..., chi_{m-1}}` is an orthogonal basis of `C^K`:

- `<delta_0,chi_j>=0`,
- `<chi_j,chi_k>=m delta_{jk}`,
- `||delta_0||^2=1`.

So the apparent dimension mismatch between `p` additive frequencies and `p-1` multiplicative characters is exactly one zero atom. No quotient or hidden coordinate is required.

### Unit-only image

Let

`V_0={f in C^K : f(0)=0}=span{chi_j}`.

Fourier inversion at zero gives

`f(0)=(1/p) sum_t F_+(f)(t)`.

Hence

`F_+(V_0)=H_0={A in C^K : sum_t A_t=0}`.

Both spaces have dimension `p-1`, so the unit-only transform is already injective and bijective onto this codimension-one hyperplane. Dropping `delta_0` therefore does not cause mysterious rank loss: it imposes one exact global linear constraint.

## 4. Forward Gauss transition, rank and determinant

For the zero atom,

`F_+(delta_0)(t)=1` for every `t`.

For the trivial unit character,

- `F_+(epsilon)(0)=p-1`,
- `F_+(epsilon)(t)=-1` for `t != 0`.

For `j != 0`,

- `F_+(chi_j)(0)=0`,
- for `t != 0`,

`F_+(chi_j)(t)=chi_j((-t)^(-1)) G_j`.

The last identity is the exact change of variable `y=(-t)x`.

For every nontrivial `chi_j`, classical orthogonality gives

`|G_j|^2=p`.

Let `M_p` be the `p x p` matrix whose columns are `F_+(delta_0)` followed by `F_+(chi_j)`. Parseval and orthogonality of `B_x0` give the exact Gram identity

`M_p^* M_p = p diag(1, (p-1) I_{p-1})`.

Therefore

`rank(M_p)=p`

and

`|det M_p|^2 = p^p (p-1)^(p-1)`.

This proves the full zero-completed transition is invertible for every prime `p`.

### Explicit coefficient inversion

If

`f=c_delta delta_0 + sum_j c_j chi_j`

and `A=M_p c=F_+(f)`, then

`c_delta=(1/p) sum_t A_t`,

and

`c_j=(1/(p(p-1))) sum_t conjugate(F_+(chi_j)(t)) A_t`.

Thus the bridge is not merely full rank abstractly; it has an exact typed inverse.

## 5. Reverse expansion of additive characters

The reverse direction has two sharply different cases.

For `s=0`,

`psi_0 = delta_0 + epsilon`.

For `s != 0`, multiplicative Fourier inversion on `U` gives

`psi_s = delta_0 + (1/(p-1)) sum_j chi_j(s) G_{-j} chi_j`.

The `j=0` coefficient is `-1/(p-1)` because `G_0=-1`; all nontrivial coefficients have magnitude `sqrt(p)/(p-1)`.

This handles the constant character, the zero point, and all nonzero additive frequencies without silently identifying `K` with `U`.

## 6. Jacobi sums are sparse cross-structure constants

Define additive convolution on `K` by

`(f *_+ h)(x)=sum_{y in K} f(y) h(x-y)`.

Define

`J_{j,k}=sum_{u in K} chi_j(u) chi_k(1-u)`.

For every `x != 0`, the substitution `y=xu` gives

`(chi_j *_+ chi_k)(x)=J_{j,k} chi_{j+k}(x)`.

At `x=0`, however,

`(chi_j *_+ chi_k)(0) = (p-1) chi_k(-1)` if `j+k=0 mod m`,

and is `0` otherwise.

Hence the full function law is:

### Non-resonant sector: `j+k != 0`

`chi_j *_+ chi_k = J_{j,k} chi_{j+k}`.

When the product character is nontrivial, the usual Gauss/Jacobi relation reads

`J_{j,k}=G_j G_k / G_{j+k}`.

This includes the one-trivial/one-nontrivial case because `G_0=-1`, yielding

`epsilon *_+ chi_j = chi_j *_+ epsilon = -chi_j` for `j != 0`.

### Inverse-character resonance: `k=-j`, `j != 0`

Using `J_{j,-j}=-chi_j(-1)`, one gets

`chi_j *_+ chi_{-j} = -chi_j(-1) epsilon + (p-1) chi_j(-1) delta_0`.

### Trivial/trivial resonance

`epsilon *_+ epsilon = (p-2) epsilon + (p-1) delta_0`.

For `p=2` this reduces exactly to `epsilon *_+ epsilon=delta_0`.

Therefore the unit-character sector is closed under additive convolution except precisely at inverse-character resonance, where a zero atom is emitted.

Define the zero-projection defect

`Def_0(j,k)=(p-1) chi_k(-1) 1_{j+k=0} delta_0`.

This is the operation-level information that is lost if one works only on `U`.

## 7. Why the bridge is not a natural convolution-algebra isomorphism

On `U`, define multiplicative convolution

`(f *_x h)(x)=sum_{y in U} f(y) h(x y^(-1))`.

Then

`chi_j *_x chi_k = (p-1) delta_{jk} chi_k`.

So `e_j=chi_j/(p-1)` are mutually orthogonal primitive idempotents.

If the natural Gauss transform intertwined multiplicative convolution with pointwise multiplication of additive Fourier coordinates (equivalently with additive convolution before Fourier transform), then for `j != k` one would have

`F_+(e_j)(t) F_+(e_k)(t)=0` for every `t`.

For every `p>=3`, take `j=0`, `k=1`. For every `t != 0`,

- `F_+(chi_0)(t)=-1`,
- `F_+(chi_1)(t)=chi_1((-t)^(-1))G_1 != 0` because `|G_1|^2=p`.

Their pointwise product is therefore nonzero. For `p=2`, the unique normalized unit idempotent maps to `(1,-1)`, whose pointwise square is `(1,1)`, not itself.

Thus the natural Gauss transition is **not** an operation-intertwining algebra map for any prime `p`.

This statement is deliberately narrow: it does **not** assert that no abstract complex-algebra isomorphism can be manufactured after changing the objects or operations. It says the natural Gauss/Jacobi bridge does not identify the two natural convolution structures.

A second structural warning is that adjoining `delta_0` fixes the linear dimension mismatch, but `0` is absorbing for field multiplication rather than an element of the unit group. Hence zero completion is canonically useful for the linear bridge but does not automatically extend the unit-group convolution algebra.

## 8. Exact strength classification

| Strength | Verdict | Exact reason |
|---|---|---|
| Correlation probe | `YES` | Gauss coefficients and Jacobi coefficients quantify overlap of additive and multiplicative character structure. |
| Invertible typed transform | `YES` | `B_x0` is a basis and `|det M_p|^2=p^p(p-1)^(p-1)>0`. |
| Unit-only typed transform | `YES -> H_0` | Exact image is `sum_t A_t=0`, dimension `p-1`. |
| Natural convolution-algebra intertwiner | `NO` | Multiplicative primitive idempotents have overlapping nonzero Gauss spectra. |
| Zero-free additive-convolution closure | `NO at inverse resonance` | Exact `delta_0` defect occurs iff `j+k=0`. |

The terminal classification is therefore stronger than `GAUSS_BRIDGE_IS_CORRELATION_NOT_OPERATION_ISOMORPHISM`: the bridge is genuinely invertible as a **typed linear spectral transform**, while its natural operation-level intertwining is obstructed.

## 9. Enterprise translation: minimal `GAUSS_JACOBI_BRIDGE_PACKET`

A minimal finite packet should retain only:

1. field size / prime `p`;
2. explicit zero atom `delta_0`;
3. multiplicative character index `j in Z/(p-1)`;
4. additive frequency `t in F_p`;
5. Gauss transition column rule `M_p(t,j)`;
6. inverse normalisations `p` and `p-1`;
7. Jacobi cross-structure constants `J_{j,k}`;
8. zero-resonance defect `Def_0(j,k)`;
9. strength flags:
   - `LINEAR_TYPED_INVERTIBLE=true`,
   - `CORRELATION_PROBE=true`,
   - `NATURAL_CONVOLUTION_INTERTWINER=false`.

This is finite, exact, operation-audited, and does not import a heavier ambient theory.

### Candidate connection to Enterprise Math

The useful pattern is a **two-coordinate system with a one-type completion and a sparse resonance defect**:

- one coordinate system diagonalises additive translation;
- the other diagonalises unit-group multiplicative translation;
- transition is full rank after a single missing-type completion;
- cross-convolution is index-additive away from a codimension-one/inverse-pair resonance;
- the resonance emits a distinguished defect atom rather than destroying invertibility.

This pattern is potentially reusable when Enterprise Math encounters two operations whose natural state spaces differ by a small typed boundary sector.

## 10. Exact verification

Frozen checker:

`research_checks/ADDMUL_GAUSS_ADDITIVE_MULTIPLICATIVE_SPECTRUM_CHECK_20260830.py`

Frozen table:

`research_artifacts/ADDMUL_GAUSS_ADDITIVE_MULTIPLICATIVE_SPECTRUM/exact_table_p_le_31.json`

The checker uses no floating-point cyclotomic approximation. It certifies identities by exact residue permutations, cyclic exponent multisets, and root-of-unity orthogonality.

Coverage:

`p in {2,3,5,7,11,13,17,19,23,29,31}`.

Exact core assertions checked: **79,261**.

The table records primitive roots, full/unit dimensions, nontrivial Gauss-column counts, ranks, determinant certificates, and inverse-character resonance counts. For every tested prime:

- `full_transition_rank=p`,
- `unit_transition_rank=p-1`,
- every nontrivial Gauss column is nonzero,
- the determinant certificate agrees with `p^p(p-1)^(p-1)`,
- the exact Jacobi convolution counter agrees on every `(j,k,x)`.

The finite checker is a regression guard, not the proof of the all-prime theorem; the all-prime statements above follow from the symbolic orthogonality/change-of-variable arguments.

## 11. Decision on `F_q`

No `F_q` extension is required to settle the hard target. Over `F_q`, the same strength classification is expected after replacing `psi_t(x)` by trace-defined additive characters and indexing multiplicative characters of the cyclic group `F_q^x`; the zero atom remains a one-dimensional completion. A norm map becomes relevant only when comparing or descending characters between fields, not for the internal `F_q` bridge itself.

Because this adds no new strength category, extending to `F_q` now would increase surface area without changing the answer. It is intentionally deferred.

## 12. Kill list / guards

The result does **not** license any of the following:

- “addition and multiplication are algebraically identical over `F_p`”;
- treating character orthogonality as an operation isomorphism;
- dropping the zero atom without recording the hyperplane constraint;
- treating `G_0` like a nontrivial Gauss sum of norm `sqrt(p)`;
- extrapolating distribution statements from `p<=31`;
- claiming classical Gauss/Jacobi identities as new Enterprise theorems;
- importing an infinite spectral state where the finite packet suffices.

## 13. Hard-target disposition and next control-plane recommendation

`FINITE_FIELD_ADDITIVE_MULTIPLICATIVE_SPECTRAL_BRIDGE_CLASSIFIED` is satisfied with disposition:

`ZERO_COMPLETED_GAUSS_TRANSITION_FULL_RANK / UNIT_ONLY_IMAGE_EXACT_CODIM1 / JACOBI_SPARSE_ADDITIVE_CONVOLUTION_WITH_INVERSE_RESONANCE_ZERO_DEFECT / NATURAL_CONVOLUTION_ALGEBRA_INTERTWINER_OBSTRUCTED`.

Recommended Driver action:

1. accept the typed-linear bridge and zero-resonance defect as the A6 result;
2. keep the algebra-isomorphism guard explicit;
3. compare the reusable pattern `small typed completion + sparse operation defect` against A1/A2/A4/A5 only after those independent lanes return;
4. open an `F_q` successor only if a downstream task actually needs trace/norm functoriality rather than merely the same local classification.
