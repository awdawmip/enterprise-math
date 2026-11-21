# EC49FWA — Exact optimal translation defect of the rational-anchor certificate masks

**Research line:** EC49AS, independent portable continuation. **Frozen scientific input:** BRC16943 (unchanged Bernoulli-to-11-adic projective certificate). **Parent:** EC49FVZ at immutable commit \`ff12523630a3d1e236a9e7107db65bbf7363ad85\`, file \`research_notes/portable_direct/EC49FVZ_DIHEDRAL_CLASSIFICATION_THEOREM.md\`. **Date:** 2026-11-21. **Status:** AUTHOR_PROVED / EXACT_FINITE_CLASSIFICATION / PARENT_DEPENDENT / NOT_REVIEWED.

## Question and exact definitions

EC49FVZ classified rational anchors with a perfect fixed delay between the left and right denominator masks. Here we solve the quantitative alternative: **what is the smallest possible mismatch over all fixed delays**, including anchors without perfect reflection?

Retain the frozen predicate
\[
C_{11}(h,n)= {\bf1}_{(h\bmod10,n\bmod10)\in P_{10}}
{\bf1}_{9h+10n\not\equiv0\pmod{11}},
\]
where \(P_{10}\subset(\mathbb Z/10)^2\) is the **same 44-cell set** rebuilt from the eleven original projective rows, including the exceptional \(z=3\) row, in the verifier. Let \(0<a<b\), \(\gcd(a,b)=1\), and \(T=110b\). Define exact sets of denominator residue classes
\[
R_s(a,b)=\{q\pmod T : b\mid(aq+s),\
C_{11}((aq+s)/b,\ q-(aq+s)/b)=1\},\quad s=\pm1.
\]
They have equal size under the inherited sign symmetry. Define the **optimal symmetric-difference defect**
\[
D(a,b)=\min_{d\in\mathbb Z/T\mathbb Z}
\left|R_+(a,b)\mathbin{\triangle}(R_-(a,b)+d)\right|
\]
and \(N(a,b)\) as the number of translations achieving this minimum. These count denominator classes, not physical amplitudes, Bernoulli probabilities or accepted Foundation laws.

## Theorem — exact quantitative no-lag residue

Put
\[
\varepsilon(a,b)=
\begin{cases}
0,&2\mid b\text{ and }(5\mid a\text{ or }5\mid(2a-b)),\\
1,&\text{otherwise},
\end{cases}
\qquad
F(a,b)=\begin{cases}11,&11\mid(a+b),\\10,&11\nmid(a+b).\end{cases}
\]
Then for every reduced rational anchor \(0<a/b<1\),
\[
\boxed{D(a,b)=2\,\varepsilon(a,b)F(a,b).}
\]
Thus the **entire optimal defect spectrum is exactly \(\{0,20,22\}\)**. For a non-reflective anchor, its best translated left-mask and the right-mask differ at exactly 20 or 22 of the \(110b\) possible denominator positions (equivalently two entries on the primitive 10-position word, repeated by the appropriate 11-component).

The number of optimal translations is also explicit. Construct the mod-10 word \(U_{a,b}\) below; let
\[
\kappa(a,b)=\#\{c\bmod10:|U_{a,b}\triangle(c-U_{a,b})|
=\min_t|U_{a,b}\triangle(t-U_{a,b})|\}.
\]
Then
\[
\boxed{N(a,b)=\kappa(a,b)\cdot
\begin{cases}11,&11\mid(a+b),\\1,&11\nmid(a+b).\end{cases}}
\]
In particular \(\kappa\) belongs to \(\{1,2,4\}\); it equals 1 for the eight perfectly reflective classes, while the other 64 primitive mod-10 direction classes split as 24 with \(\kappa=1\), 24 with \(\kappa=2\), and 16 with \(\kappa=4\). The source verifier reconstructs \(\kappa\) for any supplied direction class, so this is an effective exact classification rather than an average bound.

## Proof

**1. Affine denominator transport and reflection.** Choose \(q_0\) with \(a q_0\equiv1\bmod b\), set \(h_0=(a q_0-1)/b\), \(n_0=q_0-h_0\). The minus candidates have \(q=q_0+bt\), \((h,n)=(h_0,n_0)+t(a,b-a)\) modulo \(T\). Let \(W(t)=C_{11}(h_0+at,n_0+(b-a)t)\), \(t\in\mathbb Z/110\mathbb Z\). The established identity \(C_{11}(-h,-n)=C_{11}(h,n)\) gives \(R_+=-R_-\). For any translation with nonzero intersection between \(R_+\) and \(R_-+d\), necessarily \(d\equiv-2q_0\bmod b\). Such a shift is uniquely parameterized by a reflection center \(c\bmod110\), and comparing the two denominator masks becomes comparing \(W(t)\) and \(W(c-t)\). A shift outside this congruence has disjoint masks and defect \(2|R_-|\ge80\); the construction below always achieves at most 22.

**2. Factor the 110-position word without losing the joint mask.** By CRT,
\[
W(t)=U(t\bmod10)\,V(t\bmod11),
\]
where \(U\) is the projective 44-cell word restricted to the primitive affine line
\((b-a)h-a n\equiv-1\bmod10\), and \(V\) is the mod-11 nonzero condition. If \(11\mid(a+b)\), \(V\) is identically one. Otherwise it has exactly one excluded residue among eleven. Both types possess a reflection center, and their maximum reflected-support intersection is respectively 11 or 10. This maximum can be reached simultaneously with any chosen mod-10 reflection center because CRT makes the centers independent. Hence
\[
D(a,b)= F(a,b)\,
\min_{c\bmod10}|U\triangle(c-U)|
\]
and the numbers of maximizing centers multiply.

**3. Exhaust the primitive direction classes.** The affine line is completely determined up to rotation of its word by the primitive direction \((a,b)\bmod10\). There are
\(10^2(1-2^{-2})(1-5^{-2})=72\) such classes. The exact verifier reconstructs all 44 projective cells from the frozen rational constants, forms all 72 ten-bit words, and checks all ten possible centers with integer arithmetic. It proves the following exhaustive histogram:

| Least mod-10 defect | Number of maximizing centers | Number of primitive directions |
|---:|---:|---:|
| 0 | 1 | 8 |
| 2 | 1 | 24 |
| 2 | 2 | 24 |
| 2 | 4 | 16 |

The eight zero-defect classes agree exactly with the EC49FVZ congruence criterion. Every other primitive class has **minimum defect 2**, completing the formula. This is a finite classification argument with all required states checked, not extrapolation from bounded rational denominators.

**4. Lift to mod 110.** Each primitive mod-10 direction has 120 primitive mod-110 lifts: 10 satisfy \(a+b\equiv0\bmod11\) (the mod-11 constant word), while 110 have a one-hole mod-11 word. Thus all \(8640\) primitive directions have exact defect histogram

| \(D\) | Primitive directions mod 110 |
|---:|---:|
| 0 | 960 |
| 20 | 7,040 |
| 22 | 640 |

For completeness, the optimal-shift multiplicity counts are \(D=0:N=1\) for 880 classes, \(D=0:N=11\) for 80; \(D=20:N=1,2,4\) for 2640,2640,1760; \(D=22:N=11,22,44\) for 240,240,160. These counts add to 8640.

## Reproduction, exact input and scope

The attached independent executable JavaScript verifier uses integer modular arithmetic, reconstructs \(P_{10}\) directly from
\[
U=\frac{4822040484}{8132285009},\qquad
\Gamma=\frac{141024}{1653649},\quad p=11,\quad 637,
\]
and compares \(C_{11}\) against all eleven original projective rows for every \(1\le h,n\le110\) (12,100 direct checks). It evaluates the complete 72-direction table, all 8640 mod-110 direction lifts and independently constructs the literal denominator masks over a period for all 277 reduced anchors with \(2\le b\le30\). The stored execution record says ALL PASS. These independent anchor checks validate implementation; the universal theorem follows from CRT plus the complete 72-class finite certificate.

Representative exact examples: \(a/b=1/2\) has \(D=0,N=1\); \(1/7\) has \(D=20\); \(1/10\) has \(D=22\). Perfect fixed-delay impossibility in the nonreflective cases is refined to a sharply quantified finite mismatch, without treating the defect as noise or discarding which signed denominator classes differ.

**Next mathematical question:** determine whether the 2-class primitive dihedral mismatch admits a short conceptual proof without the 72-class computation, and classify the cyclic positions of the two defects (including sign and orientation). Separately, determine whether the finite-residue quantification helps control moving Farey gaps; no new bound for the global \(HG_{\max}(H)\) conjecture is claimed.

**Publication boundary:** author proof and exact finite checker only; the inherited BRC16943 projective/Bernoulli bridge and P000 premises are kept at their existing pin and evidence strength. Independent review and native Task Result are pending; existing owner/CLAIM records are unchanged.
