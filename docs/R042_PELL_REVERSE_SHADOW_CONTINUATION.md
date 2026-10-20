# R042 continuation — Pell reverse shadow, local gate residual, and superlacunary recurrence constraint

Status: `L2 CONTINUATION CHECKPOINT / PROVED + PRIOR_ART-ASSISTED + EXECUTABLE_CHECKED / NOT CANONICAL`

Current Researcher-ID: `EM-R042-963283`

Historical phase-I provenance only: `EM-R042-290D7A`

Task: `RS-R042-POLYGONAL-NONSQUARE-BRANCH-LIMIT-PELL-RECURRENCE`

Taskbook source lock: `5e95b8b589ffa75975de165b46f70139b2e0720b`

Consumed frozen phase-I owner head: `fb03a917f8ea343428d5805348f045910fc28752` (Draft PR #528)

Consumed intervening same-session continuation head during bounded reconciliation: `b3ca1369c147e50d1a841d3f86c081f2cb152f68` (`exact correction cocycle + growing-modulus reverse address + elementary Pell-rank acceleration`)

Primary return:

`HIT_ANCESTRY_ONTOLOGY_REPLACED / SMALLER_EXACT_RECURRENCE_OBJECT_FOUND / NOT_CANONICAL`

Refined disposition:

`CORRECTION_RENORMALIZATION_STRENGTHENED_BY_REVERSE_SHADOW / LOCAL_GATE_CORRELATION_RESIDUAL_ISOLATED / SUPERLACUNARY_INFINITE_RAY_NECESSITY_PROVED / INFINITE_RECURRENCE_OPEN / NOT_CANONICAL`

## 0. Frozen phase-I boundary

This continuation does **not** reopen the phase-I results. In particular it consumes as frozen:

1. for nonsquare integer `r>=5`, `s!=4`, finite nonempty positive initial support,
   \[
   \dim_H K=\underline{\dim}_B K=\overline{\dim}_B K
   =\frac{\log2}{\log\sqrt r};
   \]
2. the branch-limit subset with infinitely many exact-hit times, if nonempty, has Hausdorff dimension zero;
3. that exceptional subset has zero positive-survival conditioned Bernoulli mass;
4. finite nonconsecutive hit revisit exists, so `at most one hit per branch` is false;
5. branchwise infinite recurrence is exactly equivalent to an infinite directed ray in the unique-predecessor hit-ancestry forest.

The sole mathematical frontier here is whether such an infinite ray can actually exist.

## 1. New disposition

A universal finite-height theorem is **not** proved here, and no infinite ray is constructed.

During publication, the same owner branch had already advanced to `b3ca1369...`, which proved the complementary exact correction cocycle `xi_(t+1)=sqrt(r) xi_t+q_t`, a growing-modulus reverse address, a finite residue-preserving Pell-seed quotient, and an elementary rank-acceleration law. This checkpoint consumes that head rather than overwriting it. The reverse-shadow argument below refines the **remaining accelerated-ray frontier** and strengthens the elementary rank acceleration to a superlacunarity necessity using a linear-forms lower bound.

The useful decomposition now has three additional layers:

1. a **finite reduced Pell class** plus a Pell-unit exponent for every ambient exact hit;
2. a closed-form **ideal reverse shadow** that every dynamically reachable ancestry must track within a uniform constant window;
3. an ordered sequence of exact **local reverse-gate residuals** whose survival is the remaining branch-accessibility correlation.

This decomposition yields a theorem that any infinite reachable hit ray, if it exists, must be **superlacunary** in both Pell-unit exponent gaps and branch-time gaps. Consequently no bounded-gap, periodic, fixed-step Pell-unit renormalization can generate the requested recurrence.

The remaining possibility is a much thinner object: a superlacunary Pell shrinking-target sequence that simultaneously survives every exact local reverse gate.

## 2. Centered exact carrier

Write

\[
a=s-2,\qquad c=s-4,\qquad m=2a,\qquad
\kappa=\frac{c}{m},\qquad \alpha=\sqrt r,
\]

and

\[
z_k=mk-c=m(k-\kappa),\qquad B=(r-1)c^2.
\]

For the centered index

\[
x=k-\kappa=\frac{z_k}{m},
\]

the exact real forward target is

\[
F(x)=\sqrt{r x^2-(r-1)\kappa^2}.
\]

Every legal child center `y=j-kappa` brackets `F(x)` on the unit-spaced centered lattice, hence

\[
|y-F(x)|<1,
\]

with equality zero at an exact hit.

The continuous reverse map is

\[
\boxed{
G(y)=\sqrt{\kappa^2+\frac{y^2-\kappa^2}{r}}.}
\]

For positive states,

\[
0<G'(y)<\frac1\alpha.
\]

Therefore if `R(j)` is the exact unique endpoint predecessor of `j`,

\[
\boxed{
|R(j)-\kappa-G(j-\kappa)|<\alpha^{-1}.}
\]

Claim status: `PROVED`.

## 3. Closed-form ideal reverse shadow

The reverse map has an exact iterate identity:

\[
\boxed{
G^n(y)^2=\kappa^2+r^{-n}(y^2-\kappa^2).}
\]

Define the ideal depth-`n` reverse index of endpoint `J` by

\[
I_n(J)=\kappa+
\sqrt{\kappa^2+r^{-n}\bigl((J-\kappa)^2-\kappa^2\bigr)}.
\]

Repeated use of the `1/alpha` Lipschitz bound gives:

> **Reverse-shadow lemma.** If the exact predecessor chain `R^n(J)=h` exists, then
> \[
> \boxed{
> |h-I_n(J)|<C_n,
> \qquad
> C_n=\sum_{t=1}^n\alpha^{-t}
> =\frac{1-\alpha^{-n}}{\alpha-1}
> <\frac1{\alpha-1}.}
> \]

Claim status: `PROVED`.

Two useful consequences are immediate.

- For nonsquare `r>=10`, `1/(sqrt(r)-1)<1/2`, so a depth-`n` ancestor, if it exists, is the unique nearest integer to `I_n(J)`.
- For `r in {5,6,7,8}`, the total shadow radius is `<1`, so at most two integer ancestor candidates survive the global shadow at any depth.

These are candidate-count reductions only. They do **not** certify intermediate gate survival.

## 4. Centered energy and exact scale residual

Define

\[
A(k):=(k-\kappa)^2-\kappa^2
=\frac{z_k^2-c^2}{m^2}
=\frac{2P_s(k)}a.
\]

The ideal reverse shadow scales this quantity exactly by `r^-n`.

If an exact branch segment of length `ell` joins a hit `h` to a later hit `H`, the reverse-shadow lemma gives the exact necessary estimate

\[
\left|
\frac{A(H)}{r^\ell A(h)}-1
\right|
\le
\frac{2|h-\kappa|C_\ell+C_\ell^2}{A(h)}.
\]

Along a fixed Pell class the right side is `O(epsilon^-n)` in the source Pell-unit exponent `n`; this exponential shrinking is the key arithmetic input below.

Claim status: `PROVED`.

## 5. Finite reduced Pell classes

Exact hits are positive solutions of

\[
Y^2-rZ^2=-B,
\qquad Y,Z\equiv-c\pmod m,
\]

where `Z=z_h` and `Y` is the discriminant coordinate of the unique exact child.

Let

\[
\varepsilon=u+v\sqrt r>1,
\qquad u^2-rv^2=1
\]

be the fundamental positive Pell unit. Its inverse action is

\[
(Y,Z)\longmapsto (uY-rvZ,\ uZ-vY).
\]

For a positive norm-`-B` solution, the second coordinate after inverse-unit action is always positive because

\[
\frac YZ<\sqrt r<\frac uv.
\]

The first coordinate remains positive exactly when

\[
rZ^2>u^2B.
\]

Hence repeated inverse-unit reduction stops at a unique positive representative satisfying

\[
\boxed{rZ_0^2\le u^2B.}
\]

There are only finitely many such positive representatives. Every positive solution is therefore uniquely encoded by

\[
(i,n),
\]

where `i` is one of finitely many reduced norm classes and `n>=0` is a Pell-unit exponent. Exact-hit affine-lattice compatibility selects a periodic subset of `n` in each class, because the unit matrix has finite order modulo `m`.

Claim status: `PROVED` for the exact reduction statement; generic Pell-unit orbit theory is `PRIOR_ART`.

### A tempting monotonicity is false

The candidate theorem “a reachable hit-to-hit edge strictly decreases the reduced Pell class/rank” is killed by

\[
(s,r)=(8,40),\qquad 1\to4\to24.
\]

Both `1` and `24` are exact-hit parents and belong to the **same** reduced Pell class. The fundamental unit is `(u,v)=(19,3)`; the hit pair for `k=1` is `(Y,Z)=(44,8)` and the hit pair for `k=24` is its one-unit translate.

Claim status: `EXECUTABLE_CHECKED` exact counterexample.

Therefore no finite-height conclusion is obtained by reduced-class descent.

## 6. Pell-unit shrinking target

For reduced class `i`, choose a positive representative `(Y_i,Z_i)` and define

\[
\tau_i=Y_i+\alpha Z_i.
\]

Since the norm is `-B`, its conjugate is `-B/tau_i`. At unit exponent `n`, the exact Pell denominator is

\[
Z_i(n)=
\frac{\tau_i\varepsilon^n+B/(\tau_i\varepsilon^n)}{2\alpha}.
\]

Consequently

\[
\boxed{
A_i(n)=
\frac{
\tau_i^2\varepsilon^{2n}
+B^2\tau_i^{-2}\varepsilon^{-2n}
-2(r+1)c^2
}{4rm^2}.}
\]

Now suppose there is a dynamically reachable hit-to-hit edge from source class/exponent `(i,n)` to target `(j,N)` with branch gap `ell>=1`. Put

\[
d=N-n,
\qquad
\Gamma_{ij}=\left(\frac{\tau_j}{\tau_i}\right)^2.
\]

Combining the exact `A_i(n)` formula with the reverse-shadow estimate yields, uniformly over the finite class pairs,

\[
\boxed{
\left|
\Gamma_{ij}\varepsilon^{2d}r^{-\ell}-1
\right|
\le C_{s,r}\varepsilon^{-n}}
\]

for all sufficiently large source exponents `n` participating in such an edge.

Claim status: `PROVED`.

This is the **Pell-unit shrinking-target condition** forced by exact branch accessibility. It is strictly stronger than ambient Pell membership.

## 7. Superlacunarity theorem for any hypothetical infinite ray

The algebraic number

\[
\Gamma_{ij}\varepsilon^{2d}r^{-\ell}
\]

cannot equal `1` when `ell>=1`. Indeed

\[
N_{\mathbf Q(\sqrt r)/\mathbf Q}(\Gamma_{ij})=1,
\qquad N(\varepsilon)=1,
\qquad N(r^{-\ell})=r^{-2\ell},
\]

so equality to `1` would force `r^{-2\ell}=1`, impossible.

A standard effective lower bound for a nonzero linear form in logarithms of fixed algebraic numbers (Matveev/Baker theory) therefore gives constants `K,C_0>0`, depending only on the fixed cell and finite class pair, such that

\[
\left|
\Gamma_{ij}\varepsilon^{2d}r^{-\ell}-1
\right|
\ge
K(1+|d|+\ell)^{-C_0}.
\]

Combining this polynomial lower bound with the exponentially shrinking upper bound from Section 6 gives

\[
\boxed{
\max\{|d|,\ell\}\ge \exp(cn)}
\]

for some `c=c(s,r)>0` once `n` is large. Taking logarithms of the same shrinking-target relation gives

\[
2d\log\varepsilon-\ell\log r+
\log\Gamma_{ij}=O(\varepsilon^{-n}),
\]

so `d` and `ell` are linearly comparable; in particular, for sufficiently large source exponents on a reachable edge, both are positive and both grow at least exponentially in `n` up to cell-dependent constants.

> **Superlacunarity theorem.** If an infinite dynamically reachable exact-hit ray exists for fixed nonsquare `r>=5`, `s!=4`, then after finitely many initial hits, its successive Pell-unit exponent gaps and its successive branch-time gaps grow at least exponentially in the current source Pell-unit exponent.

Claim status: `PROVED USING PRIOR_ART LINEAR-FORMS LOWER BOUND`.

This kills the following infinite-recurrence mechanisms:

- bounded Pell-unit exponent gaps;
- eventually periodic hit-to-hit Pell-unit increments;
- fixed-step Pell renormalization;
- any finite-state renormalization whose transitions carry uniformly bounded Pell exponent increments.

It does **not** kill a superlacunary ray.

## 8. Exact local gate residual: the hidden correlation

The global reverse shadow is necessary but not sufficient because actual branch accessibility is an ordered local condition.

For a proposed endpoint edge with discriminant coordinates

\[
z_{t-1}=z_{k_{t-1}},\qquad z_t=z_{k_t},
\]

define the exact integer residual

\[
\boxed{
E_t=r z_{t-1}^2-z_t^2-B.}
\]

For positive stable states `z_t>m`, `k_t` is a legal child of `k_{t-1}` exactly when

\[
\boxed{
-2mz_t+m^2<E_t<2mz_t+m^2,}
\]

with the exact endpoint oracle handling the finite low-height boundary cases.

Moreover,

\[
z_t^2-c^2=r(z_{t-1}^2-c^2)-E_t,
\]

so

\[
\boxed{
A(k_t)=rA(k_{t-1})-\frac{E_t}{m^2}.}
\]

Over a length-`ell` branch segment this telescopes to

\[
\boxed{
r^\ell A(h)-A(H)
=\frac1{m^2}
\sum_{t=1}^{\ell}r^{\ell-t}E_t.}
\]

This identity locates the missing correlation exactly:

> The Pell/shadow scale condition controls only one weighted aggregate of the ordered residual word `(E_1,...,E_ell)`. Dynamic reachability requires **every individual local gate** in that ordered word to survive.

This ordered local-gate residual word is the smaller exact recurrence object left after the global Pell-scale component is separated.

Claim status: `PROVED`.

Relation to `b3ca1369...`: its finite correction digits encode a two-step affine cocycle, while `E_t` is the one-step exact gate residual. They are complementary rather than competing states: the correction cocycle provides the finite-alphabet/growing-modulus address, and the `E_t` word exposes the per-gate correlation that a global Pell/shadow resonance still fails to control.

## 9. Strong exact witness that global shadow does not imply accessibility

The cell

\[
(s,r)=(5,14)
\]

gives a compact witness. Both

\[
h=2,\qquad H=95
\]

are exact-hit parents. The source hit pair is `(Y,Z)=(41,11)`; the target hit pair is `(2129,569)`.

At putative reverse depth `ell=3`, the ideal shadow square is exactly

\[
I_3(95)-\kappa\quad\text{squared}=
\frac{40813}{12348}.
\]

Since `kappa=1/6` and `h-kappa=11/6`, direct rational comparison gives

\[
\left(\frac{11}{6}-\frac1{60}\right)^2
<\frac{40813}{12348}<
\left(\frac{11}{6}+\frac1{60}\right)^2.
\]

Thus

\[
|I_3(95)-2|<\frac1{60},
\]

well inside the universal reverse-shadow allowance `C_3`.

Nevertheless

\[
\boxed{R(95)=\varnothing.}
\]

The two nearest inverse lattice candidates are parent indices `25` and `26`. Their local residuals are

\[
E(25,95)=-12960,
\qquad E(26,95)=12576,
\]

while the legal gate interval is

\[
-6792<E<6864.
\]

Both fail, on opposite sides.

Equivalently, using the target hit's Pell companion `Y=2129`, the two centered first-gate residue lifts have

\[
D=rz-Y\in\{-43,41\},
\]

and both fail the exact pure-integer first reverse gate.

Claim status: `EXECUTABLE_CHECKED` with exact rational/integer certificates.

This witness kills the stronger shortcut

`Pell orbit compatibility + very accurate global reverse shadow alignment => branch accessibility`.

## 10. Pure-integer first reverse gate at a target hit

For a target hit pair `(Y,Z)` and a predecessor lattice coordinate `z`, define

\[
D=rz-Y.
\]

The lattice condition is

\[
D\equiv-Y-rc\pmod{rm}.
\]

Using `Y^2-rZ^2=-B`, one obtains the exact identity

\[
\boxed{
r\bigl(W(z)^2-Z^2\bigr)
=D(2Y+D)-(r+1)B.}
\]

For `Z>m`, the candidate `z` is an exact predecessor coordinate of the target endpoint exactly when

\[
\boxed{
r(-2mZ+m^2)
< D(2Y+D)-(r+1)B
<r(2mZ+m^2).}
\]

This gives a square-root-free first-gate test on Pell data. As a Pell orbit grows, this first-gate decision is controlled by a narrow bounded lift of a residue class modulo `rm`, but this is only the first reverse gate and is not promoted to a full fixed-modulus reachability automaton.

Claim status: `PROVED`.

## 11. Exact checker and bounded diagnostics

New continuation checker:

`tools/r042_pell_reverse_shadow.py`

Focused tests:

`tests/test_r042_pell_reverse_shadow.py`

The exact local run at this checkpoint reports:

`8 tests / PASS`.

The tests certify:

- closed-form reverse-shadow scaling;
- preservation of frozen finite revisit witnesses;
- the `(8,40)` same-reduced-class counterexample;
- the exact reduced-pair stopping bound;
- the `(5,14)` strong-shadow/non-accessibility witness;
- the pure-integer first reverse gate;
- the ordered local residual gate;
- the weighted residual telescoping identity.

A separate discovery-only bounded unit-class scan was used to attack the tempting statement “every hit ancestor is a reduced Pell representative.” Across the explored finite window it found no ancestor with positive reduced-unit exponent and no three-hit ancestry, but this remains `BOUNDED_DIAGNOSTIC` and is **not** a theorem or return claim.

## 12. Prior-art boundary

No novelty is claimed for generic Pell-unit orbit theory, continued fractions, Ostrowski numeration, or lower bounds for linear forms in logarithms.

The quantitative external theorem used in Section 7 is the standard Baker/Matveev type fact that a nonzero linear form in logarithms of fixed algebraic numbers has an effective lower bound polynomial in the maximum integer coefficient. A direct prior-art root is E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217--1269, DOI `10.1070/IM2000v064n06ABEH000314`. The R042 contribution here is the derivation of the specific algebraic shrinking-target expression from exact polygonal branch accessibility and its superlacunarity consequence.

Quadratic Ostrowski/Beatty automata are relevant only as a possible next language for the **ordered gate-survival word**. Prior-art roots are P. Hieronymi and A. Terry Jr., *Ostrowski numeration systems, addition and finite automata*, arXiv:`1407.7000`, and L. Schaeffer, J. Shallit, S. Zorcic, *Beatty Sequences for a Quadratic Irrational: Decidability and Applications*, arXiv:`2402.08331`. These works do not replace exact accessibility and are not used to prove the current result.

## 13. Remaining frontier

The original infinite-ray question is not forced closed.

After this continuation, an infinite recurrent branch would have to satisfy all of the following simultaneously:

1. lie in finitely many residue-compatible generalized-Pell unit orbits;
2. hit exponentially shrinking Pell-unit/base-`r` scale targets;
3. use successively superlacunary Pell exponents and branch gaps;
4. survive the entire ordered exact local-gate residual word between successive hits.

The next exact attack should therefore target the **gate-survival cocycle** rather than the ambient Pell orbit or the already-solved dimension theory. Two plausible routes remain:

- a growing-modulus/profinite or Ostrowski description of the ordered gate word, with exact endpoint-oracle verification retained; or
- a constructive search for a genuinely nested superlacunary sequence satisfying both the shrinking-target inequality and all local gates.

A fixed-modulus residue-only automaton remains excluded by phase I and is not revived here.

## 14. Driver return

Researcher-ID: `EM-R042-963283`

Primary return:

`HIT_ANCESTRY_ONTOLOGY_REPLACED / SMALLER_EXACT_RECURRENCE_OBJECT_FOUND / NOT_CANONICAL`

Secondary theorem payload:

`SUPERLACUNARY_INFINITE_RAY_NECESSITY_PROVED / LOCAL_GATE_CORRELATION_RESIDUAL_ISOLATED / INFINITE_RECURRENCE_OPEN`

Hard block: `NONE`.

CI disposition: `CI_NOT_REQUIRED_FOR_RESEARCH`.
