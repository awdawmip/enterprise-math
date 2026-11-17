# PREFIX-854 — Variable-modulus named BRC: a two-heartbeat terminal recovery and an all-horizon four-bit impossibility certificate

Date: 2026-11-17. Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Scientific frozen pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Provenance: independent auxiliary named positive-integer Q-observer, Source Activity \`RA-14044F2E842D112941E256BF\`, Researcher-ID \`EM-DIRECT-B518B3\`. This is not a shared X6 CLAIM or an admitted Cell/Link/Port law.
Dependencies: PREFIX-846 (stationary streaming), PREFIX-848/849 (dynamic finite window), PREFIX-853 (fixed-modulus lifetime).

## 1. Question, observer and quantifiers

Five **named** binary positive-integer source increments are encoded injectively:

    p=5, x=(x_0,...,x_4) in {0,1}^5,
    U(x)=sum_{i=0}^4 2^i x_i in {0,...,31}.

The receiver initially knows none of these source bits. There are no missed prehistory updates in this problem. Between consecutive observations, the source may flip at most one named bit, including a no-op. Denote the admissible successors of x by

    N(x)={x} union {x XOR 2^i : i=0,1,2,3,4}.

Choose a **predeclared**, possibly variable, odd modulus sequence q_1,q_2,..., each q_j>=3. At integer observer-step t_j the scalar output is

    Y_{t_j}(x_j)=c_{t_j}(S_0+U(x_j)) mod q_j,
    c_{t_j}=2^{floor(t_j/2)}.

Oddness implies gcd(c_{t_j},q_j)=1; with the known baseline and clock, the observer can convert Y to the exact residue U(x_j) mod q_j. The observer knows the schedule and all prior outputs, and may retain them and perform unrestricted exact decoding. This theorem minimizes only the **maximum per-sample raw modulus bitwidth**, including the entire schedule, not total receiver RAM, communication for announcing an otherwise unknown schedule, or the latency.

The requested guarantee at window length w is **terminal-state recovery**: for *every* pair of valid source trajectories having identical observed residues at all w observations, the last states must agree. We distinguish this from perpetual sliding-window recovery that must work from any start time on the same fixed observation schedule.

## 2. Exact pair-state observer and finite closure

For q odd define an equality relation on pairs of source states:

    E_q={(x,y): U(x)≡U(y) (mod q)}.

Here U(x)=x when x is interpreted as its integer bit mask. An ordered pair (x,y) represents two candidate trajectories that are indistinguishable to the receiver. Define a pair relation transform:

    T_q(P)={(u,v): exists (x,y) in P,
       u in N(x), v in N(y), and u≡v (mod q)}.

For any finite fixed schedule q_1,...,q_w, the exact relation of all terminal pairs having identical full observation streams is

    P_1=E_{q_1},
    P_j=T_{q_j}(P_{j-1}) for j=2,...,w.

This identity follows in both directions by the definition of all admissible paired trajectories; no probabilistic or average-case argument enters. Thus terminal recovery is equivalent to

    P_w subseteq Delta={(x,x):0<=x<32}.

All pair states are finite subsets of the 1,024 ordered state pairs. A finite closed family of pair relations that contains every allowed first-step E_q and contains no subset of Delta is an exact proof that **no finite schedule** drawn from the allowed moduli can guarantee terminal recovery.

## 3. Theorem 854-A: exact optimal five-bit port for five sources

For the above p=5, one-flip-or-no-op model with arbitrary unknown initial source state and independently selected predetermined odd moduli at each reading, the smallest possible maximum per-reading raw bitwidth that can guarantee exact terminal-state recovery after some finite number of readings is

    **B*=5 bits.**

Moreover two readings suffice, using the ordered moduli

    **(q_1,q_2)=(17,31).**

**Constructive finite proof.** Compute the pair relation

    P_2=T_31(E_17).

By exhaustively iterating all 32^2 first-state ordered pairs and every pair of 6 permitted successors, P_2 consists precisely of the 32 diagonal pairs. Therefore any two legitimate two-step trajectories producing the same residues modulo 17 then 31 must have the same final named state. The reverse schedule (31,17) leaves a distinct-state pair; the order is genuinely meaningful.

**Exact impossibility of four bits (all finite horizons).** A maximum four-bit odd modulus can be only in

    Q_4={3,5,7,9,11,13,15}.

Start with the seven E_q relations, close them under every T_q with q in Q_4, and index newly discovered distinct relation bitsets in breadth-first order. The exhaustive computation yields **15 distinct reachable relations**. The persisted results JSON supplies for each of the 15 relations:
- its index, one actual offdiagonal endpoint pair (x,y) with x != y;
- the number of offdiagonal endpoint pairs;
- all seven indexed successors for moduli 3,5,7,9,11,13,15.

The checker independently asserts that every transition from every listed relation belongs to this same 15-state set; there is no unexamined edge. Every one of the 15 relations contains a distinct terminal pair. By induction over schedule length, each arbitrary finite schedule over Q_4 ends in one of these 15 relations and therefore fails terminal recovery. This proves that no four-bit (or narrower odd) predetermined variable-modulus schedule succeeds, at any finite horizon.

The five-bit explicit construction together with the closed-family obstruction proves the exact optimum.

## 4. Reproducibility and comparison

Run the standalone Python 3 exact-integer checker:

    python research_notes/portable_direct/PREFIX854_R6_VARIABLE_MODULUS_AUTOMATON_CHECK.py

The checker constructs each relation as a 1,024-bit Python integer bitset, which is simply an exact encoding of a finite set (there are no real-number operations). It also implements a separate set-comprehension trajectory oracle for schedules (17,31) and (31,17). It returns \`ALL_EXACT_ASSERTIONS_PASSED\`, 15 reachable relations in the closed four-bit automaton, zero offdiagonal terminal pairs for (17,31) and 32 diagonal terminal pairs, and a reversible ordering contrast. The complete 15-state directed-transition table and an explicit offdiagonal witness in every relation are preserved in the results JSON.

This construction improves the **terminal recovery latency** over the earlier PREFIX-849 four-heartbeat *sliding-window* 5-bit example. The two guarantees differ: PREFIX-854 has an explicitly designated initial observation and does not establish the universal exactness of every sliding two-observation window on the periodic repetition 17,31. PREFIX-853's no-repair theorem assumed a single fixed modulus; varying the modulus removes its stationary-alias obstruction.

The mathematical objects are typed positive-integer named-source BRC Q readouts with exact provenance. This auxiliary model by itself does not certify actual native X6 Cell/Link/Port events, triadic balance, time duration, or physical calibration.

## 5. Next questions

1. Determine whether any *periodic* five-bit odd-modulus schedule can make every sliding two- or three-observation window terminal-lossless under the same one-flip dynamic rule. Use pair-relation recurrence and cycle detection; distinguish finite initial sync, eventual fixed-delay sync, and universal sliding-window sync.
2. Generalize pair-automaton lower-bound certificates to arbitrary p and h, and derive analytical witnesses that compress the finite relation closure. Account for total receiver history memory, port read widths and any schedule-signaling cost.
3. Investigate a separately typed native Cell/Link/Port event observer and permitted source/target relation before using this auxiliary result as an X6 event theorem.

Code: \`research_notes/portable_direct/PREFIX854_R6_VARIABLE_MODULUS_AUTOMATON_CHECK.py\`.
Full exact certificate: \`research_notes/portable_direct/PREFIX854_R6_VARIABLE_MODULUS_AUTOMATON_RESULTS.json\`.
