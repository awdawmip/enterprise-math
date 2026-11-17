# R749SSZ — Exact two-read phase collisions and a future-observer residual

**Date:** 2026-11-17. **Evidence level:** AUTHOR_EXACT_NOT_REVIEWED; an exact SymPy author certificate was executed locally. Independent review remains open. **Mode:** portable, independently derived auxiliary scalar research (no native X6 CLAIM/Result/Review).

**Frozen input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Precursors:** R749SST (six-phase quasipolynomials and global 11-read sufficiency), R749SSV (phase limits), R749SSW (known-q inversion), R749SSY (four limit classes distinguished by one reading for q>=501). All original review statuses are retained.

## Model and question

Keep five distinct labeled sources with weights \(w=(1,1,2,3,6)\). For integer \(q\ge6\),

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
\[
S(q)=18q^4+54q^3-345q^2+2070q-16315,\qquad
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108}.
\]
\[
\mathcal O_q^{(m)}(e,d)=
(Y_q(e,d),Y_{q+6}(e,d),\ldots,Y_{q+6(m-1)}(e,d)),
\qquad(e,d)\in[-2,2]^2.
\]

The same \(e,d\) must be shared across all observations of a candidate. The four limiting classes have residue memberships \(\{1,5\},\{2,4\},\{3\},\{0\}\). We investigate whether two exact readings can resolve the two non-singleton residue classes at arbitrarily large cutoff.

## Theorem A — Infinite families of exact two-read collisions

For **every integer \(q\ge73\) with \(q\equiv1\pmod6\)**, put \(p=q+4\equiv5\pmod6\). There are **rational** \(E(q),D(q)\in(-2,2)\) such that

\[
\boxed{\mathcal O_q^{(2)}(0,0)=\mathcal O_{q+4}^{(2)}(E(q),D(q)).}
\]

For **every integer \(q\ge14\) with \(q\equiv2\pmod6\)**, put \(p=q+2\equiv4\pmod6\). Again there are **rational** \(E(q),D(q)\in(-2,2)\) such that

\[
\boxed{\mathcal O_q^{(2)}(0,0)=\mathcal O_{q+2}^{(2)}(E(q),D(q)).}
\]

The two candidate errors are constant within each two-read vector. The exact limits of the constructed alternative parameters are

| Residues \((q,p)\) | \(p-q\) | Lower cutoff | \(\lim_{q\to\infty}E(q)\) | \(\lim_{q\to\infty}D(q)\) |
|---|---:|---:|---:|---:|
| (1,5) | 4 | 73 | \(719/486\) | \(-10/81\) |
| (2,4) | 2 | 14 | \(2977/3888\) | \(-17/81\) |

**Consequence.** There is no global threshold after which **two** exact scalar observations determine all six residue classes. The globally sufficient number of observations for identifying all six residues is therefore **at least three**. This lower bound complements the earlier eleven-read upper bound; three-read sufficiency remains an open question.

## Theorem B — The constructed two-read quotient loses a future observation

Fix either family and its exact \(E(q),D(q)\). Define the third-read residual

\[
R_3(q)=Y_{p+12}(E(q),D(q))-Y_{q+12}(0,0).
\]

Then, for **every** \(q\) covered by Theorem A,

\[
\boxed{R_3(q)<0.}
\]

Thus the two-read observer has nontrivial fibers: a pair of different states may have the same two observations while a later permitted observation distinguishes them. In BRC terminology this is a **future-observer nonfactorization witness**. Any two-read-only quotient intended to preserve the third six-step readout is lossy on these families. The result is an exact statement about this auxiliary labeled-source observer; a native X6 Cell/Link/Port carrier requires its own typed construction.

## Complete constructive proof

**Exact quasipolynomial inputs.** The distinct labeled weights give the generating functions

\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

After multiplication by \((1-z^6)^6\) or \((1-z^6)^7\), the numerators are polynomials of degrees \(23\) and \(29\). Thus on each progression \(q=6+r+6j\), \(C_q\) and \(T_q\) are exact degree-5 and degree-6 rational polynomials, respectively. The binomial coefficient extensions are valid even for the first \(j=0\) because the maximum numerator shift is below the denominator exponent. Interpolating six or seven exact source counts therefore determines each entire infinite progression. The executable certificate checks surplus source counts for every residue.

**Exact collision formulas.** Given \(p=q+h\), with \(h=4\) or \(2\), set for \(j=0,1\):

\[
y_j=Y_{q+6j}(0,0),\quad
x_j=\frac{y_j+S(p+6j)/108}{(p+6j)^3},\quad
b_j=x_jC_{p+6j}-T_{p+6j}.
\]

The two desired equalities are exactly \(E-x_jD=b_j\). Consequently the following explicitly computed rational functions work:

\[
\boxed{D(q)=\frac{b_0-b_1}{x_1-x_0},\qquad E(q)=b_0+x_0D(q).}
\]

The Python/SymPy companion reconstructs and reduces these rational functions, asserts the two identities by exact rational cancellation, and outputs the full formulas in the machine-readable results file.

**Proof that both errors always lie strictly inside the permitted square.** For either parameter \(V(q)=N(q)/H(q)\), shift \(q=q_0+k\), with \(q_0=73\) or \(14\) and \(k\ge0\). The three polynomials \(H(q_0+k)\), \(2H(q_0+k)-N(q_0+k)\), and \(2H(q_0+k)+N(q_0+k)\) all have degree 12 and **all 13 coefficients strictly positive**. Hence \(H>0\) and \(-2<V<2\) everywhere in the stated interval. The minimum exact coefficient in each certified polynomial is:

| Family | \(E:H\) | \(E:2H-N\) | \(E:2H+N\) | \(D:H\) | \(D:2H-N\) | \(D:2H+N\) |
|---|---:|---:|---:|---:|---:|---:|
| (1,5), \(q_0=73\) | 52488 | 27324 | 182628 | 4374 | 9288 | 8208 |
| (2,4), \(q_0=14\) | 209952 | 259146 | 580662 | 8748 | 19332 | 15660 |

All **156 coefficients** are independently checked using exact integer arithmetic by the sibling script and can be regenerated into its machine-readable JSON.

**Proof of strict third-read separation.** Substitute the above exact \(E(q),D(q)\) into \(R_3(q)\) and reduce the fraction. The resulting rational numerator and denominator have degrees 15 and 20. For each shifted \(q=q_0+k\), the **negative** of its numerator and its denominator have strictly positive coefficients, proving \(R_3(q)<0\). Their minimum coefficients are \(969292800,162\) for the (1,5) family and \(376482240,162\) for the (2,4) family, respectively. All **74 integer coefficients** are checked and exported by the script. This is a polynomial proof over the full infinite range, not a finite grid search.

## Exact witness values

For \(q=73,\ p=77\), the original state is \((e,d)=(0,0)\) and the alternative state is

\[
(E,D)=\left(\frac{161410530278749232579}{80920497832103909961},
-\frac{2809928951420394832}{26973499277367969987}\right).
\]

Both return first reading \(1429915/139914\) and second reading \(70726835/7875846\). Their alternative-minus-original third reading is exactly

\[
-\frac{91819440949694837419012459}{86654385746672240556595340808}<0.
\]

For \(q=14,\ p=16\), take

\[
(E,D)=\left(\frac{164564889239}{89946921178},
-\frac{9715958336}{224867302945}\right).
\]

The two matching readouts are \(2088313/35748\) and \(809315/17388\); the third-read difference is

\[
-\frac{4317740311435911772}{25414697480166605541}<0.
\]

## Reproduction, evidence status, next question

Run **R749SSZ_TWO_READ_PHASE_COLLISION_CERT.py** with Python 3 and SymPy. The locally executed author certificate returned PASS: 2 exact symbolic collision families, 156 strictly positive degree-12 parameter-guard coefficients, 74 strictly positive third-read sign coefficients, plus rational witness checks. The script generates **R749SSZ_TWO_READ_PHASE_COLLISION_RESULTS.json** with the complete symbolic rational functions and coefficient vectors.

**Verification scope:** exact symbolic and rational calculations under the frozen auxiliary model; independent mathematics review is outstanding. This note does not claim an accepted native X6/BRC dynamical theorem, a shared-task CLAIM, or a global three-read upper bound.

**Next discriminating research:** determine whether three or four exact readings distinguish six residues at all sufficiently large cutoffs; formulate a provenance-preserving carrier for the third-read residual; sharpen cutoff-dependent positive-noise separations. Preserve the exact \(q,p\) and per-candidate shared-error semantics when testing these.
