# Heartbeat: coherent memory blocks instead of frozen sectors

Event-ID: brc-heartbeat-coherent-memory-blocks-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author derivations and checks, no independent review, Lean or admission.
Source read: enterprise-math@f5f2c5a3c54a921f4238dd82809438e140e1b8fa; global@68c6635c5d2e0c96581f9178ec9e4360c36115ec.
Standalone parent:9ed22f44d0e29dfc3f8a2e66b3ee07eb9d5051a0. P000 and residual-first constraints unchanged.

## Exact new interface and its limits

Continue H=H_B+J X_S+Z_S B/2 with B=gamma(N_B-Ke)+epsilon(n0-e). Select two strongly hopping active bath sites. In the cut model the other K-2 modes have arbitrary number-conserving internal H_R, but no active-remote hopping or density interaction. Internal density interactions within each region are allowed. This is a specified dimerized subclass, not an exact solution of Stage22's uniformly strongly connected ring. The effective central-to-total-number coupling remains nonlocal; no free native local realization is asserted.

Conserved active and remote particle numbers label positive matrix-valued blocks. Active occupancies0 and2 give central2x2 blocks. Occupancy1 keeps the coherent |10>,|01> pair and gives H_m=J XI+kappa IX+d_m ZI+g ZZ, d_m=[gamma(m+1-Ke)+epsilon(1/2-e)]/2, g=epsilon/4. The originally observed field B is genuinely nonconserved. Its mixing is not treated as an error or deleted. Arbitrary initial correlations require conditional matrices, not scalar weights times a common state. Central-only future instruments act on the same blocks; bath operations mixing the retained charges leave this exact quotient.

For iid bath occupation e=u/v, all spectator weights binom(K-2,m)u^m(v-u)^(K-2-m) are retained as integers. There are K-1 quantum4x4 blocks and2(K-1) central2x2 blocks. No nonzero probability tail is removed. Generic active clusters or arbitrary inhomogeneous couplings need not share this small representation.

## Explicit memory, long-time readout and delayed source

Let rho_+- be the coherence between the two active occupations and H_+=JX+(d+g)Z, H_-=JX+(d-g)Z. Exactly,
i hbar dot rho_+-=H_+rho_+--rho_+-H_-+kappa(rho_---rho_++).
Its solution is the transported initial coherence minus i kappa/hbar times the integral of the past diagonal-block difference under X->U_+(t-s)X U_-^dag(t-s). This propagator preserves Hilbert-Schmidt norm; decay of memory is not assumed. The diagonal-block equations retain the corresponding backflow terms. Solving the joint4x4 block avoids fitting or repeatedly resetting this memory.

Write H^2=A I+D, A=J^2+kappa^2+d^2+g^2 and D=2Jkappa XX+2kappa d ZX+2dg IZ. The three Pauli products anticommute, giving D^2=R^2 I with R^2=4(J^2kappa^2+kappa^2d^2+d^2g^2). The propagator follows from the two squared frequencies A+R,A-R. Exact R=0 degeneracies are handled separately, never with a tolerance-based merge. Inherited root_trig is reused unchanged; integer square-root intervals and derivative bounds1/2 for cos(sqrt y),1/6 for sinc(sqrt y) retain all irrational-argument error. There is no time-stepping error. The mathematical formula holds for finite times; the implementation retains explicit argument/precision budgets.

For initial central diag(1-p,p) and active I2/2, coherent-minus-frozen probability first differs at order6:
[2(1-2p)J^2g^2kappa^2/45]t^6+O(t^8).
At J=kappa1/4,g1/40,p1/3 the coefficient is1/27648000. This order is a commutator cancellation, unrelated to the count of native axes. At t1/100 the conditional probability difference is3.61689109197447155649e-20, inside a168-bit outward interval excluding zero. With epsilon=1/18446743979220271189,t64 and the declared K2 detuning, the difference is1.82922702800943654755e-38, strictly positive in a192-bit interval and independently checked by100-digit4x4 matrix exponentials. The large integer is a coupling parameter, not a factorization or temperature result.

Repeatedly deleting active coherence is an intervention, not free compression. A fixed16-time example approaches the frozen probability0.5589306848 under increasingly frequent dephasing, rather than the coherent0.5556790225. Exact rational history checks also separate the processes. Standard projection kernels, spectral algebra, reaction-coordinate enlargement and quantum Zeno dynamics are prior art.

## Nonzero boundary: retained, with a conditional quadratic certificate

Restore two boundary hoppings of magnitudes eta_L,eta_R and arbitrary retained phases. Set v=|eta_L|+|eta_R|. Generic system trace distance from the cut law is at most min(1,v|t|/hbar). If the ENTIRE initial joint state is invariant under active-number parity, H_cut is even and the boundary hopping is odd. The reduced central law is then even in the boundary amplitude. Twice differentiated Duhamel propagation gives the stronger bound min(1,(v|t|/hbar)^2). This is independent of the total number of bath modes. It does not apply to discarded parity-even density couplings, unverified joint symmetry, or arbitrarily normalized selected outcomes.

At eta_L=eta_R1/1000,t64, the bound is256/15625=0.016384. A separately derived weaker-link certificate eta_each1/100000 uses the same cut calculation and bounds the actual K1200 ring probability in approximately[0.356139842380982,0.356143119180982], strictly below the frozen result by at least9.7147524e-5. This parameter was chosen after the main run; it is a mathematical extra certificate, not additional frozen performance statistics. Strong boundaries can make the bound uninformative and require a larger active region.

The symmetry is not inferred from stationary marginals. A full-rank correlated initial state with both marginals maximally mixed violates it. Its100-digit reference trace difference is1.64582501171965406579e-7 at eta_each1/10000,t1, exceeding the incorrectly applied quadratic4e-8 but respecting the generic0.0002 bound. The first imaginary-coherence trial did not provide this witness because its response cancels; the full12-case construction record is preserved, not counted as random evidence.

Two small full-bath diagnostics execute inherited directed Taylor propagation for16 initial columns: actual-minus-cut probabilities are approximately5.68122825336e-8 at eta1/100,t4, and4.52288010452e-8 at eta1/1000,t16. Both intervals exclude zero and agree with independent100-digit full16x16 exponentials. Error upper bounds are not confused with these much smaller actual effects.

## Preparation-dependent all-time floor

For the initial independent bath tau=e^N(1-e)^(K-N), conservation of bath number implies [U,I_S tensor tau]=0 even with nonzero active mixing, remote density interactions and boundary hopping. The reduced central channel is therefore unital. If rho_S>=p_min I, then rho_S(t)>=p_min I for all time. This extends the floor beyond conserved B, but relies on the actual conserved preparation. It is not a claim that all admissible native states have this symmetry, and not a temperature assignment to arbitrary populations. Initial sector coherences, correlations with the target, number-changing interactions, measurement conditioning or resets can change the premise. No universal zero-temperature or Shor theorem follows.

## Executed costs and checks

Frozen selected-development plan:5 cases,3 repeats,15 complete rows. J=kappa=gamma1/4,epsilon1/10,e1/4,p1/3. K12 at times4,64,128 yields probabilities0.5285285210752941,0.4358008914608830,0.4579287738405053; frozen-label results0.5285011067462966,0.4273840840429343,0.4471256246322999. Complete compilation medians0.051571746,0.058741630,0.062102168 seconds. K120/K1200 at t64 yield0.3912360168407226/0.3561414807809820 in0.774943221/9.860236347 seconds. K1200 has1199 quantum blocks plus2398 scalar blocks, representing accessible dimension2^1201 for this specified class. Probability interval width is1/154742504910672534362390528. Native layout, binomial weights and every sector readout are charged; module startup is excluded. No CPU affinity and no best-classical speed claim. The inaccurate frozen method is faster, not a same-accuracy competitor.

3877 main finite checks passed, including100 exact squared-spectrum identities,3200 directed-entry references,54 exact delayed-source coefficients,72 coupled memory equations,24 exact energy identities,27 full-bath compression comparisons,27 nonzero boundary comparisons and exact symmetry/preparation checks. Main15 rows and10 timing medians replayed without replacing times;7 independent100-digit selected4x4 exponentials and2 full-bath exponentials additionally checked. Production is integer/Fraction and inherited kernels are unchanged. A tool timeout preserved14 complete main rows; only the missing fifteenth row resumed. Same author, no independent reviewer, Lean or full-project regression.

## Next and durability

Next unfinished unit: enlarge the active region when its boundary is not weak, retain inter-block coherence and certify accumulated flux rather than extrapolating a small-boundary estimate indefinitely. The current model does not solve generic long-time strong-link memory. All prior work, true tiny responses, cancelled trial witnesses and resource limits are retained in the cumulative standalone bundle, not the full Enterprise Math repository. Actual upload/hash receipts follow publication. Persistence is not mathematical acceptance.

Primary context: Nazir-Schaller arXiv1805.08307; Lacroix et al.arXiv1406.4965; Facchi-Pascazio arXiv0903.3297. No global novelty or new general BRC family is asserted.
