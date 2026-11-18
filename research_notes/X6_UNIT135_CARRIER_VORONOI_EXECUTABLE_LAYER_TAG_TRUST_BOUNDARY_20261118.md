# X6 Unit135 — carrier Voronoi executable, current/frozen source parity, and layer-tag trust boundary

Status: **AUTHOR-SOURCE-PROVED / EXACT-REPLICA-WITNESS / BOUNDED_CONSUMER_AUDIT / UNREVIEWED / NOT_ADMITTED**. Date: 2026-11-18.
Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; mother objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`.
Research lane `chatgpt-research-onhour-enterprise-math-20260923`; author Researcher `EM-X6-FB6990`, Source SID `MCP-082892eb480e45dea6d4b9fcc0491034`. No maintenance/Driver identity or independent review is implied.

## 1. Frozen/current executable evidence and actual LP consumer scope

The exact entire file `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py` was read at the pre-rebase comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3` and at current GitHub `main`; **both have identical Git blob `900e246b0dafaa35d2452191e3df508a2d15a389`**, 563 source lines. This is one newly classified executable *carrier* consumer in the LP001/LP024/LP026 downstream dependency census; not an exhaustive search, not the original R063 native six-file benchmark, and not evidence of an incorrect current X6 call.

Exact source points:
- Lines 1–8: the file explicitly excludes native Enterprise metric implementation;
- Lines 21–24: `CURRENT_CENTER_CARRIER_SPECIALIZATION_ONLY`, `GLOBAL_TOOL_CLAIM=False`, no independent second Enterprise metric family;
- Lines 35–38: `ExactDistanceSemantics` carries `name: str`, `layer: str`, and an arbitrary `score` callable;
- Lines 62–77: `nearest_sites` requires non-null comparator, compares only `semantics.layer` string to requested layer, and minimizes the supplied `score`;
- Lines 257–278: the quadratic form `Q(x,y)=x²+xy+y²` is explicitly tagged `carrier`;
- Lines 463–518: seven center-carrier sites, exact ties and empty circumdisk; an explicit negative test rejects `required_layer="native"` with the existing carrier wrapper.

This is a **KEEP_CARRIER / NO_VERIFIED_NATIVE_PROMOTION** judgment. The frozen and current source preserve the same type boundary; the older carrier result's mathematics are not a replacement X6 metric.

## 2. Exact interface-level theorem: a caller-provided tag is not semantic proof

Fix any site family `S`, query `x`, and exact comparator `q(x,s)`. The implementation computes
`F(x,S;semantics)=sort({s in S:q(x,s)=min_t q(x,t)})`.
For any carrier comparator `q` supplied in an `ExactDistanceSemantics("carrier", "carrier", q)`, construct a *second wrapper using exactly the same function q* with `layer="native"`. The code in lines 68–77 only checks the string `layer` and then computes with `q`; therefore its output under `required_layer="native"` for the second wrapper equals the original carrier nearest-site output. No native metric theorem or trustworthy signed-X6 provenance has been created by the wrapper change.

Tiny exact witness in the triangular carrier chart: `S={"A":(0,0),"B":(1,0)}`, `x=(0,0)`, `q(u,v)=du²+du·dv+dv²`. Both `q(x,A)=0` and `q(x,B)=1`. The correctly tagged carrier invocation returns `("A",)`, and the `required_layer="native"` invocation with its carrier wrapper raises a semantic mismatch. Recreating an otherwise identical wrapper with `layer="native"` returns `("A",)` instead. The arithmetic and branch conditions were executed in a small faithful standard-library Python replica with `fractions.Fraction`, producing these three observations; **the full original 563-line program was not executed in this unit**.

The result is *a prospective trust boundary*, not a claim of an existing misusing caller, a security exploit, mathematical failure of the carrier theorem, or incorrect existing regression. A consumer may rely on the declared layer only when the comparator's semantics and provenance have independently been established by the typed Source contract. The script's currently enumerated concrete calls do not assert full signed-X6 distance.

## 3. Relationship to preceding research and remaining obligations

Reuse the already-published centered signed-X6 P000 scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03` and historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3` without changing them. This audit extends the existing selected 28-LP source/consumer crosswalk by **one precisely scoped executable consumer plus a metadata-trust criterion**; it does not replace Unit131's native shell enumeration, Unit134's package/test audit, or the original carrier/Voronoi tool's separate review.

Unfinished: exact old LP011 signed-native argmax caller and LP019 natural-N-BRC signed-cancellation caller are still `UNRESOLVED_PROVENANCE`; 28-LP active downstream closure remains partial; independent Driver `REQUEST_REVISION` remains open. Any future actual native caller passing `ExactDistanceSemantics` should be audited for the origin of its comparator and signed-X6 type, not merely its `layer` text. No current code patch is justified on this evidence alone.

This Unit135 source audit is authored/unreviewed evidence and **must not be described as native Result admission, original-program execution, or complete 28-LP coverage**. Previously saved Units1–134, original R063 benchmark, Research Activity and all historical requests remain unchanged.
