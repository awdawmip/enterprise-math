# R5 — Exact minimal adaptive choose-one source transducer for one named Set control

**Date:** 2026-11-16 (Asia/Shanghai). **Frozen scientific input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## 1. Exact question, old foundation, and observation scope

Continue [the static choose-one theorem](../r5_shared_source_helly_20261116/STATIC_CHOOSE_ONE_OPTIMAL_ALPHABET_TRIBONACCI_THEOREM.md) and [the common-source Helly-two theorem](../r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md) at source PR #2427, commit `576a408cfa86af78c15bb26110c800edbff9610a`. Use the previously established cycle of k>=3 triangles, with k named spine helpers, every leaf helper available, and a binary *unavailability* mask u. The one-step optimal source-labelled library size is 5k+q(u), where q(u)=sum_i u_i*u_(i+1) with cyclic indices. A fixed library is simultaneously individually optimal for a finite family U exactly when q(OR U)=q(v) for every v in U.

Here the **only future commands** are Set_0(0) and Set_0(1), overwriting unavailable bit u_0. A deterministic finite Moore transducer is required, from every initial u, to output after each command (including the empty word) a *concrete labelled* feasible library of cardinality exactly 5k+q(u), and to update its internal state deterministically according to the named command. Minimize the number of reachable internal states when arbitrary u may be the initial input; output labels and source identities are part of the observer. The transducer may choose one optimum rather than represent all optimum libraries.

This is an **auxiliary discrete integer-indexed centre model**. The P000 native X6 and Heartbeat World contracts, input pin and original Source/CLAIM authority remain fixed. The proof certifies a quotient for exactly this observer and its unrestricted Set_0-word horizon.

## 2. Exact transducer-state theorem

Put n=k-1 and write u=(b,z), where b=u_0 and z=(u_1,...,u_(k-1)) is an n-bit path word. Define
```text
C(z) = sum_{i=1}^{n-1} z_i z_(i+1)
s(z) = z_1 + z_n
Q_0(z) = C(z),           Q_1(z) = C(z) + s(z).
```
For k=3 this formula includes the single path edge between z_1,z_2.

Let P_n be the set of length-n binary words containing **no ordinary contiguous 000 substring**. Let T_n=|P_n| and A_n=|{z in P_n:z_1=z_n=0}|. Then the minimal number of states among all source-labelled adaptive choose-one transducers for the stated command alphabet is exactly
```text
N_k = 2 T_(k-1) - A_(k-1),    for every k>=3.
```
T_0=1,T_1=2,T_2=4 and T_n=T_(n-1)+T_(n-2)+T_(n-3) for n>=3. The endpoint-zero count A_n has A_2=1,A_3=1,A_4=3 and A_n=A_(n-1)+A_(n-2)+A_(n-3) for n>=5 (equivalently, use the regular-language finite automaton with fixed first/last zero).

The theorem is about *minimal deterministic state cardinality*, not only a minimum number of different static library outputs.

## 3. Necessity: source compatibility + Set-congruence

Each exterior word z has two raw states (0,z) and (1,z). Write a_z and b_z for their transducer state images. Let δ_0 and δ_1 be Set_0(0/1). From the physical reset semantics, δ_0(a_z)=δ_0(b_z)=a_z and δ_1(a_z)=δ_1(b_z)=b_z.

If any of a_z,b_z shares a transducer state with any of a_t,b_t, applying δ_0 and δ_1 forces a_z=a_t and b_z=b_t. Thus exterior words are partitioned into groups, with each group contributing **one or two** internal states; a group contributes one iff its a and b states coincide.

Within a group S the one B-output must be a fixed individually optimal labelled library for all (1,z), z in S. By the inherited exact common-library theorem, Q_1(OR S)=Q_1(z) for every z in S. Likewise Q_0(OR S)=Q_0(z) because the A-output is common. Thus both Q_0 and s=Q_1-Q_0 are constant within each group. If s>0, the two individual optimum cardinalities differ, forcing two distinct states. If s=0, one state remains possible.

Call z **Q_1-fiber-maximal** if there is no strict bitwise superword t>z with Q_1(t)=Q_1(z). Every z extends to a fiber-maximal superword without changing Q_1, and coordinatewise monotonicity of the nonnegative components Q_0,s makes their values constant along this extension. Distinct fiber-maximal words cannot be in the same exterior group: any common group union would be a strict superword with the same Q_1 value, contradicting maximality. Thus one or two states are forced per distinct fiber maximum, with the weight determined by its s value. This proves the lower bound
```text
N >= sum_{w fiber-maximal} (1 + indicator[s(w)>0]).
```

For Q_1(z)=z_1+z_n+sum z_i z_(i+1), flipping a zero endpoint to one always raises Q_1. At any interior position, flipping a zero raises Q_1 exactly when at least one neighbor is one. Therefore fiber-maximal words are precisely P_n, those without 000. Among P_n, s=0 precisely when both endpoints vanish, a set of cardinality A_n. Hence the lower bound equals 2T_n-A_n.

## 4. Attainment: deterministic source-preserving construction

Fix an order of exterior bit positions. For each z, greedily flip any zero whose change leaves Q_1 constant until reaching a fiber maximum w(z). Each flip is monotone and cost-preserving; w(z) is in P_n, z<=w(z), Q_1(z)=Q_1(w(z)). Because Q_1=Q_0+s is a sum of two nonnegative coordinatewise-monotone functions, both Q_0 and s are separately constant on this extension.

For each maximal w with s(w)>0, create two states (w,0) and (w,1), outputting the inherited canonical source-labelled optimum library L(0,w) or L(1,w) respectively. For each maximal w with s(w)=0, create a single state (w,*), outputting L(1,w). The latter library is also feasible and cardinality-optimal at (0,z) whenever z<=w in the same Q_1 fiber: unavailable sets only shrink and q stays constant. Likewise both libraries are feasible and optimal for all raw states mapped to them.

Map (b,z) to (w(z),b) if s(w(z))>0, otherwise (w(z),*). Set_0(c) acts by replacing the second label with c (or retaining *). It is a well-defined deterministic transition on the quotient because commands never modify z or w(z). Every word, however long, preserves correctly named and available source provenance and outputs an individually minimum-size library. This attains the lower bound.

The counting recurrences follow by the finite-state 000-avoidance transfer and fixed endpoint constraints. They are exact for every k>=3.

## 5. Exact values, independent computations, and inherited source labels

| k | Static optimum output alphabet M_k | Adaptive Set_0 states N_k | Scalar-only future states | Full Opt spectrum |
|---:|---:|---:|---:|---:|
| 3 | 7 | 7 | 5 | 8 |
| 4 | 11 | 13 | 9 | 16 |
| 5 | 21 | 23 | 14 | 32 |
| 6 | 39 | 43 | 19 | 64 |
| 7 | 71 | 79 | 24 | 128 |
| 8 | 131 | 145 | 29 | 256 |
| 9 | 241 | 267 | 34 | 512 |
| 10 | 443 | 491 | 39 | 1024 |
| 11 | 815 | 903 | 44 | 2048 |

The script `VERIFY_R5_SINGLE_SET_ADAPTIVE_SOURCE.js` was executed through its own exact integer/Boolean verifier functions before source publication; it checks every raw input for k=3,...,11 (4,088 masks), source eligibility and cardinality, all 8,176 Set transitions, and 179,750 pairwise maximal-source incompatibilities. Separately, for k=3,4,5 it enumerates *every* subset of exterior configurations as a potential common-optimal group and solves the exact weighted grouping problem independently of the proposed fiber-maximal construction. All minima agree.

The source witness uses old-core labelled `O1-edge`, optional `O0-edge`, and paired `O0-helper/O4-helper` sources, with triangle edges indexed deterministically. Its edge-incidence feasibility and number of sources are checked directly; the radius-two indexed-core equivalence is inherited from the exact original source theorem. The script uses no floating point or stochastic assumptions. The full finite evidence is included as JSON.

## 6. Consequence and next problem

For k=6 and one named controllable spine helper, the minimum adaptive source transducer has **43 states**, versus **39** static chosen outputs, **19** scalar-observation future states, and **64** full raw-source-spectrum states. Hence adding just one named Set command can require more dynamic states than a static one-optimum library selector, but still admit a strict source-preserving compression relative to all 2^k masks.

Next resolve two *adjacent* named controls J={0,1}: obtain either a sharp state count or a finite constructive/optimization algorithm preserving optimum labelled libraries and Set-congruence. Test the inherited k=6 masks with unavailable helper 3 versus 4; they are scalar-future equivalent but have no common individual-optimum library of size 30.

**Attribution:** historical researcher `EM-DIRECT-B78E55`, Activity `RA-33C87C2B703418F0706695E9` (not an authenticated current execution CLAIM). No Result/Review/Task publication or protected Activity mutation is implied by independent research preservation.
