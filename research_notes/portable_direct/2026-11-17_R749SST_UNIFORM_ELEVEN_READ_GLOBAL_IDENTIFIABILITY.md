# R749SST — Uniform eleven-read global identification of an unknown cutoff

Date: 2026-11-17. Status: **AUTHOR_EXACT_NOT_REVIEWED** (author's symbolic exact certificate PASS, independent mathematical review pending).
Mode: independent portable N2 five-distinct-labeled-source scalar observation research. Source science frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
Predecessors: R749SSJ (PR #2563, known-cutoff two-read calibration), R749SSR (PR #2585, no fixed-horizon uniform *noise* margin), and R749SSS (PR #2589, phase 2/4 fifth-order near alias). The latest fifth-order jet construction is **reused, generalized and sharpened in scope**, not recalculated as an independent novelty claim.

## Statement and hypotheses

Let the five *distinct, labeled* sources have weights \(w=(1,1,2,3,6)\), with the first unit-weight source marked. For integers \(q\ge6\), put
\[
\Omega_q=\{(k_1,\dots,k_5)\in\mathbb Z_{\ge0}^{5}:
k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{\Omega_q}k_1.
\]
With \(S(x)=18x^4+54x^3-345x^2+2070x-16315\), define
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\quad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]
Each candidate state has *real* \((e,d)\in[-2,2]^2\), fixed through that candidate's ordered six-step observations. Competing cutoffs may use independently chosen \((E,D)\).

**Theorem A (uniform exact global recovery).** For every distinct integers \(p,q\ge6\), and all permitted errors,
\[
\boxed{\mathcal O_q^{(11)}(e,d)\ne \mathcal O_p^{(11)}(E,D).}
\]
Consequently eleven exact ordered readings recover the cutoff \(q\) globally, without a prior upper bound on it. Combining this with the previously proved known-\(q\) two-read strict monotonicity in R749SSJ, the same eleven readings determine the entire triple \((q,e,d)\) uniquely.

**Theorem B (same asymptotic phase limit).** If \(\lim_{j\to\infty}Y_{q+6j}(e,d)=\lim_{j\to\infty}Y_{p+6j}(E,D)\), then **ten** reads are sufficient:
\[
\boxed{\mathcal O_q^{(10)}(e,d)\ne \mathcal O_p^{(10)}(E,D),\quad p\ne q.}
\]
The limits are independent of calibration and fall into the four classes
\[
r=q\bmod6:\quad L_0=455/36,\quad L_3=185/36,\quad
L_1=L_5=-295/36,\quad L_2=L_4=-25/36.
\]
These are **sufficient upper bounds**, not sharp minimal read counts.

## Proof 1: exact rational functions on each six-phase track

The labeled generating functions are
\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
After multiplication by \((1-z^6)^6\) and \((1-z^6)^7\), respectively, the numerators are
\[
z(1+z+\cdots+z^5)^3(1+z^2+z^4)(1+z^3),\quad
z^2(1+z+\cdots+z^5)^4(1+z^2+z^4)(1+z^3),
\]
of degrees 23 and 29. Coefficient extraction at \(q=6n+r\) gives exact polynomials \(C_r(x)\) of degree 5 and \(T_r(x)\) of degree 6. The binomial polynomials \(\binom{n-j+5}{5}\) (\(j\le3\)) and \(\binom{n-j+6}{6}\) (\(j\le4\)) vanish at each required early index \(0\le n<j\). Thus these polynomials hold for *all* integer cutoffs, not just finitely many interpolated inputs.

Put
\[
R_r(x;e,d)=\frac{N_r(x;e,d)}{C_r(x)+d},\quad
N_r=x^3(T_r(x)+e)-\frac{S(x)}{108}(C_r(x)+d).
\]
Exact coefficient cancellation reduces \(N_r\) to degree **5**. Hence \(R_r\) is a rational function with numerator/denominator degrees at most \((5,5)\), and it equals \(Y_x(e,d)\) for every integer \(x\ge6\) of residue \(r\).

For distinct \(p,q\), set \(r=q\bmod6,\ t=p\bmod6,\ h=p-q\ne0\). The difference
\[
F_{r,t,h}(x)=R_r(x;e,d)-R_t(x+h;E,D)
\]
has a polynomial numerator of degree at most 10. If \(L_r=L_t\), its leading degree-10 term cancels, so the numerator has degree at most 9. Since \(C_x\ge C_6>2\) and increases, all denominators at \(x=q+6j\), \(x+h=p+6j\) are strictly positive for allowed errors.

It remains to prove this rational difference is never identically zero for any compatible nonzero integer shift \(h\).

## Proof 2: universal nonidentity by five Laurent jets

When \(L_r\ne L_t\), equality as rational functions is impossible from their limits at infinity.

When \(L_r=L_t\), there are exactly ten ordered phase pairs: the six diagonal pairs \((r,r)\) and \((1,5),(5,1),(2,4),(4,2)\). Expand at infinity:
\[
F_{r,t,h}(x)=c_1x^{-1}+\cdots+c_5x^{-5}+O(x^{-6}).
\]
The first four coefficients are linear in \((d,e,D,E)\). Exact rational coefficient extraction gives the **same determinant for all ten pairs**:
\[
\boxed{\det\frac{\partial(c_1,c_2,c_3,c_4)}{\partial(d,e,D,E)}
=3224862720000\,h^2(3h^2+1445).}
\]
It is nonzero for every real \(h\ne0\). Therefore a hypothetical rational identity would force the unique real values solving \(c_1=c_2=c_3=c_4=0\), and would additionally require the resulting \(c_5=0\).

For the six diagonal pairs, exact substitution gives the following \(c_5\), each a nonzero multiple of \(h(\alpha h^2+\beta)\) with positive \(\alpha,\beta\):

| \(r=t\) | \(c_5\) after first-four-jet matching |
|---|---|
| 0 | \(1150h(258213h^2+6816674)/[9(3h^2+1445)]\) |
| 1 | \(100h(10664979h^2+243694783)/[27(3h^2+1445)]\) |
| 2 | \(10h(100428693h^2+2357398450)/[27(3h^2+1445)]\) |
| 3 | \(20h(15902457h^2+394064185)/[9(3h^2+1445)]\) |
| 4 | \(10h(100279653h^2+2405588050)/[27(3h^2+1445)]\) |
| 5 | \(100h(10679883h^2+238875823)/[27(3h^2+1445)]\) |

For the four off-diagonal equal-limit pairs, the exact fifth coefficients have denominator \(27(3h^2+1445)\) and numerators:

| \((r,t)\) | Numerator of matched \(c_5\) |
|---|---|
| (1,5) | \(-100(414h^4-10672431h^3+276630h^2-241285303h+1201140)\) |
| (5,1) | \(100(414h^4+10672431h^3+276630h^2+241285303h+1201140)\) |
| (2,4) | \(10(4140h^4+100354173h^3+2756580h^2+2381493250h+7329600)\) |
| (4,2) | \(-10(4140h^4-100354173h^3+2756580h^2-2381493250h+7329600)\) |

Each parenthesized quartic reduces to \(+h\) or \(-h\) **modulo 3**. Compatibility with the two different phase residues imposes \(h\equiv t-r\pmod6\), so \(h\not\equiv0\pmod3\). Every quartic is therefore a *nonzero integer*. This proves \(c_5\ne0\) for all compatible integer shifts. The proof does not require the calibrated errors to lie inside the allowed square: nonidentity actually holds for all real parameters whenever the rational functions are defined.

The fifth-order obstruction includes and extends R749SSS's phase-2-versus-phase-4 \(h=2\) result, and explicitly handles all shifts and same-phase pairs.

## Proof 3: root counting and full-state recovery

If two length-11 observations were equal, the numerator of \(F_{r,t,h}\) would have eleven distinct roots \(q,q+6,\dots,q+60\). A nonzero polynomial of degree at most ten cannot have eleven distinct roots. This contradicts Proof 2 and proves Theorem A. When \(L_r=L_t\), the degree bound is nine and ten distinct roots suffice, proving Theorem B.

Finally, for known \(q\), invert each \(Y\) reading to \(X=(Y+S(q)/108)/q^3\). R749SSJ proved \(X(q+6;e,d)-X(q;e,d)>1\) for all \(q\ge6\) and \((e,d)\in[-2,2]^2\). The two equations \(e-X_0d=X_0C_q-T_q\) and \(e-X_1d=X_1C_{q+6}-T_{q+6}\) have a nonzero determinant \(X_1-X_0\). Hence two exact readings recover \((e,d)\) after \(q\) is known, proving full-triple identification.

## Verification, scope and transfer

The paired Python/SymPy certificate reconstructs exact \(C_r,T_r\), checks 24 direct labeled enumerations, verifies the six numerator degrees and phase limits, checks all ten determinant/fifth-coefficient identities in \(\mathbb Q(h)\), proves the modular exclusions, and checks 585 exact sample instances of known-\(q\) strict monotonicity as a supplemental test. Local author execution: **PASS**. Independent review is pending.

This is a *global exact injectivity theorem* for this auxiliary scalar observer, not a uniform positive measurement-noise claim. The previous no-uniform-noise results R749SSR/SSS remain in force: even infinitely many readings can admit arbitrarily close streams at large cutoff.

The five source labels, common calibration inside each trajectory, time/read ordering and complete observer fibres are explicitly retained. This N2 observation result does not itself define a native P000 X6 event or BRC Cell/Link/Port transition. A native transfer requires an explicit typed carrier, forward-operation law and fibre-preservation certificate.

**Next questions:** tighten the global sufficient horizon 11 (e.g. rule out five-read collisions with algebraic elimination or a Chebyshev/variation-diminishing argument); obtain cutoff- and observation-budget-dependent minimax noise bounds; build a typed provenance-preserving BRC observer state and identify its minimal future-observation repair coordinate.
