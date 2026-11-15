# R5 — Exact slack-source cover and deterministic named-Set belief-state kernel

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / SOLVER_CROSSCHECKED / NOT_REVIEWED.

## Scope and inherited source semantics

This note continues [GENERAL_NAMED_SET_OPTIMAL_SOURCE_TRANSDUCER_THEOREM.md](../r5_general_named_set_adaptive_20261116/GENERAL_NAMED_SET_OPTIMAL_SOURCE_TRANSDUCER_THEOREM.md) and [SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md](../r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md) at the same frozen pin. The object is the auxiliary cycle-of-k-triangles indexed-centre radius-two repair model, **not** a native X6 Cell metric or a BRC physical execution.

For k>=3, let u in {0,1}^k encode unavailable named spine helpers, and let q(u)=sum_(i mod k) u_i u_(i+1). The minimum number of concrete old source-labelled entries in a valid single-a library is 5k+q(u). The inherited *common-source theorem* is stronger than a value identity: for any nonempty family B of raw masks, a library feasible for every u in B needs at least 5k+q(OR B) entries; the canonical library L(OR B) attains it. The canonical sources include all mandatory E1 edge entries, named H0/H4 helper pairs for available spines, and E0 entries for edges not covered by those pairs.

Fix an **additive slack** integer s>=0. An output at raw state u must be one feasible labelled library L with |L|<=5k+q(u)+s. Source labels are never relabelled or simulated. We study (i) a static dictionary that can choose an appropriate output for each u and (ii) a deterministic Moore transducer that must do so after every named Set_i(0/1) command. The input set includes all 2^k raw masks; the command alphabet is explicitly specified. Nonoptimal outputs of up to s extra entries are allowed; this is an exact bounded-resource observer.

## Theorem A — Exact static dictionary as a monotone finite cover

Let M_stat(k,s) be the smallest number of **distinct** fixed source-labelled library outputs sufficient for every raw mask. For v in {0,1}^k put

    C_s(v) = {u: (u & v)=u and q(v)-q(u)<=s}.

Then, for every k>=3 and s>=0,

    M_stat(k,s) = min {|D|: D subset {0,1}^k, union_(v in D) C_s(v) = {0,1}^k}.

In particular a minimum output dictionary can always be chosen from the canonical L(v), with its complete source provenance.

Proof: A canonical L(v) is feasible whenever u<=v; its size is 5k+q(v), so it serves exactly C_s(v) under the slack restriction. Conversely let L be any output serving a nonempty family B of raw masks, and let v=OR B. The common-source theorem implies |L|>=5k+q(v), while the slack bounds imply |L|<=5k+q(u)+s for each u in B. Thus every u in B belongs to C_s(v). Replacing L by L(v) preserves all those cases and never increases the number of outputs. Apply this replacement to every dictionary entry. QED.

This reduction is exact for *all* source-labelled old libraries admitted by the inherited graph model, rather than an arbitrary restriction to a preferred library family.

## Theorem B — Sharp large-slack discontinuities and universal lower bound

For every k>=3,

    M_stat(k,k)=1,
    M_stat(k,k-1)=3,
    M_stat(k,k-2)=4.

For every integer r with 1<=r<=k-1,

    M_stat(k,k-r) >= r+2.

In particular **two static outputs never suffice** for any s<k.

Proof of lower bound: The all-ones unavailable mask 1^k can only be served by canonical centre v=1^k. This centre has q=k and fails to serve every u with q(u)<r when s=k-r. Suppose there are at most r other centres v_1,...,v_r (some may be absent). Each v_j distinct from 1^k omits some vertex i_j. Form u with unavailable bits precisely the union of those omitted witnesses; this uses at most r vertices. A proper subset of fewer than k vertices in a cycle induces a disjoint union of paths, hence q(u)<=r-1<r. Therefore 1^k fails by slack, while every v_j fails the inclusion condition u<=v_j. This contradicts coverage. QED.

For s=k, L(1^k) has 6k entries and is within slack of every optimum. For s=k-1 choose the centres 1^k and 1^k\{i},1^k\{i+1} for two adjacent indices. The latter have q=k-2. Every q=0 mask omits at least one of the adjacent indices and is covered by one of those proper centres; q>=1 masks are covered by 1^k. This gives three outputs. For s=k-2 choose 1^k plus three single-vertex-deletion centres at three consecutive indices i,i+1,i+2. Every q<=1 mask omits at least one of those indices (all three present would give two internal cycle edges); every q>=2 mask is served by 1^k. The proper centres have q=k-2, hence meet the slack even for q=0. The lower-bound theorem makes both constructions sharp. QED.

## Theorem C — Exact finite belief-state optimization for adaptive source outputs

Let J subset {0,...,k-1} be the permitted named control coordinates and T_(i,b) overwrite the indicated bit to b. For nonempty B subset {0,1}^k define admissibility

    A_s(B): q(OR B)-min_(u in B) q(u) <= s.

Let F range over finite families of distinct nonempty admissible belief sets B, such that:

1. the union of B in F covers all raw masks;
2. for every B in F and every permitted command T_(i,b), there exists C in F with T_(i,b)(B) subset C.

Then the minimum number N_dyn(k,J,s) of states of a deterministic source-labelled Moore transducer that admits a chosen initial state for each raw mask and outputs a feasible <=s-slack library **after every finite command word** is exactly

    N_dyn(k,J,s) = min_F |F|.

Proof (necessity): For an arbitrary valid deterministic transducer, associate to each reachable internal state t the set B_t of raw masks that can be represented at t along any permitted initialisation and command history. The union of B_t covers all inputs. Determinism forces T(B_t) subset B_(delta(t,T)). The one library emitted at t is feasible with slack s at every u in B_t, so the common-source theorem gives A_s(B_t). Identical belief sets can be deduplicated in the minimization only after constructing F; the number of distinct sets cannot exceed the number of transducer states.

Proof (sufficiency): Select any admissible F meeting coverage and successor conditions. Initialise a raw mask u in any member containing it. At belief state B emit the canonical library L(OR B), whose size and source feasibility satisfy all members by A_s(B). On command T, select a successor C containing T(B); then the concrete state remains represented. Fixed successor choices produce a deterministic transducer. QED.

The finite family formulation is a complete exact combinatorial kernel. It does not assert that membership-state minimization can be replaced by a naive partition or by scalar cost equivalence.

## Theorem D — Full named control: a sharp no-compression regime and explicit bounded-slack construction

When **all k coordinates are controllable**, then

    N_dyn(k,all,0)=N_dyn(k,all,1)=2^k.

For every integer 2<=s<=k-1,

    N_dyn(k,all,s) <= 2^(k-s+1),

and N_dyn(k,all,k)=1.

Proof of lower bound for s<=1: Take any two different raw masks and choose a coordinate i on which they differ. Apply a common Set word overwriting *all other* coordinates: set both neighbours of i to 1, and all remaining vertices to 0. The two resulting masks differ only at i. Changing that bit from 0 to 1 adds **exactly two** cyclic edges, including k=3 where the two neighbours are themselves adjacent. Their minimum common labelled library needs two more entries than the low mask's optimum. No <=1-slack output can serve both. Thus the two initial raw masks cannot share a deterministic state, and all 2^k initial masks are pairwise distinguishable. Tracking the entire mask gives the matching upper bound.

For 2<=s<=k-1, take a consecutive block T of s-1 vertices. Ignore its coordinates, remember exactly the other k-s+1 bits, and emit L(u OR 1_T), where all forgotten bits are forced unavailable. The number of cycle edges incident to a proper consecutive block of t vertices is t+1=s. Thus 0<=q(u OR 1_T)-q(u)<=s. Set commands on tracked vertices update those bits; commands on forgotten vertices leave the stored state unchanged. This yields a valid 2^(k-s+1)-state transducer with explicit source-labelled output. For s=k, the single L(1^k) output works. QED.

These bounds exhibit a strict difference between static source selection and transition-faithful source selection: static M_stat(k,1) can be far below 2^k, but full named control forbids any state compression at slack 1.

## Theorem E — Exact smallest dynamic witness at k=3, s=2

For the three-cycle with all three named Set operations and s=2,

    M_stat(3,2)=3,   N_dyn(3,all,2)=4.

The four-state construction from Theorem D remembers bits 0 and 2 and forgets bit 1. Its belief sets, encoded as bitsets over the eight raw masks 0,...,7, are 5, 80, 10, 160, corresponding to raw pairs {0,2},{4,6},{1,3},{5,7}. Each emits its canonical OR library.

For the matching lower bound, exhaustive enumeration visits all 2^8-1 nonempty raw belief sets and finds exactly 49 admissible at slack 2. It checks all choose(49,3) triples; 216 triples cover the eight raw masks, but **zero** also satisfy every named Set closure condition. A two-state transducer would have at most two distinct static outputs, whereas Theorem B requires at least three; therefore there are no transducers with fewer than four states. The standard-library checker independently verifies source availability and the four-state witness.

## Reproducibility and finite spectra

\`VERIFY_R5_SLACK_DYNAMIC.py\` is Python standard-library only. It tests the two sharp static constructions and their actual E0/E1/H0/H4 source coverage on every k=3,...,12 mask, yielding 33,661 successful witness/source checks, and completely enumerates the 3-cycle dynamic lower bound. Observed result: \`PASS_R5_SLACK_SOURCE_DYNAMIC\`.

\`VERIFY_R5_SLACK_STATIC_MILP.py\` constructs the exact binary set-cover matrix C_s(v) and calls SciPy/HiGHS integer programming with zero requested relative gap. The finite optima for k=3,...,8 and s=0,...,k are:

    k=3: [7,4,3,1]
    k=4: [11,7,4,3,1]
    k=5: [21,11,7,4,3,1]
    k=6: [39,21,10,7,4,3,1]
    k=7: [71,33,17,9,7,4,3,1]
    k=8: [131,59,25,16,9,6,4,3,1].

Each vector is indexed by increasing slack s. All solver instances returned status OPTIMAL and MIP gap zero (or within floating solver tolerance). These numbers are solver-checked finite results rather than independent universal proofs; the exact general theorems above use symbolic arguments. Evidence summary is in \`EXACT_R5_SLACK_SOURCE_EVIDENCE.json\`.

## Scope, provenance, and next mathematical question

The original frozen 954-event science pin, P000 six-dimensional spatial basis, temporal typing, original coordinate model and any BRC constraints remain unchanged. The cyclic graph and helper-label optimization are a declared auxiliary integer-indexed observer. Theorem C retains all actual source labels in every emitted library, and changes the *observer budget*: exact optimality was s=0, whereas this note explicitly permits s additional entries. Independent mathematical review: NOT_REVIEWED. Formal Task-ID, active CLAIM and protected Activity checkpoint are not asserted by this Draft science commit.

**Next:** Determine exact N_dyn(k,J,s) beyond the present sharp regimes, starting with k>=4, full named Set, slack 2 and the gap between the static k-1 slack dictionary of size 3 and the adaptive upper bound 4. Analyse whether every minimal belief family admits an economical structural representation without enumerating 2^(2^k) candidates.