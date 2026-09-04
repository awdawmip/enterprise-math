# Free Research — Odd-Simplex Constant-Mode Anchor

Status: `FREE_RESEARCH_FRONTIER / EXACT PRIME_SQUARE_LOCAL_ANCHOR / MACROSCOPIC COMPOSITE_CHORD_ANCHOR / TERMINAL_SCALAR_READOUT_CLOSED / SAME_PRIME_MASS_NO_GO / FULL_ENERGY_RECURRENCE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parents:

- `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V16_20260904.md`;
- `FREE_RESEARCH_PARITY_TWISTED_SHELL_INCIDENCE_V16_20260904.md`;
- `FREE_RESEARCH_PRIME_WINDING_PAIR_SIMPLEX_VARIANCE_20260904.md`.

Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `REUSE_APPLIED` — the odd quotient triangle already existed; the new result is its exact integration as the missing V16 constant-mode anchor and the accompanying mass audit.

## 1. Executive correction

The V16 radial top/leaf incidence operator has a uniform gap on every nonconstant parity-twisted mode, but leaves one common constant mode.  The preceding frontier described its elimination as requiring an exact endpoint-overlap submeasure or a block-relation substitute.

That is unnecessarily restrictive.  The existing degree-two quotient carrier already contains a macroscopic non-bipartite chord.

For two prime-power actions `a,b`, the paths

\[
n\xrightarrow{a}q_a(n)\xrightarrow{b}q_{ab}(n)
\]

and

\[
n\xrightarrow{ab}q_{ab}(n)
\]

meet at the same endpoint.  The two-step route has even history parity, while the direct composite chord is observed by one signless edge.  Their parity mismatch forms an odd signed triangle and kills the common parity-twisted constant exactly.

After summing over all ordered `a,b`, this chord has total mass `U_N^2`.  Therefore the terminal scalar readout has no logarithmic normalization loss:

\[
\boxed{
4U_N^2|r(N)|^2\le3\mathfrak E_N.}
\]

The V16 constant-mode anchor and one-time scalar coercive readout are consequently closed.  The sole remaining mathematical bridge is the end-to-end recurrence for the complete normalized odd-simplex energy `mathfrak E_N/U_N^2`.

---

## 2. Universal odd quotient triangle

For every positive integer action `d`, define

\[
q_d(n):=\left\lfloor\frac nd\right\rfloor,
\qquad
\delta_df(n):=f(n)+f(q_d(n)).
\]

Natural-number division obeys

\[
\boxed{q_b(q_a(n))=q_{ab}(n).}
\tag{2.1}
\]

Writing

\[
x=f(n),\qquad y=f(q_a(n)),\qquad z=f(q_{ab}(n)),
\]

one has

\[
\delta_af(n)=x+y,
\]

\[
\delta_{ab}f(n)=x+z,
\]

and

\[
\delta_bf(q_a(n))=y+z.
\]

Hence

\[
\boxed{
2f(n)=
\delta_af(n)+
\delta_{ab}f(n)-
\delta_bf(q_a(n)).}
\tag{2.2}
\]

Cauchy--Schwarz gives the sharp fixed-root inequality

\[
\boxed{
4|f(n)|^2
\le3\left(
|\delta_af(n)|^2+
|\delta_{ab}f(n)|^2+
|\delta_bf(q_a(n))|^2
\right).}
\tag{2.3}
\]

Sharpness follows by taking `y=z=-x/3`.

---

## 3. Parity-twisted geometry

Put

\[
G_0=x,
\qquad G_1=-y,
\qquad G_2=z.
\]

The two adjacent Hamming edges become ordinary differences:

\[
|x+y|^2=|G_0-G_1|^2,
\qquad
|y+z|^2=|G_1-G_2|^2.
\]

The direct composite chord is

\[
|x+z|^2=|G_0+G_2|^2.
\]

Thus the parity-twisted 2-simplex is not bipartite: the same-parity shells are joined by a positive signless chord.  A common twisted constant `G_0=G_1=G_2=c` has zero adjacent-edge energy but chord energy

\[
|G_0+G_2|^2=4c^2.
\]

Therefore the direct composite edge is precisely the missing constant-mode anchor.

This is the correct geometric completion of the radial shell analysis:

\[
\boxed{
\text{radial incidence gap on nonconstants}
+
\text{odd composite chord on constants}
=
\text{full signed-simplex coercivity}.}
\]

---

## 4. Macroscopic weighted anchor

Let `S` be any finite action family, let `u_a>=0`, and put

\[
U:=\sum_{a\in S}u_a.
\]

Define

\[
E_1(f;n)
:=\sum_{a\in S}u_a|\delta_af(n)|^2,
\]

\[
E_{\rm dir}(f;n)
:=\sum_{a,b\in S}u_au_b
|\delta_{ab}f(n)|^2,
\]

and

\[
E_{\rm tr}(f;n)
:=\sum_{a,b\in S}u_au_b
|\delta_bf(q_a(n))|^2.
\]

Multiplying (2.3) by `u_au_b` and summing gives

\[
\boxed{
4U^2|f(n)|^2
\le3\left(
UE_1(f;n)+E_{\rm dir}(f;n)+E_{\rm tr}(f;n)
\right).}
\tag{4.1}
\]

For the prime-winding action weights

\[
u_a=\frac{\Lambda(a)}a,
\qquad a\le Y_N:=\lfloor\sqrt N\rfloor,
\]

the right side is the existing positive pair-simplex energy

\[
\mathfrak E_N
=U_NE_1+E_{\rm dir}+E_{\rm tr}.
\]

Consequently

\[
\boxed{
|r(N)|^2
\le\frac34\frac{\mathfrak E_N}{U_N^2}.}
\tag{4.2}
\]

This is exactly the terminal one-time scalar readout required by V16.  It uses the complete degree-two provenance measure and does not require exact equality of one- and two-history quotient endpoints after coarse projection.

---

## 5. Fixed-prime square anchor

There is also a local atomic specialization.  For any prime `p` and `n>=p^2`, take

\[
a=b=p,
\qquad ab=p^2.
\]

Then

\[
\boxed{
2f(n)=
\delta_pf(n)+
\delta_{p^2}f(n)-
\delta_pf(q_p(n)).}
\tag{5.1}
\]

Let

\[
\mathcal Q(f;n)
:=\sum_{q\le n}\frac{\Lambda(q)}q
|\delta_qf(n)|^2.
\]

Weighted Cauchy--Schwarz, with weights

\[
\omega(p)=\frac{\log p}{p},
\qquad
\omega(p^2)=\frac{\log p}{p^2},
\]

gives

\[
\boxed{
|f(n)|^2
\le
\frac{p(p+2)}{4\log p}
\left(
\mathcal Q(f;n)+
\mathcal Q(f;q_p(n))
\right).}
\tag{5.2}
\]

The continuous function

\[
x\longmapsto\frac{x(x+2)}{\log x}
\]

is increasing for `x>=2`; therefore the optimal prime is `p=2`:

\[
\boxed{
|f(n)|^2
\le\frac2{\log2}\left(
\mathcal Q(f;n)+
\mathcal Q(f;\lfloor n/2\rfloor)
\right).}
\tag{5.3}
\]

This proves directly that no nonzero field can satisfy all `2`, `4`, and transported `2` signless edges exactly.

---

## 6. Why the fixed-prime anchor is not the quantitative endpoint

The fixed-prime triangle is pointwise but its action mass is small after normalization.  More generally, every factorization for which both primitive actions and their direct product remain prime powers must use one common prime.

The total infinite same-prime ordered-pair mass is

\[
\begin{aligned}
J_\infty
&:=\sum_p\sum_{u,v\ge1}
\frac{\log p}{p^u}
\frac{\log p}{p^v}\\
&=\boxed{
\sum_p\frac{(\log p)^2}{(p-1)^2}<\infty.}
\end{aligned}
\tag{6.1}
\]

The full ordered prime-power pair mass is

\[
U_N^2\asymp(\log N)^2.
\]

Hence same-prime exact action chords occupy only

\[
O((\log N)^{-2})
\]

of the normalized pair cloud.  Any proof using only direct **prime-power** chords pays a vanishing-mass penalty.

The macroscopic anchor (4.1) avoids this obstruction because `ab` is retained as a degree-two provenance label even when it is not itself a primitive prime-power action.  Its endpoint and signless direct edge are legitimate finite history observables, and all ordered pairs contribute.

Therefore:

\[
\boxed{
\text{primitive same-prime chord}
\text{ kills the exact kernel locally but is quantitatively sparse};}
\]

\[
\boxed{
\text{composite provenance chord}
\text{ kills the constant mode at full }U_N^2\text{ mass}.}
\]

---

## 7. Correction to the V16 boundary

The following items are now closed, by reuse and exact integration of the existing pair-simplex theorem:

1. elimination of the common parity-twisted constant mode;
2. a positive macroscopic anchor that does not rely on exact endpoint overlap;
3. the terminal one-time scalar coercive readout;
4. the distinction between sparse primitive chords and full composite provenance chords.

The remaining theorem is not an atomic anchor.  It is the following end-to-end energy propagation statement.

### Complete odd-simplex recurrence target

Put

\[
\overline{\mathfrak E}(N)
:=\frac{\mathfrak E_N}{U_N^2}.
\]

Prove a retained two-channel inequality of the form

\[
\boxed{
\overline{\mathfrak E}(N)
\le
\sum_{q\le N}p_N(q)
\mathcal K_{N,q}
\overline{\mathfrak E}(\lfloor N/q\rfloor)
+F(N),}
\tag{7.1}
\]

where:

1. `K_(N,q)` keeps the parity/mean and standard channels typed separately;
2. its standard block contains the exact `1/9` `S_3` factor;
3. its scalar profile converges to
   \[
   k(s)=1-\frac{32}{9}s(1-s);
   \]
4. `F(N)` is summable at the claimed logarithmic exponent;
5. no per-level scalar reconstruction is inserted.

Once (7.1) is proved, the V16 discrete Mellin barrier applies, and (4.2) gives the scalar remainder in one final step.

---

## 8. Current classification

Exact finite theorem/reuse closure:

- odd quotient identity and fixed-root coercivity;
- parity-twisted interpretation of the direct chord;
- macroscopic weighted pair-simplex anchor;
- terminal scalar readout (4.2);
- fixed-prime square anchor;
- same-prime normalized-mass no-go.

Open:

- the complete normalized odd-simplex recurrence (7.1);
- compatibility of its direct composite-chord block with the persistent row mixer;
- a summable forcing audit for all three pair-simplex channels;
- a promoted logarithmic prime remainder;
- any RH-scale conclusion, Working Truth, or Foundation promotion.

The V16 obstruction has therefore moved one step further:

\[
\boxed{
\text{constant-mode anchor: closed};
\qquad
\text{full energy recurrence: uniquely open}.}
\]
