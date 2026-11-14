# EC49FHC — Exact B=20 five-path exclusion (2026-11-10)

Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original nine-state BRC observer, 24 H2–H9 labeled demands and ordered signed six-axis native microstep prefix cost. Prior 7-full-cache-key witnesses A and B each cost 94.

## Finite theorem
Take exactly five labels Q from either EC49FGJ witness, keeping the remaining 19 original paths fixed. Suppose these fixed paths still use all seven original complete raw cache keys, and their cost-93 replacement prefix budget is B(Q)=20. Under the full frozen observer, terminal native-X6 endpoint, and maximum seven complete keys, no five legal replacement paths yield a total cost <=93. There are precisely 116 such Q for each witness. In each of the resulting 232 fixed-background problems the exact minimum cost is 94, achieved by the original witness.

## Proof by complete finite enumeration
Write E for the native prefix set of the 24 original paths (|E|=94). For each e in E, S(e) is its support set of labeled paths. For Q, fixed prefixes F(Q)={e in E: S(e) is not a subset of Q}, and B(Q)=93-|F(Q)|=#{e in E:S(e) subseteq Q}-1. A replacement word w creates D_Q(w)=P(w) minus F(Q). A cost-93 completion exists exactly if all five legal selected words satisfy |union D_Q(w_i)|<=B(Q). All raw keys of the fixed paths already number seven, so replacement words must use one of those same keys.

The frozen nine-state model completely enumerates 178850 admissible words, of which 9838 use the witness's seven keys. The executable exact checker tests every 5-of-24 label subset Q and every admissible candidate group in this precise class. Every exact native prefix is one independently indexed arbitrary-precision integer bit; unions use bitwise OR and costs use bit_count. Five-stage set-union dynamic programming retains subset-minimal feasible masks; deleting Y when X subseteq Y is sound because X union Z subseteq Y union Z for every later Z. Exact pairwise checking is an additional valid necessary filter.

Both witness runs passed all 116 B=20 positions, with 0 cost-93 completions. An independent alternate atom-index/antichain implementation verified 12 deterministic positions per witness, 24/24 consistent. The reproducible checker writes full per-Q EXACT_REPORT_EC49FHC.json. Dependencies are the prior EC49FGW_RADIUS5_EXACT_SCREENS_20261110 and EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110 sibling modules on PR #1730, reusing the already published EC49FGJ witness inputs.

## Continuation
For each witness the remaining no-key-release five-path positions are 48 (B in {21,22,23,25}); another 4898 positions release an original cache key and require joint reassignment. The unrestricted seven-key C_min(7)<=94 problem remains open. Classification: exact finite author-side computational proof; independent Driver mathematical admission pending.