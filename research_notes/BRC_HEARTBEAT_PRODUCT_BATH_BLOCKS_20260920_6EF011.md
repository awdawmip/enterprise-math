# Heartbeat — ordinary full-rank product baths through total-spin blocks

Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE / NOT ADMITTED

Stage24 removes Stage23's symmetric-packet-plus-identity-tail preparation and uses an ordinary identical diagonal full-rank product bath rho(e)^{tensor K}. The permutation-invariant nonquadratic Hamiltonian is decomposed through every total-spin irrep j=K/2-r with exact multiplicity C(K,r)-C(K,r-1). In an unnormalized spin basis the evolution remains rational; all product-bath eigenweights and multiplicities are retained.

The representation identities sum_r m_r(2j+1)=2^K and sum_{r<=min(k,K-k)}m_r=C(K,k) are checked for K<=32. Full product-bath trace is exactly1 for multiple rational local states. Independent 90-digit full-Hilbert references for K=2,3,4 lie inside the integer candidate intervals.

A direct information-loss witness shows that keeping only the maximal-spin block is invalid for an ordinary product bath. At K=12,e=1/4 that block carries only797161/16777216 of bath trace; renormalized maximal-spin readout at t=1 is about0.3533729195 versus0.3536038843 with all blocks.

Executed t=1 results: K=12/24/36 use three repeats; K=48 one costed run. Quotient bath basis states are49/169/361/625 instead of2^K microscopic configurations; central+bath initial trajectories are98/338/722/1250. Populations are approximately0.3536038843/0.3536170657/0.3536214599/0.3536236571 with candidate absolute numerical bounds below6.3e-18. The current implementation is polynomial but not optimal; worst-case work per fixed Taylor layer is O(K^3), not O(log K).

For p=1/3,e=1/4, the complete finite apparatus has a general central rank-one probability floor (1/3)2^{-K} under arbitrary joint unitary evolution. It is positive for every finite K but decays exponentially with bath size. Therefore local full-rank imperfection alone does not supply a K-independent positive temperature/excitation floor. This is a retained boundary for the strong absolute-zero program, not a refutation of that goal.

Scope: identical diagonal full-rank product baths and the declared permutation-invariant Hamiltonian. Identical coherent product baths require matrix-valued Schur blocks; nonidentical product baths carry multiplicity-space information. No generic many-body simulation theorem, Shor speedup, or universal absolute-zero theorem is claimed.
