# PREFIX-1087 — Complete divergence control space and the irreducible single-envelope floor

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Continuation of PREFIX-1086, not a numerical Gram benchmark. Original own research registration r6-20261123-2358-session-start-own-v1 recovered SUCCEEDED, EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Current owner query r6-20261125-2150-owner-read last observed RUNNING; no CLAIM or shared Task mutation. Registration readback is not execution authority.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve original full signed phase-paired Cell/port/ordered multiplicity carrier. All character variables below are auxiliary CT observation variables, not native spatial or time coordinates. The inherited observer correspondence and finite norm estimates are conditional premises, not revalidated native dynamics.

Parents:
- 855e604a7ddd689e9aac5b155d9c5db1edc41c6c:research_notes/portable_direct/2026-11-25_r6_prefix1086_ct_divergence_null_controls.md
- 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md
- ba684dc121d63bef952982f17c35aee8e356475b:research_notes/portable_direct/2026-11-25_r6_prefix1084_newton_global_tail_certificate.md

## 1. Enlarge scalar-gradient controls to independent six-axis divergence controls

Fix m>=0,r>=1,k>=3,U>=7, M=m+r, D_m(k)>0. In the parent notation x=SB/36, y=1-x, a=M+2, b=Q-3, w_Q=x^a y^b, c=1/(8*36^6), Q=k+u. The full orbit carrier F_Q is a real rational Laurent polynomial, inversion-even (z maps to z^{-1}) and S6 invariant. D_M(Q)=c CT[w_Q F_Q]. Let E_i z^v=v_i z^v. For any six rational-coefficient star-odd Laurent polynomials V_i (V_i(z^{-1})=-V_i(z)), define

    T_Q(V) = sum_i [x^2 y^2 E_i V_i
                  + xy ((a+2)y-(b+2)x) (E_i x) V_i].

This is a star-even rational Laurent polynomial. By the exact product rule,

    w_Q T_Q(V)=sum_i E_i(w_Q x^2 y^2 V_i),
    CT[w_Q T_Q(V)]=0.

It includes the scalar-gradient family of PREFIX-1086 by V_i=E_i G. Independent V_i remove the restriction that the vector be a gradient. A rational basis is given by one coordinate V_i=z^v-z^{-v} with other coordinates zero, for integer six-tuples v. Its permutation average remains null and preserves S6 invariance if desired. This is an algebraic identity at every applicable bin, including points where w_Q vanishes, with no division in the implementation. It is an auxiliary observer control, not permission to erase a native relation.

## 2. Completeness of the enlarged family at each fixed bin

Use the parent's positive unit-character Haar realization only as a proof tool. Let H_Q be the real inversion-even L2 space for the finite measure w_Q dHaar. The closure of the real linear span of T_Q(V) in H_Q equals the entire mean-zero subspace. Rational finite combinations are dense in that span as well.

Proof. First establish connectedness of the regular region Omega={0<x<1} in the six-character torus. For S=sum z_i, the derivative of the two real components of S has rank 2 except when all six characters are collinear as vectors in C. Thus regular points of S=0 constitute a smooth real dimension-4 manifold; the rank-deficient points at S=0 are among the finitely many circles z_i=sign_i z_1 with three plus and three minus signs. Equality x=1 in the triangle inequality holds exactly when all six characters are equal, a dimension-1 circle. These sets have real codimension at least 2. More explicitly, in the universal-cover coordinate charts, their lifts have countably many smooth parametrization patches of dimension at most 4. For any endpoint outside the lifts, the set of intermediate points whose straight segment from that endpoint meets a lifted bad patch lies in its cone (a countable union of locally Lipschitz images of dimension at most 5), hence has six-dimensional measure zero. For two chosen lifts of endpoints in Omega, select an intermediate point outside both bad cones. The two segments project to a path in Omega. Therefore Omega is connected and its complement has Haar measure zero. This argument does not evaluate any classical reference function or change P000.

Suppose h in H_Q is orthogonal to all T_Q(V). On Omega h is locally integrable, because w_Q is bounded below on compact subsets. Write A_Q=w_Q x^2 y^2, positive on Omega. Let phi be a real smooth compactly supported odd test function on Omega (odd under simultaneous inversion of all characters). The function phi/A_Q extends by zero to a smooth odd function on the torus, because its support is compact in Omega. Approximate this quotient in C^1 by odd real finite Fourier polynomials (e.g. smooth Fourier approximation), and their finitely many real sine-basis coefficients by rationals. Equivalently the approximants, after a fixed imaginary scalar, are rational star-odd Laurent polynomials V_i. In local angular coordinates E_i=(1/i)partial_i, so multiplying the odd real approximants by i makes E_i V_i the real derivative. The displayed polynomial formula for T_Q implies convergence in weighted L2 for fixed Q: all coefficients x,y,E_i x are bounded and the approximants converge in C^1. The limiting control equals (partial_i phi)/w_Q on Omega, zero off the compact support; equality in the weighted L2 space is enough. Orthogonality now gives integral h partial_i phi dHaar=0.

For even test functions the same integral vanishes by inversion parity (h even, derivative odd). Decomposing arbitrary compactly supported tests into even and odd parts proves all distributional derivatives of h vanish on Omega. A locally integrable function with zero distributional gradient is almost everywhere constant on each connected component (local convolution gives constants on smaller charts, which agree on overlaps). Omega is connected, and its complement is null. Thus h is constant in H_Q. Constants are orthogonal to every control by section 1. The Hilbert-space orthogonal-complement identity proves the asserted density. Averaging a converging finite control combination over S6 proves the corresponding result in the permutation-invariant subspace. The scalar-gradient-only density is NOT established by this proof; the enlarged independent divergence family is essential to this argument.

Set b_Q=CT[w_Q]>0 and mu_Q=CT[w_Q F_Q]/b_Q. The exact infimum of CT[w_Q(F_Q-T_Q(V))^2] over finite rational controls is b_Q mu_Q^2. Indeed the difference F_Q-mu_Q has mean zero and can be approximated arbitrarily closely; the mean is unchanged and orthogonal to the zero-mean component. This is an existence/convergence theorem, not a bound on the number of basis modes required.

## 3. Infinite joint tail: exact limit of Gram optimization and its floor

Let c_u=binom(u+r-1,r-1), b_u=c_u b_(k+u), mu_u=mu_(k+u). Parent B=sum b_u and C=sum c_u CT[w_Q F_Q^2] are finite. Define

    C_min = sum_(u>=U) b_u mu_u^2 <= C,
    L = sum_(u>=U) b_u |mu_u| <= sqrt(B C_min).

Every pointwise-bin-null correction has squared norm at least C_min by the weighted variance identity at each bin. Conversely choose a finite initial set of bins, make independent finite divergence corrections in each, and leave the remaining tail unchanged. The uncorrected excess norm is bounded by the original C tail, tending to zero. The fixed-bin approximation theorem lets the finite corrections reduce the remaining excess arbitrarily. Therefore the infimum over finite-support-in-u rational divergence controls is exactly C_min. These supports are coefficient selectors in an auxiliary certificate, not changes to the BRC evolution. Such controls have finite rational Gram data; for finite support compute their CT contributions directly, and the unmodified global C by the inherited finite tail identity.

A single joint Cauchy-Schwarz envelope therefore has the exact optimal limit

    A_floor = c sqrt(B C_min)/D_m(k).

The true absolute mass is A_true=c L/D_m(k). With the probability weights pi_u=b_u/B, the squared gap is

    A_floor^2 - A_true^2
      = (c B / D_m(k))^2 Var_pi(|mu_u|).

In particular equality occurs if and only if |mu_u| is constant on the tail bins. If the means have different absolute magnitudes, enlarging the null family alone cannot attain the exact absolute mass under a single global Cauchy-Schwarz envelope. This separates character-wise invisible variance (removable) from inter-bin magnitude variation (requires a different outer certificate). It does not assume a particular nonzero gap for the actual Stage46 numerical inputs.

## 4. Combined block refinement approaches the exact negative mass

Partition into the first N singleton bins and one infinite final block. On each singleton use the preceding finite Gram approximation. The exact optimal singleton envelope is c b_u |mu_u|/D_m(k); its actual finite approximation can be made arbitrarily close. Keep the original parent envelope for the remaining infinite tail: c sqrt(B_(U+N) C_(U+N))/D_m(k), which tends to zero by inherited convergence. Therefore, over such finite partitions and finite rational divergence controls, the infimum of the combined absolute envelopes is exactly A_true. The envelope never falls below A_true because each bin value is unchanged and Cauchy-Schwarz is valid. Since the exact signed tail S_U is unchanged, the corresponding infimum of (envelope-S_U)/2 is the actual negative mass.

This is a constructive-existence result: for any positive target excess choose N so the explicit inherited rational squared tail bound is small enough, then enumerate finite rational divergence bases at each selected bin and solve the finite Gram systems. The singleton squared target can be checked using the exact CT mean and rational comparison. Completeness proves termination for a positive tolerance under the inherited finite norm and exact arithmetic premises. This is not a speed claim: calculating every singleton mean itself may already solve the desired finite part; high-degree modes and dense Gram systems can be expensive. The theorem identifies where a low-cost method must improve: shared low-dimensional controls for a range of bins, and block selection based on the variance of their mean magnitudes. For a block I the exact floor uses B_I C_min,I; splitting reduces the gap, and finite final-tail control guarantees convergence.

## 5. Evidence and next step

Written proof checked by: Laurent product rule, star parity, rank and codimension of zero sets, elementary path connectivity, test-function density and orthogonal complement, weighted variance identity, and inherited finite-norm convergence. No new numerical CT/Gram evaluation, classical reference arithmetic, native-path re-enumeration, formal checker or independent review. In particular the requested numerical benchmark at (m,r,k)=(0,1,115), U=7,20,120 from PREFIX-1086 is still open. The present advance changes the theory of what a certificate can attain, not its measured cost or physical interpretation.

Next: compute a small finite subset of the independent Laurent vector controls (start with low-degree pair-symmetric monomials) at the fixed Stage46 benchmark, compare with scalar-gradient H=L F and the existing orbit certificate, and isolate the cost of reducing within-bin variance versus the inter-bin floor. Preserve real last spectral boundary, zero multiplicity and explicit positivity threshold as separate open problems.
