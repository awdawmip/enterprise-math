# Discrete-cell observer comparison and tetrahedral manuscript revision

Progress-Event-ID: CELLREV-EED916-20260911-01
Researcher-ID: EM-CELLREV-EED916C8640C
Research-Activity-ID: RA-CELLREV-EED916C8640C
Status: NONCANONICAL_RESEARCH / ORDINARY_PROOFS / FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_FOUNDATION
Source-snapshot: awdawmip/enterprise-math@9086c58616d5343f6ef839ffce46cd80eb952ab7
Parent-objective: Direct user request to find recent discrete/cell work, improve outreach, and revise the actually submitted paper with relevant project results.

## Preserved source and boundaries

The actual submission basis is YUAN X's September 3 eight-page Tetrahedral Endpoint-Sum Residuals and a Non-split Affine 2-Torsion Extension. A separate eleven-page Pell/Ramanujan manuscript is described in endorsement emails but was not used or reconstructed from those summaries. The proposed revision retains title and author, is ten pages, and has not replaced the journal submission. Original K4 results remain separated from revision additions. The prior Lean checkpoint 95a9cd418f6abdb4916f5cf8182437af61dba9db is provenance reported by the original manuscript; no Lean rebuild or formalization of additions occurred this session.

P000 is unchanged. Native X6 Cell coordinates are not identified with K4 edge coordinates: E0 has rank five, while the native cell torsor has rank six. No physical model, QCA realization, unitary dynamics, continuum limit, or arXiv endorsement is established.

## Exact added arguments

1. Coordinate-free star realization. For edges (AB,AC,AD,BC,BD,CD), opposite sums are (p,q,-p-q), and normal form is N(p,q,e)=(e,0,0,-p-q,q,p-e). The four star parities are (e,e+p,e+q,e+p+q), with p,q reduced modulo two. Each vanishes on delta(V0), and their sum vanishes. They identify W=R/2R with the even-weight functions on four vertices, equivariantly under (g f)(i)=f(g^{-1}i). The torsion vector maps to the constant-one function. This gives the affine-plane model without relying on an unspecified precomposition convention.

2. Observer-specific parity repair. Reuse P023 fibre-constancy and coarsest-repair laws (REUSE_APPLIED), not a newly invented general quotient theory. On R, the matching map m is equivariant and supports all finite S4 operation words when only matching outputs are requested. It does not determine star parity: every m-fibre consists of N(p,q,0) and N(p,q,1). The coarsest repair for chi_A is (m,chi_A), exactly one binary coordinate per fibre, sufficient for all rotated star outputs. In W the adjacent-transposition actions are s1(p,q,e)=(p,p+q,e+p), s2=(q,p,e), s3=(p,p+q,e). The outputs e, e after s1, and e after s1*s2 recover e,p,q, giving exactly 2,4,8 observation classes at horizons 0,1,2. Non-splitting does not invalidate the matching-only quotient. Integral-lift enabledness requires m=0 and chi_A=0; zero and tau witness loss of enabledness under m alone. No positive-mass replacement of signed data is made.

3. Connected regular-graph classification. Let G be finite simple connected d-regular with d>0, n vertices and m edges. The zero-total signless-incidence cokernel R_G is Z^(m-n+1) if G is bipartite; Z^(m-n) if nonbipartite with n odd; Z^(m-n) plus Z/2 if nonbipartite with n even. Proof: let L=delta(V0) and Lsat=(L tensor Q) intersect E0. In the nonbipartite case delta is injective: kernel values alternate signs along edges, and an odd cycle forces zero. For x=delta(u) integral, fractional coordinates of u alternate signs modulo Z; an odd cycle forces all of them to be zero or all one-half. Zero total excludes the half class for odd n. For even n it exists, e.g. u1=(1-n)/2, ui=1/2 for i>1, giving precisely Z/2 torsion. Rank(L)=n-1. In the bipartite regular case the parts have equal size. Subtract a rational multiple of the alternating kernel vector to remove every fractional coordinate without changing zero total or delta(u); thus L is saturated and has rank n-2. Subtracting these ranks from rank(E0)=m-1 proves the formula. Regularity is necessary for this exact restriction: sum(delta(v))=sum(deg(i)*vi), which vanishes on all vi-vj precisely when all degrees agree.

4. Even complete-graph non-splitting. For each even n>=4, T=Tor(R_Kn)=Z/2 is fixed by S_n. Let H be the zero-total edge subspace over F2. An invariant functional on H is represented by coefficients c modulo constant vectors. Invariance means gc-c is constant. Every transposition fixes its own edge, so that constant must be zero. Transpositions generate S_n, whose edge action is transitive; therefore c is constant and the functional vanishes. Hence Hom_Sn(H,F2)=0. The quotient R_Kn/T is free, so T embeds after reduction modulo two. An equivariant retraction from R_Kn/2R_Kn to T would pull back along H -> R_Kn/2R_Kn to a forbidden nonzero invariant functional. Integral retractions also factor modulo two. Both extensions are non-split. The ordinary proof is included in the revised manuscript. No first-discovery claim is made for this elementary classical-adjacent argument.

## Executed exact regression

Python 3.13.5, SymPy 1.14.0, NetworkX 3.6.1. All assertions passed: original ten maximal minors (2,0,0,0,2,0,-2,0,0,2); 3125 integer normal-form/lift cases; 192 all-star covariance cases (8 states times 24 permutations); all eight possible linear functionals on W; horizon class counts 2,4,8; all 15 connected regular graph-atlas representatives with 2 through 7 vertices; K3 through K10 Smith forms; zero invariant-dual dimensions for K4,K6,K8,K10; 729 signed three-axis depth-repair cases. These are finite regressions, not proofs of the quantified theorems. The P023 generic executable module was not claimed to have been run; its mathematical interface was applied and this model was checked directly.

## Current-project reuse and external research

Applied docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md; consulted src/enterprise_math/partial_operation_quotient.py for enabledness; used definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md and the joint-observer-preservation contract. The current cell comparison is x=r+h(1,1,1), r=x-min(x)(1,1,1), h=min(x): integer-depth loss, not finite torsion.

Most direct external contact: Trezzini/Bisio/Perinotti exact QCA renormalisation, Quantum 9 (2025) 1756, DOI 10.22331/q-2025-05-28-1756; fermionic continuation arXiv:2511.23398 (2025-11-28). Further 2026 comparisons: Ludewig arXiv:2603.10501v3 (2026-03-25), and Ji/Yang arXiv:2606.19657 (2026-06-17). These motivate questions only; no map from the present extension class to QCA invariants has been constructed. Boyle/Mygdalas arXiv:2601.07769 remains a lattice/symmetry contact, not evidence of physical equivalence. Classical quotient/refinement reference: Paige and Tarjan, SIAM J. Comput.16 (1987),973-989, DOI10.1137/0216062.

## Artifact fingerprints and continuation

Proposed revised PDF: tetrahedral_residuals_revised.pdf, 10 pages, 435879 bytes, SHA256 bbbf77c8902aab2cfee06d9be949805c5d2ca9ef864a425bb0c39e22d73775d5.
Editable LaTeX SHA256: 6004db1d3b56ca72e2eb393ef24921e77d7794bfb91da4e7d6310e2c847b8ce4.
verify_revision.py SHA256: 1405a009febf095603b228a7569315332f46e6aae5dcce2a1dfbfb659a5f291d.
verification_results.json SHA256: 92cd76410e78c660013d419e9fc0d8c8237526db0ecf6e7dfb7f58c2121bebfa.

The full PDF is also attached to two unsent outreach drafts, one revised Boyle version and one targeted Perinotti version. No email sent. The original attachment-bearing Boyle draft was retained because the connector does not support editing such drafts in place. Private draft metadata belongs only in the account journal, not this source note. The existing math.NT endorsement request concerns the separate longer manuscript, not this attachment.

Next: independent proof/prior-art review of the regular-graph and even-Kn extensions, then author decision on scope and journal replacement. Do not replay old submission or send any draft automatically. No Foundation, Working Truth, task claim, review acceptance, or theorem-promotion status is changed by this persistence.
