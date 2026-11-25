# PREFIX-1086 — Exact CT divergence null controls for global signed residual tails

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent continuation of PREFIX-1085; own session metadata recovered by r6-20261125-2050-recovery-read, original session MCP-f6d93209fc8e4c5bb2c3b44f69a47174, EM-DIRECT-780BBE / TASK_RESEARCH. Metadata recovery is not execution authorization. Owner read r6-20261125-2050-owner-read last observed RUNNING / NATIVE_RUNNER; no new CLAIM or shared task mutation.

Frozen scientific input: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full signed phase-paired Cell/port/ordered multiplicity carrier remains intact. CT and x are auxiliary joint observer variables, not spatial or heartbeat time coordinates.

Parent: 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md (sections 1–3). Also inherits PREFIX-1084 finite signed tail and its radial moment assumptions. This paper proves exact identities within that BRC-derived Laurent observer, conditional on the inherited native/observer correspondence. No new path enumeration, classical reference evaluation, numerical CT run, or independent review.

## 1. Null-observer controls rather than ordinary radial regression

Use parent notation: x=SB/36, y=1-x, a=M+2, b=Q-3, Q=k+u, M=m+r, k>=3, D_m(k)>0, r>=1. Let F=F_Q be the full six-axis orbit average of the parent four-term Newton carrier, with the same c=1/(8*36^6). Then D_M(Q)=c CT[w_Q F_Q] where w_Q=x^a y^b. On the unit character carrier x,y are nonnegative, F_Q is star-real, and CT is a positive normalized observation. All derivatives below are formal Laurent derivations, not physical time derivatives and not classical numerical reference propagation.

For the six Laurent variables z_i let E_i(z^v)=v_i z^v. CT E_i A=0 identically for any Laurent polynomial A. E_i reverses star parity. For any star-real rational-coefficient Laurent polynomial G_Q define the polynomial

    L_Q G = sum_i { x^2 y^2 E_i^2 G
       + xy[(a+2)y-(b+2)x] (E_i x)(E_i G) }.

This is the expansion of E_i(w_Q x^2 y^2 E_i G)/w_Q; the displayed polynomial is defined also where w_Q=0. The product rule gives the exact identity, without dividing at those points:

    w_Q L_Q G = sum_i E_i(w_Q x^2 y^2 E_i G).

Consequently for EVERY integer Q>=3,

    CT[w_Q L_Q G]=0.

This is stronger than a single global weighted mean constraint: subtracting any Q-dependent multiple of this control preserves every individual terminal bin and hence every grouped residual, every cutoff signed sum, every negative mass, and all their subsequent linear combinations in this declared observer family. It does not permit erasing a native branch, changing the blocked link, or substituting a new physical evolution. Six-axis averaging commutes with L_Q, since x and the sum over all six derivations are permutation invariant.

For star-real P,G, the constant-term product rule also gives

    CT[w_Q P L_Q G] = - sum_i CT[w_Q x^2 y^2 (E_i P)(E_i G)].

As E_i P is star-odd (pure imaginary on the unit carrier), the right side for P=G is nonnegative, equal to the weighted squared norm of its six derivatives. No sine, cosine, pi or external model is evaluated.

## 2. Strictly improving the existing orbit-averaged certificate

Put H_Q=L_Q F_Q, c_u=binom(u+r-1,r-1), and define the inner product <P,G>_U=sum_(u>=U)c_u CT[w_Q P_Q G_Q]. The sums below converge; see section 3. Set B=<1,1>, C=<F,F>, A=<F,H>, Z=<H,H>. If Z=0 set alpha=0 and C*=C; otherwise set

    alpha=A/Z, F*=F-alpha H, C*=C-A^2/Z.

These are rational quantities. By the preceding exact bin identity, F* represents precisely the same D_M(Q), for every Q>=3, even outside the cutoff used to choose alpha. Expanding the square proves C*>=0 and that alpha uniquely minimizes <F-tH,F-tH> when Z>0. The new bound is

    A_null = c sqrt(B C*)/D_m(k),
    N_tail(U) <= (A_null-S_U)/2,
    A_null <= A_orbit.

Here S_U is the exact signed tail of PREFIX-1084 and A_orbit=c sqrt(B C)/D_m(k). In particular all comparisons of squared absolute envelopes are exact rational comparisons. When C,Z>0 the squared improvement factor is 1-A^2/(CZ). This is not an assertion of a particular numerical improvement.

Strict improvement holds if F_Q is nonconstant for at least one u>=U: then A>0 by the weighted derivative identity, since a nonconstant Laurent polynomial has a nonzero E_i derivative, and the positive radial weight is positive almost everywhere. The exceptional sets x=0 and y=0 have measure zero (zero sets of nonzero real Laurent polynomials on the character carrier). For the inherited Stage46 carrier, each P_d=O(x), hence F_Q vanishes at a character point S=0 (choose opposite character pairs). Whenever D_M(Q) is nonzero, F_Q cannot be constant. The inherited eventual positive tail ensures such a bin for every finite U. Thus under the parent hypotheses the single-direction correction strictly improves the full orbit envelope for every fixed admissible parameter set. It preserves all original signed residual values: the improvement is entirely in the certificate, not a change of the mathematical residual.

This answers the proposed Gram-projection route with a zero-observer subspace. Ordinary projection onto radial polynomials alone does not prove exact preservation of every terminal bin; its discarded component requires an error payment. Here preservation is an algebraic CT identity before projection.

## 3. Finite rational reduction

Write F as the orbit average of sum_(d=0)^3 (-1)^d binom(Q,d) x^d y^e P_d, e=3-d. Parent P_d are Laurent polynomials rational over the paired carrier, with at least two remaining S,B factors in total. For f=x^d y^e P and J=d y-e x, the polynomial contribution to L_Q f divided by the explicit factor x^d y^e is the sum over i of

    x^2 y^2 E_i^2 P
    +2xy J (E_i x)(E_i P)
    +[xy J E_i^2 x
       +(d(d-1)y^2-2de xy+e(e-1)x^2)(E_i x)^2] P
    +[(a+2)y-(b+2)x] [xy(E_i x)(E_i P)+J(E_i x)^2 P].

This is a polynomial identity; d or e equal to zero causes no division. The only new Q factor is -Q x inside the final bracket. Since Q binom(Q,d)=d binom(Q,d)+(d+1)binom(Q,d+1), H is a finite combination of terms binom(Q,t) x^j y^e R where 0<=t<=4, j>=t, e>=0, and R is a fixed rational Laurent polynomial at fixed M. F has the same form with t<=3.

Therefore A and Z (and C) use the same parent finite L(P,i,q,h,V) tail transform:
- multiply pairs of basis terms; expand binom(Q,t)binom(Q,t') by the parent subset-union identity (union size <=8);
- expand binom(k+u,h) by Vandermonde into binom(k,h-j)binom(u,j);
- apply the exact multiplicity shift and parent finite signed negative-binomial tail identity to each fixed Laurent product.
For U>=9 the shifted V=U-j>=1. Smaller U is handled by a finite initial segment plus the U=9 tail. The base exponent after a shift satisfies i-(r+j)>=m+2 because the explicit x powers dominate the binomial orders. All y exponents in the resulting L are nonnegative when k>=3. No infinite numerical scan is needed. Products retain all six axes until CT; no classical reference arithmetic enters.

For justification of convergence, on the unit character carrier E_i x=O(sqrt(x)), E_i^2 x=O(1), P_d=O(x), E_i P_d=O(sqrt(x)), E_i^2 P_d=O(1). These follow from x=SB/36, S,B bounded, B=star S, and the remaining S,B degree >=2. Differentiating x^d y^e yields bounds |E_i f|<=const x^(d+1/2) and |E_i^2 f|<=const x^d (with zero-power cases interpreted directly). Hence |H_Q|<=const sum_d binom(Q,d) x^(d+2)(1+Qx). With the inherited fixed-order zero-edge estimate CT[x^i y^Q]=O_i(Q^(-i-1)), B=O(U^(-m-3)), C=O(U^(-m-5)), Z=O(U^(-m-7)), A finite by Cauchy-Schwarz. This also justifies the inner products and finite summation. For the individual expanded Laurent terms the explicit x powers and shifted tail order give absolute integrability even without the sharper combined derivative bound.

## 4. Multidirection and block refinement

For any finite family of admissible controls H_i=L_Q G_i with finite norm, build the rational Gram matrix K_ij=<H_i,H_j>, vector v_i=<F,H_i>. v is in the range of K: any kernel combination of H_i has zero norm and is orthogonal to F. Solve K beta=v on an independent basis, or any consistent rational solution. The resulting squared norm is C-v^T beta. It cannot increase as controls are added, since the old minimizer is feasible in the larger subspace. Every terminal bin still has its exact original value, even when coefficients are chosen from aggregate information. This includes iterated controls G=F*, or distinct choices of Laurent G with sufficient x-power for summability. All six-axis symmetries may be retained.

For disjoint consecutive blocks, use separate optimal coefficients and sum each block's absolute envelope. The old global optimum remains feasible in every block; Cauchy-Schwarz across blocks shows the optimized block sum is no larger than the global optimized envelope. This supplies two independent monotone refinement directions (null-space enlargement and block subdivision). It does not guarantee a specific convergence rate or cheap execution.

## 5. Current verification and next problem

Full hand-checkable proof above: formal Laurent derivation/product rule, star parity, positivity, rational Gram minimization, explicit finite expansion and tail integrability. No new numerical CT values, no claimed acceleration, no native kernel re-execution, no external classical comparison. The first exact implementation should reuse the parent's fixed (m,r,k)=(0,1,115), U=7,20,120, compare A^2/(CZ) and the orbit bound from the already-published evidence, then check Gram products against direct finite bins. The two additional directions to test are G=F* and independent derivative-generated controls; optimize cost only after actual measured values. Still open: real last spectral boundary and multiplicity certification, explicit uniform positivity constants, inexpensive global small-error certificate, and how much of the non-observer variance the null controls actually remove in those cases.
