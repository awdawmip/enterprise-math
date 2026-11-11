# X6 / LP011 — reconstructing signed native displacement from the relative observer, shortest-length and median sign

**Status:** AUTHOR_PROVED / EXACT_REGRESSION_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. This is a new self-contained mathematical unit, **not** a canonical Result, independent review, authenticated historical claim or native TASK checkpoint.

**Mother Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`; current historical intake `HRI-1A48B2D7F0E242FCC2C57D7E`; independent disposition `HIRR-1C60C7CCFAE8636E82F43A76 = REQUEST_REVISION`. This note consumes and extends the previous LP011 chamber theorem `research_notes/X6_LP011_SIGNED_DOMINANCE_FIBRE_CHAMBER_20261112_ONHOUR.md` without claiming its original historical caller was found.

## Exact selected-X6 question and theorem

Use the frozen mathematical inputs of this Task, specifically `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` and the historical comparison generation `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Fix an ordered selection of three native axes within P000's full signed six-dimensional Cell torsor, with the *other three relative components exactly zero* (a centered three-axis subtorsor, not an independent native plane). This is raw internal displacement mathematics and **not** the six-field final nonnegative Cell-address encoding.

For a raw signed displacement `d=(d_1,d_2,d_3) in Z^3`, define

```
h=min_i d_i
a=rho(d)=d-h*(1,1,1),  min(a)=0
(0,b,M)=sort(a),  0<=b<=M
N(d)=sum_i abs(d_i)       # exact shortest signed-native coordinate path length
s(d)=sgn(h+b)             # sign of the MEDIAN RAW component, including 0
```

**Theorem (exact one-sign reconstruction).** The map
`d -> (rho(d), N(d), s(d))` is injective on all of `Z^3`. More precisely, for each prescribed `a`, `N(h)=sum_i |h+a_i|` obeys the complete four-chamber formula

```
h <= -M:        N(h)=-3*h-b-M
-M <= h <= -b: N(h)=M-b-h
-b <= h <= 0:  N(h)=M+b+h
h >= 0:        N(h)=3*h+b+M.
```

The formulas agree on overlaps, including repeated components and `M=b=0`. They imply that `N(h)` is strictly decreasing on integer depths `h<-b`, has its unique minimum `N(-b)=M`, and is strictly increasing for `h>-b`. Consequently `s` identifies the unique monotone branch and determines `h` exactly. The resulting native signed displacement is `d=a+h*(1,1,1)`.

One explicit inverse for realizable triples `(a,N,s)` (reject failed integer-divisibility, sign or forward-length checks):

- `s=0`: necessarily `N=M`, `h=-b`;
- `s=-1`: for `M<N<=2*M-b`, `h=M-b-N`; for `N>2*M-b`, `h=-(N+b+M)/3`, requiring an integer;
- `s=+1`: for `M<N<=M+b`, `h=N-b-M`; for `N>M+b`, `h=(N-b-M)/3`, requiring an integer.

**Proof.** Because sorting the three `a_i` does not change their sum of absolute values, `N(h)=|h|+|h+b|+|h+M|`. Resolve the three absolute-value breakpoints `-M,-b,0` to obtain the displayed exact formulas. Slopes are `-3,-1,+1,+3` in successive open chambers; endpoints preserve strict monotonicity on either side of `-b`. The sign of the median raw component is precisely `sgn(h+b)` and distinguishes the two monotone branches and the unique minimum, proving injectivity and the inverse. QED.

**Sharp sufficiency boundary.** The relative coordinate `a` plus shortest path length `N` alone need *not* determine signed native geometry, even when `N` is exact. At `a=(0,1,4)`, take

```
d_- = (-2,-1,2), h=-2, N=5, s=-1,
d_+ = ( 0, 1,4), h= 0, N=5, s=+1.
```

The signed endpoints differ while `rho(d_-)=rho(d_+)=a` and `N(d_-)=N(d_+)=5`. In particular the exact shortest-word BRC cardinalities differ:
`B(d_-)=5!/(2!1!2!)=30`, versus `B(d_+)=5!/(0!1!4!)=5`. Hence neither native signed dominant-axis/sign/tie information, native norm nor shortest BRC cardinality in general descends to `(a,N)`. The sign `s` restores the *endpoint* exactly. **It does not by itself reconstruct an ordered path word, branch history, weighted or channel-constrained BRC provenance.** Retain ordered-path information if future operations require it. For `N>M`, whenever both sign branches realize the same input `(a,N)`, at least one binary-side distinction is necessary for exact signed-endpoint readout; this is a scoped witness, not an information-theoretic claim about all encodings.

## LP011 and source/caller consequence

Combine this theorem with the preceding exact chamber rule `theta=2*h+M`. Recover `h` from `(a,N,s)`; then `theta>0` selects positive max-`a` axes, `theta<0` negative min-`a` axes, `theta=0` both endpoint groups with their respective signs. The `M=0` case uses `sgn(h)`. This is an explicit **observer/future-operation sufficiency certificate** for the *declared raw signed endpoint, dominant-axis, native norm and unweighted shortest-path BRC* queries, not for every enriched Path/Packet observer.

The inherited historical 28-row ledger's LP011 entry is an **author/review summary**, not yet a located original historical 'max chooses dominant native signed axis' passage. Bounded exact-old-source search this round examined the following frozen files with their substantive formulas: native line trace, R061 arbitrary-point directed gauge, R062 BRC bridge, bidirectional spectrum, diagonal displacement quotient, path-valued square-root operator, vector endpoint/reverse geodesic segment, segment shortest-path routing, three-positive-axis carrier definition, coordinate/BRC bridge, diagonal-gauge theorem package, signed path/BRC, all-slice-return no-go, directed gauge/projection contraction, common-depth cocycle. No standalone original LP011 dominant-axis/sign/tie selector was identified **in this bounded set**. The `M=max(A,B,C)` formula at historical R061 `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` blob `58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0`, lines 236–250, is the **relative reverse decoder** `can3(-d)=M*1-can3(d)`; its use alone does not establish a historical native dominant-axis caller.

Do not silently turn this bounded absence into repository-wide absence. The current review `REQUEST_REVISION` requires a finite version-pinned corpus/dependency manifest, exact old LP passages and real downstream callers, typed disposition and anti-regression coverage of every declared current consumer. Preserve prior 28-row data, the verified 72 one-sector and 213 observer mass, 30 signed shell/846 signed shortest words, (1,1,1) hidden native displacement, carrier closed-disk geometry and all completed old checkers rather than rerunning them.

## Executed exact regression and research continuation

The separate self-contained integer checker `research_checks/X6_LP011_SIGNED_MEDIAN_BIT_LENGTH_RECOVERY_20261112.py` was executed locally and returned:

```
PASS selected_X6_signed_L1_median_bit: signed_points=6859 length_signatures=5830 double_fibres=1029 piecewise_cases=7161 witness_BRC=30_vs_5
```

Coverage: complete finite cube `[-9,9]^3` (6859 raw signed displacements), 5830 distinct `(a,N)` signatures, 1029 signatures with two possible raw depths (whose median signs differ), and 7161 further chamber checks on 217 min-zero residuals in `[0,8]^3` and depths `[-16,16]`. Exact integer arithmetic, no floating point. These are finite implementation regressions. The infinite-domain injectivity theorem follows from the algebraic proof above, **not** from finite enumeration.

**Persistence/authority boundary:** The present Source may accept this note and checker as portable evidence through the already authorized GitHub write path; no current winning X6 CLAIM/run or native semantic checkpoint is inferred from source preservation. The predecessor historical Result remains under `HRI` and `HIRR REQUEST_REVISION`. Original chat-transport prepare `onhour-research-20261112-0418-prepare-selected-v1` failed `TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR`; original continuation `onhour-research-20261112-0422-x6-continuation-v1` succeeded. The latter is only an exact packet/route, not an automatic CLAIM. Existing ordinary-control Research conversation label: `chatgpt-research-onhour-enterprise-math-20260923`; other maintenance conversation identities are unrelated and excluded.

**Next smallest exact action:** through the existing authorized lane, consume the successful typed continuation and verify the actual Source-backed historical progress artifact, prepare with its precise immutable frontier and accepted predecessor CAS, then establish own winning CLAIM/open before formal checkpoint. Continue the *remaining* LP011 original source/caller/corpus trace, now with the signed-depth/median-side theorem usable as a repair certificate. No current scientific manuscript or path script is an independently accepted Result.

**Authorship/exposure:** current ChatGPT TASK_RESEARCH mathematical author; NONBLIND; uses preceding Task materials, original Driver revision and signed X6 foundation. Identity/session provenance is not a mathematical independence assertion.
