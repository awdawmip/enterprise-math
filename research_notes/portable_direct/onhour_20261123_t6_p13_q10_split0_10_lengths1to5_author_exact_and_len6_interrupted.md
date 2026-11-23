# T6 p13: exact qorder10 split(0,10), named negative lengths 1–5; length6 interrupted observation

Date: 2026-11-23. Mother Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, frozen scientific task input `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. This author work proceeds from the saved complete p13 qorder9 signed split(4,5) positive q-pattern(1,1,1,1) result, not from a Native CLAIM. Prior research at other maximal primes and the separately delegated Source p17 q14 preflight remains distinct.

## Exact finite result

For maximal prime p=13, valuation one, total vertical qorder10, and signed split `(0,10)`, negative named atoms `(q,r)` have full composite denominator `a=13(13q+r)` and original mass `169q+13r-1`. Negative qorders sum to10. Both full original sides have exponent mass at most2331, all named multiplicities and signs are retained, and the original `H0,...,H6` moments imply the six mixed inverse-power congruences modulo `13^j`, for `j=1,...,6`. Smaller-prime completion is still a separate obligation.

The existing *saturated* 12D q0 integer lattice has index `13^21=247064529073450392704413` and minimum exact rational GS squared diagonal `78577530278042129705264382752517501995032553011464356025 / 4243983974238642688103181306691645151538473248349`. This is above `2(2331)^2` and therefore above the squared radius `(2331)^2+(2331-c_minus)^2` for every vertical-budget-eligible q10 roster. Exact rational nearest-two reverse-GS recursion exhausts the necessary affine ball.

All canonical named negative rosters of lengths 1,2,3,4,5 have been enumerated and checked:

| negative named length | all qorder10 rosters | over vertical mass budget | exact GS nodes | necessary ball leaves | original side-budget-valid |
|---|---:|---:|---:|---:|---:|
| 1 | 12 | 0 | 26 | 0 | 0 |
| 2 | 654 | 0 | 1,836 | 0 | 0 |
| 3 | 10,656 | 0 | 29,637 | 0 | 0 |
| 4 | 79,704 | 0 | 219,819 | 0 | 0 |
| 5 | 324,012 | 5,061 | 878,117 | 3 | 0 |
| **Total** | **415,038** | **5,061** | **1,129,435** | **3** | **0** |

Three exact sphere candidates in negative length5 were retained in the [length5 certificate](../../research_checks/T6_P13_Q10_SPLIT0_10_NEG_LEN5_AUTHOR_EXACT_CERT_20261123.json); their original positive/negative masses are respectively `(1910,4891)`, `(2452,6110)`, and `(4720,2681)`. All their six signed mixed-congruence residues are zero. All violate the original 2331-per-side mass limit.

The author-executed full local JSON certificate SHA256 values for lengths1 through5, respectively: `9f6fd32b47185f48180ef3b679b316bb3c4a7277f0deceb92d8b3e3696b7bce3`, `de59a65d856b48afe368ab8811a7c55755a99c230b1c4dead570363069819f1a`, `d58fb94839ccaeabe0447356eafe5cb8ba29ee8f206009d6860c8bca8bf998f5`, `1e12170b8ec0e2035d994255ac34e4b2699cc1c3bf51d783fd2a3c87f381f5cd`, `8cf1f484e605c350359ce9a0a122fb248017534429c8132950192a29209d7891`. These full local JSON files were executed and hashed; compact exact certificates and a Python replay source have been published to GitHub. The GitHub replay wrapper has **not** been separately rerun after publication, and these are **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**, with no independent mathematical admission.

## Complete roster domain and exact mass prefilter

Independently, the exact integer generating function
`F(x,z,y)=product_{q=1..10,r=1..12}(1-x^q z y^r)^(-1)`, truncated at `x^10`, enumerates qorder10 named multisets by length and residue sum `S`. Their negative vertical mass equals `1690+13S-length`. The mass cap is equivalent to `S<=floor((641+length)/13)`. Integer DP gives **5,098,938** full named rosters, of which **2,795,372** pass this necessary vertical budget and **2,303,566** exceed it. The per-length exact census is in [the integer-DP certificate](../../research_checks/T6_P13_Q10_SPLIT0_10_INTEGER_ROSTER_MASS_CENSUS_20261123.json). Direct exact length5 search independently observed 5,061 overbudget rosters, matching DP.

Consequently **409,977** vertical-budget-eligible rosters in lengths1..5 have received the exact GS test; all have no legal compensation. **2,385,395** eligible rosters are in lengths6..10 and remain to be finished (with the partial observation below).

## Interrupted length6 computation — preserve without promoting

An attempted exact negative-length6 full sweep was stopped by host computation timeout. A stdout log shows that the first three of five q-partitions were fully processed as follows:

- `(1,1,1,1,1,5)`: 52,416 named rosters, 7,247 vertical-overbudget, 124,398 GS nodes, 0 sphere leaves, 0 budget-valid.
- `(1,1,1,1,2,4)`: 196,560 rosters, 25,082 overbudget, 471,338 nodes, 2 sphere leaves, 0 budget-valid.
- `(1,1,1,1,3,3)`: 106,470 rosters, 13,872 overbudget, 253,633 nodes, 3 sphere leaves, 0 budget-valid.

These three rows total 355,446 named rosters and 849,369 exact GS nodes **as observed in interrupted process output**. The process terminated before writing its output JSON, so the five leaf witness vectors and durable exact per-partition certificates are not saved. Treat these as `CALCULATED_LOG_ONLY / WITNESS_READBACK_PENDING`, not an accepted or complete six-atom certificate. The fourth q-partition was interrupted, the fifth not visited; neither is classified EMPTY.

## Next exact action and control provenance

The smallest remaining evidence completion is **negative length6**: reconstruct and persist five provisional leaf witnesses for the first three partitions (or reproduce those three patterns if necessary); complete and certify `(1,1,1,2,2,3)` and `(1,1,2,2,2,2)`, then continue negative lengths7..10. Reuse completed and independently pinned length1..5 computations. Keep the global p13/lower-prime and `T6=2332` goal OPEN.

Native read `onhour-20261123-1144-t6-live-task-ro-v1` returned `SUCCEEDED/error=null` at its admitted Source snapshot. Sites recovery using historical bridge SID `MCP-de3e5bafb24f43f4a5e6285e7601676a` returned `OWN_SESSION_REGISTRATION_NOT_FOUND`; current-client line `T6` checkpoint read returned `CHECKPOINT_NOT_FOUND`. These observations do not invalidate prior GitHub authorship or prior conversation client checkpoints; this run **does not authenticate a current winning native CLAIM/run**, publish protected semantic PROGRESS, bind the historical Research Activity, or use the maintenance lane. Local/remote scientific publication is distinct from canonical native Task progress. No scheduler or notification setting was changed.
