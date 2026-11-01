# D25/LIFT — third-digit Green/mirror ratio with a necessary cyclotomic carry

2026-10-31; TASK_RESEARCH logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`, distinct from maintenance. Publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. P000 ACTIVE unchanged. **AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**; no canonical Result or native source checkpoint.

## Reused exact inputs and derived theorem

For p=6l+1 prime >=7, keep original a_n=binom(2n,n)^2 binom(3n,n)/216^n, Green terminal Gamma_l=(-1)^l/[18 binom(p-1,l)binom(p-1,2l)], and original mirror M_p=-a_(p-1)/p^3. Put Q_p(a)=(a^(p-1)-1)/p, q=Q_p(2), Q=Q_p(216), A=H_l+H_(2l), B=H_l^(2)+H_(2l)^(2), D=q-13/2.

Already established by previous same-lane work:
- EM \`cd0d692a5510dddcc42991b056ed032933e0b164\`: 18Gamma_l=1+pA+p^2(A^2+B)/2 (mod p^3) by a Pfaff–Saalschütz binomial product.
- EM \`9b72fd1afead2a4c5ad441f5398ec87af36821fd\`: M_p=1+p(13/2-Q)+p^2(115/4-13Q/2+Q^2) (mod p^3).
- EM \`484b05f619e5cd52bc04b57b8e5e7c07a52ad385\`: the new cyclotomic first-digit theorem A=q-Q (mod p). These inputs are consumed, not re-attributed.

Thus the exact p-local **carry**
\[
\mathcal C_p=(A-q+Q)/p\in\mathbb Z_{(p)}
\]
is well-defined, and for every prime p=6l+1 >=7:
\[
\boxed{\frac{18\Gamma_l}{M_p}\equiv
1+pD+p^2\left[\mathcal C_p+
\frac{q^2-13q+27+B-Q^2}{2}\right]\pmod{p^3}.}
\tag{1}
\]

**Proof.** Write b=13/2-Q, v=115/4-13Q/2+Q^2, u=(A^2+B)/2. Dividing the preceding two **p-adic unit** series gives
\[
18\Gamma_l/M_p=1+p(A-b)+p^2(u-Ab+b^2-v)\pmod{p^3}.
\]
Since A=q-Q+pC_p exactly, A-b=D+pC_p. In the p^2 coefficient reduce A to q-Q modulo p; exact algebra gives
\[
u-Ab+b^2-v\equiv(q^2-13q+27+B-Q^2)/2\pmod p.
\]
Insert both expressions to prove (1). All denominators are p-units for p>=7. Notice that using A≡q-Q one precision digit too early discards **exactly p^2 C_p**. The first-digit shared original-216 Fermat quotient cancels from D, but the next digit needs C_p and B. No denominator replacement or Green/R port collapse is licensed.

## Reproducible executed check

Actual executed Python standard-library program \`d25_green_mirror_third_digit_bridge_check_20261031.py\` imports the previous byte-verified first-digit checker; evaluates Gamma from exact binomial products, M independently from the p-stripped original factorial formula modulo p^3; verifies (1) for every one of 207 primes p=6l+1 <=3000. It separately checks M from the original unstripped integer binomial coefficients for p=7,13,19,37,67,283,373. All PASS, marker \`PASS_D25_THIRD_DIGIT_GREEN_MIRROR_RATIO 207 primes\`.

For p=373:
\[
(q,Q,B,C_p,D)\equiv(204,23,298,328,11)\pmod{373},
\]
\[
(18\Gamma_{62},M_{373},18\Gamma_{62}/M_{373})
\equiv(23023799,21211019,1117136)\pmod{373^3}.
\]
The p^2 coefficient of the ratio, with the **full mod-p^2 lift of D** retained, is 312 mod373. This is an exact source-observer certificate, not a universal original D25 cancellation.

**BRC actual reuse: COMPOSE_APPLIED.** The signed p-adic carrier retains p, original 216, original indices/weight, Gamma and mirror port identity, valuations, q/Q, A/B and actual carry C_p. Low-precision scalar coincidence is not equivalence under next-digit operations. External p-adic result; no native P000 X6 transfer.

**Open:** Frozen original A_p≡p (mod p^3) for p mod24 in {13,19}, and the original four-port first-jet/Green/integer-carry/signed-R joint cancellation. Next: seek a single finite WZ/CM/adjoint identity joining these carry ports to the low/middle signed 216 strata and preserving separate Green scalar/log-residue and signed R, with p=19,67,373 as nonzero boundary anchors.

Gateway 0.6.11 during this research run: research_authority_granted=false, executor_binding_configured=false, active_jobs 5/5, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Native session/CLAIM/open/checkpoint/admission not asserted; support path #1558 unchanged; maintenance identity, protected old staging and scheduling unchanged.
