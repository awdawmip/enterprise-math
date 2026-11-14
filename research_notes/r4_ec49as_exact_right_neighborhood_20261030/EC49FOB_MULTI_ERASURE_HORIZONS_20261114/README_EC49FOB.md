# EC49FOB — Exact BRC multi-erasure horizon 10 and minimal forcing cores

Date: 2026-11-14. Status: author-side exact finite enumeration, **NOT_REVIEWED**. Continuing EC49FOA, PR [#2352](https://github.com/awdawmip/enterprise-math/pull/2352), immutable author commit `25c1a57c326df1a62c193a60501ca4d1fcf14a59`. Frozen scientific input pin remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Precise proposition

Fix a lawful partial allocation of 24 distinguishable demands to native legal first-microstep roots 03, 05, 06, 07, with current assigned masks `S_r`, unassigned set `U`, legal root sets `R_i`, and exact rooted signed ordered-prefix minimum-cover costs `D_r` computed from the pinned frozen words. For any future subset `T ⊆ U`, put

`f_p(T)=min_{rho∈∏(i∈T) R_i} Σ_r D_r(S_r ∪ {i∈T:rho(i)=r})`.

Then `T⊆T' ⇒ f_p(T)≤f_p(T')`, by restriction of any lawful root placement for `T'` and monotonicity of each `D_r`. Thus the family `{T⊆U:f_p(T)≤B}` is down-closed. At threshold `B=155`, its **minimum obstruction cardinality** is precisely

`h*(p)=min{|T| : T⊆U, f_p(T)>155}`, if the set is nonempty.

Equivalently, `h*(p)=min{h:H_h(p)>155}`, with `H_h(p)=max_{|T|=h} f_p(T)`. If no such subset exists, `F(p)=f_p(U)≤155`, and an exact lawful full placement witnesses feasibility. An exhaustive census of subsets and native legal roots is therefore a complete finite certificate for the asserted `h*`. This proof relies on the native rooted minimum-cover model rather than additive independence of demands.

## New finite results

Nine distinct EC49FNY cuts from the frozen cache case 32279 are used. Exactly `k` **distinct previously assigned labels** are erased from their rooted masks, leaving all other masks unchanged. Each resulting state is lawful but auxiliary, with no assertion it occurred in a historical DFS trace. For `k=2,3`, **all** unordered erasure combinations at **all nine** cuts were enumerated. For `k=4…7`, a precisely selected one-cut family was explored; those rows are not full-population censuses.

| Erasures `k` | Coverage | States | First strict horizon by depth (number of states) | Full feasible `F≤155` |
|---:|---|---:|---|---:|
| 2 | Complete, 9 cuts | 2,081 | h1:211; h2:722; h3:705; h4:357; **h5:18** | 68 |
| 3 | Complete, 9 cuts | 13,902 | h1:360; h2:2,318; h3:4,427; h4:3,937; h5:1,977; **h6:146** | 737 |
| 4 | Pattern 159571690231449, include label 15 | 1,140 | h4:4; h5:87; h6:406; **h7:455** | 188 |
| 5 | Same pattern, include 4,5,6,15 | 17 | h7:4; **h8:11** | 2 |
| 6 | Same pattern, include 4,5,6,8,15 | 16 | h8:4; **h9:10** | 2 |
| 7 | Same pattern, include 4,5,6,8,9,15 | 15 | h9:4; **h10:9** | 2 |

Together these disjoint, explicitly scoped groups contain **17,171** distinct state-enumeration records, including **a strict horizon-10 witness**.

## Sharp ten-demand obstruction

Base pattern `159571690231449`. Erase exactly `[4,5,6,8,9,10,15]`, leaving rooted masks `[0,5312517,8667274,10240]` and remaining demands `[4,5,6,8,9,10,15,17,19,21]`.

The exact complete sequence of maximal minimum costs is

`(H1,H2,H3,H4,H5,H6,H7,H8,H9,H10)=(122,132,140,143,146,149,151,153,155,156)`.

Every future subset of at most nine labels admits a legal rooted allocation of cost at most 155; all ten together have minimum exactly **156**, attained by roots `[06,05,05,05,06,06,05,06,05,06]` in the stated label order. This proves `h*=10` for this particular partial allocation and threshold. The `k=7` selected family contains nine such horizon-10 witnesses.

The earlier one-erasure horizon-4 witness therefore extends within this frozen exact finite model to selected horizon-5,6,7,8,9,10 obstructions under additional legal erasures. The result establishes no global horizon bound outside the declared finite families.

## Reproduction and integrity

Source files are **unchanged**: `master_and_radius3_cases.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, `EC49FNY_CERT_ALL.txt` SHA256 `708da9a677ecf1d7842daf732ea51c796262a2974ef3476c9ef34f2f4107b271`. The Python dependency `VERIFY_EC49FNY_INDEPENDENT.py` is the previously published independent native prefix-trie DP from [PR #2343](https://github.com/awdawmip/enterprise-math/pull/2343), verified alongside the pinned files. The exact 94-key/178,850-word source is used, and every eligible root choice and future-label subset is enumerated with integer arithmetic.

Place these three pinned inputs alongside `VERIFY_EC49FOB.py`, then execute:

`python VERIFY_EC49FOB.py master_and_radius3_cases.txt EC49FNY_CERT_ALL.txt EC49FOB_ALL_CENSUSES.json`

The new verifier checks both frozen hashes, rebuilds all four rooted cost functions from original signed words, reconstructs nine distinct cuts, checks every classification and exact full optimum, and writes every member of all six census groups. The uncompressed complete machine-readable output obtained by the author has SHA256 `9bdacc2449dab2ba135846c978f1895d08fe95121b8860261168380c19b53b2a`. All six expected histograms assert in code, so a mismatched run fails.

Original full census, code, input copies and verification logs are also available as a separately delivered user artifact. This PR stores a reproducible verifier and full mathematical report; the generated large JSON is not duplicated as a GitHub source file. Scientific results are author-validated finite computations, **not** independently reviewed or a formal task Result.

## Next scientific question

Find an observer-safe exact certificate for the minimal forcing subsets that avoids testing all future-label subsets. In particular, classify which root-sharing interactions cause late `h*` and determine the true largest obstruction cardinality within the pinned 24-demand configuration. Compare these auxiliary ancestors with actual recorded DFS cuts and separately test nonstable neighboring caches without repinning the science.
