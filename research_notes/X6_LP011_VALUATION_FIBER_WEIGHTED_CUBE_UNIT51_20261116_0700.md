# X6 LP011 / valuation consumer: exact finite signed-cube fiber lift — unit 51

Date 2026-11-16. Researcher EM-X6-FB6990, own SID MCP-082892eb480e45dea6d4b9fcc0491034; TASK_RESEARCH lane chatgpt-research-onhour-enterprise-math-20260923. Parent RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Scientific status: AUTHOR-EXACT / EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen scope, exact current consumer

Native centered signed X6 baseline: awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03. Historical comparison pin: awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3. A selected three-axis signed Cell displacement cube is a **three-dimensional slice census**, not the complete signed six-axis norm shell.

The frozen research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_REPORT_20260822.md (blob 386a307a81816b27d9753562e53bea254f4062dc), lines 393-425, 760-776, defines the positive min-zero atlas A_E={v in N_0^3 : min(v)=0} and integer atlas horizon sigma(v)=max(v). It proves F_A(n)=3n²+3n+1 and b_A(0)=1, b_A(n)=6n for n>=1. Source line 409 expressly disclaims treating sigma as native length/radius/area/volume. The present main consumer retains the same typed statement (lines 396-425,762-776): KEEP_AS_ATLAS. Already completed LP005 common-depth reconstruction and LP011 signed argmax/BRC theorems are inputs, not new proof claims here.

## Exact finite-cube fiber theorem

For every integer d>=0 let C_d = {x in Z^3: -d<=x_i<=d}; put h=min(x), rho(x)=x-h(1,1,1), m(v)=max(v). Then

rho(C_d) = {v in A_E : m(v)<=2d},

rho^{-1}(v) intersect C_d = {v+h(1,1,1): h=-d,-d+1,...,d-m(v)},

so its exact cardinality is w_d(v)=2d-m(v)+1.

Proof: for v>=0 and min v=0, the cube constraint on all components v_i+h is equivalent to h>=-d and h+m(v)<=d. Each signed native triple has a unique pair (rho(x),min x); hence these fibers partition C_d without multiplicity or missing endpoints. Using the atlas shell count gives the exact integer identity

sum_{v in A_E, m(v)<=2d} w_d(v)
= (2d+1) + sum_{m=1}^{2d} 6m(2d-m+1)
= (2d+1)^3.

By contrast, the unweighted old atlas count at n=2d is F_A(2d)=12d²+6d+1. This is a typed weighted-fiber lift of the correct old valuation; it does not change the original atlas result.

**Operation-sensitive obstruction:** x=(-1,0,0) and y=(0,1,1) are both in C_d for every d>=1, with rho(x)=rho(y)=(0,1,1). But native G(x)=1 versus G(y)=2; shortest positive signed-step BRC(x)=1 versus BRC(y)=2; signed dominant labels Dom(x)={(axis 0, negative)} versus Dom(y)={(axis 1,positive),(axis 2,positive)}. Thus rho alone cannot be used to identify native squared norm, LP011 signed dominant axis/tie, or BRC. Retaining h gives a lossless implementation/observer contract.

## Original execution and coverage

Executed research_checks/X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_CHECK_20261116_0700.py in Python 3 normal and -O mode; both returned exit 0 and PASS_X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_0_512. Exact exhaustive **native triples and fibers** for d=0..8; exact polynomial certificate for d=9..512, plus the named signed-axis/norm/BRC collision witness. Machine certificate research_checks/X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_RESULTS_20261116_0700.json has canonical payload SHA256 c11207d64339364e0e369deaa3f84d01eaee7700e5d27196c1f799b276b388fd. For d=1: native cube 27, observer keys 19, weighted sum 27. For d=2: 125, 61, 125.

## Newly bounded frozen historical source search

Inspected the exact nontruncated frozen Git tree (5,014 entries), then successfully fetched **every one of the 62** definitions/, research_notes/, experiments/ .md/.py/.json blobs with a filename date 2026-08-16 through 2026-08-29. Searched every body using case-insensitive probes for argmax/dominant-axis/Chinese dominant terms/max(A,B,C), signed BRC, cancellation/相消/抵消 and positive/signed paths; this is a filename-date corpus and not all frozen repo files.

1. Frozen OG definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md blob 58ccac6d... line 241, frozen OQ definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md blob 11f47f9d... line 144, frozen NQ research_notes/DIAGONAL_GAUGE_DERIVED_DISPLACEMENT_THEOREM_PACKAGE_20260826.md blob 609334fa... line 75: M=max(A,B,C) is used for explicit quotient/relative inverse; none establishes the alleged *native signed* wrong caller in LP011.
2. Newly inspected original valuation report blob 386a307a... lines 407/413/765: max(a,b,c) defines the *positive atlas horizon*, distinct from native signed dominant axis. Its present current source keeps that type.
3. Frozen research_notes/TOOL_DISCOVERY_DISCRETE_MORSE_ACYCLIC_MATCHING_RESULT_20260823.md blob 5a71d15a... lines 42-60,76-107: chain complex cancellation over Z/Q with declared unit/invertibility conditions, not positive natural N_BRC signed subtraction; KEEP_CHAIN_HOMOTOPY_TYPE.
4. Frozen definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md blob 6ec0d73a... line 33 explicitly excludes signed/amplitude cancellation from historical BRC. No particular alleged wrong native positive-path cancellation caller was found among these 62 bodies.

This extends the 28-LP active consumer table with two separately typed historical source locations, one correct current valuation reader and an exact signed-cube adapter. It does not establish repository-wide absence: LP011 and LP019 specific historical false-call attribution remain UNRESOLVED_PROVENANCE outside the scanned corpus. The old 28-claim ledger retains its historical attribution unchanged. The current task still needs all-active-consumer closure, any demonstrable Helly address-type repair, and independent Driver REQUEST_REVISION.

## Preserved native state and next step

Original same-session request onhour-20261116-0644-x6-original-r063-native-17gate-512-unit49-50-source-progress-v1 is SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED; previously executed #50 original six-file R063 17/17 gates and 512/512 rows remain unchanged. Own exact continuation request onhour-20261116-0701-x6-exact-continuation-v1 was consumed as SUCCEEDED but projected execution_authorized=false, so this GitHub author's saved unit alone is not a native semantic checkpoint. Original SID, claim MCP-30a8f5fd123215e08bd4a7cf and RUN-3356cbe3c2b4916d79399941 are retained as historical/continuation pointers; revalidate real Source ownership before any native unit51 publish. Do not borrow maintenance identity, restart previously completed science, or hand the author's evidence to oneself as independent Driver review.