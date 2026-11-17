# PREFIX-853 — Fixed-modulus dynamic named BRC: exact lifetime resynchronization dichotomy

Date: 2026-11-17. Status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Dependencies: PREFIX-850 (one-source local update), PREFIX-851 (erased observation), PREFIX-852 (partial prior baseline). Provenance: independent auxiliary positive-integer named-source Q-observer; historical research lineage EM-DIRECT-B518B3 / RA-14044F2E842D112941E256BF. No shared RS-X6-NATIVE-TIME-DYNAMICS CLAIM is asserted.

## 1. Precise experiment and two types of uncertainty

Take p>=1 named binary sources, x=(x_0,...,x_{p-1}) in {0,1}^p, and the injective source-named code

    U(x) = sum_{i=0}^{p-1} 2^i x_i.

At the first resumed observation, the observer knows the old values only on K={0,...,p-1}\J, with J unknown. During r>=0 lost steps, at most one named source flips per step (no-op allowed). Therefore the exact first-current-state candidate set given old known assignment z_K is

    R(z_K;J,r)={x: Hamming(x_K,z_K)<=r}.

After this first resumed observation, at each new observed heartbeat at most h>=0 named source coordinates may flip; this is an explicitly enlarged auxiliary transition family, reducing to one flip when h=1. The observer knows J, r, h, the old known assignment, time t, the public fixed baseline S_0, and a single *fixed odd integer* q>=3. At each observed step it reads

    Y_t(x)=c_t(S_0+U(x)) (mod q),   c_t=2^{floor(t/2)}.

All times are integer indices of the declared observer update, not inferred physical X6 duration. Odd q ensures c_t has an inverse, hence the observed residue is equivalent to U(x) mod q at every step. The receiver retains all observed residues and may decode with unlimited computation; the theorem minimizes only the raw modulus/port width, not the receiver's total memory or latency. The prior complete named state may be used after its exact recovery.

For any subset J and nonnegative integer v define the *nonzero divisibility obstruction set*

    D(p,J,v) =
      { |sum_i epsilon_i 2^i| >0 :
        epsilon_i in {-1,0,+1},
        |supp(epsilon) intersect K| <= 2v },  K=J^c.

All entries are nonzero integer values <2^p. Put

    D_init = D(p,J,r),
    D_step = D(p,empty,h).

The two sets have different semantics. D_init expresses collisions among initially possible states from a partially known old baseline; D_step expresses collisions between two possible successors of the *same fully known current state*.

## 2. Exact temporal theorem

**THEOREM 853-A (fixed odd modulus, arbitrary finite observation horizon).**
For *every* old known assignment z_K, every admissible missed-step history and every pair of later h-flip-per-step source trajectories, the last state x_w can be recovered uniquely from w>=1 consecutive residues with fixed odd modulus q exactly under the following conditions:

    w=1:    q divides no element of D_init;
    w>=2:   q divides no element of D_init union D_step.

The quantifiers are uniform over all legal source configurations and trajectories; no stochastic assumptions are made. The criterion for all w>=2 is independent of the number of extra heartbeats.

**Proof, initial ambiguity.**
Two first-current states x,y occur under one common old K assignment iff their K-Hamming distance is <=2r. Necessity follows from the triangle inequality; sufficiency follows by splitting their differing K coordinates into two groups of size at most r and choosing an intermediate common old assignment. J coordinates are free. Thus the first-residue collisions are exactly q|d for d in D_init (PREFIX-852-A). If a collision exists, choose the two distinct initial states and let both trajectories perform no-op transitions for all later steps. Since q and 2 are coprime, every subsequent observation stays the same for the two distinct constant states. Hence *no* finite length w can repair a failed initial observation at a fixed modulus.

**Proof, post-read ambiguity.**
For a known predecessor z, two next states x,y are each at Hamming distance <=h from z iff Hamming(x,y)<=2h. The forward implication is the triangle inequality; conversely, partition the differing bit coordinates into two groups, each of size at most h, and assign z to match the opposite candidate on each group. Across all predecessors z, possible nonzero signed binary difference values are exactly D_step. If q divides one such difference, choose the common predecessor as the first-current state, obtained by choosing old known bits to match it and no-op during the erased steps. The first observation is identical along both paths. At the second step split into the two distinct states x,y with equal second residues, then hold both states constant. Their observed streams agree at every later step, while their terminal named states differ. Therefore a horizon w>=2 cannot be uniformly lossless if D_step has a divisible member.

**Proof, sufficiency.**
When q avoids D_init, the first residue uniquely identifies x_1 in R(z_K;J,r). The receiver now knows its complete named state. When q additionally avoids D_step, each subsequent residue distinguishes every pair of successors within Hamming distance h of that previously recovered state. Inductively every x_j is recovered. Thus the last state is unique for any finite w, completing the proof.

## 3. Optimal raw port and special cases

Define, with min over odd q>=3,

    q_init^* = min {q: no d in D_init is divisible by q},
    q_life^* = min {q: no d in D_init union D_step is divisible by q}.

Both exist because q=2^p+1 is always sufficient. The exact optimum for a fixed one-residue window is q_init^* and for *every* fixed w>=2 is q_life^*. The output width is ceil(log2 q^*) bits.

**COROLLARY 853-B (continuing the original one-flip model).**
If r>=h, then D_step subseteq D_init: a signed difference supported on <=2h arbitrary coordinates necessarily has <=2r nonzeros on K. Hence

    q_life^* = q_init^*   whenever r>=h.

In particular for the PREFIX-852 observer with r>=1 missing one-source steps and h=1 future updates, its exact one-shot minimal q is also the minimal fixed odd q for arbitrarily long exact dynamic tracking, irrespective of unknown-source arrangement J. Additional repeated observations at that same q cannot repair an initial alias.

**COROLLARY 853-C (no missed steps can still incur future tracking cost).**
When r=0 and J is a single unknown source, first observation requires only q>=3 odd, but future one-flip-per-step tracking may require a larger q. Example p=4,J={0},r=0,h=1:

    q_init^*=3, but q_life^*=11.

The first reading distinguishes the two source-0 alternatives, while the later step must distinguish an arbitrary one-coordinate update. A 2-bit fixed modulus therefore solves the initial query; a 4-bit fixed modulus is optimal for all subsequent heartbeats.

Example p=6,J={3},r=h=1 yields q_init^*=q_life^*=27 (5 bits). q=25 fails because 25=1+8+16 is the absolute value of an allowed signed difference, with only two nonzero entries outside J. Thus a pair of named states can remain indistinguishable indefinitely under fixed q=25.

## 4. Exact computation

The accompanying standalone Python checker:
- Enumerates the full signed-difference sets for the declared small parameter ranges, without randomly sampling differences;
- Independently enumerates old known assignments, first-current candidate pairs, every allowed h-coordinate post-read transition and the equality of successive residues;
- Verifies the theorem's predicted terminal distinguishability against that separate path-pair oracle for w=1,2,3;
- Tests p=1..3 with every J and p=4 with J masks 0,1,2,3,8,12,15; r,h each 0..min(2,p); odd q=3..2^p+1.

Recorded result: 872 (p,J,r,h,q) instances, 2,616 terminal-window assertions, 280 instances satisfying the uniform lifetime condition, 592 failing it; all exact assertions passed. Counts concern code-verified finite coverage, not the source of universal quantification. Arithmetic uses integers; time normalization uses the invertible power of 2 rather than any physical oscillator or forbidden classical phase operation.

## 5. Scope and next discriminating problem

This result sharpens PREFIX-852's one-observation result to *repeated fixed-modulus dynamic tracking*. It is a theorem about the declared auxiliary named positive Q observer, preserving source identities. It does not identify U with a native X6 Cell/Link/Port event or prove a physical coupling/duration law. It does not address schedules with **different moduli** or feedback/adaptive moduli, for which the stationary no-op witness need not be indistinguishable at all later residues.

Next: construct the exact finite *paired-trajectory observer automaton* for variable odd q_t and distinguish three objectives: (i) terminal state after a fixed length, (ii) guaranteed resynchronization after some bounded length, (iii) continuous state tracking. Compare finite schedules with the fixed-modulus optimum at equal per-sample bitwidth while accounting for history memory and schedule signaling. Separately seek native typed BRC/Cell/Link/Port admission before transferring the observer's result to the X6 world.

Code: research_notes/portable_direct/PREFIX853_R6_FIXED_MODULUS_DYNAMIC_MEMORY_CHECK.py
Results: research_notes/portable_direct/PREFIX853_R6_FIXED_MODULUS_DYNAMIC_MEMORY_RESULTS.json
