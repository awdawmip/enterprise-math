# X6 R063 PathSqrt — exact full signed six-axis N=2500 shell and shortest native N-BRC

Date: 2026-11-14, 13:00 Asia/Hong_Kong.
Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
Researcher `EM-X6-FB6990`; original Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Status: **AUTHOR-VERIFIED FINITE INTEGER CERTIFICATE / UNREVIEWED / NOT_ADMITTED**. This is not an independent Driver review or completion of historical R063 C3/C4 original benchmark.

## Question and scientific input firewall

The previous source-bound R063 consumer repair proves that the historical two-positive-axis operator does **not** exhaust the selected signed `Z^3` shell for squared norm 2500: six fixed-sector roots versus 150 signed three-axis endpoints. Its report at `0158c83178cc3026ce94b85472fe5d31d28b4fc4:research_notes/X6_R063_PATHSQRT_CURRENT_NATIVE_SCOPE_CONSUMER_20261114_1200.md` explicitly leaves the full signed six-axis native shell uncomputed. This unit closes **only that finite full-six-coordinate enumeration and shortest native N-BRC count**, not the historical R063 generality or any underlying unexecuted benchmark.

Frozen P000 V5: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json`, blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`.
Frozen X6 Cell torsor: same pinned commit, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. It defines Cell displacements in signed `Z^6`, `L_E(d)^2=sum_i d_i^2`, twelve primitive signed axis steps, and shortest signed path N-BRC mass `B_min(d)=(sum_i|d_i|)!/prod_i |d_i|!`. Chosen Cell anchor and ordered six-axis labels are retained. This **does not** identify the native 120-degree Enterprise readout with a classical three-dimensional Euclidean realization.

## Complete exact finite result

At squared native component norm `N=2500`, over **all** `d=(d_1,...,d_6) in Z^6` with `sum_i d_i^2=2500`:

- Distinct signed full-native **endpoint displacements: 102,539,052**.
- Aggregate shortest ordered primitive-path `N-BRC` multiplicity:
  `46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372`.
- Possible shortest path lengths `T=sum_i|d_i|` range from **50 to 122**, with **32 distinct attained T strata**.
- For `k=1,2,3,4,5,6` fixed ordered native axes, the `N=2500` endpoint-count prefixes are respectively **2, 20, 150, 18,744, 1,360,890, 102,539,052**. In particular, the previously checked selected signed `Z^3` shell has 150 endpoints; **102,538,902** six-axis shell endpoints lie outside that coordinate-supported three-axis slice.
- Explicit six-support endpoint `d=(1,1,1,2,27,42)`, with `1+1+1+4+729+1764=2500`. It cannot be reached by any two-generator fixed-sector operator or by a path restricted to one particular three-axis coordinate slice. Its displacement is a *composite* native path, not a newly primitive direction.

This is a **sum over all signed, ordered six-axis native endpoints of their distinct shortest word counts**. It is neither a Boolean-BRC support count, a carrier/relative-observer return count, nor a count of non-shortest paths. No quotient of common diagonal, sign or path provenance is taken.

## Exact recurrence and proof of exhaustive coverage

Let `C_k(n,t)` count signed `k`-coordinate displacement endpoints with `sum d_i²=n`, `sum |d_i|=t`, and let `W_k(n,t)` sum shortest ordered path multiplicities over those endpoints. Start with `C_0(0,0)=W_0(0,0)=1`; every other zero-axis state is zero. For `v=0,1,...,floor(sqrt(n))`, put `s(v)=1` for `v=0` and `s(v)=2` for `v>0`. Then

`C_k(n,t)=sum_v s(v) C_{k-1}(n-v²,t-v)`

and

`W_k(n,t)=sum_v s(v) binom(t,v) W_{k-1}(n-v²,t-v)`.

Reason: one signed coordinate contributes exactly 1 or 2 sign choices. An old shortest signed word of length `t-v`, and `v` copies of the new signed axis, have `binom(t,v)` distinct order-preserving interleavings. Every endpoint has a unique signed final coordinate, proving neither omission nor double counting. No unsigned/relative-axis identification occurs.

Independent check: enumerate magnitude triples `a,b,c>=0` with `a²+b²+c²<=2500`, weight each by `2^(#nonzero)` and `(a+b+c)!/(a!b!c!)`, aggregate by squared norm and total length, then split the six ordered axes as `(1,2,3)|(4,5,6)`. Convolving a triple state `(n,t)` with `(2500-n,u)` counts endpoints by product and words by `binom(t+u,t)` times the two triple word totals. **Both independently implemented exact-integer computations matched** on all headline totals in the current research run (no floating-point square tolerance).

## Executable reproduction and authority boundaries

New source-verified checker:
`awdawmip/enterprise-math@67053ca8c17cf998979205109d84893bcf54c69c:research_checks/X6_R063_FULL_SIGNED_SIX_AXIS_N2500_NBRC_20261114_1300.py`.
Git blob `6b0e4f096bc0d818849536f9fcb2d8679ca24ccc`, exact UTF-8 SHA256 `8ea40c71571a41e83ab2b66e710d38c137ad318e81dcf5894bf5f8ef27bcc7f0`. Saved connector file readback matched the stored source body. The two algorithmic calculations were executed directly in this research environment; the committed checker bytes have been read back, but have **not** separately been run by an independent third-party runner. The certificate remains author-side.

No original R063 `1<=r<=512` C3/C4 native benchmark was rerun. Original frozen R061/R062 and R063 sources, P000 and the already-reviewed N=25 and N=2500 selected-slice certificates remain unchanged. Historical Gaussian root factorization stays valid in its fixed two-positive-axis sector.

## Parent frontier and remaining executable gaps

This result closes **one** previously open full-six-axis R063 `N=2500` enumeration; it does **not** assert an all-`N` PathSqrt operator, an exhaustive off-native observer classification, or admissibility of previously unverified non-coordinate extra decorations.

Still open: trace the specific historical LP011 wrong dominant-axis/argmax native consumer and LP019 erroneous positive-path signed cancellation consumer at actual frozen call sites; finish the 28-LP claim-level old/current dependency ledger, inspect any identified external/dynamic R063 and Helly consumers, then send for independent Driver `REQUEST_REVISION` without self-admission.

Original Source checkpoint `onhour-20261114-1214-x6-r063-pathsqrt-native-scope-progress-v1` is `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED`, commit `81e75cad1b6f92d84d54c3bc5955063b5ba550da`. The above new finite six-axis extension was **not** part of that earlier Source publication. Preserve the same SID, CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, RUN `RUN-3356cbe3c2b4916d79399941`; use fresh own winning-claim/lease and current writer generation before any subsequent native semantic write, never a historical authorization receipt alone.
