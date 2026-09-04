# Free Research — Odd-Simplex Energy Is a Graph Norm, Not a Lyapunov Function

Status: `FREE_RESEARCH_CORRECTION / EXACT MARKOV IDENTITY / FIXED-TYPE POSITIVE RECURRENCE NO-GO / TERMINAL COERCIVITY RETAINED / SIGNED OR GROWING-DEPTH ROUTE REQUIRED / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V17_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Research-Mode: `FREE_AXIOM_DISCOVERY`

## 1. Executive correction

V17 isolated one desired theorem: turn the normalized odd-simplex energy into a positive same-type two-channel recurrence. The local matrix and the terminal odd-chord coercivity are both correct, but they do not imply that the complete odd-simplex energy is itself a dissipative state.

There is an exact obstruction. For any Markov quotient operator `P`, any real field `f`, and residual

\[
e=(I+P)f,
\]

the expected energy of the complete odd two-simplex is

\[
\boxed{
\mathfrak O_P(f)
=2\bigl(f^2+P^2(f^2)+P(fe)+f\,Pe\bigr).
}
\tag{1.1}
\]

In the homogeneous limit `e=0`,

\[
\boxed{
\mathfrak O_P(f)=2\bigl(f^2+P^2(f^2)\bigr).
}
\tag{1.2}
\]

Thus the odd-simplex packet is an elliptic graph norm of the present amplitude and its even-depth return. It is not a one-step Lyapunov energy. Its direct composite chord is exactly what anchors the parity constant, but that chord also prevents the packet from being discarded as local dissipation.

Consequently, no universal proof may both:

1. retain the full odd chord with positive coefficient;
2. treat the resulting packet as a fixed finite-dimensional state;
3. demand a strict positive one-step recurrence for every field using only the local two-channel matrix.

The terminal inequality remains valid and essential. What fails is only the attempted use of the same packet as the contracting recursive state.

---

## 2. Abstract adaptive quotient operator

Let `X` be any finite or well-founded state space and let `P` be a positive Markov operator,

\[
(Pf)(x)=\mathbb E_x f(X_1).
\]

For the prime-winding application,

\[
(Pf)(n)
=
\frac1{A(n)}
\sum_{q\le n}\frac{\Lambda(q)}q
f\!\left(\left\lfloor\frac nq\right\rfloor\right),
\]

whenever `A(n)>0`.

Put

\[
R=f^2,
\qquad
e=f+Pf.
\tag{2.1}
\]

The one-edge signless energy is

\[
\mathcal E_1(f)
:=
\mathbb E_x|f(X_0)+f(X_1)|^2.
\tag{2.2}
\]

The transported edge energy is

\[
\mathcal E_{\rm tr}(f)
:=P\mathcal E_1(f),
\tag{2.3}
\]

and the direct two-step chord is

\[
\mathcal E_{\rm dir}(f)
:=
\mathbb E_x|f(X_0)+f(X_2)|^2.
\tag{2.4}
\]

Define the complete adaptive odd-simplex packet

\[
\boxed{
\mathfrak O_P(f)
:=
\mathcal E_1(f)+
\mathcal E_{\rm tr}(f)+
\mathcal E_{\rm dir}(f).
}
\tag{2.5}
\]

All three terms are nonnegative.

---

## OGN-T01 — Exact one-edge telescope

Since

\[
Pf=e-f,
\]

we have

\[
\begin{aligned}
\mathcal E_1(f)
&=f^2+2fPf+P(f^2)\\
&=P(f^2)-f^2+2fe.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal E_1(f)
=PR-R+2fe.
}
\tag{3.1}
\]

Along a Markov history `X_j`, this yields

\[
\boxed{
\mathbb E|f(X_j)+f(X_{j+1})|^2
=M_{j+1}-M_j+2\mathbb E[f(X_j)e(X_j)],
}
\tag{3.2}
\]

where

\[
M_j:=\mathbb E f(X_j)^2.
\]

Thus adjacent signless-edge energy telescopes across depth, up to the already bounded residual forcing.

---

## OGN-T02 — Exact direct-chord formula

Applying `P` to `Pf=e-f` gives

\[
P^2f=Pe-Pf=f-e+Pe.
\tag{4.1}
\]

Hence

\[
\begin{aligned}
\mathcal E_{\rm dir}(f)
&=f^2+2fP^2f+P^2(f^2)\\
&=3f^2+P^2(f^2)-2fe+2fPe.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal E_{\rm dir}(f)
=3R+P^2R-2fe+2fPe.
}
\tag{4.2}
\]

The direct chord is not a small residual term. In the exact alternating regime it is the macroscopic component that reads the surviving amplitude.

---

## OGN-T03 — Complete graph-norm identity

Transporting (3.1) gives

\[
\mathcal E_{\rm tr}(f)
=P^2R-PR+2P(fe).
\tag{5.1}
\]

Adding (3.1), (4.2), and (5.1), all intermediate `PR` and local `fe` terms cancel, leaving

\[
\boxed{
\mathfrak O_P(f)
=2\left(
R+P^2R+P(fe)+fPe
\right).
}
\tag{5.2}
\]

This is (1.1).

If `e=0` on the relevant two-step interior, then

\[
\boxed{
\mathfrak O_P(f)
=2(R+P^2R).
}
\tag{5.3}
\]

The complete positive odd simplex is therefore a present-plus-even-return norm.

---

## 6. Compatibility with the odd-triangle anchor

For every individual two-step history, writing

\[
x=f(X_0),\quad y=f(X_1),\quad z=f(X_2),
\]

gives

\[
2x=(x+y)+(x+z)-(y+z).
\]

Consequently

\[
4x^2
\le3\bigl((x+y)^2+(x+z)^2+(y+z)^2\bigr).
\]

After expectation,

\[
\boxed{
4R\le3\mathfrak O_P(f).
}
\tag{6.1}
\]

There is no contradiction between (5.2) and (6.1): the chord makes the graph norm coercive, but coercivity is not dissipation.

For the prime-winding pair simplex this remains the correct one-time terminal scalar readout.

---

## OGN-N01 — Fixed-type positive recurrence no-go

Consider an interior two-colour Markov tree on which every child has the opposite field value,

\[
f(X_{j+1})=-f(X_j),
\]

and the boundary is placed beyond the finite depth under examination. Then `e=0` on that interior and `R` is constant along every even-depth return. Hence

\[
\mathfrak O_P(f)=4R,
\qquad
P\mathfrak O_P(f)=4R.
\]

Therefore no inequality

\[
\mathfrak O_P(f)
\le q\,P\mathfrak O_P(f)
\tag{7.1}
\]

with `q<1` can hold as a universal local positive theorem.

The arithmetic quotient carrier prevents a globally exact alternating field through recoalescence and boundary effects. But any proof of contraction must use those genuinely global inputs. It cannot be obtained from the local odd-simplex algebra and positivity alone.

This is the energy-level counterpart of the small-action Weyl sequence and the fixed-provenance-depth no-go already found in V16.

---

## 8. Consequence for the V17 target

The V17 target

\[
\overline{\mathfrak E}(N)
\longmapsto(R(N),V(N))
\]

cannot mean that the whole positive odd-simplex graph norm is itself transported by the local two-channel matrix as a strict same-type Lyapunov state.

The correct architecture must split its roles:

1. **terminal role:** the full odd chord anchors the parity constant and reads `r(N)` once;
2. **recursive role:** adjacent-edge carré-du-champ and retained standard channels telescope or mix across depth;
3. **global role:** signed history cancellation, arithmetic recoalescence, a growing-depth commutator fold, or a slow-oscillation theorem removes the surviving even-depth component.

Equivalently,

\[
\boxed{
\text{ODD SIMPLEX = TERMINAL COERCIVE GRAPH NORM},
\qquad
\text{NOT A FIXED-DEPTH POSITIVE LYAPUNOV FUNCTION}.
}
\]

---

## 9. New minimal target

A valid next theorem may take either of two forms.

### Signed Green route

Control the alternating even-depth component in (5.2) through the exact stopping expansion

\[
f(n)=f(1)\mathbb E_n(-1)^\tau+
\mathbb E_n\sum_{j<\tau}(-1)^je(X_j).
\]

### Growing commutator-jet route

Replace the fixed two-channel state by a finite but depth-dependent Volterra/provenance jet. The first jet defect is exactly the parity-fold scalar carrier; higher jets compare tail-capacity moments with ordered multi-history continuation measures.

The companion V18 commutator note develops the second route.

---

## 10. Classification

Closed exactly:

1. one-edge second-moment telescope;
2. direct two-step chord formula;
3. complete graph-norm identity (5.2);
4. compatibility with terminal odd-triangle coercivity;
5. universal fixed-type positive-recurrence no-go;
6. separation of terminal and recursive roles.

Still open:

1. control of the even-depth return by a signed or growing-depth state;
2. arithmetic stability of the alternating Green kernel;
3. a commutator-jet norm that closes under the moving prime-power cutoff;
4. a promoted native quantitative prime remainder;
5. any RH-scale, Working Truth, or Foundation claim.
