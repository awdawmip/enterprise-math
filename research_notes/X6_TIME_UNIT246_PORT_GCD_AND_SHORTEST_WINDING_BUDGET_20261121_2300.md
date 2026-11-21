# X6 native time — Unit246: directed-centre Port gcd conservation and exact shortest-history budget

Date: 2026-11-21 23:00 Asia/Hong_Kong.
Status: **AUTHOR_PROVED / SOURCE-CERTIFICATE-REPLAYED / UNREVIEWED / NOT_ADMITTED**.
Task: `RS-X6-NATIVE-TIME-DYNAMICS` / `TP2-91D4A7C2F63805BE21A3`, parent `PO-X6-UPPER-STRUCTURE-20260906`.
Original author-side lane provenance: `chatgpt-research-onhour-enterprise-math-20260923`, `EM-X6-FB6990`, historical SID `MCP-082892eb480e45dea6d4b9fcc0491034`. These historical identifiers do not assert a newly won live CLAIM.

## Source and object

Consume the frozen `P000` signed native X6 Cell torsor @`a72226e2430ffa4786321ac86e7f0c599d5f0389`, the existing 12-Cell OUTER lift, mandatory full BRC chronology and Unit242's two-triad ring exclusion theorem. The exact 36 source cases and full shortest-route strings are in the existing immutable Unit245 result certificate [at this source pin](https://github.com/awdawmip/enterprise-math/blob/f56840285cafeb9f5767ea91e903e1f53808186f/research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json).

Use the same **conditional** whole-triad target-empty serial model as Unit245. The original signed ring edges `x_k ↔ x_(k+1)` remain available; the only centre transfers are `x_i→P` and `P→x_j` with even i,j. Two labelled intact triads start and finish at `(x0,x2)`. Their net *original ring* signed increments are exactly `L_A=-12`, `L_B=+12`. Centre events retain their own signed primitive X6 Cell step and count zero toward ring winding. This conditional model does not postulate an admitted physical Port law.

## Theorem 1 — modular closure and minimum mandatory Port usage (all legal histories)

Let `d=(j-i mod 12)` and `m(d)=12/gcd(12,d)` (in particular `m(0)=1`). For a labelled triad T, let `c_T` be the number of its completed centre excursions `x_i→P→x_j`; let `n_T^+` and `n_T^-` count its forward and reverse original ring edges.

Because the triad finishes at its starting ring Cell, native Cell index conservation gives

\[
n_T^+-n_T^-+d\,c_T\equiv0\pmod{12}.
\]

For the specified closed target `L_A=-12,L_B=+12`, this becomes

\[
\boxed{d\,c_T\equiv0\pmod{12},\qquad m(d)\mid c_T.}
\]

At least one centre excursion is needed: if both `c_A=c_B=0`, the Unit242 cyclic-order/exclusion invariant prohibits opposite winding on a single fully guarded ring. Therefore

\[
\boxed{c_A+c_B\ge m(d).}
\]

In particular offsets `d=±2` require at least **six** centre excursions (**12** signed centre events), while `d=±4` require at least three, and `d=6` at least two. This is a non-enumerative arithmetic obstruction even before source-specific Port guards are tested.

## Theorem 2 — exact nonnegative event-cost decomposition (all legal histories)

For each T, define `R_T=n_T^++n_T^-` and `b_T=(R_T-|L_T|)/2`. Exact integer parity implies `b_T\in Z_{\ge0}`: it counts ring-event excess in reversal pairs beyond the required net winding. With `c=c_A+c_B`, `b=b_A+b_B`, the complete chronological primitive event count is exactly

\[
\boxed{N=24+2c+2b,\qquad N\ge24+2m(d).}
\]

No replacement of an original signed step by a carrier jump is used; the quantities retain labelled Port occupancy, source/target Cells, event order and ring/centre event types. This lower bound is valid under the declared Port model irrespective of scheduling.

## New exact result for the 36 previously verified optimal routes

Replay every stored Unit245 **shortest** route in its original order. In all 36 cases, the exhibited shortest witness uses exactly `c=m(d)` excursions, all by one labelled triad, so the compulsory arithmetic Port budget can be reached **at the globally minimal cost**. The remaining cost is entirely ring backtracking:

\[
\boxed{N(i,j)=24+2m(j-i)+2b(i,j)}
\]

with the following exact nonnegative `b` matrix (rows ingress i, columns egress j; each ordered 0,2,4,6,8,10):

| i \\ j | 0 | 2 | 4 | 6 | 8 | 10 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2 | 1 | 3 | 5 | 4 | 5 |
| 2 | 1 | 2 | 5 | 4 | 5 | 3 |
| 4 | 1 | 0 | 3 | 6 | 4 | 2 |
| 6 | 0 | 0 | 2 | 5 | 4 | 2 |
| 8 | 0 | 0 | 2 | 4 | 5 | 2 |
| 10 | 0 | 1 | 2 | 4 | 6 | 3 |

This is an **existence result about the stored optimal witnesses**, not an assertion that every tied shortest route must use the same allocation.

Immediate sharp observed consequences in the declared model:
- A native-event budget below **36** excludes every gateway whose entry-to-exit offset is ±2, by the modular theorem alone.
- The exact 28-event optimum is possible only at the already certified (i,j)=(6,0) and (8,2), both `d=6`, where `m=2` and `b=0`.
- Zero-backtracking shortest witnesses also occur for (4,2), (6,2), (8,0), and (10,0), with different minimum compulsory centre excursion counts. A zero-backtracking witness need not be a 28-event witness.
- The most expensive exact 48-event cases are (4,6) and (10,8): both have `m=6,b=6`. Their extra twelve ring events are trace-dependent resource detours, not additional Port traversals.

## Verification and active physical admission boundary

The executable JS checker replays the 36 original immutable complete BRC strings; it checks labelled native Cell occupancy, each signed one-axis step in the selected X6 slice, declared Port orientation, signed ring winding, exact return, `m|c_T`, minimal attained excursions, and the nonnegative budget decomposition. The result file records the per-pair counts and an independently inspectable 6×6 residual matrix. **Actual in-session V8 exact integer checks: 5755, no assertion failures**. It reuses Unit245's separately executed exhaustive FIFO certificates for the statement that the input strings are shortest; this new replay is not a new BFS shortestness proof.

The newer 2026-11-18 positive-direction whole-triad candidate `research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md` allows only +E_i transfers and has no physically admitted environment update. Unit240's exact signed-Port obstruction still rules out executing the necessary reverse ring steps under that candidate; the mathematical offset cost table is therefore a **screening certificate for a future Source-admitted signed-Port rule**, not a physically executed experiment.

Next genuine science: acquire a physically Source-admitted signed whole-triad Port transition/guard including specific `x_i→P` and `P→x_j`; use the modular lower bound to reject nonviable event budgets immediately, then replay only actually admitted directed edges of the corresponding Unit245 BRC sequence with the real environment response. Independently observe a same-labelled-Cell pre/post C12/C24 precision fibre. The original R063 six-file native benchmark belongs to the distinct `RS-X6-LEGACY-PLANE-RECONCILIATION` task and is not replaced by this certificate.

Earlier Units233–245, their Source artifacts and Activity246 remain consumed without rewriting. Original terminal failed native PROGRESS/typed prepares remain unchanged; the protected Native semantic PROGRESS is pending actual winning Source authorization (support #2903). This work is `UNREVIEWED / NOT_ADMITTED`.
