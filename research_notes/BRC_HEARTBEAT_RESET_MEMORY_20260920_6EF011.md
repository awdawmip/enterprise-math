# Heartbeat: reset memory, heat accounting and the weak-contact limit

Event-ID: brc-heartbeat-reset-memory-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author derivations/checks, no independent review, Lean, Working Truth or Foundation admission.
Source read: enterprise-math@cd55c04299c8626cbc8849f7daede529689ef2d6. Standalone parent761de5f1e48f1850aee1d4d37d4b20f43a394192.

## Exact correlation-preserving reset

The inherited24-state residual/controller Hamiltonian now evolves between explicit fresh thermal reset contacts. The heartbeat interval is autonomous, but the entire supply/switch schedule is staged and is NOT claimed autonomous. Preparation, bath supply and physical pulse timing remain resources. Native axes, P000 and the residual-first constraint are unchanged.

For a fresh bath state tau and W=cI-is SWAP_CB, c^2+s^2=1, the exact channel on the correlated CS state is

 Omega'=c^2 Omega+s^2 tau_C tensor Omega_S+i cs[Omega,tau_C tensor I].

For R=Omega-Omega_C tensor Omega_S, R'=c^2R+i cs[R,tau tensor I]. In the bath eigenbasis each block multiplies by c^2+i cs(lambda_j-lambda_i). If c!=0, a nonzero correlation cannot become exactly zero in one such contact. Its squared Frobenius norm contracts by at most c^2(c^2+s^2 Delta_tau^2); for c3/5,s4/5,e1/4 this is117/625. This is a channel-specific diagnostic, not entropy, temperature or monotonic decay during the intervening heartbeat. A full swap transfers the old C and its correlations into B rather than destroying global information.

An exact two-qubit witness has equal Gibbs marginals diag(3/4,1/4), but adding an admissible imaginary correlation in the01/10 block changes the next target probability by3/50 compared with the product of those same marginals. The product replacement is an incorrect proxy, not a free physical eraser.

## Small coherent terms change a many-contact limit

With c=cos(theta),s=sin(theta), the channel contains an O(theta) commutator and O(theta^2) mixing. For theta~sqrt(h), the former cannot be dropped as independent noise. In a covariant rotating frame exp(+i theta tau_C), the second-order generator is

 L(Omega)=tau_C tensor Omega_S-Omega+1/2[tau_C tensor I,[tau_C tensor I,Omega]].

The frame changes observables too; implementing a physical counterrotation requires resources. The full generator is the limit of CPTP channels, not a claim that the double commutator alone is a noise channel.

For even n, u=1/(2n), c=(1-u^2)/(1+u^2), s=2u/(1+u^2), k=n^2 and bath spectral difference1/2, the raw coefficient is z=(c^2-i cs/2)^k. The exact rational rotating-frame coefficient z(c+i s)^(k/2) tends to exp(-7/8), whereas deleting the commutator gives exp(-1). The ratio tends to exp(1/8); with initial coherence1/2 the limiting trace-distance discrepancy is about0.0244913. The uncentered phase does not converge. All five predeclared n4,8,16,32,64 cases were computed using integer powers and independently checked at60 digits. This is a specified contact-channel limit, not a universal physical law inferred from Heartbeat geometry.

## Energy and entropy ledger

Let H_on=H_C+V, H_ref=H_S(phi0), K=V-I_C tensor H_ref. Disconnect K for the bare-energy-conserving reset, then reconnect it. For heat Q_B entering the fresh Gibbs bath, the exact switch work is W_switch=Tr[V(Omega'-Omega)], and the cycle obeys Delta E_on=W_switch-Q_B. The switch is not free merely because the local bath contact conserves C+B bare energy.

The exact enlarged-system Landauer identity is

 beta Q_B=S(CS)-S(CS)'+I(CS:B)'+D(B'||tau_B).

Its expansion retains I(C:S)'-I(C:S). The positive corrections are not discarded. With fresh independent baths that never return, this identity telescopes across contacts without storing all bath histories; a returning bath must reenter the retained state. This observer-scoped trace is different from replacing current CS correlations by zero.

For the large arithmetic input N18446743979220271189,a2,quarter character,12 contacts and initial(15/16)|00><00|+I/384, the total bath heat is0.207260534290, switching work0.062826337261, and joint energy change-0.144434197029. The computed heartbeat energy drift is retained inside its bound. These are24-state model computations, not a physical experiment, large thermal simulation or Shor speedup.

## Tiny memory affects a subsequent observation

After12 quarter-character cycles, dropping CS correlations changes the next target-site distribution by TV0.00799752432102. For weak character1, pure initial|00> and4 contacts, squared Frobenius correlation is2.25560511725407611759e-40 and the next-site TV discrepancy is3.54980030300853915490e-40. Their respective error margins are24*4.89381709527675e-48 and2.446908547638375e-47, both small enough to certify strict positivity. An independently implemented100-digit matrix exponential and Kraus reset confirm these values and switch work2.07414808790099655e-20. The pure initial preparation is explicit and is not a full-rank cooling example.

Static nonzero source N128,a3,s1 remains separable in the ideal model. Its small numerical centre lies inside the error bound and is not promoted to physics. Full reset gives exact zero retained CS correlation, with the old correlation moved to B.

## Positive tail and costed implementation

For physical Omega>=mu I, a reset gives mu'>=mu gamma, gamma=c^2+d_C s^2 lambda_min(tau). Hence mu_k>=mu_0 product gamma_j and p_exc>=(d_S-g)d_C mu_k. Here gamma=17/25 for the partial contact. Nonzero correlated uncertainty in coupling strengths is handled by deterministic endpoint products. This is a conditional preparation floor; no universal positive mu_0, finite total budget or temperature of an arbitrary non-Gibbs state is inferred.

Production uses exact common-denominator integer density matrices and exact CPTP resets. Inherited certified propagator columns bound an operator defect delta; normalized propagation has trace-distance defect at most delta(2+delta), accumulated over all uses. An explicit adapter replaces known zero-phase controller links by their exact values before unchanged stage18 propagation. An initial mismatch between rounded and exact controller energy conventions was fixed, not called a physical residual. Entropy checks use separate float references with2e-12 tolerance; they are not directed entropy certificates.

The retained matrix is24x24, not24*2^k bath amplitudes. Matrix arithmetic is O(k*d^3) with growing integer bit length, not constant-bit work. Frozen selected-development plan:6 cases*3 repeats=18 records,192 contact cycles, plus5 weak-limit runs. Median total seconds, including compilation, cycles and next-memory comparison: small partial4.621634015; small full3.740156966; small no reset4.559899606; large quarter4.631452391; large weak2.913925830; static3.684159654. Final numerator sizes2577--5438 bits. No CPU pinning; completed JSONL rows survived timeouts and only missing rows resumed.

Checks passed:576 exact dilation marginals;288 exact reset energy balances,288 memory contractions and288 nonzero-memory conditions;288 numerical entropy equalities;81 spectral-floor checks;108 nonzero-uncertainty endpoint checks; the exact3/50 witness and full-swap correlation transfer; integer-core audit. Independent-path replay checked all18 raw records/192 cycle ledgers,64 matrix-exponential/Kraus steps and6 saved timing medians, plus the100-digit weak case. A reference real/complex array mistake was fixed before final reference checks. Same author, not independent research review or full-project/Lean validation.

## Prior art and continuation

Unchanged executed reuse: stage18 profile, graph and propagator; stage17 residual/phase engine; inherited interval modules. The stage19 controller-edge canonicalization is an explicit adapter. Primary context: Reeb-Wolf arXiv1306.4352; Strasberg et al.arXiv1610.01829/PRX7,021003; Bhoi-Shaji arXiv2606.14163(2026 preprint); Micadei et al.arXiv1711.03323. These are established thermodynamic/memory/weak-limit methods; no global novelty or new accepted family is asserted.

Next: replace staged bath delivery/reset by a costed autonomous resource conveyor and justify its initial preparation class. Returning baths must retain their correlations. Do not discard the coherent term before taking a weak-contact limit. The strong zero-temperature objective remains a goal, not a premise or a theorem established here.

Full proofs, integer code, exact raw evidence and all prior histories are in the cumulative standalone bundle, not the whole Enterprise Math repository. Actual Drive upload/hash/readback are recorded after delivery; this note does not fabricate them. Persistence is not mathematical acceptance.
