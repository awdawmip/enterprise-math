# R720 — Three-tag-local BRC triad source recovery: optimal fixed four versus adaptive three queries

**Status:** author-side mathematically proved linear statements + complete finite exact integer computation; not a native Result, independent review, or verified legal X6 dynamic event.
**Parent task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`. **Frozen scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Predecessor R719: Draft PR #2083, `2026-11-11_R719_BRC_TWO_AXIS_LEDGER_TWO_PROBE_THEOREM.md`.
**Original researcher:** `EM-X6-562B89`, activity `RA-0876B79D7B866702F881CB83`. No formal CLAIM or task semantic checkpoint.

## Model and observer

Let \(V=\{0,1,2,3,4,5\}\) be *identities of X6 native axes*. Candidate BRC source carrier: the Boolean identity tuple \(h=(h_T)_{T\in\binom V3}\). The observer records exact integer counts \(D_{ij}(h)=\sum_{T\supset\{i,j\}}h_T\) for all 15 unordered pairs. The allowed future operation is: given verified old \(h^{(0)}\), an update changes only triads meeting **one of three known distinct event tags** \(A=\{0,1,2\}\); \(h^{(1)}_{345}=h^{(0)}_{345}\). Exact new \(D\) and permitted single-triad membership queries are available. There are \(20-1=19\) potentially changed source bits. All new results are covariant under simultaneously permuting the six axis labels, tags, ledger rows and query locations.

The algebra treats distinct labeled candidates as BRC branches and sums their Boolean occupancies; it does not use a classical propagator or physical force calculation. Signed source attributes, Cell/time/Link/Port identity and V29/V39 dynamics remain separately typed.

## Theorem R720.1 — exact linear deficit is four

Let \(A_U\in\{0,1\}^{15\times19}\) be the pair-triple incidence matrix with lexicographically sorted edge rows and all triple columns except 345. Then
\[
\operatorname{rank}_{\mathbb Q}(A_U)=15,\qquad \dim_{\mathbb Q}\ker A_U=4.
\]

**Proof:** For the full 15×20 incidence matrix \(A\), a row relation \(y^\top A=0\) says \(y_{ij}+y_{ik}+y_{jk}=0\) on each triple. Fix \(k\ne l\), and set \(d_i=y_{ik}-y_{il}\) for each of the other four vertices. Subtracting the triple equations for \((i,j,k)\) and \((i,j,l)\) gives \(d_i+d_j=0\). Using any three distinct vertices among those four forces each \(d_i=0\). Thus \(y_{ik}\) is independent of \(k\ne i\); symmetry makes all \(y_{ij}\) equal, and a triple equation forces the common value to be zero. Hence \(\operatorname{rank}A=15\), \(\dim\ker A=5\). The Pasch difference
\[
\{012,034,135,245\}-\{013,024,125,345\}
\]
is in \(\ker A\) and has nonzero 345-coordinate. Intersecting \(\ker A\) with the hyperplane \(z_{345}=0\) therefore reduces its dimension by one. This intersection is exactly \(\ker A_U\), proving the claim. □

## Theorem R720.2 — four fixed queries suffice

Query the four source bits \(h^{(1)}_{013},h^{(1)}_{014},h^{(1)}_{023},h^{(1)}_{024}\). Subtract from each of the 15 new ledger rows the **known unchanged** source 345 contribution, then subtract contributions of these four queried bits. The remaining 15 unknown bits solve the explicit 15×15 system
\[
A_{U\setminus Q}\,x = D(h^{(1)})-A_{\{345\}}h^{(0)}_{345}-A_Qh^{(1)}_Q.
\]
In lexicographic row/column order, the square incidence matrix has determinant **96**, so this is an *exact, unique rational solution*. For an actually admissible Boolean source state its entries are necessarily zero or one. For a candidate ledger use this unique solution and check each bit is Boolean and that all 15 ledger counts match. This gives a direct full-source decoder with four nonadaptive probes for any change pattern among the 19 allowed bits. □

## Theorem R720.3 — exact optimal query complexities

Using the 19-bit interior source states and fixed outside bit, the complete finite census is:

| Source configurations in an exact pair-count fiber | Number of fibers |
|---:|---:|
| 1 | 492,428 |
| 2 | 13,308 |
| 3 | 1,392 |
| 4 | 216 |
| 5 | 36 |
| 6 | 4 |

There are **524,288** configurations, **507,384** distinct pair ledgers, **19,200** colliding unordered state pairs and only **15** distinct symmetric-difference support sets (nine of size 8 and six of size 12).

**Fixed-membership queries:** Let \(\mathcal S\) be the 15 difference-support masks from the actual collisions. A chosen query set \(Q\subseteq U\) distinguishes all states iff \(Q\cap S\ne\varnothing\) for each \(S\in\mathcal S\). Complete enumeration of all \(\binom{19}{k}\) candidate sets for \(k=0,1,2,3,4\) gives zero successful sets for \(k\le3\) and **1,296** successful sets for \(k=4\). Together with R720.2 this proves \(Q_\mathrm{fixed}=4\).

**Adaptive membership queries:** For each of the 507,384 source fibers, recursively minimize the maximum depth of valid source-membership decision trees; a leaf is a singleton state. The full census of optimal depths is **492,428 at depth 0, 13,308 at depth 1, 1,608 at depth 2, and 40 at depth 3**. In particular all fibers admit a 3-query tree; the four fibers with six states require at least \(\lceil\log_2 6\rceil=3\) Boolean answers. Hence \(Q_\mathrm{adaptive}=3\).

The maximal 6-state fiber also proves that the minimum additional **arbitrary** fixed-length code after observing the exact ledger uses three bits, \(\lceil\log_2 6\rceil=3\). This arbitrary code need not consist of three preselected membership bits.

The statements about optimal fixed/adaptive queries are **exhaustive finite combinatorial proofs for this 19-bit Boolean model**, implemented by the attached verifier, rather than inferred from a real-valued rank computation. The determinant/rank claim additionally has the algebraic proof above.

## Verified evidence

Execute `python R720_BRC_THREE_AXIS_LEDGER_VERIFY.py` (Python 3 standard library). Integer Gray-code enumeration visits exactly \(2^{19}\) distinct states and records a base-5 packed pair ledger (all individual pair counts are at most four, hence no radix carry). It computes all collisions, their exact support masks, all 969 three-query and all 3,876 four-query sets, all exact adaptive decision trees, the 15×19 rank and the quoted determinant. Machine-readable expected results: `R720_BRC_THREE_AXIS_LEDGER_EVIDENCE.json`. Verified local run: `R720_BRC_THREE_AXIS_LEDGER_EXACT_PASS`. No numerical tolerance or sampling was used.

## Next test: real X6 event

Read exact frozen scientific references and locate *one* lawful signed/timed Cell/Link/Port update with V29 PASS/TRANSFER and V39 loop \(j\). Explicitly list before/after **native** triadic identities, count observer rows, and changed-source support. Determine whether the support belongs to a known single-, double- or triple-tag star, and whether fixed source queries are legal native observations. This native mapping and event admissibility are the outstanding bridge; the present theorem supplies the precise candidate observer/repair interface rather than assuming the bridge.