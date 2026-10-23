# D25/LIFT — Exact LOW first-jet m-shift, its new p-pole, and a LOW/HIGH joint seam-cancellation line

2026-10-24 | TASK_RESEARCH | **author-proved all-m rational recurrence and target-class p-local theorem** | **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **not changed**. Author-provenance logical lane chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921. This independent portable note does not claim a live Source CLAIM/open, Result or original native experiment.

**Inputs actually consumed:** (i) original finite LOW first jet J_m^{lo} and epsilon/e/d sequences, and the two-sector high forcing, from [the other lane's LOW-JET reduction](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md); (ii) our immediately preceding [four-port LOW-jet/harmonic operator proof](20261024_hourly_d25_low_jet_four_port_harmonic_transport.md); (iii) the distinct prior [high m-seam Cauchy law](20261024_hourly_d25_high_cauchy_m_shift_seam_residues.md). Those already completed identities are not re-claimed. Parent LIFT/CM comparison remains OPEN.

## 1. All-m exact first-jet shift (no prime assumption)

Keep b_{m,n}=(-1)^n 2^{-n} binom(m,n), k_n=(1-3n)(6n+3)/[(3n+1)(3n+2)], epsilon_n=3/(6n+1)-1/(3n+2)-2/(3n+1), e_n=sum_{j<n}epsilon_j, d_n=2/(1-3n)+2/(6n+3)-1/(3n+2)-2/(3n+1), and J_m^{lo}=sum_{n<=m}b_{m,n}k_n(e_n+d_n).

Write Q_m^{(r)}(a;x)=sum_{n=0}^m b_{m,n}x^n/(3n+a)^r. The operator H_epsilon on polynomials was proved in the preceding note, with H_epsilon[x^n]=e_n, and is an exact **finite rational** polynomial integral, not a limit prescription. Introduce the shifted **indexed** kernel
\[
T_m(x)=\sum_{n=0}^m b_{m,n}k_{n+1}x^n
=-2(1-x/2)^m+2Q_m^{(1)}(4;x)+3Q_m^{(1)}(5;x).\tag{T}
\]

**Theorem 1.** For EVERY integer m>=0 the original LOW jet satisfies:
\[
\boxed{\begin{aligned}
J_{m+1}^{lo}-J_m^{lo}
={}&-\tfrac12\mathscr H_\epsilon[T_m]
+\tfrac47Q_m^{(1)}(\tfrac12;1)-\tfrac7{12}Q_m^{(1)}(1;1)
-\tfrac{73}{42}Q_m^{(1)}(4;1)\\
&-\tfrac{15}4Q_m^{(1)}(5;1)
+2Q_m^{(2)}(4;1)+\tfrac32Q_m^{(2)}(5;1).
\end{aligned}}\tag{JET-SHIFT}
\]

**Complete proof.** Pascal's binomial identity gives b_{m+1,n}=b_{m,n}-(1/2)b_{m,n-1}, with b out of range set to zero. Therefore
\[
J_{m+1}^{lo}-J_m^{lo}
=-\tfrac12\sum_{n=0}^m b_{m,n}k_{n+1}(e_n+\epsilon_n+d_{n+1}).
\]
The sum with e_n is exactly H_epsilon[T_m]. Direct common-denominator algebra gives the *rational identity*:
\[
\boxed{\begin{aligned}
k_{n+1}(\epsilon_n+d_{n+1})
={}&-\frac{16}{7(6n+1)}+\frac{7}{6(3n+1)}
+\frac{73}{21(3n+4)}-\frac4{(3n+4)^2}\\
&+\frac{15}{2(3n+5)}-\frac3{(3n+5)^2}.
\end{aligned}}\tag{PF}
\]
Convert 1/(6n+1)=1/[2(3n+1/2)], sum each rational kernel against b_{m,n}, and multiply by -1/2. This is precisely (JET-SHIFT). Every identity is over Q, and every index and n=m+1 incoming term is retained. QED.

This supplies an exact transition algorithm combining **one shifted harmonic channel** and six individually named rational moment ports; it is not the same as the earlier rank-two update for the non-jet LOW head A_m. The two unusual ports a=1/2 and a=4,5 are consequences of the original epsilon cocycle and actual one-step shift, not arbitrary added parameters.

## 2. Sharp new p-pole when the LOW cutoff moves one step

Now let p=6m+1 be prime with m>=2 (so p>=13; in particular this covers the actual target subclasses p=13,19 mod 24). Keep p FIXED when comparing the auxiliary rational sequences with indices m and m+1. This is NOT induction between two different source primes.

For n<=m, the only denominator in (JET-SHIFT) divisible by this fixed p is 6n+1 at n=m in Q_m^{(1)}(1/2;1). Indeed 3n+4<=3m+4<p, 3n+5<=3m+5<p for m>=2; all epsilon_j inside H_epsilon[T_m] have j<n<=m and denominator 6j+1<p, while all other displayed ports and rational coefficients have p-unit denominators. Since b_{m,m}=(-1)^m2^{-m},
\[
Q_m^{(1)}(\tfrac12;1)
=\frac{2(-1)^m2^{-m}}p+
\sum_{n=0}^{m-1}\frac{b_{m,n}}{3n+1/2}.
\]
Define the **explicit p-integral finite residual**
\[
\begin{aligned}
V_m^J={}&-\tfrac12\mathscr H_\epsilon[T_m]
+\tfrac47\sum_{n=0}^{m-1}\frac{b_{m,n}}{3n+1/2}
-\tfrac7{12}Q_m^{(1)}(1;1)
-\tfrac{73}{42}Q_m^{(1)}(4;1)\\
&-\tfrac{15}4Q_m^{(1)}(5;1)
+2Q_m^{(2)}(4;1)+\tfrac32Q_m^{(2)}(5;1)\ \in\mathbb Z_{(p)}.
\end{aligned}
\]
Then JET-SHIFT gives the EXACT rational decomposition
\[
\boxed{\Delta_m J^{lo}:=J_{m+1}^{lo}-J_m^{lo}
=\frac{8(-1)^m2^{-m}}{7p}+V_m^J.}\tag{LOW-POLE}
\]
The numerator is a p-unit for p>=13; hence
\[
\boxed{v_p(\Delta_m J^{lo})=-1\quad(p=6m+1\ \mathrm{prime},\ m>=2).}\tag{LOW-VAL}
\]
This proves an actual **seam pole** enters when one moves the formerly p-integral LOW cutoff beyond n=m. It would be incorrect to reduce the naive forward J recurrence modulo p before isolating this pole. The exceptional p=7,m=1 is OUTSIDE this statement: there 3m+4=p introduces an additional double pole, and direct exact arithmetic gives v_7(J_2-J_1)=-2. No inference is made for that case.

## 3. Joint LOW/HIGH pole cancellation is unique in rank two

The independently proved high Cauchy theorem defines
\[
M_m^{(6)}=\sum_{r=1}^{m-1}\frac1{2^r(6r+1)}
+\frac13\sum_{r=m+1}^{3m-1}\frac1{2^r(6r+1)}
\]
and proves, for the same fixed p=6m+1,
\[
\Delta_m M^{(6)}=\frac{2^{-m}}p+V_m^{(6)},\qquad V_m^{(6)}\in\mathbb Z_{(p)}.
\]
Combining this **existing** HIGH result with the **new** LOW-POLE identity immediately yields
\[
\boxed{\mathcal C_m:=\Delta_m J^{lo}
-\frac{8(-1)^m}{7}\Delta_m M^{(6)}
=V_m^J-\frac{8(-1)^m}{7}V_m^{(6)}\in\mathbb Z_{(p)}.}\tag{LOW-HIGH-CANCEL}
\]
Both p^{-1} principal parts cancel **exactly over Q**, not merely modulo p. Moreover for any p-integral rational c,
\[
\boxed{\Delta_m J^{lo}-c\,\Delta_m M^{(6)}\in\mathbb Z_{(p)}
\iff c\equiv\frac{8(-1)^m}{7}\pmod p.}\tag{UNIQUE}
\]
Necessity follows because 2^{-m} is a p-unit; sufficiency follows from the displayed exact decompositions. This is the UNIQUE cancellation coefficient mod p when the observer uses just the LOW-jet and the first HIGH moment.

The earlier second high moment satisfies Delta M_m^{(2)}=2^{-3m}/(3p)+V_m^{(2)}. Hence with both high ports a more general exact affine family survives:
\[
\boxed{\Delta_m J^{lo}-c_6\Delta_m M^{(6)}-c_2\Delta_m M^{(2)}
\in\mathbb Z_{(p)}
\iff
c_6+\frac{c_2}{3\,2^{2m}}\equiv\frac{8(-1)^m}{7}\pmod p,}\tag{THREE-PORT-LINE}
\]
for p-integral c_6,c_2. This exhibits the two-dimensional annihilator of the three observed pole residues; it DOES NOT say the resulting finite residual vanishes. All three observer port labels, the removed r=m HIGH seam and the incoming n=m+1 LOW cutoff remain distinguishable.

## 4. Executed checks, scope and next scientific unit

Author-side exact Python Fraction checks reconstructed b_{m,n}, k_n, epsilon_n, e_n, d_n, J_m directly from original finite sums and all Q and M moments independently. PF held symbolically by exact rational simplification and pointwise for n=0..29; JET-SHIFT agreed for all m=0..19. For the target primes p=13,19,31,37,43,61,67,73,79, the HIGH split and LOW-POLE split agreed exactly; LOW-HIGH-CANCEL and its residual formula were exact Q equalities and the computed residuals had p-unit denominators. Sample (p : C_m mod p): 13:7, 19:14, 31:6, 37:2, 43:34, 61:40. **These NONZERO values disallow describing pole cancellation as a proof of the full LIFT.** p=7 exception was checked separately.

The proofs cover all stated m, p via Pascal, rational partial fractions, finite polynomial moment identities and p-unit bounds; finite checks are author regression only. BRC actual usage: preserve the independent LOW first-jet n-branch and two HIGH seam-labeled Cauchy branches; move cutoff under a stated observer, expose exact incoming p^{-1} residual, and cancel only in the uniquely justified joint scalar channel. There is no native-X6 calculation, native benchmark, source-specific CM normalization, formal Lean proof, independent Driver review or accepted Source checkpoint.

**Smallest next unit:** feed LOW-HIGH-CANCEL / THREE-PORT-LINE and the previous high five-boundary law into the exact whole D_m^{finite} observer, including G_m, B_m, q_p(6), H_{2m}, the rank-two HIGH reflection and the original n=4m terminal, to seek a terminating p-integral WZ/finite-difference certificate. A p-integral auxiliary m-shift is a necessary seam-aware coordinate, **not** a cross-prime proof of D_m^{finite}=0. The original Source D25 native hard target also still needs an actual CM/divided-power representative comparison: primitive class, direction/semilinearity, ordinary omega+6 nabla_lambda omega relationship, exact leading normalization, and same-class bridge. Do not substitute this portable result for that input.

Control status: original historical Researcher session was read-only recovered with no winning CLAIM/authorized run, and source-specific native continuation remained OPEN/PARKED; a new canonical dispatch, if not yet terminal, must be reconciled under its own original request ID. Neutral preserved staging remains neutral, not completed research. This is a GitHub proof preservation only, with **UNREVIEWED / NOT_ADMITTED** status. Frozen Source pins, owner, scheduler cadence/phase/enabled/notification settings untouched. Support path https://github.com/awdawmip/enterprise-math/issues/1558.
