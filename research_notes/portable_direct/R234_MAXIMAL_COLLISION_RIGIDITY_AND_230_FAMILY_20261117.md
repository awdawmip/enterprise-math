# R234 — Rigidity of maximal source-spectral collisions and a non-isolated 230-mode family

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Native BRC EffectHistogram: **NOT_EXECUTED**.

## Source pins and precise mathematical scope

This result continues the R232 Sperner bound and R233 two-eigenvalue 230-order witness.

- R232 immutable source: awdawmip/enterprise-math@b7801c2e08e1ae3f857b6d5f14e26184caa1bf54:research_notes/portable_direct/R232_SPERNER_MAXIMAL_SPECTRAL_COLLISION_231_20261117.md
- R233 immutable source: awdawmip/enterprise-math@da4569ba1c607ac3eaf4502bb15bf36c0c2e39cf:research_notes/portable_direct/R233_TWO_EIGENVALUE_RATIONAL_COLLISIONS_230_20261117.md
- Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

P000 and ACTIVE Heartbeat World remain unchanged: the six native spatial axes, separate time, 12 signed directions, native three-dimensional slice, and joint/provenance preservation all retain their proper types. This note treats only the **derived scalar source-support principal-ideal-cardinality observer** of a finite stochastic source model. It does not reduce the native BRC sign, port, source, branch, provenance, multiplicity, rational-weight or cross-moment carrier.

For seven sources 0,...,6 (0 neutral), consider the stationary, strictly positive sticky-reset Markov chain

\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad
0<\alpha_i<1,\quad\pi_i>0,\quad\sum_{i=0}^{6}\pi_i=1,
\]

where all seven holding values are pairwise distinct. Put \(b_i=(1-\alpha_i)\pi_i\). For each proper nonneutral mask \(U\subsetneq[6]\), put \(D_U=\{0\}\cup U\) and

\[
C_{D_U}(x)=\prod_{i\in D_U}(x-\alpha_i)
-\sum_{i\in D_U}b_i\prod_{j\in D_U\setminus\{i\}}(x-\alpha_j).
\]

By R229–R233, the stationary scalar expected-ideal-size sequence has minimal recurrence polynomial equal to the lcm of \(x-1\) and these 63 block polynomials. The generic degree sum is \(1+\sum_{U\subsetneq[6]}|D_U|=250\).

## Theorem 1. Equality classification for 20 proper blocks

Fix a **non-pole** real \(\lambda\notin\{\alpha_0,\ldots,\alpha_6\}\) and put \(d_i=b_i/(\lambda-\alpha_i)\). Suppose the eigenvalue \(\lambda\) occurs in 20 different proper-mask polynomials. Then a single \(c>0\) satisfies

\[
|d_1|=\cdots=|d_6|=c.
\]

Let \(A=\{i\in[6]:d_i>0\}\) and \(B=[6]\setminus A\). Necessarily

\[
\boxed{d_0=1-(3-|B|)c,\qquad |A|\ne3.}
\]

Conversely these equal-magnitude, neutral-value, non-pole and \(|A|\ne3\) conditions imply **exactly 20** proper masks share \(\lambda\), characterized by

\[
Y=(U\cap A)\cup(B\setminus U),\qquad |Y|=3.
\]

**Proof.** The secular relation \(\sum_{i\in U}d_i=1-d_0\) becomes \(\sum_{i\in Y}|d_i|=1-d_0+\sum_{i\in B}|d_i|\). Strict positive weights make the solution family an antichain of the Boolean lattice. The R232 LYM argument bounds the cardinality by \(\binom63=20\). If 20 proper masks occur, LYM equality forces every \(Y\) to have size 3, since each set outside the middle layer contributes strictly more than \(1/20\) to LYM. Thus all 20 three-subsets occur. Comparing any two three-subsets differing by exchanging \(i\) and \(j\) proves \(|d_i|=|d_j|\). Their common value is \(c\), and \(3c=1-d_0+|B|c\). The excluded full mask \(U=[6]\) maps to \(Y=A\), so \(|A|\ne3\). The converse follows by reversing the steps. If \(|A|=3\), the same identities yield **19** proper solutions because the twentieth is the excluded full mask. QED.

## Theorem 2. Uniqueness of the maximally repeated non-pole mode

With pairwise distinct \(\alpha_1,\ldots,\alpha_6\), **two distinct real non-pole eigenvalues cannot each occur in 20 proper blocks**.

**Proof.** If \(\lambda\ne\mu\) both saturated the bound, Theorem 1 would give positive constants \(c,c'\) such that

\[
b_i=c|\lambda-\alpha_i|=c'|\mu-\alpha_i|\quad(i=1,\ldots,6).
\]

Then all six distinct \(x=\alpha_i\) would solve
\[
(\lambda-x)^2=(c'/c)^2(\mu-x)^2.
\]
For \(\lambda\ne\mu\) this is a nonzero polynomial of degree at most two; it cannot vanish at six distinct numbers. QED.

This rules out simultaneous *20-fold* modes; simultaneous smaller collisions remain possible.

## Theorem 3. An exact one-parameter 230-mode family

Set \(I=(39/100,41/100)\), \(\lambda=1/2\), \(c=5/18\), and for real \(s\in I\) define

\[
A_*={1\over3}+{2\over7}+{1\over11}+{1\over2}={559\over462},
\quad h(s)={21\over8}-A_*-{{1\over2}-s\over1-s},
\quad t(s)={h(s)+1/2\over h(s)+1}.
\]

Choose

\[
\alpha(s)=(1/5,\,1/4,\,3/10,\,9/20,\,s,\,2/3,\,t(s)),
\]

\[
\pi_0={3\over8}(1-c)={13\over48},\qquad
\pi_i(s)=c{|1/2-\alpha_i(s)|\over1-\alpha_i(s)}\quad(i=1,\ldots,6).
\]

For every \(s\in I\), all seven \(\alpha_i\) are distinct in (0,1), all \(\pi_i>0\), and \(\sum_i\pi_i=1\). The strictly positive source chain is reversible. There are **20 proper blocks** sharing \(\lambda=1/2\), and independently the two blocks \(U=\varnothing\), \(U=\{1,3\}\) (mask 5) share \(r=5/12\). Consequently the minimum recurrence order is at most 230. Moreover, the minimal order is **exactly 230 for all but finitely many parameter values in \(I\)**, and in particular it is 230 on some real open neighborhood of \(s=2/5\).

**Proof of normalization.** For \(i=1,2,3,4\), \(b_i/(1/2-\alpha_i)=+c\); for \(i=5,6\) the ratio is \(-c\). By the definition of \(t(s)\),

\[
\sum_{i=1}^6 {|1/2-\alpha_i|\over1-\alpha_i}
=A_*+{1/2-s\over1-s}+{t(s)-1/2\over1-t(s)}
={21\over8}.
\]

Thus \(\sum_i\pi_i=\frac38(1-c)+c\frac{21}{8}=1\), and \(b_0/(1/2-\alpha_0)=1-c\). Theorem 1 gives the 20 masks and a reduction by 19.

**Proof of the second collision.** The neutral-only block root is
\[
r=\alpha_0+b_0=1/5+(4/5)(13/48)=5/12.
\]
The added contributions for sources 1 and 3 are, throughout the family,
\[
{b_1\over r-\alpha_1}=5/12,\qquad
{b_3\over r-\alpha_3}=-5/12.
\]
They cancel, so \(r\) is also a root of mask 5. Neither mask is in the preceding twenty-mask family. This gives one additional degree reduction.

**Proof of the generic exact order.** Every block polynomial has coefficients rational in \(s\) and regular on \(I\). At the base parameter \(s_0=2/5\), the exact R233 certificate (also independently regenerated by the accompanying program) proves all 63 blocks squarefree and every pairwise gcd trivial except the 190 forced \(x-1/2\) pairs and the single forced \(x-5/12\) pair. After dividing out forced common factors, all residual discriminants and relevant pairwise resultants are nonzero rational functions at \(s_0\). As nonzero rational functions of one variable, they have only finitely many zeros on \(I\), and remain nonzero in some neighborhood of \(s_0\). Hence there are no extra coincidences except possibly at finitely many exceptional parameter values, and none near \(s_0\). The strictly positive stationary reversible observer has positive spectral weight on each killed-block eigenmode by R229/R232, so its polynomial lcm is the **minimal scalar recurrence polynomial**. QED.

The neighborhood is existential; no numerical certified radius is asserted.

## Reproducible exact validation

Execute the accompanying Python standard-library script R234_spectral_collision_rigidity_family_check.py. It independently regenerates \(\alpha,\pi,b\) at three rational parameters \(s=39/100,2/5,41/100\). For each parameter, it constructs 63 killed-block polynomials over exact fractions, checks squarefreeness and absence of unit roots, verifies 20 roots at \(1/2\) and precisely two at \(5/12\), and evaluates **all 1953 rational pairwise polynomial gcds**. Each sample yields exactly 190 nontrivial gcd pairs at \(1/2\) plus one at \(5/12\), and minimum order **230**. Total tests: **5859 exact gcds**, **189 squarefree checks**, three full finite instances. The JSON evidence is R234_verification.json, status PASS.

Theorems 1–2 are general symbolic author proofs. Theorem 3 is a symbolic rational-family existence/resultant argument, supported by the exact three-case program and R233 pinned base certificate. Independent review: NOT_REVIEWED. Proof-assistant formalization: NOT_EXECUTED. Native typed BRC EffectHistogram integration: NOT_EXECUTED.

## Durable frontier

Seek exceptional parameter values \(s\) where a **third** independent eigenvalue collision lowers the recurrence order below 230; calculate exact resultant factors and test any candidate with rational polynomial gcds. Investigate lower bounds in a well-defined distinct-holding subclass, as Theorem 2 only excludes simultaneous maximally repeated modes. Compare complete integer/rational bit-complexity for 230-/250-order recurrence versus 256-state direct mask/current-source propagation. Build a **read-only** native BRC EffectHistogram observer preserving signed directions, ports, source, provenance, exact positive weights, branch multiplicity and cross moments.

Research publication is separate from formal Task CLAIM, Result/Review, or Foundation admission.