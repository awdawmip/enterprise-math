# X6 LP011 — signed dominant-axis fibre chamber and observer-quotient nonfactorization

**Status:** AUTHOR_PROVED / EXACT_REGRESSION_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / NOT_A_NATIVE_RESULT. This is a *new, bounded, source-preserved research unit*, not a reconstructed historical result, not a claim that LP011's original old caller has been located, and not a claim that the full legacy-plane Task is complete.

**Mother Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2` (selected by this Research conversation's fresh canonical dispatch `onhour-research-20261112-0406-dispatch-v1`). The prior scientific originals remain `RR-943A793DB1F7B8012A85` in prospective historical custody `HRI-1A48B2D7F0E242FCC2C57D7E`; review `HIRR-1C60C7CCFAE8636E82F43A76` is **REQUEST_REVISION**, not ACCEPTED. No current winning CLAIM/run or formal native checkpoint is asserted by this note.

**Frozen mathematics:** centered, signed, selected three-axis affine subtorsor of native X6 from `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, particularly `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`. The historical comparison pin is `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. A three-axis slice is a restricted native X6 chart, **not** a native independent plane. Raw signed charts are distinct from final six-field nonnegative Cell addresses. Time is separate. This report makes no full-X6 rotation, carrier-to-native equivalence or Foundation claim.

## Precise LP011 question and exact chamber result

The inherited 28-row ledger's LP-011 says “Dominant branch is max of a positive/min-zero normalized displacement”, retyped only informally as `argmax_i |delta_i|` plus orientation sign. The current Driver found the actual **historical LP011 dominant/sign/tie caller still unlocated**; that evidentiary obligation remains OPEN.

Define, for raw signed `d=(d1,d2,d3) ∈ Z^3`,

```
h = min(d1,d2,d3)
a = d - h*(1,1,1)    # relative observer, min(a)=0
M = max(a1,a2,a3)
D(d) = {(i, sgn(d_i)): |d_i|=max_j |d_j| > 0}
```

Here `D` is **set-valued**, retaining all tied dominant signed axes; `D(0)=∅`, and no positive-index tie-break is silently promoted into native semantics. Let `I_max(a)={i:a_i=M}` and `I_min(a)={i:a_i=0}`.

**Theorem (full signed chamber rule on each relative-observer fibre).** If `M>0`, put `theta=2*h+M`. Exactly:

```
theta > 0:  D(d) = {(i,+1):i in I_max(a)}
theta < 0:  D(d) = {(i,-1):i in I_min(a)}
theta = 0:  D(d) = {(i,+1):i in I_max(a)}
                    union {(i,-1):i in I_min(a)}
```

The transition `theta=0` is possible for integer `h` precisely when `M` is even and `h=-M/2`. If `M=0`, the native displacement is `d=h*(1,1,1)`: all three axis signs are positive for `h>0`, all negative for `h<0`, and the signed-axis set is empty for `h=0`.

**Proof.** Every `a_i` lies between the attained endpoint values `0` and `M`. Since `x ↦ (h+x)^2` is strictly convex, its maximum on this finite interval occurs only at endpoint positions for `M>0`. Compare the two endpoint squares:
`(h+M)^2-h^2=M(2h+M)`.
When it is positive, the `a_i=M` endpoint wins and `h+M>0); when negative, `a_i=0` wins and `h<0); on equality both extreme endpoint groups tie with opposite signs. This proves every case including multiplicities; `M=0` follows directly. **QED.**

**Observer nonfactorization, with constructive universal witnesses.** For *each* relative residual `a` with `min(a)=0`, take `d_plus=a+(1,1,1)` and `d_minus=a-(M+1)*(1,1,1)`. Both share the same relative address `a`. In the first, every raw coordinate is positive and `D(d_plus)` contains only positive max-endpoint axes. In the second, every raw coordinate is negative and `D(d_minus)` contains only negative min-endpoint axes. Hence `D(d_plus) != D(d_minus)` **for every observer fibre**. No function of the min-zero residual `a` alone can recover the native signed dominant-axis set for arbitrary signed displacements. Retaining `h` (or another genuinely sufficient repair datum) makes the above readout exact. This is an operation-sensitive information-loss proof, not merely a claim that old numbers are false.

**Reversal and old max formula.** Native reversal is `d ↦ -d`, so `D(-d)={(i,-s):(i,s) in D(d)}`. At the observer layer the historical formula survives exactly:
```
a_reverse = rho(-d) = M*(1,1,1) - a
h_reverse = -h-M
theta_reverse = -theta.
```
Thus `M=max(a)` is legitimate as the **relative quotient inverse parameter**, not an authenticated historical “native dominant branch” selector. The nearby historical source `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, frozen blob `58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0`, lines 236–250, uses `M=max(A,B,C)` specifically for the reverse directed observer decoder. It does **not** by itself locate LP011's claimed independent dominant/sign/tie caller.

**Exact witnesses.** With `a=(0,2,4)`, `M=4`: at `h=-3` dominant is `{(1,-)}`; at `h=-2` it is the genuine tie `{(1,-),(3,+)}`; at `h=-1` it is `{(3,+)}`. The two native signed displacements `(-2,1,0)` and `(1,4,3)` have identical `rho=(0,3,2)` but `D={1-}` and `D={2+}`. In the 3-4-5 witness, `d=(3,4,0)` has native `D={2+}`, and its true reverse `(-3,-4,0)` has `D={2-}`, shortest-path BRC multiplicity `35` in both directions. Observer normalization of the reverse yields `rho=(-d)=(1,0,4)`, which is **not** its raw native reverse.

For shortest signed coordinate paths, `N(d)=∑_i |d_i|`, `B(d)=N(d)!/∏_i |d_i|!`; `B(-d)=B(d)` but positive branch mass does not encode orientation sign, and the observer fibre may change even `B`. Retain signed path identity/provenance before BRC recoalescence and before any min-zero quotient when native future operations are declared.

## Executed reproducible certificate

Source file: `research_checks/X6_LP011_SIGNED_DOMINANT_FIBRE_CHAMBER_20261112.py`, Git blob `1ee09fddc9456f5bf1cfc2641fe4a5dcfb7f4bc5`, committed at `cf7add9d2882ff370c5c3e0a6ae8ec2c2ffacb8d`. A separately executed corresponding exact-integer regression returned:

```
PASS X6_LP011_SIGNED_DOMINANT_CHAMBERS chambers=3175 ties=537 nonfactor_fibres=127 signed_cube=2197 observer_inverse=exact reversal=equivariant BRC=symmetric
```

It checks `127` different min-zero triples in `{0,...,6}^3`, `25` integer common-depth values each (`3175` cases), exact signed reversal/chart inversion/BRC symmetry on each, `537` tied-dominance cases, an explicit nonfactorization witness for every one of the `127` fibres, and the full signed cube `[-6,6]^3` (`2197` points). Finite tests are regressions; the universal theorem above is symbolic. The Git source checker was read back; no assertion is made that a remote host executed it.

## Scope, immutable frontier, and continuation

**Already-complete evidence NOT to redo:** inherited `28` historical ledger rows as historical evidence, the independently supported signed `N=25` restricted-shell `30` endpoints / `846` shortest path words, original one-sector `72`, relative section `9` / `213`, native `(1,1,1)` versus carrier return, and closed-filled-disk carrier radius/overlap/cover. None of those is newly proved here, and no previous reviewer authority is inherited.

**Genuine remaining X6 Task obligations:** (1) locate LP011's *actual* historical dominant-axis/sign/tie statement and its real callers; the old inverse-gauge `max` line is not enough; (2) specify a finite immutable old/current corpus/dependency manifest and trace every declared active consumer; (3) augment each material LP row with old location, old semantic type, corrected exact obligation, evidence, downstream caller and repository action; (4) preserve external/restricted carrier typing. The existing historical `HIRR-1C60C7CCFAE8636E82F43A76 / REQUEST_REVISION` remains controlling. No old report/checker, signed-shell census, Hart/prime sample or other completed benchmark was rerun.

**Control lane:** `conversation_id=chatgpt-research-onhour-enterprise-math-20260923`; actual session `MCP-de3e5bafb24f43f4a5e6285e7601676a` (RESEARCHER). Canonical dispatch `onhour-research-20261112-0406-dispatch-v1` selected this Task; pending original requests `onhour-research-20261112-0418-prepare-selected-v1` and `onhour-research-20261112-0422-x6-continuation-v1` must be reconciled/read, never replayed. At the time of this document, their definitive winning claim/run and a Source native semantic checkpoint are **not yet established**. This Git research note is durable candidate evidence, **not** an admitted Result, native checkpoint, or HANDOFF. Next exact action after the original receipts: verify own winning claim and open/continue authorized run; bind this immutable artifact to the next scoped ledger/corpus checkpoint, then continue source/caller discovery, not a fresh 28-row rewrite.

**Global/Source write boundary:** only this new research note and fresh checker are written; frozen Foundation, pre-rebase provenance, older Result and old reviews remain immutable. No Working Truth, Foundation or native law promotion is claimed.
