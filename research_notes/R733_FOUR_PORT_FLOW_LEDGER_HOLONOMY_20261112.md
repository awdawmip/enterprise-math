# R733 — Four-port V29 cumulative ledger recovers BRC arc counts on both optimum carriers

Date: 2026-11-12 (Asia/Shanghai). Scope: exact positive BRC candidate count-event model; mathematical author result, not native force-law acceptance. Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Frozen parent science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. P000 is unchanged. Separately declared V29 candidate `PASS` grammar: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` @ `30fb16d39465708fd1b54c70a58d06ad20f310f8`. Previous author results: [R731b PR #2119](https://github.com/awdawmip/enterprise-math/pull/2119), [R732 nonabelian PR #2124](https://github.com/awdawmip/enterprise-math/pull/2124). Their author-side standing is not an independent Result.

## Exact question

R731b assigned each of the fifteen directed triad arcs `e_i`, in the original 60-arc universe order, a fixed ordered **two-PASS** word
[
  j(e_i)=(\lfloor i/12\rfloor,\ i\bmod 12),\quad 0\le i<15.
]
There are twelve off-diagonal local V29 port pairs, indexed `0..11`. Both PASS letters increment their corresponding **same cumulative** counter. Let `n=(n_0,...,n_14)` be the nonnegative *arc multiplicity* vector of an ordered BRC history, and `Y\in\mathbb N^{12}` the final ledger increment. Its exact linear readout is `Y=Cn`, with
[
 C_{r,i}=[r=\lfloor i/12\rfloor]+[r=i\bmod12].
]
The two letters must be added into a **single** counter array; retaining position-separated counters would be a different observer.

Let `B_E` be the directed vertex-incidence matrix of carrier E: for arc `u>v`, the corresponding column is `-1` at u and `+1` at v. For any path beginning at `s` and ending at `t`, `B_En=\delta_t-\delta_s` (zero for a closed path). The two networks are the R730 15-arc carrier masks in the 60-arc 3-subset graph on labels `0,1,2,3,4`:
- A: `211733226574`;
- B: `5363347296468`.
These labels describe an abstract subcarrier of six-axis X6, not an added spatial axis or a P000 force event.

## Theorem A — A terminal triad repairs the four-port aggregate, for every path length

For **both** R730 carrier A and B,
[
oxed{\ker_{\mathbb Q} C\cap\ker_{\mathbb Q}B_E=\{0\}.}
]
Thus `(Y,s,t)` **uniquely determines all fifteen arc counts** for every finite valid directed history, including rooted cyclic nonbacktracking (CNB) histories. The result is exact for arbitrary length and arbitrary nonnegative arc multiplicities consistent with endpoint flow, not merely the finite verifier's horizon.

A stronger integral certificate is available. Form the 15-by-15 matrix `T_E` by stacking all twelve rows of `C` and the three vertex-balance rows indicated below:

| Carrier | Chosen balance vertices | Exact det(T_E) |
|---|---|---:|
| A | 012, 013, 014 | -2 |
| B | 012, 013, 123 | +2 |

These determinants come from exact integer fraction-free elimination. In particular, the restricted linear map from integer arc counts to `(Y,B_E n|_{selected})` has index 2. Since `\sum_rY_r=2\sum_i n_i` and the target even-parity sublattice also has index 2, the exact image lattice is **precisely** the vectors with even total `Y` (when the selected three balance coordinates are otherwise arbitrary). Integer recovery from any such algebraic data is unique. For *actual directed path* realizability, the remaining balance rows, nonnegativity and allowed arc-order constraints still apply.

**Proof:** Write `n,n'` for histories with equal ledger `Cn=Cn'` and the same start/end triad. Then `B_E(n-n')=0`. The corresponding differences annihilate `T_E`. Since its determinant is nonzero, `n=n'`. The index-2 assertion follows from the determinant and the parity containment. No bounded-length argument is needed. The standalone verifier reconstructs the full matrices from the published masks and recomputes both exact determinants.

## Theorem B — Three residual states now suffice *also* for the four-port/two-PASS code

Let the retained observer be `(s,t,Y)` together with a three-valued residue `k\in C_3`, in a streaming implementation also retaining the current active triad and codeword phase while an event word is processed. By Theorem A the completed-word endpoint and full twelve cumulative V29 counters determine the **exact arc-count vector** `n`. R732 established the local V17 slot permutation sign homomorphism:
[
 \epsilon(h)=\sum_e n_e\epsilon(p_e)\pmod2.
]
Therefore the sign of the final named V17 frame permutation is recovered from `Y,s,t`. In `S_3=C_3\rtimes C_2`, the remaining component is `k\in\{0,1,2\}`. Updating the frame by each typed source-state indexed V17 arc permutation determines the new three-cycle residue, using the recovered sign from the running counts. Hence **three states are sufficient** to reconstruct final named V17 holonomy from completed four-port ledger and endpoints over *all finite valid histories*, not just the five-port count-injective code.

They are also **necessary** on the same declared carrier families: R732 PR #2124 exhibited six rooted seam-legal length-12 CNB histories built from the same four excursions `{X,X,Y,Y}`, which share identical complete arc multiplicities and therefore identical `Y`, yet realize all three even named holonomies `012,120,201`. The exact cardinality lower bound is 3, attained by `k`.

**Scope:** The above is a *minimal number of states for final named-holonomy recovery given complete word boundary, current/terminal triad, and cumulative ledger*. A standalone sequential PASS decoder still needs word-boundary and current-state management. No claim is made that a finite register recovers the full historical path order or an absolute V29 ledger from a contrast-only observer. The 4-port coding is a declared coupled candidate transducer; no genuine `TRIADIC_CLOSURE_E` signed-force certificate, independent review, Source formal CLAIM or Result is inferred.

## Exact verification

The accompanying `R733_FOUR_PORT_FLOW_VERIFY.js` constructs the 60-arc universe, both 15-arc masks, exact `C` and signed incidence `B`, then evaluates the two full 15-by-15 determinants with integer Bareiss elimination. It also enumerates all rooted nonbacktracking path prefixes up to 10 arcs, compares every `(t,Y)` fiber's full multiplicity vectors, checks positive count grades, and directly verifies the six ordered `{X,X,Y,Y}` holonomy witnesses from the two fixed R732 excursion pairs. Results are written as `R733_FOUR_PORT_FLOW_RESULTS.json` with status `PASS` on validation. These finite tests corroborate but do not substitute for the all-length determinant proof.

## Residual and next executable question

R732 left the four-port three-state **sufficiency** unproved because `Y` seemed coarser than arc counts; this result supplies the missing graph-flow repair **at no additional arc-count register cost** when both endpoints are retained. The next unit should connect one **genuine frozen P000** three-signed-source `TRIADIC_CLOSURE_E` Cell/Link/Port certificate and V29/V39 scheduler to the source-indexed PASS coupling, then test whether the candidate flow and holonomy observers survive that *actual native event constraint*. This proof does not pre-admit a physical triadic closure, does not rebase frozen inputs and does not modify P000.
