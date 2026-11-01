# D25 — signed beta middle/middle moment theorem and complete four-port budget

2026-11-01 (Asia/Hong_Kong). TASK_RESEARCH / AUTHOR-SIDE EXACT PROOF / FINITE EXACT CHECK / **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**.

Mother Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Research logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, not maintenance. Previous high/low result: \`e5f31bafe2c7dd421430023f4d717013c424525f\` (consumed, not recredited).

## New all-prime arithmetic results

For every prime \(p\ge13\), \(p\equiv5\pmod8\), set

\[
a=(5p-1)/8,\quad b=(7p-3)/8,\quad m=b-a=(p-1)/4.
\]

Use the **original** p-local coefficients and the original signed clipped-square boundary:

\[
\beta_k=\frac{(1/8)_k(3/8)_k}{9^k(k!)^2}
=\frac{\prod_{j=0}^{k-1}(8j+1)(8j+3)}{576^k(k!)^2},\quad 0\le k<p,
\]
\[
T_{\beta,p}=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
(8(i+j)+1)\beta_i\beta_j.
\]

The exact valuation bands are \(L=[0,a]\) (valuation 0), \(M=[a+1,b]\) (valuation 1), \(H=[b+1,p-1]\) (valuation 2). Define \(s_r=\beta_{a+1+r}/p\bmod p\), \(0\le r<m\).

**Theorem A (middle-band initial coefficient and recurrence).**

\[
\boxed{
s_0\equiv\frac{10}{441}\binom ba9^{-a}\pmod p,\qquad
s_{r+1}\equiv s_r\frac{(8r+8)(8r+10)}{9(8r+15)^2}\pmod p,\quad0\le r<m-1.
}
\]

All denominators are units for this range. **Proof.** At the transition \(a\to a+1\), exactly one numerator factor contains \(p\): \(8a+1=5p\), while \(8a+3=5p+2\) and \(a+1\equiv7/8\bmod p\). Therefore \(\beta_{a+1}/p\equiv\beta_a10/(576(a+1)^2)\equiv(10/441)\binom ba9^{-a}\pmod p\). Apply the exact recurrence \(\beta_{k+1}/\beta_k=(8k+1)(8k+3)/(576(k+1)^2)\) at \(k=a+1+r\) after dividing by the same \(p\). Substitution \(8a=5p-1\) gives the displayed recurrence. QED.

Define the two finite moments

\[
S=\sum_{r=0}^{m-1}s_r,\qquad
W=\sum_{r=0}^{m-1}(a+1+r)s_r\pmod p.
\]

**Theorem B (middle/middle signed original-port factorization).** Retain all ordered pairs and unmodified sign weight in

\[
T^{MM}_{\beta,p}=
\sum_{\substack{i,j\in M\\i+j\ge p}}(8(i+j)+1)\beta_i\beta_j.
\]

Then

\[
\boxed{T^{MM}_{\beta,p}\equiv p^2S(S+16W)\pmod{p^3}.}
\]

**Proof.** Because \(2(a+1)>p\), every ordered pair in \(M^2\) lies in the clipped region. The original middle coefficients all have valuation 1; after division by \(p^2\), the signed weight is \(1+8i+8j\), and summing over the whole ordered square gives \(S^2+16SW\). This two-moment compression is valid **only** for the designated signed scalar mod \(p^3\), not for native H0/B0, Green/Hesse, derivatives or a future operation. QED.

**Theorem C (full original source budget modulo \(p^3\)).** Label the original signed clipped sums by \(LL,LM,LH,MM\), counting both orientations for unequal bands. Then

\[
\boxed{T_{\beta,p}\equiv T^{LL}_{\beta,p}+T^{LM}_{\beta,p}+T^{LH}_{\beta,p}+T^{MM}_{\beta,p}\pmod{p^3}.}
\]

**Proof.** All excluded \(MH,HH\) pairs have valuation at least 3, and these four sources exhaust the rest. The completed \(LH\) formula is reused at its exact prior statement. Crucially, \(LL\) still needs precision \(p^3\) and \(LM\) needs its one-digit carry modulo \(p^2\); neither is erased. QED.

For the original target class \(p\equiv13\pmod{24}\), **conditional on** the previously established p-local unit \(H_p\), original identity \(B_p=G_pH_p-T_{\beta,p}\), and external 2304 theorem \(B_p\equiv p\chi_{-3}(p)\pmod{p^3}\), the remaining second-digit target is equivalent to

\[
\boxed{
G_p\equiv0\pmod{p^2}\iff
T^{LL}_{\beta,p}+T^{LM}_{\beta,p}\equiv-p\chi_{-3}(p)\pmod{p^2}.
}
\]

The right side is **NOT proved for all** \(p\equiv13\pmod{24}\). The Jacobi divided-Frobenius relation \(8J/p=5C_1+7C_\lambda\pmod p\) and the 216 model \(\Delta_p-R_p\pmod p\) remain OPEN. The theorem closes the remaining valuation-two signed beta source, not the mother problem.

## Actually executed exact certificate

Program: \`research_notes/portable_direct/d25_beta_middle_moment_fourport_20261101.py\`. Python standard library, integer modular arithmetic, no floating-point approximations. Executed **109/109** primes \(13\le p\le3000,\ p\equiv5\bmod8\), including **53** target primes \(p\equiv13\bmod24\). Per prime the program checks the full original beta recurrence mod \(p^3\), valuation bands, middle seed and every recurrence term. At seven selected primes it also independently evaluates all original signed ordered pair classes and compares the full four-port reconstruction with a separate suffix-sum computation. All assertions passed.

| p | S | W | MM/p² mod p | earlier LH/p² mod p | full clipped T mod p³ | LL+LM mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 12 | 3 | 5 | 8 | 1170 | 156 |
| 29 | 17 | 5 | 25 | 11 | 17690 | 29 |
| 37 | 25 | 34 | 17 | 28 | 13653 | 1332 |
| 53 | 30 | 4 | 11 | 42 | 61851 | 53 |
| 61 | 6 | 26 | 31 | 11 | 44591 | 3660 |
| 109 | 1 | 20 | 103 | 65 | 974133 | 11772 |
| 373 | 232 | 195 | 332 | 111 | 29773233 | 138756 |

At \(p=373\), the **distinct** new \(MM/p^2=332\) and previous \(LH/p^2=111\) total 70 mod373; both lower-valuation \(LL\) and \(LM\) still contribute. Neither 332 nor 111 is native \(\kappa\), \(\Delta-R\), or Green/Hesse.

## BRC, unresolved science and exact recovery

BRC COMPOSE_APPLIED to original ordered indices, source labels, valuation bands, sign, clipping predicate, modulus and declared observer. New factorization is not permission to collapse those sources under other operators. **Next science unit:** consume both completed \(LH,MM\) and attack **joint \(LL+LM\) cancellation modulo \(p^2\)** for the 13 class; then couple the original 216 \(\Delta-R\). Do not repeat completed high-index seeds.

The original-class fixed-\(373\) **native H0/B0 divided-power** experiment is still **NOT_RUN / PENDING_OWNER**, tracked by existing Enterprise Math **#1559**. The original native \([X]U\bmod139129\), rank, actual semilinear Frobenius direction/eta, odd signed Green/Hesse, \(\kappa\), and independent reproduction must be executed and validated by an authorized Source owner/native evaluator or implementation maintainer. No surrogate scalar here discharges any such obligation.

Gateway 0.6.11 status in this run: `research_authority_granted=false`, `executor_binding_configured=false`; native active-job quota reached. Prior request `research-onhour-20261031-0205-dispatch-r15` receipt query returned scoped `CONTROL_REQUEST_NOT_FOUND`; its *global* state remains UNKNOWN. No own current Source session, winning claim, open run, Source checkpoint, review or Result admission established. No request replay or maintenance identity borrowed; the three older staging sources remain separately attributed. Frozen science pin, P000, ACTIVE worldview and scheduled configuration are unchanged.
