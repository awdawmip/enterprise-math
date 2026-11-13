# D25/LIFT: rank-two residual-centralizer gauge orbits (author-side)
Date: 2026-10-28. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. No native CLAIM or original H0/B0 experiment is inferred.

## Exact new problem and inherited result
Earlier author-side results (this Draft PR) established, in an explicitly auxiliary semilinear matrix model modulo p^3, the normalized odd-square jet K=[B,A]=BA-AB. The prior trace-annihilator certificate Im(ad_A)=Z(A)^perp and its p^dimZ(A) source-marked B fibers are reused without recrediting. The NEW question is which of the admissible signed matrices K remain distinct after residual basis changes that leave the first even coefficient A fixed.

Let p be an odd prime, k=F_p, A in M_2(k). Define K_A={BA-AB : B in M_2(k)} and G_A=Z_GL2(k)(A), acting on K_A by K->gKg^{-1}. This residual action is not the same as a p-adically small first-jet gauge; no identification with the unknown native H0/B0 gauge group is asserted.

## Theorem: complete orbit classification
If A is nonscalar, |K_A|=p^2. Its G_A-orbits have exactly these numbers:
- A split with distinct k-eigenvalues: p+2.
- A with irreducible quadratic characteristic polynomial: p.
- A with one Jordan block (repeated eigenvalue): 2p-1.
For scalar A, K_A={0}, hence one orbit.

Proof for split distinct: In an ordered eigenbasis A=diag(a,b), a!=b, every admissible K= [[0,u],[v,0]] for u,v in k, and every such K is a commutator. G_A=diag(s,t), s,t!=0, acts by (u,v)->((s/t)u,(t/s)v). Its orbits are: the zero pair; upper-only nonzero; lower-only nonzero; one orbit for each uv=w in k* (p-1 choices). Total p+2. All nonzero orbits have size p-1. In particular det(K)=-uv merges three different orbits with zero determinant and is not a lossless signed observer there.

Proof for irreducible: Identify the marked k-vector space with F_{p^2}, with A=m_theta for theta outside k. Let tau(z)=z^p and m_x denote multiplication by x. Every k-endomorphism has a unique expression m_x+m_y tau. Since [m_y tau,m_theta]=m_{y(theta^p-theta)} tau, the commutator image consists exactly of K_y=m_y tau. The centralizer units are m_s, s!=0, and conjugate K_y to K_{s^{1-p}y}. The subgroup of factors s^{1-p} is precisely the norm-one group of F_{p^2}/k, of order p+1. For nonzero y, its orbit is determined exactly by Norm(y). As det(tau)=-1 (choose a trace-zero basis element), det(K_y)=-Norm(y). Hence determinant is a complete invariant in this case: one zero orbit and p-1 nonzero determinant orbits, each nonzero orbit of size p+1. Total p.

Proof for Jordan: In a Jordan basis A=aI+J with J=E12. All commutators have the shape K(u,v)=[[-v,u],[0,v]] with arbitrary u,v in k. Every g in G_A is s(I+cJ), s!=0, and directly conjugates K(u,v) to K(u+2cv,v). For each v!=0, the full range of u is one size-p orbit indexed by the SIGNED v, contributing p-1 orbits. For v=0, each u is fixed, contributing p singleton orbits. Total 2p-1. The determinant -v^2 forgets the sign of v and every v=0 upper entry u, so it is not complete.

These are exhaustive rational 2x2 nonscalar conjugacy types. The scalar case follows from [B,A]=0. QED.

## Exact observer and BRC information-preservation boundary
The theorem certifies one reduction ONLY under the declared population K_A and allowed operation G_A. Preserve each signed/ordered K and source-marked B until the actual residual stabilizer H and future observers are known. If H is smaller than G_A, the displayed orbits can split. If operations also change A, this fixed-A classification is inapplicable without a simultaneous-conjugacy certificate. The auxiliary finite-field matrix coordinate is not the Enterprise native six-dimensional Cell space; no original-class observer bridge or full-X6 claim is made.

For p=373, the PROVED (not exhaustively enumerated at that p) orbit counts are split=375, irreducible=373, Jordan=745 for 373^2=139129 admissible K values. Concrete distinct zero-determinant split witnesses K=E12 and K=E21 remain inequivalent when A=diag(0,1). For Jordan A=E12, K(0,1) and K(0,-1) have equal determinant but different signed v, hence are inequivalent. In the irreducible case A=[[0,2],[1,0]] is a valid p=373 representative because 2 is a nonsquare.

## Actual finite checks and next native discriminator
The author ran an exact Python standard-library checker covering p=3,5,7,11,13,19 and all three nonscalar types: 18 case families, all 2202 admissible K matrices, 41164 explicit centralizer conjugations, and 18 separate semilinear odd-square checks modulo 373^3. It checked explicit commutator preimages and equality of each predicted label fiber with one entire group orbit; verdict PASS. The all-odd-prime statement follows from the algebra above, NOT extrapolation from this finite scan. Local executed code SHA256=e29e0f8b679bb205490c8b20ea11726a43fcbf23b4d2f25ce921b517faef1211; local JSON result SHA256=82319d885d4d0aefb8537de4f3b409e793743e4d10668e148bc0975283048fa7.

Native support Issue #1559 must first identify the authentic same-original-class operator rank, first even coefficient A mod p, actual allowed residual basis group H, signed odd-square port K, Frobenius direction, and the target Delta_p-R_p interface. Only if rank two and an observer-preserving identification are proved can these auxiliary labels be used to test original-class gauge fidelity. No benchmark, native publication, admission, independent review, or Source task completion is claimed. UR V2 mathematics is not repeated; the original four-file 94687-byte SHA256=4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 bundle still needs byte-exact provenance recovery.
