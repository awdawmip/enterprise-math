# D25 / SECOND-DIGIT-LIFT — p≡5 mod8 beta terminal seed and separately signed high/low clipped port

Date: 2026-11-01 11:00 Asia/Hong_Kong. **TASK_RESEARCH / AUTHOR-SIDE EXACT PROOF / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.**

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** is unchanged. Ordinary Research logical conversation: **chatgpt-research-onhour-enterprise-math-20260923**; the maintenance conversation is not an actor in this research. P000 and the applicable ACTIVE worldview are unchanged.

## Exact target-critical question

The unresolved target p≡13 (mod24) requires a second-digit CM cancellation, whereas the p≡19 (mod24) beta Gauss clipped-square tail already has a proved termwise p² reflection. The p13 beta tail contains genuine valuation-zero and valuation-one source pairs; the p19 reflection cannot simply be moved to p13. We determine **only the genuinely valuation-two high/low source** in the original, signed, two-index clipped beta square. This provides an exact reusable p13-origin port without declaring the full tail or original 216 LIFT solved.

Let p≥13 be prime with p≡5 (mod8), write

\[
p=8t+5,\quad a=(5p-1)/8,\quad b=(7p-3)/8,\quad \lambda=1/9,
\]

and work in the p-local rationals. Retain the exact original beta Gauss coefficient

\[
\beta_k=\frac{(1/8)_k(3/8)_k}{9^k(k!)^2}
=\frac{\prod_{r=0}^{k-1}(8r+1)(8r+3)}{576^k(k!)^2},\quad 0\le k<p.
\]

The original clipped-square signed boundary is

\[
T_{\beta,p}=\sum_{\substack{0\le i,j<p\\ i+j\ge p}}
(8(i+j)+1)\beta_i\beta_j .
\]

**Theorem 1 (new exact all-p≡5 mod8 terminal seed).** For every specified p,

\[
\boxed{\quad \beta_{p-1}/p^2\equiv 1\pmod p,\qquad v_p(\beta_{p-1})=2.\quad}\tag{T}
\]

**Proof.** The numerator factors of beta at k=p−1 run over 0≤r≤p−2. Among 8r+1 exactly 5p occurs, at r=a, and among 8r+3 exactly 7p occurs, at r=b. These indices both lie in [0,p−2] because p≥13. No other numerator factor is divisible by p. Since 8 is a unit, the residues of 8r+1 on 0≤r≤p−1 run over all of F_p; removing the zero at a and the omitted last value 8(p−1)+1≡−7 gives, by Wilson,

\[
\prod_{\substack{0\le r\le p-2\\r\ne a}}(8r+1)
\equiv\frac{-1}{-7}=\frac17\pmod p.
\]

Likewise, the omitted last residue of 8r+3 is −5, hence

\[
\prod_{\substack{0\le r\le p-2\\r\ne b}}(8r+3)
\equiv\frac15\pmod p.
\]

After extracting the two exact p factors, the numerator divided by p² is \(5\cdot7\cdot(1/7)\cdot(1/5)=1\) modulo p. Fermat and Wilson give \(576^{p-1}((p-1)!)^2\equiv1\pmod p\). The quotient is therefore 1 modulo p; this also proves valuation exactly two. QED.

The p≡3 (mod8) predecessor seed is 3/35, not 1. For this p≡5 branch the source factors are **5p and 7p**; the distinct p≡3 branch has 3p and p. The previous p≡19 reflected recurrence is reused below at its exact statement, while its seed and active index set are not borrowed.

**Theorem 2 (new separately sourced signed high/low port).** Put \(q_0=1\) and, for 0≤j<t−1,

\[
q_{j+1}=q_j\frac{576(j+1)^2}{(8j+13)(8j+15)}\pmod p.
\]

All denominators are p-units in this range. For 0≤j<t,

\[
\boxed{\beta_{p-1-j}/p^2\equiv q_j\pmod p.}\tag{R}
\]

Define the actual **high-low subset of the original clipped double sum**, counting both orientations exactly once each:

\[
T_{\beta,p}^{HL}
=2\sum_{j=0}^{t-1}\ \sum_{i=j+1}^{a}
\bigl(8(i+p-1-j)+1\bigr)\beta_i\beta_{p-1-j}.
\]

Then

\[
\boxed{
\frac{T_{\beta,p}^{HL}}{p^2}\equiv
2\sum_{j=0}^{t-1}q_j
\sum_{i=j+1}^{a}\bigl(8(i-j)-7\bigr)
\binom ai\binom bi\,9^{-i}\pmod p .
}\tag{HL}
\]

**Proof.** The numerator factors at a and b show \(v_p(\beta_i)=0\) for 0≤i≤a, equals 1 for a<i≤b, and equals 2 for b<i<p. Thus the high indices are precisely p−1−j, 0≤j<t. Reverse the exact beta recurrence

\[
\frac{\beta_{k-1}}{\beta_k}=\frac{576k^2}{(8k-7)(8k-5)}
\]

at k=p−1−j, divide the high terms by p² before reduction, and apply (T) to obtain (R). Since j<t, the clipped condition \(i+(p-1-j)\ge p\) is exactly i≥j+1. A high term has valuation two. Pairing it with a valuation-one or valuation-two term contributes zero modulo p³; pairing with 0≤i≤a retains exactly the two distinct high/low orientations in \(T^{HL}\). Finally \(\beta_i\equiv\binom ai\binom bi9^{-i}\pmod p\) for i≤a, and the original signed weight reduces to \(8(i-j)-7\). This establishes (HL) without collapsing any other pair category. QED.

**Crucial boundary:** \(T^{HL}\) is only one labeled component of \(T_{\beta,p}\). For this p≡5 branch, the remaining low/low and low/middle clipped pairs can have valuation zero or one and may cancel nontrivially in the total. In particular **(HL) is not an evaluation of \(T_{\beta,p}/p^2\)**, nor a p13 proof of \(G_{\beta,p}\equiv0\bmod p^2\).

## Executed independent finite certificate

Executable: research_notes/portable_direct/d25_p13_gauss_highlow_reflection_20261101.py (Python standard library, all operations exact integer / modular arithmetic).

Successfully checked **all 109 primes p≤3000 with p≡5 (mod8), p≥13** (including **53** original p≡13 (mod24) target primes). For each p, independently computed the original beta recurrence modulo p³; confirmed the entire three-part valuation band, the Wilson terminal seed, every reversed q_j and every original signed high/low pair against (HL). Independent full numerator-product checks were executed at p=13,29,37,53,61,109,373; the complete original signed clipped double tail was additionally evaluated with independent suffix sums.

| p | \(T_{\beta,p}^{HL}/p^2\bmod p\) | full \(T_{\beta,p}\bmod p^2\) | full \(T_{\beta,p}\bmod p^3\) |
|---:|---:|---:|---:|
| 13 | 8 | 156 | 1170 |
| 29 | 11 | 29 | 17690 |
| 37 | 28 | 1332 | 13653 |
| 53 | 42 | 53 | 61851 |
| 61 | 11 | 3660 | 44591 |
| 109 | 65 | 11772 | 974133 |
| 373 | 111 | 138756 | 29773233 |

At p=13, the source-resolved high/low contribution is \(8p^2=1352\bmod p^3\), whereas the **complete** tail is 1170 mod p³ and 156=−p mod p². The difference is from the preserved other pair sources; it is not silently erased. At p=373, the high/low coefficient is **111**, while original 216 scalar Delta=R=196 mod373 belongs to a different observer and cannot be identified with 111.

These are new all-prime *elementary valuation/recurrence statements* with finite exact regression; no formal proof checker or independent Source reviewer has admitted them.

## BRC, mother and exact continuation

BRC **COMPOSE_APPLIED**, using the original index-pair population, p-adic valuation, separately labeled high/low, low/middle and low/low branches, the signed \(8(i+j)+1\) weight and mod-p³ terminal observer. The compression to a single HL scalar is valid **only for this named component**; it is not a safe quotient for subsequent full-tail, derivative or native Green/Hesse operations. Ordinary finite-field reflection is external arithmetic, not native Heartbeat X6/H0/B0 semilinear Frobenius.

Mother remains **\(A_p\equiv p\pmod{p^3}\) for p≡13,19 (mod24)**, equivalently frozen \(\Delta_p-R_p=0\pmod p\). The p≡13 Jacobi divided-Frobenius two-port cancellation \(8J/p=5C_1+7C_\lambda\pmod p\) remains the nearest direct all-prime proof obligation. **Next mathematical step:** use the new fixed high/low p² port without recomputation and target the remaining p13 low/low plus low/middle signed carry jointly; any candidate CM/WZ proof must recover the complete \(T_{\beta,p}\) and the original 216 \(R_p\), not only this source.

**Original native benchmark independently OPEN:** Enterprise Math #1559 still requires fixed p=373 **same-original-class** H0/B0 divided-power \([X]U\bmod139129\), module rank, actual semilinear Frobenius direction and eta, odd signed Green/Hesse, κ, and independent reproduction. Responsible path: authorized canonical Source Task owner/native executor or designated implementation maintainer; assignment/runner is **PENDING_OWNER**. Acceptance requires raw original-class versioned computation and independent validation, not this ordinary beta coefficient theorem. The original three neutral staging sources remain separately attributed.

**Authority and recovery at this turn:** Gateway 0.6.11 reported research_authority_granted=false and executor_binding_configured=false for the authenticated read-only client; own checkpoint read returned ACCESS_DENIED; receipt lookup for original target_request_id research-onhour-20261031-0205-dispatch-r15 returned scoped CONTROL_REQUEST_NOT_FOUND. No historical request was replayed. Recovery_status is advertised as an ordinary control operation but not exposed as an authorized callable tool in this client. No current own Source claim, open run, official checkpoint, publication freeze, Result, review or admission was established by these reads. This is a durable **author-side** artifact only, with independent Source registration/checkpoint still pending. Preserve the original request for authorized later reconcile; do not infer NO_DISPATCH or take a maintenance identity. Research schedule, phase, enabled state and notification behavior remain untouched.
