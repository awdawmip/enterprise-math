# R5 — Exact fixed-fiber Blackwell census: 49 sharp edges

Date: 2026-11-11. **Author-side exact finite theorem**; not independently reviewed or admitted as a formal Source Result. This auxiliary P/Q–BRC observer-fiber result does not change P000's six-dimensional native X6 spatial ontology.

## Frozen input and exact theorem

Use the same 30-coordinate strictly positive rational physical transfer witness as [PR #2017, WITNESS.txt](https://github.com/awdawmip/enterprise-math/blob/fab8456e8587ce54b3727579d951d5c6c7bf172a/research_notes/brc_r5_six_edge_circuits_20261111/WITNESS.txt), reproduced in the verifier. Frozen ratio numerators are
\[
R=(2,10,15,20,25,30,38),\quad r_i=R_i/20.
\]
The 30 allowed arcs are all $(i,j)$ for $i=0,\ldots,6$ and dynamic source $j\in\{1,2,3,5\}$, plus singleton arcs $(0,0),(6,6)$. The 21-component observer $C$ records target marginals, source marginals and first target-ratio moments at every source; $\operatorname{rank}(C)=15$. Let the **single fixed physical fiber** be
\[
\mathcal F=\{E\in\mathbb R^{30}_{\ge 0}:CE=CE^0\}.
\]
No physical parameters, ratios, or observer right-hand sides are varied in this census.

[PR #2045](https://github.com/awdawmip/enterprise-math/pull/2045) enumerated 15,120 seven-label $K_4$ plus doubled-high-pair assignments, finding 14,832 full signed 14-arc circuits and 288 degenerate ones, and supplied the exact graph criterion for sharp word length four. The present theorem is:

**Exactly 49 of those 14,832 full 14-arc candidate circuits occur as adjacent-vertex directions in the above fixed fiber.** The distribution by degree-three source pair is $(1,2):15$, $(1,5):15$, $(2,5):19$, and zero for the other three choices $(1,3),(2,3),(3,5)$.

All 49 edges have **two 15-positive-arc endpoints**. The 49 edges have **58 distinct endpoints**. Retaining only these sharp edges yields a forest with **nine connected components** of vertex sizes $2,4,6,6,6,6,8,10,10$; 38 endpoints have sharp-subgraph degree 1 and 20 have degree 3. This is the sharp-only graph, not the complete adjacency graph of these vertices. Subject to PR #2045's preceding sharp-support criterion, these are all length-four adjacent rays in this particular fiber. The 49 incidence count itself is an exact result for the 14,832 explicitly enumerated candidate circuits regardless of their external admission status.

## Proof 1: edge support is exactly sixteen arcs

Let $S$ denote a full signed 14-arc circuit of this type. Its dynamic observer submatrix satisfies $\dim\ker C_S=1$ and $\operatorname{rank}C_S=13$; its one-dimensional signed nullspace has full support $S$.

The two singleton arcs $(0,0)$ and $(6,6)$ have strictly positive masses in **every** transfer of $\mathcal F$, since their corresponding source marginals are fixed by the observer and there are no alternative outgoing arcs at those source ports. Thus if adjacent vertices $V,W$ have difference support $S$, their union support $U=\operatorname{supp}V\cup\operatorname{supp}W$ has at least 16 arcs. A face of a nonnegative equality fiber supported on $U$ has dimension
\[
|U|-\operatorname{rank}C_U.
\]
Since $V,W$ are adjacent, this is 1. Since $\operatorname{rank}C\le15$, necessarily $|U|\le16$. Hence
\[
U=S\cup\{(0,0),(6,6)\}
\]
**exactly**. The two singleton source-marginal coordinates are independent of the dynamic-source submatrix, so $\operatorname{rank}C_U=13+2=15$. The face supported on precisely $U$ is consequently a one-dimensional affine line intersected with coordinate nonnegativity. It forms a genuine adjacent edge with full signed support $S$ **if and only if** this face has a point with all 16 specified entries strictly positive. Each passing $S$ determines exactly one edge.

This proves that searching the entire 15-dimensional polytope's vertices is unnecessary: every one of the 14,832 candidate supports has a *necessary and sufficient* sixteen-arc strict-feasibility test.

## Proof 2: strict feasibility is one rational interval

Choose low-degree dynamic source ports $p,q$ and high-degree ports $h,k$. Assign the seven distinguishable target labels to the source pairs
\[
A=pq,\ B=ph,\ C=pk,\ D=qh,\ E=qk,\ F=hk,\ G=hk,
\]
with the two repeated $hk$ labels ordered by target index $F<G$.

For target $i$, let $M_i$ be its dynamic target marginal from $E^0$ (subtract the two singleton contributions at targets 0,6). For dynamic source $j$ let $Q_j$ denote source mass and let $T_j=\sum_i R_iE^0_{ij}$ be the unscaled first-moment total. In each of the seven allowed source pairs, write the first source mass as $x_i$ and the second as $M_i-x_i$; full 14-arc support means $0<x_i<M_i$ for every $i=A,\ldots,G$.

Denote their seven ratio numerators $a,b,c,d,e,f,g$. The two low source marginal/moment equations and the first high source equations give, by exact elimination, with $t=x_A$:
\[
\begin{aligned}
x_B&=\frac{T_p-cQ_p-(a-c)t}{b-c},&
x_C&=Q_p-t-x_B,\\
x_D&=\frac{T_q-a(M_A-t)-e(Q_q-M_A+t)}{d-e},&
x_E&=Q_q-M_A+t-x_D,\\
H_0&=Q_h-M_B-M_D+x_B+x_D,&
H_1&=T_h-bM_B-dM_D+b x_B+d x_D,\\
x_F&=\frac{gH_0-H_1}{g-f},&
x_G&=H_0-x_F.
\end{aligned}
\]
All denominators are nonzero because the frozen ratios are distinct. The remaining source equations follow from global target-marginal and ratio-moment conservation. Every $x_i$ is therefore an explicit *rational affine function* of the single parameter $t$.

Each inequality $0<x_i(t)<M_i$ cuts out a rational **open interval** of $t$. The intersection of seven such intervals is nonempty if and only if its largest lower bound is strictly less than its smallest upper bound. This is both necessary and sufficient for a strictly positive point on the sixteen-arc support, hence for the edge by Proof 1. All comparisons in the verifier use exact Python fractions, not floating-point feasibility tests.

For example, low ports $(1,2)$ and label order $(A,B,C,D,E,F,G)=(0,3,1,2,6,4,5)$ yield precisely
\[
\frac{8974459}{407710128}<t<\frac{629849805}{24598511056}.
\]
The rational midpoint $t=1756963247/73795533168$ gives a valid sixteen-arc strictly positive transfer.

## Proof 3: complete finite count and graph structure

There are $\binom42=6$ low source pairs and $7!/2=2520$ target-label assignments each: **15,120** cases, exhaustive and without duplicate assignment. Use the exact signed integer circuit coefficients in PR #2045 to distinguish 14,832 full from 288 degenerate supports. For each full support, derive the unique affine line and intersect all seven exact rational open intervals. **49** have nonempty strict intervals; **14,783** do not.

For every passing case the verifier reconstructs both rational endpoints in the complete 30-arc order and checks their target/source marginals, all source ratio moments, nonnegative masses, and the selected observer submatrix rank 15. In all 49 cases, exactly one of the 16 arcs vanishes at each endpoint, giving a rank-15 (hence extreme) 15-arc transfer. Exact 30-tuples identify 58 unique endpoints. Exact adjacency graph construction over the 49 endpoint pairs gives degree counts 38 of degree 1 and 20 of degree 3, and component sizes $2,4,6,6,6,6,8,10,10$. Since vertices minus edges equals components ($58-49=9$), the sharp-only graph is a forest.

The actually executed expanded local verifier used Python Fraction and SymPy **exact** arithmetic. The observed output is archived in EXACT_OUTPUT.txt. It includes the terminal marker:

    PASS_EXACT_FIXED_FIBER_SHARP_INCIDENCE

The repository's VERIFY_FIXED_FIBER_SHARP_INCIDENCE.py is a condensed, separately published transcription of that same derivation and exact checks. Its own published bytes **have not been independently re-executed in this turn**, so do not conflate GitHub persistence with a separate completed run. No random search, tolerance-dependent LP, or uncertified numerical count enters the final theorem.

## BRC interpretation and follow-up

The carrier is labelled joint branch mass; the observer $C$ forgets internal allocations; each edge direction preserves a nonzero signed residual in $\ker C$. The result is a scoped exact fiber theorem: it is not a proof of redundancy under arbitrary future observers. Follow-up exact lemma: SOURCE3_SPARSE_SUPPORT_LEMMA.md proves every transfer in this one fixed fiber has at least four positive target arcs at source 3. It supplies an exact mass/moment gap explaining why source 3 cannot be a degree-three port. Next: derive the same sharp obstruction without the finite 35-triple census; explain the nine sharp-edge trees structurally; classify the **non-sharp** adjacent edges incident to the 58 vertices; preserve frozen scientific inputs when experimenting with new physical parameters.

The current native researcher registration and active-owner read were attempted but returned BACKEND_IDENTITY_CHECK_UNAVAILABLE. No formal R5 CLAIM, owner reassignment, independent Driver review, Source Result acceptance or P000 alteration is asserted.
