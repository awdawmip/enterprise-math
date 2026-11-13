# EC49FNV — Exact bidirectional low-layer frontier transfer with changing root domains

**2026-11-14 · Frozen input** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · Independent finite proof and executed C++17 certificate · **NOT_REVIEWED**.

## Scope, prior art and genuine increment

Continues EC49FNT ([PR #2325](https://github.com/awdawmip/enterprise-math/pull/2325)) and acknowledges independently published EC49FNU ([PR #2330](https://github.com/awdawmip/enterprise-math/pull/2330)), which already proved one-sided superset-sensitivity transfer on 82 common-domain edges and directly checked two domain expansions by enumerating 1,296 extra complete assignments per expansion. **This note does not re-claim the FNU theorem or 84-edge equality.**

The new result is a **bidirectional, root-domain-aware transfer procedure**: source cutoff frontier pruning by exact *target partial* native-root DP, selective repairs only when that direct target bound becomes unsafe, and bounded searches only for root choices newly available in the target. It certifies both orientations of all 84 edges, i.e. 168 directed transfers, without rerunning a complete target assignment DFS for each transfer.

The finite input is precisely the EC49FNT local evidence package: 94 cached complete keys, 178,850 legal ordered-signed native words, 24 distinct demand labels, roots 03/05/06/07 and the 84 first-neutral edges among cases 32000–32999. Input files and their SHA256 hashes are listed below. The original 1,000-case optimization is **not** repeated.

## Theorem — complete transfer of a low-layer assignment certificate

Let `D_{K,r}(S)` be the exact nonempty native rooted-prefix cover cost of demand subset `S` at legal root `r`, allowing other labels to be covered. Its monotonicity, `S⊆T ⇒ D_{K,r}(S)≤D_{K,r}(T)`, follows by reusing a cover of `T` for `S`. A lawful complete root allocation `a` costs `F_K(a)=Σ_r D_{K,r}(S_r(a))`.

Run a source `K` cutoff DFS at integer threshold `b`, preserving its complete low leaves `L` with costs `≤b` and its disjoint *first-pruned partial* frontier `P` with source lower bounds `LB_K(p)>b`. For target `K'`, make three checks:

1. Each source cut `p` either is not a lawful partial target assignment, has exact target lower bound `LB_{K'}(p)>b`, or is **selectively refined**, branching only below that cut with target legal options and the monotone target cutoff. Record any target-low complete leaf found in the refinement.
2. Re-evaluate each source complete low leaf under exact target rooted costs, discarding target-illegal or target-above-cutoff leaves while retaining its allocation identity and exact new cost.
3. For every **target-only** legal root choice `(label,root)` absent from the source legal domain, run a target bounded search forced to contain that choice. Retain each complete target-low assignment, deduplicated by allocation identity.

The union of retained leaves in (1)–(3) is **exactly** the target low-layer identity/cost map `A_{K'}(b)`.

*Proof.* Any lawful complete target allocation either contains some target-only legal choice, and so is covered by (3), or uses only source-lawful choices. In the latter case, completeness of the source search partitions it into one source leaf or a unique source cut subtree. A leaf is handled by (2), and a cut subtree by (1). A target-illegal partial assignment has no lawful target extension. An exact target lower bound above `b` excludes every extension by native-root monotonicity. The selective refinements and target-only searches exhaust their explicitly enumerated legal options and only prune with these valid lower bounds; hence the procedure has no missing or spurious allocation at cost `≤b`. QED.

If the transferred map equals `A_K(b)` and contains the minimum `C` and the next distinct cost `S` with `C<S≤b`, the two endpoints have the same `C`, minimizer count `m`, and strict gap `g=S−C` (EC49FNT Proposition 2).

The theorem is about exact *finite* root-domain and complete-assignment semantics. It is not a universal performance or asymptotic complexity bound. Rooted subset DP construction is still needed at the target; only the target's complete low-cost root-assignment tree is avoided.

## Executed finite certificate — 168/168 directed transfers

The attached C++17 program independently rebuilds source cutoff maps for the 51 endpoints from the frozen native words and checks their known `C,m,S`. It then transfers each source frontier to its edge-neighbor **in both directions**. All arithmetic is integer-exact. The 168-row output is included losslessly, not sampled.

| Certificate count | Exact |
|---|---:|
| Undirected edges / directed orientations | 84 / **168** |
| Matching-domain transfers / domain-changing transfers | 164 / 4 |
| Source cut nodes tested at targets | 16,876 |
| Source cut nodes with target bound `≤b` | **18** (9+9) |
| Selective repair nodes / nodes pruned | **84 / 62** |
| Complete low-cost leaves found by repair | **0** |
| Target-only root choices checked | 4 |
| Target-only bounded-search nodes / pruned nodes | **592 / 344** |
| Complete low-cost new-domain leaves | **0** |
| Source low-cost complete leaves checked at target | 512 |
| Exact target leaf costs changed | **0** |
| Successfully transferred first two-layer maps | **168/168** |

The four different-domain directions are `32315↔32279` and `32318↔32279`. Only `32279` has two additional legal choices, root 03 for labels 11 and 13. In either expansion direction to `32279`, nine previously pruned source nodes require selective repair, which visits 42 nodes and prunes 31; the two new-root searches visit 296 nodes and prune 172. Neither route finds a low-cost completion. The reverse directions require no selective repair and no new-domain search.

**Sharper comparison with EC49FNU:** its general superset-deviation envelope classified 390 unsafe old frontiers over 22 common-domain source→target edges; here **exact target rooted partial costs** eliminate all target cutoff failures on the 164 common-domain *directed* transfers. The difference is in the certificate strength and evaluated states, not a new claim of changing original optimal costs. EC49FNU's 1,296 extra complete allocations per expansion are replaced here by two targeted cutoff searches visiting 296 nodes per expansion, plus the 42-node cut repair. No end-to-end speed ratio is claimed.

## Reproduction and integrity

The following saved files are base64-encoded xz of actual UTF-8 content. Decode with `base64 -d | xz -d`. `VERIFY_EC49FNV.cpp.xz.b64` contains the executed verifier (local filename `VERIFY_EC49FNU.cpp`); `EC49FNV_RESULTS.txt.xz.b64` contains all 168 result rows (local filename `EC49FNU_RESULTS.txt`). Original file bytes SHA256:

- Verifier source: `942c584c51d572a588b96dbde5803d50d8db49b6b037072cffe74401d1ac4dcd`
- 168-row result: `76345af1c0e66764a1a953f258dd04a018982cb1f635f967b5eda50044cdcaa4`

Reproduce with the unchanged prior scientific files:

```sh
base64 -d VERIFY_EC49FNV.cpp.xz.b64 | xz -d > VERIFY_EC49FNU.cpp
base64 -d EC49FNV_RESULTS.txt.xz.b64 | xz -d > EC49FNU_RESULTS.txt
g++ -O2 -std=c++17 VERIFY_EC49FNU.cpp -o verify_fnv
./verify_fnv FIRST_NEUTRAL_EDGES_EC49FNS.txt EXACT_NATIVE_32000_32999.txt < master_and_radius3_cases.txt > reproduced.txt
cmp reproduced.txt EC49FNU_RESULTS.txt
```

Frozen original input SHA256: `master_and_radius3_cases.txt` = `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `FIRST_NEUTRAL_EDGES_EC49FNS.txt` = `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`; `EXACT_NATIVE_32000_32999.txt` = `c9314021942397a0b5a3e7a90d965fb19a853bdc486f7610721fc748a057c0f9`.

The prior EC49FNT eight-file SHA256 manifest passed; the optimized source was compiled and executed twice with identical output. A cross-build at `-O0` exceeded a bounded local attempt and is **not** presented as independently verified. The output table was independently parsed for 168 distinct oriented edges, all passes and all listed aggregate counts.

### Current status / next concrete question

Independent author result `NOT_REVIEWED`; no Task `RS-EC49AS` CLAIM or Result asserted. The remaining useful mathematical question is a *uniform rooted perturbation envelope* that transfers whole source cut frontiers without even evaluating the target exact rooted cost at every cut node. For changing legal domains, seek a combined inequality that excludes all newly enabled root choices directly.

Formal task ownership, result freeze, independent review and Foundation admission remain separate.
