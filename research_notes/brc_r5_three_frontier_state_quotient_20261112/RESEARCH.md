# R5 — A 954-state exact activation quotient for 1,065 BRC path certificates

**Research date:** 2026-11-12, author-side independent continuation; no native CLAIM, Result, review or Foundation promotion is asserted by this note.

## Frozen dependencies and precise scope

This is an additional theorem in the existing **external 28-coordinate P/Q–BRC Blackwell auxiliary model**, not a change to P000 or a native X6 identification. Scientific fixtures and the 1,065 selected lawful words are inherited without repinning from:

- The 15-atom exact fixture: `enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Exact dual-zero word selection/right-persistence: `ad7013218d0474e1e942906e3beadec1eccb9213` (Draft PR #2152).
- The 953 distinct monotone activation thresholds: `d37154e58cf971457da190d80a95d4ffdd72ee0c` (Draft PR #2155).

Let `W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)` and `K=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)`. For each of the 32768 labeled masks, form `w(S)=sum(W_i)` and `k(S)=sum(K_i)`. Define `N={-w(S):w(S)<=-3}` and the **selected eligible pair set**

`C={(q,n): q in {3,12,15}, n in N, exists nonempty mask S with w(S)=-n and k(S)=-36q}`.

The earlier 28-coordinate proof gives exactly one chosen legal labeled word for each pair of C and establishes that *that same word*, evaluated at its own moving time `u_q(r)=x(1-23r)/q`, is legal iff `r>=tau_(q,n)` for `L<=r<U`, where `tau_(q,n)=(1-36q/n)/23`, `L=-427508577031693280/628800490619`, `U=1/23`, `x=155682221/25142124560000000`. This is a scientific dependency, not rederived from the two-port census here.

## Theorem: only three integer frontiers are needed

For each `q`, let `N_q={n:(q,n) in C}` sorted increasingly and `c_q(r)=#{n in N_q: n<=36q/(1-23r)}`. For **every** real `r in [L,U)` and `(q,n) in C`,

`the word (q,n) is active iff n <= 36q/(1-23r)`.

Consequently, in each of the three q families, active certificates are exactly the **initial segment of N_q of length c_q(r)**. The entire active-word indicator vector (1,065 entries) is recoverable from just `(c_3,c_12,c_15)` and the fixed sorted pair-key dictionary. The word labels/provenance remain in that static dictionary; we do not discard them or claim that the 28-dimensional transport state itself has only three degrees of freedom.

**Proof.** For r<U, 1-23r>0; since n>0,
`r >= (1-36q/n)/23 <=> n(1-23r) <= 36q`.
For fixed q, the right-hand threshold is independent of n, so every eligible n up to the bound is active, and every larger n inactive. The inherited right-persistence lemma converts this exact threshold test into legality of the chosen word at its own scale. QED.

The independent 15-weight census has `|N_3|=538, |N_12|=298, |N_15|=229`. An explicitly packed independent-frontier counter representation uses respectively **10, 9 and 8 bits**, totaling **27 logical dynamic-state bits** (four physical bytes when packed). This replaces 1,065 *dynamic* activity flags for this declared query, **not** the static dictionary, event thresholds, LOUDS payload or index. No amortized runtime measurement is asserted.

## Theorem: exactly 954 reachable activity states; 10 bits is tight

The previously established event set for C contains exactly 953 distinct interior thresholds. Every threshold activates at least one new eligible pair, and none ever deactivate as r increases. The initial state below the first threshold and the states immediately at each of 953 thresholds are therefore **954 pairwise different sets**, covering every `r in [L,U)`. There are no other active sets because indicators are constant on the open intervals between thresholds.

Thus a lossless, parameter-independent identifier of these **954 patterns**, given a fixed event table, requires at least `ceil(log2(954))=10` bits and the *activation-event ordinal* `j=#{t in T:t<=r}` attains 10 bits. This is an exact finite-state lower/upper bound for the chosen active-set observer; the static event table and the cost of converting a given rational r to ordinal j are additional resources.

For r=a/b in reduced form with b>0 and r<U, the activity test can be executed by integer comparison `n(b-23a)<=36qb`, so no floating-point boundary decision is needed. An exact right-biased binary search over the 953 sorted rational walls maps r to j in O(log 953) rational comparisons; decoding j to all flags is linear output work unless additional static indexing is maintained.

## New exact finite census

Re-enumeration of all 32768 masks yields 1,144 fixed n values, 1,065 pair keys and 2,935 candidate masks, distributed by q as **538, 298, 229** for q=3,12,15. The 953 distinct activation walls consist of **869 single**, **56 double** and **28 triple** events; first wall `-179/23`, last wall `8/211`. At **r=0**, the active-frontier tuple is **(100,276,229)**, giving exactly **605 active selected words** (not 1,649 candidate masks). The 953 threshold inclusions and the intervening open intervals are checked with `fractions.Fraction` and direct reconstructed membership sets.

The companion standalone script `VERIFY_THREE_FRONTIERS.py` was run with CPython 3; its output is in `EXACT_OUTPUT.txt`. It recomputes two-port pair eligibility and threshold arithmetic independently; the parent 28-coordinate word-legality theorem remains separately pinned.

## Reusable methods and next unresolved unit

- **Three-frontier query:** with the static three ordered `N_q` arrays, derive `c_q(r)` by integer or exact rational bisection. This offers fast membership/pattern queries under the selected moving-ray observer with no per-word activation flags.
- **Tight event-ordinal quotient:** the mutable pattern can instead be represented by a single 10-bit event ordinal plus static event-index decoding. Choose between 27-bit counters, 10-bit event rank, and the previous prefix-counter trie according to the required query/update interface and total storage.
- **Next:** derive/query prefix aggregate `C_v(r)` efficiently from the event ordinal and the retained trie without materializing all 2,880 mutable prefix counters. Compare a wavelet/range-count structure and Fenwick over lexicographically ordered terminals against the prior 7,444-increment algorithm; count static indices, decode RAM, event search, and actual time separately. Benchmark on the 1,065 *original selected words* rather than on abstract masks.

**BRC reuse decision:** `EXTEND_EXISTING_TOOL` — preserves the existing exact labeled-word and provenance carrier, changes only the observer-specific activity-state representation. Exact 28-coordinate claims are inherited at their stated source scope, and no formal shared task ownership has been asserted.
