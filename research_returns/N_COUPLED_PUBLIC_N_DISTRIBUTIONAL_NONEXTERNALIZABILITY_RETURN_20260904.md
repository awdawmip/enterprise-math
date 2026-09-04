# N-coupled public-N distributional nonexternalizability — Research Return

Researcher-ID: `EM-NCASDIST1-3F7A91`  
Task: `RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY`  
Publication: `TP2-5D9C21A7B40E683F1C52`  
Claim: `CLM-NCDIST-3F7A91C4E82D105B6A37`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / EFFECTIVE_PUBLIC_GENERATIVE_SEMANTICS_ARE_DISTRIBUTIONALLY_EXTERNALIZABLE`.

Hard-target disposition:

`EFFECTIVE_PUBLIC_EFFECTS_EXACTLY_EXTERNALIZED_FOR_G_EFFECT_DIST_EFF`.

Freeze the exact class `G_effect-dist^eff`: an oracle-free public program whose full operational semantics, transition interpreter and stochastic primitives are effective from the public specification and public input `N`, and whose terminal materialization is a finite explicit presentation. For probabilistic programs, almost-sure termination is sufficient. For nondeterministic programs, branch choices must be effective and finitely branching or computably enumerable.

Within this class, a positive distributionally nonexternalizable survivor is impossible. An external machine can interpret the same public program on an independent copy of the same public random source, producing exactly the same law of terminal explicit presentations. For effective nondeterminism, dovetailing the public branch tree enumerates exactly the reachable terminal presentation support.

This closes a strictly larger class than predecessor `G_effect-seed`: the seed space need not be finite, the execution need not have a bounded trace, and the branch compiler need not be given as one finite pushforward map. It is enough that the complete runtime is itself publicly and effectively executable.

No factoring or complexity lower bound, novelty claim, Working Truth, Foundation, L4 or canonical promotion is asserted.

## 2. Frozen class `G_effect-dist^eff`

A probabilistic member is a public oracle-free effective machine `P_N` with:

1. input only public `N` and public code/specification `P`;
2. a computable small-step transition interpreter;
3. stochastic primitives whose exact sampling algorithms are public and effective (equivalently, after inlining, a public random tape model such as independent fair bits);
4. no hidden `p/q`, CRT selector, factor-correlated environment state, secret implementation or noncomputable/physical oracle;
5. almost-sure termination;
6. a finite explicit terminal presentation `C`.

A nondeterministic member replaces the random tape by effective finitely branching or computably enumerable choices and has the same public-state and terminal-presentation requirements.

`externally sampleable` means: there is a public randomized algorithm taking only `(P,N)` whose terminal presentation has exactly the runtime presentation law. `support enumerable` means: there is a public algorithm enumerating every reachable terminal presentation and no unreachable one.

Machine-readable contract:

`research_artifacts/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY/effect_dist_public_emulator_contract.json`.

## 3. Theorem A — public emulator / exact distributional externalization

Let `P_N` be a probabilistic `G_effect-dist^eff` program. Then there exists an external public sampler `Ext(P,N)` with exactly the same terminal-presentation distribution as the runtime effect.

### Proof

Inline every public effective stochastic primitive into its public sampling algorithm, leaving a deterministic public interpreter driven by a random tape `rho`. Let

`F(P,N,rho)`

be the terminal presentation when the run halts. The runtime draws `rho` from the declared public tape law and evaluates this interpreter while withholding the realized tape and internal branch from the pre-readout transcript.

Define `Ext(P,N)` to run the same public interpreter on an independent tape `rho'` with the same public law and return the explicit terminal presentation. Since `rho` and `rho'` have the same law and the interpreter is the same deterministic measurable/effective map, `F(P,N,rho)` and `F(P,N,rho')` have exactly the same pushforward law.

Equivalently, one may couple the two executions by taking `rho'=rho`; then their states and outputs agree pathwise at every step. Hiding the runtime's realized tape destroys recovery of the actual branch, but does not destroy the public generative law.

Almost-sure termination is enough: the external simulation halts with exactly the same probability one. No finite seed space or bounded execution depth is needed. QED.

## 4. Theorem B — effective support enumeration

For a probabilistic fair-bit presentation of `P_N`, the support of its terminal-presentation law is computably enumerable.

Enumerate all finite bit strings `u`. Simulate `P_N` using `u` as a prescribed random prefix, and output a terminal presentation whenever the machine halts before requesting a bit beyond `u`. Every emitted presentation is reachable. Conversely, every halting run uses only finitely many random bits before termination, so its terminal presentation is discovered when its consumed prefix is enumerated. Therefore the reachable support is c.e.

For effective finitely branching nondeterminism, enumerate finite branch words and perform the same simulation. For computably enumerable branching, dovetail the branch enumerators and the corresponding finite executions. Hence pure effective nondeterminism cannot obtain support nonenumerability either.

This theorem does not say that the exact point probabilities of an arbitrary almost-surely-halting program are uniformly computable. The task target needs an external sampler or enumerator; the exact sampler is supplied by Theorem A and support enumeration by this theorem.

## 5. Unbounded almost-surely-halting boundary witness

Consider a public fair-bit effect that counts consecutive `1` bits until the first `0`, then outputs presentation label `C_even` or `C_odd` according to the parity of the count. The run is unbounded but halts almost surely.

Exactly,

`Pr(C_even) = 1/2 + 1/8 + 1/32 + ... = 2/3`,

`Pr(C_odd)  = 1/4 + 1/16 + 1/64 + ... = 1/3`.

The external universal interpreter samples the same fair bits and therefore exactly reproduces this law. This witnesses that the theorem genuinely extends beyond predecessor finite-seed externalization.

## 6. Corollary — the item-5/item-6 tension is exact

The successor task requires a positive survivor to be simultaneously:

- operationally executable from its fully public specification without oracle/secrecy; and
- not externally sampleable/enumerable from that public specification.

Within `G_effect-dist^eff`, these requirements contradict Theorems A and B. Therefore any alleged survivor must obtain an operational resource not represented by the public effective semantics. Concretely, it must rely on at least one excluded ingredient such as:

- a noncomputable/physical oracle or nonsimulable external source;
- secret implementation/state not recoverable from the public specification;
- hidden factors, CRT side information or factor-correlated environment state;
- a change of externalization rules that forbids the external machine from using a resource the runtime is allowed to use.

These are authority/resource escapes, not consequences of branch opacity. The last case is merely an asymmetric model definition and is not a public-N effect capability.

## 7. Readout preservation

Let `R(N,C)` be any frozen public deterministic terminal materialization/readout on the explicit presentation. Applying the same `R` to identically distributed presentations preserves the output law. Thus if a `G_effect-dist^eff` runtime has some proper-gcd/factor success distribution after materialization, the external simulator has exactly the same distribution after the same readout.

This is a semantic compilation result only. It does not prove the external simulation efficient relative to any complexity model and does not imply a factoring lower bound.

## 8. Mechanism firewall

No positive factoring candidate is introduced. The theorem uses no order/smoothness, collision/cycle, square-relation, p-adic/Hensel, hidden-factor or CRT mechanism. Direct randomized presentation/nonunit search remains covered as a special case of externalized public random generation.

A future positive survivor, if one is admitted under a broader model, must first identify the extra operational resource and pass the taskbook firewall. Calling that resource `randomness`, `environment` or `effect` does not avoid the theorem when its sampling/transition semantics remain public and effective.

## 9. Exact checker

Checker:

`research_checks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_CHECK_20260904.py`.

Exact replay result:

`PASS G_EFFECT_DIST_PUBLIC_EMULATOR {"branch_opacity_nontrivial": true, "calculus": "G_effect-dist^eff", "finite_rational_specs": 128, "finite_terminal_paths": 7680, "law_mismatches": 0, "status": "PASS", "support_mismatches": 0, "unbounded_as_halt_example": {"even": "2/3", "odd": "1/3"}}`

The checker compares two independent exact constructions of the output law for 128 finite public rational branching systems: state-mass dynamic pushforward versus complete path enumeration. Across 7,680 terminal paths there are zero law or support mismatches. It separately checks the exact `2/3,1/3` unbounded almost-surely-halting fair-bit example and confirms nontrivial hidden branch opacity.

These checks guard the implementation and boundary examples. Theorems A and B are symbolic computability arguments, not extrapolations from finite regression.

## 10. Closed and open boundary

Closed for this task:

`FULLY_PUBLIC_EFFECTIVE_GENERATIVE_SEMANTICS + ORACLE_FREE_EXECUTABILITY => EXTERNAL_SAMPLER`,

and

`EFFECTIVE_BRANCHING => C.E._TERMINAL_PRESENTATION_SUPPORT`.

Hence `PUBLIC_EXECUTABILITY + DISTRIBUTIONAL_NONEXTERNALIZABILITY` has no survivor inside `G_effect-dist^eff`.

Open only outside this frozen class: models granting the runtime an operational resource that is not effectively available from the public specification. Such a model must be separately justified and must not smuggle in secrecy, hidden factors, factor-correlated state, noncomputability/physical oracle authority, or a reviewed classical mechanism.

Recommended control action: `DRIVER_REVIEW`. If accepted, freeze this stronger semantic no-go and require any continuation to name and justify a genuinely additional public operational resource rather than republish hidden-branch or distributional opacity.
