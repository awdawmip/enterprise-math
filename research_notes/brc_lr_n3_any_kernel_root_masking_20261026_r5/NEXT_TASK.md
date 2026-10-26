# Next exact research unit: sharp parameter region for N=3 root masking

Parent/source: PROOF.md, exact author-level theorem. Frozen inputs: global main@d1dd5aa7e590ab3dec37f1f4eb2851770df489c8 and EM main@0929779757189d61ebfa1e815d8c5a31fd95f6df. Not native Result/Driver accepted.

Original model: Q(R|a)=(alpha,1-2alpha,alpha); Q(R|b)=(beta,1-2beta,beta); R=(1/2,1,3/2); P(R|h)=R Q(R|h); root histories a,b each Q=P=1/2 and L1=1. Final Q kernel mu_r has positive support Y and mean r; P kernel is Y mu_r(Y)/r. All stops/decisions through N=3 allowed, and O=(e_P,e_Q,E_P tau,E_Q tau).

Completed: For 0<alpha<=beta<1/2, beta<=3alpha, 3beta-alpha<=1 the O-polytopes of full-history and (time,LR)-only randomized strategies agree for ALL coherent terminal kernels. A strictly positive rational kernel violating the predecessor's convex order is exhibited and checked (call gap 27/224), hence convex order is not necessary.

OPEN: Is this alpha,beta region SHARP for universal masking? For exact rational alpha,beta outside it, either construct a strictly positive mean-preserving finite terminal kernel and signed rational (A,B,C,D) with V_LR>V_full, or prove a wider sufficient region. Use phi(r)=min(H(r),C r+D+E_mu_r H(Y)), H(r)=min(A r,B), G=2 phi(1)-phi(1/2)-phi(3/2)>=-2(H(1)-phi(1)), d_a=d0+alpha G, d_b=d0+beta G, and the exact root envelopes from PROOF.md. Existence of an abstract G does NOT ensure realizability by a coherent terminal kernel. Report source, exact certificates and finite-search completeness scope.

Secondary route: N>=4 when terminal kernel depends on hidden history, no longer only current LR. Preserve BRC path-residual and P000/native-transfer boundary. Do not reuse an earlier active owner/CLAIM or claim independent Driver review.
