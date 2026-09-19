# Finite-carry multi-prime routing: bounded control, planar obstruction, and congestion

Status: RESEARCH_NOTE / ELEMENTARY_DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-FINITE-CARRY-ROUTING-20260910-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local continuity key, not a platform ID)
Mode: TASK_RESEARCH / direct user continuation / no Task-ID or CLAIM
Date: 2026-09-10
Source snapshot: enterprise-math@a12be839318bded31998207ee18ef76762b7a856
Parent note: research_notes/nollm_chart_neighbor_locality_20260910_c6c82.md at 4b60cc6500d9ec5057528c2daf4be3cfcc84db63
Unchanged parent executable: experiments/nollm_chart_neighbor_locality_20260910_c6c82.py at f66eb4799a0ae1ef728cdb40e443fea122c2ff45
Parent executable SHA256: 3e09fb193258ad328fcad8d5e7678a69234d719e57ed02cfedbee77d26e3778b
New executables: experiments/nollm_finite_carry_routing_20260910_c6c82.py; experiments/nollm_permutation_fabric_20260910_c6c82.py

## 1. Question, provenance, and population

Consume the nine existing checkpoints; do not replay them as discoveries. The exact next question is whether prime-local distance control can be realized jointly, and what a bounded-degree hierarchy pays when transporting the six relation ports.

This is ordinary rank-two lattice/computational-network mathematics, a comparison slice. P000, Nollm physical cells, layers, and runtime are not modified. Quotient capacity multiplication is not an embedding of ordinary integer-label multiplication. Geometric adjacency is a synthetic proxy, not a measured semantic relation.

Keep separate: fine-grid hex hops; digit operations; logical router hops; simultaneous cut load; switch stages; and wire length. None is silently substituted for another.

## 2. The single-11 rescue does not stay planar-local in a joint CRT plane

Use the parent's C=[[-4,1],[21,-5]], det C=-1, at 11 and identity at 5. At simultaneous even precisions t, the common plane is X_M=(Z/MZ)^2 with M=5^t*11^t. Let B_t be the unique matrix modulo M satisfying B_t=I mod5^t and B_t=C mod11^t.

Every lift v of B_t e1 satisfies v=e1 mod5^t, but v cannot equal e1 because C e1 differs modulo 11. At least one coordinate of v-e1 has magnitude >=5^t. Hence its hex graph norm max(|q|,|r|,|q+r|) is >=5^t-1. The forward edge cost already diverges; retaining the 26-hop local bound on the joint plane is false.

Exact six-generator checks:

t | M | maximum forward hex hops
1 | 55 | 10
2 | 3025 | 1426
3 | 166375 | 94500
4 | 9150625 | 5504999

These are exact modular generator calculations, NOT enumerations of M^2 states. Deeper values through t=8 are included in results.

More generally, for a cofinal system where every retained prime precision tends to infinity, a prime-local tuple (V_p) has uniformly bounded forward AND inverse images of the physical unit generators on the common CRT plane only if all V_p are reductions of the SAME C in GL2(Z). Proof: bounded integer lifts become unique once the common modulus exceeds twice the bound; compatibility forces constant columns. Apply the same argument to the inverse. Conversely such a common integer-unimodular matrix supplies a bound. Demanding exact identity at every 5 precision forces this common matrix to be I, excluding a nontrivial 11 action. This is a refinement of the parent's local determinant criterion, under the stated cofinal/linear/metric contract.

## 3. A physically long transformation can have a tiny finite carry automaton

Write a prime-local transformation as y=A x/d, where A is an integer 2x2 matrix and both d and det A are units modulo p. Read each coordinate in base p, least significant digit first. For input digit pair x_i in {0,...,p-1}^2, use

z_i=A x_i+c_i,
y_i=d^(-1) z_i mod p,
c_(i+1)=(z_i-d y_i)/p,
c_0=0.

Then A X_n-d Y_n=p^n c_n for the n-digit truncations. The output is exactly the desired modular map, and extending the input cannot change earlier output digits.

For row j put P_j=sum of its positive entries and N_j=sum of the absolute negative entries. The fixed interval

-N_j-d <= c_j <= P_j

is invariant: use 0<=x_i,y_i<=p-1 in the recurrence. Thus the carry set is finite, independent of depth. Breadth-first exploration terminates within this proved finite box, and closing every transition is an all-depth certificate, not a guessed large-depth cutoff.

For U=A/13 with A=[[1,-3],[3,4]], and U^-1=[[4,3],[-3,1]], there are exactly 22 reachable carry states in each direction, at both p=5 and p=11. There are 550 transitions at p=5 and 2662 at p=11. The integer C and its inverse use 30 carry states at p=11, or 3630 transitions each. The old and new coordinate conventions are not conflated.

Different carry states c give different residual affine functions (A x+c)/d. They cannot agree at every precision unless c is equal. Exact Mealy partition refinement independently confirms these pair-alphabet machines are minimal for this specific coordinate-digit encoding. This is NOT a minimum hardware-memory claim, and 22 is NOT the number of states of the complete rotating-tower transducer below.

## 4. One arithmetic layer in, one layer out; no full-address waiting

Reuse the parent's encode_digits/decode_digits and three-phase active_line functions unchanged. In each coordinate-digit pair, the first tower label is chi_l(x_i), the second is a complementary coordinate; l rotates by W each pair.

A tower machine retains (carry, phase mod3, pending first digit or NONE). On the first input label alpha, temporarily set its complementary input beta to zero and compute the first output label. The three-line compatibility of the matrix makes that output INDEPENDENT of beta. Every possible beta was checked on every reachable first-half state. On the next beta, emit the second label and update the carry. Thus it emits exactly one p-ary refinement label per input label, including at odd truncations.

Full finite machine counts:

map | carry states | reachable tower states | minimized tower states
U5 and inverse | 22 | 396 | 264
U11 and inverse | 22 | 792 | 462
C11 and inverse | 30 | 1080 | 790

The minimum is for the declared finite-state letter-to-letter map and digit encoding, computed by exact output/transition partition refinement to a fixed point. Complete raw graphs and partitions are reproducible outputs. Every state has a permutation of its output alphabet, so these are rooted-tree automorphisms. They preserve common-prefix depth in the p-ary tower. This is hierarchical proximity, NOT hex-plane physical proximity.

The U machines keep the earlier normalized first-layer labels and addition. C keeps the earlier explicitly rescaled first-layer convention and addition. In particular the 5 planar no-go does not imply that 5 needs unbounded control memory; it admits the 264-state serial machine. The cost is O(k) digit steps and a k-digit output address, not O(1) time or total memory.

Separate prime machines can be interleaved in any order that preserves each prime's own input order; their product outputs and all component projections agree. No repeated giant global inverse or complete point-cloud expansion is needed to convert ONE address. Other prime factors pass through unchanged. This does not claim physical locality on a common plane.

## 5. A bounded-degree routing tree: exact endpoint, logarithmic route, linear congestion

For a concrete network use equal even tower depths k5=k11=2t, with N=55^(2t) terminal identities. Interleave their tower labels by refinement level. Encode a base-5 digit in three bits and a base-11 digit in four bits, retaining only valid codewords. The resulting binary prefix tree has maximum degree 3 including the parent, depth H=14t, and leaf-to-leaf paths <=28t. These are added ROUTING microlevels, not Hecke layers or Nollm physical layers. No equal-probability claim is made for intermediate bit branches.

At t=1, all 3025 endpoints and all six directed original unit-neighbor messages per endpoint were executed after applying U5 and C11. Results:

- 6721 tree nodes, including 3696 internal routers and 3025 terminals;
- 18150 complete routed messages; every transported endpoint and synthetic integer aggregation correct;
- maximum route 28 logical edges; mean 108/5=21.6;
- route counts by length: 12:3630, 14:2420, 24:4840, 26:2420, 28:4840;
- maximum per-edge load for the simultaneous round: 4840 messages.

The congestion is not accidental. The root branch with bit prefix '1' is exactly the first base-5 label 4. For the normalized U5 that label is the source r mod5. Its bucket contains N/5 vertices. Four of the six original unit directions cross out, and the four reverse messages cross in, giving exactly 8N/5 messages on that cut. Under total undirected edge capacity one per tick, any schedule takes at least 8N/5 ticks; under independent full-duplex unit capacities each direction takes at least 4N/5 ticks. Thus logarithmic dilation does not imply logarithmic parallel service time.

This tree closes bounded-fanout abstract endpoint routing, not a scalable low-congestion physical memory layout. Individual wire lengths, queues, memory area, and sequential-versus-concurrent workloads remain material.

## 6. Distributed comparison: classical Benes permutation fabric

Do not stop at the congested tree. Each transported relation port is a permutation of the same N identities. Route the six ports in separate passes through a classical rearrangeable binary permutation network. This is an explicit application of established Benes routing, not a new network theorem.

At N=3025, pad with 1071 idle ports to width K=4096. A K-input Benes network has 2 log2 K-1=23 stages and K/2*(2 log2 K-1)=47104 two-by-two switch elements. The implementation configures it recursively: color alternating input-pair/output-pair cycles, send opposite colors into the two subnetworks, and recurse.

All six transported port permutations were configured and executed. Every intermediate stage contains each token exactly once; every real message reaches its prescribed terminal. Six separate passes aggregate the original six-neighbor signal exactly. With precomputed controls, fully parallel switches, and one unit per interstage wire per stage, the six nonoverlapped passes use a budget of 6*23=138 switch stages with no wire conflicts within a pass.

This is NOT a measured speedup from 4840 ticks to 138 real clock cycles. The network has much more hardware and nonlocal interstage wiring. Configuration needs O(K log K) work/storage; the 22-state arithmetic controller does not replace these switch settings. Geometric wire delay, memory-bank bandwidth, hardware placement and physical fanout compliance remain unimplemented. Each switch has only two inputs and two outputs, but small local degree alone does not solve spatial embedding.

The whole circuit and six configurations can be deterministically regenerated from the source. A separate 176-test small/exhaustive/random permutation suite checks 12700 token endpoints in addition to the actual six 4096-port runs. The 2x2 switch construction and stage-wise bijections supply collision-freedom; the final endpoint test checks the requested permutation, not merely an arbitrary bijection.

## 7. Exact execution and limits

Core verification: 65976 fully enumerated word/classes at depths1..4 across six maps; 66816 prefix checks; 32988 inverse-word checks; 131952 additive-generator checks; 1080 vector-digit checks; 1200 mixed-prime interleavings; 840 deeper sampled words through depth257. Depth257 is sampled; no astronomical full enumeration is claimed. All-depth causality and bounded memory follow from the carry interval and closed finite transition graph.

Two fresh executions of both final programs produce byte-identical summary JSON; all finite-machine tables and switch configurations also match. Existing locality and tower functions are imported unchanged after SHA256 checks. Raw machine state counts are counts of controller states, not simultaneous memory branches or independent remembered numbers.

BRC REUSE_EXECUTED: prior tower bases, residue canonization, rotating frames, exact transports and locality constants. EXTEND_EXISTING_TOOL: task-local streaming realization and routing audit. COMPOSE_APPLIED: keep identity, relation port, phase, carry, and component precisions separately. Six-port reduction uses proven translation invariance. The tree cut counts preserve message multiplicity; the same terminal support cannot certify throughput. The initial lookup surfaced no extra relevant carry implementation; this is not a claim that the project lacks every equivalent tool or that classical automata/network ingredients are novel.

## 8. Remaining frontier and interpretation

Resolved in this slice: a common-plane obstruction stronger than the single-factor claim; exact finite-state all-layer arithmetic conversion for 5/11; a bounded-degree hierarchical route; an explicit congestion witness; and an executable distributed permutation-fabric alternative with honest resource accounting.

The promising split is stable identity / streamed coordinate translation / separately provisioned relation routing. Uniform planar placement alone is inadequate. The next missing physical contract is how much distributed routing capacity and wire length are permitted by actual Nollm layer/coverage mechanics. No live Nollm code was changed. Ordinary integer multiplication intrinsic to a planar field, arbitrary-prefix uniformity, and semantic-neighbor utility remain unresolved.

Classical sources: Anashin, Automata finiteness criterion in terms of van der Put series of automata functions, arXiv:1112.5089; Mirzaei, Minimum Average Delay of Routing Trees, arXiv:1601.02697; Koloko, Design and implementation of fast and hardware-efficient parallel processing elements to set full and partial permutations in Benes networks, DOI 10.1049/tje2.12037 (2021); Kannan, The KR-Benes Network, arXiv:cs/0309006. These provide comparison context, not proofs of this experiment's exact numeric certificates. No novelty or Foundation acceptance is claimed for CRT, finite automata, or permutation networks.
