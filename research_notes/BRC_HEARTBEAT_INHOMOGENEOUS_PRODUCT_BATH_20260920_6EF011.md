# Heartbeat — nonidentical full-rank product baths via observer-safe permutation twirl

Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE / NOT ADMITTED

Stage26 allows independent but nonidentical diagonal full-rank bath units. Under a bath-permutation-invariant Hamiltonian and central-only future instruments, the initial bath may be replaced exactly by its permutation twirl. This is an observer-specific quotient; site-resolved bath labels are not declared nonexistent.

The twirled nonidentical product bath is carried by the exact Poisson-binomial polynomial F(z)=prod_i[(1-e_i)+e_i z]=sum_k P_k z^k. Every normalized total-spin state with physical occupation k has eigenvalue P_k/C(K,k), which is then combined with all total-spin multiplicities from Stage24. No e_i is replaced by its mean before forming P_k, and no tail coefficient is cut.

A mean-matched witness uses alternating e_i=1/5,3/10, whose mean is exactly1/4. It is not equivalent to an iid e=1/4 bath: at K=12,t=4 the central population differs by about+5.40835358e-5. At t=1 the differences remain nonzero for K=12/24/48. Conversely, a site-resolved bath observer immediately distinguishes the original and twirled states, so the quotient is valid only under the declared symmetric evolution/central-observer lease.

Small K=2,4,6 full-Hilbert references match the candidate. Frozen t=1 experiments K=12,24,36 use three repeats and K=48 one run. Candidate numerical bounds remain below6.3e-18.

The finite-device spectral floor is min(p,1-p)*prod_i[2 min(e_i,1-e_i)]>0 at finite K but can decay with resource size. Thus heterogeneous local full rank still does not imply a K-independent positive temperature floor. Nonidentical coherent product baths require matrix-valued twirled Schur blocks and are the next unclosed unit.
