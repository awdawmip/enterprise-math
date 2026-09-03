# Uniqueness of the Euler rotation-character completion

Status: `FREE_RESEARCH / FINITE-ALGEBRAIC CORE + STANDARD METRIC COMPLETION / NOT FOUNDATION`  
Date: `2026-09-04`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Purpose

The preceding local package constructed, from the current six-gate Cell geometry,

1. a six-direction rotor `G`;
2. an actual twelve-phase Cell/gate square root `H`;
3. the chiral complex-structure operator
   \[
   J=H^3=r(R-R^{-1}),\qquad J^2=-1;
   \]
4. a chirality-selected dyadic root tower
   \[
   K_{n+1}^2=K_n;
   \]
5. nested finite polygon bounds with common completion `L`;
6. a geometric proof that
   \[
   L=\pi.
   \]

A remaining conceptual objection was that an abstract chain of finite cyclic groups does not by itself force the standard unit-circle group or the standard exponential completion.

This note closes that objection at the **derived rotation-character layer**.

The central result is:

\[
\boxed{
\text{Cell-derived }J
+\text{normalized quadratic isometry}
+\text{dyadic rotor states}
\Longrightarrow
S_J^1\cong U(1)
}
\]

with a unique continuous phase extension

\[
\operatorname{Exp}_J:\mathbf R\longrightarrow S_J^1
\]

of period `2L=2pi` satisfying

\[
\operatorname{Exp}_J(L)=-1,
\qquad
\operatorname{Exp}_J(L/2)=J.
\]

The word “unique” here is typed precisely: unique normalized positive quadratic norm invariant under the quarter-turn `J`, followed by uniqueness of metric completion and uniqueness of continuous extension from a dense subgroup.

## 2. The character algebra

Work in the real two-dimensional algebra

\[
A_J=\mathbf R[J]/(J^2+1).
\]

Every element is uniquely

\[
z=x+yJ.
\]

Conjugation is

\[
\overline{x+yJ}=x-yJ.
\]

The already derived operator `J` is not declared to be a primitive spatial axis. It is the Cell-radius-normalized chiral difference between positive and negative right-turn transport.

Freeze boundary:

`J_IS_DERIVED_ROTATION_COMPLEX_STRUCTURE_NOT_NATIVE_SPATIAL_AXIS`.

## 3. Unique normalized quadratic rotation norm

Let a general real quadratic form on the coordinate pair `(x,y)` be

\[
q(x,y)=a x^2+2bxy+c y^2.
\]

Multiplication by `J` sends

\[
(x,y)\longmapsto(-y,x).
\]

Assume:

1. `J` is an isometry:
   \[
   q(-y,x)=q(x,y)
   \quad\text{for all }x,y;
   \]
2. the identity state is normalized:
   \[
   q(1,0)=1.
   \]

Evaluating invariance at `(1,0)` gives

\[
c=a.
\]

Evaluating at `(1,1)` gives

\[
a-2b+c=a+2b+c,
\]

hence

\[
b=0.
\]

Normalization gives `a=1`, so also `c=1`. Therefore

\[
\boxed{
q(x,y)=x^2+y^2.
}
\]

Thus the unit character conic

\[
S_J^1=\{x+yJ:x^2+y^2=1\}
\]

is not one arbitrarily chosen ellipse among many. It is the unique normalized positive quadratic rotation shell on which the Cell-derived quarter-turn operator acts isometrically.

This theorem does not identify `q` with the primitive Enterprise native metric. It selects the norm of the **derived character representation**.

## 4. Multiplication preserves the unique norm

For

\[
z=x+yJ,
\qquad
w=u+vJ,
\]

one has

\[
zw=(xu-yv)+(xv+yu)J.
\]

Consequently

\[
\begin{aligned}
\lVert zw\rVert^2
&=(xu-yv)^2+(xv+yu)^2\\
&=(x^2+y^2)(u^2+v^2).
\end{aligned}
\]

Hence `S_J^1` is a group under multiplication. Conjugation is inversion on the unit shell:

\[
z^{-1}=\overline z.
\]

This is the exact finite algebra behind the usual complex unit circle; no exponential, sine, cosine or numerical value of `pi` is needed.

## 5. The nested dyadic state subgroup

Let

\[
N_n=6\cdot2^n
\]

and let `K_n` be the chirality-selected rotor of order `N_n`, with

\[
K_{n+1}^2=K_n,
\qquad
K_n^{N_n/2}=-1.
\]

Define

\[
D_n=\langle K_n\rangle
=\{K_n^k:0\le k<N_n\}.
\]

Because `K_(n+1)^2=K_n`,

\[
D_n\subset D_{n+1}.
\]

Set

\[
D=\bigcup_{n\ge0}D_n.
\]

Then `D` is a subgroup of `S_J^1`. Abstractly,

\[
D\cong
\left(\frac16\mathbf Z[1/2]\right)\big/\mathbf Z,
\]

through

\[
\frac{k}{6\cdot2^n}\longmapsto K_n^k.
\]

This map is well defined because refinement replaces `(k,N_n)` by `(2k,2N_n)` without changing the state.

## 6. The mesh tends to zero without an angle coordinate

Write

\[
K_n=c_n+s_nJ,
\qquad
c_n^2+s_n^2=1,
\qquad
s_n>0,
\]

and let

\[
\tau_n=\frac{s_n}{1+c_n}>0.
\]

The positive root recurrence gives

\[
\tau_n=rac{2\tau_{n+1}}{1-\tau_{n+1}^2}.
\]

Therefore

\[
0<\tau_{n+1}<\frac{\tau_n}{2}.
\]

The chord mesh of the regular `N_n` phase polygon is

\[
\delta_n=\lVert K_n-1\rVert.
\]

Since

\[
\delta_n=2s_{n+1}
=\frac{4\tau_{n+1}}{1+\tau_{n+1}^2},
\]

one has

\[
0<\delta_n<4\tau_{n+1}
<\frac{4\tau_1}{2^n}.
\]

Thus

\[
\boxed{\delta_n\longrightarrow0.}
\]

No real angle parameter is used: shrinking is certified entirely by the algebraic Cayley/root recurrence.

The finite phase polygons visit the whole unit conic in cyclic order, and their maximum chord mesh tends to zero. Hence `D` is dense in `S_J^1` for the uniquely selected quadratic metric.

The final density implication is standard compact planar geometry; the mesh estimate itself is target-free and algebraic.

## 7. Why the completion is necessarily the unit circle group

The subgroup `D` already sits isometrically in `S_J^1`, and Section 6 shows that its image is dense. Therefore the metric completion of `D` is uniquely isometric to `S_J^1`.

Since multiplication and inversion are continuous on the finite-dimensional normed algebra, they extend uniquely from the dense subgroup. Thus the completed topological group is

\[
\boxed{
\widehat D\cong S_J^1.
}
\]

After choosing the standard scalar avatar `J -> i`, this is exactly the usual group `U(1)`.

The conclusion is not that the full Enterprise space is the complex plane. It is:

\[
\boxed{
\text{the unique normalized metric completion of the finite rotation character states is }U(1).
}
\]

This closes the earlier `FINITE_ROOT_TOWER_DOES_NOT_YET_SELECT_UNIQUE_U1` boundary at the derived character level.

## 8. The intrinsic phase lift

The preceding polygon theorem defines

\[
L=\pi
\]

internally as the common area/semiperimeter completion. Before applying the name `pi`, retain the symbol `L`.

Let

\[
\Lambda=\frac16\mathbf Z[1/2]\subset\mathbf R.
\]

For `q=k/N_n`, define the finite state

\[
\chi_D(q)=K_n^k.
\]

Define its lifted forward phase length by

\[
\ell(q)=2Lq.
\]

This phase scale is itself the limit of finite polygonal path lengths. Indeed, if the state `K_n^k` is represented at refinement depth `m>=n`, its forward polygonal length is

\[
\ell_{m}(q)
=k2^{m-n}\lVert K_m-1\rVert.
\]

Since

\[
N_m\lVert K_m-1\rVert
=2A_{m+1}^-
\longrightarrow2L,
\]

one obtains

\[
\ell_m(q)\longrightarrow2L\frac{k}{N_n}=2Lq.
\]

Thus additive phase is not inserted before the finite rotations. It is the compatible completion of refined polygonal travel.

## 9. Unique geometric exponential

The scaled lift

\[
2L\Lambda
\]

is dense in `R`. On it define

\[
E_J(2Lq)=\chi_D(q).
\]

This is a group homomorphism, because finite characters multiply according to phase addition. It is uniformly continuous for the completed phase metric, and therefore has a unique continuous extension

\[
\boxed{
\operatorname{Exp}_J:\mathbf R\longrightarrow S_J^1.
}
\]

It satisfies

\[
\operatorname{Exp}_J(t+u)
=\operatorname{Exp}_J(t)\operatorname{Exp}_J(u),
\]

and its kernel is

\[
2L\mathbf Z.
\]

Consequently

\[
\boxed{
\mathbf R/(2L\mathbf Z)\cong S_J^1.
}
\]

On the dense finite subgroup,

\[
\operatorname{Exp}_J\left(2L\frac{k}{N_n}\right)=K_n^k.
\]

In particular,

\[
\boxed{
\operatorname{Exp}_J(L)=-1,
}
\]

and, from the actual C12 layer,

\[
\boxed{
\operatorname{Exp}_J(L/2)=J.
}
\]

Changing chirality replaces `J` by `-J` and reverses the parameter. The half-turn endpoint remains unchanged.

The notation `exp(Jt)` may now be used for this unique continuous character extension. In this typing, the scalar constant `e` is not a primitive spatial ingredient; it belongs to an analytic representation of the already defined one-parameter rotation group.

## 10. Intrinsic cosine and sine

Define coordinate readouts from the completed character itself:

\[
C_L(t)
=\frac{\operatorname{Exp}_J(t)+\operatorname{Exp}_J(-t)}2,
\]

\[
S_L(t)
=\frac{\operatorname{Exp}_J(t)-\operatorname{Exp}_J(-t)}{2J}.
\]

Then identically

\[
\boxed{
\operatorname{Exp}_J(t)=C_L(t)+J S_L(t).
}
\]

The addition formulas are consequences of the group law:

\[
C_L(t+u)=C_L(t)C_L(u)-S_L(t)S_L(u),
\]

\[
S_L(t+u)=S_L(t)C_L(u)+C_L(t)S_L(u).
\]

Also

\[
C_L(t)^2+S_L(t)^2=1.
\]

After the geometric polygon theorem identifies `L=pi` and the scalar representation sends `J` to `i`, these intrinsic coordinate functions are the classical cosine and sine. Thus Euler's formula is not used to define the finite states; it is the coordinate decomposition of their unique continuous completion.

## 11. Cell-rooted Euler identity

The completed statement is

\[
\boxed{
\operatorname{Exp}_J(L)+1=0.
}
\]

The Cell polygon theorem gives `L=pi`, so

\[
\boxed{
\operatorname{Exp}_J(\pi)+1=0.
}
\]

Under `J -> i`,

\[
\boxed{e^{i\pi}+1=0.}
\]

Its geometric content is now fully layered:

- `-1` is orientation reversal;
- `J` is the uniquely normalized chiral quarter-turn structure derived from Cell rotation;
- `L=pi` is the area/half-perimeter completion of the Cell-rooted polygon tower;
- `Exp_J` is the unique continuous extension of the dense finite rotation characters;
- the equation says that completed travel through one geometric half-period equals reversal.

## 12. What is now closed and what remains open

Closed at the local derived-character level:

1. exact C6 direction quotient from ordered adjacent Cell pairs modulo translation;
2. actual C12 Cell/gate refinement;
3. Cell-radius derivation of `J^2=-1`;
4. chirality-selected dyadic bisector tower;
5. target-free finite lower/upper period and area bounds;
6. geometric identification `L=pi`;
7. unique normalized quadratic character norm;
8. density of the finite rotor union;
9. uniqueness of its metric group completion as `U(1)`;
10. unique continuous exponential extension and Euler identity.

Still open or deliberately excluded:

1. a theorem that every admissible full six-dimensional native rotation trajectory factors through this local character system;
2. identification of the character norm with the primitive native length metric;
3. a physical one-step Cell realization of refinement levels beyond C12;
4. an intertwiner identifying this dyadic `C2` hierarchy with the tetrahedral or paired-Pell `C2` classes;
5. historical novelty for the classical algebra of unit-circle completion, rational/dyadic density, Viète products or polygon exhaustion.

Candidate freeze:

`AC-EM-FREE-F6D046-EULER-CHARACTER-COMPLETION-UNIQUENESS-V1`:

> The Cell-derived chiral operator J uniquely selects the normalized quadratic character norm x^2+y^2. The nested finite rotors form a dense subgroup of its unit conic because their algebraically certified chord mesh tends to zero. Metric and group completion therefore force the standard unit-circle group, and finite polygonal travel uniquely extends to a continuous phase character Exp_J of period 2L. Since the Cell-rooted polygon completion gives L=pi, Exp_J(pi)=-1 and, under J->i, e^(i pi)+1=0.