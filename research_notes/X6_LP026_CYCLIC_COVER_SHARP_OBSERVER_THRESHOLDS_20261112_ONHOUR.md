# X6 / LP026 — sharp finite-horizon safety thresholds for cyclic common-depth observers

Date: 2026-11-12. Lane: on-hour TASK_RESEARCH (declared logical label `chatgpt-research-onhour-enterprise-math-20260923`); Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
Status: AUTHOR_PROVED / EXACT FINITE CHECK EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED. This is scientific evidence, not a native semantic checkpoint, CLAIM, Result, independent review, or P000 revision.

## Source and typed domain

Frozen science: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` (P000 V5, signed Cell-centered X6); historical comparison: `@fd2bcff10ca6e147348b6c1236027fc0d2877df3`. This unit consumes the previous signed BRC pushforward proof, `research_notes/X6_LP026_FINITE_CYCLIC_COVER_SIGNED_BRC_PUSHFORWARD_20261112_ONHOUR.md` at `033a3bb5b62cda782e26930c30d8efeac1130ac0`, rather than re-proving it.

The inspected current source `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` (blob `3f7d9e62a4dd66e7888a69ff87276b283c891aac`) implements the *derived observer* `CoverState(Coord6(r),[h]_m,m)`. `signed_brc.py` (blob `300a96e3dc24bf6fff73743037a0347a8bc83176`) supplies signed native endpoint BRC. A cover quotient is never itself asserted to be P000's full Cell identity.

For signed primitive words of **exactly** length N, the reachable endpoint set is

```
S_N = {z in Z^6 : |z|_1 <= N and |z|_1 = N (mod 2)}.
```

For m>=1 let `h=min_i z_i`, `r=z-h*1`, and `pi_m(z)=(r,[h]_m)`. Two endpoints have equal projected cover state iff `z'=z+k*m*1` for some integer k. Define `G(z)=sum_i z_i^2`; `B_N(z)` counts ordered signed 12-generator words with native endpoint z and length N.

## Theorem: three distinct sharp thresholds

For every integer m>=1 and N>=0, *restricted to S_N*:

1. **Exact endpoint recovery:** `pi_m|S_N` is injective iff **N<3m**.
2. **Native component squared norm:** `G|S_N` is constant on every `pi_m` fiber iff **N<=3m**.
3. **Endpoint-specific length-N BRC:** `B_N|S_N` is constant on every `pi_m` fiber iff **N<3m**, or **N=3m with m in {1,2}**.

This is a positive, fixed-horizon *observer-specific* safe-compression certificate. For m=0 the full integer depth is lossless for all N. For unrestricted horizons no finite m preserves native identity, norm or endpoint-specific BRC globally. **Projected BRC fiber sums** remain exact for all N and m under the previously proved pushforward formula; do not confuse equality of B_N at separate endpoints with validity of that sum.

### Proof, including optimality

If distinct projected endpoints z and z' are both reachable, choose k != 0 with z'=z+km*1. Then

```
6*|k|*m = |z'-z|_1 <= |z'|_1+|z|_1 <= 2N.
```

Thus N<3m implies injectivity, hence all endpoint functions descend. At N=3m take `z=(-m,-m,-m,0,0,0)` and `z'=z+m*1=(0,0,0,m,m,m)`: both have length 3m and the same cover state. Endpoint injectivity therefore fails exactly at this bound.

Now suppose N=3m and z,z' are any distinct points in the same fiber. The inequality forces |k|=1, equalities in both length and triangle estimates, and `|z|_1=|z'|_1=3m`. Taking k=+1 by swapping the endpoints, each coordinate `-m<=z_i<=0`, so `sum_i z_i=-3m`. Consequently

```
G(z+m*1)-G(z)=2m*sum_i z_i+6m^2=0.
```

Hence norm descends even though Cell identity does not. At this boundary all colliding endpoints have shortest length N, so `B_N(z)=N!/prod_i |z_i|!`.

For m=1, write t_i=-z_i in {0,1}. The sum of six t_i is 3, so exactly three are ones; the complement map t_i -> 1-t_i merely swaps the counts. For m=2, t_i in {0,1,2} with sum 6 implies the number of zero entries equals the number of two entries; complement t_i -> 2-t_i preserves the multiset. Thus the factorial product, and B_N, agree for every fiber at N=3m for m=1,2.

For every m>=3, a counterexample at N=3m is

```
t=(m,m,0,1,1,m-2),
z=-t,  z'=z+m*1=(0,0,m,m-1,m-1,2).
```

These share a cover key, have shortest length 3m and identical G; their BRC factorial denominators are `D=m!^2*(m-2)!` and `D'=2*m!*(m-1)!^2`, with `D'/D=2(m-1)/m !=1`. Thus B_N fails to descend for m>=3 already at the identity-collision boundary.

Finally let N=3m+k with k>=1, and take

```
z=(-m-k,-m,-m,0,0,0),
z'=z+m*1=(-k,0,0,m,m,m).
```

Both have shortest length exactly N, share `pi_m`, yet

```
G(z)-G(z')=2mk>0,
B_N(z')/B_N(z)=binomial(m+k,m)>1.
```

This simultaneously gives the norm and BRC sharpness for every N>3m. All claims follow. QED.

## Exact certificates and local execution

The checker `research_checks/X6_LP026_CYCLIC_COVER_FINITE_HORIZON_SHARP_20261112_ONHOUR.py` was executed with Python integer arithmetic. It independently generated every signed 12-generator **exact-length** endpoint distribution for N=0..9 and used actual dynamic-programming word counts, not only the shortest-word formula. For every m=1..4, it grouped endpoints by `pi_m` and checked collision, G constancy, and B_N constancy: **343,240 distinct cover-key checks**, all PASS; largest shell size 48,940. Explicit formula witnesses were separately checked for m=1..15 and k=1..15, plus boundary cases, **253 additional exact tests**, all PASS.

| m | N | Native identity | G on cover fibers | B_N on cover fibers |
| --- | ---: | --- | --- | --- |
| 1 | 3 | collision | constant | constant |
| 1 | 4 | collision | differs | differs |
| 2 | 6 | collision | constant | constant |
| 2 | 7 | collision | differs | differs |
| 3 | 9 | collision | constant | **differs** |

For m=3,N=9, `z=(-3,-3,0,-1,-1,-1)` and `z'=(0,0,3,2,2,2)` have `G=21` in both cases, but `B_9(z)=10080` and `B_9(z')=7560`. This proves *norm-safe does not imply BRC-safe* at the same finite horizon.

### Current consumer integration and pending execution

Source read confirms `x6_cover.py::CoverState.step` is a correctly typed projection transition, while `x6_coordinate.py::Coord6.norm_squared` computes the section norm `sum r_i^2`, not in general `G(z)`: the exact relation is `G(r+h*1)=G(r)+2h*sum_i r_i+6h^2`. For native `-e_i`, `G=1`, whereas its min-zero section has squared norm 5. The older `check_x6_coordinate.py` calls the latter derived value `full_reverse_axis_norm_squared=5`; if exported as a native claim, that label is misleading. Its source-level correction should preserve the derived checker while explicitly renaming the readout as `derived_section_reverse_norm_squared=5` and separately checking native `spatial_norm_squared(-e_i)=1`. No active implementation edit is claimed in this unit.

**Still unexecuted:** the earlier checker’s actual imported-source `CoverState.step` interoperability branch. This unit’s finite-horizon checker was run stand-alone, and was *not* an import of those original Python modules. Do not mark that integration target PASS. Next precise action: use a faithful repository-source layout to run the pending import branch and then apply only grounded consumer typing repairs under legitimate ownership; continue LP011/LP019 original-caller tracing. Preserve Driver `REQUEST_REVISION`, typed-continuation support #2141, and unverified native X6 CLAIM/open.

## Continuation/authority distinction

Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Preserve all frozen R063 and earlier LP026 science; no prior result is reopened by this local lemma. Original receipt `onhour-20261112-1700-x6-task-read` observed `SUCCEEDED`, with `HANDOFF_READY/NEEDS_DISPATCH`, no active owner and no authenticated new X6 CLAIM/open. The historical research Activity `RA-629C868A22A736334628BEFA` and SID `MCP-de3e5bafb24f43f4a5e6285e7601676a` are provenance, not a fresh service authority. A Sites read-only recovery attempt for that SID returned `OWN_SESSION_REGISTRATION_NOT_FOUND` under the distinct Sites subject; no adoption, prepare, claim or dispatch was attempted. Current work is UNREVIEWED/NOT_ADMITTED until its required native/Driver steps occur.
