# EC49FFG — Exact interval-hitting oracle for BRC signature quotas, with lexicographic key-depth optimization

Date: **2026-11-09** (Asia/Shanghai). Scientific input retained at immutable pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-side finite theorem and exact standard-library computational audit. P000/ACTIVE worldview unchanged. Source-native research CLAIM and independent Driver admission remain to be established by their own authority.

## Mathematical setting

Take the original six-operation ordered signed-native-X6 BRC model, nine-state observer and complete key `K=(x,y,z)` from the frozen source, with count-admissible `x>=2z`, `y>=0`, `z>=1`; also consider the stricter positive domain `x,y,z>=1`. The observation windows are `H2..H9`. Distinguish four low terminal signatures `1,2,4,8` and two high signatures `16,32`. We ask for the **minimum number of distinct full keys** needed to realize every requested signature by some legal ordered BRC word. Separate words may serve different requirements; one key may serve multiple words and windows. This is a coverage question, not yet a minimization of the union of ordered signed-native-X6 path prefixes.

The verified EC49FFD observer staircase says that a key whose terminal horizon is `H=x+y-1` produces **all four low signatures** at every integer `h` with

`H - min(x-2z,y) <= h < H`, 

and high signatures at `h=H` (16 iff `x>2z`, 32 iff `y>0`). The EC49FFF canonical domination theorem permits replacing any key with `H>=3`, for *signature quota cardinality only*, by the canonical `K_H=(2+floor((H-1)/2), H-1-floor((H-1)/2), 1)`; it has both high labels at `H`, and low labels precisely at

`ceil((H+1)/2) <= h < H`.

At `H=2`, high 16 and 32 require distinct keys `(3,0,1)` and `(2,1,1)` (and high16 is unavailable in the strictly-positive domain).

## Theorem 1: exact greedy minimum-cardinality oracle

Represent a requirement mask by low-window bits `L_h` for `h=2,...,9`, by high-window bits `U_H` for `H=3,...,9` (one bit means either or both of high16/32 are required), and by separate H2 bits for high16, high32. These are the 17 bits of EC49FFF.

For every high requirement at `H>=3`, force the canonical key `K_H`; for each H2 high bit, force its corresponding distinct key. Let `S` denote the resulting forced terminal horizons `H>=3`.

**Algorithm.** Scan the required low windows `h=2,3,...,9` in increasing order. A low requirement at `h` is already satisfied precisely when `S` contains a terminal horizon within the integer interval

`I_h=[h+1,2h-1]`.

For every low requirement not yet covered, add the canonical key with terminal horizon `H=2h-1` to `S`. The number of forced H2 keys plus `|S|` is **exactly the global minimum full-key cardinality** for that mask. If `x,y,z` are strictly positive and H2 high16 is demanded, the instance is unreachable.

**Proof.** The staircase implies the equivalence `canonical K_H supplies low at h <=> h+1<=H<=2h-1`. A high signature at `H>=3` forces some key with that exact terminal horizon; its canonical representative supplies both high signatures and dominates all low capabilities. H2 high bits force the two distinct H2 representatives as specified. Remove low intervals already hit by these mandatory points. It remains to stab a set of integer intervals `I_h` with additional terminal points. As `h` increases, both the left endpoint `h+1` and the right endpoint `2h-1` increase. For the earliest uncovered interval `I_h`, any solution must select some point `q` in that interval; replacing `q` by its right endpoint `r=2h-1` still stabs `I_h` and every later interval that `q` stabbed, because the later intervals have right endpoints at least `r` and left endpoints at most `q<=r`. This exchange does not increase the number of points. Repeating proves the right-endpoint greedy optimum. The canonical theorem gives an actual BRC key and observer word for each selected point. QED.

The minimum cardinality can therefore be queried without enumerating subsets of 17 keys or a table of 131,072 requirements. For `H2..HU`, a direct scan costs `O(U^2)` elementary comparisons as written, and can be implemented with a linear number of interval selections and a compact ordered set.

## Theorem 2: exact secondary canonical-length dynamic program

For a selected canonical key `K_H` the number of ordered native signed-X6 microsteps in any word equals `2(x+y+z-1)=2(H+1)` because `z=1`. H2 keys each have length **6**. Define the secondary surrogate objective as the **sum of one native word length per selected canonical key**, optimized lexicographically after minimizing the number of keys. This proxy tracks minimal representative depth; it is not the native prefix-union edge count.

Remove the low requirements already hit by the forced high keys. Let the remaining low horizons be `h_0<...<h_{m-1}` and write `F(m)=(0,0)` for `(extra key count, extra length sum)`. For every `i<m`, define

`F(i) = lexmin_{H=h_i+1,...,2h_i-1} [(1,2(H+1)) + F(j(i,H))]`,

where `j(i,H)` is the first index `j>i` such that `h_j>=H` (or `m` if none). Append the forced high keys and their lengths. **This recurrence gives the exact lexicographic optimum** in the canonical representative family.

**Proof.** Any solution of the suffix low requirements must choose a terminal horizon `H` in `I_{h_i}` to cover its first interval. Since both endpoints of `I_h` increase with `h`, that chosen point covers exactly a consecutive prefix of the still-uncovered suffix: `h_i,...,h_{j-1}` with `h_j>=H`; it covers no later unfulfilled low interval. Therefore all remaining requirements form precisely the suffix beginning at `j`, and an optimal suffix solution can be appended. Taking the lexicographic minimum over all permissible `H` proves the recurrence by induction on the suffix length. Forced high keys have fixed cardinality and canonical lengths, so appending them preserves the optimum. QED.

A monotone `j` pointer as `H` increases gives at most `O(U^2)` integer operations per mask, using `O(U)` states, for the bounded H2..HU family.

## Exact new examples and full independent checks

All eight low windows H2..H9 need **exactly four** keys. The key-count greedy right-endpoint witness has terminal horizons `(3,5,9,17)`, with keys

`(3,1,1), (4,2,1), (6,4,1), (10,8,1)`,

and canonical-length sum **76**. The secondary dynamic program finds another exact four-key solution with horizons `(3,4,6,10)`:

`(3,1,1), (3,2,1), (4,3,1), (6,5,1)`,

whose canonical-length sum is **54**. This is an exact reduction of **22 native microsteps in the surrogate sum**, not a claim about native prefix-union edge savings.

All eight low signatures together with high observations at H3, H5, H7 and H9 need **exactly five** full keys. The greedy canonical witness has horizons `(3,5,7,9,17)`; the independent exhaustive verifier returns the same minimum cardinality.

The standalone programs prove their finite census claims by integer enumeration of the entire 17-bit requirement space. `VERIFY_EC49FFG.py` checks every mask against an independently implemented 17-key-subset enumeration plus min-over-supersets transform. Both count-admissible and strict-positive domains match EC49FFF's exact cardinality histograms in all **131,072 masks each**: `62,232` and `40,976` masks, respectively, are realizable with at most five keys. `VERIFY_EC49FFG_SECONDARY.py` computes the lexicographic minimum by independent full-subset enumeration. `VERIFY_EC49FFG_DYNAMIC.py` then checks the recurrence against that independent enumeration for all 131,072 count-admissible masks and all 65,536 reachable strict-positive masks, **zero mismatches**.

The greedy minimum-cardinality witness has a larger canonical-length sum than the secondary optimum in **93,216** of 131,072 count-admissible masks; the analogous difference occurs in **46,608** of 65,536 reachable strict-positive masks. The maximal observed difference in either domain is **22**. These counts concern the precisely defined surrogate and follow from exhaustive finite exact computation.

To reproduce locally from this folder (Python standard library only):

```bash
python VERIFY_EC49FFG.py
python VERIFY_EC49FFG_SECONDARY.py
python VERIFY_EC49FFG_DYNAMIC.py
```

The generated `EXACT_REPORT_EC49FFG.json` and the three `RUN_EC49FFG_*.txt` files contain the actual checked results. Scripts use no floating-point comparisons. `VERIFY_EC49FFG.py` directly computes the canonical coverage masks, and the brute-force and dynamic algorithms are independently implemented. Soundness of the reduction to canonical representatives uses the explicit EC49FFD/EC49FFF observer theorem and the frozen original nine-state DFA sources.

## Scientific application, status, next concrete question

**New reusable interface:** fast exact minimum-key feasibility and a lexicographic low-depth canonical representative selector for arbitrary H2..H9 observer quota masks. The selector can reject any mask requiring >5 keys and prioritize shallow reachable candidates without running the original 17-key subset search. This complements, but does not replace, native ordered-path prefix optimization.

**Next EC49FFH:** choose five-key or fewer observer quota masks not contained in previously classified 22/23/24-path structures. Recover actual original keys and complete ordered six-axis words (which may outperform cardinality-canonical representatives under prefix sharing). Search for a legal `C_native<=93` witness or establish a case-specific exact prefix lower bound with the existing disjoint-prefix/dual certificate methods. First test the explicit new 4-key all-low family with multiple high requirements, using exact native word generation; do not infer prefix savings from the surrogate.

**Scientific and control status:** author-checked analytical finite proof; exact exhaustive computational validation. The linked native source identity/CLAIM/Result and independent Driver mathematical review require their own current control receipts. The research artifacts are preserved on the existing authorized project PR branch, not promoted automatically to main or Foundation.

### Immutable provenance

- Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (preserved, not rebased).
- Original operation counts and native length: EC49FFC at `2dd856c416f111d90d523dcb10cde952248ec814`.
- Observer staircase and all-signature reachability: EC49FFD at `df0dbc54707a6926db858631e5a03fea189dccde`.
- Canonical key domination and exact original quota census: EC49FFF at `58cdba9c360bc180028183cff711405d2e2f37c0`.
- Model: signed X6 primitive microsteps, complete BRC key and original nine-state observer; no new P000 or WORLDVIEW axiom.
