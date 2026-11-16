# PREFIX-850 — No finite-memory port-width discount for one through four binary named sources

Date: 2026-11-17 (Asia/Shanghai).  
Status: AUTHOR_PROVED / EXACT_FINITE_AUTOMATON_CERTIFICATE / INDEPENDENT_LOCAL_PYTHON_RECHECK / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged.  
Direct predecessor: PREFIX-849, `2026-11-17_r6_prefix849_four_heartbeat_dynamic_source_memory_threshold.md`.  
Scientific scope: the explicitly specified Q-only BRC *named binary source observer*, not an assertion of native X6 Cell/Link/Port event permission.

## 1. Question and model

For `p` named sources set `X_p={0,1}^p`, and encode `U(x)=sum_{i=0}^{p-1}2^i x_i`, with `0 <= U < 2^p`. At every integer heartbeat the source state may stay fixed or flip at most one named bit; the decoder is not given the flip. At time `t>=1`, transmit one scalar

```
Y_t(x_t) = 2^floor(t/2) (S_0 + U(x_t)) (mod m_t),
1 <= m_t <= 2^B,
```

where the integer `S_0`, moduli schedule and time are known to the receiver, and the schedule is predetermined and state-independent. A rolling observer must recover the exact named state `x_t` from its most recent `w` readings for every allowed infinite source trajectory and each `t>=w`. Let `B_dyn(p,2,w,2)` denote the minimal maximal single-port bit width.

The predecessor PREFIX-849 settled the sharp `p=5` threshold: six bits for `w=1,2,3` and five for `w>=4`. This note settles every finite window length for `p=1,2,3,4`.

## 2. Exact theorem

**Theorem.** For every `p in {1,2,3,4}` and every finite integer `w>=1`,

```
B_dyn(p,2,w,2) = p+1.
```

Thus an arbitrarily long *finite* rolling observation window cannot save a port bit when there are at most four named binary sources. Five sources form the first instance in this `p<=5` family where the previous four-heartbeat construction actually saves one bit.

## 3. Proof: effective odd moduli and exhaustive finite closure

**Gain reduction.** Let `c_t=2^floor(t/2)`. For any modulus `m`, two states yield the same reading precisely when

```
U(x) = U(y) (mod q_t),  q_t = m / gcd(m,c_t).
```

If `m_t<=2^B`, then for all `t>=2B`, `2^B|c_t`, and `q_t` equals the odd part of `m_t`. Consequently `q_t` belongs to the fixed finite alphabet `Q_B={1,3,5,...,2^B-1}`. In any sufficiently late window all readings have effective moduli from `Q_B`.

**Pair-trajectory exactness.** Put `n=2^p`, `D={(x,x):x in X_p}`. For a nonempty word `q_1,...,q_w` of effective moduli, define

```
R_1(q_1) = {(x,y) : U(x)=U(y) mod q_1},

F_q(R) = {(u,v) : exists (x,y) in R with
                   Hamming(x,u)<=1, Hamming(y,v)<=1,
                   U(u)=U(v) mod q},

R_w = F_{q_w}(...F_{q_2}(R_1(q_1))...).
```

Induction on `w` identifies `R_w` with *all* endpoint pairs of two admissible hidden-update histories with identical reports throughout that window. Every relation includes `D` (two identical stationary trajectories). The final state is uniquely recoverable exactly when `R_w=D`. It is ambiguous if `R_w\D` is nonempty.

**Finite, all-length certificate.** Fix `B=p`. Starting from *every* `R_1(q)`, `q in Q_p`, exhaustively close the reachable relations under *every* transition `F_q`. Relations are exact bitsets indexed by the `n^2` ordered pairs. The attached self-contained JavaScript enumerates these sets using only integer/BigInt arithmetic, and independently reproduces each transition in a separate Python implementation. Its complete reachable-state table and all outgoing edges are recorded in the accompanying JSON. Results:

| `p` | Odd effective moduli | Reachable relations in the complete closure | New relations by first-word depth | Resetting `D` reachable? |
|---:|---:|---:|---|---|
| 1 | 1 | 1 | 1 | No |
| 2 | 1,3 | 2 | 2 | No |
| 3 | 1,3,5,7 | 4 | 4 | No |
| 4 | 1,3,5,7,9,11,13,15 | 53 | 8,13,19,13 | No |

There are precisely `1+4+16+424=445` verified, closed, directed transitions among these four cases. Every stored relation contains the diagonal and at least one off-diagonal pair. Every alphabet symbol has a stored successor within the enumerated set. By induction on word length, *no* finite word in `Q_p` has a relation equal to `D`; this proves the lower bound `B_dyn>=p+1` for every finite `w`.

**Upper bound.** Choose the constant modulus `m=2^p+1`. It is odd, so `c_t` is invertible modulo `m` at every heartbeat, and it exceeds all possible source codes `U(x) in [0,2^p-1]`. Removing the known offset and gain recovers `U(x_t)` at each single heartbeat, and `m=2^p+1<=2^{p+1}`. Thus `B_dyn<=p+1`. Combined with the lower bound, the equality is proved.

The closure is a finite witness for a universal theorem over *all finite window lengths*, not an extrapolation from windows of length four or six.

## 4. Reproduction, validation and contrast with PREFIX-849

- Exact checker: `research_notes/portable_direct/PREFIX850_R6_NORESET_OBSERVER_AUTOMATON_CHECK.js`. Run `node <path>` to print the complete JSON certificate.
- Complete relation masks, initial-state IDs, successor IDs, depth inventories, all checks and the five-source bridge: `research_notes/portable_direct/PREFIX850_R6_NORESET_OBSERVER_AUTOMATON_RESULTS.json`. Relation bit positions are `n*x+y`.
- An independently written local Python integer verifier checks every transition in two formulations (precomputed successor masks and explicit nested legal-transition loops). It independently reproduces closure sizes `1,2,4,53`, the four-source depth histogram, and the four shifted `p=5` windows. The publication's executable JavaScript uses a distinct integer/BigInt implementation. No floats, randomized tests, probabilistic inference or external libraries are needed.

For continuity, the four cyclic windows of the PREFIX-849 five-source witness `(25,19,29,11)` were rechecked. Their ordered off-diagonal counts by time are `(14,18,0,0)`, `(26,6,12,0)`, `(6,12,0,0)`, and `(62,14,18,0)`. The four-source obstruction and five-source success exhibit a concrete finite-state transition in the value of accumulating heartbeat memory.

## 5. Interpretation and subsequent scientific problems

The observation model uses real named-coordinate flips, the exact Q-only positive integer BRC scalar carrier and a declared observer. The result concerns the informational recovery capacity of this interface; an X6-native event realization requires its own typed, provenance-preserving event map.

The new 53-state transition certificate is a reusable compressed exact proof object. Its reachable relations are stronger than a bounded-window failed search, and weaker than a single universal ten-pair ambiguity trap: the *set of possible endpoint pairs* stays nonempty for every schedule, even though a fixed pair is not required to survive every modulus.

Natural next questions:

1. Determine the sharp earliest memory-saving window for `p=6`, and test whether there is an arithmetic/combinatorial family of short all-time schedules as `p` increases.
2. Derive a smaller symbolic invariant proving the `p=4` no-reset fact without storing 53 relation bitsets; compare invariant-quotient representations under exact transitions.
3. Add constraints from independently permitted X6 Cell/Link/Port events to the named-update relation, and check which proof certificates remain valid under those typed event restrictions.

Author result: exact proof conditional only on the declared model plus complete finite closed-transition tables; independent scientific review and project admission remain separate.
