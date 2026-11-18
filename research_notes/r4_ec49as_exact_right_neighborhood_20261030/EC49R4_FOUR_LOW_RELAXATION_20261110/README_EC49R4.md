# EC49R4 — Exact 64-edge lower bound from the H4/H6/H7/H8 low-signature slice of the frozen 24-label BRC objective

Date: 2026-11-10 Asia/Shanghai. Classification: **AUTHOR_EXACT_FINITE_THEOREM / INTEGER_DP_EXECUTED / INDEPENDENT_WORD_AUDIT_PASS / UNREVIEWED / NOT_ADMITTED**. Researcher-ID `EM-DIRECT-DC91B4`; Research-Activity-ID `RA-24112E361A2904DB33393759`. Frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact subproblem and scope

Use the original signed-X6 ordered primitive codewords `a=(-1,-1)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`, `f=(1,-1)`, `g=(2,-2)`. An integer denotes a signed **native axis**, not one-dimensional signed displacement. The original nine-state DFA and terminal-signature table are at `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git Blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.

Retain four exact **high-signature** frozen mother paths: H2:16=`fe`, H2:32=`ge`, H3:16=`feg`, H3:32=`gef`. They have **16 different nonempty signed-native microstep prefixes**. For each horizon h in {4,6,7,8}, select one length-h operation word for each of four **low** signatures {1,2,4,8}, satisfying `#e=#a+1>=1` and a strictly positive complete BRC key `K=(h+1-#g,h+1-2#e-#f,#e)`. This gives 20 demands/paths.

This is an explicit relaxation of the original 24-label mother: allow *different* low paths within one horizon to have different positive complete keys, impose no global key budget, and omit H5/H9 high-signature demands. Minimize the number of **distinct nonempty ordered signed-X6 primitive-step prefixes** in all 20 paths. Preserve original frozen operation-to-primitive expansion, observation state, endpoint and provenance.

## Theorem — complete exact finite classification

```text
min C_native(H2-high,H3-high,H4-low,H6-low,H7-low,H8-low) = 64
```

The complete enumerator produces respectively **176**, **4,932**, **25,060**, **125,680** legal low-candidate operation words at H4,H6,H7,H8: **155,848** candidates total. Their native ordered signed-prefix Trie contains **623,045 nodes including root**.

Assign a different bit to each of the 16 low-signature demands. At trie vertex v, D_v(S) is the minimum additional edge cost for covering mask S using descendant terminal words. Assign baseline H2/H3 prefix edges weight zero and every other edge weight one. A terminal can supply its own label at zero descendant cost. At a child edge e, merge masks A and B:

```
D_after(A union B) = min(D_before(A) + D_child(B) + w(e)*[B != empty]).
```

Mask overlap is permitted in the implementation: removing redundant selected paths cannot increase prefix cost, so overlap and exactly-once formulations share the same minimum. Induction on trie height establishes that all legal label assignments are represented and each nonbaseline signed-prefix edge is charged once. Exact root result is **48 new edges**; with the 16 fixed baseline edges the minimum is **64**. The actual integer DP ran through **1,828,108 states** and **25,275,504 mask combinations**, without floating-point optimization or candidate sampling.

## Exact 64-edge attaining witness

| h | signature 1 | signature 2 | signature 4 | signature 8 |
| --- | --- | --- | --- | --- |
| 4 | `gefd` | `fegd` | `fegc` | `gefc` |
| 6 | `gefdff` | `fegdff` | `fegcgg` | `gefcgg` |
| 7 | `gefdfff` | `fegdfff` | `fegcggg` | `gefcggg` |
| 8 | `gefdffff` | `fegdffff` | `fegcgggg` | `gefcgggg` |

Together with the four frozen H2/H3 paths, all 20 words have native signed-X6 displacement `(+2,0,0,0,0,0)` and the declared terminal outputs. A **separate direct Cartesian-product enumerator** (not the DP's recursive generator) reproduces all four pool sizes; independent literal signed-primitive expansion recomputes **64** distinct prefixes. The selected 16 low words use **seven distinct complete positive keys**, with multiple keys in some horizons: **this is not a full mother-model five-key witness**.

## Valid consequence for frozen mother task

Any valid solution of the **original 24-label** mother task contains these four exact H2/H3 high seeds and the specified H4/H6/H7/H8 low requirements. Thus its complete signed-native prefix cost is at least **64**, even after the original one-full-key-per-horizon and at-most-five-keys rules are reinstated. A target solution with total cost <=93 must meet the missing H5/H9 high demands using **at most 29 further distinct prefix edges**, possibly fewer depending on its actual 20-demand base cost. This is a necessary budget, **not** a proof of infeasibility or existence under the five-key restriction.

Two related separately computed relaxed cases gave exact minima 52 (H7/H8 only) and 56 (H6/H7/H8 only), with the same fixed H2/H3 high baseline. A complete unrestricted 24-label DP attempt did not finish within a 120-second execution limit, and **no full mother optimum is claimed**. Previous auxiliary H2-low or H7-high mode papers use different mother demands and do not transfer automatically.

## Evidence and continuation

Files beside this note: `VERIFY_EC49R4_EXACT_DP.py` and `ec49fgd_mixed_seed_dp.py` are the exact integer Trie DP and frozen nine-state/native signed-code generator; `VERIFY_EC49R4_INDEPENDENT.py` supplies a separate word-language and witness audit; `EXACT_REPORT_EC49R4.json` is the actual 64-edge result; `DP_RUN.log` and `INDEPENDENT_RUN.log` are execution records. Both Python scripts ran successfully using standard-library exact integer arithmetic.

**Next precise question:** jointly constrain all H4–H9 signature paths to one complete key per horizon, at most five globally, and include H5/H9 high labels, optimizing signed-native prefix sharing while retaining the original four H2/H3 **high** seeds. Start with the 64-edge relaxed 20-demand core as an admissible lower-bound tool, use key-conditioned branch decomposition or 2-stage DP to avoid the unrestricted 20-bit trie explosion. Exact owner/CLAIM remained unavailable: native query for historical `EC49AS` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`. No formal Result, Driver acceptance, Source Foundation change, P000 change or ACTIVE-worldview modification is asserted.
