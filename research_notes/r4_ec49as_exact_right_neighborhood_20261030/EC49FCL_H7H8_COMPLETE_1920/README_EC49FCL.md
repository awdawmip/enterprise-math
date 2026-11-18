# EC49FCL — exact 1,920-group early3 + H7 + H8 five-path rigidity

Date: 2026-11-06. Status: AUTHOR_EXACT_FINITE_CHECK / UNREVIEWED / PORTABLE_DRAFT. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact proposition
Use the frozen `frozen_model.py` path words, 9-state signature observer and full BRC cache-key constraints L=(4,2,1), M=(7,3,2). Ten H4–H6 slots comprise the early family; H7 and H8 have four signature slots each. The 1,920 selections are ordered by `itertools.combinations(early,3)`, then increasing H7-signature order and H8-signature order. For every one of these selections S, hold the other 19 of the original 24 paths fixed and replace the five selected paths by any legal words of their frozen individual pools. The exact minimum number of distinct nonempty ordered primitive-prefix edges is **158**.

## Complete proof by finite dynamic programming
Write P(w) for the exact set of nonempty ordered primitive prefixes of a word. For a quintet S, let F be the union of P(w) for the 19 fixed paths and let R_s(w)=P(w)\F for a legal replacement in slot s. The exact edge cost is |F|+|union_{s in S}R_s(w_s)|. The original 158-edge witness is feasible for each S, giving upper bound 158. Set c=158-|F|. To find any strict improvement, discard only single-slot residues of size >= c and then form all distinct residual unions, pruning unions of size >= c at every stage. A discarded union cannot later regain an improvement because union cardinality is monotone. Duplicate residues and duplicate union states are exactly interchangeable for all later union operations. An empty final state family certifies absence of 157-or-fewer-edge choices; otherwise a surviving state gives an explicit improvement.

FCK had fully executed and audited indices [0,240); its immutable source commit is `6c37431f7c81bad40a32f17bff061d1670f13218`. This run executed the published exact bitset algorithm for every index in [240,1920) (1,680 new cases) on the exact frozen model. Every group has minimum 158; the maximum intermediate bitset DP state count across all 1,920 groups is 1,020. Complete unpruned Cartesian candidate count across all groups is 20,081,488,896,000 (a parameter-space product, not number of actual DP operations).

## Independent antichain verification
A second actually executed program `CROSSCHECK_EC49FCL_ALL.py` represents each primitive prefix as an actual literal signed symbol string, stores residuals as `frozenset` and independently verifies all 1,920 groups. Its pruning additionally retains inclusion-minimal states: if A subseteq B, then A union T subseteq B union T for every future set T, so the larger B is dominated for minimum union size and for strict-bound feasibility. By induction on remaining slots, inclusion-minimal pruning preserves the existence and value of every strict improvement. All 1,920 independent results agree with the bitset optimum and the fixed-edge counts.

## Native six-axis typing / faithful bridge
The frozen program uses the signed alphabet {+1,-1,+2,-2,+3,-3}. For the declared static prefix-cardinality observer, an explicit injective native-X6 word embedding maps each signed j to the corresponding signed primitive E_j direction of Z^6 for j in {1,2,3}, keeping E4,E5,E6 components zero in the selected chart. It preserves all ordered word-prefix equalities and cardinalities. Thus the theorem is exact for this specified restricted path family inside native X6; research on additional E4–E6 primitive steps, other legal cache schedules and full 93-edge target remains available.

## Reproduction and evidence
`frozen_model.py` and `VERIFY_EC49FCK.py` in this directory reuse the verified immutable Git blobs from FCK (no alteration of the scientific program). Recompute [240,1920) using `python VERIFY_EC49FCK.py --start 240 --stop 1920 --output REPORT.json`; FCK supplies [0,240) in the immutable parent source. Independently run `python CROSSCHECK_EC49FCL_ALL.py`. `EC49FCL_1920_COMPACT.json.gz.b64` is canonical gzip (mtime=0) of JSON with 1,920 index-ordered fixed-edge counts and the exact minimum 158 for every group, plus the source pin and group-order definition. Full per-group stage counts and Cartesian products can be regenerated using the published verifier, and their recorded checksums are in the summary. Decode by base64 then gzip; `EC49FCL_SUMMARY.json` includes hashes of the complete locally executed reports and the compact certificate.

All published results are author-side evidence; no Source CLAIM, official Result, or independent Driver review is asserted.

## Next discriminating research
Study three early paths with two other late signatures (H7+H7, H8+H9, H7+H9, etc.) and then six-path coordinated substitutions. Separately test whether admissible X6 uses of E4–E6 or altered full cache keys permit <=157 edges, with the frozen observer and input distinctions carried explicitly.
