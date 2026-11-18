# R762FA — Seventh- and eighth-trit q=9 BRC periods and sharp preperiods

Date: 2026-11-19 (Asia/Shanghai). Independent portable research continuation of task \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. The immutable taskbook is \`awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`, Git blob \`218bf9ce05fd2dd79f477ac269fc3590f83f482e\`. Scientific model and frozen task pins unchanged. Prior R762EM/EO/ER and R762EX–EZ are author-side, \`NOT_REVIEWED\`.

## Exact model and new result

In the integral group ring \(R=\mathbb Z[(\mathbb Z/9\mathbb Z)^3]\), retain all three terminal coordinates and all six distinct named **positive** steps
\[
(0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1).
\]
Let \(P=1+X+Z+XY+YZ+XYZ\), \(f(n)=\max(0,\lfloor n/3\rfloor-2)\), and
\[
S_h(n)=3^{-f(n)}P^n\bmod3^h\in (\mathbb Z/3^h\mathbb Z)[(\mathbb Z/9\mathbb Z)^3].
\]
The coefficientwise integrality is the R762ER antecedent. The underlying six-dimensional Heartbeat X6 world, triadic P000 arity and signed Cell/Link/Port structure are retained as distinct native objects; this theorem concerns their declared positive terminal BRC observer only.

**Theorem, conditional on the exact author-side R762EM/EO spectral antecedents.** The complete 729-terminal sequences have precisely the following minimum eventual periods and earliest periodic indices:

| \(h\) | modulus \(3^h\) | minimum eventual period \(T_h\) | exact preperiod \(N_h\) |
|---|---:|---:|---:|
| 7 | 2,187 | **13,122** | **26** |
| 8 | 6,561 | **39,366** | **27** |

Equivalently, \(S_7(n+13122)=S_7(n)\) for all integers \(n\ge26\), and \(S_8(n+39366)=S_8(n)\) for all \(n\ge27\). Every eventual period is a positive multiple of the respective minimum. The period pattern \(T_h=18\cdot3^{h-1}\) therefore holds for \(h=1,\dots,8\), using the cited earlier cases; no all-\(h\) inference is made.

## Infinite-tail proof from exact finite certificates

The q=9 convolution operator has a degree-127 monic integral annihilator \(M(T)=T^{127}+\sum_{j=0}^{126}c_jT^j\) from R762EM. The Newton slopes from R762EO give \(v_3(c_j)\ge\lceil(127-j)/3\rceil\). For \(L\equiv0\pmod3\) set \(b=L/3\) and \(E_L(n)=P^{n+L}-3^bP^n\).

For \(n\ge9\), \(f(n+L)=f(n)+b\); hence \(S_h(n+L)=S_h(n)\) is equivalent to \(E_L(n)\in3^{f(n)+b+h}R\). The annihilator implies
\[
E_L(n+127)=-\sum_{j=0}^{126}c_jE_L(n+j).
\]
Because \(f(n+127)-f(n+j)\le\lceil(127-j)/3\rceil\), 127 successive exact coefficientwise congruences propagate by induction to all later \(n\). This uses all 729 coordinate coefficients and integer divisibility rather than a scalar return observer.

For \(h=7\), the accompanying GNU MP integer checker verifies the 127 consecutive complete-vector equalities at \(n=26,\ldots,152\), using \(L=13122\). For \(h=8\), it verifies at \(n=27,\ldots,153\), using \(L=39366\). Each covers \(127\cdot729=92,583\) exact coefficient equalities. Together with the quoted annihilator antecedent, these establish the infinite-tail periods.

## Minimum periods

Modulo \(3^6\), the previously established minimum period is 4,374 (R762EZ). Since 13,122 is a period modulo \(3^7\), its least period is either 4,374 or 13,122. Within the proven \(h=7\) periodic tail, at endpoint \((0,0,1)\):
\[
S_7(27)=1422,\qquad S_7(4401)=2151\pmod{2187}.
\]
Thus 4,374 is not an eventual period. Indeed these unequal values recur at all indices \(27+k\cdot13122\) and \(4401+k\cdot13122\), so the obstruction persists arbitrarily far into the tail.

Likewise the \(h=7\) minimum period is 13,122; hence the \(h=8\) minimum divides 39,366 and is a multiple of 13,122. At the same endpoint:
\[
S_8(27)=3609,\qquad S_8(13149)=5796\pmod{6561},
\]
ruling out 13,122 at arbitrarily late translates. Thus 39,366 is minimal.

## Exact earliest starts

At the unit endpoint \((0,0,0)\), the finite exact residues are
\[
S_7(25)=729,\qquad S_7(13147)=0\pmod{2187}.
\]
The second index lies in the already proven period-13,122 tail. Every positive multiple of 13,122 would send \(n=25\) to the latter residue, so the preperiod cannot begin at 25.

At endpoint \((0,0,1)\):
\[
S_8(26)=3083,\qquad S_8(39392)=896\pmod{6561}.
\]
The same tail argument rules out a start at 26. The exact starts are therefore 26 and 27. In particular the previously suggested alternating-linear extrapolation \(N_8=28\) is false: this is an exact counterexample to that *candidate extrapolation*, not to the period theorem.

## Reproducible arithmetic and scope

The accompanying \`R762FA_Q9_H7_H8_VERIFY.cpp\` uses GNU MP integer arithmetic and the six literal group-ring shifts. For each \(h\), it calculates all 729 coefficients of \(P^n\bmod3^{f(\mathrm{LAST})+h}\) through LAST, reducing only every twelfth multiplication (exactly equivalent modulo the fixed modulus), divides each checked coefficient by its exact \(3^{f(n)}\), and retains residue modulo \(3^h\). All 549 observed full vectors pass the coefficient divisibility assertion; the 127 equality windows and each witness are exact.

Reproduce with:

\`\`\`sh
g++ -O3 -std=c++17 R762FA_Q9_H7_H8_VERIFY.cpp -lgmp -o r762fa_verify
./r762fa_verify 7 > R762FA_Q9_H7_EVIDENCE.json
./r762fa_verify 8 > R762FA_Q9_H8_EVIDENCE.json
\`\`\`

The fixed moduli are \(3^{4442}\) through \(n=13312\) (h=7) and \(3^{13191}\) through \(n=39556\) (h=8). Output JSON records all certificate ranges, witnesses, and normalization checks. Compiled and run locally on 2026-11-19; both returned exit code zero. Algebraic infinite extension is dependent on the antecedent spectral assertion and remains \`AUTHOR_PROVED / EXACT_CERTIFICATE_PASS / NOT_REVIEWED / NO_FORMAL_CHECKER\`. These are full terminal *positive* BRC observations, not primitive signed \`TRIADIC_CLOSURE_E\` licensed events or future-safe V17/V29/V39 transports.

## Frontier

1. Prove or refute the proposed uniform \(T_h=18\cdot3^{h-1}\) for every \(h\); the new h=7/8 checks are evidence for two further instances.
2. Classify the exact preperiod \(N_h\); observed \(N_1,\ldots,N_8=(8,9,14,16,20,22,26,27)\) rules out the simple previously proposed alternating-linear extrapolation at \(h=8\).
3. Independently audit R762EM/EO/ER and construct source-licensed signed native Cell/Link/Port triadic event with a future-operation-preserving BRC observer/transport. Do not substitute the positive terminal observer for this still-open native question.
