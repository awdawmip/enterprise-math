# R059P First-Round Exact Validation Report

Researcher-ID: `EM-R059P-8A2C7D`  
Task: `RS-R059P-PATH-SPECTRUM-COUPLING-DYNAMIC-STEADY-STATE-VALIDATION`  
Taskbook source: `8f4e83ed6404bad6804e3d5f9f2f291c1ec42cf2`  
Lane: independent R059P; no R059L artifact was read or consumed.

## Primary disposition

`NEUTRAL_PATH_COUPLING_CYCLE_FOUND`

Supporting subdispositions:

- `AUTOMORPHISM_INVARIANT_PATH_SPECTRUM_DEGENERACY_PROVED`
- `SYMMETRIC_STRICT_PATH_RUBBER_BANDS_INSUFFICIENT_FOR_PERSISTENT_ACTIVITY`
- `MACRO_STEADY_DEGENERACY_PROVED`
- `INTRINSIC_ACTIVITY_SELECTION_RULE_OPEN`
- `QUANTUM_BRIDGE_OPEN`

## Stage 0

The Stage-0 semantic freeze passed before T1/T2/T3 computation. The deterministic checker rejects all required forbidden mutations.

| Artifact | SHA256 |
|---|---|
| `R059P_PATH_SPECTRUM_PROTOCOL.json` | `fa143d43d0a1c2ef3f9b2bf89e041ed456161e9eb5d7d2c7c535ed1fd1658fe8` |
| `R059P_PAIR_COUPLING_MODEL_REGISTRY.json` | `0188c288e9e059ff811289f5e82a17ac9cb84ef45769d1cc52360330b76a6394` |
| `R059P_DYNAMIC_UPDATE_MODEL_REGISTRY.json` | `ea3499017c94424c0e11c51fb35df8e1d38c8686539174870c47332246a64d4b` |
| `R059P_SEMANTIC_FIREWALL.json` | `e1ba0c53b865ef15cc69651941c4f26d76a35f357a66c3b95812bd58853b3d8d` |
| `R059P_COMPUTATION_REGISTRY.json` | `8fb63848a797d9823a9ef7257d70a337dcf128b9e118d1afb875e4ef210cd501` |
| `check_r059p_stage0.py` | `df138d279719519e215ac6222a0675e9711548c8d54d9812be14592bea472511` |
| `R059P_STAGE0_CHECKER_OUTPUT.json` | `b12d6c403995add1c958c4064ab9682039fd0672adf72f14af3f4b41d4248fbb` |

Checker result: `PASS`.

Rejected mutation classes:

1. PATH_COUNT relabeled as geometric length;
2. shortest-path-only spectrum;
3. Euclidean distance used as pair-coupling premise;
4. atom/physical energy promoted to N0;
5. R059L artifact consumption;
6. zero-point motion assumed explained;
7. cycle asserted under unchanged finite strict-descent semantics.

## T1 — exact relational automorphism invariance

Let `Gamma_n(a,b)` be the set of all admissible adjacency walks
`(x_0,...,x_n)` from `a` to `b` with exactly `n` transition events.
For any adjacency-preserving bijection `phi`, apply `phi` coordinatewise:

`(x_0,...,x_n) -> (phi(x_0),...,phi(x_n))`.

Adjacency preservation makes this a walk from `phi(a)` to `phi(b)` with the same transition count. The coordinatewise action of `phi^-1` is its inverse. Therefore this is a bijection of walk sets and

`W_n(phi(a),phi(b)) = W_n(a,b)`

for every finite `n`.

Hence each frozen finite path spectrum is invariant, and any frozen pair readout depending only on that spectrum is invariant under simultaneous carrier automorphism of all tagged sites. No geometric meaning is attached to the automorphism.

Disposition:

`AUTOMORPHISM_INVARIANT_PATH_SPECTRUM_DEGENERACY_PROVED`.

## T2 — strict scalar descent cannot sustain microscopic activity

For finite `Omega`, if every accepted update satisfies

`E(S') < E(S)`,

then no state can repeat on an accepted trajectory. A repeated state would imply `E(S) < E(S)` after chaining strict inequalities. Therefore an accepted trajectory contains at most `|Omega|` distinct states, hence at most `|Omega|-1` accepted transitions. Every maximal accepted trajectory ends at a sink of the strict-descent transition graph.

For a unilateral move of marker `i` with

`E = sum_(p<q) e_pq`,
`U_i = sum_(j!=i) e_ij`,

and all nonincident pair terms unchanged,

`E(S')-E(S) = U_i(S')-U_i(S)`.

Thus strict local best response is exact global potential descent.

Disposition:

`SYMMETRIC_STRICT_PATH_RUBBER_BANDS_INSUFFICIENT_FOR_PERSISTENT_ACTIVITY`.

## T3 — exact neutral dynamic steady-state orbit

The tiny carrier uses four packet labels with only the declared relation

`i ~ j iff j = i +/- 1 mod 4`.

The labels are implementation labels only; no square, distance, direction, angle, or embedding is claimed.

Two tagged markers `A,B` occupy distinct packets. An elementary update moves exactly one marker through one declared adjacency to an unoccupied packet.

### Automorphism degeneracy

The adjacency automorphism `phi(i)=i+1 mod 4` gives the configuration orbit

`(0,1) -> (1,2) -> (2,3) -> (3,0) -> (0,1)`.

By T1, all finite pair path spectra agree along this orbit. However, each collective `phi` step moves both tagged markers and is not an elementary one-marker update. This explicitly separates degeneracy from a dynamics.

### Strict toy mismatch

Use the frozen C0 window `n=1,2` with preferred spectrum `(1,0)`:

`e_strict = |W_1-1| + |W_2|`.

Among the 12 ordered distinct-marker states:

- 8 states have `E=0`;
- 4 states have `E=3`;
- the strict accepted graph has 16 directed edges;
- all strict edges go from `E=3` to `E=0`;
- there are 8 sinks;
- there is no directed cycle;
- the longest accepted trajectory in this toy has one step.

### Neutral plateau witness

Use the frozen C1 toy readout

`e_plateau = 2 W_1 + W_2`.

For every ordered distinct-marker state of this carrier, the pair spectrum is one of:

- `(W_1,W_2)=(1,0)`, giving `e=2`;
- `(W_1,W_2)=(0,2)`, giving `e=2`.

Thus all 12 states lie on one exact `E=2` plateau.

A minimal elementary equal-E cycle is

`(0,1) -> (0,2) -> (0,1)`.

A stronger witness avoiding consecutive same-marker reversal is

`(0,1) --A--> (3,1) --B--> (3,2) --A--> (0,2) --B--> (0,1)`.

Every step is one legal adjacency transition of one marker and every state has exactly the same macro readout `E=2`. The pair spectrum itself alternates between `(1,0)` and `(0,2)`, so this is an equal-macro-readout orbit, not a stronger equal-spectrum orbit.

The plateau weights were deliberately chosen to equalize the two spectrum classes. Therefore this is an exact existence theorem about admissible higher-level semantics, not evidence that nature uses these weights.

## Stage-B mechanism classification

### Neutral plateau moves

Exact cycle existence is proved. Allowing `E(S')=E(S)` removes the strict-potential no-cycle obstruction. Persistent motion still requires an N1 transition policy that actually continues selecting neutral moves.

A deterministic state-only policy can be defined on the witnessed cycle, so history memory is not mathematically necessary for persistence in this toy. However, no intrinsic or physically calibrated neutral selector has been derived.

### Path-history memory

Not required by the minimal witness. It remains a separate candidate because a state space `(configuration, memory)` contains information not ordered by the configuration-only scalar `E(S)`; therefore T2 does not automatically apply to the extended dynamics.

### Nonreciprocal local coupling

Not required and not tested as a physical mechanism. Once pair preferences are nonreciprocal, the exact unilateral global-potential identity need not exist. This is a separate higher-level model, not default atomic attraction.

### Stochastic or external drive

Can select neutral moves or permit non-descent transitions, but it is an explicitly added N1 mechanism and is downstream calibration, not an N0 explanation.

### Quantum calibration

Open. The first-round model has no mass/isotope parameter, quantum state, commutation structure, or calibrated zero-point mechanism.

## External calibration constraints

Only after the native exact results were frozen, the following established external observations were used as qualitative constraints:

- Duan et al., *Physical Review Letters* **135**, 196901 (2025), report cryogenic zero-point polar-optical-phonon motion in CsPbI3 nanocrystals.
- Prisk et al., *Physical Review B* **107**, 094511 (2023), use inelastic neutron scattering on solid hydrogen and identify quantum contributions to displacement/kinetic energy.
- Wyart, Liang, Kabla, Mahadevan, *Physical Review Letters* **101**, 215501 (2008), show strong dependence of elastic behavior on network coordination near rigidity onset.
- Bergman et al., *Nature Physics* **3**, 487–491 (2007), analyze a frustration-induced highly degenerate ground-state manifold and fluctuating spin-liquid regime.
- *Physical Review Letters* **134**, 096702 (2025) reports low-temperature spin-ice noise, relaxation pathways, and aging behavior.

These observations are constraints/analogies only. None was used in T1/T2/T3.

Calibration answers:

1. Persistent activity without thermal drive? **Strict M0: no. Neutral M1 + explicit transition policy: yes mathematically; physical driver open.**
2. What stores persistence? **In the minimal neutral witness, the transition policy, not `E`; a history model would instead store it in explicit memory.**
3. Does activity vanish under strict potential descent? **Yes, exactly, on finite state space.**
4. Collective low-strain modes? **Only degeneracy/orbit evidence; a selective nontrivial mode family is not derived.**
5. Nontrivial mode spectrum without Euclidean displacement? **Open.**
6. Future mass/isotope parameter? **None identified.**

## First-round conclusion

The original “many path-count rubber bands” idea separates into two mathematically different statements.

First, finite path-spectrum coupling has exact relational degeneracies under carrier automorphisms. This supports the possibility of macroscopically unchanged coupling readouts across distinct configurations.

Second, degeneracy alone does not create activity. If every move must strictly decrease one finite state-only symmetric scalar readout, activity stops. The smallest exact change that reopens persistent dynamics in the first toy model is to admit neutral plateau moves. Once equality moves are allowed, exact elementary cycles exist.

Therefore the first-round result is not “path coupling explains zero-point motion.” It is:

**strict symmetric state-only path coupling is static-only; neutral coupling semantics can support exact persistent cycles, but the intrinsic physical rule selecting those cycles remains unresolved.**
