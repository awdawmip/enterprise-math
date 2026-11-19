# R762FJ — The ninth-trit q=9 BRC period: exact 118,098, preperiod 32

Date: 2026-11-19 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECK_PASSED / NOT_REVIEWED**.

Frozen Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`; taskbook \`awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`. The scientific object is the **positive six-named-step, complete 729-terminal BRC observer** on a three-coordinate slice of native X6, not a signed Cell/Link/Port closure or a new P000 premise.

## Theorem

Let \(G=(\mathbb Z/9\mathbb Z)^3\), \(R=\mathbb Z[G]\), and
\[
P=1+X+Z+XY+YZ+XYZ,\qquad f(n)=\lfloor n/3\rfloor-2\quad(n\ge9).
\]
Then \(P^n/3^{f(n)}\) has **integer coefficients for all \(n\ge9\)**. Put \(S(n)=3^{-f(n)}P^n\).

At ninth-trit precision, the complete 729-terminal vector has the **exact minimum eventual period**
\[
\boxed{T_9=118098=18\cdot3^8}
\]
and **exact preperiod** \(\boxed{N_9=32}\):
\[
S(n+118098)\equiv S(n)\pmod{3^9}\quad\text{for all }n\ge32.
\]
The congruence fails at \(n=31\). No positive eventual period below 118098 is possible.

This extends the prior recorded \(h=7,8\) periods, which the present independent checker also reproduces. No universal all-\(h\) claim is made.

## 1. Exact centered orbit reduction

Reuse the independently authored moving-frame theorem R762FH in [PR #2773](https://github.com/awdawmip/enterprise-math/pull/2773): let \(c=5=2^{-1}\pmod9\), \(D=\operatorname{diag}(1,-1,1)\), and \(h_n(y)=[nc(1,1,1)+Dy]P^n\). The six centered steps are \(t=D(s-c\mathbf1)\). They form a multiset invariant under simultaneous coordinate permutations and global sign reversal, the group \(S_3\times C_2\).

Thus \(h_n\) is constant on precisely 85 orbits with canonical representative
\(\kappa(y)=\min_{\rm lex}(\operatorname{sort}(y),\operatorname{sort}(-y))\).
An exact integer 85-state operator \(C\) obeys
\[
h_{n+1}(k)=\sum_{s\in\{0,X,Z,XY,YZ,XYZ\}}
h_n(\kappa(k-D(s-c\mathbf1))).
\]
Every repeated neighbor is counted with its named-step multiplicity. Since every period considered is divisible by 9, the centered frames for \(n\) and \(n+L\) coincide, so **85-orbit equality is exactly equivalent to equality of all 729 original terminal counts**.

The supplied verifier independently compares the 85-orbit evolution with unrestricted original six-step, 729-terminal integer convolution at all \(n=0,\ldots,55\), totaling 40,824 exact comparisons.

## 2. A directly certified 33rd-order trajectory recurrence

Let
\[
Q(T)=T^{33}+\sum_{j=1}^{33}a_jT^{33-j}\in\mathbb Z[T].
\]
Its 34 integer coefficients in ascending order are in the verifier and JSON evidence, copied from the independently computed moving-frame R762FI spectrum in [PR #2773](https://github.com/awdawmip/enterprise-math/pull/2773). The new verification **does not need to assume the prior eigenvalue enumeration is correct**: it constructs \(C\), computes \(h_1,\ldots,h_{34}\) directly with exact integers, and checks all 85 entries of
\[
\sum_{j=0}^{33}[T^j]Q(T)\,h_{j+1}=Q(C)h_1=0.
\]
Since \(C\) commutes with its polynomial, \(Q(C)h_n=0\) for every \(n\ge1\). In addition, it checks all 33 integer inequalities
\[
v_3(a_j)\ge\lceil j/3\rceil.
\]

These two **finite exact certificates** prove the trajectory recurrence and its divisibility bounds independently of a general spectral completeness claim.

## 3. Independent all-time normalization-integrality proof

For \(n=9,\ldots,41\) all 85 integer orbit values \(h_n\) are explicitly checked divisible by \(3^{f(n)}\). For any \(n\ge9\), the recurrence
\[
h_{n+33}=-\sum_{j=1}^{33}a_j h_{n+33-j}
\]
propagates this divisibility because
\[
f(n+33)-f(n+33-j)\le\lceil j/3\rceil\le v_3(a_j).
\]
Induction establishes \(3^{f(n)}\mid h_n(k)\) for all \(n\ge9\), all 85 orbits and therefore all 729 original terminal coefficients. Hence every comparison below is between genuine integer-normalized states, without needing to assume the earlier R762ER integrality claim.

## 4. All-time period from 2,805 exact high-index congruences

For \(L=118098\), \(b=L/3=39366\), set \(\delta_n=h_{n+L}-3^b h_n\). It satisfies the same degree-33 recurrence. The script evaluates high powers by reducing \(T^{n-1}\) modulo \(Q(T)\) over \(\mathbb Z/3^E\mathbb Z\), then applying the reduced polynomial to the 33 directly computed orbit vectors \(h_1,\ldots,h_{33}\). This is exact modular exponentiation, not floating-point spectral approximation.

At \(h=9,N=32\), the script independently checks
\[
\delta_n(k)\equiv0\pmod{3^{f(n)+b+9}}
\quad (32\le n\le64;\; k\in G/(S_3\times C_2)).
\]
All **33 × 85 = 2,805** congruences pass. The maximum modulus exponent used in the shared scan through \(n=74\) is explicitly recorded in JSON; no coefficient reduction is done before the required division. By the recurrence coefficient bounds in §2, if the congruences hold for 33 consecutive times, they propagate to all later times. Division by \(3^{f(n)+b}\) proves the claimed normalized period for every \(n\ge32\).

For exact onset, at \(n=31\), centered orbit \(k=(0,0,1)\), the normalized discrepancy is
\[
[S(31+118098)-S(31)]_{\rm centered\ k}
\equiv 6561=3^8\pmod{19683=3^9}.
\]
The corresponding original endpoint is \(g=(2,2,3)\). Hence \(N_9=32\).

## 5. Minimality of the eventual period

The separately published R762FG [character valuation theorem](https://github.com/awdawmip/enterprise-math/pull/2768) supplies the following short algebraic necessity, recalled here for exact dependency scope. Take the integral cyclotomic character
\[
(X,Y,Z)=(1,\zeta_9,\zeta_9^2),\quad
\lambda=2+\zeta_9+\zeta_9^2+2\zeta_9^3,\quad
\beta=\lambda^3/3.
\]
The exact cyclotomic identity \(\beta^6=1+3u\), with \(u\) a 3-adic unit, and \(\beta\) of order six modulo 3, yield \(v_3(\beta^{6t}-1)=1+v_3(t)\). For sufficiently late multiples of three \(n\), the normalized character difference at an eventual period \(L\) forces
\[
18\cdot3^{h-3}\mid L\qquad(h\ge3).
\]
In particular, at \(h=9\), every eventual period is divisible by 13122. This is a symbolic 3-adic lower bound; the referenced R762FG files give the exact six-basis computation of \(\beta\).

As 118098 is itself an eventual period, the minimum eventual period must divide 118098. The only remaining candidates are 13122, 39366 and 118098. The script evaluates the smaller candidate \(L=39366\) at \(n=33\ge N_9\), obtaining the exact original endpoint witness:
\[
[S(33+39366)-S(33)]_{\rm centered\ (0,0,1)}
\equiv6561\pmod{19683},
\]
corresponding to original endpoint \(g=(3,3,4)\). Hence 39366 is not an eventual period; a period of 13122 would also imply a period of 39366. The minimum eventual period is **118098**.

The step from one witness to the eventual-period claim is justified: once the sequence is 118098-periodic for all \(n\ge32\), any smaller eventual period, if it existed at a later start, would also hold from \(n=32\) by shifting both compared indices forward by a sufficiently large multiple of 118098. The witness at \(n=33\) rules it out.

## Reproduction and evidence

Run:
\`\`\`bash
python3 R762FJ_ORBIT_PERIOD_CERTIFICATE_VERIFY.py --h 7 8 9 --scan-end 42 --output R762FJ_EVIDENCE.json
\`\`\`

The actual local run passes: 85 exact \(Q(C)h_1=0\) entries, 33 coefficient-valuation checks, 33 integral-normalization base times, 40,824 unrestricted terminal comparisons, 33×85 high-index congruences per precision, and the two distinct \(h=9\) failure witnesses. Reproduced regression values: \(h=7:L=13122,N=26\), \(h=8:L=39366,N=27\); **new** \(h=9:L=118098,N=32\). The script operates on unbounded Python integers and exact modular arithmetic only. Scientific status: **NOT_REVIEWED**; full code and JSON preserve arithmetic and finite verification coverage.

## Next precise problems

1. Prove or refute the all-\(h\) extrapolation \(T_h=18\cdot3^{h-1}\) and derive a formula for exact onset \(N_h\); the present proof covers \(h=9\) and independently checks \(h=7,8\).
2. Evaluate \(h=10\) with the same 33×85 modular certificate, recording computation and precision costs, before generalizing.
3. Independently define native signed \`TRIADIC_CLOSURE_E\` Cell/Link/Port update and future-operation-preserving V17/V29/V39 transport. The current equal-positive-endpoint symmetry does not encode signed force cancellation or path-provenance erasure.
