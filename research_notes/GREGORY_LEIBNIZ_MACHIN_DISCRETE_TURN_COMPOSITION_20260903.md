# Gregory–Leibniz / Machin as exact discrete turn composition

Status: `FREE_RESEARCH / EXACT_RATIONAL_TURN_CALCULUS + FAREY_REFINEMENT + CLASSICAL_COMPLETION / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Issue returns: comments `5525994652`, `5526054300`

## 1. Question and boundary

Issue #1160 asks whether arctangent-based pi identities can be split into:

1. an exact finite integer/rational rotation-composition layer;
2. a finite-resolution direction/winding readout;
3. a later analytic completion in which real `arctan`, Gregory–Leibniz, and pi appear.

The required falsification forbids defining the native turn by `arctan(y/x)`.

This note gives a positive answer. The algebraic carrier below is a two-coordinate **rotation certificate/readout carrier**. It is not asserted to replace the P000 six-dimensional spatial substrate.

Freeze:

`INTEGER_DIRECTION_CERTIFICATE != FULL_ENTERPRISE_6D_SPATIAL_ONTOLOGY`.

No historical novelty is claimed for Gaussian integers, Farey/Stern–Brocot arithmetic, the arctangent series, or Machin's formula. The project-level result is the exact typing and composition bridge among these layers.

## 2. Native rational-turn group

Let

\[
\mathcal T_{\mathbf Q}=\mathbf Q(i)^\times/\mathbf Q_{>0}^\times.
\]

Positive rational scale is erased; orientation is not. Every class has a primitive integer representative `(a,b)` after clearing denominators and dividing by the positive gcd.

Define Gaussian pair multiplication

\[
(a,b)\star(c,d)=(ac-bd,\ ad+bc).
\]

For a direction state `v=(x,y)`, the raw action is

\[
(a,b)\star(x,y)=(ax-by,\ bx+ay).
\]

This is exact integer arithmetic. Composition is associative and commutative at the turn-factor level before any real angle is introduced.

Define reciprocal-turn generators

\[
U_q^+=[q+i],\qquad U_q^-=[q-i]=(U_q^+)^{-1},\qquad q\in\mathbf N_{>0}.
\]

On a rational slope `s=y/x`, where denominators are nonzero,

\[
U_q^+(s)=\frac{qs+1}{q-s},
\qquad
U_q^-(s)=\frac{qs-1}{q+s}.
\]

Thus the core turn law survives the Issue #1160 falsification gate with no `arctan` input.

## 3. Relative-turn theorem

For integer directions

\[
u=(a,b),\qquad v=(c,d),
\]

define

\[
\operatorname{Rel}(u,v)
=(u\cdot v,\det(u,v))
=(ac+bd,\ ad-bc).
\]

Then

\[
\boxed{
 u\star\operatorname{Rel}(u,v)=\|u\|_2^2v.
}
\]

Indeed,

\[
a(ac+bd)-b(ad-bc)=(a^2+b^2)c,
\]

and

\[
a(ad-bc)+b(ac+bd)=(a^2+b^2)d.
\]

Hence, after positive-scale quotient,

\[
\boxed{[u]\,[\operatorname{Rel}(u,v)]=[v].}
\]

This is the exact algebraic relative-turn law.

### 3.1 Unimodular edge corollary

If primitive rays satisfy

\[
|\det(u,v)|=1,
\]

then their exact relative turn is a reciprocal integer generator

\[
\boxed{[u\cdot v\pm i].}
\]

Therefore every unimodular/Farey neighbor edge has an integer reciprocal-turn label equal to the dot product of its endpoints.

## 4. Machin's formula as an exact integer path

Starting at slope zero, apply four `U_5^+` turns:

\[
0\to\frac15\to\frac5{12}\to\frac{37}{55}\to\frac{120}{119}.
\]

Then one `U_{239}^-` correction gives

\[
\frac{120}{119}\to1.
\]

The same certificate in Gaussian integers is

\[
(5+i)^4=4(119+120i),
\]

and

\[
(119+120i)(239-i)=28561(1+i)=169^2(1+i).
\]

Therefore

\[
\boxed{(5+i)^4(239-i)=114244(1+i).}
\]

No real angle or pi is required to verify this identity.

### 4.1 Why the integer 239 appears

Let

\[
u=(119,120),\qquad d=(1,1).
\]

Then

\[
\det(u,d)=-1,
\qquad
u\cdot d=239.
\]

By the relative-turn theorem, the exact correction from the fourth-power primitive direction to the diagonal is

\[
\boxed{(239,-1).}
\]

Thus `239` is the dot-product label of the final unimodular correction edge. Equivalently,

\[
120-119=1,
\qquad
120+119=239,
\qquad
119^2+120^2=169^2.
\]

Machin's constant is therefore already encoded in the finite integer endpoint geometry.

## 5. General repeated-turn / one-correction criterion

Let

\[
\operatorname{prim}((q+i)^k)=(A,B),
\qquad A,B>0,\quad \gcd(A,B)=1,
\]

and target the diagonal `d=(1,1)`.

The relative factor is

\[
\operatorname{Rel}((A,B),d)=(A+B,A-B).
\]

Since

\[
\gcd(A+B,A-B)\mid2,
\]

a single **primitive reciprocal-integer** correction exists, apart from the already-diagonal case, iff

\[
\boxed{|A-B|\in\{1,2\}.}
\]

Then the correction denominator is

\[
\boxed{r=\frac{A+B}{|A-B|},}
\]

and its sign is the sign of `A-B`.

Examples:

- `q=2,k=1`: `(A,B)=(2,1)`, `r=3`;
- `q=2,k=2`: `(A,B)=(3,4)`, `r=7`;
- `q=3,k=1`: `(A,B)=(3,1)`, `r=2`;
- `q=3,k=2`: `(A,B)=(4,3)`, `r=7`;
- `q=5,k=4`: `(A,B)=(119,120)`, `r=239`.

An exact bounded census over

\[
2\le q\le500,
\qquad
1\le k\le50,
\]

restricted only to positive first-quadrant primitive powers found exactly these five cases. This is finite computational evidence, not a global classification theorem.

## 6. Finite-resolution direction and winding readout

Before introducing real angle, use a finite dihedrally completed Farey fan `F_H`.

Within each octant, retain primitive rational rays to Farey height `H`, ordered entirely by quadrant signs and integer determinants. An arbitrary rational direction is represented by either:

- an exact fan ray; or
- the pair of adjacent fan rays bracketing it.

A turn word obtains an **unwrapped sector index** by lifting the cyclic fan index according to the declared sign of each `U_q^\pm` step. This is a finite direction/winding readout; no `arctan` is part of its definition.

For adjacent fan rays `u,v`,

\[
|\det(u,v)|=1.
\]

Hence the native edge label is

\[
(D,\pm1),\qquad D=u\cdot v.
\]

Only after analytic completion is its real angular width

\[
\arctan(1/D)<1/D.
\]

For the Machin final edge

\[
(119,120)\to(1,1),
\]

the finite residual coordinate is exactly

\[
D=239.
\]

At fan height `H>=120`, both rays are represented exactly. The displayed Machin prefix stays in the first quadrant and the final correction returns to the diagonal, so the completion branch has winding zero and cannot hide a `2\pi` ambiguity.

## 7. Farey–Machin path theorem

Let

\[
v_0=(1,0),\ v_1,\ldots,v_m=(1,1)
\]

be a monotone first-quadrant chain of primitive rays satisfying

\[
\det(v_{j-1},v_j)=1.
\]

Set

\[
D_j=v_{j-1}\cdot v_j.
\]

By the relative-turn theorem,

\[
[v_{j-1}][D_j+i]=[v_j].
\]

Therefore, exactly in the native rational-turn group,

\[
\boxed{
[1+i]=\prod_{j=1}^m[D_j+i].
}
\]

A signed unimodular chain gives the corresponding signed product, with the unwrapped finite fan index carrying the winding branch.

After analytic completion, a monotone chain yields

\[
\boxed{
\frac\pi4=\sum_{j=1}^m\arctan\frac1{D_j}.
}
\]

Examples:

\[
(1,0)\to(2,1)\to(1,1)
\]

has labels `2,3`, giving

\[
\frac\pi4=\arctan\frac12+\arctan\frac13.
\]

The chain

\[
(1,0)\to(3,1)\to(2,1)\to(1,1)
\]

has labels `3,7,3`, giving

\[
\frac\pi4=2\arctan\frac13+\arctan\frac17.
\]

Machin's word is a compressed signed path. Four coarse `U_5^+` jumps land one unimodular edge beyond the diagonal. Indeed

\[
\boxed{[5+i]^4=[1+i][239+i],}
\]

because

\[
(5+i)^4=2(1+i)(239+i).
\]

The usual negative `239` term is exactly the operation of moving that overshoot edge to the other side of the identity.

## 8. Exact mediant refinement theorem

Take one positive unimodular edge

\[
u\to v,\qquad \det(u,v)=1,\qquad D=u\cdot v.
\]

Insert the mediant ray

\[
w=u+v.
\]

The refined labels are

\[
D_1=u\cdot w=\|u\|^2+D,
\qquad
D_2=w\cdot v=D+\|v\|^2.
\]

Both refined edges remain unimodular.

Lagrange's identity gives

\[
\|u\|^2\|v\|^2=D^2+1.
\]

Therefore

\[
D_1D_2-D(D_1+D_2)=1,
\]

and

\[
D_1+D_2=\|u+v\|^2=\|w\|^2.
\]

Hence the exact integer refinement law is

\[
\boxed{
(D_1+i)(D_2+i)=\|w\|^2(D+i).
}
\]

So one finite native turn is replaced by two finite native turns before any analytic angle is introduced.

At completion,

\[
\boxed{
\arctan\frac1D
=\arctan\frac1{D_1}+\arctan\frac1{D_2}.
}
\]

The first refinement of the diagonal edge is

\[
1\mapsto(2,3),
\]

because

\[
(2+i)(3+i)=5(1+i).
\]

Refining the `D=2` edge gives

\[
2\mapsto(3,7),
\]

because

\[
(3+i)(7+i)=10(2+i).
\]

Thus the familiar small Machin identities sit inside a recursively generated Stern–Brocot/Farey turn-refinement hierarchy.

## 9. Refinement strictly lowers the equal-depth completion residual proxy

The same determinant-one identity gives

\[
\frac1{D_1}+\frac1{D_2}
=\frac1D-\frac1{DD_1D_2}
<\frac1D.
\]

Since `D_1,D_2>D`, for every real `p>=1`,

\[
\boxed{D_1^{-p}+D_2^{-p}<D^{-p}.}
\]

Define the integer-labeled path cost

\[
C_p(P)=\sum_{e\in P}D_e^{-p}.
\]

Every mediant refinement satisfies

\[
\boxed{C_p(P_{\mathrm{refined}})<C_p(P),\qquad p\ge1.}
\]

This is a finite arithmetic monotonicity theorem.

It becomes an analytic completion-error theorem because the `N`th arctangent truncation has exponent

\[
p=2N+3.
\]

Thus, at fixed truncation depth per factor, every Farey mediant refinement strictly improves the sum of standard completion-error upper bounds.

This does **not** prove fixed-total-work optimality: refinement also increases the number of factors. The correct fixed-compute optimization is a separate problem.

## 10. Analytic completion and the Gregory–Leibniz boundary

Only now introduce the classical completion character in the first quadrant:

\[
\Theta([q+i])=\arctan(1/q).
\]

The diagonal generator is the single finite native turn

\[
U_1^+=[1+i].
\]

Its completion is

\[
\Theta(U_1^+)=\frac\pi4.
\]

The Gregory–Leibniz series is therefore not the native turn. It is the boundary power-series expansion of the analytic readout:

\[
\frac\pi4
=\arctan(1)
=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
\]

For `q>=1`, define the finite rational truncation

\[
A_N(q)=\sum_{n=0}^{N}
\frac{(-1)^n}{(2n+1)q^{2n+1}}.
\]

Using the finite geometric identity for `1/(1+t^2)` and integrating only at the completion layer gives

\[
R_N(q)
:=\arctan(1/q)-A_N(q)
=(-1)^{N+1}\int_0^{1/q}\frac{t^{2N+2}}{1+t^2}\,dt.
\]

Therefore

\[
\boxed{
\frac{q^2}{q^2+1}
\frac1{(2N+3)q^{2N+3}}
\le |R_N(q)|
\le
\frac1{(2N+3)q^{2N+3}}.
}
\]

At `q=1`, this is the slow Gregory–Leibniz boundary completion.

## 11. Machin truncation hierarchy

The exact native factorization is

\[
U_1^+=(U_5^+)^4U_{239}^-.
\]

Applying analytic completion gives

\[
\frac\pi4
=4\arctan\frac15-\arctan\frac1{239}.
\]

At equal truncation depth define

\[
M_N=4A_N(5)-A_N(239).
\]

The two remainders have the same alternating sign, and

\[
4|R_N(5)|>|R_N(239)|.
\]

Hence

\[
\boxed{
0<(-1)^{N+1}\left(\frac\pi4-M_N\right)
<\frac{4}{(2N+3)5^{2N+3}}.
}
\]

This gives a certified alternating finite hierarchy.

The structural reason for the acceleration is now exact:

`FINITE DIAGONAL TURN -> NATIVE RATIONAL FACTORIZATION -> ANALYTIC SERIES`.

Direct Gregory–Leibniz expands the diagonal turn at the boundary `1`. Machin first factors the same finite turn into factors read out at `1/5` and `1/239`, then expands. The geometric decay is a completion consequence of the finite factorization, not part of the native definition.

For scale only:

- the equal-depth Machin bound is below `10^-6` already at `N=3`;
- it is below `10^-10` at `N=6`;
- the direct Gregory alternating bound would require about `5*10^5` and `5*10^9` terms respectively.

## 12. First full-refinement examples

Starting from the single diagonal edge, full mediant refinement gives edge-label sets:

- level 0: `[1]`;
- level 1: `[2,3]`;
- level 2: `[3,7,8,5]`;
- level 3: `[4,13,17,12,13,21,18,7]`.

For `p=3`, the exact-path residual proxies are approximately

- level 0: `1`;
- level 1: `0.162037`;
- level 2: `0.049906`;
- level 3: `0.0205125`.

The monotone decrease follows theoremically from local refinement, not from these decimal checks.

The compressed Machin word `[5,5,5,5,-239]` has absolute `p=3` proxy

\[
4\cdot5^{-3}+239^{-3}\approx0.0320001.
\]

This comparison does not establish a global optimum; it shows that compressed signed factorizations and edge-by-edge positive refinements occupy the same discrete optimization landscape.

## 13. Tool reuse / prior-art boundary

Phase-B repository lookup found no existing Enterprise Math result indexed under Gaussian-integer rotation, rational-slope Machin composition, or Farey winding. The existing `T5 Integer Precision / Refinement Calculus` is the appropriate general precision family; this note treats the Farey fan hierarchy as a task-local mathematical specialization and does **not** propose a new global tool family.

Classical ingredients remain classical prior art:

- Gaussian integer multiplication;
- determinant/dot-product angle identities after classical completion;
- Farey/Stern–Brocot unimodular adjacency;
- Gregory–Leibniz and arctangent power series;
- Machin's formula itself.

No historical novelty claim is made for those ingredients.

## 14. Current theorem packet

The strongest exact results established here are:

1. `RATIONAL_TURN_GROUP`: finite integer/rational turn composition exists without `arctan` input.
2. `RELATIVE_TURN`: `Rel(u,v)=(u·v,det(u,v))` maps the ray of `u` exactly to the ray of `v`.
3. `MACHIN_239_CERTIFICATE`: the fourth `U_5` state is `(119,120)`, unimodular-adjacent to `(1,1)`, with dot label `239`.
4. `ONE_CORRECTION_CRITERION`: for primitive `(A,B)`, one reciprocal correction to the diagonal exists iff `|A-B| in {1,2}`.
5. `FAREY_MACHIN_PATH`: every finite unimodular path gives an exact reciprocal-turn product certificate and, after completion, a Machin-type identity.
6. `MEDIANT_REFINEMENT`: `(D_1+i)(D_2+i)=||u+v||^2(D+i)` under a Farey mediant split.
7. `REFINEMENT_RESIDUAL_MONOTONICITY`: `C_p` strictly decreases under every mediant refinement for `p>=1`.
8. `COMPLETION_SEPARATION`: Gregory–Leibniz appears only as the analytic boundary expansion of the already finite diagonal turn.
9. `MACHIN_TRUNCATION_BOUND`: equal-depth Machin truncations alternate around `pi/4` with error below `4/((2N+3)5^(2N+3))`.

The Issue #1160 no-go branch is therefore not triggered.

## 15. Open frontier

The next nontrivial problems are now sharply separated:

- classify repeated-generator states `prim((q+i)^k)` whose reduced determinant to a target ray is one; the finite `q<=500,k<=50` census is not a proof of global classification;
- define and solve a **fixed-total-work** optimization problem for reciprocal-turn factorizations, since fixed-depth refinement always helps but increases factor count;
- determine whether a canonical shortest or Pareto-optimal signed path exists under a declared cost model;
- only after such algebraic questions are stable, test whether any of this certificate carrier admits a justified operation-safe bridge to a genuinely native Enterprise rotation quotient. No such Foundation promotion is claimed here.
