# EC49FVC — 7-adic and 13-adic exact certificates for irrational likelihood lattice phases

Date: 2026-11-21 (Asia/Shanghai). Research status: **AUTHOR_PROVED / EXACT_RATIONAL_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED**.

## Sources, scope and typing

Independent portable continuation of EC49FVB [Draft PR #2870](https://github.com/awdawmip/enterprise-math/pull/2870), immutable scientific predecessor \`239d0e8a1016d7f3469f7ae368cffe468a82cd49\`; earlier EC49FVA [PR #2868](https://github.com/awdawmip/enterprise-math/pull/2868). Scientific input remains frozen **BRC16943** at \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Current operational rules and P000 remain separate from the frozen Bernoulli scientific constants.

This is an **exact arithmetic theorem about a derived Bernoulli hit observer**, not a complete native six-axis X6 dynamical/temporal model, not a projection preserving all future native observations, and not a claim of physical time or a native space reduction. A rational prime-valuation vector is an exact carrier for this stated irrationality test; the logarithmic phase is a derived readout. The theorem itself is independent of the earlier composite-minimax endpoint-reduction proof. Transfer of any second-order minimax or least-favorable-prior conclusions to the complete composite game remains conditional on the author-proved, not independently reviewed EC49FUQ/FUR reductions.

## Frozen definitions

Let \(x=m/d\in(0,1)\) be a **reduced positive rational** with \(0<m<d\), and set
\[
\beta=\frac3{637},\qquad \gamma=\frac{141024}{1653649},
\qquad u=\frac{4822040484}{8132285009}.
\]
Use exactly the predecessor's rational functions
\[
T_0=(1-x)(1-\beta x),\quad
T_E=(1-x)(1+\gamma x),\quad
a=1-T_0=x(1+\beta-\beta x),\quad b=1-uT_E,
\]
\[
R=\frac{T_0}{uT_E},\quad S=\frac{bT_0}{auT_E}=\frac{bR}{a},
\qquad t(x)=\frac{\log R}{\log S}.
\]
The frozen model's strict ordering \(0<a<b<1\) gives \(1<R<S\), hence \(0<t(x)<1\).

If \(t(x)=h/k\in\mathbb Q\) in lowest terms, then \(0<h<k\) and
\[
R^k=S^h\quad\Longrightarrow\quad
k v_p(R)=h v_p(S)\tag{*}
\]
for **every rational prime** \(p\). We produce explicit valuations that contradict (*) for \(p=7\) or \(p=13\). No logarithmic numerical approximation is used for the infinite-family proof.

## Theorem A: 7-adic certificate modulo 343

For every reduced rational \(x=m/d\in(0,1)\) with \(7\nmid md\),
\[
\boxed{m d^{-1}\bmod343\ne99\quad\Longrightarrow\quad t(x)\notin\mathbb Q.}
\]
Thus **293 of the 294 7-adic unit residue classes** modulo \(343=7^3\) have this certificate. The remaining class \(99\) is unresolved **by this theorem**, not asserted rational.

**Proof.** The exact frozen constants satisfy
\[
v_7(\beta)=-2,\quad v_7(\gamma)=v_7(u)=0,
\quad v_7(1+\gamma)=0.
\]
All rational fractions below have 7-unit numerator and denominator.

**Case I: \(x\not\equiv1\pmod7\).** Put \(j=v_7(1+\gamma x)\ge0\). Because \(1-x\) is a unit, \(1-\beta x\) has valuation \(-2\), and \(a=x(1+\beta-\beta x)\) has valuation \(-2\).
Consequently
\[
v_7(R)=-2-j.
\]
If \(j=0\), then \(b=1-uT_E\) is 7-integral and
\[
(v_7(R),v_7(S))=(-2,v_7(b)),\qquad v_7(b)\ge0.
\]
If \(j\ge1\), then \(T_E\) has positive 7-adic valuation, so \(b\) is a unit and
\[
(v_7(R),v_7(S))=(-2-j,-j).
\]
Both patterns contradict (*) with \(0<h<k\): in the first case a negative cannot equal a nonnegative valuation after positive multiplication; in the second case the magnitude of the negative left valuation is strictly larger than the right.

**Case II: \(x\equiv1\pmod7\).** Put \(j=v_7(1-x)\ge1\). Since \(1+\gamma x\) is a 7-unit, one has \(v_7(R)=-2\). Meanwhile \(T_E\) has positive 7-adic valuation, so \(v_7(b)=0\). Write
\[
a=x\left(1+\frac3{49\cdot13}(1-x)\right).
\]
If \(j=1\), then \(v_7(a)=-1\), yielding \((v_7(R),v_7(S))=(-2,-1)\).
If \(j\ge3\), then \(v_7(a)=0\), giving \((-2,-2)\).
If \(j=2\), put \(z=(1-x)/49\), a 7-adic unit. Then
\[
a=x(1+3z/13),\quad
a\equiv0\pmod7\iff z\equiv-13/3\equiv5\pmod7.
\]
This is equivalent to \(x=1-49z\equiv1-245\equiv99\pmod{343}\).
Outside the residue 99, \(v_7(a)=0\), giving \((-2,-2)\). Each listed nonexceptional valuation pair violates (*). This proves the theorem. \(\square\)

## Theorem B: 13-adic certificate modulo 169

For every reduced rational \(x=m/d\in(0,1)\) with \(13\nmid md\),
\[
\boxed{m d^{-1}\bmod169\ne157\quad\Longrightarrow\quad t(x)\notin\mathbb Q.}
\]
Thus **155 of the 156 13-adic unit residue classes** modulo \(169=13^2\) are certified; the class \(157\) is unresolved by this criterion.

**Proof.** The exact constants give
\[
v_{13}(\beta)=-1,\qquad v_{13}(\gamma)=1,\qquad v_{13}(u)=0.
\]
Since \(x\) is a 13-unit, \(1+\gamma x\) is a unit.

**Case I: \(x\not\equiv1\pmod{13}\).** Now \(1-x\) is a unit and \(1-\beta x\) has valuation \(-1\). Thus \(v_{13}(R)=-1\) and
\(v_{13}(a)=-1\). Since \(uT_E\) is 13-integral, \(v_{13}(b)\ge0\). Therefore
\[
(v_{13}(R),v_{13}(S))=(-1,v_{13}(b)),\qquad v_{13}(b)\ge0,
\]
contradicting (*).

**Case II: \(x\equiv1\pmod{13}\).** Let \(j=v_{13}(1-x)\ge1\). Now \(v_{13}(R)=-1\), \(v_{13}(b)=0\), and
\[
v_{13}(S)=-1-v_{13}(a),\qquad
a=x\left(1+\frac3{13\cdot49}(1-x)\right).
\]
For \(j\ge2\), \(a\) is a unit, yielding \((-1,-1)\), incompatible with \(0<h<k\).
For \(j=1\), write \(z=(1-x)/13\), a unit. Then
\[
v_{13}(a)>0
\iff 1+3z/49\equiv0\pmod{13}
\iff z\equiv-49/3\equiv1\pmod{13}.
\]
The exceptional class is \(x\equiv1-13=157\pmod{169}\). For every other residue, \(a\) is a unit and \((v_{13}(R),v_{13}(S))=(-1,-1)\), proving the theorem. \(\square\)

## Corollary: one exceptional CRT class among 45,864 units

For reduced rational widths with \(\gcd(md,91)=1\), the 7- or 13-adic certificate proves irrationality unless **both**
\[
x\equiv99\pmod{343},\qquad x\equiv157\pmod{169}.
\]
By the Chinese remainder theorem these two are equivalent to
\[
\boxed{x\equiv38858\pmod{57967}},\qquad 57967=343\cdot169.
\]
The total number of classes in \((\mathbb Z/57967\mathbb Z)^\times\) is
\(\varphi(343)\varphi(169)=294\cdot156=\boxed{45864}\).
Exactly **45,863** classes receive a certificate, and **one** is not covered by this paired-prime criterion. This is a count in the rational unit-residue parameter space, **not** a real-density statement or a uniform asymptotic statement.

The present two primes do not replace the earlier 29/673/416677/2/3 sieve; their covered populations overlap and neither proof automatically handles fractions having 7 or 13 in the reduced numerator/denominator.

### A strictly new witness beyond the predecessor's five-prime *coarse* CRT sieve

Take the **exact rational width**
\[
\boxed{x=\frac{56925995064}{195174840217}}.
\]
Let \(M=8132285009\), \(L=8M=65058280072\), and \(N=3L=195174840216\). Here \(\gcd(m,d)=1\), \(d=N+1\), and therefore \(d\equiv1\pmod{N}\). The numerator satisfies
\[
m\bmod M=1,\quad m\bmod8=0,\quad m\bmod3=0.
\]
Thus it lies in one of the 40 classes **left open by the five-prime coarse CRT sieve** of EC49FVB. Yet the new prime produces
\[
\boxed{(v_{13}(R),v_{13}(S))=(-1,0)},
\]
which contradicts (*) immediately. This establishes that the present theorem supplies an actual new arithmetic certificate, not just another tally of previously covered residues. It does not assert that no other previously available higher-lift method could certify this same fraction.

## Reproducible exact validation

Companion code: \`research_notes/portable_direct/EC49FVC_SEVEN_THIRTEEN_ADIC_SIEVE_VERIFY.py\`. Pure standard-library \`fractions.Fraction\` arithmetic, rational valuations and modular inverses; no floating-point inference.

**Actual executed local results**:
\`\`\`
EXACT_FINITE_CROSSCHECK_PASS {7: 23390, 13: 26653} CRT_exception=38858 mod57967 unit_classes_certified=45863/45864
STRICT_NEW_WITNESS 56925995064/195174840217 v13 (-1, 0)
\`\`\`
The finite checker exhausts every reduced \(0<m<d\le320\), for each prime wherever its respective hypotheses hold and the excluded residue does not, and verifies both valuations contradict the equation (*). It also recomputes exact valuations at representative rational widths. The general theorems follow from the two written 7-/13-adic case splits; the finite tests cross-check their arithmetic.

The GitHub artifact and its checker are **author-side research**, not independently reviewed or canonically admitted, and not a Source-native CLAIM, Result or Review. Historical authors retain provenance; a new execution session is not inferred from an old Researcher ID. Current source observation of \`RS-EC49AS\` is \`NO_CANONICAL_PUBLICATION_DIRECTORY\`, which is a scoped task-directory observation, not a complete owner projection.

## Next exact scientific questions

Extend the paired-prime sieve to fractions with 7/13-divisible numerator or denominator; derive the valuation structure in the single surviving unit CRT class \(38858\bmod57967\); and use the 7/13 witnesses together with the earlier five-prime CRT sieve to describe the *intersection* of all exceptions, without changing the frozen Bernoulli scientific input. A separate useful direction is effective and uniform second-order phase-error bounds for variable widths, with the existing unreviewed composite minimax reduction kept explicitly conditional.
