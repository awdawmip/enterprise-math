# Stage285-B — upstream-dependent occupancies and the shared-port moment quotient

**Research status:** proposed portable author handoff; `UNREVIEWED / NOT_ADMITTED`. Parent: Stage284-B positive-rational non-IID DAG; independently open: Stage278-A N=12 Bellman next-face.

## Exact verified input to reuse, not redo

Stage284-B scientific commit in Draft PR #1571, directory `research_notes/n12_aux_iid_stage284b_shared_port_conic_20261029_RESEARCH2/`, contains full proof, Fraction enumeration, executed stdout and this next packet. Two positive nonIID sources with `Pr(R=0)=Pr(R=1)=1/2`, `Pr_P(S=0|R=0,1)=(1/4,3/4)`, `Pr_Q(S=0|R=0,1)=(1/3,2/3)`; a single shared Bernoulli parameter y is sampled twice after each `(R,S)` observation. Its exact route observer has true fixed-policy max reward 1/2, independent route-wise moment cone relaxed max 5/8, gap 1/8. For any fixed positive route weights `w_j`, the exact convex hull of shared-port moment lifts `(z_j=w_j y, v_j=w_j y²)` consists of **one shared** `m1,m2` with `0≤m1≤1`, `m1²≤m2≤m1`, and `z_j=w_jm1`, `v_j=w_jm2` for all j. Source/readout scope is finite positive rational ordered paths and affine terminal observers; no native X6 bridge or canonical theorem acceptance.

## New research question and first exact discriminating experiment

Introduce an upstream, source-blind binary control `x∈[0,1]` *before* choosing/observing the downstream route, so that reach masses `w_{i,r}(x)` are positive-rational affine expressions in x (or use an explicit stopping mass when a weight vanishes at endpoints). Then visit the **same source-blind y port twice** after any surviving route. The candidate lift contains `z_{i,r}=w_{i,r}(x)y`, `v_{i,r}=w_{i,r}(x)y²`, so normalized moment consistency across routes/source is no longer an affine constraint in `(x,z,v)`; correlations between the upstream and downstream policies may matter in ex ante mixtures.

Find a finite complete nonIID ordered-path model and one bounded terminal observer for which (i) separate per-route conic hulls are provably loose, or (ii) imposing only common normalized first/second moments remains loose under mixture because the x-dependent occupancy map is not preserved. Compute the precise rational continuous optimum gap using a valid algebraic global bound or present a scoped exact factorization theorem ruling out a gap for a nontrivial subclass. Do not label finite grid agreement as a universal result. Distinguish fixed shared `x,y`, ex ante mixtures of entire global settings and history-adapted fresh settings; do not silently enlarge the policy class.

## Evidence and completion

Give the full two-source positive rational input law, ordered branch/source/port IDs and horizon, all terminal mass formulas, bounded observer, exact optimal value or obstruction, proof for the **whole** real parameter domain, exact source-tagged Fraction DFS (record actual stdout), separate next unit, and author-versus-independent/native acceptance status. BRC first-line: keep positive mass/repeated branch provenance and the joint observer/future-operation scope. P000/ACTIVE native X6 work requires a separate registered full six-field codec, typed time and path/port relation-preserving mapping. Preserve the unrelated Stage278-A Bellman next-face problem rather than claiming it closed.
