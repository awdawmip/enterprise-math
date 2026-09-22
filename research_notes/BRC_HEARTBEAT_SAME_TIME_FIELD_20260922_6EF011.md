# Heartbeat: same-time field and retained boundary response

Event-ID: brc-heartbeat-same-time-field-20260922-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: PROPOSAL_AND_EXACT_FINITE_DERIVATIONS / NOT ADMITTED
Parent standalone: f75cd53f578faca9f369313d3a3437af7d5d2416 (Stage38).
Global read:3213a53c9e70f62433bb882d921a32e803484e70. P000 and protected worldview unchanged.

## User direction

The user proposes solving an instantaneous whole field instead of silently treating computational order as physical time: later-discovered constraints should revise earlier provisional values. The added conjecture that the whole field necessarily reaches its global energy minimum is retained as a question requiring explicit conditions, not adopted as a physical axiom.

Physical time t, solver iteration k and logical/spatial layer j are separately typed. This does not invalidate earlier explicitly declared real-time unitary models. A numerical initial guess may be revised; a hard fixed preparation cannot be overwritten without changing the problem. Posterior inference is not automatically backwards physical causation.

## Completed bounded mathematics

For Phi=[x^2+(x-y)^2+(y-epsilon)^2]/2, the unique minimum is x=epsilon/3,y=2epsilon/3,Phi=epsilon^2/6. Freezing x=0 before processing the right-hand boundary gives y=epsilon/2 and Phi=epsilon^2/4. All three directed drops at the actual minimum remain epsilon/3, so zero stationarity error does not imply zero structural residual. Epsilon=1e-8 is retained exactly.

The correct eliminated carrier is x(y)=y/2 and Phi_eff(y)=y^2/4+(y-epsilon)^2/2, not the frozen number x=0. General positive quadratic elimination retains the Schur complement, source response and interior reconstruction. This is standard Schur/Kron reduction applied as a candidate BRC boundary interface, not a novelty claim.

For unitary links U_j, positive weights w_j and fixed complex endpoints a,b, minimize Phi=(1/2)sum w_j||psi_(j+1)-U_j psi_j||^2. Define W_0=I,W_(j+1)=U_j W_j,R_k=sum_(j<k)1/w_j,R=R_L. The exact solution is psi_k=W_k[a+(R_k/R)(W_L^dagger b-a)], with Phi_min=||W_L^dagger b-a||^2/(2R). A weighted Cauchy-Schwarz proof and five exact direct normal-equation comparisons retain noncommuting phases. Compatible b=W_L a recovers the original forward circuit. An incompatible imposed output yields a best-fit residual field, not a correct simulation of the unchanged circuit or a discovered Shor answer.

For a fixed unwrapped winding sector m and loop offsets alpha_j, minimizing (1/2)sum w_j(theta_(j+1)-theta_j-alpha_j)^2 yields residual_j=(m-sum alpha)/(w_j R) and energy (m-sum alpha)^2/(2R). The global optimum may retain every local mismatch. This is a declared quadratic phase model, not an exact cosine replacement.

The unchanged Stage38 unitary cycle is reused: D^dagger D=2I-H_hopping. For the three-INTERNAL-label seam M(q)=cI-isX, det(D^dagger D)=16q^4/(1+q^2)^2; q=0,1/3,1e-8 are checked exactly. Nonidentity alone does not exclude a zero mode: seam X retains its +1 direction and gives rank5. A nonzero boundary/norm condition is needed to exclude the trivial zero field. No spatial triangle or primitive-force law is inferred.

A stationary full-rank rho=diag(1/3,2/3),H=diag(0,1) is unchanged under unitary evolution and has nonminimal energy2/3. Thus same-time, stationary, equilibrium and ground-state are different claims. Numerical relaxation requires its own iteration parameter; physical dissipation and finite-temperature free-energy criteria cannot be supplied silently. Positive structural residuals or shifted positive ground energy do not prove nonzero temperature.

## Evidence and next question

86 exact assertions passed. Candidate reuses unchanged Stage19 rational matrices, Stage32 operators and Stage38 ring Hamiltonian; a separately coded SymPy normal-equation path checks five complex weighted paths. A first checker compared unsimplified expressions syntactically; replacing it with exact simplification resolved the check without changing the derivation. Same author, no independent review or Lean. Prior 875-file manifest and all ancestor manifests verified unchanged. No physical experiment, performance benchmark, universal zero-temperature theorem or Shor acceleration is claimed.

Primary context at actual scope: official abstracts quant-ph/0405098,1305.0681,1102.2950,1804.03023; David Tong statistical physics official HTML section1.3.4. One configured arxiv query, private Issue478,batch affce431-998c-4778-bc80-7897f857939d,matched result5777398515,returned COMPLETED with one metadata/abstract record and one provider call; no full paper was read through the bridge. Full raw-cache catalog integration is pending.

Next: a fixed-physical-time phase-sensitive general-graph boundary-response solver with reversible interior reconstruction and elimination-order comparisons. Preserve boundary types, phase, loop operators, structural mismatch and numerical convergence error. Do not continue expanding cyclic-clock hardware as though it were the only representation of the user's field question.
