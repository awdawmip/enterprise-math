# EC49BP — Exact finite-filter algebra for selected X6 BRC path ensembles

**2026-10-30 | AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**

## Typed population and source
A path witness is an ordered signed-axis word over the six native axes ±E_i, from a chosen chart-relative Cell (no global origin). Fix path length n, endpoint displacement d∈Z⁶, a finite witness universe U, and twelve strictly positive rational direction weights. Its single-path product is χ(t)=∏_j w(t_j). The pinned native `signed_brc.py` API computes `endpoint_weight(n,d,w+,w-)`, which SUMS χ(t) over **all** compatible words. We separately define a mathematical selected-ensemble interface μ:U→Q_{≥0}; neither selection nor filtering is an existing native API argument.

Declare the future language before quotienting: uniform finite-subgroup axis relabeling H≤S₆, algebraic word inversion, known one-hole concatenation and path predicates with their Boolean/operation pullback closure. A future outputs a positive-rational weighted sum of surviving path witnesses and, when stipulated, the original witness count. Each operation sequence induces a rational row ℓ:U→Q: the final weight of one original witness if retained, or zero. Its total output is ℓ·μ. Let V be the Q-linear span of all these pulled-back rows, adding constant row 1 when count is observed. Because U is finite, V is finite-dimensional, even for infinitely many allowed known contexts.

## Theorem A — exact minimal additive future-sufficient state

For any rational basis v₁,...,vᵣ of V, the vector T(μ)=(vⱼ·μ)ⱼ is exactly future-sufficient: T(μ)=T(ν) iff **every declared future observation** agrees. Moreover, among Q-linear additive rational statistics on **all** μ∈Q_{≥0}^U, no statistic with fewer than r=dim_Q V coordinates can be sufficient.

**Proof.** Every ℓ is a Q-linear combination of the vⱼ, hence all future outputs factor through T. Conversely each vⱼ is a linear combination of actual observation rows, so equality of all outputs implies equality of T. For minimality suppose another Q-linear S is sufficient. For any rational z∈ker S choose rational a with a,a+z≥0 coordinatewise. Sufficiency yields ℓ·z=0 for all observed ℓ. Thus ker S⊆ker ℓ for all ℓ and V⊆rowspan_Q(S), requiring rank(S)≥dim_Q V. QED.

**Exact scalar reduction test.** Let u(t)=χ(t). For unrestricted selected rational ensembles, the single unfiltered aggregate u·μ suffices iff V⊆span_Q{u}; with independently retained initial witness count the pair (1·μ,u·μ) suffices iff V⊆span_Q{1,u}. These are necessary and sufficient exact row-rank tests. The case of a single known fixed full ensemble μ≡1 has no variable ensemble to distinguish; that trivial information claim does not implement filter operations in native endpoint_weight. The rank lower bound is for Q-linear additive coordinates, not arbitrary integer codings or bit complexity.

## Theorem B — finite H-stable Boolean-filter closure

Suppose an H-stable Boolean algebra B of filters on U contains all pullbacks of the declared filters, H relabelings, inversion and known contexts. Suppose each future path weight is a known common scalar times χ(σt) for σ∈H. For each nonempty Boolean atom A∈B and σ∈H define
F_{A,σ}(μ)=Σ_{t∈A} μ_t χ(σt).
The vector of these atom/orbit sums, plus 1·μ if count is observed, is sufficient and complete for all declared future outputs. Its rational row rank, rather than its raw row count, is the exact minimum additive dimension.

**Proof.** Any Boolean filter is a disjoint union of atoms; intersections reduce to unions of atoms, and permitted pullbacks stay in B. Each future weight is by hypothesis a common rational scalar times one H-orbit weight, so every future output is a combination of atomic rows. Conversely each atom/orbit pair is directly selectable by a legal Boolean predicate and relabeling. Apply Theorem A to their row span. QED. A prefix-sensitive predicate outside this Boolean algebra is **not** covered.

## Fully enumerated native-X6 example and obstruction

Set n=4, d=(0,0,0,0,0,0), w+=(2,3,3,2,1,1), w-=(1,1,1,1,1,1), H={id,(1 2)} and a fixed weight instrument. Filter generators are 'axis 1 occurs' and 'axis 3 occurs'; H closure adds 'axis 2 occurs'. There are 7 reachable atoms of the three presence bits (111 is impossible at length 4). Inversion preserves these presence bits and closed-path χ. A known concatenated context changes each presence bit b_i to b_i∨c_i; it multiplies χ by a known common factor. Thus the stated filter closure hypothesis is met.

All 396 ordered signed-axis closed four-step words were enumerated exactly. The native kernel gives endpoint_multiplicity(4,0)=396 and endpoint_weight(4,0,w+,w-)=1560, matching the exact word sum. There are 21 possible loop-count histograms. Among 17 candidate row functions (count, two unfiltered orbit weights and 14 atom-orbit weight rows), the unfiltered count-plus-H-orbit Q-rank is **3** and the filtered Q-rank is **10**. Hence seven additional independent Q-linear additive coordinates are necessary for arbitrary selected ensembles. A transparent rank decomposition: atoms 000,001,011,101,110 each contribute one weight dimension; atoms 010,100 each contribute two, total nine, and the count row is independent because weights vary within atom 000. Exact SymPy rational matrix ranks were independently computed over all 396 words and the 21 histogram representatives.

An explicit counterexample with the **same ordered first +E₅ and last −E₅** is:
A={(+5,+1,−1,−5),(+5,+2,−2,−5)};
B={(+5,+3,−3,−5),(+5,+4,−4,−5)}.
Each selected ensemble has witness count 2 and the same unfiltered H-orbit aggregate (5,5), but selecting paths containing axis 1 gives weighted outputs **2** and **0**. Thus the former unfiltered aggregate is not sufficient for the expanded filter language. In a *single-path* test retaining first and last labels, the H-orbit and filtered partitions both have 192 classes; this does not invalidate the aggregate rank increase, because aggregation loses contribution-level association.

## Validation and limits
An actually executed Python Fraction/SymPy checker pins native signed_brc.py Git Blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, calls its endpoint_multiplicity and endpoint_weight, checks all 396 words, exact rational 396-column matrix ranks against 21 representative columns, 1,188 known-context identities, inversion/axis-permutation closure and the two-ensemble witness. Repeated stdout was byte-identical to the JSON report. The universal finite-U theorem rests on algebra, not extrapolation from n=4.

Signed/complex amplitudes, unrestricted physical heartbeat time, and native filtration support are **not** claimed. P000/ACTIVE worldview remain unchanged. Next EC49BQ: order-/prefix-sensitive selectors and n-dependent additive-rank growth, retaining boundary/source/provenance and finite-bit resource semantics.