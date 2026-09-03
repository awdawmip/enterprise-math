# Viète half-angle chain from normalized segment bisectors: exact refinement theorem, antipodal seed obstruction, and precision parity

Status: `FREE_RESEARCH / EXACT_G1_REFINEMENT_THEOREM + CURRENT-G0-UNDERDETERMINATION + CLASSICAL_COMPLETION / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Durable predecessor: `research_notes/EULER_ROTATION_DYADIC_VIETE_CONSEQUENCE_20260903.md` (`6cfadba0fe2cd8ba9a0ff9b5a61264b75519b500`)

## 1. Frontier recovered rather than restarted

The predecessor already establishes the target-free radical recursion and its classical completion to Viète's product. Its explicit remaining boundary is

`TARGET_FREE_ALGEBRAIC_RECURSION != NATIVE_CELL_DERIVATION`.

This note therefore does not re-prove that result as new work. It attacks the missing mechanism: when is the square-root refinement forced by a finite oriented-segment construction, and where is genuinely new information still required?

## 2. Typed orientation readout, not a native continuous circle

Work at a rebuilt algebraic orientation-readout layer. A finite oriented state is represented by a pair

\[
v=(c,s),\qquad c^2+s^2=1.
\]

Only the finitely generated states used below are required. This notation does **not** assert that every point of a Euclidean unit circle is a native Cell state, nor does it identify carrier angle with Enterprise native angle.

Use the algebraic rotation composition

\[
(a,b)\odot(c,d)=(ac-bd,ad+bc).
\]

The identity orientation is

\[
e=(1,0).
\]

The square-sum normalization is compatible with the current sector-local Enterprise Pythagorean readout, but the existence of a canonical Cell-to-orientation quotient is a separate bridge obligation.

Freeze boundary:

`FINITE_G1_ORIENTATION_READOUT != NATIVE_G0_CELL_STATE`.

## 3. Exact normalized-bisector square-root theorem

For any unit orientation state

\[
v=(c,s),\qquad c^2+s^2=1,\qquad c>-1,
\]

form the equal-endpoint resultant with the identity orientation and normalize it by the Pythagorean norm:

\[
B(v)
=\frac{e+v}{\|e+v\|}
=\frac{(1+c,s)}{\sqrt{(1+c)^2+s^2}}
=\frac{(1+c,s)}{\sqrt{2(1+c)}}.
\]

Write

\[
B(v)=(c',s').
\]

Then exactly

\[
\boxed{c'=\sqrt{\frac{1+c}{2}}},
\]

with the principal positive longitudinal branch, and

\[
\boxed{s'=\operatorname{sgn}(s)\sqrt{\frac{1-c}{2}}}.
\]

More importantly, this normalized resultant is an exact rotation square root:

\[
\boxed{B(v)\odot B(v)=v}.
\]

Proof: the normalization denominator satisfies

\[
D^2=(1+c)^2+s^2=2(1+c).
\]

Hence

\[
(c')^2-(s')^2
=\frac{(1+c)^2-s^2}{D^2}
=\frac{2c(1+c)}{2(1+c)}=c,
\]

and

\[
2c's'=\frac{2(1+c)s}{D^2}=s.
\]

Therefore the Viète plus-radical update is not an arbitrary trigonometric import once this finite normalized-bisector operation is declared: it is forced by `equal resultant + square-sum normalization`.

No numerical value of \(\pi\), no sine/cosine function, no circumference, and no continuum of circle points occurs in this theorem.

## 4. The antipodal seed obstruction is the unique failure of the same rule

At the half-turn/reversal state

\[
v=-e=(-1,0),
\]

one has

\[
e+v=(0,0).
\]

Therefore `B(v)` is undefined. The two algebraic square roots of the half-turn are

\[
(0,+1),\qquad(0,-1),
\]

and the equal-resultant normalization cannot select between them.

Thus there is one genuine seed obstruction:

\[
\boxed{\text{half-turn} \longrightarrow \text{quarter-turn}}
\]

requires an orientation/branch choice not supplied by the same bisector rule.

After a quarter-turn seed is supplied, every later dyadic refinement has longitudinal coordinate \(c>-1\) and the normalized-bisector theorem applies recursively without another such singularity.

Freeze:

`ANTIPODAL_HALF_TURN = UNIQUE_NORMALIZED_BISECTOR_SINGULARITY_ON_THE_DYADIC_CHAIN`.

## 5. Why the coarse six-state orientation shell must refine to at least twelve states

The current Euler rotation-character candidate uses the coarse oriented quotient

\[
C_3\times C_2\cong C_6.
\]

This is a typed orientation quotient, not a claim that six carrier directions are six primitive native axes.

A cyclic state space has an exact quarter-turn element iff its order is divisible by \(4\). Since \(4\nmid6\), the coarse \(C_6\) shell contains a half-turn but no quarter-turn.

Any finite cyclic refinement that contains the coarse \(C_6\) shell and also contains an order-four state must have order divisible by both \(6\) and \(4\). Hence its order is divisible by

\[
\operatorname{lcm}(6,4)=12.
\]

The minimum cyclic refinement is therefore

\[
\boxed{C_6\hookrightarrow C_{12}}.
\]

Equivalently in a character realization,

\[
\mu_6\subset\mu_{12}.
\]

This gives a precise role to the six-state picture: it is a **pre-Viète seed shell**. It cannot itself execute the first half-angle step. The first doubled resolution supplies the missing quarter-turn; only then does the recurrent normalized-bisector mechanism generate the Viète tower.

## 6. Exact finite radical tower from the quarter-turn seed

Choose one oriented quarter-turn seed

\[
(c_0,s_0)=(0,\varepsilon),\qquad \varepsilon\in\{+1,-1\}.
\]

Define recursively

\[
(c_{n+1},s_{n+1})=B(c_n,s_n).
\]

Then

\[
\boxed{c_{n+1}=\sqrt{\frac{1+c_n}{2}}},
\qquad
\boxed{s_{n+1}=\operatorname{sgn}(s_n)\sqrt{\frac{1-c_n}{2}}}.
\]

Set

\[
r_n=2c_n.
\]

Then \(r_0=0\) and

\[
\boxed{r_{n+1}=\sqrt{2+r_n}}.
\]

Thus

\[
r_1=\sqrt2,
\quad
r_2=\sqrt{2+\sqrt2},
\quad
r_3=\sqrt{2+\sqrt{2+\sqrt2}},\ldots
\]

The familiar plus nested radicals are exactly the longitudinal coordinates of repeated normalized segment-bisector refinement.

## 7. The minus radical is the transverse/chord residual

Let the signed transverse quantity be

\[
h_n=2s_n.
\]

For \(n\ge1\),

\[
h_n^2=4s_n^2=2-r_{n-1}.
\]

Hence the complementary minus radical is not an unrelated formula:

\[
\boxed{|h_n|=\sqrt{2-r_{n-1}}}.
\]

Also

\[
\boxed{r_n^2+h_n^2=4}.
\]

Squaring the half-state back to the previous state gives

\[
s_{n-1}=2c_ns_n,
\]

or equivalently

\[
\boxed{h_{n-1}=r_nh_n}.
\]

This is the exact finite bridge between the longitudinal plus-radical chain and the transverse minus-radical residual.

## 8. Exact telescoping and finite precision-pi readout

Because \(|h_0|=2\), repeated use of

\[
|h_{n-1}|=r_n|h_n|
\]

gives

\[
\prod_{k=1}^{n}r_k=\frac{2}{|h_n|}=\frac1{|s_n|}.
\]

Therefore the Viète partial product

\[
P_n:=\prod_{k=1}^{n}\frac{r_k}{2}
=\prod_{k=1}^{n}c_k
\]

satisfies the exact finite identity

\[
\boxed{P_n=\frac{1}{2^n|s_n|}}.
\]

Define the finite rotation-precision readout

\[
\boxed{\Pi_n:=\frac{2}{P_n}=2^{n+1}|s_n|}.
\]

This is an entirely finite algebraic quantity. It does not need the target numerical value of \(\pi\) as input.

## 9. Monotonicity is already finite algebra

From

\[
|s_n|=2c_{n+1}|s_{n+1}|,
\]

one gets

\[
\Pi_n=c_{n+1}\Pi_{n+1}.
\]

Along the post-quarter-turn chain,

\[
0<c_{n+1}<1.
\]

Hence

\[
\boxed{\Pi_{n+1}>\Pi_n}.
\]

So monotonic improvement of the finite precision readout is proved before any classical trigonometric completion.

## 10. Classical completion and explicit precision law

Only now add the classical rotation-character interpretation

\[
(c_n,s_n)
=\left(\cos\frac{\pi}{2^{n+1}},\;\varepsilon\sin\frac{\pi}{2^{n+1}}\right).
\]

Then

\[
\boxed{\Pi_n=2^{n+1}\sin\frac{\pi}{2^{n+1}}}.
\]

Consequently

\[
\Pi_n\uparrow\pi,
\]

and

\[
\prod_{k=1}^{\infty}c_k=\frac2\pi.
\]

Let

\[
M=2^{n+1}.
\]

Since \(x=\pi/M\in(0,\pi/2]\), the alternating Taylor bounds for sine give

\[
\boxed{
\frac{\pi^3}{6M^2}-\frac{\pi^5}{120M^4}
\le
\pi-\Pi_n
\le
\frac{\pi^3}{6M^2}
}.
\]

Therefore

\[
\boxed{
\pi-\Pi_n
\sim
\frac{\pi^3}{6\,4^{n+1}}
}.
\]

One dyadic orientation refinement therefore asymptotically divides the scalar \(\pi\)-error by \(4\): one added bit of orientation resolution yields about two bits of scalar precision.

## 11. Orientation reversal: the answer depends on which residual is typed

Orientation reversal acts by

\[
R(c,s)=(c,-s).
\]

The normalized-bisector rule is equivariant:

\[
B(c,-s)=R(B(c,s)).
\]

Therefore:

- every longitudinal state \(c_n\) and every plus-radical factor \(r_n\) is **even** under orientation reversal;
- the signed transverse state \(s_n\) and \(h_n\) is **odd**;
- the scalar precision readout \(\Pi_n=2^{n+1}|s_n|\) is **even**;
- the signed readout \(\widehat\Pi_n=2^{n+1}s_n\) is **odd**.

Under analytic completion, write the signed fine phase as

\[
x=\varepsilon\frac{\pi}{2^{n+1}}.
\]

The orientation-factored scalar defect is

\[
D(x)=1-\frac{\sin x}{x}.
\]

It satisfies

\[
D(-x)=D(x)
\]

and begins with

\[
\boxed{D(x)=\frac{x^2}{6}-\frac{x^4}{120}+O(x^6)}.
\]

Thus the **first scalar precision residual is even and quadratic** after orientation is factored out. By contrast, the raw signed additive residual between signed phase and signed readout is odd.

This resolves the parity question in #1158 only after the residual type is specified; saying simply “the residual is even” would erase the signed orientation carrier.

## 12. Current G0 Cell verdict: positive G1 theorem, no canonical native derivation yet

The normalized-bisector theorem supplies an exact algebraic mechanism for the Viète recurrence at a rebuilt finite orientation-readout layer. It does **not** prove that the current native Cell transition law canonically realizes that mechanism.

Current Foundation freezes one Cell as the instantaneous rotating-segment state, while the exact Cell-to-orientation quotient and native six-dimensional rotation law remain unfinished. Independently, the accepted Q29 finite typed-countermodel result establishes at its declared scope

`NO_CANONICAL_ROTATION_LAW_SELECTED_BY_CURRENT_P000`.

Therefore the strongest current classification is:

\[
\boxed{
\text{G1/G2: exact target-free Viète refinement mechanism proved;}
}
\]

\[
\boxed{
\text{G0: canonical native Cell derivation is not supplied by current Foundation.}
}
\]

A native promotion would require additional noncircular structure establishing at least:

1. an operation-safe Cell/segment-to-oriented-state quotient;
2. an oriented quarter-turn seed or equivalent resolution-extension clause at the antipodal singularity;
3. compatibility of the normalized-bisector operation with the actual Cell transition/refinement semantics.

The first item cannot be silently replaced by a Euclidean circle embedding, and the second cannot be selected using the target value of \(\pi\).

## 13. #1158 resolution frontier

The research question now splits cleanly.

### Proved at finite algebraic/readout strength

- exact normalized segment-bisector operation forces the half-rotation square root;
- the real/longitudinal trace is the Viète plus nested radical;
- the transverse trace is the complementary minus radical;
- exact telescoping gives the finite precision readout \(\Pi_n\);
- \(\Pi_n\) is strictly increasing before analytic completion;
- classical completion converges to \(\pi\) with explicit \(O(4^{-n})\) error;
- the scalar first residual is reversal-even/quadratic, while signed transverse/additive residuals remain reversal-odd.

### Precisely unresolved at native Cell strength

- current P000 does not canonically choose the Cell-level rotation/refinement law;
- the antipodal half-turn cannot be bisected by the same normalized-resultant rule;
- the minimum coarse cyclic refinement that can supply the missing quarter-turn is \(C_{12}\), but declaring that refinement native still requires an additional typed bridge.

So the six-state orientation shell does not directly *contain* Viète. It supplies the half-turn seed; the first resolution doubling repairs the quarter-turn obstruction, and from that point onward the Viète radical tower is forced by normalized finite segment bisection.
