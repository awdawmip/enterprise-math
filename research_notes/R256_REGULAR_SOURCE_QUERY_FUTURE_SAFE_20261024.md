# R256 — Exact future-safe source-query memory in positive six-axis BRC

**24 October 2026 | Author-side mathematical evidence | UNREVIEWED | Not a formal Task Result or native heartbeat theorem**

## Frozen source and boundaries

GLOBAL_KNOWLEDGE_V1 was read at canonical main 7b33f8066e9993e7c941959a9d738ed405248eb8. P000 is ACTIVE_LOCKED (blob ba8e4c75cdb3663ab3fde07e4286782344b0ed42): six native spatial axes and a distinct seventh time dimension are assumed, never put under proof or falsification. Enterprise Math Source is pinned at main 77f350a94f60c42f6c3d70befc7b494ba9c603b6; source interfaces are brc_transport.py (blob be1debe367263931bd5e93fd750be3ed54624fe1) and brc_control_port.py (blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8). R255's verified author-side rank/unrank proof at f4e9857a3ec1dade733eb92d78318eacc667c13b is consumed, not repeated.

The following example is a mathematically declared positive-branch BRC control model. Its selector tokens are NOT verified R193 physical edge IDs; the sign-flips/translations are NOT yet proved to be legal P000 native Cell updates or heartbeat rotations; one discrete composition step is NOT a measured physical heartbeat time interval. No native package was imported in this run.

## 1. Exact carrier and source query

Let nonspatial controls Q={0,1,2}; at each control q there are two distinct source-local selector edges a=0 and a=1. Each has positive rational weight 1 and path multiplicity 1. Edge triples (next control, linear sign, first native-axis translation) are:

| q | selector 0 | selector 1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

The six-axis formal affine action is F_(eps,k)(z)=diag(eps,eps,1,1,1,1)z+k e_1. Chronological Source Affine.then law, validated by source reading, is

\[
F_{(\epsilon,k)}\operatorname{then}F_{(\eta,b)}
=F_{(\eta\epsilon,\,\eta k+b)}.
\]

The coarse complete-effect observation after an ordered selector history w of length m is O_m(w)=(terminal q,eps,k). Although that retains the whole *affine effect*, it forgets the original word.

Choose one precise source-history question: does the selector word contain the consecutive substring 00? Its deterministic monitor has R={0,1,2}, initial 0, accepting 2. States mean (0) no 00, last selector not 0; (1) no 00, last selector 0; (2) seen 00 (absorbing). The transition table is:

| r | on 0 | on 1 |
|---|---|---|
| 0 | 1 | 0 |
| 1 | 2 | 0 |
| 2 | 2 | 2 |

This language is only a controlled example, not a claim about the actual R193 query grammar.

## 2. Theorem A: exact positive query-effect transport

Define H_m(q,eps,k,r) as the number of ordered positive paths from q=0 of length m with indicated endpoint, full action and query state. Start H_0(0,+1,0,0)=1 with all other atoms zero. For each original state (q,eps,k,r), positive count c, and one outgoing edge a=(q_a,eta_a,b_a), update by

\[
H_{m+1}(q_a,\eta_a\epsilon,\eta_a k+b_a,\delta(r,a))
\mathrel{+}=H_m(q,\epsilon,k,r).
\tag{1}
\]

**Theorem.** Equation (1) retains the exact positive multiplicity of every joint terminal/effect/query atom for every finite horizon. Its projection over r equals the former terminal-indexed EffectHistogram, and its accepting part H_m(q,eps,k,2) equals the exact number of words in the queried language in that complete-effect fiber. It is serially composable under compatible edge-labelled time ports *while r remains in the state*.

**Proof.** The empty history gives the initial atom. Every nonempty path has exactly one last edge and a unique prefix. The Source chronological affine formula computes its exact action; the deterministic query transition computes its exact query state. Since every edge has positive unit weight, summing distinct histories adds nonnegative integer path multiplicities rather than amplitudes. Conversely every recurrence summand describes a valid path. Induction proves the identity. Erasing r only after the last required future-query observation recovers the existing exact effect histogram by disjoint summation. Erasing r earlier is not generally valid, as Theorem C will prove. The same inductive argument works for any later compatible finite edge packet sequence with the same labelled query monitor. QED.

At length m, |k|≤m; therefore at most 3·2·(2m+1)·3=18(2m+1) joint atoms exist. For this fixed graph and DFA, dynamic evaluation through m costs O(m²) exact integer additions; the final layer uses O(m) counters (or O(m²) stored counters when retaining all layers). These are arithmetic-operation, not bit-time, bounds; counts can have Θ(m) bits.

## 3. Theorem B: finite future-safe quotient certificate

For a fixed finite labelled deterministic control graph and a finite deterministic query monitor, use the synchronous product S=Q×R. A pair of annotated individual histories with equal current terminal q and full affine effect can be collapsed without a repair tag **for every future source-query observation** exactly when their product states have equal accepting output after every common admissible selector suffix u.

Sufficiency: equal q and affine effect imply identical future terminal/effect for the same suffix; monitor right congruence implies equal future accept/reject. Necessity for a *uniform pathwise* quotient: if suffix u distinguishes acceptance, that pair remains identical in terminal/effect after u but has different source-query output, so erasure is unsound. The statement does not assert the strongest possible quotient for a single already-aggregated positive histogram, nor does it imply historical word recovery.

This equivalence is decidable by finite Moore-automaton partition refinement: initially split accepting from nonaccepting product states and repeatedly refine using both selector successors. With N=|S| states, either the partition stabilizes, certifying all-future equality, or an inequivalent pair has a distinguishing suffix of length at most N−1. Here N=9, giving a conservative finite bound 8. The three R states in fact differ already by length 0 or 1 suffixes. No claim is made that this constructs a minimum BRC weighted-linear representation.

## 4. Theorem C: sharp static-versus-online conditional memory separation

**Fixed final-time query.** At depth three, the two different positive histories 000 and 101 share the exact O_3=(0,+1,-1), yet 000 contains 00 while 101 does not. For every m≥3 append the same suffix consisting of m−3 copies of selector 1. Both resulting histories have the same terminal and full affine effect by chronological composition, but opposite query truths. Hence at least one additional source-query bit is necessary at **every m≥3** when conditioned on the original complete-effect observation. The Boolean answer bit is sufficient, proving a **sharp one-bit** fixed-horizon cost.

**All-future online query.** A sharper effect-conditioned obstruction occurs at depth seven. The following three distinct positive histories have exactly the same complete-effect observation O_7=(2,-1,+1):

| history | monitor r | current queried truth |
|---|---:|---|
| 1110101 | 0 | false, trailing 1 |
| 1011010 | 1 | false, trailing 0 |
| 0000000 | 2 | true |

State r=2 is distinguished from the other two without adding any suffix. States r=0 and r=1 are distinguished by the common next selector 0: r=0 then becomes 1 and is still false; r=1 becomes 2 and is true. Their complete BRC terminal/effect observation is still identical after this suffix, because it was identical before and both execute the same labelled edge from the same q. Therefore **three distinct annotations are necessary in that one current observation fiber** for exact pathwise source-query answers under all finite futures, requiring at least ceil(log_2 3)=2 bits. The three-state DFA itself realizes this lower bound with at most two bits per individual path. This is a sharp online result at m=7, not a claim that two bits are always minimal for unrelated queries or graphs.

Thus an answer to today's provenance question (one bit) is not necessarily a sufficient state to answer tomorrow's question (two bits); both are much smaller than R255's full-history conditional rank tag of order m−(1/2)log_2 m+O(1).

## 5. Theorem D: exact total count invariant

Every q offers both distinguishable selectors. Thus there are exactly 2^m ordered histories irrespective of observed effect merging. Let A_m be the number whose selector word avoids 00. Separating words with terminal 1 and 10 gives A_m=A_(m−1)+A_(m−2), A_0=1,A_1=2, hence A_m=F_(m+2) with F_0=0,F_1=1. Consequently

\[
\sum_{q,\epsilon,k,\,r\ne2}H_m(q,\epsilon,k,r)=F_{m+2},
\qquad
\sum_{q,\epsilon,k}H_m(q,\epsilon,k,2)=2^m-F_{m+2}.
\]

These totals cannot in general replace the effect-conditioned query counts.

## 6. Executed exact verification

Independent Python and C++17 (boost::multiprecision::cpp_int) implementations each verified all steps m=0..96 in exact integers: positivity, path mass 2^m and Fibonacci no-00 count. Each independently enumerated every selector word through m=12: sum_{m=0}^{12}2^m=8,191 histories checked against DP. Both verified the 3-step and 7-step witnesses. They did NOT enumerate 2^96 histories.

| m | path count | avoiding 00 | containing 00 | nonzero joint query-effect atoms |
|---:|---:|---:|---:|---:|
| 3 | 8 | 5 | 3 | 7 |
| 7 | 128 | 34 | 94 | 49 |
| 12 | 4,096 | 377 | 3,719 | 122 |
| 24 | 16,777,216 | 121,393 | 16,655,823 | 290 |
| 48 | 281,474,976,710,656 | 12,586,269,025 | 281,462,390,441,631 | 626 |
| 96 | 79,228,162,514,264,337,593,543,950,336 | 135,301,852,344,706,746,049 | 79,228,162,378,962,485,248,837,204,287 | 1,298 |

The infinite-horizon claims follow from the induction and finite congruence proof, not from 96 tested horizons.

## 7. Explicit reuse, limits, next question

Tool resolution: Source toolbox T0_BRC and T0_BRC_AFFINE_EFFECT_TRANSPORT, registry blob 3889506451091ebcfbf7a58cda6517c4af8c3597. Reuse state **REUSE_APPLIED** for exact Affine.then and EffectHistogram/ControlPacket source laws; **REUSE_EXECUTED not claimed** because no installed original enterprise_math package was available. The source EffectHistogram merges edge-word provenance, so the query monitor is an **EXTEND_EXISTING_TOOL** candidate rather than a new admitted family.

Native session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false; task inventory returned CONTROL_QUOTA. Neither active owner nor winning CLAIM was established. GitHub research draft publication is an **author-side versioned note only**; not a formal Result/Research Driver review or Foundation theorem. Actual R193 source-path grammar, physical edge IDs, time-port observer query and native legal six-axis heartbeat actions remain unverified.

**R257 next exact unit:** Obtain the real R193 source-token/observer/port specification at an immutable Source pin; prove a word-preserving or explicitly quotienting map into a query-labelled BRC carrier, or give an exact counterexample. If real R193 queries are nonregular, do not substitute the 3-state demo DFA; identify necessary additional memory. Execute Source-matched original ControlPacket.from_edges/then and compare exact effects and source observer, without asserting unproved heartbeat legality. Formal task activation and independent review require new authorized native gates.

**Do not repeat:** R254 shared-DAG theorem, R255 full-history rank/unrank, or R256 proofs without a new fidelity/legality input.