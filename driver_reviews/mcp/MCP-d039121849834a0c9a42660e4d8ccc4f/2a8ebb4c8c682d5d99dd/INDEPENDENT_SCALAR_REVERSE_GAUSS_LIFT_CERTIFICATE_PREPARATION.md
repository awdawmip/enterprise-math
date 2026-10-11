# CM24 independent scalar and reverse Gauss forcing certificate

Status: PAPER_PREPARATION / OUTSIDE_FROZEN_RR / PARENT_UR_AND_LIFT_OPEN

Date: 2026-10-11. Author: EM-ENTERPRISE-CB50ED.
This supplements the immutable RR-AA50A881C6A2DD42BDD3; it does not amend that Result, its sixteen files, or its completed run. No new arithmetic campaign was executed after freeze24. Root EM-DVR-4C90FB and the independently registered reviewer EM-ENTERPRISE-3F2857 have paper checked the main scalar sign and reverse operator. The q descent was supplied by that reviewer and independently derived by the author and Root; this is directed, shared mathematical work, not blind review.

## 1. Exact old JT2 observers and independently frozen target scalar

Let p=6m+1, p≡13 or19 mod24. Work over Z_p and the unramified quadratic ring with fixed s²=2, σ(s)=−s and x±=(2±s)/4. Keep the original full-level marking, branch and h/ω tags.

Set
\[
 a_n=\frac{(1/6)_n(1/3)_n}{(n!)^2},\quad
 b_n=\frac{(1/3)_n(2/3)_n}{(n!)^2},\quad
 f_p(w)=\sum_{n=0}^{p-1}a_nw^n,\quad
 L_p(x)=\sum_{n=0}^{p-1}b_nx^n .
\]
All displayed coefficient denominators are p-adic units. The exact old JT2 definitions are
\[
 B_i=a_i2^{-i},\qquad g=f_p(1/2),\quad
 h=\sum_{i=0}^{p-1}(12i+1)B_i=g+6f'_p(1/2),\quad G_p=g/p .
\]
The coefficient recurrence B_{i+1}/B_i=(6i+1)(3i+1)/(36(i+1)^2) is the same one in the old return. The inherited CM0/divisibility gives p|g.

The OLD target scalar, denoted R_p throughout this memo, is independently fixed before any new comparison:
\[
 R_p=
 2\sum_{i=1}^{m}B_i\sum_{r=1}^{i}
 (1+6(i-r))\,D_r\pmod p,\qquad
 D_r=\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r}.
 \tag{OLD-R}
\]
Here r≤m ensures every denominator is a unit; no inverse of a vanishing Hasse invariant is used. This is the already frozen reflected-tail scalar, not a definition from G_ph or U_p.

Source provenance at commit d9f1cc87019d8b43e7058b98f545c025bc753cfe:
- old JT2 return: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md; 9953 bytes, SHA256 54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827, blob cf36004694dc2c8c9134e2e1e989c076b88e4c03;
- OLD-R source: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md; 10919 bytes, SHA256 f2dde9c2d0411285d7cd449bd2853fae87b83b0c2a00cd4f57dcfcfe47a96483, blob 3fedf7bef09b426037840721855f9a9d05558a0b.

Both were connected full-file reads, locally preserved without semantic edits. The Taskbook/parent records and reduction certificate were also fully read and pinned in JT2_CURRENT_SOURCE_DEFINITION_PINS.json. Notation warning: the older reflected return calls g itself G_p; this memo uses the newer JT2 G_p=g/p.

## 2. Retained full carrier and scalar forcing

Write q=4x(1−x), t=1−2x and H=L_p modp. The primary proof gives
\[
 f_p(q)=L_p(x)+p^2x^pA_p(x)\pmod {p^3},
 \quad
 D_HA_p=-\frac29S_p,\quad
 D_H=x(1-x)\partial_x^2+(1-2x)\partial_x-\frac29,
\]
where S_p=Σ_{j=0}^{p-2}x^j and deg A_p≤p−2.
The separate global-reflection supplement proves A_p(1−x)=−A_p(x), and
\[
 A_p=I_p-\frac{I_p(1)}2H
     =\frac{I_p(x)-I_p(1-x)}2 .
\]
This is the full carrier, retaining the homogeneous seed needed for derivatives. Its value-specific cancellation at CM0 remains a separate fact.

The independently integrated Wronskian forcing T_* satisfies
\[
 T_*'= -\frac29 S_pH,\quad T_*(0)=T_*(1)=0,\quad
 T_* = x(1-x)(A_p'H-A_pH').
\]
At CM let τ_p=T_*(x+)∈F_p. Reflection gives this scalar membership. With
\[
 H'(x+)=\alpha_ps,\qquad A_p(x+)=\beta_ps,
\]
SIMPLE gives α_p∈F_p× and the Wronskian gives α_pβ_p=−4τ_p.

Define the exact observer
\[
 W_p(x)=L_p(x)+6L_p'(x)/q'(x)\pmod{p^2},
 \qquad q'(x+)=−2s ,
\]
and
\[
 U_p=\tfrac12\operatorname{Tr}
       [(L_p(x+)/p)W_p(x+)]\pmod {p^2}.
\]
The division by p uses L_p(x+) modp³; W_p needs modp². The finite transport gives W_p(x+)=h modp² and W_p modp=−3α_p. Also
\[
 \sigma(x+)A_p(x+)=\frac{\beta_p}{2}(s-1).
\]
Multiplying the correction by W_p modp and taking half trace gives
\[
 \boxed{G_ph=U_p-6p\tau_p\pmod {p^2}.}\tag{PAIR}
\]
The sign follows directly from α_pβ_p=−4τ_p and Tr(s)=0. This identity is finite arithmetic; it does not identify U_p with a geometric cup product by terminology.

## 3. Independent base-field symmetric input

The symmetric polynomial L_sym=(L_p(x)+L_p(1−x))/2 has a unique q-descended polynomial M_p(w)∈Z_p[w], deg M_p≤(p−1)/2. Define it independently, without reading f_p, G_p, OLD-R, I_p, B or the discrepancy:
\[
 S_0(w)=2,\quad S_1(w)=1,\quad
 S_n(w)=S_{n-1}(w)-\frac w4S_{n-2}(w),\qquad
 \boxed{M_p(w)=\frac12\sum_{n=0}^{p-1}b_nS_n(w).}\tag{M}
\]
The b_n are computed from their own rising-product recurrence. S_n(q)=x^n+(1−x)^n proves this definition. This independent M input is retained at modp³; its derivative is retained at modp².

Oddness of A and p odd give a unique C_p∈F_p[w],
\[
 A_p(x)=tC_p(q),\qquad \deg C_p\le(p-3)/2=3m-1 .
\]
C_p is NOT the old R_p. From subtracting the two branch polynomial identities,
\[
 L_p(x)=M_p(q)-\frac{p^2}{2}A_p(x)\pmod {p^3}.
\]
Consequently, using x^p=(1−t^p)/2 over F_p,
\[
 \boxed{f_p(w)=M_p(w)-\frac{p^2}{2}
       (1-w)^{(p+1)/2}C_p(w)\pmod {p^3}.}\tag{DESC}
\]
The polynomial substitution q has unit leading coefficient −4, so the descended identity follows coefficientwise, not just at selected points.

For χ_2(p)=−1 at the two target classes,
\[
 (1/2)^{(p+1)/2}\equiv-1/2\pmod p,
\]
and therefore
\[
 G_p=\frac{M_p(1/2)}p+\frac p4 C_p(1/2)\pmod{p^2},\qquad
 h=M_p(1/2)+6M_p'(1/2)\pmod{p^2}.\tag{OBS}
\]
At CM t+=−s/2, so C_p(1/2)=−2β_p and M_p'(1/2)=−α_p/2 modp. Thus
\[
 C_p(1/2)M_p'(1/2)=\alpha_p\beta_p=-4\tau_p.
\]
Moreover W_p(x+)=M_p(1/2)+6M_p'(1/2) modp² and
L_p/p=M_p/p−pA_p/2 modp². Since A_p has trace zero at CM,
\[
 \boxed{U_p=
 \frac{M_p(1/2)}p\bigl(M_p(1/2)+6M_p'(1/2)\bigr)
 \pmod {p^2}.}\tag{BASE-U}
\]
This saves the full marked branch information in the original state, while the scalar computation itself takes place in the base field.

## 4. A genuinely independent reverse Gauss definition of C_p

This is a new paper-derived computational interface. It uses only binomial forcing and units, not the discrepancy or a boundary fitted from I/H.

Direct differentiation yields
\[
 A'_p=-2C_p+4t^2C_p',\qquad
 A''_p=-24tC_p'+16t^3C_p'',
\]
where primes on C mean w derivatives. Hence
\[
 D_H(tC_p(q))=4tD_CC_p,\qquad
 D_C=w(1-w)\partial_w^2+
       (1-\tfrac52w)\partial_w-\tfrac59.
\]
This is the Gauss operator with parameters (2/3,5/6;1). Also
\[
 S_p(x)=\frac{4(x-x^p)}q
       =2t\frac{(1-q)^{3m}-1}{q},
\]
so
\[
 \boxed{D_CC_p=
 -\frac{(1-w)^{3m}-1}{9w}
 =\sum_{j=0}^{3m-1}r_jw^j,\qquad
 r_j=-\frac{(-1)^{j+1}}9\binom{3m}{j+1}.}\tag{FORCE}
\]
The apparent division by w is polynomial division; its numerator has zero constant coefficient.

Now define c_{3m}=0 and, DOWNWARDS for j=3m−1,...,0,
\[
 \boxed{c_j=
 \frac{(j+1)^2c_{j+1}-r_j}
      {(j+2/3)(j+5/6)},\qquad
 C^{rev}_p(w)=\sum_{j=0}^{3m-1}c_jw^j.}\tag{REVERSE}
\]
Modulo p, 2/3=2m+1 and 5/6=m+1. The denominator zeros are j=4m and5m, both strictly outside 0≤j≤3m−1. Every downward division is therefore a unit, including p=7,m=1. The coefficient of w^j in D_CC is (j+1)^2c_{j+1}−(j+2/3)(j+5/6)c_j, so (REVERSE) solves every equation, including the top equation.

Uniqueness follows by descending subtraction with the same unit multipliers and terminal c_{3m}=0. Since the descended primary carrier solves (FORCE) in the same degree range,
\[
 \boxed{C_p^{rev}=C_p.}
\]
Thus the full carrier is independently computable from one reverse, inhomogeneous Gauss recurrence. No α inverse, harmonic Fermat quotient, I(1), fitted C(1/2), or hidden old target equality enters its construction.

An additional exact independent equation for M is
\[
 D_GM_p=-\frac{(p-2/3)(p-1/3)b_{p-1}}8S_{p-1}(w),\qquad
 D_G=w(1-w)\partial_w^2+(1-\tfrac32w)\partial_w-\tfrac1{18}.
\]
It follows by applying D_H to L_sym and D_H(F∘q)=4(D_GF)∘q. Here S_{p-1} is the independently defined root-power polynomial of (M), not the geometric-series S_p. The exact identity is over Q with integral p-adic coefficients; Wilson b_{p-1}/p²=1 gives D_GM_p=−p²S_{p-1}/36 modp³. This equation does not alone evaluate the CM pairing.

## 5. Exact remaining old target, with no fitted side

Evaluate M and its derivative at 1/2 with the precisions specified above. Let U be (BASE-U), C be (REVERSE), and R_p be (OLD-R). Then
\[
 \mathrm{UR}\quad\Longleftrightarrow\quad U_p\equiv1\pmod p.
\]
Only after UR, the divided second digit is defined and
\[
 \mathrm{LIFT}\quad\Longleftrightarrow\quad
 \frac{U_p-1}{p}-6\tau_p=R_p\pmod p.
\]
Equivalently,
\[
 \boxed{\frac{M_p(1/2)}p
 (M_p(1/2)+6M_p'(1/2))
 \equiv1+p\left[R_p-\frac32C^{rev}_p(1/2)M_p'(1/2)\right]
 \pmod {p^2}.}\tag{INDEPENDENT-LIFT}
\]
The first M/p is an exact divided lift requiring M modp³. On the right C and M′ need only F_p. Old R_p remains independently defined; the formula does not assign its value from the left. Both original target classes remain required.

## 6. Concrete next bounded unit and failure criteria

The next unit can freeze three separate input constructors before comparison: the symmetric Hesse M recurrence (M), the reverse Gauss recurrence (REVERSE), and the pre-existing OLD-R sum. A new independent finite check on exactly p=13,19 with both marked branches can compare C^{rev} against the already frozen carrier bytes, verify M/DESC/BASE-U and compute the exact residual in (INDEPENDENT-LIFT). This is a new constructor comparison, not a repeat of the old prime campaign or a claimed all-prime proof. A mismatch in any coefficient, branch or second digit is a decisive counterexample to that new interface and must be saved without changing the normalization.

For proof work, the smallest first theorem is the all-prime first-digit U_p=1 modp for these independent M inputs. A candidate finite adjoint/creative-telescoping or independently normalized crystalline determinant must actually derive that evaluation. Merely naming U a cup pairing, treating an ordinary-unit-root formula as valid at supersingularity, or restating Gh=1+pR_p is not progress. The next precision theorem is exactly (INDEPENDENT-LIFT), with the independently computed Gauss correction retained.

There is a second independent geometric preparation file specifying how to compute a residue/cup normalization and Frobenius frame without fitting G or h. Root chooses and publishes the next bounded scope. The present author run is closed; this memo is paper preparation and does not reauthorize it.

Boundary: primary finite transport proved; directed independent primary review PASS; frozen Result awaits Driver disposition. Parent UR/LIFT, raw theta-period normalization, full marked crystalline identification and native global X6 propagation remain open. No mathematical objective was marked complete because a run ended.

