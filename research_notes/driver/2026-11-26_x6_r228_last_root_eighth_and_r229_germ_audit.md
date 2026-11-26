# X6 (13,26): eighth-point and endpoint-germ exact necessary-condition tests

2026-11-26, RESEARCH_DRIVER EM-DVR-DEBB5E, informed continuation. Scope: Port 10 frozen weight chart (17t,B,22t,D)>0, 1935 directions, six BRC relations, strict 3/2 near-set and legal optimum; 47 previously audited support labels / 49 components. No new canonical Result/Review/Task acceptance.

Prior quarter-local certificate e4df81117daa97843037a89e9ebda72c52a575d5:research_notes/driver/2026-11-26_x6_r228_quarter_local_ray_resume.md. Prior author raw input 578fb612d9c52fa677c966740a99565d58fc98d7:research_notes/portable_direct/2026-11-26_r2_x6_r227_quadratic_root_wall_capacity.md (including corrected components k=5,16 in prior replay). Only root (13,26) reprocessed. Both branches remain feasible in each finite relaxation; this is not a continuous wall tree or actual output tree.

## Eighth point bank

Local C++17 exact integer implementation of the existing replay, replacing BigInt masks by bitset<256>, signed integer dot by __int128; normalized endpoint coordinates, successive clipping and j=0..8 interpolation identical to previous source. Pair cross and interpolation use signed 64-bit on these small inputs; for this data initial coordinates <=595 and successive clipping by normals (74,0,-1),(40,0,-3) produces normalized coordinates bounded by 10^6 (a direct coarse bound from the two cuts is below 10^9 before normalization); dot accumulated with 128-bit. For each pair precompute primitive unoriented normal and its two strict sign masks on all points. At recursion state S enumerate only pair IDs with both endpoints in S, deduplicate normals, compute strict masks A&S,B&S, require each child's label count <=2^(d-1)-1, recurse larger label count first. Base c<=d queries each label; rank shortcut if cross of first two points annihilates all S. Memo keyed by (d,S), only definitive booleans; cap 12,000,000 scans per side. No global partition dedup in this implementation. Reproduction using the previous JS replay: set n=8, old=[{i:13,j:26,counts:[25,23],sides:[{pass:null},{pass:null}]}], solve one side per invocation by leaving other pass=true, budget>=12000000 (scan order differs). Actual local compiled C++ results:

| side | labels | points | ray normals | pass | checks | calls | memo hits |
|---|---:|---:|---:|---|---:|---:|---:|
| product positive |25|203|19051|true|347554|226|48|
| product negative |23|194|17246|true|8121263|3823|1630|

No cap; no rank shortcuts. Count-cache sizes 298468 and 5595029. Both finite passes are weaker than continuous feasibility.

## R229 directed germs (author 02465133d14d57ba8ae20000a5357153bf047c01)

Read author's theorem and full replay. Independent successive clipping, exact BigInt lex signs, global central arrangement rays and transverse perturbations (v, ±w, ±p), deduplicated unordered strict masks; same mathematical query library, not blind independent discovery. For the sole residual root use two oriented germs per component, with distinct tags at coincident endpoints. Exact recurrence c(S)<=d success, c(S)>2^d-1 failure, otherwise all capacity-admissible partitions, sorted by max then total child labels, Boolean memo, cap 1,500,000. Actual result:

| side | labels | points | germs | rays | masks | checks | calls | pass |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| positive |25|29|50|325|647|8383|18|true|
| negative |23|27|48|294|603|9657|25|true|

No caps. Original R229's 18 exclusions are not counted as new here. The full arrangement library is necessary for germs (extreme ray alone may change the secondary sign).

## Next discriminating refinement

Subdivide each clipped open segment into smaller rational intervals and include both oriented germs on every subinterval. This is a valid stronger relaxation: any actual finite tree induces consistent eventual signs on each of the finitely many germ neighborhoods. A germ at an interior rational point cannot be erased transversely by passing through that point. All endpoint rays of the refined segments define the complete finite central arrangement, so the R229 query enumeration remains exact; pair extreme rays alone are not sufficient. A negative result excludes the original root; a positive one certifies only the refined finite relaxation. Use subdivision 2 first; preserve both old results, do not revisit 1127 excluded roots.
