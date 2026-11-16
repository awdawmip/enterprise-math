# PREFIX-849 — A sharp four-heartbeat memory threshold for autonomous binary-source BRC recovery

**Date:** 2026-11-17.  
**Status:** AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).  
**Dependencies:** PREFIX-847 (local update lower bound); PREFIX-848 (exact streaming pair-trajectory/overlap-graph criterion); PREFIX-845/846 (constant-source modular observation and time-window distinctions).  
**Domain:** explicitly defined named positive-integer Q-only BRC scalar observer. These heartbeat transitions are not asserted to be an admitted native X6 Cell/Link/Port event.

## 1. Exact question

There are five named sources with positive integer weights 1 or 2. Pack the named digits `x_i=w_i-1` as

```text
X = {0,1}^5,   U(x)= x_0+2 x_1+4 x_2+8 x_3+16 x_4 ∈ {0,...,31}.
```

At each heartbeat, the source state either stays unchanged or updates *at most one named coordinate*, allowing any binary digit flip. Thus the transition `x -> y` means Hamming distance at most one. The change is hidden from the decoder.

Let `a=2, b=1` (so `C=ab=2`), `c_t = a^floor(t/2) b^floor((t-1)/2)=2^floor(t/2)`, and `S_0` be a fixed publicly known integer. A predetermined state-independent modulus schedule transmits one scalar at time `t`:

```text
Y_t = c_t (S_0 + U(x_t)) mod m_t,   1 <= m_t <= 2^B.
```

The receiver knows the time, modulus schedule and `S_0`, but stores only the last `w` transmitted values. For **every** permitted infinite source trajectory it must recover the last state `x_t` at every `t>=w`. Define `B_dyn(5,2,w,2)` as the least maximum port bit width `B` satisfying this requirement. Prior history cannot be supplied as a separate exact baseline.

## 2. Main theorem — sharp onset at four heartbeats

For every integer window length `w>=1`,

```text
                  { 6,  w = 1,2,3;
B_dyn(5,2,w,2) =  {
                  { 5,  w >= 4.
```

Thus a four-heartbeat rolling observer reduces the required per-heartbeat width from six to five bits, while retaining exact recovery of the current **named** source state under arbitrary admissible changes. A concrete optimal periodic modulus schedule is

```text
m_t = 25,19,29,11,25,19,29,11,... .
```

The result is an all-time theorem for this finite source alphabet and update relation; finite enumeration is used as a complete certificate for finite constituent graphs.

## 3. Pair-trajectory exactness lemma

For any positive integer effective moduli word `z=(q_1,...,q_w)`, define the ordered-pair relation

```text
R_1(q_1) = {(x,y)∈X² : U(x)=U(y) (mod q_1)};
R_{j+1} = {(x',y') : ∃(x,y)∈R_j,
            x -> x', y -> y',
            U(x')=U(y') (mod q_{j+1}) }.
```

Let `Δ={(x,x):x∈X}`. The window determines its final source state for **all trajectories** exactly when `R_w(z)⊆Δ`.

*Proof.* The initial relation is precisely the set of two first-heartbeat states producing the same reading. The recurrence extends both arbitrary legal trajectories by one step and keeps only equal new readings. Induction identifies `R_j` with *all* pairs of length-`j` legal trajectories sharing the entire report prefix, projected to their endpoint states. Ambiguous endpoint recovery is equivalent to a non-diagonal element of `R_w`. No path, named coordinate or update distinction has been discarded in constructing this relation. QED.

Because all moduli in the constructive schedule are odd, `gcd(m_t,c_t)=1` at every time. The public multiplicative gain and offset may therefore be inverted, and these raw observations have exactly the above equality fibers with `q_j=m_j`.

For any bounded schedule with `B<=5`, after a sufficiently late time its effective modulus is `q_t=m_t/gcd(m_t,c_t)`: the odd part of `m_t`. This follows from `c_t=2^floor(t/2)` and the finite upper bound on `m_t`.

## 4. A ten-pair perpetual ambiguity trap proves B>=5 for every finite w

Consider the following ten pairs of **distinct** packed states, indexed 1–10:

| Index | Pair | Index | Pair |
|---:|---|---:|---|
| 1 | (15,22) | 6 | (16,31) |
| 2 | (15,24) | 7 | (18,31) |
| 3 | (15,26) | 8 | (20,31) |
| 4 | (15,28) | 9 | (22,31) |
| 5 | (15,30) | 10 | (24,31) |

For every current pair in this set and each odd effective modulus `q∈{1,3,5,7,9,11,13,15}`, there exists a successor pair in the same set such that both named-source trajectories make at most one bit flip and the two new states are congruent modulo `q`.

An explicit successor certificate, with destination indices indexed as above, is:

| From / next q | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 5 | 5 | 1 | 9 | 8 | 7 | 5 |
| 2 | 2 | 2 | 6 | 10 | 2 | 3 | 4 | 6 |
| 3 | 2 | 2 | 5 | 10 | 2 | 3 | 7 | 5 |
| 4 | 2 | 2 | 5 | 10 | 2 | 8 | 4 | 5 |
| 5 | 1 | 5 | 5 | 1 | 9 | 3 | 4 | 5 |
| 6 | 2 | 2 | 6 | 10 | 2 | 8 | 7 | 6 |
| 7 | 1 | 6 | 6 | 1 | 9 | 3 | 7 | 6 |
| 8 | 1 | 6 | 6 | 1 | 9 | 8 | 4 | 6 |
| 9 | 1 | 5 | 5 | 1 | 9 | 8 | 7 | 5 |
| 10 | 2 | 2 | 6 | 10 | 2 | 3 | 4 | 6 |

Every cell can be checked using two integer bit-count comparisons `popcount(u xor u')<=1`, `popcount(v xor v')<=1` (allowing swapped pair orientation), and a congruence check `q | (u'-v')`. All 80 transitions are checked by the attached exact verifier. At the first chosen late heartbeat take any trap pair congruent for that modulus, and inductively select the listed successor. This yields two indefinitely legal source histories with the same reports at **every** heartbeat yet different current source states.

For any `B<=4`, every sufficiently late effective modulus is one of the eight odd integers in this table. Thus a universally decodable observer with any finite window must satisfy `B>=5`. This statement is stronger than any one finite-window enumeration.

## 5. No permanent five-bit observer exists for w<=3

At width `B=5`, all sufficiently late effective moduli belong to

```text
A = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31}.
```

For a window of length `w`, call a word of these moduli *good* when its pair relation is contained in the diagonal. Following the PREFIX-848 finite directed overlap graph criterion, a predetermined infinite schedule works if and only if the graph of good length-`w` words has a directed cycle. The vertices are overlapping `(w-1)`-words and the edges are good `w`-words.

The exact fully enumerated results are:

| Window | Good words / graph vertices | Graph result | Consequence |
|---:|---:|---|---|
| 1 | none (every effective q is below 32) | no edge | five bits insufficient |
| 2 | exactly 1 good word, (17,31) / 2 vertices | acyclic | five bits insufficient |
| 3 | 37 good words / 42 vertices | all 42 vertices topologically eliminated | five bits insufficient |

The full list of 37 good triples, the single good pair, and the precise graph statistics are in the results JSON. The accompanying independent exact JavaScript verifier reconstructs the **entire** ordered-state-pair relation for all `16^2=256` two-words and all `16^3=4096` three-words, and validates the no-cycle claim with a separate topological elimination. This is complete finite enumeration, not a sampling inference.

A constant modulus `m=33` (odd, at most 64, coprime to `c_t`) reads the packed state injectively at each heartbeat. Thus six bits are sufficient for `w=1,2,3`, completing these three sharp cases.

## 6. Constructive four-heartbeat five-bit observer

Set `m_t` to the period-four cycle `(25,19,29,11)`. Every modulus is odd and at most 32. Direct exact pair-trajectory recurrence for every cyclic four-word yields:

| Four-heartbeat word | Non-diagonal pairs after 1st, 2nd, 3rd, 4th reports |
|---|---|
| (25,19,29,11) | 14, 18, 0, 0 |
| (19,29,11,25) | 26, 6, 12, 0 |
| (29,11,25,19) | 6, 12, 0, 0 |
| (11,25,19,29) | 62, 14, 18, 0 |

Consequently every sliding four-word is good, including every overlap boundary and every source trajectory. This is an unbounded-time construction. Retaining more than four observations cannot hurt decoding, so five bits suffice for every `w>=4`. Section 4 provides the matching lower bound.

## 7. Verification and provenance

Published artifacts:
- `research_notes/portable_direct/PREFIX849_R6_DYNAMIC_STREAM_MEMORY_THRESHOLD_CHECK.js`: self-contained exact integer (BigInt) pair relation, graph, periodic-window and 10-state ambiguity-trap checker; no external dependency.
- `research_notes/portable_direct/PREFIX849_R6_DYNAMIC_STREAM_MEMORY_THRESHOLD_RESULTS.json`: all 37 good triples, graph topological statistics, four period checks and all 80 trap successor indices.
- The code was executed in an isolated JavaScript V8 calculation and returned `ALL_EXACT_ASSERTIONS_PASSED`. An independent Python integer-set recurrence confirmed the four periodic-window non-diagonal counts and 37 good triples.

Reproduction: `node research_notes/portable_direct/PREFIX849_R6_DYNAMIC_STREAM_MEMORY_THRESHOLD_CHECK.js > /tmp/PREFIX849_R6_RESULTS.json`. The mathematical enumeration uses integer residues and exact bit masks, without floating-point or heuristic search. The proof of the infinite statements consists of the finite trap induction, finite DAG criterion and periodic four-window induction; the finite checks certify their hypotheses.

The result refines PREFIX-848's length-2/3 table and answers its open question by exhibiting a genuine resource saving beginning at length four. Its Q-only source packing preserves all five named-coordinate labels. No native X6 force, spatial coordinate, triadic event or observer permission is inferred from this scalar coding.

## 8. Open continuation questions

1. For general `p` and `W=2`, characterize the first memory length at which the autonomous optimal width strictly improves upon one-heartbeat width.
2. Replace the finite overlap-graph exhaustive search by compressed exact pair-bisimulation or number-theoretic certificates and derive asymptotic bounds as `p` grows.
3. Test whether a separately authorized X6-native Cell/Link/Port source event realizes the declared coordinate-update relation, and preserve its event provenance/causal order during any port mapping.

**Role/publication distinction:** this is an independent author theorem in an auxiliary BRC observer. Publication and Activity association do not acquire a shared X6 CLAIM or constitute independent mathematical review.
