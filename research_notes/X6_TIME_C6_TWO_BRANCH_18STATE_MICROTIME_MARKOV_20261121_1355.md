# X6 native time — Unit234: exact 18-state C6 two-branch microtime and BRC provenance hierarchy

Date: 2026-11-21 (Asia/Hong_Kong). Task: `RS-X6-NATIVE-TIME-DYNAMICS`; registered publication `TP2-91D4A7C2F63805BE21A3`. Original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, own Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / NOT_REVIEWED / NOT_ADMITTED. This is a source-defined native path *possibility* model, not a new physical branch-selection or precision-fiber dynamics law.

## Original sources and objective

- Frozen P000 V5: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; 6D signed native Cell torsor, primitive signed unit-axis steps, time orders relational changes, and BRC provenance must be retained until observer-safe.
- Frozen constructive source: same commit `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`, §§4–7, 11–13. Each of the six adjacent shell macro-edges in the selected centered three-axis STAR has *exactly two* shortest two-step native realizations, via the pivot (INNER) or the nonzero sum Cell (OUTER). The all-OUTER branch is the actual proven selected C12 native microcycle; arbitrary mixed branches are **possible primitive paths**, not known permitted physical trajectories.
- Frozen `research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md`: relative root selection ±3 is static at fixed sweep chirality; no physical precision transfer is supplied. This result does not alter it.
- Prior Unit227 path provenance and Unit233 S6-reflection conditional holonomy are consumed, not republished. The current open target is the *minimum native time state* that distinguishes real native Cell changes from history and precision refinement.

## Exact six-axis-native Cell data

Choose an actual pivot Cell anchor and embed the selected three-axis slice in the full X6 signed torsor. Write
\[
a_0=e_1,\quad a_1=e_2,\quad a_2=e_3,\quad
a_3=-e_1,\quad a_4=-e_2,\quad a_5=-e_3,
\]
with indices `r mod 6` and all omitted signed components zero under **slice membership**, not a global dimensional collapse. For the adjacent shell step `a_r -> a_(r+1)` there are precisely two native paths
\[
{\rm INNER}:\;a_r\to0\to a_{r+1},\qquad
{\rm OUTER}:\;a_r\to g_r:=a_r+a_{r+1}\to a_{r+1}.
\]
Each arrow is one signed primitive axis step. The six `a_r` are distinct, the six `g_r` are distinct, and `0` is the same native pivot for all INNER paths. Hence **13 distinct spatial Cell positions** are visited across the whole unrestricted two-branch local population: six shells, six outer gates, and one pivot. The pivot is a chosen spatial Cell, not an ontic origin or an extra axis.

## Theorem A — minimal current-and-future Cell Markov carrier is exactly 18 states

Define a typed microtime state set
\[
\mathcal T=\{S_r,I_r,O_r:r\in\mathbf Z/6\mathbf Z\}
\]
with current Cell outputs `c(S_r)=a_r`, `c(I_r)=0`, `c(O_r)=g_r`. Its native event transitions are:
\[
S_r\to I_r\ \text{or}\ O_r,\qquad
I_r\to S_{r+1},\qquad O_r\to S_{r+1}.
\]
The branch at `S_r` is an explicit nondeterministic *BRC alternative*, not a presumed physical stochastic weight or deterministic law. Both alternatives consume **two** primitive microsteps per macro-edge. The first half of a macro-edge chooses its intermediate Cell; the second is forced to the scheduled shell destination.

For the observation horizon comprising the *current spatial Cell* and all possible *future native Cell observations under the specified transitions*, `mathcal T` is an exact minimal sufficient Markov carrier. Sufficiency is immediate from the displayed transition law and output function. Necessity: all six shell outputs are distinct and have signed-axis component-square norm one; all six outer gate outputs are distinct and have component-square norm two; these differ from the pivot. Thus all states except the six `I_r` are separated by their **present Cell** observation. The six `I_r` have the same current output `0`, but their uniquely forced next outputs are the six distinct `a_(r+1)`. Therefore every pair of distinct states is distinguished by a current/one-step-future Cell observation. No smaller deterministic labeled-state quotient can preserve this declared observable transition interface.

Consequently:
\[
\boxed{|\mathcal T|=18,\quad B_{\rm live}=\lceil\log_2 18\rceil=5\text{ bits}.}
\]
**Observer boundary:** this is minimal for current/future Cell observations and permitted branch choices. It is not sufficient to recover already elapsed BRC branch history or a putative internal precision fiber; the arbitrary physical branch-selection law remains unproved.

## Theorem B — exact BRC ambiguity at fixed elapsed microstep count

Start at `a_0`, follow the fixed six shell edges clockwise and repeat the circuit `W\ge1` times. Put `M=6W`. Each macro-edge independently has the two frozen native shortest realizations; the resulting population contains exactly `2^M` **distinct ordered native Cell microtraces**, all with:
- the same initial and final spatial Cell `a_0`;
- the same ordered sequence of `M+1` shell Cell reads at every *even* microstep;
- the same physical primitive **event count** `2M=12W`;
- different INNER/OUTER observations at some odd microstep whenever branch words differ.

Distinct branch words give distinct odd-step Cell outputs `0` or `g_r` at their first disagreement. The full path-provenance observer therefore needs exactly `M=6W` binary bits, attained by the branch word. Neither endpoint, event count nor sampled shell-only C6 phase reconstructs it. More generally, when the observer asks only for total pivot visits `J`, then
\[
\#\{\text{histories with }J=j\}=\binom{M}{j},\quad
j=0,\ldots,M,
\]
and the *pivot-count-only* observation has exactly `M+1` outcomes, so it needs `\lceil\log_2(M+1)\rceil` bits. These are **different scoped BRC observers**: Boolean visited-pivot, total count, full ordered provenance and signed/phase-fiber readout may not be conflated.

On the frozen source's *strict nonzero intermediate phase C12 native-lift lease*, only the unique all-OUTER branch word is eligible among these `2^M` paths. This is not a claim that the law of physical motion selects it. The all-OUTER restricted 12-state C12 clock and the unrestricted 18-state two-branch microtime automaton address different populations.

## Executed certificate

`research_checks/X6_TIME_C6_TWO_BRANCH_18STATE_CHECK_20261121.py` and `research_checks/X6_TIME_C6_TWO_BRANCH_18STATE_RESULTS_20261121.json` enumerate the 18 live states and distinguish every pair through current/next Cell, verify all native axes of the 12 local micro-arrows, enumerate all `2^6=64` and `2^12=4096` distinct native branch paths for `W=1,2`, and compare every exact pivot-count multiplicity with its integer binomial coefficient. Results: 13 distinct physical Cells, 18 minimal live states, 0 mismatches; for `W=1` pivot multiplicities `1,6,15,20,15,6,1`; for `W=2` the binomial `M=12` row. The symbolic arguments above hold for every `W\ge1`; the finite checks independently exercise the defined interfaces.

## Original mother-objective boundary and next discriminating action

**Established here:** a concrete, fully native-signed and source-grounded 18-state minimal present/future Cell microtime tool, with quantitative BRC history loss and a strict outer-only C12 observer lease. The construction respects six spatial dimensions, no seventh spatial axis, and keeps physical event count distinct from phase, provenance and precision/root level.

**Not established:** whether the actual X6 rotation/triadic law permits each INNER choice, selects OUTER deterministically, or couples a physical Port/Link/internal/precision fiber to intermediate Cells. No new physical fiber update, independent C12/C24 readout, triadic closure rule or R063 original six-file native benchmark was executed. Independent Driver review/Result admission remains open.

Next: inspect a *genuine frozen native rotation or Port transition rule* with declared branch admissibility, then restrict this 18-state carrier to its **reachable** population and recompute its exact minimal observer quotient, while retaining provenance and original R063 benchmark as distinct obligations. If no such physical transition law exists in admissible frozen sources, preserve the 18-state conditional full-branch and 12-state all-OUTER results as **separate proven observer scopes**, and record the missing update/observer data rather than inventing dynamics.
