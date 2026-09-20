# Heartbeat — coherent full-rank product baths as matrix-valued Schur blocks

Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE / NOT ADMITTED

Stage25 extends the ordinary full-rank product-bath result to an identical coherent one-site bath state rho=[[43/100,6/25],[6/25,57/100]], whose eigenvalues are3/4 and1/4. The K-fold product bath remains permutation invariant, but each total-spin block is matrix-valued rather than a scalar weight.

The exact Schur-Weyl block is (det rho)^r Sym^(K-2r)(rho), repeated with multiplicity C(K,r)-C(K,r-1). In the unnormalized spin basis the matrix entries are rational. The production readout retains all off-diagonal block entries, constructs the integer propagator columns, and contracts the full matrix-valued initial block. No local dephasing or phase randomization is used.

Exact trace identities pass through K=16. Independent90-digit full-Hilbert references for K=2,3 lie inside the candidate intervals. At K=12,t=4, the coherent bath gives central population~0.5607533222565554 while diag(3/4,1/4), with the same local eigenvalues/entropy but a different basis orientation, gives~0.5460597190233154. At K=12,t=1, deleting only the off-diagonal entries while retaining the same local occupation probabilities changes the result by about-1.73569e-7.

Frozen t=1 timing cases K=4,8,12,16,24,32 use three repeats each. Median candidate times are about0.0087,0.0450,0.151,0.381,1.508,4.150 seconds; candidate numerical probability bounds remain below9e-17. This is a polynomial exact-block prototype, not an optimal or generic many-body algorithm.

The finite-device full-rank floor remains positive at every finite K but decays with K; coherence does not create a K-independent positive temperature floor. Nonidentical product baths and local symmetry breaking require multiplicity-space transport rather than the current identity multiplicity factor. No generic quantum simulation theorem, Shor speedup, or universal absolute-zero theorem is claimed.
