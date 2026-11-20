# EC49FVD — denominator certificates and coupled 7/13-adic residual obstruction

2026-11-21 (Asia/Shanghai) · AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Scientific scope and frozen provenance

Independent portable continuation of EC49FVC [PR #2871](https://github.com/awdawmip/enterprise-math/pull/2871) at immutable commit 8d803fd265b3b964ef7c78076a9b33a9c13cec76, frozen BRC16943 scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The claims concern the *derived Bernoulli hit observer*; they assert neither a complete native X6 state nor a physical time law. Irrationality of the log phase here is independent of the prior, unreviewed composite-minimax endpoint reduction.

Use exact frozen rational quantities
\[
\beta=\frac3{637},\quad \gamma=\frac{141024}{1653649},\quad u=\frac{4822040484}{8132285009},
\]
\[
T_0=(1-x)(1-\beta x),\quad T_E=(1-x)(1+\gamma x),\quad
a=1-T_0=\frac{x(640-3x)}{637},\quad b=1-uT_E,
\]
\[
R=\frac{T_0}{uT_E},\quad S=\frac{bR}{a},\quad t(x)=\frac{\log R}{\log S}.
\]
For rational \(0<x<1\) the frozen observer has \(0<a<b<1\) and \(1<R<S\), so \(0<t<1\). If \(t=h/k\in\mathbb Q\), then \(0<h<k\) and
\[
k v_p(R)=h v_p(S)\qquad\text{for every rational prime }p.\tag{*}
\]

## Theorem A — denominators divisible by 7 or 13

For every reduced rational \(x=m/d\in(0,1)\),
\[
\boxed{7\mid d\ \text{or}\ 13\mid d\quad\Longrightarrow\quad t(x)\notin\mathbb Q.}
\]

**Proof for 7.** If \(v_7(x)=-j\), \(j\ge1\), coefficient valuations are \(v_7(\beta)=-2\), \(v_7(\gamma)=v_7(u)=0\). Hence
\[
v_7(1-x)=-j,\quad v_7(1-\beta x)=-(j+2),\quad
v_7(1+\gamma x)=-j.
\]
It follows that \(v_7(T_0)=v_7(a)=-(2j+2)\) and \(v_7(T_E)=v_7(b)=-2j\). Thus \((v_7(R),v_7(S))=(-2,0)\), contradicting (*).

**Proof for 13.** If \(v_{13}(x)=-j\), then \(v_{13}(\beta)=-1\), \(v_{13}(\gamma)=1\), \(v_{13}(u)=0\). When \(j\ge2\), direct leading-term valuations give
\[
v_{13}(T_0)=v_{13}(a)=-(2j+1),\quad
v_{13}(T_E)=v_{13}(b)=-(2j-1),
\]
so \((v_{13}(R),v_{13}(S))=(-2,0)\).

For \(j=1\), put \(w=v_{13}(1+\gamma x)\ge0\). Then \(v_{13}(T_0)=v_{13}(a)=-3\), \(v_{13}(T_E)=w-1\), and \(v_{13}(R)=-2-w\). For \(w=0\), \(v_{13}(b)=-1\), so the pair is \((-2,0)\). For \(w=1\), \(v_{13}(b)\ge0\), yielding \((-3,v_{13}(b))\). For \(w\ge2\), \(v_{13}(b)=0\), yielding \((-2-w,1-w)\), whose entries are both negative, with the first strictly larger absolute magnitude. In every case (*) is impossible because \(0<h<k\). QED.

This covers the denominator cases omitted by the EC49FVC unit-residue statements. Coverage may overlap existing 29/673/416677/2/3 certificates; it is not a claim of disjoint novelty.

## Theorem B — two exceptional primes together give a certificate

Assume \(\gcd(md,91)=1\) and the old individual exceptional residues
\[
x\equiv99\pmod{343},\qquad x\equiv157\pmod{169},
\]
where rational congruence means \(m d^{-1}\) modulo each modulus. Define
\[
r=v_7(a)=v_7(640-3x)-2\ge1,\qquad
s=v_{13}(a)=v_{13}(640-3x)-1\ge1.
\]
The individual-prime FVC casework then gives
\[
(v_7(R),v_7(S))=(-2,-2-r),\qquad
(v_{13}(R),v_{13}(S))=(-1,-1-s).
\]
Thus rational \(t=h/k\) would simultaneously require
\[
\frac hk=\frac2{2+r}=\frac1{1+s}
\quad\Longrightarrow\quad\boxed{r=2s}.\tag{C}
\]
In particular, \(r=1\) immediately proves irrationality even though *neither individual exceptional prime* alone excludes rationality.

Since \(640-3x\) has the unique zero \(x\equiv1814\pmod{2401}\), precisely one of the seven lifts of \(x\equiv99\pmod{343}\) has \(r\ge2\); the other six have \(r=1\). The 13-adic exception remains the one residue \(x\equiv157\pmod{169}\). By CRT these two exceptional lifts intersect in exactly
\[
\boxed{x\equiv270726\pmod{405769}},\quad 405769=2401\cdot169.
\]
Therefore for \(\gcd(md,91)=1\), every unit class modulo 405769 *except this one* has irrational \(t\). There are
\(\varphi(2401)\varphi(169)=2058\cdot156=321048\) unit classes, of which **321047 are certified** by the joint 7/13 criterion. The remaining class is unclassified by this certificate, **not asserted rational**. All counts refer to modular residue classes, not real density.

### Optional 3-adic compatibility condition

If additionally \(3\nmid d\), \(3\mid m\), and \(q=v_3(m)\ge1\), exact valuations \(v_3(\beta)=v_3(\gamma)=1\), \(v_3(u)=6\) yield \((v_3(R),v_3(S))=(-6,-6-q)\). Coupling with (C), rationality would require
\[
\boxed{q=3r=6s}.\tag{D}
\]
This imposes a further exact necessary condition for those fractions; in particular a numerator valuation \(q\) not divisible by 6 rules out rationality.

## Explicit hard witness

The reduced rational
\[
\boxed{x=\frac{9422903036783328}{11313699962800873}}
\]
lies in **all five old coarse 2/3/29/673/416677 CRT exception classes** and in the *individual* 7- and 13-adic exception classes. To verify, put \(M=8132285009\), \(N=3\cdot8M=195174840216\), \(m_0=56925995064\); its denominator is \(d=1+57967N\), and its numerator satisfies \(m\equiv m_0\pmod N\), \(m d^{-1}\equiv38858\pmod{57967}\). Nevertheless,
\[
(v_7(R),v_7(S))=(-2,-3),\qquad
(v_{13}(R),v_{13}(S))=(-1,-2),
\]
which require contradictory rational values \(t=2/3\) and \(t=1/2\). This is a precise demonstration of the new *coupled-prime* certificate. It does not assert that all finer older single-prime lifts are inconclusive.

## Recalculation and next scientific question

Companion exact checker: research_notes/portable_direct/EC49FVD_DENOMINATOR_COUPLED_VERIFY.py. Standard-library Fraction and modular arithmetic checked all reduced \(0<m<d\le350\) with denominator divisible by 7 or 13, **4758** and **2568** instances respectively; checked the 405769-modulus CRT lift and the witness. These finite tests are arithmetic crosschecks; the infinite claims are proved by the displayed valuations.

Next: classify the remaining \(270726\bmod405769\) class with higher lifts and simultaneous valuation constraints, and test compatibility with the 3-adic numerator requirement. This project-native portable record preserves the source and does not claim an authenticated live Researcher, CLAIM, formal Result or Review.