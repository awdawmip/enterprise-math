# D25/LIFT — factorial and two-moment compression of the corrected Clausen middle-rank leakage

Date: 2026-10-26. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. This is not a native Source checkpoint, original-class CM experiment, or accepted all-target-prime congruence.

## Precise newly consumed question

The preceding, actually persisted corrected-jet p^4 bridge (research_notes/portable_direct/20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge.md; commit 0b3f941f6955911e30caa6da1270427b68807296) established the next-digit intermediate-rank contribution, but not its compact closed factorial kernel. With p=6m+1 prime >=7, corrected parameter family

\[
\widetilde b_n(x)=\frac{(-x)_n(-2x)_n}{(\frac12-3x)_n n!},\qquad u_{k,n}=[t^k]\widetilde b_n(m+t),
\]

the prior exact result is

\[
\frac1p\left(\frac{Q_p}{p^2}\right)_{\rm middle}
\equiv-\frac1{108}\sum_{j=m+1}^{2m}\sum_{\ell=1}^{j}
(6(j-\ell)+1)2^{-(j+p-\ell)}u_{1,j}u_{2,p-\ell}\pmod p.\tag{1}
\]

Here Q_p is the original *ordered signed* Clausen cutoff, not a nonnegative support count.

## Theorem E — explicit factorial sources in F_p

Set a_j=u_{1,j} for m<j<=2m, and h_l=u_{2,p-l} for 1<=l<=2m, all reduced modulo p. Then

\[
\boxed{a_j=(-1)^{m+j+1}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2}\pmod p,}\tag{2}
\]
\[
\boxed{h_\ell=\frac{2\,m!\,(2m)!\,((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!}\pmod p.}\tag{3}
\]

All factorial arguments in the denominators are <p. The hypergeometric ratios are

\[
\boxed{\frac{a_{j+1}}{a_j}=-\frac{(j-m)(2m-j)}{(j+1)^2}\quad(m<j<2m),}\tag{4}
\]
\[
\boxed{h_1=\frac2{(m+1)(2m+1)},\quad
\frac{h_{\ell+1}}{h_\ell}=
\frac{\ell^2}{(\ell+m+1)(\ell+2m+1)}\quad(1\le\ell<2m).}\tag{5}
\]

**Proof.** At x=m+t, the factor (-x)_j has a single zero -t at index m when m<j<=2m, while (-2x)_j is nonzero; removing the zero, and reducing denominator (1-p/2)_j j! to (j!)^2 modulo p, gives (2). For high rank n=p-l>2m, two zeros -t and -2t occur at indices m and 2m. Their product gives the exact leading jet

\[
u_{2,n}\equiv
2(-1)^m\frac{m!(2m)!(n-m-1)!(n-2m-1)!}{(n!)^2}\pmod p.
\]

Apply Wilson's factorial complement (p-1-k)! = (-1)^{k+1}/k! modulo p with k=l-1,l+m,l+2m, observing sign cancellation, to obtain (3). Ratios of consecutive factorial values give (4) and (5). QED.

## Theorem F — source-faithful O(p) two-moment readout

Define P_0=T_0=0 and for 1<=j<=2m, recursively in F_p,

\[
P_j=P_{j-1}+2^j h_j,\qquad T_j=T_{j-1}+j\,2^j h_j.\tag{6}
\]

Then the signed middle port has the exact **linear-time** finite-field expression

\[
\boxed{\frac1p\left(\frac{Q_p}{p^2}\right)_{\rm middle}
\equiv-\frac1{108}\sum_{j=m+1}^{2m}a_j\,2^{-j-1}
\big[(6j+1)P_j-6T_j\big]\pmod p.}\tag{7}
\]

**Proof.** Fermat gives 2^{-p}=2^{-1} modulo p. The inner signed weight in (1) is (6j+1)-6l. Thus
\[
\sum_{\ell=1}^j(6(j-\ell)+1)2^{-(j+p-\ell)}h_\ell
=2^{-j-1}((6j+1)P_j-6T_j)\pmod p.
\]
Substitution proves (7); (6) updates both exact future-relevant moments in O(1) work per rank. QED. Projecting to absolute values, boolean support, or P alone is **not** a proven information-preserving quotient, because the signed l-moment T is required by the future observer.

## Computation and interpretation

The accompanying Python stdlib verifier checks each factorized a_j and h_l against independently constructed corrected **rational** Taylor jets, verifies the O(p^2) signed kernel against (7), and independently isolates the p^3 middle/high contribution from original Pochhammer source coefficients modulo p^4. All **22** primes p=1 (mod 6), 7<=p<=211 passed. Middle/p residues mod p: p=7 ->4, p=13 ->2, p=19 ->2, p=31 ->9. Exact finite checks are author verification; generality comes from the proofs.

**BRC COMPOSE_APPLIED**, in the narrow finite arithmetic sense: a_j and h_l carry original rank, corrected denominator, Hasse-order and valuation provenance, while (P,T) preserve the actual signed future observer. No native BRC/Heartbeat X6 application or independent review is claimed. Prior p^4 bridge and its fixed-denominator predecessors are consumed as inputs, not recredited as new results.

**Next precise task:** seek a rational hypergeometric antidifference or WZ pair for the kernel in (7), while keeping both P,T and the fully corrected Clausen differential operator. Determine whether the endpoint can match the all-target-prime D25 LIFT residual, rather than assuming cancellation. Authentic original CM H_0/B_0, [X]U modulo p^2, Frobenius direction/normalization and kappa mapping are still missing, native CM NOT_RUN; D25/LIFT/JT2 remains OPEN. One new native continuation read this execution returned INVALID_ARGUMENT / CONTROL_QUOTA, so no new native winning CLAIM/authorized OPEN/checkpoint exists in this report. The maintenance conversation, frozen scientific pin and scheduler were not modified.
