# R749SSM — Exact local four-read separation of unknown cutoffs 7 and 8

**Date:** 2026-11-16. **Mathematical status:** AUTHOR_EXACT_NOT_REVIEWED.
**Frozen science:** a72226e2430ffa4786321ac86e7f0c599d5f0389; continue R749SSK–SSL on [PR #2566](https://github.com/awdawmip/enterprise-math/pull/2566), immutable commit cff1f9e3a101d9291a505dfa8990df76775597e0. The immutable pin is not rebased by current behavioral-policy reads.

## Model and theorem

For the five labeled-source weights (1,1,2,3,6), let

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q} k_1.
\]

Let \(S(q)=18q^4+54q^3-345q^2+2070q-16315\) and define

\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\qquad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]

The *same* real calibration pair \((e,d)\in[-2,2]^2\) is used for every read of a given state. The provenance label \(q\) is unknown to the observer.

**Exact theorem.** The two four-read image sets are disjoint:

\[
\boxed{\mathcal O_7^{(4)}([-2,2]^2)\cap\mathcal O_8^{(4)}([-2,2]^2)=\varnothing.}
\]

R749SSL gives an exact three-read intersection for this pair, so **four is the smallest number of consecutive six-shift observations that always distinguishes the pair of cutoffs 7 and 8**, uniformly over both real error squares. The algebraic four-read obstruction needs only \(|d|\le2\) on the cutoff-7 side (and defined denominators), without bounds on the numerator errors or cutoff-8 error pair.

## Full exact source anchors

| q | C_q | T_q |
|---:|---:|---:|
| 7 | 65 | 91 |
| 8 | 98 | 156 |
| 13 | 506 | 1261 |
| 14 | 662 | 1767 |
| 19 | 2106 | 7447 |
| 20 | 2576 | 9553 |
| 25 | 6331 | 28883 |
| 26 | 7441 | 35214 |

They follow from the labeled generating function \(\prod_{w\in(1,1,2,3,6)}(1-z^w)^{-1}\), with exact prefix sums. The companion certificate reconstructs them from the source weights, rather than taking them as unchecked inputs.

## Derivation of two necessary determinant equations

Suppose a four-read collision exists between cutoff \(q=7\) with \((e,d)\) and cutoff \(p=8\) with \((e',d')\). At index \(j=0,1,2,3\) write \(q_j=7+6j\), \(p_j=8+6j\), and put

\[
V_j=p_j^3(C_{q_j}+d),\qquad
U_j=q_j^3(T_{q_j}+e)+\frac{S(p_j)-S(q_j)}{108}(C_{q_j}+d).
\]

The raw cutoff-8 ratio required by the shared smoothed read is \(x_j=U_j/V_j\), so

\[
e'-x_jd'=x_j C_{p_j}-T_{p_j}.
\]

Each \(V_j>0\) on \(|d|\le2\). Multiply the equation by \(V_j\). Its augmented row is

\[
L_j=(V_j,-U_j,C_{p_j}U_j-T_{p_j}V_j).
\]

Any triple of compatible rows must have determinant zero. In particular,

\[
H_2(e,d)=\det(L_0,L_1,L_2)=0,\quad
H_3(e,d)=6\det(L_0,L_1,L_3)=0.
\]

No division by a difference of observed values is used, so there is no exceptional inverse denominator. Both are bivariate integer polynomials of degree two in \(e\) and at most three in \(d\).

Express \(H_i=a_i(d)e^2+b_i(d)e+c_i(d)\). The complete integer coefficients are:

~~~
a2 = -25999464658656 - 2170402847280*d
b2 = 25665881152213864 + 3818332725903764*d + 8517190893192*d^2
c2 = -45032970208568420 - 49829920474516588*d
     - 4939292865911139*d^2 + 923243492481*d^3

a3 = -2376041366849184 - 111784049774064*d
b3 = 2145129655398174560 + 315754546776127640*d + 531210657740480*d^2
c3 = -851458936224224926 - 4586875289048978667*d
     - 423838272588088662*d^2 + 55771703467759*d^3
~~~

## Resultant and uniform sign proof

For quadratic polynomials \(f=ae^2+be+c\) and \(g=Ae^2+Be+C\),

\[
\operatorname{Res}_e(f,g)
=(aC-Ac)^2-(aB-Ab)(bC-Bc).
\]

Exact multiplication of the foregoing polynomial coefficients gives

\[
\boxed{
\operatorname{Res}_e(H_2,H_3)
=-67436544(d+65)(d+506)(234443938d+1569882365)\,Q(d).
}
\]

Writing \(Q(d)=A_0+A_1d+\dots+A_5d^5\), its exact coefficients from constant to leading are:

~~~
A0 = 109796349314075020060949372306640574723358682
A1 = -38045439719073116059985350517020931359464817
A2 = -2277402286244385991893563886215342942920759
A3 = 923053369069668327403631270396371444479035
A4 = 14501898594290005726122391371730051335594
A5 = 175742992512176288201620423729874424
~~~

For every *real* \(|d|\le2\), the triangle inequality yields the strict integer bound

\[
Q(d)\ge A_0-\sum_{i=1}^{5}2^i|A_i|
=\boxed{16979397777109496872916184850765128499562660}>0.
\]

The other factors satisfy \(d+65\ge63\), \(d+506\ge504\), and
\(234443938d+1569882365\ge1100994489\). Therefore the resultant is never zero for the permitted cutoff-7 denominator error. A common root \(e\) of \(H_2,H_3\) would force a vanishing resultant. This proves the four-read separation for **all real permitted errors**, without mesh sampling or floating-point approximation.

Because the two error squares are compact and both smooth-observer maps are continuous on them, the disjoint four-read image sets have positive minimum distance in any fixed finite-dimensional norm. No *numerical* optimal noise radius is asserted.

## Sharpness: the known three-read collision

At cutoff 7, R749SSL uses \((e,d)=(e_*,-1)\) with \(e_*\) the unique root in \((0,1/100)\) of

\[
P(e)=5957265452844e^2-5464016404300823e+35816460863863.
\]

The exact inverse parameter pair at cutoff 8 lies in \(1<e'<2\), \(-1<d'<0\), and its first three observations agree because the exact compatibility determinant is \(-P(e)/191164619161600000\). The preceding source gives the complete parameter inequalities and proof. Hence three reads can collide, while four never do. Every shorter horizon inherits the three-read collision by truncation.

## Certificate and scientific boundary

The companion standard-library-only Python file *R749SSM_FOUR_READ_PAIR_SEPARATION_CERT.py* implements integer source enumeration, rational bivariate polynomial determinants, a complete integer resultant identity, and the strict positivity calculation. Its companion PASS JSON contains the exact coefficients, counts, and lower bound. The certificate has been locally executed with Python 3; the proof uses no uncertain numerical roots.

**Evidence state:** AUTHOR_EXACT_NOT_REVIEWED, with a complete reproducible author proof, pending independent mathematical review. The result is a narrowly typed scalar Walsh source-observer theorem. It is not a native X6/Heartbeat-time law or a verified typed BRC Port mapping. Source labels, the common error relation and observation ordering are preserved. The current P000, ACTIVE worldview and joint-relation observer-preservation conditions remain in force for any subsequent native embedding.

**Next questions:** classify the four-read image intersections for other cutoff pairs; derive an explicit rational noise margin for the \(\{7,8\}\) pair; and separately establish or refute unknown-cutoff identifiability for integer bounded errors. A later BRC/Port embedding will require a proved map preserving future-observer fibres, not only matching a scalar value.
