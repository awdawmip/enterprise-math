# X6 R61 — Repeated-source star moments: exact bounded-degree tomography and sharp observation depth

Date: 2026-11-20 (Asia/Shanghai). Line: RS-X6-NATIVE-TIME-DYNAMICS. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Source provenance and exact scope

Continue X6 R60, '2026-11-20_x6_r60_general_collision_graph_positive_motif_tomography.md', immutable source https://github.com/awdawmip/enterprise-math/blob/d66d63f1d80352f88aca1de232a7aff1eb3adf45/research_notes/portable_direct/2026-11-20_x6_r60_general_collision_graph_positive_motif_tomography.md. Scientific P000 V5 remains frozen at source commit a72226e2430ffa4786321ac86e7f0c599d5f0389 (p000_reality_foundation.json, blob dc84bdae6595b5e237a2ad50d8b21916adb2e447). Current norms are separately read from canonical main and do not change the frozen science.

We work only in R60's explicitly conditional two-source positive BRC experiment: the same p named Ports on source A and B; arbitrary successful directed 0/1 incidence S=(S_ij), its forbidden complement C; successful AB weight uv with u,v>0 independent of Port; independent reset trials preserving S and a shared Port reference. For a repeated-source star observer, the A Port must be the SAME across trials, while B Port names are free and may repeat. This is a deliberately weaker cross-trial predicate than full motif tomography: B-to-B equality, inequality and edge-to-edge incidence constraints are NOT needed. The AB words denote complete conditional branches, not primitive two-force balances or physical heartbeat steps. Native TRIADIC_CLOSURE_E admission remains open.

Let r_i=sum_j S_ij be successful outdegree, 0<=r_i<=D<=p (D is a known degree bound). Let c_d=number of i with r_i=d. We assume p,u,v known or independently calibrated; in particular normalization of positive masses divides by (uv)^t. Set m_0=p.

## R61.1 The repeated-A star identity

For every integer t>=1, perform t independent reset AB trials, require all A Port names to coincide, do NOT constrain B Port labels and sum positive permitted branch masses. Its normalized observation is

m_t := Z_star(t)/(uv)^t
    = sum_i sum_{j_1,...,j_t} product_{k=1}^t S_{i,j_k}
    = sum_i (sum_j S_{ij})^t
    = sum_{d=0}^D c_d d^t.

This follows by distributing the product over independent B choices. There is no signed path cancellation and no assumption of a transition matrix as a physical propagator. For t=0, m_0=p is given by the known Port cardinality, not by an invented zero-step physical experiment.

## R61.2 Exact finite reconstruction at depth D

The D+1 numbers m_0,m_1,...,m_D determine the entire row-degree multiplicity vector (c_0,...,c_D), with no numerical fit. Define the signed Stirling coefficients s(k,j) by

s(0,0)=1;
s(k,j)=s(k-1,j-1)-(k-1)s(k-1,j), for k>=1,
with out-of-range coefficients zero.

Then set F_k=sum_{j=0}^k s(k,j)m_j. The falling-factorial identity x_(k)=sum_j s(k,j)x^j gives

F_k=sum_{d=k}^D c_d (d)_(k),   (d)_(k)=d(d-1)...(d-k+1).

This triangular system has nonzero diagonal k!, so exact back-substitution recovers

c_D=F_D/D!,
c_k=[F_k - sum_{d=k+1}^D c_d (d)_(k)]/k!,  k=D-1,...,0.

In particular, the degree-generating polynomial G(z)=sum_{d=0}^D c_d z^d has the finite Taylor identity

G(z)=sum_{k=0}^D (F_k/k!)(z-1)^k.

This is a scope-typed sufficient-statistic theorem: repeated-A positive-star observations through D preserve exactly the row-degree histogram. It is not a quotient preserving all future joint incidence or arbitrary Cell/Link operations. If the known bound D=0, m_0=p suffices.

## R61.3 Uniform sharpness of the depth bound

For every integer D>=1 and every p>=2^(D-1), there exist TWO p-by-p 0/1 incidence tables with maximum successful row degree at most D, nonisomorphic even under independent row relabelling, that agree in ALL repeated-A normalized observations of depths 0,...,D-1 but differ at depth D.

Construction: set c_d^even=binom(D,d) for even d and 0 for odd d; set c_d^odd=binom(D,d) for odd d and 0 for even d. Both have exactly 2^(D-1) rows. For p larger, pad both by p-2^(D-1) zero-degree rows. Since 2^(D-1)>=D for D>=1, every row degree is realizable on p B Ports by making S_ij=1 for j<r_i and 0 otherwise.

The Dth finite-difference identity yields

m_t(even)-m_t(odd)
    = sum_{d=0}^D (-1)^d binom(D,d) d^t
    = 0 for 0<=t<D,
    = (-1)^D D! for t=D.

Thus observation depth D cannot be replaced by a uniform smaller depth within the repeated-A-star family when p>=2^(D-1). This lower bound is specifically about THIS observer family. Additional non-star joint probes may distinguish these witnesses sooner.

Concrete D=4, p=8 witnesses:
even histogram c=(1,0,6,0,1) and odd histogram c=(0,4,0,4,0).
Their m_0,...,m_3 coincide: (8,16,40,112).
Their m_4 are respectively 352 and 328 (gap 24=4!).

## R61.4 Relation to R60 residual and resource count

The full motif family of R60 can distinguish the complete simultaneous-Port-renaming orbit, but may require up to p^2 successful AB trial events per individual motif and numerous templates. For the strictly smaller target of the successful outdegree histogram with bound D, the present reconstruction needs only D star observers (t=1,...,D), each involving at most D AB trials, plus known m_0=p; running each once consumes D(D+1)/2 AB trial occurrences before precision/repetition overhead. For D<<p, this is a substantive reduction in required trial depth and observer complexity.

The collapse is provably safe for readouts depending only on the row-degree histogram; it is NOT safe for general future incidence-sensitive observations. In particular, R60's three-Port S_A and S_B have identical row AND column degree histograms, so even both orientations of ALL such star observations fail to distinguish them, whereas the two-trial non-star Q observer differs by (uv)^2. This supplies an exact residual-fidelity boundary.

The scalar readout may require large exact integer precision as t grows; trial-count savings alone are not a general bit-cost improvement. Source weights, reset, persistent A-Port equality and physical admission are explicit assumptions.

## Exact author reproduction

Companion: research_notes/portable_direct/x6_r61_repeated_source_star_moment_verify.js.
Results: research_notes/portable_direct/x6_r61_repeated_source_star_moment_results.json.

Node.js BigInt checker exhaustively enumerates all 530 binary incidence tables for p=1,2,3 and recovers each degree histogram from m_0,...,m_p using the displayed Stirling/back-substitution formula. It also validates even/odd sharpness witnesses for every D=1,...,10, including the exact Dth gap, and inverts both degree histograms. All assertions PASS. The symbolic theorem covers arbitrary integer p,D satisfying the stated hypotheses; finite checks are not an independent proof review.

## Next discriminating frontier

1. Find bounded-degree joint incidence families whose complete simultaneous-Port-renaming orbit can be reconstructed from a fixed set of short positive motif observers, or a sharp witness against the proposed family. Exact star signatures alone are insufficient (R60 obstruction).
2. Test the frozen-P000 native whole-triad event signature: is a repeatable cross-trial A Port identity with stable Cell/Link incidence and valid TRIADIC_CLOSURE_E carrier actually constructible? If not, preserve the conditional model and locate which equality/reset interface fails.
3. Derive finite-resolution bounds for the integer inversion when m_t is noisy, tracking the high-degree moment amplification and precision resource cost.

Control observation (read-only): request r2-20261120-2215-x6-native-cont-read-v1 SUCCEEDED as of 2026-11-20T14:17:34Z, source 7c2f164ec817efcd749276be473cac53b09ed784. It reported owner=taskbook/unassigned, dispatch=NEEDS_DISPATCH, execution_authorized=false, and typed predecessor continuation required for formal CLAIM/PROGRESS. Own historical researcher EM-X6-214D9C, SID MCP-d467c19ce42d4d7fa65a3901db1cf6b2, Activity RA-545183ADD4EF71C3E4698AEE retained as provenance. This independent portable publication does not mutate formal Task/CLAIM/Result or assert native admission.
