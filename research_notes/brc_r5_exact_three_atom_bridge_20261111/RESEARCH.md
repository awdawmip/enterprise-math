# R5: sharp three-atom A→B bridge under the optimal five-support bound

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact rational theorem and exhaustive certificates; formal independent review and canonical Source Result admission pending.

## Scientific object and provenance

Continue immutable R5 predecessor [PR #2076](https://github.com/awdawmip/enterprise-math/pull/2076), source commit `ad38b1e68cfffc72af315024e2772d980747e3e4`, especially `research_notes/brc_r5_atomic_support_bridge_cb_ab_20261111/VERIFY_BRIDGES.py`. The frozen auxiliary P/Q–BRC Blackwell scientific pins remain: GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current operational rules are separately refreshed; P000 and native X6 semantics are unchanged.

There are 28 dynamic arcs `(target i, source port j)`, with `i=0,...,6` and `j∈{1,2,3,5}`, plus two unchanged positive singleton arcs `(0,0),(6,6)`. The seven exact likelihood parameters are `R=(2,10,15,20,25,30,38)`. The exact observer `A` has 15 target/source-total/first-moment rows of rank 13; the right-hand side `b` comes from the pinned strictly positive reference transport. All work is inside the fixed nonnegative observation fiber:

\[
\mathcal F=\{x\in\mathbb Q_{\ge 0}^{28}:Ax=b\}.
\]

Define the positive target masks at source port 3:

\[
A_\mathrm{mask}=\{1,3,4,6\},\qquad
B_\mathrm{mask}=\{2,3,4,5\}.
\]

An atomic operation moves along a signed six-arc `K_(2,3)` kernel direction: choose source compensator `j∈{1,2,5}` and a triple of labeled targets, put a weighted zero-sum/zero-first-moment three-vector on source 3 and its negative on source j. The operation's open line segment must be nonnegative. Peak support counts the union of *positive source-3 target labels* on all open segments. Both endpoints may vary inside the original fixed fiber.

## Theorem: exact minimum of three atoms

\[
\boxed{N_{\mathrm{atomic}}(A_\mathrm{mask},B_\mathrm{mask};\,\mathrm{peak}_3\le5)=3.}
\]

**Constructive upper bound.** The compatible exact rational path from PR #2076 uses successive compensator sources 1, 2, 5 and positive multipliers

\[
t_1={1544855\over475661816},\qquad
t_2={196521\over67951688},\qquad
t_3={226755\over8493961}.
\]

Its source-3 masks are

\[
\{1,3,4,6\}\to\{1,2,3,4,6\}
\to\{2,3,4,6\}\to\{2,3,4,5\}.
\]

The precise 28 rational initial masses are in the inherited `VERIFY_BRIDGES.py` text at the head of `VERIFY_R5_SHARP_ATOMIC_BRIDGE.py`. The verifier checks all 15 exact observation equations, nonnegative masses at each stage, each atom's kernel identity, every positive multiplier, and five-support unions. This establishes `N≤3`. A single triple-supported atom cannot alter all four members of `A_mask △ B_mask={1,2,5,6}`, hence `N≥2`.

**Lower bound, finite exhaustive proof.** Suppose a two-operation path exists with peak at most five. At the first segment, at most one target not in `A_mask` can become positive; at the second segment, the intermediate state has at most one target not in `B_mask`. Every source-3 state must have at least four positive targets in this frozen fiber: for every one of the \(\binom73=35\) potential triples, its total mass, likelihood-ratio first moment and per-target capacity bounds give an empty rational interval, independently checked by the verifier. The first atom must introduce exactly one of the new targets `2,5`; it cannot introduce target `0` because the final atom would still have to alter four other target labels.

The remaining two-step support behaviors form two exhaustive classes:

1. **Type I: exchange one old for one new.** The first atom removes `old1∈{1,6}` and creates `new1∈{2,5}`, the second removes the other old and creates the other new. First atom's third target is in `{3,4,other-old}`, second atom's third target is in `{3,4,first-new}`. Exact moment sign conditions select 18 ordered triple patterns. Each has 9 ordered compensator pairs `(j1,j2)∈{1,2,5}²`: 162 cases.
2. **Type II: introduce one new while retaining both old.** The first atom uses one new target and two of the four initial positive targets, with no old target removed, and the second atom necessarily removes both old targets and introduces the other new using the triple `{1,6,other-new}`. This yields 12 signed ordered triple patterns and 108 ordered compensation-port cases.

The possibility of removing both old targets in the first step would leave at most three positive targets, contrary to the exact 35-triple result. A first-step removal of a common target cannot satisfy the two five-support open-segment bounds and the final three-target change budget. A first-step atom that removes one old and creates both new targets is forbidden by its zero-mass/zero-first-moment constraints: `R[1]=10` and `R[6]=38` both lie strictly outside `[R[2],R[5]]=[15,30]`.

Thus exactly 30 signed target-triple patterns times 9 compensation choices, i.e. 270 feasible *combinatorial possibilities*, exhaust all two-operation legal paths. The proof checks their algebraic feasibility, without presuming strict positivity at the unknown endpoints.

For a candidate with signed kernel directions `H1,H2`, let `x` be its initial nonnegative transfer and `u,v≥0` its step magnitudes. The necessary linear system fixes the initial mask, terminal mask, `Ax=b`, and stagewise nonnegativity

\[
x\ge0,\quad x+uH_1\ge0,\quad x+uH_1+vH_2\ge0.
\]

A source-3-only necessary relaxation also imposes original per-target capacity `x_{i,3}≤b_i` at every stage. For each candidate write its equalities as `Ez=d`, inequalities as `Uz≤f`, with `z≥0`.

The attached exact Farkas certificates provide free rational multipliers `y` and nonnegative rational multipliers `λ` satisfying

\[
E^\top y+U^\top\lambda\ge0
\quad\text{componentwise},\qquad
d^\top y+f^\top\lambda=-1<0.
\]

This is inconsistent with the existence of any nonnegative primal solution. All 86 duals are explicitly saved, have nonempty exact rational entries, and are individually checked by Python `fractions.Fraction` arithmetic with no numerical tolerances:

| Proof family | Certificates | Coverage |
|---|---:|---|
| Source-3-only exact Farkas duals | 23 | 23 of 30 signed target patterns, irrespective of compensator port |
| Full labeled observation-fiber exact duals | 63 | Remaining 7 target patterns, all 9 compensator pairs |
| Complete exact coverage | **86** | **270 of 270** candidate two-step patterns |

A separate exact 35-case rational interval test excludes source-3 support 3 or fewer. Hence no valid two-atom path exists at peak 5; with the explicit three-atom witness the theorem follows.

## Reproducible machine evidence and execution scope

The research directory includes:

- `VERIFY_R5_SHARP_ATOMIC_BRIDGE.py`: standard-library Python verifier, incorporating exact original witness from PR #2076 and the new finite case/dual checker.
- `R5_TWO_ATOM_FARKAS_CERTIFICATES.json.gz.b64`: a complete lossless gzip/base64 representation of the **39,874-byte JSON** dataset containing all 86 rational duals and their case keys. Decode with `python3 -c "import base64,gzip;open('R5_TWO_ATOM_FARKAS_CERTIFICATES.json','wb').write(gzip.decompress(base64.b64decode(open('R5_TWO_ATOM_FARKAS_CERTIFICATES.json.gz.b64','rb').read())))"` if needed; the verifier directly reads the encoded file without a conversion step.
- `EXACT_OUTPUT_R5_20261111.txt`: actual local execution output of a standalone equivalent Fraction checker, before inlining the predecessor's exact witness. Both code paths use the same 270 cases and 86 duals.

In the directory run

`python3 VERIFY_R5_SHARP_ATOMIC_BRIDGE.py R5_TWO_ATOM_FARKAS_CERTIFICATES.json.gz.b64`.

The local standalone verifier finished with `PASS_R5_EXACT_86_DUAL_CERTIFICATES_AND_SHARP_THREE_ATOM_BRIDGE`, checking all dual products, contradictions and the original positive witness. The packaged inlined verifier itself should be rerun independently from its published GitHub bytes; source publication and author verification do not confer independent review or canonical Source result status.

The duals were discovered using an exploratory floating-point LP followed by exact rational reconstruction; mathematical validity of the published theorem rests only on the saved rational certificates, exact-complete finite case enumeration and the original witness. The theorem applies to the pinned auxiliary Blackwell observer fiber; it does not assert new original-native X6 dynamics, physical calibration or a P000 replacement.

## Next new mathematical objective

Determine the Pareto frontier if `peak_3≤6`: two atoms might become possible by allowing a wider intermediate positive support. A complementary proof direction is compressing the 86 exact Farkas duals into a symbolic parametrized capacity/cut theorem on a rational neighborhood of the frozen likelihood ratios and right-hand side. Preserve source/target labels and signed compensator port structure when changing the operating budget.