# D25: original-weight 216/2304 reflected transfer and four exceptional ports

Date: 2026-11-03 (+08). TASK_RESEARCH author-side portable mathematics. Scope: original 216 and 2304 hypergeometric kernels and original signed weights; under task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / publication TP2-B6F4FC938FF94941C1B7 / frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3. Separate logical Research lane chatgpt-research-hourly-enterprise-math-20260923, not maintenance chatgpt-hourly-enterprise-math-20260921. HAND_PROVED / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Consumes the immediately preceding author proof in enterprise-math@58dc537391b4bd1f8e2e585bdef7714c5cfdb8e2: for p>=5, h_kh_(p-k)=tau_p(k)(1+pE_p(k)) mod p², with fully defined three-stratum tau and Fermat-quotient/harmonic E. Those definitions are reused here; no re-proving or re-registering of an old result.

## Theorem: exact weighted source ports and regular second-order transfer

For p>=11 prime, 1<=k<p, put

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5\,216^k},\quad
c_k=\frac{(4k)!}{(k!)^4\,2304^k},\quad
g_k=\frac{(8k+1)c_k}{(6k+1)b_k}.
\]

The exact rational identity

\[
g_kg_{p-k}=h_kh_{p-k}\frac{(8k+1)(8(p-k)+1)}{(6k+1)(6(p-k)+1)}
\]

preserves original weights, source ordering and the k↔p-k pairing. Introduce distinct exceptional residues

\[
Z_p=\{8^{-1},-8^{-1}\}\subset\mathbb F_p^\times,\qquad
P_p=\{6^{-1},-6^{-1}\}\subset\mathbb F_p^\times.
\]

1. For k mod p in Z_p, the *weighted reflected ratio* has exact valuation v_p(g_k g_(p-k))=+1.
2. For k mod p in P_p, its valuation is -1.
3. For the remaining p-5 nonzero residues, both numerator/denominator factors are p-units. Define N=1-64k², D=1-36k², and \(\Gamma_p(k)=N/D\). Then

\[
\boxed{
g_kg_{p-k}\equiv\tau_p(k)\Gamma_p(k)
\left[1+p\left(E_p(k)
+\frac{8(8k+1)}{1-64k^2}
-\frac{6(6k+1)}{1-36k^2}\right)\right]\pmod{p^2}.
}
\]

All regular-case denominators are p-units. The formula supplies the exact second-order p-adic weighted-reflection observer demanded by the original (6k+1)/(8k+1) comparison.

## Proof

The exact identity follows from the definition g_k=h_k(8k+1)/(6k+1). The previously proved h_kh_(p-k) is a p-adic unit for every index.

Modulo p, numerator zeros occur exactly at 8k=±1, and denominator zeros at 6k=±1. The two sets cannot overlap for p>=11: overlap would imply 8=±6 mod p, hence p|2 or p|14. Within each exceptional set, precisely one of the two weighted factors is p-divisible. Since every positive weighted factor lies between 1 and 8(p-1)+1<p² for p>=11, its valuation is exactly one. This proves assertions 1 and 2, and also establishes exactly four distinct exceptional source indices.

For regular indices, expand the exact paired weights:

\[
(8k+1)(8(p-k)+1)=N+8p(8k+1),
\]
\[
(6k+1)(6(p-k)+1)=D+6p(6k+1).
\]

Invert the denominator in Z_p to first order, obtaining

\[
\frac{N+8p(8k+1)}{D+6p(6k+1)}
\equiv\frac ND\left[1+p\left(\frac{8(8k+1)}N-\frac{6(6k+1)}D\right)\right]\pmod{p^2}.
\]

Multiplication by the proved h_kh_(p-k)=tau_p(k)[1+pE_p(k)] yields the boxed result. QED.

## Exact test observations

An independent V8 BigInt calculation in this run constructed original p-stripped factorial-unit products, multiplied by the *unmodified* paired weighted factors, and compared the regular formula for all regular indices at p=13,19,373. It also counted precisely two zero-ports and two pole-ports per prime. All checks PASS. Port sets are:

- p=13: Z={5,8}, P={2,11}; regular k=1 gives g_1 g_12 = 7 mod 169.
- p=19: Z={7,12}, P={3,16}; regular k=1 gives g_1 g_18 = 59 mod 361.
- p=373: Z={140,233}, P={62,311}; regular k=1 gives g_1 g_372 = 3735 mod 139129.

The four exceptional ports require exact numerator/denominator p-power bookkeeping rather than inversion modulo p². This is a source- and operation-scoped information-fidelity requirement; the old three-class mod-p kernel observer and its harmonic lift alone do not encode the original-weight singularities.

## Frontier

Mother goal still open: Delta_p-R_p=0 mod p, equivalent under the frozen scalar bridge to W216(p-1)=p mod p³ for p mod24 in {13,19}. The sibling source enterprise-math@90bc3567d93d82323e9becf477d20a3e81df6e50 already discharged the 2304 Q4 tail by the published Guo-Zudilin theorem.

Next exact scientific unit: make a terminating p-dependent two-index 216/2304 weighted telescope respecting all **four** exceptional weight ports, the three factorial-unit strata, the p² harmonic correction, inclusive p-1 cutoff and previously derived terminal -2p³ mod p⁴. Test a candidate at p=13,19,373 before any universal claim. Alternative path is the remaining 216 low-half/Q3 signed cancellation. Do not redo the scalar 301-prime comparison or 2304 Q4 proof.

Native gateway status inherited from fresh read on 2026-11-03T07:23:51Z: 0.6.11 / UPSTREAM_CODE_REVIEW_REQUIRED / research_authority_granted=false / executor_binding_configured=false / quota 5 of 5. Historical recovery #6637, failed continuation #6638, control support #1558, native H0/B0 support #1559 unchanged. This work creates no native claim, open, checkpoint, Result or mathematical admission.
