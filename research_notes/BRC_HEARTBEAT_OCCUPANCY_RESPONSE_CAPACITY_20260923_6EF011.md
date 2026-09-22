# Heartbeat42: occupancy-dependent infinite response and macroscopic residual capacity

Event-ID: brc-heartbeat-occupancy-green-capacity-20260923-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE / SAME-AUTHOR DERIVATIONS AND TESTS / NOT ADMITTED
Parent standalone:9234568a28b2feed8a1eb64d483b7b9677798ee8.
Global read:0d398136f50aa991796ea162c321e8c354336c44; project read:82596e6fd92632c34f0cfc85f642f6f507bd82c3.

## Scope and actual change

The user corrected the object from a rigid rod to joint native Cell occupancy, macroscopic integrity and residual response at arbitrarily large distances in one self-consistent heartbeat. Stage42 does not impose fixed length, a prescribed angle, or a repeated field reset. P000 and the provisional heartbeat definition are unchanged. This is a new explicit constitutive candidate, not a derived physical law: each configuration X gives a finite supported real source s_X; edge loads on the native Z6 nearest-neighbour graph satisfy D j=s_X and minimize C(j)=sum j_e^2/2 for that fixed source. The simplest version is s_X(z)=q*n_z(X); signed source variants are separately stated. Source, field load, probability and complex amplitude are not interchangeable.

## Infinite response and a useful remaining loop

The prior positive-cone flow is a valid finite-cost witness, not an already minimized field. On the native e1/e2 plaquette with corner e1 its circulation is Q/56. Subtracting Q/224 times the unit circulation changes no divergence and lowers C by exactly Q^2/25088. The prior existence result is preserved; it never claimed optimality. The old edge function is actually executed unchanged.

For L=D D*, L phi(x)=12phi(x)-sum_neighbours phi(y), the decaying infinite Green kernel has Fourier multiplier 1/(12-2sum_i cos k_i). Both that multiplier and its square are locally integrable in dimension6. For finite s, phi=G*s is in ell2 and j*=D*G*s is the unique minimum ell2 load: any other load differs by divergence-free h orthogonal to j*. Thus C_*(s)=s^T G s/2. G(x)>0 at every finite displacement, and symmetry plus L G=delta0 gives the exact identity G00-G01=1/12 for adjacent Cells. Boundary class and reconstruction remain explicit.

Exact finite Dirichlet computations for R1/2/3 use7/28/84 symmetry-orbit states rather than729/15625/117649 cube vertices. They give G00 lower bounds353/3808,1164877/12521223,and19284815919736623208242338473/207213889825892710885718459904. Their displays are0.09269957983,0.09303220620,0.09306719707. These are lower bounds, not the infinite value. The local-cycle improvement gives upper2687/12544; the remaining gap is not concealed. Orbit multiplicities and boundary diagonal terms are retained.

## Occupancy feedback cannot be reduced to its mean

For mu=E[s_X] and source covariance Sigma, E C_*(s_X)=C_*(mu)+Tr(G Sigma)/2. The missing term is nonnegative. This law does not say covariance alone suffices for arbitrary future quantum observations.

A two-Cell example explicitly permits two labelled materials to share a Cell. Preparation A has(0,0) or(e1,e1), each with probability1/2; preparation B has(0,e1) or(e1,0), each with probability1/2. All single-material marginals and mean source fields agree. Yet A has same-Cell probability1, B has0, and E_A-E_B=q^2/12 exactly. Mean source alone loses that cost.

A linear effective quantum Hamiltonian retains the four configurations: H=-J(X_A+X_B)+(d/2)Z_A Z_B,d=q^2/12-epsilon. Epsilon is an explicitly optional contact preference, not hidden rigidity. The initial full-rank state is.99|++><++|+.01 I/4. With q1,J1/48,t4, the actual inherited exact Pade22 propagation gives p_same0.4730055019011752 for epsilon0, and0.5269944980988248 for epsilon1/6, each with deterministic continuous-probability radius5.4793517127e-12. Separately assembled180-digit full4x4 exponentials give0.47300550190095855 and0.52699449809904145. One-material position probabilities remain1/2 throughout. Removing the interaction by averaging the source first leaves p_same0.5. No nonunitary renormalization or prescribed pose is used.

The constructive signed-source extension needs no extra contact attraction: with contributions q_A and q_B, same- versus separate-Cell cost differs by q_A*q_B/12. Opposite q_A=-q_B gives d<0 and encourages joint occupancy in this toy. For q1 its Hamiltonian is exactly the already computed epsilon1/6 matrix up to an omitted common scalar; that existing trajectory is reused, not counted as a new experiment. Long-time binding, forbidden co-occupancy models and a microscopic fast-field elimination are not thereby proved.

At q1e-8 the occupancy difference from q0 at t4 is-2.7246311574204856e-18. The inherited64-order rational Taylor computation has radius1.2665774374e-141 without normalization repair; an independently assembled180-digit exponent lies inside. This is a model effect, not an experimental signal. The q1e-4,64-step case keeps a18929-bit denominator; tiny parameters need not be computationally cheap.

## A conditional macroscopic capacity theorem

A native cube of side ell has12*ell^5 outgoing edges. For a net source Q inside, disjoint expanding cuts and Cauchy-Schwarz imply C_out>=Q^2/(192*ell^4). This bounds every admissible flow, not just the minimizer.

Let each of N materials contribute the same unscreened sign q>0. The compact-whole event C requires a connected cluster of m>=(1-delta)N materials inside a cube of side ell, with m>=nu*ell^6. Then C_field(X)>=q^2*nu^(2/3)*(1-delta)^(4/3)*N^(4/3)/192 on C. Suppose H_other>=-bN I and the current total energy expectation is at most eN. No thermal, ground-state or equilibrium premise is needed. The entire quantum state obeys

P_C<=min(1,192(e+b)/(q^2*nu^(2/3)*(1-delta)^(4/3)*N^(1/3))).

This is a conditional probability capacity law, not a measured universal material size. Same sign, no compensating sources, unit edge costs, fixed density and the energy budget are substantive premises. For q=nu=e+b=1,delta0,N=ell^6, sides16/32/64/128 give caps3/4,3/16,3/64,3/256. These are exact certificate evaluations, not huge-body simulations.

There is a constructive alternative. Pair adjacent Cells in an even-sided block into(+q,-q) or(-q,+q), retaining the pair relationship. Putting load q on each of N/2 disjoint matching edges gives C_min<=Nq^2/4. Every local residual is nonzero but cancels configuration by configuration. Compare a mixture of all+q and all-q: identical one-Cell sign laws and zero mean source, but E[Q^2]=N^2q^2 rather than0. Mean cancellation is not actual cancellation. A fixed unpaired Q can still use the prior infinite flow, with combined cost no more than(sqrt(Nq^2/4)+sqrt(3Q^2/28))^2=O(N). Thus local complementarity plus a genuine infinite remainder is mathematically possible without deleting either.

## Instantaneous constraint and physical update remain separately testable

The same-heartbeat response is delta phi(x)=sum_y G(x-y)delta s(y), so a point-source comparison changes the constraint solution at every finite distance. It is not by itself an operational infinite-speed message or a derived state transition. A separately declared finite-inertia law phi_ddot+c^2 Lphi=c^2s has the same static equation but retains field momentum. From zero initial field under a point-source step, at graph distance r the first nonzero Taylor term has order t^(2r+2) and coefficient Q*c^(2r+2)*r!/[prod|x_i|!*(2r+2)!]. Exact coefficient tests run through distance5. No strict zero light cone or instantaneous physical transfer is inferred from this comparison.

A finite local rearrangement of edge loads changes only a zero-total source. A material hop produces q(delta_y-delta_x), not a newly created unbalanced Q. Existing infinite flux, source preparation, external compensation and remote measurement must be distinguished in the eventual signaling test.

## Execution, evidence and next frontier

216 new main assertions and10 signed-source assertions pass;36600 inherited assertions are separately replayed, not counted as new research. Eighteen immutable experiment rows cover three exact Green solves and three finite occupancy trajectories, each repeated3times. Core medians are0.000808838/0.010572400/0.193905071 seconds for R1/2/3, and0.010367205/0.009844994/0.174161241 seconds for the three trajectories. These are different computational tasks, not physical times or best-classical speed comparisons. Four180-digit reference records and six complete result replays check the saved outputs without replacing original timings.

The first serialization attempt hit Python's4300-digit output guard; the bounded scientific-output limit was explicitly raised. A110-digit reference was insufficient for the tiny1e-141 certificate; only reference precision was increased to180. Final local tests completed through container after Python-frontend interruptions. Software defects are not called physical residuals. All references are separately coded by the same author, not independent research review or Lean.

Primary context actually read at abstract/metadata scope: Henley0912.4531; Lorenzana/Castellani/DiCastro cond-mat/0010092; Bravyi/Hastings/Verstraete quant-ph/0603121; Lyons/Peres author book page. These supply established-method context, not proof of our conditional six-dimensional law. Dedicated private query Issue679/request3c0f6383-02a4-4f73-8e6a-5ea7d026d251 matched result5782380776: outerFAILED/innerPARTIAL,2metadata/abstract records,1provider call,0bridge-model calls. Returned articles were not directly relevant and were not used as theorem evidence; canonical cache ingestion remains pending.

Next: specify a local, source-conserving mechanism that forms and sustains complementary residual correlations from a common initial preparation, retains field memory, and measures integrity probability/cost versus size. No rigidity default, physical instantaneous signal, real size calibration, N,a-to-coupling compiler, modular-order extraction, Shor speedup, universal zero-temperature theorem or mathematical admission is claimed. Source/Drive publication and activity aggregate intake are separate.
