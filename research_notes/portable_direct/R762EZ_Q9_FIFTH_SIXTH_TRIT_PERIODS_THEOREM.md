# R762EZ — Exact fifth- and sixth-trit periods and preperiods for q=9 full-three-coordinate BRC

Scientific date 2026-11-19 (Asia/Shanghai). Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Frozen taskbook source: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8, research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md (Git blob 218bf9ce05fd2dd79f477ac269fc3590f83f482e). Independent portable author science; no claim of a new protected native execution, Result, Review or promotion. Antecedents R762EM, R762EO, R762ER, R762EY are author-side and NOT_REVIEWED.

## Typed BRC input and observer

Let \(R=\mathbb Z[(\mathbb Z/9\mathbb Z)^3]\). Preserve all three terminal coordinates and the original six distinct named positive branch steps
\((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)\).
Their full terminal polynomial is \(P=1+X+Z+XY+YZ+XYZ\). Put
\[
f(n)=\max(0,\lfloor n/3\rfloor-2),\quad
S_h(n)=3^{-f(n)}P^n\bmod 3^h\in R/3^hR.
\]
R762ER establishes full-n integrality of the normalized coefficient vector. The companion checker also verifies integrality of the entire finite window below. The observer has all 729 terminal coefficients but aggregates the labelled historical paths: this is explicitly an observer-specific quotient, not native signed Cell/Link/Port identity or future-operation preservation.

## New theorem (conditional on exact R762EM/EO spectrum)

| Precision | Modulus | Minimum eventual period | Exact preperiod |
|---|---:|---:|---:|
| h=5 | 243 | **1458** | **20** |
| h=6 | 729 | **4374** | **22** |

Thus \(S_5(n+1458)=S_5(n)\) for every \(n\ge20\), and \(S_6(n+4374)=S_6(n)\) for every \(n\ge22\). Every eventual period is divisible by the tabulated minimum. These starts are sharp over all possible eventual periods.

### Proof of the infinite tails

By R762EM, the multiplication operator has the monic integral minimal polynomial
\(\mu_9(T)=T^{127}+\sum_{j=0}^{126}c_jT^j\).
R762EO proves all its nonzero roots have \(v_3(\lambda)\ge1/3\), so the elementary-symmetric formula gives
\[
v_3(c_j)\ge \lceil(127-j)/3\rceil,\qquad 0\le j<127.
\]
The zero eigenvalue contributes no smaller valuation. For an integer \(L\) divisible by 3, let \(b=L/3\) and
\(E_L(n)=P^{n+L}-3^bP^n\).
For \(n\ge9\) the equality \(f(n+L)=f(n)+b\) means equality of the normalized terminal vectors modulo \(3^h\) is equivalent to
\[
E_L(n)\in3^{f(n)+b+h}R.
\]
Since \(\mu_9(P)=0\), this vector difference satisfies
\[
E_L(n+127)=-\sum_{j=0}^{126}c_jE_L(n+j).
\]
For all \(n\ge9\),
\[
f(n+127)-f(n+j)\le\lceil(127-j)/3\rceil.
\]
Consequently 127 successive full-vector congruences imply the next one, and induction implies the entire infinite tail. This is a valid weighted divisibility induction; it does not replace the full-three-coordinate vector with a scalar observation.

For h=5 take L=1458 and verify the 127 initial vectors at n=20,...,146. For h=6 take L=4374 and verify the 127 initial vectors at n=22,...,148. Both complete-window verifications have been executed with the original six shifts on every one of the 729 endpoints: 92,583 coefficient equalities per precision and 185,166 in total. By the weighted recurrence these finite exact certificates prove the stated infinite-tail identities, conditional on R762EM/EO.

### Minimum periods and exact earliest starts

For h=5 the previously established mod-81 minimum eventual period is 486 (R762EY). Reduction modulo 81 makes every mod-243 period a multiple of 486. As 1458 is a verified period, its minimum is either 486 or 1458. At terminal (0,0,0), the exact normalized residues modulo 243 are \(S_5(21)=229\), \(S_5(507)=67\); hence 486 fails. At the same cell \(S_5(19)=63\), \(S_5(1477)=225\), so no eventual periodicity can begin at 19.

For h=6 reduction modulo 243 has minimum 1458, leaving only 1458 or 4374 as a possible minimum period dividing the verified 4374. At terminal (0,0,0), residues mod 729 are \(S_6(22)=309\), \(S_6(1480)=66\), ruling out 1458. At terminal (0,0,1), residues are \(S_6(21)=494\), \(S_6(4395)=8\), ruling out a start at 21. Any eventual period must be a multiple of its tail minimum; the one-step-before witness cannot be repaired by choosing a longer period. QED.

## Exact verification and semantics

The companion pure-Python-stdlib script R762EZ_Q9_FIFTH_SIXTH_TRIT_VERIFY.py outputs R762EZ_Q9_H5_H6_EVIDENCE.json in sorted JSON format. It uses only integer modular arithmetic, with a constant modulus \(3^{1511}\) to evolve all six original named shifts through power 4522 and computes exact normalized residues at every power. Its integer assertions cover 4,523 mass checks, 3,297,267 divisibility checks and 185,166 coefficient period checks. For each precision it records the complete window-pair SHA-256 under the declared unsigned little-endian 16-bit cell encoding, as well as the two sharp witnesses. No floating-point operations occur.

Proof evidence: AUTHOR_PROVED / EXACT_CERTIFICATE_PASS / NOT_REVIEWED / NO_FORMAL_CHECKER. The infinite-tail proof depends specifically on the exact author-side R762EM/EO 127-degree polynomial and coefficient-valuation bound. Frozen P000, ACTIVE X6 worldview and original scientific task input pins are untouched.

## Open questions

Prove or falsify for all h the suggested q=9 pattern \(T_h=18\cdot3^{h-1}\), and derive a non-tabulated formula for exact preperiod \(N_h\) without 127 new vector comparisons at every precision. Independently audit R762EM/EO and R762ER, and construct source-licensed native signed TRIADIC_CLOSURE_E Cell/Link/Port dynamics with V17/V29/V39 future-operation-safe transport before claiming an X6-native theorem. Existing related PR science is referenced without duplicate publication.
