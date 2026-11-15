# PREFIX-818 — Finite-type BRC count quotients and a minimal pure-removal future moment carrier

Date: 2026-11-16 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH auxiliary science. Frozen project scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessor: PREFIX-817. Research identity provenance: `EM-DIRECT-AB379B`, existing direct-research session `MCP-ddad8ec8dced4918a59a479555c21490`; this is not a CLAIM on `RS-X6-NATIVE-TIME-DYNAMICS`.

Status: AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / INDEPENDENT_REVIEW_PENDING. P000, the ACTIVE residual-fidelity worldview, six-axis native X6 space, separately typed event time, and source/port rules are retained. The following is an auxiliary weighted *formal-toggle* BRC count system, with future-operation and readout scope explicitly declared.

## 1. The precise predecessor model

For m named branches, capacity 0<=q<=m, states are subsets S⊆[m] with |S|<=q. A legal addition S→S∪{i} (i∉S, |S|<q) has weight α_i∈Z_{>=0}; a removal S→S\{i} (i∈S) has weight β_i∈Z_{>=0}. Path weights multiply and alternative paths add. Q is the corresponding nonnegative integer weighted adjacency; C[S,k]=1{|S|=k}. The declared h-step output is the **complete terminal-count histogram** Q^h C, for all formal h>=0. The complete named trace, path provenance, and native Cell/Link/Port event semantics are additional interfaces, not collapsed by this statement.

PREFIX-817 proved the finite observability certificate and for q=1 a minimal three-moment exact linear carrier.

## 2. Theorem 818.1: exact weighted type-count quotient for arbitrary capacity

Suppose the m branches are partitioned into r nonempty *types* I_t, with sizes m_t. Within each type, α_i=a_t and β_i=b_t. Map a named subset S to n(S)=(|S∩I_t|)_t. The legal quotient tuples are 0<=n_t<=m_t and Σ_t n_t<=q, and its weighted transitions are

`B[n,n+e_t]=(m_t-n_t)*a_t` when Σn<q, and
`B[n,n-e_t]=n_t*b_t` when n_t>0.

The quotient readout is `D[n,k]=1{Σ n_t=k}`. For every named state S and every h>=0, its count histogram is **exactly** the n(S)-row of B^h D. More generally, initial named integer mass μ is pushed forward by adding masses with the same n, and its complete future-count readouts are identical under the quotient.

*Proof.* Each named state S of type-count n has precisely m_t−n_t distinct addition destinations of type n+e_t, each with weight a_t, and n_t removal destinations of type n−e_t, each with weight b_t. Thus summing weighted outgoing transitions over each quotient class depends only on n, and gives B. If P is the 0/1 map P[S,n]=1{n(S)=n}, then QP=PB and C=PD. Inductively Q^hC=PB^hD. Linearity proves the mass statement. QED.

The number of quotient states is
`K(m_1,...,m_r;q)=Σ_{k=0}^q [z^k]∏_{t=1}^r(1+z+...+z^{m_t})`.
It is at most `binom(q+r,r)` and at most the named-state count `N=Σ_{k=0}^q binom(m,k)`. This provides a nonnegative integer carrier of dimension K for arbitrary α,β constant on types, without requiring negative coordinates. For r=1, the quotient is the exact (q+1)-state birth/death chain with addition weight (m−k)a and removal weight kb.

## 3. Theorem 818.2: exact elementary-symmetric integer moment carrier for all future pure-removal readouts

Specialize to **pure removal**: all α_i=0, arbitrary β_i∈Z_{>=0}. For any named initial integer mass μ_S, define for 0<=h<=k<=q

`M_{k,h}=Σ_{|S|=k} μ_S e_h(β_i:i∈S)`,

where e_h is the elementary symmetric polynomial (e_0=1). Retain the `T(q)=(q+1)(q+2)/2` integer coordinates M_{k,h}, independent of m.

Under one formal removal step, the update is exactly

`M'_{k,h}=(h+1) M_{k+1,h+1}` for k<q, and `M'_{q,h}=0`.

The complete output is `Y_k=M_{k,0}`, while at h future steps

`Y_k^{(h)}=h! M_{k+h,h}` if k+h<=q, otherwise 0.

*Proof.* A source S of cardinality k+1 contributes to destination S\{i} with weight β_i. Hence its contribution to M'_{k,h} is Σ_{i∈S}β_i e_h(β_{S\{i}})=(h+1)e_{h+1}(β_S), since each monomial supported on h+1 distinct elements is counted h+1 times. Summing over μ proves the update; induction gives the output formula. Equivalently, precisely h! removal orders exist for each h-element subset of S, each with the same product β. All equations are exact over the integers. QED.

Since all trajectories have at most q removal steps, Q^{q+1}=0. The carrier is a **future-count** sufficient observer for this fixed removal-only operation language, including arbitrary initial signed/integer mass; for nonnegative μ the moments stay nonnegative. Computing moments initially from a dense named μ requires reading all nonzero input masses, and their bit lengths grow with weights. The carrier gives O(q²) integer coordinates and O(q²) elementary update operations after this conversion.

## 4. Theorem 818.3: sharp minimal linear dimension and maximal partition separation

Assume m>=q+1, β_1,...,β_m are **pairwise distinct positive integers**, and α_i=0. Then the minimal rational linear realization dimension for all initial named mass and all future terminal-count histograms (in the sense of PREFIX-817's observability theorem) is **exactly** T(q).

*Proof of minimality.* PREFIX-817 identifies the minimum with the rank of the future observability matrix. For fixed initial size k, the k+1 columns of observations with horizons h=0,...,k and terminal count k−h equal the functions `h!e_h(β_S)` on k-element subsets S. They have support only on initial size k. Choose any k+1 distinct branch indices U. For i∈U, take S_i=U\{i} (each size k). Their generating polynomials are `P_i(z)=∏_{j∈U\{i}}(1+β_j z)`. Evaluating a linear combination Σ_i c_i P_i(z)=0 at z=−1/β_l annihilates every P_i with i≠l; P_l(−1/β_l)=∏_{j≠l}(1−β_j/β_l)≠0. Thus all c_l vanish, proving k+1 independent polynomial coefficient vectors. This shows rank k+1 on each initial-cardinality slice. Since the corresponding columns are supported on disjoint slices, total rank is Σ_{k=0}^q(k+1)=T(q). The carrier in Theorem 818.2 attains the bound. QED.

Furthermore, the **coarsest exact named-state partition** preserving current count and all future-count histograms is the discrete partition of the `N=Σ_{k=0}^q binom(m,k)` named states. Distinct initial cardinalities differ at horizon 0. For two different k-subsets S,T, equality at every horizon would give equality of all e_h(β_S) and e_h(β_T), hence equality of `∏_{i∈S}(x+β_i)` and `∏_{i∈T}(x+β_i)`. Distinct positive β_i imply S=T by uniqueness of polynomial factorization. Every distinct pair of named states is separated by some horizon <=q. Consequently, although no two named states may be merged by such a partition, a linear integer moment carrier of only T(q) coordinates is lossless for this declared output and operation language.

**Exact separation witness.** Take m=8,q=2, α=(0,...,0), β=(1,2,3,4,5,6,7,8). There are N=37 named states, all 37 named-state partition classes remain distinct, yet the minimal exact linear count carrier has T(2)=6 integer coordinates. In the equal-type nonnegative case, Theorem 818.1 instead provides the (q+1)-dimensional count-only carrier, illustrating how the minimal dimension depends on the chosen weight family and allowed quotient.

## 5. Independent exact regression and limits

Executable standard-Node BigInt checker: `research_notes/portable_direct/PREFIX818_R6_PURE_REMOVAL_MOMENT_CHECK.js`. JSON output: `research_notes/portable_direct/PREFIX818_R6_PURE_REMOVAL_MOMENT_RESULTS.json`. The checker uses generic named-state weighted path propagation (not the moment formulas) as one side, and elementary-symmetric moment / explicit type-quotient propagation as the other.

Finite tested range:
- Pure removal: m=1..7, q=0..min(m,4), three positive pairwise-distinct β sequences per m; 87 full parameter cases, 1,467 named initial states, 8,871 exact histogram comparisons through horizon q+2, 33,870 pair separations, 195 nonzero Vandermonde evaluation certificates.
- Type quotient: m=1..5, q=0..min(m,3), r=1..min(m,3) (balanced contiguous nonempty types), 36 deterministic pairs of a_t,b_t∈{0,1,2} per tuple; 1,584 parameter cases, 11,592 named initial states, 69,552 exact horizon comparisons at h=0..5.
- All finite assertions passed, with the range and deterministic generation fully exposed in code. Arbitrary-parameter theorems follow from proofs, not extrapolation of finite tests.

## 6. Next scientific questions and provenance

Derive the minimal future-count dimension for q>=2 with **both** additions and removals nonzero, refining the type-count quotient K and testing exact observability ranks/Smith normal form with generic named weights. A second direction is the effect of admitting one addition operator into the pure-removal language: determine the minimal repair moments and find the smallest explicit source-residual witness. Compare complete input conversion, arithmetic bit length, memory, and full output recovery in any algorithmic claim.

This is an independent auxiliary named-source BRC theorem, not a native X6 Cell/Link/Port event rule or a physical-time clock. Current shared task `RS-X6-NATIVE-TIME-DYNAMICS` remains subject to its native owner/typed-continuation authority; this paper does not claim that task or modify its frozen evidence.
