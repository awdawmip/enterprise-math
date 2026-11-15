# R5 — Exact adaptive source-aware quotient for every named Set control subset

**Frozen input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Date:** 2026-11-16 (Asia/Shanghai). **Evidence:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Model, predecessor and objective

Continue the cycle-of-k-triangles auxiliary integer-indexed radius-two centre repair model, k>=3. There are named spine-helper unavailability bits u_i; old library sources retain explicit edge/core/helper identities. The exact individual optimum is `kappa_a(u)=5k+q(u)` with `q(u)=sum_{i mod k}u_i*u_(i+1)`. Inherited common-source theorem: one fixed source-labelled library is simultaneously individually optimal for a finite family U of masks iff `q(bitwise_OR U)=q(v)` for every v in U. Sources: [R5 common-source Helly theorem](../r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md) and [R5 single-control theorem](../r5_single_set_adaptive_source_20261116/SINGLE_SET_ADAPTIVE_SOURCE_TRANSDUCER_THEOREM.md), same Draft PR #2427.

Choose **any** named controllable set J of spine vertices. Commands Set_i(0) or Set_i(1), i in J, overwrite only the indicated bit; all finite command words, including the empty word, are permitted. The output after every command must be one concrete feasible *individually cardinality-optimal, source-labelled* old library. The transducer is deterministic, with its initial state selected from the raw u; minimize the total number of reachable states needed across all raw initial masks.

## General exact theorem

Let K={0,...,k-1}\\J be the fixed exterior vertices, z in {0,1}^K the exterior unavailability bits, and x in {0,1}^J the controllable bits. On the cycle write
```text
q(x,z) = H(x) + C(z) + sum_{i in J} b_i(z) x_i
H(x) = sum_{edge ij inside J} x_i x_j
C(z) = sum_{edge ij inside K} z_i z_j
b_i(z) = sum_{j in K, edge ij} z_j
d_i = number of i's neighbors belonging to J.
```
All coefficients are nonnegative. Put `F_J(z)=q(1_J,z)`, the cost after setting all controlled bits to unavailable. Let `M_J` be the set of **fiber-maximal exterior words**: w belongs to M_J iff no strict bitwise superword v>w has `F_J(v)=F_J(w)`. For w in M_J define the active-coordinate set
```text
A_J(w) = {i in J: b_i(w) + d_i > 0}.
```
Then the exact minimum deterministic adaptive choose-one source-transducer size is
```text
                 N(k,J) = sum_{w in M_J} 2^{ |A_J(w)| } .
```
The formula applies to every k>=3, every J (including empty and full), and every allowed finite Set word. It is a minimal-state theorem with an explicit optimal output and transition construction.

## Lower bound: two independent information constraints

For every exterior z, let its controlled cube `(x,z)`, x in {0,1}^J, be mapped into the transducer. Suppose any states from two exterior configurations z,t are identified. Apply the same command word setting **every** controlled coordinate to one; determinism then forces `(1_J,z)` and `(1_J,t)` to share a state. The identical Moore output must be one labelled library optimal for both. The inherited exact common-library theorem implies `F_J(z)=F_J(t)=F_J(z OR t)`.

Consequently distinct maximal exterior words w,v in M_J can never have a common transducer state, since equality for their OR would violate maximality (or their F_J values already differ). This gives mutually disjoint necessary state pools, one for each w in M_J.

For each fixed w, take two controllable assignments x,y differing in at least one active coordinate i. Set all other controllable coordinates to one without touching i. Their resulting scalar costs differ by `(x_i-y_i)*(b_i(w)+d_i)`, which is nonzero. Thus every distinct restriction x|A_J(w) requires a distinct internal state. There are exactly `2^{|A_J(w)|}` such restrictions. Summing over the disjoint maximal-word pools gives the stated universal lower bound.

## Upper bound: q-fiber extension, exact source validity, deterministic descent

For every exterior z, repeatedly flip a zero exterior bit to one whenever this does not raise F_J, using a fixed order, obtaining a maximal word w(z)>=z in M_J with F_J(w(z))=F_J(z). Because
```text
F_J(z) = H(1_J) + C(z) + sum_i b_i(z)
```
and C,b_i are each coordinatewise nondecreasing, their individual values are equal at z and w(z). Therefore `q(x,z)=q(x,w(z))` for **every** controlled assignment x, and the active sets agree.

Create one transducer state `(w,a)` for each w in M_J and every `a in {0,1}^{A_J(w)}`. Map raw state (x,z) to `(w(z),x|A_J(w(z)))`. Under Set_i(v), update a_i to v when i is active; otherwise leave the abstract state unchanged. This is a well-defined deterministic action with the correct transitions for every finite command sequence.

For a state (w,a), form the full controlled assignment x^+ which agrees with a on active coordinates and sets every **inactive** coordinate to 1. Output the inherited canonical labelled optimal library for the raw mask (x^+,w). For every raw (x,z) represented at the same state, its unavailable-set mask is bitwise bounded by (x^+,w), and its q value is equal: the changed exterior bits preserve C and b, while changing inactive controlled coordinates does not change q. Hence this fixed library is source-valid for every represented raw input and has the exact individually minimum cardinality `5k+q(x,z)`. This attains the lower bound.

This is an explicit observer- and operation-scoped source/provenance compression certificate; all original raw source labels remain in the emitted library.

## Closed-form consequences

1. **No controllable vertices:** J=empty yields one state for each cyclic 000-avoiding maximal word, reproducing the static optimum-alphabet count M_k.
2. **Every vertex controllable:** J=all yields a single exterior word with all k coordinates active, so N(k,J)=2^k.
3. **Exactly one controllable vertex:** J={0} recovers `N=2 T_(k-1)-A_(k-1)`, with T_n the number of ordinary n-bit words avoiding 000 and A_n the subset with both endpoints zero.
4. **Two adjacent controllable vertices:** for J={0,1}, each controlled vertex has one controlled neighbor, so `|A_J(w)|=2` for every w. The complement is a path of n=k-2 exterior vertices, each endpoint penalized in F_J. Its fiber maxima are precisely the length-n path words avoiding 000 (for n=1,2 all words qualify). Hence
   ```text
   N(k,{0,1}) = 4 T_(k-2),    every k>=3.
   ```
   T_0=1, T_1=2, T_2=4, T_n=T_(n-1)+T_(n-2)+T_(n-3).
5. **Nonadjacent control comparison:** for k=6 and J={0,3}, every exterior position is adjacent to one controlled vertex, hence all 16 exterior words are fiber-maximal. Each controlled vertex has two distinct exterior neighbors. Summing the four possible neighbor pair values for each controlled vertex gives 1+3*2=7; the two independent pairs contribute `N(6,{0,3})=7^2=49`.

| k | Adjacent two-control exact states | Full raw masks |
|---:|---:|---:|
| 3 | 8 | 8 |
| 4 | 16 | 16 |
| 5 | 28 | 32 |
| 6 | 52 | 64 |
| 7 | 96 | 128 |
| 8 | 176 | 256 |

In particular, k=6 gives 52 states for adjacent controls and 49 states for opposite controls, compared with 64 raw states. The previous six-cycle masks with only helper 3 respectively helper 4 unavailable remain distinguished by the source-aware quotient despite their scalar future observations being identical under J={0,1}.

## Reproducibility and independent finite cross-check

The companion `VERIFY_R5_GENERAL_SET_ADAPTIVE_SOURCE.js` uses only exact integer/Boolean operations. It executes the construction for every k=3,...,8 and **every** named control subset J (504 pairs (k,J)). It checks all 87,360 raw-state library outputs for provenance feasibility and the exact cardinality, all 669,888 named Set transitions, and 121,883 distinct-maximal incompatibility pairs. Independently, for adjacent two controls k=3,...,6 and opposite controls k=6, it enumerates all subsets of exterior configurations as potential groups, requires each group's fixed library to be optimal under the full Set assignment, and solves the exact weighted group-partition DP without using the proposed fiber-maximal formula. The exact minima match.

All universal claims are supported by the constructive lower/upper proofs. Independent mathematical review and native X6 interpretation remain separate; the auxiliary result does not alter the frozen scientific pin, P000 or Heartbeat World. No Result, Review, Task or protected Activity mutation was requested for this scientific preservation.

**Next question:** Characterize when source-aware transducer states can be compressed further if the output is allowed to be a *repair program* that uses an explicitly bounded number of nonoptimal intermediate libraries, rather than always emitting an individually optimal library at each command. Keep concrete source labels and compare the exact bounded-operation observer with the present theorem.

Historical scientific provenance: `EM-DIRECT-B78E55` and `RA-33C87C2B703418F0706695E9`. Current Source execution CLAIM/owner remains a separate control question.
