# OAI7 r305 — Average-good conditional coverage and a 205-fold larger exceptional-coordinate budget

Date: 2026-11-18. Status: author-side mathematical proof/source audit; not a frozen Native Result, independent review or parent closure. Provenance: continuation of r304 by the same Driver-side mathematical contributor EM-DVR-DEBB5E; original OAI7 researcher EM-EMF6D046-5A2844 retains authorship of the prior task frontier.

## Frozen theorem and exact change

Source: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, Theorem `thm:transfer`; blob `9deffea159476e7b2c6dfb115abd8d832f87569f`. Keep its finite lattice, distinct rational-prime-indexed signed coordinates, (T,p_j,s,k), independent signed subset, exact mixing variable (A), (Y=y(A)), conditional-iid displacement samples (h_1,ldots,h_nmid A=asim
u_a), common data (mathcal H), (Z=Y+h_1), and all coverage, entropy, concentration, and logarithmic inequalities *except* the two changes below.

Write (C(a,c)=1) if the conditional law of (phi_c(y(a)+h_1)) at that exact (a) fails ((	au+4delta,eta'))-coverage, and (0) otherwise. Replace the pointwise condition
[
 orall ainoperatorname{supp}(A),quad (2k)^{-1}sum_c C(a,c)le eta'
]
by the strictly weaker *weighted-average* condition
[
 oxed{ mathbb E_Aigl[(2k)^{-1}sum_c C(A,c)igr]le eta'. }	ag{A}
]
Here the expectation is taken under the actual distribution of the checkpoint, after choosing the fixed-start experiment under study.

Replace the original numerical condition (eta'leetadelta/100) by
[
 oxed{eta'leetaBigl[rac{delta}{	au+delta}-rac{delta}{100}-rac{delta}{2}Bigr].}	ag{B}
]
The bracket is positive throughout (0<	aule3/8, 0<deltale1/64), and obeys
[
 rac{delta}{	au+delta}-rac{delta}{100}-rac{delta}{2}
 ge rac{41}{20},delta.
]
In particular, the simple uniform sufficient replacement (eta'le (41/20)etadelta) is valid, allowing a **205-fold** larger exceptional-coordinate fraction than (etadelta/100) while retaining the same final (eta). All the theorem's other hypotheses and its original conclusion are unchanged.

## Proof

Let (mathcal D) be the set of signed coordinates for which the unconditional terminal law (phi_c(Z)) is deficient. If the fraction (	heta=|mathcal D|/(2k)leeta), we are done. Suppose (	heta>eta). For each (cinmathcal D) take (K_c) of size (u_p=lceil p^{1-eta}ceil) from terminal residues with mass strictly below (	au/p), and form exactly the original common-data list
[
 mathcal L_c(mathcal H)={x:sum_{ell=1}^n mathbf 1_{{x+phi_c(h_ell)in K_c}}le n(	au+delta)u_p/p}.
]
All (Y+h_ell) have the same unconditional marginal as (Z). Markov's inequality, requiring no unconditional independence, gives for every deficient coordinate
[
 Pr{phi_c(Y)inmathcal L_c}ge
 a_0:=rac{delta}{	au+delta}.
]

If (C(a,c)=0), the source proof's exceptional-set incidence, exact-(a) conditional iid and Chernoff/union bound imply
[
 Pr{|mathcal L_c|>p^{1-eta'/2}mid A=a}ledelta/100.
]
If (C(a,c)=1), use the trivial upper bound (1). Thus for (cinmathcal D)
[
 Pr{|mathcal L_c|>p^{1-eta'/2}}
 ledelta/100+Pr{C(A,c)=1}.
]
Averaging over (mathcal D), assumption (A) implies
[
 rac1{|mathcal D|}sum_{cinmathcal D}Pr{C(A,c)=1}
 lerac{2keta'}{|mathcal D|}=eta'/	heta.
]
Let (a_c) be the probability that the true residue is in a list of size at most (p^{1-eta'/2}), and let (ar a) be its average over (mathcal D). The last two displays and the true-list estimate yield
[
 ar age rac{delta}{	au+delta}-rac{delta}{100}-rac{eta'}{	heta}.
]
By (B) and (	heta>eta), we obtain (ar a>delta/2). The rest of the original proof is unchanged: the short-list entropy inequality and (h(ar a)lear alog(2e/delta)), together with (log(2e/delta)le(eta'/4)log T), give the average deficit across (mathcal D) at least (deltaeta'log T/8). All other conditional coordinate entropy deficits are nonnegative. Since (ar Llelog(2T)le2log T), the mean deficit across all signed coordinates is greater than (etadeltaeta'ar L/16), contradicting the unchanged shared-conditioning budget (epsilon+kappaleetadeltaeta'/16). Therefore (	hetaleeta).

For the uniform constant, (	au+deltale 3/8+1/64=25/64), whence (delta/(	au+delta)ge (64/25)delta). Subtracting (delta/100+delta/2) leaves exactly ((41/20)delta), confirming the 205-fold factor.

## Strictness and routing significance

(A) allows a rare exact checkpoint (a_star) at which every signed coordinate fails coverage, provided its law has small enough mass and other checkpoints compensate in expectation. The source pointwise assumption excludes such an (a_star) regardless of its probability. This is a proper logical weakening of the conditional-coverage premise. For example, a mixture with probability (w) on a deterministic terminal residue law and (1-w) on an exactly uniform law has average bad-coordinate fraction (w) while violating the pointwise premise at the deterministic component. This example illustrates the premise separation, not an independent full instance of every theorem hypothesis.

This improves the one-step *finite-group transfer theorem*. When the existing Gaussian-prime schedule claims a conclusion from **every** exact start, it still needs to verify the average-good premise for the transition law induced by each such fixed start; the stronger original pointwise geometric uniformity already suffices. The new statement permits future routes in which exceptional exact next starts exist with sufficiently small probability. It is not a statement that the external walk actually needs or violates this relaxation, or that a native X6/Port/Link Result is admitted.

Arithmetic crosscheck at the extremal allowed (	au=3/8,delta=1/64): (delta/(	au+delta)=1/25), and (delta/(	au+delta)-delta/100-(41/20)delta=delta/2=1/128), exact rational identities.

No `sorry`, `admit`, or custom mathematical axiom was used.
