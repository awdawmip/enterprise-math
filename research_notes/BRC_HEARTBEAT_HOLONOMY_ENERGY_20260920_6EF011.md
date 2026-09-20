# Heartbeat residuals: native-loop holonomy, energy, and a preparation-dependent temperature floor

Event-ID: brc-heartbeat-holonomy-energy-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author exact derivations and finite checks, no independent review, Lean, Working Truth or Foundation admission.
Source read: enterprise-math@f481e0c6b184769d1d0c6e5ae80213ba8ec48af9; cumulative local parent abd195490bfb653726048bcb74bad7a972a276a9.

## What was built, and what was not assumed

Retained the active residual-first method constraint. The new bridge does not require residuals or control inaccuracies to vanish. On a legal12-edge native loop (+e1 through+e6, then-e1 through-e6), encode the retained sixth-difference residual as a total oriented link phase. The local energy is the phase-twisted nearest-neighbor Dirichlet form. This is an explicit candidate coupling with supplied positive energy scale kappa, NOT a derivation of a unique physical Hamiltonian, control apparatus or thermal environment from P000. The loop uses only raw X6 native-axis steps; time and Hilbert-space site labels do not add spatial axes. No primitive mechanical force-balance claim is made.

Reuse E(t)=a^t-sum_(j<6)binom(t,j)(a-1)^j and Delta^6 E(t)=(a-1)^6 a^t. For unit a modulo N and character s, phi_t=[s(a-1)^6 a^t mod N]/N has constant reduced denominator q=N/gcd(s(a-1)^6,N). The unchanged stage16 certificate verifies this with seven modular-power queries, not a trajectory table or an order input.

## New observer and exact conditional statements

For normalized v on L12 sites, H has energy kappa sum_j |v_(j+1)-exp(2pi i alpha_j)v_j|^2, with sum alpha_j=phi modulo1. Site gauge changes alter individual links but not this loop phase. Every connection is gauge-equivalent to uniform links phi/L. Changing a connection without also transforming the state is not this equivalence.

The spectrum is lambda_k=2kappa[1-cos(2pi(k-phi)/L)]. Writing delta=dist(phi,Z),
E0=4kappa sin^2(pi delta/L). For q>1, E0>=16kappa/(L^2 q^2)>0 at every heartbeat. If actual loop phase is within circular error e of the retained value, E0>=16kappa max(0,delta-e)^2/L^2. Nonzero error is permitted. An inconclusive bound is not interpreted as zero energy or rejection of the object. For example, centre1/4 and error1/100 still certify E0>=4kappa/625.

The excitation gap above the whole ground subspace satisfies gap>=16kappa/(L^2 q), including the separately treated half-flux degeneracy. At delta<1/2 the exact gap is4kappa sin(pi/L)sin(pi(1-2delta)/L). At delta1/2 there are two ground modes, and the next gap is4kappa sin(2pi/L)sin(pi/L). Exact rational flux decides degeneracy; close levels are not numerically rounded equal.

A mode has uniform density but circulating bond current J_k=2kappa sin(2pi(k-phi)/L)/(L hbar). At half flux the two ground currents are opposite. Hence a stationary density, nonzero circulation, nonzero baseline energy, excitation above ground, and temperature are distinct. Formal Gibbs zero-temperature limits remain valid ground projectors of this finite Hamiltonian. Positive E0 alone does not prohibit them, because shifting H by E0I changes neither Gibbs probabilities nor current. Physical finite preparation is the separate theorem to prove; the strong absolute-zero target is retained, not assumed or abandoned.

For a concrete residual-phase wave psi_j=exp(2pi i s E(t+j)/N)/sqrt(L), take the explicitly parameterized mixed state rho_eta=(1-eta)|psi><psi|+eta I/L. eta is not inferred from an arithmetic remainder. Spectral ordering gives exact maximum system-unitary work (1-eta)(<psi,Hpsi>-E0) and passive energy above ground eta(2kappa-E0). The latter is not automatically thermal energy: the passive state is generally not Gibbs. This bridge separates recoverable coherence from the mixed tail instead of calling all motion heat. If phi is externally changed at fixed rho, Tr[rho(H_new-H_old)] is control work, not spontaneous heat.

## Preparation and an explicit imperfect cooling process

Reuse the stage16 full-rank resource bound, unchanged. A target of dimension L, ground degeneracy g and initial least eigenvalue mu>0, with independent finite full-rank ancillas, has p_exc>=(L-g)mu exp(-B), B=-sum ln(d_i mu_i), after any joint unitary/discard operation. Pure resets, favorable postselection and uncounted pure/correlated resources are outside this premise.

For this actual energy observer, E-E0>=gap*(L-g)mu exp(-B). If B<=Bmax and the FINAL state is Gibbs, then

 T>=gap/[k_B(Bmax-ln(g mu))]>=16kappa/[L^2 q k_B(Bmax-ln(g mu))]>0.

This is a conditional finite-resource temperature floor with an explicit Hamiltonian/gap, not universal zero-temperature nonexistence. It does not assign a temperature to arbitrary nonthermal states or infer all physical preparations from X6 geometry. kappa, allowed controls and available resource states still need independent physical justification.

Implemented a partial-SWAP process between target and fresh stationary bath copies with the same H. U=cI-i sqrt(1-c^2)SWAP conserves total bare energy. Exact partial trace yields rho'=c^2rho+(1-c^2)tau+i c sqrt(1-c^2)[rho,tau]. If [tau,H]=0, E'=c^2E+(1-c^2)E_tau even for coherent rho. For commuting states and irregular couplings, rho_k=tau+product(c_j^2)(rho_0-tau). Declared coupling intervals are propagated without assuming their errors independent. No remainder is cleared.

The exact12-level example rho_0=I/12, tau=diag(2/3,1/33,...,1/33), c3/5 gives p_exc(k)=1/3+(7/12)(9/25)^k. This stationary tau is NOT a Gibbs state of the nondegenerate cycle. At1024 copies the retained initial factor is4.5056845799185762853e-455, stored as a positive exact fraction even when a decimal display prints p_exc as1/3. Three-run median recurrence computation0.781454ms is not physical cooling time. The model consumes1024 fresh copies and, at interaction norm bound G, its specified sequence takes at least1024 hbar acos(3/5)/G. It is not an unrestricted-unitary optimum or a logarithmic physical-resource algorithm.

## Executed numerical results

Frozen plan51 records=15 residual-bridge runs+24 Gibbs-law runs+12 exchange runs; three repetitions each; no CPU pinning. All candidate arithmetic uses integer/Fraction and inherited directed intervals. Reference numpy/mpmath/sympy calculations are separate and do not feed candidates.

Hard arithmetic input N18446743979220271189,a2,t0, same underlying sixth source1:
- s1: E0/kappa8.0567113452674568e-40; gap/kappa0.2679491924311227.
- s=(N-1)/2: E0/kappa0.06814834742186343; gap/kappa1.4692818989612168e-20.
- s=(N-1)/4: E0/kappa0.01711027725237918; gap/kappa0.1351306577250473.
Larger phase contrast near half flux raises baseline energy while nearly degenerating the two lowest modes. This is a structural sensitivity/gap tradeoff, not a failure to handle imperfect data. The exact-half case is kept separately.

A snapshot at t2^128+17 also succeeds (phi8833449548962669573/N). Residual-spectrum median times are0.132--0.212s after phase-context initialization; extra wave/work calculations0.265--0.348s. The initial context and all calls are charged separately in raw records. These are small12-state observer computations on a large arithmetic input, NOT large-system thermal simulations or new Shor samples.

Finite-Gibbs examples at phi1/4 have p_exc0.457437511606 at beta*kappa4 and0.104628850624 at beta*kappa16, each enclosed by integer endpoints. They use real Gibbs spectra, distinct from the rational stationary bath in the exchange example.

Checks passed:72 rotated native edges;1104 residual-holonomy identities;1044 spectral interval entries;100 independent gauge-conjugation checks;396 nonzero perturbation bounds;40 energy/ergotropy decompositions;133 exponential enclosures;240 Gibbs probabilities;72 exact exchange recurrences;12 rational coherent joint-unitary/energy identities;48 full-rank resource checks;5 stationary currents;192 irregular-coupling endpoint checks;7 input boundaries;integer-core AST. Independent-path replay checked180 recorded spectral entries,288 Gibbs weights,15 work decompositions and12 exact exchange rows. Same author, not independent researcher or Lean verification. One reference syntax defect and one unnormalized reference state were found/fixed before final tests; they are documented as implementation errors, not physical residuals.

## Reuse, evidence status and next problem

Reuse executed unchanged: stage16 residual phase and full-rank resource interfaces, stage15 residual core, stage14 native rotation vendor. P023 applies only to covariantly transformed gauge observations. Signed phases remain distinct from positive BRC weights. Prior art: magnetic graph Laplacians (Lange et al.2015, DOI10.1007/s00526-015-0935-x), ergotropy (Allahverdyan et al.2004), partial-SWAP homogenization (Ziman et al.quant-ph/0110164), finite-resource cooling (Ticozzi--Viola2014; Masanes--Oppenheim2017). No global novelty or new family admission is asserted.

Next: couple the residual source and its controller autonomously, with a specified energy-conserving preparation model and explicit accounting for correlation/purity supplied by the controller. The present externally prescribed connection is a valid tested bridge, but does not derive spontaneous Heartbeat heat production or exclude all formal ground states. Preserve nonzero residuals and their phase/gap tradeoffs rather than demanding perfect closure.

Full proofs, integer code, frozen plans, raw evidence and all inherited history are in the cumulative standalone Git bundle. It is not the entire Enterprise Math repository. Actual Drive upload/hash/readback will be recorded only after delivery. This text is a research checkpoint, not mathematical acceptance.
