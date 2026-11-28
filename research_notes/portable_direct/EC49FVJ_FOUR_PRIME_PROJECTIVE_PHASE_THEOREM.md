# EC49FVJ — Four-prime projective residual theorem for rational likelihood phases

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_FIELD_AND_CRT_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Scientific provenance and frozen input

Continues EC49FVI, science commit dcb080750ff13eb6fccd75b5281d47eb7afe4cb6, especially the mod-11 obstruction and the 11/17 union proof in research_notes/portable_direct/. The derived Bernoulli observer is pinned to BRC16943 (fc0f038e7bfd12c886b4d37f900bfb770c0f61ab). P000 and the ACTIVE six-axis worldview are unchanged. This is a theorem about the derived rational-width Bernoulli model; compound minimax transfer still depends on the separately unreviewed FUQ/FUR endpoint reduction.

For rational \(0<x<1\), take exactly the predecessor's fractions
\[
u=\frac{4822040484}{8132285009},\quad
\gamma=\frac{141024}{1653649},\quad
L_a(X)=\frac{637-3X}{637},\quad L_b(X)=u(1+\gamma X),
\]
\[
a(X)=1-(1-X)L_a(X),\qquad b(X)=1-(1-X)L_b(X),\qquad
R=\frac{1-a}{1-b},\quad S=\frac{b(1-a)}{a(1-b)},\quad
t(x)=\frac{\log R}{\log S}\in(0,1).
\]
The affine equality \(L_a(x)=L_b(x)\) occurs only at \(x=18335876195/2489980929>1\), so the denominator below is nonzero on our domain.

If \(t(x)=h/(h+n)\) for positive integers \(h,n\), then
\[
a(x)^hL_a(x)^n=b(x)^hL_b(x)^n.
\]
Define the exact polynomial divided difference
\[
G_{h,n}(X)=\frac{a(X)^hL_a(X)^n-b(X)^hL_b(X)^n}{L_a(X)-L_b(X)}\in\mathbb Q[X].\tag{1}
\]
The numerator is divisible by the affine denominator since the two terms coincide on the affine diagonal. Its degree is at most \(D=2h+n-1\). At each prime below all input denominators and the linear leading coefficient of \(L_a-L_b\) are units, so \(G_{h,n}\in\mathbb Z_{(p)}[X]\). A rational root would induce a root of the degree-\(D\) homogenization on \(\mathbb P^1(\mathbb F_p)\). This projective test includes rational widths whose reduced denominator is divisible by \(p\).

## Theorem A: new exact prime-local periodic exclusions

For \(p=19\) or \(31\), let \(T_p\) be the subset of ordered exponent residues \((h,n)\bmod(p-1)\) for which (1) is nonzero at all nonsingular finite field points and at infinity. Positive exponent representatives of zero residues are \(p-1\).

The following data are exact reductions and exhaustive counts; the final two rows are newly proved here.

| p | u mod p | γ mod p | singular z | common a=b | common L | singular coefficient αh+βn | \(\lvert T_p\rvert\) | certified classes modulo \(p(p-1)\), squared |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | 4 | 6 | 3 | 10 | 10 | 9h+10n | 44 | 4,840 / 12,100 |
| 17 | 3 | 16 | 4 | 8 | 8 | 7h+8n | 96 | 26,112 / 73,984 |
| **19** | **3** | **2** | **3** | **5** | **2** | **4h+5n** | **66** | **22,572 / 116,964** |
| **31** | **29** | **10** | **5** | **27** | **22** | **26h+27n** | **402** | **373,860 / 864,900** |

For either new prime and all positive \(h,n\), if
\[
(h\bmod(p-1),n\bmod(p-1))\in T_p,\qquad
\alpha_ph+\beta_pn\not\equiv0\pmod p,\tag{2}
\]
then
\[
\boxed{\forall x\in\mathbb Q\cap(0,1):\quad t(x)\ne h/(h+n).}
\]
The attached exact program reconstructs the entire finite set \(T_p\) from the given rational input, rather than relying on opaque fixed tables.

### Prime-local proof

At every finite point \(z\) where \(L_a(z)\ne L_b(z)\), evaluate \(G_{h,n}(z)\) by the ordinary quotient in (1). Each input residue is a polynomial expression in the fixed rational constants. For \(p=19\) and \(31\), \(L_a=L_b=L\) has exactly one solution \(z_p\), with \(a=b=A\ne0\) and \(L\ne0\). At that point the polynomial divided difference satisfies
\[
G_{h,n}(z_p)=L^{n-1}A^{h-1}[nA-h(1-z_p)L]\pmod p.\tag{3}
\]
Hence (3) is nonzero precisely when the linear condition in (2) holds.

Writing \(c=-3/637,\ d=u\gamma\), the reductions of \((c,d)\) are respectively \((3,2),(6,14),(13,6),(29,11)\) for \(p=11,17,19,31\); each has \(c\ne d\). At projective infinity the leading-degree coefficient of (1) is
\[
G_{h,n}^*(1,0)=\frac{c^{h+n}-d^{h+n}}{c-d}\pmod p.\tag{4}
\]
All nonsingular field values and (4) depend only on exponent residues modulo \(p-1\): for positive exponents zero bases stay zero and nonzero bases follow Fermat's theorem. Therefore the finite-field enumeration of \((p-1)^2\) base patterns is exhaustive. For each qualifying pattern, exactly \(p^2-p\) exponent-pair lifts mod \(p(p-1)\) satisfy (3), because (2) is one nonzero linear equation in two residues modulo \(p\). The projective zero-free criterion then excludes rational roots. QED.

Two strictly new reduced rational-phase witnesses are
\[
\boxed{t(x)\ne1/31\quad\text{and}\quad t(x)\ne7/26\quad
\text{for all rational }0<x<1.}
\]
The first is certified by \(p=19\), exponents \((1,30)\), but not by either 11 or 17. The second is certified by \(p=31\), exponents \((7,19)\), but not by 11, 17 or 19. Both have reduced phase denominator greater than the FVH bound 25.

## Theorem B: exact four-prime CRT union

Let \(C_p\) be the exponent residue-pair classes certified by (2). Define
\[
Q=\mathrm{lcm}(10,16,18,30)=720,\quad
M=Q\cdot11\cdot17\cdot19\cdot31=79,302,960.
\]
All four prime-local certificate conditions are periodic modulo \(M\) in each exponent. Every prime \(p\in\{11,17,19,31\}\) is coprime to \(Q\). Fix \((h,n)\bmod Q\), and let \(J\) be the set of primes for which this base pair lies in \(T_p\). CRT makes the singular congruences modulo distinct \(p\) independent; each one fails for exactly \(p\) of \(p^2\) choices. The conditional certified fraction is therefore exactly
\[
1-\prod_{p\in J}\frac1p,\quad\text{with the empty-set value }0.\tag{5}
\]

Exhaustive counts over the \(720^2=518400\) base pairs, using bit indices \(2^0,2^1,2^2,2^3\) for primes \(11,17,19,31\), respectively:

| Mask | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 111696 | 45792 | 56880 | 25632 | 12000 | 17280 | 7200 | 10368 |
| Mask | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
| Count | 51168 | 49344 | 32544 | 39744 | 11760 | 24960 | 7056 | 14976 |

Summing (5) over the 16 masks gives
\[
\boxed{\frac{|C_{11}\cup C_{17}\cup C_{19}\cup C_{31}|}{M^2}
=\frac{421142}{550715}\approx0.764718593101695.}
\]
Precisely **4,809,284,233,966,080 of 6,288,959,464,761,600** ordered exponent-pair residue classes modulo \(M\) are certified. The 11/17 predecessor's fraction \(564/935\) is recovered exactly. Adding prime 19 first gives \(34931/53295\); adding 31 yields an exact incremental gain over the 11/17 union of
\[
\boxed{\frac{421142}{550715}-\frac{564}{935}
=\frac{8086}{50065}\approx0.16151003695.}
\]

This fraction measures ordered **exponent residues**, not distinct reduced rational phases or rational detection widths. The prime-local singular linear defects are retained during CRT composition; their correlation with the base pattern and separate prime residues is precisely the information needed to avoid incorrect naive addition of marginal rates.

## Computation, independent review and next question

Attached Python 3 standard-library checker: EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_VERIFY.py. It reconstructs rational coefficients; enumerates every finite-field nonsingular base pattern at all four primes; cross-checks direct evaluations and positive-period shifts; verifies the preceding 11/17 counts; exhaustively counts 720² base masks and derives exact rational CRT coverage. Observed run returned ALL PASS. Exact stdout is saved in EC49FVJ_VERIFY_OUTPUT.txt.

The finite enumeration and the displayed exact identities certify the infinite periodic theorem as a finite computer-assisted proof. The mathematics remains AUTHOR_PROVED and NOT_REVIEWED. The complete compound minimax-risk transfer requires separately reviewing the predecessor FUQ/FUR endpoint reduction; neither this experiment nor Source publication is a canonical Result/Review/Working Truth promotion.

Next: derive the natural density of the certified set **among coprime exponent pairs**, using Möbius inversion with period \(M\), then compare that quantity with density among distinct reduced rational phases. Also investigate rational-width rational-phase witnesses in the remaining certificate complement.
