# EC49FVB — Three-adic strengthening of the rational-width phase sieve

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / NOT_REVIEWED.
Frozen scientific input BRC16943 @ fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Part of EC49FVB PR #2870; extends its 29/673/416677/2-adic sieve without changing the signed native X6 model.

## Theorem

Under the exact EC49FVB Bernoulli hit-readout constants
\[
\beta=3/637,\ \gamma=141024/1653649,\ u=4822040484/8132285009,
\]
and definitions \(T_0=(1-x)(1-\beta x)\), \(T_E=(1-x)(1+\gamma x)\),
\(a=1-T_0\), \(b=1-uT_E\),
\(R=T_0/(uT_E)\), \(S=bT_0/(auT_E)\),
\(t(x)=\log R/\log S\in(0,1)\),
the phase is irrational for every reduced rational \(x=m/d\in(0,1)\) in any of the following three exact classes:

1. \(3\nmid m d\) (numerator AND denominator are 3-units).
2. \(v_3(d)\ge2\).
3. \(v_3(d)=1\) and the 3-unit \(3x=m/(d/3)\equiv2\pmod3\).

More precisely the valuation pairs \((v_3(R),v_3(S))\) are:

- Class 1: \((-6,-6)\).
- Class 2, with \(j=v_3(d)\ge2\): \((-6,2j-7)\) for \(j=2,3\), and \((-6,0)\) for \(j\ge4\).
- Class 3: \((-6-\kappa,-5-\kappa)\), where \(\kappa=v_3(1+\gamma x)\ge1\).

Every pair contradicts \(k v_3(R)=h v_3(S)\) for a rational \(t=h/k\) with \(0<h<k\).

**Five-prime CRT corollary.** Set \(L=8\cdot29\cdot673\cdot416677=65,058,280,072\), and let \(\mathcal H\) be the eight formerly unresolved residues mod \(M=L/8\). The four-prime sieve leaves at most 40 of L residue classes with \(\gcd(d,L)=1\). For \(\gcd(d,3L)=1\), the present 3-adic certificate excludes all those with \(x\bmod3=1\) or \(2\). Thus among **\(3L=195,174,840,216\)** residue classes for denominators coprime to \(3L\), only **40** coarse CRT classes are not certified, i.e. **195,174,840,176 certified classes**. The exceptions obey simultaneously \(x\bmod L\) in the earlier 40-class set and \(x\bmod3=0\). This is a count of modular classes, not a real-density statement.

The new theorem additionally handles all reduced rational widths with \(v_3(d)\ge2\) or \(v_3(d)=1\) and \(3x\bmod3=2\), even when their numerator/denominator ratio falls into a formerly exceptional L-class. The case \(v_3(d)=1,\ 3x\bmod3=1\) is *not* declared universally certified by this 3-adic argument.

## Proof

Write \(v=v_3\). The exact constants satisfy
\[
v(\beta)=1,\quad v(\gamma)=1,\quad v(u)=6.
\]
If \(3\nmid d\), the factors \(1-\beta x\), \(1+\gamma x\) are 3-units, so their ratio is a unit. Thus \(v(R)=-6\). Also \(v(uT_E)\ge6\), giving \(v(b)=0\), while \(v(a)=v(x)\) because \(1+\beta-\beta x\) is a unit. If \(3\nmid m\) as well, \(v(a)=0\), hence \(v(S)=-6\). This proves class 1.

Let \(3\mid d\), and write \(v(x)=-j\), \(j=v_3(d)\ge1\). If \(j\ge2\), both \(\beta x\) and \(\gamma x\) have valuation \(1-j<0\), so
\[
v(T_0)=v(T_E)=v(a)=1-2j,\quad v(R)=-6.
\]
The exponent of \(uT_E\) is \(7-2j\). For \(j=2,3\) it is positive, and \(b=1-uT_E\) is a unit, so
\[
v(S)=v(R)-v(a)=2j-7.
\]
For \(j\ge4\), \(7-2j<0\), giving \(v(b)=7-2j\) and hence \(v(S)=0\). This proves class 2.

For \(j=1\), put \(z=3x\), a 3-adic unit. Reducing the exact coefficients gives
\[
\beta x\equiv z\pmod3,\qquad \gamma x\equiv z\pmod3.
\]
When \(z\equiv2\), \(1-\beta x\) is a unit but \(1+\gamma x\) is divisible by 3, with \(\kappa=v(1+\gamma x)\ge1\). Moreover \(v(1-x)=-1\), \(v(T_0)=-1\), \(v(T_E)=-1+\kappa\), and \(v(a)=-1\). As \(v(uT_E)=5+\kappa>0\), \(b\) is a unit, yielding
\[
(v(R),v(S))=(-6-\kappa,-5-\kappa).
\]
This proves class 3. In each class the rational-phase valuation equation is impossible because its left coefficient k exceeds h while the listed signed valuations are either identical nonzero, of unequal signs, zero/nonzero, or both negative with the first strictly more negative.

For the CRT claim, denominators coprime to 3L admit independent residues modulo L and modulo 3. Each one of the 40 old L-exception classes has three lifts modulo 3L, and the two 3-unit residues are excluded by class 1, leaving just 40. All other classes are certified by the pre-existing L-sieve.

## Verification and next step

The exact Python Fraction checker EC49FVB_THREE_ADIC_REFINEMENT_VERIFY.py was executed and returned ALL PASS. It independently recalculates the coefficient 3-adic valuations and, over all reduced fractions \(0<m<d\le240\), verifies 8,760 samples from class 1, 1,416 samples from class 2, and 1,494 from class 3. It checks the CRT counts with exact integers. The infinite theorem is the case analysis above; finite checks are arithmetic crosschecks.

The phase \(t(x)\) is a derived logarithmic observer; the exact input is rational finite-prime valuation data, not a native X6 event or physical time. Downstream transfer to full composite minimax remains conditional on the EC49FUQ/FUR author proofs and independent review. No current authenticated Researcher/Activity or CLAIM was created.

**Next:** analyze the fine exceptional \(v_3(d)=1,\ 3x\equiv1\) cases, and inspect the 40 CRT survivors using new prime valuations or higher powers; determine whether any rational-width phase is rational at all.