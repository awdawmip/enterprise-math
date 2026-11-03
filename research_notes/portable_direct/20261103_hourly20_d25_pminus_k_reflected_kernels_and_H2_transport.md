# D25: pole-free p−k kernel reflection and exact 216 H2 carry transport

Date 2026-11-03. Author-side portable mathematical research, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is not a native Source checkpoint, Result or review. Project TASK_RESEARCH: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7 (verified taskbook blob 53a3ef039325534e3715add837f0eee332289984); frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. The source-input and protocol versions are distinct. Lane label: chatgpt-research-hourly-enterprise-math-20260923, not a verified platform execution identity.

## Theorem A: both original hypergeometric kernels have exact reflected valuation three

Let p≥5 be a prime and 1≤k≤p−1. Retain the original factorial-source coefficients

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5\,216^k},\qquad
c_k=\frac{(4k)!}{(k!)^4\,2304^k}.
\]

Write a=floor(2k/p)∈{0,1}, b=floor(3k/p)∈{0,1,2}, c=floor(4k/p)∈{0,1,2,3}. In this theorem a,b,c are integer quotient digits, not the original coefficients. Then

\[
v_p(b_k)+v_p(b_{p-k})=3,\qquad
v_p(c_k)+v_p(c_{p-k})=3.
\]

More strongly, the following p-adic units are given by explicit source-preserving rational cubic expressions:

\[
\boxed{\frac{b_kb_{p-k}}{p^3}\equiv
-\frac{(-1)^{a+b}\,b!(2-b)!}{36k^3}\pmod p,}
\]

\[
\boxed{\frac{c_kc_{p-k}}{p^3}\equiv
-\frac{(-1)^c\,c!(3-c)!}{576k^3}\pmod p.}
\]

The first kernel's successive open intervals (0,p/3), (p/3,p/2), (p/2,2p/3), (2p/3,p) have coefficients multiplying k^{-3} of −1/18,+1/36,−1/36,+1/18. The second kernel's intervals (0,p/4), (p/4,p/2), (p/2,3p/4), (3p/4,p) give −1/96,+1/288,−1/288,+1/96. The interval endpoints never contain integers k in this range because p≥5 and p is prime. Dividing the second unit by the first recovers the previously established three values 3/16, −1/16, 1/8 of h_kh_{p-k}, but now **each kernel's own p^3-normalized source** is explicit rather than only their ratio.

**Proof.** For 0≤q≤3 and 0≤s<p, p≥5, elementary factorial blocks yield

\[
(pq+s)!/p^q\equiv(-1)^q q!s!\pmod p
\]

(the left side is interpreted as an integer). For 1≤m<p, Wilson's complement gives

\[
(p-m)!\,(m-1)!\equiv(-1)^m\pmod p,
\quad m!(p-m)!\equiv(-1)^m m\pmod p.
\]

For j=2,3,4, write jk=pq_j+r_j with 1≤r_j<p. Under k→p−k, q_j becomes (j−1−q_j) and r_j becomes p−r_j. Thus v_p(b_kb_{p-k})=(1)+(2)=3 and v_p(c_kc_{p-k})=3. Multiplying the stripped factorial residues for b and using q_2!(1−q_2)!=1, q_3!(2−q_3)!, r_2r_3≡6k², k!(p−k)!≡(−1)^k k, and 216^{−p}≡216^{−1} yields the first boxed unit with its sign. For c use q_4!(3−q_4)!, r_4≡4k, 2304^{−p}≡2304^{−1}, and the fourth power of k!(p−k)! to obtain the second. All denominators are units because k≠0 mod p and p≥5. QED.

## Corollary B: original weighted reflection is polynomial and pole-free

Put B_k=(6k+1)b_k and C_k=(8k+1)c_k. For every integer k in the stated range, including any exceptional weighted indices (four distinct ports for primes p≥11),

\[
\frac{B_kB_{p-k}}{p^3}\equiv
(1-36k^2)\frac{b_kb_{p-k}}{p^3}\pmod p,
\]

\[
\frac{C_kC_{p-k}}{p^3}\equiv
(1-64k^2)\frac{c_kc_{p-k}}{p^3}\pmod p.
\]

These formulas do not invert 1−36k² or 1−64k². At an exceptional zero of a weight, the right side is zero; the earlier individual four-port normalized-unit theorem is needed to recover the extra digit. For mixed-source entries, the exact directed valuation table is

\[
v_p(b_kc_{p-k})=3+(a+b-c),\qquad
v_p(c_kb_{p-k})=3-(a+b-c).
\]

This gives a stratified 2×2 source matrix with independently retained directed valuations, while its unweighted determinant is exactly zero. In particular, a symmetric scalar reflected product is not a substitute for the directed sources in a WZ telescope.

## Theorem C: elementary exact transport of the H2 (valuation-two) signed 216 tail

For p=6r+1 prime (hence p≥7), isolate the original 216 signed high-band contribution

\[
H_2(p)=\sum_{k=3r+1}^{4r}(6k+1)b_k\in p^2\mathbf Z_p.
\]

Its normalized second-digit carry is a finite sum involving only factorials strictly below p:

\[
\boxed{
\frac{H_2(p)}{p^2}\equiv
\sum_{j=2r+1}^{3r}
(6j-1)\,216^{j-1}
\frac{((j-1)!)^5}{(2j-1)!\,(3j-p-1)!}
\pmod p.}
\]

**Proof.** Substitute k=p−j. The original k∈[3r+1,4r] becomes j∈[2r+1,3r] and the factorial Legendre digits for k are q_2=q_3=1, so v_p(b_k)=2. After stripping the two factors of p,

\[
\frac{b_{p-j}}{p^2}\equiv
\frac{(p-2j)!(2p-3j)!}{((p-j)!)^5}\,216^{-(p-j)}
\equiv-216^{j-1}
\frac{((j-1)!)^5}{(2j-1)!(3j-p-1)!}\pmod p.
\]

The first equality is mod p in p-adic units. The complement step uses 2j<p and 0<3j−p<p, and Fermat's theorem for 216. Finally 6(p−j)+1≡1−6j mod p, yielding the claimed plus sign. Every denominator factorial index lies in [0,p−1]. QED.

This is an explicit, independently computable high-index 216 contribution at exactly the divided second digit required for the LIFT residual. It preserves the old H2 original source and has r terms; it is a scientific subunit toward the low-half/Q3 cancellation, not a proof of its cancellation.

## Exact validation, observer, method and status

An executed Python integer checker used the original factorial p-free sources for b and c, tested both p−k reflection unit formulas, original signed weight identities and mixed valuations for every 1≤k<p over all 301 primes 5≤p≤2000: **276744 index checks, PASS**. It separately tested H2 transport for every 148 primes p=6r+1 in this range: **PASS**. For p=7,13,19,37,373, a separate factorial computation modulo p³ (not just the reduced formula) reproduced the H2 carry. The five exact (p, H2/p² mod p, H2 mod p³) observations are (7,5,245), (13,10,1690), (19,9,3249), (37,20,27380), (373,266,37008314). Finite checks are regression, while the boxed statements are supported by the displayed algebraic proofs. Project mathematical admission and independent review are pending.

BRC/information-fidelity scope: retain separate b/c factorial sources, the quotient-digit tuples, oriented k and p−k, and k^−3 units; pair readouts permit a pole-free algebraic observer but do not contain the full directional sum or second-digit weight-port information. The source coefficients remain unchanged. The accepted UR/CM0/SIMPLE/first digit are consumed but not revisited. No native 373 experiment is asserted.

**Next exact action.** Use the new H2/p² mod p finite factorial certificate as the high-index operand of a p-dependent two-index signed telescope against the verified 216 low half and Green signed prefix. At p=13,19,373 verify the signed carry *of the complete candidate* using original b_k and both directed endpoint terms; if the balance fails, retain the precise residual instead of promoting an unproved WZ transformation. In parallel keep the original \(\Delta_p-R_p\pmod p\) observer and frozen scalar equivalence intact. A finite scan alone is not LIFT closure.

Native state from 2026-11-03 direct em_status: Gateway 0.6.11, reviewed-code gate UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active quota 5/5. Previous recovery Issue #6637 contains an ACTIVE historical service session and neutral preserved staging, not present-current Source claim; Issue #6638 is a FAILED continuation request. No new CLAIM, open, Source checkpoint, freeze, Result or review is asserted. Control owner #1558 remains the existing remediation path. The next native step on changed authority is read exact recovery/status/continuation and reconcile existing effects, not borrowing maintenance conversation identity.