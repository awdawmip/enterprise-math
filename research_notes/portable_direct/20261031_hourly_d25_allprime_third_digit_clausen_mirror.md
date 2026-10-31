# D25/LIFT — all-prime third-digit reciprocal Clausen mirror

2026-10-31; author-side portable TASK_RESEARCH derivation. Logical Research conversation: chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance. Original task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen mathematical Source c47e13e4aba0e006366f989d6334d443f6333ae3. P000 and ACTIVE worldview unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This note and its exact executed program are author-side evidence, not native Source checkpoint, formal Result or independent review.

## Statement and prerequisites

Let p >= 5 be prime, h=floor((p-1)/3), and

\[
 a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n
     = (2n)!(3n)!/((n!)^5 216^n),\quad
 M_k=-18k^3 a_k (a_{p-k}/p^3),\quad1\le k\le h.
\]

All rational denominators are interpreted in the p-local integers. The known predecessor, the report 20261031_hourly_d25_fermat_endpoint_carry.md (Git blob 2f240d5769eb1be20ec3b15485a073d262cd5eff on Source HEAD 16dac259d9b5d790624fe68f9a959391667ba000), provides the exact factorial endpoint and mirror ratio

\[
 -a_{p-1}/p^3 =
 -\frac{2}{(p-1)^2(p-2)216^{p-1}}
 \prod_{r=1}^{p-2}(1+p/r)\prod_{r=1}^{p-1}(1+p/r)
 \prod_{r=1}^{p-3}(1+2p/r),
\tag{E}
\]

\[
 M_j/M_{j-1}=
 \frac{(1-p/(j-1))^3}
 {(1-2p/(2j-1))(1-3p/(3j-1))(1-3p/(3j-2))},
\quad 2\le j\le h.
\tag{R}
\]

These existing identities are consumed, not recredited as new discoveries.

## Theorem 1 — explicit endpoint third digit

Define the integer Fermat quotient Q=(216^{p-1}-1)/p, and A=13/2-Q, B=115/4-(13/2)Q+Q^2. Then for all p >= 5,

\[
 \boxed{M_1\equiv 1+pA+p^2B\pmod{p^3}.}
\tag{1}
\]

Proof: H_{p-1}=0 (mod p^2) (elementary pairwise harmonic argument for p>=5) and H_{p-1}^{(2)}=0 (mod p), so
\[
 H_{p-2}\equiv1+p,\quad H_{p-3}\equiv3/2+5p/4\pmod{p^2},
\]
\[
 H_{p-2}^{(2)}\equiv-1,\quad H_{p-3}^{(2)}\equiv-5/4\pmod p.
\]
In (E), the combined first and second reciprocal-power sums over the shifted factors are
\[
 S_1=H_{p-2}+H_{p-1}+2H_{p-3}\equiv4+7p/2\pmod{p^2},
\]
\[
 S_2=H_{p-2}^{(2)}+H_{p-1}^{(2)}+4H_{p-3}^{(2)}
 \equiv-6\pmod p.
\]
Thus the product of the shifted factors is
\[
 1+pS_1+\frac{p^2}{2}(S_1^2-S_2)
 \equiv 1+4p+\frac{29}{2}p^2\pmod{p^3}.
\]
Also
\[
 -2/((p-1)^2(p-2))\equiv1+\frac52p+\frac{17}{4}p^2.
\]
Their product is 1+(13/2)p+(115/4)p^2. Multiplication by
216^{-(p-1)}=(1+pQ)^{-1}=1-pQ+p^2Q^2 (mod p^3)
proves (1), including p=5. QED.

## Theorem 2 — third-digit transport for every mirror index

Let H_1=D_1=0 and for 2<=k<=h set
\[
 H_k=\sum_{j=2}^k
 [2/(2j-1)+3/(3j-1)+3/(3j-2)-3/(j-1)],
\tag{2}
\]
\[
 D_k=\sum_{j=2}^k
 [4/(2j-1)^2+9/(3j-1)^2+9/(3j-2)^2-3/(j-1)^2].
\tag{3}
\]
All denominators are p-units in this range. Then
\[
 \boxed{M_k\equiv
 1+p(A+H_k)+p^2[B+AH_k+(H_k^2+D_k)/2]\pmod{p^3}.}
\tag{4}
\]
Equivalently
\[
 \boxed{\frac{a_{p-k}}{p^3}\equiv
 -\frac{1+p(A+H_k)+p^2[B+AH_k+(H_k^2+D_k)/2]}
 {18k^3a_k}\pmod{p^3}.}
\tag{5}
\]
Proof: take the formal logarithm of the exact ratio (R), valid to order p^2 for units 1+pZ_(p). Its increment is
p(H_j-H_{j-1}) + p^2(D_j-D_{j-1})/2 (mod p^3).
Summing j=2,...,k and exponentiating yields
\[
 M_k/M_1\equiv1+pH_k+\frac{p^2}{2}(H_k^2+D_k)\pmod{p^3}.
\]
Multiply by (1), then substitute the exact definition of M_k. QED.

For the ORIGINAL signed 216-weighted high tail (not a replacement for the complete sum),
\[
\begin{split}
 \frac{1}{p^3}\sum_{n=p-h}^{p-1}(6n+1)a_nX^n\equiv
 -\frac1{18}\sum_{k=1}^{h}\frac{(6p-6k+1)X^{p-k}}{k^3a_k}
 [1+p(A+H_k)+p^2(B+AH_k+(H_k^2+D_k)/2)]
 \pmod{p^3}.
\end{split}
\tag{6}
\]
Exact reindexing n=p-k and (5) prove (6); multiplying by p^3 gives the weighted tail modulo p^6. The original weight, index, valuation and source labels are retained.

## Reproducible executed checks

The actual executed Python standard-library source is research_notes/portable_direct/d25_allprime_third_digit_mirror_20261031.py. SHA256: 146753953c32f3c7456769f9761814e15a9a993dfbea1433cdc70c7730775bb6. Remote Git blob: c4ae7abf92360b8d1689036ea1d6997c1ff579bd. The original-coefficient recurrence modulo p^6, low-index mirrors, original signed weighted tail, and independent integer-binomial anchors were compared.

Exactly 428 primes 5<=p<=3000, 197723 mirror pairs, 428 signed tail checks and 10 direct integer anchors passed. Marker PASS_D25_ALL_PRIME_THIRD_DIGIT_RECIPROCAL_MIRROR_EXACT; actual local execution log SHA256 740529f68fb535088fa988b4f151b1473f4c7fd0c8e6ef1a08f72a48cd015682. Anchors (p,h,M1 mod p^3,Q mod p^2): (5,1,36,17), (7,2,1,24), (11,3,1057,26), (17,5,4574,205), (23,7,10236,102), (29,9,18561,570), (37,12,9769,871), (157,52,448079,16071), (373,124,21211019,130200), (1327,442,1293839598,740143). Exact program checks do not constitute formal or independent verification; general theorem is supported by the algebraic proof.

## BRC typing, provenance, and remaining target

COMPOSE_APPLIED: preserve (prime p; original signed coefficient index; original 216 normalization; p^3 valuation stripping; exact endpoint Fermat quotient; harmonic path H_k; second jet D_k; target observer and precision). A signed tail cannot safely collapse into positive weighted mass or a total-only port. This external p-adic theorem does not imply native P000 X6 transfer.

Parent D25/LIFT/JT2 remains to prove original weighted A_p=sum_{n=0}^{p-1}(6n+1)a_n = p (mod p^3) for p mod24=13,19, equivalently the existing scoped complete four-port signed obstruction C+L-J+I=0 (modp). No such all-prime cancellation was proved here. Next: combine the low/middle valuation bands with Q, H_k, D_k while retaining the 216 normalization; obtain a genuine WZ/CM special-value identity rather than assume portwise vanishing.

Native gateway status at this research run: 0.6.11, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Historical own recovery/continuation on kimi-query-bridge #6424/#6425 were read-only and not current run authority. Existing support enterprise-math #1558; native 373 experiment #1559. No native claim/open/source checkpoint/Result, no staging or maintenance identity changes, no scheduler changes.
