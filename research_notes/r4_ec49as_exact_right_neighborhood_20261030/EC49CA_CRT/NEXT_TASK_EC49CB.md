# EC49CB — Block/one-pass modular constant-term BRC

**Parent:** EC49CA, PR #1730, author-side continuation only; NOT a Source-admitted Task, CLAIM, Result or independent review.

**Frozen mathematical model:** twelve ordered signed native-X6 steps, endpoint zero, sign-preserving H={id,(1 2)}, positive weights (2,3,3,2,1,1), negative weights all one, three-state joint DFA for adjacent (+E1,+E2) and (+E2,+E1). Use native kernel Git Blob 300a96e3dc24bf6fff73743037a0347a8bc83176, EC49CA proof/checked code/JSON and predecessor EC49BZ packed transfer. Do not change P000, the six primitive dimensions, source state, group action or observer scope.

**Open question:** Can modular CRT constant-term extraction avoid a full n-layer displacement DP for *each* reconstruction prime while preserving exact source information and an O(n^6)-like peak per-pass residue payload? A possible first trial is blocking CRT moduli into a moderate machine/big-integer product, then determining the real size-vs-pass crossover.

**Required result:** an explicit product-capacity and spatial no-alias proof; bit/time/memory bounds including growing prime sizes/count; an executed n=4/6 atom reproduction, n=8 comparison, and a larger-n benchmark against single-pass exact-integer DP and the preceding CRT and packed methods. If a block method has no resource advantage, produce a certified negative benchmark/scope result and choose the next representation. Fixed-horizon pruning must not be promoted to arbitrary future-append sufficiency.

**Status:** no formal owner/admission inferred; independent Driver/Source review pending. Author-side mathematical exploration can continue without adopting another session identity.
