# Heartbeat: autonomous residual controller, backaction and retained tiny correlations

Event-ID: brc-heartbeat-autonomous-backaction-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author derivations and checks, no independent review, Lean, Working Truth or Foundation admission.
Source read: enterprise-math@d492492af4b7559019341e7aaef90587eb5701d1. Standalone parent87be40ef0228090edf435959d39eec71987ea114.

## What changed

The phase source is no longer changed by a cost-free prescribed external clock during evolution. A finite internal controller configuration c selects residual phase phi_c=s(a-1)^6 a^(n0+c)/N modulo1 on the unchanged native12-edge loop. The joint, time-independent Hamiltonian is H=H_C tensor I+sum_c |c><c| tensor H_S(phi_c), with H_C a J-weighted path Laplacian and H_S the inherited kappa-weighted phase-twisted loop energy. Default spatial phase sits on one seam link. All source coefficients and initial states are explicitly prepared resources. This is a candidate physical coupling, not a unique Hamiltonian or pure-state preparation derived from P000. Controller configurations, integer source index and physical evolution time are distinct; none adds a native spatial axis.

After preparation, total energy is conserved. The conditional ring-plus-coupling energy V changes through (i/hbar)[H_C,V], with exactly opposite change in H_C. This is not automatically a target-only bare energy or heat. A finite controller may spread, reverse or recur; it is not an indefinitely reliable one-way tick machine.

## Exact retained relationship: a seventh residual controls the backaction

Spatial gauge equalization cannot erase the controller links. Transforming seam links to uniform phi_c/12 introduces controller-link phases j(phi_(c+1)-phi_c)/12. Deleting them changes the joint Hamiltonian. The gauge-invariant mixed plaquette at the seam is phi_c-phi_(c+1)=-s(a-1)^7 a^(n0+c)/N modulo1. Its reduced order q7=N/gcd(s(a-1)^7,N) is fixed. q7>1 certifies nonzero plaquette holonomy at every source index.

For two configurations the energy-current operator has norm
  ||(i/hbar)[H_C,V]||=2J kappa |sin(pi(phi_1-phi_0))|/hbar.
This is a capacity, not nonzero current in every state. If circular jump distance is d and phase errors total at most e, the norm is at least4J kappa max(0,d-e)/hbar. Nonzero uncertainty is allowed rather than set to zero.

A counterexample separates residual persistence from this particular coupling: N128,a3,s1 has sixth source64, constant flux1/2 and q7=1. Spatial holonomy is nonzero, but the controller and spatial Hamiltonians separate. Its product initial state generates no entanglement. The implementation's tiny nonzero centre lies inside its error interval and is not promoted to physics.

For the distinct uniform-spatial/zero-controller-link model, each spatial Fourier mode reduces the two-controller problem to [[e0+J,-J],[-J,e1+J]]. With d=(e1-e0)/2, the maximum transfer is J^2/(J^2+d^2); detuning leaves a minimum missed-tick probability d^2/(J^2+d^2). Exact energy transfer is Delta E_V=(e1-e0)p, Delta E_C=-Delta E_V. This model-specific formula does not apply to the seam model after dropping its induced gauge links, and is not a universal clock limitation.

## Actual tiny effect, not decimal disappearance

At N18446743979220271189,a2,n0=0,two controller configurations,kappa1,J1/4, initial |c0,site0>, evolve autonomously to tau2 (hbar1). The weak character s1 yields conditional energy gain7.21909042893786576e-21, paid by the controller. The final controller linear entropy is
  2.03933494068371514989640932572828e-39.
Its outward certified interval is approximately[2.0393348997663067e-39,2.0393349816011233e-39], strictly above zero. The global state/measurement numerical error bound is about1.023e-47. An independently written100-decimal-digit matrix exponential confirms the tiny correlation and energy transfer. This linear entropy measures entanglement of the pure joint packet, not temperature, and the pure initial packet is an explicitly supplied resource.

For s=(N-1)/4, the same24-state joint model gives conditional energy gain0.0204426205269 and linear entropy0.0341359090642; for s=(N-1)/2, gain3.35658740536e-21 but linear entropy0.0644199166401. Energy transfer and correlation strength are not interchangeable. These are small joint models parameterized by a large arithmetic input, not a simulated64-bit factorization or new Shor samples.

## Finite windows keep, rather than deny, the omitted paths

A formal unwrapped controller line has norm bound h=4(kappa+J). Restrict to [-R,R] while retaining the boundary diagonal2J. Starting at the centre, powers agree through orderR, giving vector error at most2 sum_(n>R)(h|tau|)^n/n!. The code evaluates the rational geometric bound on that factorial tail. The corresponding probability-law TV is no greater than the vector bound, capped at1. An inconclusive certificate is not interpreted as zero outside amplitude.

For R24,tau1,kappa1,J1/4, this boundary TV bound is about4.76e-8. A49-configuration,588-amplitude run around source index2^128+17 was executed without storing its previous trajectory or knowing its period. The formal infinite controller is a comparison model, not a free physical resource. This is a local-duration approximation, not cheap evolution to arbitrary physical time.

Production propagation uses integer/Fraction Taylor terms, inherited directed roots and a retained Hamiltonian-rounding/Duhamel residual. Complex matrix entries are forced Hermitian. Rounding, factorial tails and phase error are accumulated, then normalization is charged. The saved total-energy drift is bounded rather than assumed exactly zero in rounded arithmetic. Work is proportional to the finite graph size, Taylor degree and integer precision; no exponential path list is constructed for this local model.

## Controller resources and the continuing zero-temperature objective

For a finite initial JOINT state Omega_SC>=mu_joint I with mu_joint>0, any joint unitary, autonomous or not, obeys rho_S>=dC mu_joint I. Thus p_exc>=(dS-g)dC mu_joint. Full-rank marginals alone are not enough; an initially pure entangled resource is a boundary witness. A verified comparison Omega_SC>=xi rho_S tensor sigma_C permits the explicit floor xi mu_S mu_C and charges initial correlations through -ln xi.

For the declared correlated preparation (1-eta)|c0,j0><c0,j0|+eta I/(dC*dS), the entire positive mixed tail is unchanged by all joint unitaries, and p_exc>=eta(dS-g)/dS. eta is NOT inferred from arithmetic residuals or numerical error. If the final marginal is Gibbs for a specified fixed target Hamiltonian of excitation gapDelta, then T>=Delta/[kB ln(dS/(g eta))]. The generic evolving marginal is not Gibbs. No assumption is made that all physical preparations have a uniformly positive eta; deriving the admissible preparation class remains part of the strong zero-temperature goal.

Joint entropy conservation also gives Delta S_S+Delta S_C=I_final-I_initial. From initially independent resources, lowering target entropy requires a compensating controller entropy increase. Returning the controller marginal exactly forbids target entropy reduction; an imperfect return at trace distance e<=1-1/dC bounds the reduction by h2(e)+e ln(dC-1). This uses the standard Audenaert bound, not a new entropy theorem. It allows nonzero disturbance, charges it, and does not confuse entropy purification with all forms of energy cooling. Baths, reset devices and initial correlations cannot be omitted from this ledger.

## Executed checks and timings

Passed5856 exact seventh-residual identities,1952 denominator checks,60 exact gauge-plaquette checks,4 full gauge-conjugation matrices,3 wrong-controller-link witnesses,24 full propagation references and certified energy drifts,27 analytic two-level maxima and energy balances,18 joint-tail floors,36 exact projector sums,4 finite-window comparisons and24 entropy balance checks, plus integer-core and boundary tests. Float references have explicit tolerances; the tiny case is additionally checked at100 digits. Same author, not independent review or formal proof verification.

Frozen selected-development plan:6 cases,3 repeats each,18 complete records, no CPU pinning. Total median times include phase initialization, profile/graph construction and propagation: small N23/M3 0.419356645s; weak hard/M2 1.389415917s; quarter-character hard/M2 0.432802064s; half-character hard/M2 0.431533281s; static nonzero/M3 0.415891962s;49-configuration large-index window0.545573625s. These are computational verification times, not physical clock speeds. A decimal serialization limit affected one initially unrecorded row; the first3 completed rows were preserved and only missing rows resumed. All18 raw energy records and6 medians were replayed without replacing timing evidence.

## Scope, reuse and next

Unchanged reuse: stage17 ResidualEnergyBridge/native_loop, stage16 residual certificate and their directed integer arithmetic. BRC retains phase, source identity, controller links, energy ports and boundary residuals; P023 gauge equivalence requires transforming the state and all affected links. The residual-first constraint and P000 are unchanged. Classical context includes Woods-Silva-Oppenheim arXiv1607.04591; Woods-Horodecki arXiv1912.05562/PRX13,011016; Malabarba-Short-Kammerlander arXiv1412.1338; Ticozzi-Viola Sci Rep4,5192; Audenaert quant-ph/0610146. No global novelty or universal speedup is asserted.

Next: an explicit multi-tick/open-system limit with reset, bath, correlation and preparation budgets. Derive rather than assume which native preparations can provide a joint spectral floor, and separate coherent reversible backaction from irreversible heat. The current construction removes externally prescribed time dependence during evolution but does not derive self-created energy or forbid every formal ground state. Preserve both real tiny correlations and static-source counterexamples. Complete code/proofs/raw results are delivered in the cumulative standalone bundle, not the entire Enterprise Math repository; actual cloud/hash receipts follow publication.
