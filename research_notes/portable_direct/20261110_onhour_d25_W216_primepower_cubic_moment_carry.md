# D25 / W216 — prime-power cubic moment carry across all r

Date: 2026-11-10 (Asia/Hong_Kong). Research lane local author-side evidence; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Original scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

Classification: AUTHOR_SIDE / EXACT_PROOF / FINITE_EXACT_CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. No native Researcher session/CLAIM/open run is represented.

## Theorem (all prime-power scales)

For every prime p>3 and every integer r>=1, set N=p^r and define original rational coefficients and binomial moments

\[
A_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}
=\frac{(2k)!(3k)!}{(k!)^5 216^k},
\quad M_j(N)=\sum_{k=0}^{N-1}\binom{k}{j}A_k .
\]

Then in the p-local integers, with **no finite-scan hypothesis**,

\[
\boxed{
27\bigl(M_2(p^r)+2M_3(p^r)\bigr)
-M_0(p^r)-11M_1(p^r)
\equiv -p^{3r}\pmod{p^{3r+1}}.
}\tag{PP-CMC}
\]

In particular, the signed cubic-moment defect has exact valuation 3r (for every p>3), with leading unit -1.

### Proof

Consume the exact rational all-N finite-boundary identity proved in the immediately preceding unit:

\[
27(M_2(N)+2M_3(N))-M_0(N)-11M_1(N)
=-9(N-\tfrac12)(N-\tfrac23)(N-\tfrac13)A_{N-1}.\tag{E}
\]

The earlier independently proved prime-power terminal theorem (in research_notes/portable_direct/20261110_onhour_d25_W216_primepower_terminal_dwork_bridge.md) establishes, for p>3 and all r>=1,

\[
v_p(A_{p^r-1})=3r,\quad
A_{p^r-1}/p^{3r}\equiv-1\pmod p.
\]

All denominators 2,3 are p-units; with N=p^r,

\[
-9(N-\tfrac12)(N-\tfrac23)(N-\tfrac13)
\equiv-9(-\tfrac12)(-\tfrac23)(-\tfrac13)
=1\pmod p.
\]

Multiply these two congruences in the exact identity (E). The result is (PP-CMC), including its exact leading unit. QED.

This gives an explicit all-scale signed-observer conservation law: the compressed combination (M0,M1,M2+2M3) preserves its p^(3r)-scale terminal charge. It extends the r=1 corollary, rather than re-deriving the prior W-S terminal formula. It is a mathematical consequence of two earlier proven results and does not depend on the conjectural Dwork recurrence.

## Exact reproducibility checks

One independent implementation streams the **original** factorial-ratio coefficients as valuation/unit pairs in Z/p^(3r+1). It computes all four binomial moments over N=p^r indices, and checks (PP-CMC) against (-p^(3r)) mod p^(3r+1). Seven fully executed (p,r) tests passed:

| p | r | N | expected and observed residue |
|---:|---:|---:|---:|
| 5 | 2 | 25 | 62500 |
| 7 | 2 | 49 | 705894 |
| 7 | 3 | 343 | 242121642 |
| 11 | 2 | 121 | 17715610 |
| 13 | 2 | 169 | 57921708 |
| 19 | 2 | 361 | 846825858 |
| 31 | 2 | 961 | 26625110430 |

The source method uses exact modular arithmetic and original k values, no float or reindexed surrogate. Checks verify the implementation and detect mistakes; proof holds universally by (E)+terminal theorem.

## Relation to frozen target and BRC

This unit is a genuine structural reuse of the original p-block lift: the retained information includes index k, v_p(A_k), unit part and the signed moment operator. Its future observer is the specific cubic-moment combination; arbitrary native Frobenius, rank, and Hesse ports require their own faithful map.

The mother target remains original \(\Delta_p-R_p\equiv0\pmod p\) for all \(p\equiv13,19\pmod{24}\), or an original-class exact counterexample. The new all-scale theorem is a research tool for the frozen LIFT Frobenius port. Its proof does not substitute for the native H0/B0 experiment.

Original benchmark support issue #1559 was OPEN/PENDING_OWNER at last read on 2026-11-10: original-class p=373 [X]U mod 139129, native rank and semilinear eta, signed odd kappa/Delta-R, pinned code and independent reproduction not executed here.

## Exact continuity

Research logical lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane not accessed for mutations. Current exact Source continuation request onhour11-20261110-1407-exact-cont returned SUCCEEDED at Source c64f3e3b5cb007159795c89434003f03a57d82a3. Own recovery query gave SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED. Therefore no own winning claim/open run or formal Source checkpoint was asserted.

Already proved and not to repeat: original Source D24 UR ACCEPTED and D25 completed predecessor checkpoint, prime-power terminal lemma, all-N finite moment identity and p-block Newton transfer. Non-admitted author-side pieces stay provenance only.

Next smallest mathematical unit: establish uniformly or find an exact counterexample to \(q_3-2q_2\equiv0\pmod{p^4}\) using original b-band exceptions, and separately discharge the target supersingular M0/M1 and three-anchor firstjet hypotheses. The native H0/B0 run remains its own highest-priority authorization and compute obligation tracked by #1559.
