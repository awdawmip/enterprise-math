# P018 — Finite-Precision Proof Calculus: Supplement 09

Status: `ACTIVE RESEARCH NOTE`  
Scope: operation-scheduling holonomy, defect transport, cross-scale composition, and strict recovery thresholds  
Depends on: P018-T11, T12, T72, T73, T75, T87  
Discipline: this note does not treat the word “holonomy” itself as a discovery. The mathematical question is whether the existing collapse/refinement noncommutation admits an exact, finite, composable path-difference calculus without hidden continuum structure.

## 1. What remains after T87

Supplement 08, T87 proves that when a path contains only canonical precision projections and those projections depend only on their endpoints, endpoint-defect path curvature is automatically zero.

A genuinely nonzero path effect must therefore come from changing operation order.

P018 stage 1 already contains the smallest example. For `d|e`, define

\[
S_{p,d}(n)=R_p(nd^p),
\qquad
C_{p,d}(n)=S_{p,d}(n)^p,
\]

and define “collapse at the finer level, then project back to the coarse level” by

\[
\mathcal R_{p;e\to d}(n)
=
C_{p,e}(n)//(e/d)^p.
\]

T11 defines

\[
\chi_{p;e:d}(n)
=
\mathcal R_{p;e\to d}(n)-C_{p,d}(n)
\ge0.
\]

In path language,

\[
\boxed{
\chi_{p;e:d}(n)
=
(\text{refine to }e\to\text{collapse}\to\text{project to }d)
-
(\text{collapse at }d).
}
\]

This is not a coordinate difference between scale-only paths. It is an **operation-scheduling holonomy** measuring failure of collapse to commute with precision projection.

The theorem content of T11 is unchanged; this note places it in the correct position inside the new atlas/defect framework.

---

## 2. P018-T88 — General nonnegative defect transport

Status: `PROVED`

Fix `m>=1`. For an explicit integer base state `a>=0` and a nonnegative defect `h>=0`, define

\[
\boxed{
\mathcal T_m(a,h)
=Q_m(a+h)-Q_m(a)
=(a+h)//m-a//m.
}
\]

It measures how much of a fine-state difference `h` remains visible after projecting to a coarser layer.

Write

\[
a=mA+u,
\qquad
h=mH+v,
\qquad
0\le u,v<m.
\]

T72 gives immediately

\[
\boxed{
\mathcal T_m(a,h)
=
H+\kappa_m(u,v)
=
Q_m(h)+\kappa_m(a\bmod m,h\bmod m).
}
\]

Defect transport therefore splits into

\[
\boxed{
\text{transported defect bulk}
+
\text{boundary-crossing carry}.
}
\]

This is the first direct connection between the carry theorem T72 and a genuine operation-path defect.

---

## 3. P018-T89 — Defect transport has strict cross-scale coherence

Status: `PROVED`

For `m,n>=1`,

\[
\boxed{
\mathcal T_{mn}(a,h)
=
\mathcal T_m\bigl(Q_n(a),\mathcal T_n(a,h)\bigr).
}
\]

### Proof

Integer quotient composes as

\[
Q_m(Q_n(x))=Q_{mn}(x),
\]

and

\[
Q_n(a+h)=Q_n(a)+\mathcal T_n(a,h).
\]

Therefore

\[
\begin{aligned}
\mathcal T_m(Q_n(a),\mathcal T_n(a,h))
&=Q_m(Q_n(a)+\mathcal T_n(a,h))-Q_m(Q_n(a))\\
&=Q_m(Q_n(a+h))-Q_m(Q_n(a))\\
&=Q_{mn}(a+h)-Q_{mn}(a)\\
&=\mathcal T_{mn}(a,h).
\end{aligned}
\]

∎

Thus defect transport itself is strictly composable along a canonical precision chain even though it contains carry.

The structural lesson is:

> **An operation may fail to commute with projection while its resulting path defect still obeys its own coherent transport law.**

This is weaker than forcing the original operation to be strictly natural, and better matches finite-precision arithmetic.

---

## 4. P018-T90 — Exact cross-level composition of collapse holonomy

Status: `PROVED`

Let

\[
d\mid e\mid f,
\qquad
r=e/d,
\qquad
m=r^p.
\]

Write

\[
\chi_{e:d}=\chi_{p;e:d}(n),
\qquad
\chi_{f:e}=\chi_{p;f:e}(n),
\qquad
\chi_{f:d}=\chi_{p;f:d}(n).
\]

Then

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
\mathcal T_{r^p}\bigl(C_{p,e}(n),\chi_{f:e}\bigr).
}
\]

Using T88 gives the fully expanded form

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
Q_{r^p}(\chi_{f:e})
+
\kappa_{r^p}
\bigl(
C_{p,e}(n)\bmod r^p,
\chi_{f:e}\bmod r^p
\bigr).
}
\]

### Proof

Canonical integer projection is path-compatible, so

\[
\mathcal R_{p;f\to d}(n)
=
Q_{r^p}(\mathcal R_{p;f\to e}(n)).
\]

By definition,

\[
\mathcal R_{p;f\to e}(n)
=C_{p,e}(n)+\chi_{f:e}.
\]

Hence

\[
\begin{aligned}
\chi_{f:d}
&=Q_{r^p}(C_{p,e}+\chi_{f:e})-C_{p,d}\\
&=[Q_{r^p}(C_{p,e})-C_{p,d}]\\
&\quad+[Q_{r^p}(C_{p,e}+\chi_{f:e})-Q_{r^p}(C_{p,e})]\\
&=\chi_{e:d}
+\mathcal T_{r^p}(C_{p,e},\chi_{f:e}).
\end{aligned}
\]

Apply T88 for the second form. ∎

### Meaning

Collapse holonomy is **not simply additive**.

When an upper-level path defect is transported downward:

1. every complete block of size `r^p` becomes coarse defect directly;
2. the residual detail contributes an additional unit only if, together with the current coarse-boundary residue, it crosses the next boundary.

The new unified chain is therefore

\[
\boxed{
\text{operation noncommutation}
\to
\text{local holonomy}
\to
\text{precision transport}
\to
\text{carry cocycle}.
}
\]

This closes the loop between the early T11 result and the newer T72/T73 theory.

---

## 5. P018-T91 — When a coarse layer sees none of a fine holonomy

Status: `PROVED`

For `m>=1` and `a,h>=0`, let

\[
u=a\bmod m.
\]

Then

\[
\boxed{
\mathcal T_m(a,h)=0
\iff
u+h<m.
}
\]

Equivalently,

\[
\boxed{
\mathcal T_m(a,h)=0
\iff
h<m-(a\bmod m).
}
\]

### Proof

`Q_m(a+h)=Q_m(a)` exactly when `a+h` remains in the same quotient fiber as `a`. Starting from residue `u`, the next fiber boundary lies `m-u` integer units away. ∎

Finite precision therefore does not shrink every fine difference proportionally into a real-valued error.

A fine path defect either:

- remains entirely inside one coarse fiber and is strictly invisible at that layer; or
- crosses a finite boundary and changes the coarse state by one or more discrete units.

This is an intrinsic **finite-resolution visibility threshold**.

---

## 6. P018-T92 — Exact criterion for strict refinement recovery

Status: `PROVED`

Again let

\[
d\mid e\mid f,
\qquad
m=(e/d)^p.
\]

T12 proves

\[
\mathcal R_{p;e\to d}(n)
\le
\mathcal R_{p;f\to d}(n).
\]

We can now characterize strictness exactly:

\[
\boxed{
\mathcal R_{p;f\to d}(n)
>
\mathcal R_{p;e\to d}(n)
}
\]

if and only if

\[
\boxed{
\chi_{p;f:e}(n)
\ge
m-igl(C_{p,e}(n)\bmod m\bigr).
}
\]

### Proof

The difference between the two recovery states is exactly

\[
\mathcal T_m(C_{p,e},\chi_{f:e}).
\]

By T91 this is positive exactly when

\[
(C_{p,e}\bmod m)+\chi_{f:e}\ge m.
\]

Rearrange. ∎

T12's weak monotonicity is therefore upgraded to an exact **event criterion**:

> Increasing precision changes an already observed coarse recovery state only when the newly generated operation holonomy actually crosses the next coarse fiber boundary.

This exposes a pattern worth comparing with P010's strict history-merger criterion:

- on the time side, history multiplicity strictly increases only when a new collision occurs;
- on the precision side, recovery state strictly increases only when a new boundary crossing occurs.

Only the common event-triggered-monotonicity skeleton is recorded here. **No categorical duality is claimed.**

---

## 7. A minimal nonzero holonomy example

Reuse the T11 example:

\[
n=3,
\quad p=2,
\quad d=1,
\quad e=10.
\]

The coarse path gives

\[
C_{2,1}(3)=1.
\]

The fine path gives

\[
S_{2,10}(3)=17,
\qquad
C_{2,10}(3)=289,
\qquad
289//100=2.
\]

Therefore

\[
\boxed{\chi_{2;10:1}(3)=1.}
\]

It can now be interpreted precisely as

\[
\boxed{
\text{the minimal operation-scheduling holonomy between collapse and projection}=1.
}
\]

This is not a chart disagreement between two scale-only paths. It is a genuine state difference caused by different operation ordering at the same final coarse type.

---

## 8. Further feedback into the foundational logic

Supplement 08 proposed a base consisting of

\[
\text{typed finite states}
+\text{projection/adjunction}
+\text{defect}
+\text{obstruction}
+\text{atlas/coherence}.
\]

This stage adds the missing action layer.

### Layer 4a — Operation-labelled paths

A path records not only scale arrows but also when operations occur.

### Layer 4b — Path holonomy

Two typed operation paths with the same source and target may differ by a nonzero finite state:

\[
H(\gamma_1,\gamma_2)
=\operatorname{out}(\gamma_1)-\operatorname{out}(\gamma_2).
\]

### Layer 4c — Defect transport

A path defect is not a bare number. Under a further change of observation precision, it is transported through

\[
\mathcal T_m(a,h),
\]

and T89 proves transport coherence.

The candidate foundation therefore becomes

\[
\boxed{
\text{states/types}
\to
\text{projections/adjunctions}
\to
\text{operations}
\to
\text{exact defects}
\to
\text{representation obstruction}
\to
\text{atlas}
\to
\text{operation paths + coherent defect transport}.
}
\]

This is more natural than requiring every diagram to commute. Some diagrams may fail to commute, provided that **their noncommutation is itself a finite, explicit, transportable, composable mathematical object**.

---

## 9. Executable pressure tests

Add `src/enterprise_math/precision_holonomy.py` and `tests/test_precision_holonomy.py` to check small finite domains for:

1. T88 defect transport as quotient difference;
2. T88 bulk + carry expansion;
3. T89 two-level transport coherence;
4. T90 collapse-holonomy composition;
5. T91 zero-visibility threshold;
6. T92 strict-recovery criterion.

Computation is used for counterexample search and implementation checking, not as a substitute for proof.

---

## 10. Next open questions

### P018-Q86 — Do multiplication/power defects share the same transport law?

Transport itself depends only on coarse projection and a nonnegative state difference, so it may be more universal than the carry cocycle. Check whether existing multiplication/power naturality defects all embed into the same `T_m(a,h)` framework.

### P018-Q87 — Signed defect transport

When `h` may be positive or negative, one nonnegative `T_m` is no longer enough. Develop a unified signed transport incorporating both carry and borrow, with an explicit composition law.

### P018-Q88 — Operation-path 2-cells

Build a minimal typed 2-cell language for arrows such as project / collapse / add / multiply so that a noncommuting square's defect and T89 transport are proved structures rather than diagrammatic metaphors.

### P018-Q89 — Composition of holonomy across multiple diamonds

Concatenate operation-scheduling diamonds and ask whether total holonomy is completely determined recursively by local holonomies plus canonical transport. If not, identify the smallest missing datum.

### P018-Q90 — Connect to the P017 global-certificate route

Test whether local carry/shell/factor-precision defects in P017 can first be organized as path holonomies and then accumulated through a transported defect budget into a global certificate.

---

## 11. Current conclusion

This stage gives the first strict answer to the T87 question “where can genuinely nonzero path effects come from?”:

\[
\boxed{
\chi_{p;e:d}
=\text{collapse/refinement operation-scheduling holonomy}.
}
\]

Under further coarsening it obeys

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
\mathcal T_{(e/d)^p}(C_{p,e},\chi_{f:e}),
}
\]

where

\[
\boxed{
\mathcal T_m(a,h)
=Q_m(h)+\kappa_m(a\bmod m,h\bmod m).
}
\]

Carry is therefore no longer an isolated arithmetic phenomenon. It becomes the boundary correction that appears when a genuine operation holonomy is transported across precision levels.

The foundational principle worth testing next is now more concrete:

> **Allow noncommutation, but finitely represent it; allow defects, but require canonical defect transport; allow multiple routes, but require their differences to be comparable and composable inside one typed atlas.**