# PREFIX-494 — Exact finite-horizon minimization of BRC–KMP first-source readouts
Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_MACHINE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific input freeze: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: `2026-11-04_prefix493_full_kmp_source_mask_transfer_and_brc_append_closure.md`.
Researcher-ID: `EM-DIRECT-F01175`, activity `RA-E7360CFEC8B30A2194A01B38`. No formal claim.

## Model and exact question
Use restricted native X6 signed ordinary primitives `aAbBcCdDeE` (special sixth axis unused). Terminal KMP gate `g=aab` or `aba`; state q in 0..3; first b/B-versus-c/C source tag t in {N,B,C}, where N means neither observed, B means first observed source is b/B, C means c/C. Underlying integer BRC observation is (n, five signed displacements y, V=p_b+2p_d+p_e, W=p_c+p_e), with p_i=min(u_i,v_i), and native ordered appends update all these fields exactly as in PREFIX-493.

For a declared finite-state output O, two reachable (q,t) states are H-equivalent if every signed-letter suffix of length at most H gives the same output trace at all intermediate times. This is a source/observer-relative quotient, not an identity of all native path, branch, phase and multiplicity data. Outputs are: `q_fulltag=(q,t)`, `q_firstB=(q,[t=B])`, `accept_firstB=([q=3],[t=B])`, `firstB=[t=B]`, and `accept=[q=3]`.

## Theorem 1 — exact number of minimal horizon states for every H>=0

| gate | output | H=0 | H=1 | H>=2 |
|---|---|---:|---:|---:|
| aab | q_fulltag | 11 | 11 | 11 |
| aba | q_fulltag | 10 | 10 | 10 |
| aab | q_firstB | 8 | 11 | 11 |
| aba | q_firstB | 8 | 10 | 10 |
| aab | accept_firstB | 4 | 8 | 11 |
| aba | accept_firstB | 4 | 7 | 10 |
| aab | firstB | 2 | 3 | 3 |
| aba | firstB | 2 | 3 | 3 |
| aab | accept | 2 | 3 | 4 |
| aba | accept | 2 | 3 | 4 |

In the two-Boolean observation `accept_firstB`, exact minimal fixed-width control memory is 2 bits for H=0, 3 bits for H=1, and 4 bits for H>=2, for both gates. `aab` has the extra reachable state (q,t)=(2,N); `aba` does not.

### Exhaustive finite transition proof
For each q=0,1,2,3, KMP successors under lower-case a/b/any other character are:
```
aab: q0 => 1/0/0; q1 => 2/0/0; q2 => 2/3/0; q3 => 1/0/0
aba: q0 => 1/0/0; q1 => 1/2/0; q2 => 3/0/0; q3 => 1/2/0
```
The source automaton sends N->B on b/B, N->C on c/C, and leaves t unchanged on all other symbols or from B/C. Thus five representative letter classes `a, b, B, c/C, A/d/D/e/E` exhaust all ten signed directions. Forward reachability from (0,N) gives precisely 11 aab states (N with q0,1,2; B/C with q0,1,2,3) and 10 aba states (N with q0,1; B/C with q0,1,2,3).

Define the output partition P_0 by equality of O(s) and recursively P_(h+1) by equality of O(s) and by all corresponding successor classes in P_h. Induction on h proves that P_h equals H-future equivalence. Applying the complete displayed table yields the cardinalities above; `prefix494_automata_certificate.py` independently computes shortest distinguishing words for all unequal pairs and checks that their lengths match the first partition separation, at H=0..7. For `accept_firstB`, the H=1 aab classes are:
`{0B,1B};{0C,1C};{0N,1N};{2B};{2C};{2N};{3B};{3C}`.
For aba, remove `{2N}`. P_2 separates every state. In particular the suffix `ab` distinguishes q0B/q1B for aab, and `ba` does so for aba; appending `b` distinguishes equal-q N and C. This gives matching constructive upper/lower bounds for all H>=0: each quotient block is exactly one indistinguishability class and every different block admits a witnessing suffix.

For `firstB` alone the q component is forever irrelevant; N versus C is distinguished by appending b. For `accept` alone, the source tag is forever irrelevant; all four KMP states are distinguished after at most two appended symbols.

### Update compatibility
For H>=1, s ≡_H t implies step(s,x) ≡_(H−1) step(t,x) for every primitive append x. Hence the smaller finite-horizon quotients are exact for a query with a decreasing remaining budget. Unrestricted repeated appends for `accept_firstB` use the stable H>=2 11/10-state machine (4 bits).

## Theorem 2 — representation cost
For 0<=n<=N, individually range-encode n in ceil(log2(N+1)) bits; each of five y_i in ceil(log2(2N+1)) bits; V in ceil(log2(N+1)) bits; and W in ceil(log2(floor(N/2)+1)) bits. Adding b_H in {2,3,4} control bits for the two-Boolean query gives a valid zero-error separate-field upper bound
```
2 ceil(log2(N+1)) + 5 ceil(log2(2N+1))
+ ceil(log2(floor(N/2)+1)) + b_H
= 8 log2(N) + O(1).
```
At known fixed length n, omit the n field for 7 log2(n)+O(1). The BRC-base distinct-fiber generating function from PREFIX-493, `(1+z)^2(1+2z^2)/(1-z)^8`, has fixed-length coefficient `n^7/420+O(n^6)`. Therefore a lossless code for this declared base observation requires at least `7 log2 n-O(1)` bits at fixed n, and at least `8 log2 N-O(1)` for all lengths <=N. The proposed field representation is asymptotically optimal in its leading bit exponent. The raw-to-observer preprocessing scan takes O(n) field operations on O(log N)-bit integers; each native append uses O(1) such operations and O(log N) bit work with elementary arithmetic. This excludes the cost of storing the raw path when the selected query does not demand it.

## Executed evidence and next question
Actual Python 3 standard-library execution checked full reachability and closure for the ten signed symbols, all reachable joint states, all five observers, H=0..7, and shortest witnesses for every state pair; status `ALL_CHECKS_PASS`. Full executed local JSON log SHA256: `9202067e67913350a8a730fac4dc0ef7790edfbe605f67e8892b5cc7ffddab18`. The remote concise log reproduces its observed counts, whereas the complete original run is retained in the associated local evidence archive. Finite automaton exhaustiveness, not path-length extrapolation, supplies the all-H proof.

Next PREFIX-495: compare rank/unranking and fiber-dependent encodings of the *combined* integer+finite BRC observer against this append-closed streaming code. Account for construction, update, output recovery, all bit resources, and extension to any newly declared branch/phase/provenance output. This project-specific observer compression is not a native physical-time or phase attribution claim. No formal Result, Review or Foundation admission has been made.
