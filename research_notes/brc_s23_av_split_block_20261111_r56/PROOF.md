# R56 — Gap-independent two-block Farey merge and newest-source sufficient state

Author-side theorem/evidence, 2026-11-11. Frozen science `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`; continues R45, R49, R52, R54 and R55. This is an **auxiliary irrational circle rotation model**, retaining all original historical labels; it does not alter P000/X6.

## Definitions

Fix irrational `0<theta<1`, `m,H>=1`, integer `j`. Historical boundaries are the indexed phases `b_z={z theta}`, `z=0,...,m-1`. Source timestamps are `t=j-H,...,j-1`, with age `r=j-t`. The source at a boundary is in the arc beginning at that boundary. Let `tau_z(j)` be the smallest source age in historical arc labelled `z`, or `None` when empty. The original label `z` is kept, independently of phase rank.

## Theorem R56-A: exact two-block circular merge independent of empty index gaps

Separately take the *contiguous* index blocks `A=[0,m-1]` and `B=[j-H,j-1]`. For each block `[u,u+n-1]`, generate its R54 Farey-successor upper-error permutation `s_1,...,s_(n-1)`; then `[u,u+s_(n-1),...,u+s_1]` is the cyclic increasing fractional-phase order beginning at index `u`. Rotate each circular list to its smallest fractional phase; merge the resulting two increasing lists with history events before source events on equal phase. Initialize the current owner to the last history event in its globally sorted list. Traverse the merge, setting the current owner to each encountered history label and assigning each encountered source `t` age `j-t` to that owner. Return the minimum source age for each original label.

**Claim:** This returns exactly the full vector `tau(j)` for arbitrary integer `j` even when `|j|≫m+H`.

**Proof:** R54's successor permutation gives the exact circular order for each translated consecutive-index block. Rotation at the minimum fractional phase yields the corresponding global sorted list. Stable merge yields the exact sorted event union, including the right-inclusive boundary tie. From one historical boundary until the next, the active original label is precisely the containing historical arc. Every source is encountered once and assigned to precisely this label. The smallest age is its most recent source. No integer index in the unoccupied gap between the two blocks is traversed. QED.

For exact theta and `m,H>=1`, the generator uses `(m-1)+(H-1)` successor-index updates after **two** Farey brackets, plus `m+H` modular phase calculations, a linear rotation and `m+H` event merge. Storage is `O(m+H)`. Complete bit cost still depends on parameter precision and `log(|j|+H)` for phase arithmetic. For rational test parameters `p/q`, require `gcd(p,q)=1` and block lengths `<=q` so within-block phases are distinct; cross-block ties obey history-first assignment.

## Theorem R56-B: exact newest-only forward state

For a fixed historical partition and a chronological sliding window of width H, define `T_z(j)=j-tau_z(j)` for nonempty cells and `-infinity` otherwise. Let `d>=1`, `j'=j+d`, and let `N_z` be the latest timestamp `t∈[j,j'-1]` belonging to cell `z` (empty maximum `-infinity`). Then

```
T_z(j') = max(T_z(j), N_z)   when max(T_z(j),N_z)>=j'-H,
          -infinity         otherwise.
tau_z(j') = j'-T_z(j')      for nonempty cells.
```

If `d>=H`, previous timestamps may be dropped immediately; only the last H newcomers need classification. In general only `min(d,H)` new source phases are classified, with `O(log m)` comparisons per source after history-boundary ordering; materializing the full labelled result adds `O(m)` work.

**Proof:** All past source timestamps in a cell are at most its latest timestamp `T_z(j)`. If that latest timestamp expires at the new lower window boundary `j'-H`, all earlier ones expire too. The latest newcomer is `N_z`; their maximum, if nonexpired, is exactly the newest source in the new window. Induction proves identity across arbitrary finite chronological update sequences. Thus original-label threshold counts, stage-risk queries and other observers that are functions only of the full `tau` vector are preserved. QED.

**Observer-scope counterexample:** Arbitrary nonchronological removal of the newest source is a different operation. Source histories `{1,3}` and `{2,3}` for one cell have the same newest timestamp 3; removing timestamp 3 reveals different successors, 1 versus 2. This identifies exactly when older provenance must be retained.

## Exact verification

`VERIFY_R56.py` executed 660 deterministic small-rational cases: `m=1..11`, `H=1..15`, four selected positive, negative and remote `j` per pair, denominator `q=1009`, numerator coprime to q. All split-block results matched independently sorted/bisected phases. Five chronological batch advances per case produced 3,300 independent full-vector checks with 15,004 source insertion classifications.

Frozen S23/AV: `m=128`, `H=225`, `D=10^24`, `p_lo=262204504569236716045286`, `p_hi=p_lo+1`. Both endpoints agreed at `j=61,225` and matched the independently sorted source vector. For `j=±10^18` at each endpoint, a direct rational oracle again agreed; exactly **353 indexed nodes** were processed, despite an index gap of about `10^18`. Endpoint tests at huge j assert only these *rational endpoint* instances, not universal enclosure stability at that gap.

`CHECK_R56_FULL_RISK.py` independently combined the new split-block age vector at every one of the **78** frozen Farey stages with the pinned R55 exact compiler. All stage vectors agreed with the direct age oracle; the output was **9,697** events, **298** affine runs, **15,356** bytes, SHA-256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`. Last affine pair: `(-4017401528447,15321634290944)`.

These are author proof plus exact finite experiments; independent scientific review/admission is a separate project operation.

## Next

R57: batch R52's *observer-phase* cut crossings `z+r=s` into labelled transformations and distinguish them from Theorem B's fixed-boundary temporal sliding. Measure full integer-bit costs against R49 caching and R55 one-gap merge for varying `m,H,|j|`, parameter precision and desired observer horizons.
