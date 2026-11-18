# Stage275 — Exact Bellman real-cap face and Stage276 witness

Date: 2026-10-29. Scientific status: **PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**.
Local role: **RESEARCH_AUTHOR**; authenticated native research/owner authority not established (service said `research_authority_granted=false`; owner inventory returned `CONTROL_QUOTA`). This GitHub contribution does not assert a native CLAIM, Source Result, independent Driver approval or Foundation promotion.

## Immutable inputs and scope

- Global knowledge snapshot: `awdawmip/chatgpt-global-knowledge main@2cac8804687bc0fe9351f67edd20349f02b5cc3e`.
- Enterprise Math canonical control snapshot: `awdawmip/enterprise-math main@f8759137d869da71426061ab9e8ea7855712c833`.
- Source Stage274 predecessor: `889678bf70eacaf8142da5d8c5f525a960fb40f6` (same PR).
- P000 and ACTIVE worldview used solely as scope/typing constraints; native P000 X6 transfer is an independent outstanding theorem.
- External ternary IID sequential-decision model `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`, maximum observations `N=12`; arbitrary randomized policies may depend on every ordered history. Observers `(eP,eQ,tP,tQ)`; `V12(a,b)=min max(tP,tQ)` subject to `eP<=a,eQ<=b`. `+infinity` if infeasible.

## Stage275 author-level exact result

For
`a=1175053055941/15850845241344` and
`b=867218405255/1114512556032`,

`V12(a,b) = 539955234235/92876046336`.

One exact supporting dual has
`lambdaP=38096641024/218617401`,
`lambdaQ=6434343396/72872467`,
`H=49314920902234732441/564008885142552576`,
and the time weights `(0,1)`.
A strictly positive rational mixture of three zero-dual-gap policies attains both error caps and satisfies `tQ>tP`, giving equality with the global Bellman lower bound.

For **every real** pair `(a,b) in [0,1]^2`, the supporting affine expression `H-lambdaP*a-lambdaQ*b` equals `V12(a,b)` precisely when `(a,b)` belongs to the strictly convex non-parallelogram quadrilateral
`R275=conv(M,Jnew,Jplus,M2)` in the two error coordinates. Its exact area is
`2010397649169921875/276030719456218208796672`, and its shared supporting edge with R274 is the full M--Jnew edge (interiors disjoint). See full proof for the exact four-coordinate vertices and geometric signs.

Full ordered-history tie ancestry: Bellman ties are exactly `T=(0,0,5)` at P/C and `S4=(1,2,7)` at Q/C. `S4` is reached by 110 ordered words when T stops and by 116 when T continues (6 descendant words). Every zero-dual-gap history policy yields
`Obs(r,k)=M+r*(Jnew-M)+(k/110)*(M2-M)`
for `0<=r<=1`, `0<=k<=110+6*r`; the complete domain is attainable. Path multiplicity and two positive rational source masses are retained. This is BRC-compatible exact source tracking for the external IID model, not an asserted native-X6 dynamical model.

## Evidence archive and reproducibility

**`STAGE275_AUTHOR_EVIDENCE.tar.xz`** in this directory contains all four complete, nonempty text files:

1. `PROOF_STAGE275.md` — exact mathematical argument (13,659 bytes, SHA256 `91a414f59fcb6e7961e26e6e3aa9d6435cd192ff0e61b600e24a697ec8ac905b`).
2. `REPRO_STAGE275.py` — actual executed Python Fraction checker (9,401 bytes, SHA256 `5d070c303b45ee1b306f71fe9c96e6bd0134e9dea6b729ad673b4e61087f5ab5`).
3. `REPRO_STAGE275_EXECUTED_STDOUT.txt` — captured exact execution output (2,665 bytes, SHA256 `021345bc51de9ec3923b86ccff78e47b8f98879204d07f3e27c41ce8c0b848c7`).
4. `NEXT_TASK_PACKET_276.md` — independently actionable Stage276 handoff (4,464 bytes, SHA256 `7bb74a4cf5d0b3abbd0448c566247947edc2d36cd6b9e152793539e85fbe99ae`).

Archive SHA256 `248462dcad08edd3ae07136e65d8f72f257a44529355182538cb11a0babafd58`.
Git blob SHA1 `711c2260c48a137c569223849a6c53cd4b8c2058`.
Local archive was tested with `xz --test`; the executed checker was run again and its stdout compared byte-for-byte to the archived log.

To reproduce from this archive: `tar -xJf STAGE275_AUTHOR_EVIDENCE.tar.xz`, then `python REPRO_STAGE275.py`. It uses only Python's standard library and rational `Fraction`. Actual recorded success sentinel: `STAGE275_EXACT_ALL_REAL_FACE_PASS`. Exhaustive state check covers 455 Bellman states, 1,274 legal action costs and 817 strictly positive gaps; independent complete ordered-word DFS of five policies visits 52,268 nodes and 34,847 terminals, with P and Q total termination masses each exactly one.

## Next exact frontier — Stage276

`a276=1162027955941/15850845241344`,
`b276=868777330255/1114512556032`.
An exactly executable mixture of M2/Jplus/M3 policies gives the feasible upper bound
`V12(a276,b276)<=541791009235/92876046336`.
This target lies strictly outside R275. Derive the next exact Bellman dual (initial candidate ties T and S5=(1,2,8)), prove or obstruct its full real-cap region using full ordered-history ancestry and independently audited two-source masses. Complete hypotheses, checks, error bounds and open duties are included in the archive's `NEXT_TASK_PACKET_276.md`.

This is a portable research evidence handoff under the existing research PR, not a new canonical task or duplicate control registry.
