# X6 / LP011 — exact typed signed-dominance consumer contract on a selected native three-axis restriction

**Status:** AUTHOR_PROVED / EXACT_INTEGER_REGRESSION_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. This report is original scoped follow-up research, **not** the unlocated historical LP011 caller, a renewed historical Result, a formal native semantic checkpoint or a new CLAIM.

**Mother Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`. Historical scientific author `EM-X6P-40B5BD`; `HRI-1A48B2D7F0E242FCC2C57D7E` retains its originals and `HIRR-1C60C7CCFAE8636E82F43A76` remains `REQUEST_REVISION`. New mathematical author: ongoing TASK_RESEARCH Research lane, researcher `EM-ENTERPRISE-9C9163`; this work consumes prior results and is NONBLIND. The lane's conversation label is `chatgpt-research-onhour-enterprise-math-20260923`, distinct from control maintenance; a label alone authenticates no platform identity.

**Scientific pins:** signed centered-X6 source `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; old comparison source `@fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Current rules/P000 are read separately from frozen science. P000 retains native spatial X6, signed primitive axes, a separately typed time dimension and **no native plane**. This calculation is a fixed selected three-axis restriction, with omitted components *declared zero in this particular embedding*, not a blanket missing-is-zero convention, a complete layer model, a final six-field nonnegative Cell address, or a global rotation/transport theorem.

## Question and typed consumer

The existing 28-row LP011 ledger calls the old formula "dominant branch is max of a positive/min-zero normalized displacement" but omits its exact original independent consumer. The previously proved LP011 chamber and median-side results establish which signed state is lost. The new smallest needed question is: **for which raw signed inputs may the old positive maximum selector be reused safely as a proposed native dominant-axis/sign/tie readout, and does a properly typed selected-axis consumer commute with an explicit X6 embedding and existing native shortest-path BRC?**

For a selected ordered three-axis restriction `S=(0,2,5)` in zero-based six-axis indexing, define `iota_S: Z^3 -> Z^6` by filling exactly axes `S` with the three signed entries and setting the **other three entries to zero by definition of this restriction**. The outputs below are signed native raw-chart selectors, not public Cell addresses.

For `d in Z^3`, define `D3(d)={(i,sgn(d_i)): |d_i|=max_j|d_j|>0}`, with all ties included and `D3(0)=empty`. Define `D6` by the identical rule over six raw signed coordinates, again `D6(0)=empty`. This is a *proposed typed readout interface*, not a claim that the historical implementation used it. For `h=min(d)`, `a=d-h(1,1,1)`, `M=max(a)`, define the legacy candidate `L(a)={(i,+):a_i=M}` if `M>0`, and `empty` when `M=0`.

### Theorem A — exact legacy compatibility guard

For every `d in Z^3`, `D3(d)=L(a)` if and only if:

```text
(M > 0 and 2*h + M > 0) OR (M == 0 and h == 0).
```

At `M>0`, the existing signed chamber theorem gives the **positive** max-residual group when `theta=2h+M>0`, the **negative** min-residual group when `theta<0`, and both positive-max and negative-min groups when `theta=0`. The last two cannot equal the all-positive legacy selector; `min(a)=0<M` makes the groups disjoint, even with repeated extrema. At `M=0`, `a=(0,0,0)`, so `L(a)=empty`, while `D3(d)` consists of all three signed axes for `h != 0` and is empty exactly at `h=0`. This proves the complete if-and-only-if guard, including ties and zero. This result specializes and turns the existing chamber theorem into a **machine-checkable caller guard**, rather than reproving the older theorem as new general theory.

Example: `a=(0,2,4)`, `h=-2`, `theta=0` gives `D3={ (axis 0,-), (axis 2,+) }`, whereas `L={ (axis 2,+) }`. Zero and repeated-min/max cases are covered by the explicit set-valued definition.

### Theorem B — selected X6 embedding and exact BRC transport

For every `d in Z^3`, with coordinate injection `iota_S` defined above,

`D6(iota_S(d)) = { (S[i],sign) : (i,sign) in D3(d) }`.

Proof: When `d != 0`, the common positive absolute maximum is unaffected by inserting three zeros and all nonzero maximizers stay on the selected axes. At `d=0`, both output sets are empty. Thus the complete signed dominant-set readout, including zero and all ties, factors exactly through this **explicit restricted embedding**.

Let `N(d)=sum |d_i|` and `B(d)=N(d)!/product_i |d_i|!` denote the unweighted free shortest-coordinate-word BRC coefficient. Then

`N(iota_S(d))=N(d)=N(-d)`, and `B(iota_S(d))=B(d)=B(-d)`.

The first identity is immediate from three inserted zero components; the second uses `0!=1`, then sign invariance of absolute counts. The six-axis formula agrees with the **existing Source implementation** `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py:shortest_path_multiplicity`; that canonical module is read and reused rather than replaced. The theorem is for free unweighted shortest coordinate words only. Ordered word identity, weighted/channel-restricted paths and the other X6 axes under general dynamics require their own declared operators.

**Observer/caller consequence:** An old positive-max selector may be typed as a native signed-dominant readout only after proving the guard for its actual raw signed input population (or using `D3` directly). The historical `M=max(A,B,C)` at `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, frozen `fd2bcff...` blob `58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0`, lines 236–250, is the distinct **reverse min-zero decoder** `(M-A,M-B,M-C)`; it is not established to be an independent native LP011 selector. The 28-row historical ledger/return likewise provides a correction *description*, not an identified original LP011 calling site.

## Executed exact-integer regression and verified tool reuse

Checker: `research_checks/X6_LP011_TYPED_DOMINANT_CONSUMER_20261112.py`. Run locally using Python exact integers against all 3,375 selected signed triples `[-7,7]^3` with explicit noncontiguous axes `S=(0,2,5)`. For every triple, checks full `D3/D6` set transport, old `(a,h)` chamber readout, native reversal, exact iff guard, three- and six-axis factorial BRC and reversal symmetry. This covers 644 tied-dominance triples and the unique zero triple.

The run also imported the **unchanged actual Source `signed_brc.py` bytes** fetched through GitHub, compared its Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176` to Source, and executed its existing `shortest_path_multiplicity` unchanged for all 3,375 six-axis embedded triples. Thus `REUSE_EXECUTED` for this exact BRC interface. Additional exact witnesses: `a=(0,1,4)` with signed `d_-=(-2,-1,2)` has BRC 30 and `d_+=(0,1,4)` has BRC 5, both sharing relative observer `a` and shortest length 5; the proven median-sign recovery theorem remains a distinct earlier result.

Observed local result:

```json
{"LP011_status":"bounded proposed typed consumer; historical original caller not located","brc_shortest_formula_checks":3375,"existing_native_brc_calls":3375,"existing_native_brc_imported":true,"legacy_selector_agreement":1513,"signed_points":3375,"signed_ties":644,"status":"PASS","three_axis_embedding":[0,2,5],"zero_cases":1}
```

Exact symbolic proofs cover every input of the defined `Z^3` restriction; finite enumeration checks the implementation only. This checker was executed locally, not on the remote Source host.

## Source audit, open obligations and exact next action

Actually inspected, by full exact file reads: frozen original 28-row ledger/Result on branch `a0bfa8eace20b061f5b228c733acdc46221388d7`; historical and current R061 directed gauge, old/current signed-X6 and centered-slice definitions, current `signed_brc.py`, and current centered-slice checker. These sources show an **actual current BRC API** and a **mathematically typed proposed native dominant consumer**, not a confirmed original LP011 native consumer or all current consumers. A bounded companion review previously inspected additional old sources and 8 paired current definitions; no repository-wide exhaustive negative conclusion follows.

Unfinished under Driver `REQUEST_REVISION`: (1) produce a fixed version-pinned finite historical/caller dependency manifest, not a vague "no caller found"; (2) locate exact original LP011 dominant/sign/tie statement and any real downstream calls, or classify each declared corpus entry with its exact negative coverage and residual search boundary; (3) attach old source line, old claim ID, corrected type/strongest proof, actual current caller, keep/retype/revise disposition for each of all 28 rows, with specific quadratic/parity/affine domains; (4) independently review the corrected coverage. Do **not** repeat previously completed signed-shell 30/846, old one-sector 72, original carrier 111/kernel, closed-disk geometry or preceding chamber/median theorems as a substitute for these obligations.

**Durable continuation:** mother Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable frontiers original HRI/review and the two earlier 2026-11-12 LP011 reports plus this report/checker; native Source checkpoint and new winning X6 CLAIM/run are **not established** by a portable GitHub file. Original successful continuation request `onhour-research-20261112-0422-x6-continuation-v1` requires typed previous-claim CAS `chatgpt-x6-legacy-plane-recon-20260905-1921-c7e4b2` / Issue240 comment `5551433265` and Source-verified predecessor progress. Fresh `recovery_status` original request `onhour-research-20261112-0607-recovery-x6-v1` confirms session ACTIVE, no current run/claim and no pending uploads; this is a subject-local projection only. Do not fabricate continuation_prepare/claim/open. The next concrete *research* action is source-line/caller trace and one bounded manifest row for LP011 linked to the existing consumer guard. The next *control* action is verify an admissible Source-backed last-progress pin and use the existing typed continuation route, with formal checkpoint after a real winning CLAIM/open; until then research files remain `UNREVIEWED / NOT_ADMITTED`.

Authorship/exposure: ChatGPT TASK_RESEARCH, `EM-ENTERPRISE-9C9163` as last authenticated bridge session identity; NONBLIND reuse of published X6 foundations, old Result/review, and earlier ChatGPT LP011 notes. No claim of independent Driver or original author identity.
