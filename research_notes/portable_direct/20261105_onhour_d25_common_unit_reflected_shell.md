# D25 — signed A/B reflected upper-shell transport with a common p-unit

Date: 2026-11-05. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable scientific input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Intended Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, distinct from maintenance. **AUTHOR-PROVED EXACT IDENTITY / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.**

## Selected question and predecessor

The frozen goal on primes p≡13,19 mod24 is \(\Delta_p-R_p=0\pmod p\), strictly source-aligned with \(W_p-V_p=0\pmod{p^3}\). The previous author-side matched half-endpoint second jets imply equivalently \(K_p+\Xi_2+C_A=0\pmod p\), but uniform cancellation is open. Their uniform floor centering is consumed, not re-proved. This unit compares **both original valuation-two upper shells** via one quadratic-character endpoint normalization and two terminating reflected kernels.

## Definitions and valuation scope

For every prime p>3 set \(s=(p+1)/2,\ h=(p-1)/2,\ k_A=\lfloor(2p-1)/3\rfloor,\ k_B=\lfloor(3p-1)/4\rfloor\) and \(L_A=k_A-s+1,\ L_B=k_B-s+1\). Work in \(\mathbb Z_{(p)}\). Original source-labelled coefficients are
\[
a_k=\frac{(2k)!(3k)!}{216^k(k!)^5}
=\frac{\binom{2k}k^2\binom{3k}k}{216^k},\quad
b_k=\frac{(4k)!}{2304^k(k!)^4}
=\frac{\binom{2k}k^2\binom{4k}{2k}}{2304^k}.
\]
Let \(W_p=\sum_{k=0}^{p-1}(6k+1)a_k,\ V_p=\sum_{k=0}^{p-1}(8k+1)b_k\), with \(W_h,V_h\) the corresponding \(0\le k\le h\) sums. Legendre's factorial valuation formula gives \(v_p(a_k)=2\) for \(s\le k\le k_A\), and \(v_p(b_k)=2\) for \(s\le k\le k_B\); subsequent indices below p have valuation at least three. This is a valuation claim for **unweighted** source coefficients, with the original signed weights retained.

## Theorem 1: unit at the same upper endpoint

In \(\mathbb F_p\), put \(A_0=a_s/p^2,\ B_0=b_s/p^2\). Both are units, and
\[
\boxed{A_0=\frac{s+1}{216^s(s!)^4},\quad
B_0=\frac4{2304^s(s!)^4},\quad
\frac{A_0}{B_0}=4\left(\frac6p\right).}
\]
Thus \(A_0/B_0=-4\) for p≡13 mod24, and \(+4\) for p≡19 mod24.

**Proof.** As \(2s=p+1\), \((2s)!/p=(p-1)!(p+1)\equiv-1\pmod p\). As \(3s=p+s+1\), \((3s)!/p\equiv-(s+1)!\pmod p\); multiplying and dividing by \((s!)^5\) proves \(A_0\). As \(4s=2p+2\), remove the factors p and 2p and use Wilson twice to get \((4s)!/p^2\equiv 2((p-1)!)^2\cdot 2=4\pmod p\), proving \(B_0\). The ratio is \((s+1)(32/3)^s/4\). Since s=(p+1)/2 and s+1≡3/2, Euler's criterion converts this to \(4(32/3|p)=4(6|p)\). All denominators are p-units. The target congruence classes have \((6/p)=-1,+1\) respectively.

## Theorem 2: source-labelled reflected terminating 3F2 kernels

For \(0\le j<L_A\), \(0\le j<L_B\) respectively, define
\[
g_A(j)=\frac{(1)_j(5/6)_j(7/6)_j}{(3/2)_j^3\,2^j},\qquad
g_B(j)=\frac{(1)_j(3/4)_j(5/4)_j}{(3/2)_j^3\,9^j}.
\]
All displayed rational denominators are p-units. Then
\[
\boxed{\frac{a_{s+j}}{p^2}=A_0g_A(j),\qquad
\frac{b_{s+j}}{p^2}=B_0g_B(j)\quad(\bmod p).}
\]

**Proof.** The exact source recurrences are
\[
a_{k+1}/a_k=\frac{(2k+1)(2k+2)(3k+1)(3k+2)(3k+3)}{216(k+1)^5},\quad
b_{k+1}/b_k=\frac{(4k+1)(4k+2)(4k+3)(4k+4)}{2304(k+1)^4}.
\]
Substitute k=s+j and reduce modulo p. Their upper-shell normalized ratios become exactly
\[
\frac{g_A(j+1)}{g_A(j)}
=\frac{(j+1)(j+5/6)(j+7/6)}{2(j+3/2)^3},\quad
\frac{g_B(j+1)}{g_B(j)}
=\frac{(j+1)(j+3/4)(j+5/4)}{9(j+3/2)^3}.
\]
All divisions are by units in the specified index ranges, and both normalized sequences start at 1. Induction proves the termwise identities. The **shared denominator** \((3/2)_j^3\) is a proven representation, not an unproved transformation between the different numerators.

## Corollary: signed common-unit shell transport

Define finite-field moments
\[
U_A=\sum_{j=0}^{L_A-1}(6j+4)g_A(j),\quad
U_B=\sum_{j=0}^{L_B-1}(8j+5)g_B(j).
\]
The original weights reduce as \(6(s+j)+1\equiv 6j+4\) and \(8(s+j)+1\equiv8j+5\). Consequently for all primes p>3,
\[
W_p-W_h\equiv p^2A_0U_A,\quad V_p-V_h\equiv p^2B_0U_B\pmod{p^3},
\]
\[
\boxed{
W_p-V_p\equiv W_h-V_h+p^2B_0[4(6/p)U_A-U_B]\pmod{p^3}.}
\]
Consume the previously proved Guo–Zudilin 2304 complete/half supercongruence \(V_p-V_h\equiv0\pmod{p^3}\): since B_0 is invertible, \(U_B=0\pmod p\). For target classes, the **sole remaining cancellation** becomes
\[
\boxed{\frac{W_h-V_h}{p^2}+4(6/p)B_0U_A=0\pmod p,}
\]
where the integer p²-quotient exists by the previously established first-digit congruence. This is an **exact equivalence**, not a proof of its universal zero value.

## Executed integer verification, provenance and next action

The attached independent Python checker uses original integer binomial coefficients for upper-shell coefficients modulo p³, p-unit factorial normalization, and separate exact modular recurrences for full and half original sums. All 166 primes 5≤p≤997 (45 in frozen target classes) pass all termwise, signed, full/half and quadratic-character assertions, zero failures; no floating point is used. Representative rows:

|p|A_0|B_0|A_0/B_0|U_A|U_B|signed A shell|
|--:|--:|--:|--:|--:|--:|--:|
|13|10|4|9=-4|1|0|10|
|19|17|9|4|5|0|9|
|139|31|112|4|117|0|13|
|373|290|114|369=-4|217|0|266|

BRC observer: source A/B label, upper-shell indices and endpoints, valuation two, rational units, original signed weights, \((6/p)\), independent half-prefix carry \(K_p\) and the original mod-p³ difference. Allowed future operation: source-preserving sum, subtract, p² division only after proved divisibility. Existing half-endpoint jet/carry and 2304 theorem: **COMPOSE_APPLIED**. No positive-mass quotient erases signed cancellations.

**Next precise science unit:** find a p-dependent terminating A/B transform or WZ relation coupling the half-endpoint p² carry to the common-denominator reflected A shell, proving the boxed cancellation in both target residue classes or a valid counterexample. Do not redo CM0, UR or p⁴ sharpness. Original fixed-373 H0/B0 divided-power native \([X]U\) modulo 139129, module rank, semilinear Frobenius direction, eta/kappa, odd Hesse/Green readout and independent replication remain unexecuted under Issue #1559 (open, pending executor).

Last verified Source original request \`onhour11-20261105-1505-d25-own-read\`: SUCCEEDED with execution_authorized=false. This author-side publication is neither an authenticated Researcher session nor a native CLAIM/run/checkpoint/Result/admission.