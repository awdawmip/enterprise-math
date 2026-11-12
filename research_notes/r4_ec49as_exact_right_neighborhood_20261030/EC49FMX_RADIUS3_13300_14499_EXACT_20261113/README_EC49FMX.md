# EC49FMX — BRC seven-key radius-three exact scan, indices 13300–14499

Date: 2026-11-13. Scientific status: author-side finite computational result; not an independent Driver-reviewed theorem or formal task Result. Frozen scientific input: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Continuing EC49FMW [PR #2207](https://github.com/awdawmip/enterprise-math/pull/2207) at immutable research commit \`e3256c4a300c66e3cd3b63d0d19f79acbb7e2b98\`.

## Exact object

The frozen nine-state BRC generator yields 178,850 legal operation words, 94 complete raw cache keys, 24 required observation labels, and 38,169 deterministic radius-three seven-key configurations. For each seven-key configuration \`K_i\`, define \`C(K_i)\` as the minimum count of *distinct nonempty ordered signed-X6 native microstep prefixes* across original legal words with complete raw keys in \`K_i\`, covering all 24 labels. Prefixes retain order/sign, not only the net displacement.

## Finite-family result

All 1,200 consecutive cases 13300 through 14499 were fully emitted by the unchanged C++17 integer trie/subset dynamic program. The original command targeted a longer range, but execution was interrupted after progress 14500; this report counts no case beyond 14499.

\`min_{13300 <= i <= 14499} C(K_i) = 110\`, attained **exactly at 14472 and 14473**.

\`max = 205\`, attained at 13372, 13408, 13468, 13472, 13474 and 13478.

The *complete lossless* cost vector (1,200 bytes after decompression), both native 24-word witnesses, original result and input hashes are in \`EXACT_DATA_EC49FMX.json\`; see \`VERIFY_EC49FMX.py\` for a no-network finite-result and witness-prefix check.

* 14472 keys: \`[0,4,5,6,15,16,22]\`, witness root costs: \`46+48+16=110\` (first signed native microstep bytes 05/06/07).
* 14473 keys: \`[0,4,5,6,15,22,26]\`, witness root costs: \`46+48+16=110\`. The witnesses differ in six selected words but have the same three root costs, establishing only this *pairwise* equality, not a general swap theorem.

The independently implemented Python BRC native-prefix trie and label-assignment solver returned \`13300:132\`, \`14472:110\`, \`14473:110\`, \`14499:130\`, agreeing with C++ at all four checks. It was not run over all 1,200 cases.

## Exactness proof for the stated finite problem

Partition legal words by their first signed native microstep. Each partition has a separate ordered-prefix trie, and prefixes in different first-step roots are disjoint. In one trie, DP states enumerate subsets of observation labels covered by selected terminal words. Child subtrees combine with exact set-union convolution and additive costs; a used nonempty node is charged exactly once. Induction on trie height proves the DP minimum equals the true minimum prefix union for every demanded subset at that root. Exact enumeration of legal assignments of each of the 24 labels to a supplying root combines the independent root minima without relaxation. Hence the integer solver computes the optimum for each fixed \`K_i\`. Explicit 24-word witnesses give checkable upper bounds 110 at both minima; matching solver minima are the corresponding exact lower bounds. The 1,200-element lossless vector establishes the enumerated interval minimum.

The prior continuous interval 0–13299 had minimum 102, so the cumulative 0–14499 minimum remains 102. The unrestricted seven-key mother problem retains the independent earlier feasible 84-prefix upper bound \`C_min(7) <= 84\`, which this restricted family does not improve.

## Provenance and reproduction

Original unmodified solver: \`scan_cached_radius3.cpp\`, SHA-256 \`6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac\`. Original frozen case enumeration: \`cases.json\`, SHA-256 \`d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33\`; input file \`master_and_radius3_cases.txt\`, SHA-256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; generator \`EC49FGW_RADIUS5_SCREEN.py\`, SHA-256 \`0fbfa02b8b9b526b44f105c93a187c809e3279954cb074149af87ac271d2b9d3\`. Full non-sensitive originals are present in the EC49FMX local evidence archive, reused byte-identically from the previous full evidence package. Original 1,200-row solver output SHA-256: \`d219205bce5dc8379e888568b4404c0f61c7f7bd0d01ce008bf44f5cfd70c306\`. Complete uint8 vector SHA-256: \`5f24f31cc33d176cb2436f040c1de5f16ae59cce76a1b6efc31d33580e4f91c1\`.

With the original inputs, run:
\`\`\`bash
g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan
./scan 13300 14500 < master_and_radius3_cases.txt > replay.txt
sha256sum replay.txt
python VERIFY_RADIUS3_SELECTED.py cases.json 13300 14472 14473 14499
python VERIFY_EC49FMX.py
\`\`\`

The compact GitHub certificate gives full finite costs and complete 24-word witness choices; the local evidence archive additionally contains the original 1,200 rows, original generator, C++ and independent Python code, detailed path lists, logs and SHA-256 manifest. No classical pi or trigonometric surrogate was used.

## Control and continuation

Native exact task query \`emr4-20261113-0527-rs-ec49as-check-v1\` returned \`FAILED / CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION\`. Therefore no task CLAIM, official Result or mathematical admission is asserted. Native own-session registration request \`emr4-20261113-0527-session-r4-new-v1\` must be assessed by its final receipt, not guessed from the request. Next contiguous index: **14500**; remaining cases: **23,669**. Further objectives: cross-configuration reusable exact lower-bound certificates and an unrestricted legal construction with fewer than 84 prefixes.
