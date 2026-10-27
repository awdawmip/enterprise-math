# PREFIX-272: Sparse Z2 Phase-BRC Pair-Probe Tomography

**Author-side exact conditional mathematical result, 2026-10-26. Not admitted as a native heartbeat theorem.**

## Sources and carrier
Global Knowledge pinned to awdawmip/chatgpt-global-knowledge@1109726a4b9d2244b8aa53404ef4a4b27a3ecd04 (bootstrap, manual, P000 projection and matching original blob, ACTIVE worldview and project/math/BRC rules). Scientific input awdawmip/enterprise-math@7f073d2fb8e396773a95d1c6945215e92dc4da93 (Portable Research protocol, BRC-only arithmetic, joint observer preservation, heartbeat definitions, scoped Stage46 candidate, PREFIX-271). Native space remains six-dimensional with separately typed time; k is the number of labeled branch histories, not the spatial dimension. This paper declares formal permitted probes; it does **not** demonstrate that a native model allows these interventions.

For a rational signed labeled branch amplitude vector a, define the source-aligned Z2 ordered-path-pair BRC intensity of selected branches:
I_c(a) = sum_(p,q) |c_p a_p||c_q a_q| chi(phi_p-phi_q) = (sum_i c_i a_i)^2,
where chi(0)=+1, chi(1)=-1. The last equality is a typed pair-character identity, not a substitution of positive path counts for coherent amplitudes.

Let a graph H=(V,E) list the only hypothetical pair recombinations allowed, besides all singleton probes. The observations are I_i=I_(e_i) for every i and J_ij=I_(e_i+e_j) for (i,j) in E. Let S be the nonzero support read from I_i, r=|S| and c the number of connected components of H[S]. Magnitudes m_i=|a_i| are nonzero on S, and each observed edge supplies the exact signed cross term
G_ij=a_i a_j=(J_ij-I_i-I_j)/2, sigma_ij=G_ij/(m_i m_j) in {-1,+1}.

## Theorem A — full restricted-observation equivalence
For fixed magnitudes and nonzero support, two states have equal singleton and allowed edge-pair intensities if and only if they differ by one common sign on each connected component of H[S]. Among 2^r assignments of nonzero signs, each restricted class contains 2^c assignments and there are precisely 2^(r-c) classes. The complete labeled Gram matrix aa^T instead has 2^(r-1) classes, so exactly c-1 additional relative-component binary phase bits distinguish all full-Gram futures inside one restricted class. If r=0, the unique zero state has no phase residue.

*Proof.* Equal singleton intensities force b_i=epsilon_i a_i, epsilon_i in {-1,+1} on S. The BRC pair identity on each observed edge forces epsilon_i epsilon_j=1. This propagates throughout each connected component. Conversely a componentwise common sign flip preserves every permitted ordered-pair cross term. The stated class sizes and fiber ratio follow by direct sign-group orbit counting. Zero support cannot carry phase constraints. QED.

## Theorem B — spanning-tree minimal-query result
With all singleton values known and arbitrary active pairs legally available, the complete Gram is recoverable if and only if the actually queried pair graph connects S. Exactly r-1 pair probes are necessary and sufficient (including worst-case adaptive queries). Any spanning tree suffices: from its edge products and nonzero diagonals, an arbitrary path i=v0,...,vL=j yields
G_ij = [prod_(t=0)^(L-1) G_(v_t,v_(t+1))] / [prod_(t=1)^(L-1) G_(v_t,v_t)].
If fewer than r-1 edges were queried, at least two components remain, and flipping one component keeps all queries unchanged but changes a cross-component Gram entry. A new pair query can connect at most two formerly independent sign components. Thus r-1 is optimal in the declared singleton-plus-pair language; if an existing graph has c components, c-1 legal bridge probes exactly repair it. This result does not claim minimality for stronger arbitrary multi-branch interventions.

## Theorem C — exact signed cycle certificate
Suppose a fixed pure rank-one Z2 branch state is claimed to explain measured singleton magnitudes and the graph-edge pair intensities. Define sigma_ij=(J_ij-m_i^2-m_j^2)/(2m_i m_j) for active edges. Compatibility holds **iff** each sigma_ij equals +1 or -1 and their product is +1 around every graph cycle. Necessity follows from sigma_ij=s_i s_j and cancellation of each vertex sign twice on a cycle. Conversely fix a root sign in each component and propagate along any spanning forest; every chord's fundamental-cycle identity ensures that its edge equation is met. Only |E(H[S])|-(r-c) fundamental cycles need be checked. Three unit-magnitude branches with edge intensities (4,4,0) around a triangle give signed parities (+,+,-), hence a contradiction to the fixed pure Z2 rank-one model. This does not prove a physical anomaly or rule out mixtures, context shifts, memory or errors.

## Theorem D — block-local all-horizon conditional no-go
Suppose V=direct_sum_C V_C is a labeled branch decomposition, every allowed future linear BRC update is block-preserving, and every allowed BRC intensity is a sum of within-block ordered-path-pair contributions. Then independent componentwise sign flips are undetectable after **any finite action sequence**, including actions selected adaptively from otherwise equal observed histories. Indeed each block operator commutes with the independent sign transformation, and each within-block pair's phase difference is unchanged. The same holds under composition and by induction on adaptive histories. A newly legal coherent interblock coupling invalidates the premise; this is not a native physical impossibility theorem.

## Exact certificate and scope
For six **branch IDs** with unit magnitude and only pairs (1,2),(3,4),(5,6), r=6,c=3. The restricted observations have 8 classes, full Gram has 32, and exactly 2 missing relative-phase bits remain. States (1,1,1,1,1,1) and (1,1,-1,-1,1,1) agree under all permitted probes, whereas a hypothetical bridge pair (2,3) yields intensities 4 and 0. The six branch IDs do not equate to the native world's six spatial axes.

The executable verifier calls the exact labeled Z2 BRC ordered-pair character sum, enumerates **all 1,099 simple labeled graphs for k=1..5** and 33,866 graph/sign configurations, checks fiber sizes, graph classes, full-Gram classes and cycle realizability; it also checks rational magnitudes, zero support, six-branch examples, a contradictory triangle, and nine formal block-local permutations. The precise finite output is in RESULTS_PREFIX272.json. General k conclusions follow from proof, not extrapolated tests. The checker is an independently implemented *semantic mirror*, not an execution of the canonical installed Stage46 Source or a native inter-heartbeat map.

## Native transfer and next obligation
The pinned definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json has fixed_heartbeat_program=null; HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json requires a model_law_id and does not itself supply a full Phi:H_n→H_(n+1). Stage46's local phase port rule is explicitly SCOPED_CONSTITUTIVE_CANDIDATE / NOT_ADMITTED, not a whole-world material/field/momentum/time/boundary/source evolution law. Therefore the legal native probe graph remains **UNKNOWN**. The next step is to locate a full source-backed model law, enumerate its actual allowed phase effects, check whether they reveal singleton and spanning cross-terms (or produce a larger effect-span identifiability certificate), verify closure under that actual update, and run a canonical Source-import BRC comparator with exact labels/phase/outputs.

GitHub actor awdawmip can save author-side research. The native task read returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Live Owner/CLAIM, formal Result publication and independent Driver admission have not been established. No Google Drive permission workaround was used.

Status: AUTHOR_SIDE_EXACT_CONDITIONAL_THEOREM / EXACT_FORMAL_CHECK_PASS / SOURCE_IMPORT_PENDING / NATIVE_LAW_PENDING / NOT_ADMITTED.
