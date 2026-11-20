# Stage336-B — exact Pareto exclusion of the entire public `r3=0` stratum, with a quantitative `r0=0` subarc descent

**Date:** 2026-10-31 (Asia/Shanghai). **Scientific status:** `PORTABLE_AUTHOR_THEOREM / EXACT_RATIONAL_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Fixed provenance, admissible meaning

- Frozen GLOBAL_KNOWLEDGE_V1 canonical `main@dcffdd3270d839d765c7cab630a66c20afc926c5`, including `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md`, TASK_RESEARCH role, P000 router, ACTIVE `我眼中的世界.md`, math/code/BRC policies.
- Frozen Enterprise Math canonical `main@fd980113f72132edbc47ee27efadf15dd118441c`, including `p000_reality_foundation.json` **original blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`** (read in full because the global startup projection's original-blob pin differed), native Heartbeat World/observer preservation constraints, and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
- Scientific predecessor: Stage335-B complete proof and code at immutable `enterprise-math@c06a779d4bcf3faa2c3e69b0ddba5c66a3c0bd7e`, existing Draft PR #1736. Stage334-B sign-chamber argument is contextual; the new `r3=0` theorem below is proved directly from the exact model and does **not** assume any earlier numerical sign-census theorem.
- Live research service v0.6.11 reported `research_authority_granted=false`. The current owner list query returned `CONTROL_QUOTA`; no Source CLAIM, Result or Driver acceptance is asserted. The currently exposed write scope is a researcher-authored **portable** mathematical manuscript, not a role-bound checkpoint.

This is a theorem **inside a source-labelled, three-visit Bernoulli/BRC auxiliary probability observer**. We keep both source groups, binomial-word multiplicities and all 16 tagged comparisons. Exact rational/symbolic computations here concern this auxiliary observer and make no native X6 physical update or native residual attribution. No lossless observer/future-operation correspondence to P000, the six native spatial axes, a native three-dimensional slice, triadic closure, independent time, or six-field Cell addresses has been established.

## Definitions

For `k=0,1,2,3`, let

\[
B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
b(x,y)=\frac5{32}\sum_{k=0}^{3}w_k|r_k(x,y)|.
\]

Define the **tag-preserving** distance and cost

\[
D_3(a,z)=\frac12\sum_{k=0}^{3}w_k|B_k(a)-B_k(z)|,
\]
\[
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

For two labelled source groups `(q1,q2)`, the original objective pair is

\[
P=b(q_1)+b(q_2),\qquad T=\frac{33}{1024}+c(q_1)+c(q_2).
\]

The public residuals satisfy the exact word-multiplicity identity

\[
\sum_{k=0}^3w_kr_k=0.
\]

Write `R=[21/100,6/25] × [1/2,2/3]` and `Z_3={q∈R:r3(q)=0}`.

## Theorem A — complete `r3=0` stratum exclusion in R

**For every real** `q=(x,y)∈Z_3`, there exists `q'∈R`, arbitrarily close to `q`, such that

\[
\boxed{b(q')<b(q)\quad\text{and}\quad c(q')<c(q).}
\]

Consequently, no point in `Z_3` can be a Pareto optimum of the **full single-source auxiliary** problem, nor can any two-group candidate containing a source in `Z_3` be Pareto optimal for `(P,T)` (hold the other source fixed). This conclusion is **not** limited to a finite grid, to the Stage335-B smaller rectangle, or to one of the two sides of a tag cusp. It claims nothing about `r3=0` points outside `R`.

### Step A1: the entire r3-zero graph and signs

The equation `r3=0` is exactly

\[
4x^3+y^3=9/32.
\]

For every `x∈[21/100,6/25]`, there is a unique positive root `y=Y_3(x)`. Direct rational endpoint signs give

\[
r_3(21/100,5/8)=-523/40000000<0,
\quad r_3(21/100,63/100)=5841/5000000>0,
\]
\[
r_3(6/25,609/1000)=-87471/5000000000<0,
\quad r_3(6/25,61/100)=1027/5000000>0.
\]

As `Y3'(x)=-4x²/Y3(x)²<0`, it follows that

\[
609/1000<Y_3(x)<63/100,\qquad x<Y_3(x).
\]

On that curve,

\[
\frac{d}{dx}r_1(x,Y_3(x))=r_{1,x}+r_{1,y}Y_3'(x)>0
\]

because `r1,x=(4/5)(1-x)(1-3x)>0` and `r1,y=(1/5)(1-y)(1-3y)<0`. Its maximum satisfies

\[
r_1(x,Y_3(x))\le r_1(6/25,Y_3(6/25))<r_1(6/25,609/1000)
=-8649471/5000000000<0.
\]

Likewise, substituting `Y3'` into the `B2` derivative yields the **exact identity**

\[
\frac{d}{dx}r_2(x,Y_3(x))=\frac85x\Bigl(1-\frac{x}{Y_3(x)}\Bigr)>0.
\]

At the left endpoint `Y3(21/100)>5/8`, and `r2` increases with `y<2/3`. Thus

\[
r_2(x,Y_3(x))>r_2(21/100,5/8)=36723/40000000>0.
\]

So **every** point on the entire curve has `r1<0`, `r2>0`, `r3=0`, and only the sign of `r0` remains to classify.

### Step A2: all labelled cost derivatives retain the 16 comparison signs

On `x∈[21/100,6/25]`, the signs of `B_k(1/4)-B_k(x)` and `B_k(3/4)-B_k(x)` are, respectively, `-+++` and `--++`. On `y∈(609/1000,63/100)`, the signs of `B_k(1/4)-B_k(y)` and `B_k(3/4)-B_k(y)` are, respectively, `++--` and `---+`. These are consequences of the exact polynomials' monotonic intervals and endpoint comparisons, not numerical sampling. In particular `B_2(609/1000)>B_2(3/4)`.

Differentiating the **full** `63+1+9+7` weighted, labelled distance, with `w=(1,3,3,1)`, gives

\[
\boxed{c_x=-\frac{(1-x)(189-183x)}{256}<0,\qquad
c_y=\frac{3y(18-25y)}{256}>0.}
\]

This is valid throughout the relevant curve neighbourhood because `y>609/1000>y_\dagger=(1+\sqrt{13})/8` and `y<63/100<18/25`. Thus increasing `x` or decreasing `y` locally **strictly decreases** the tagged audit cost. The source labels have not been collapsed.

### Step A3: unique public r0/r3 double zero

Along the `r3=0` curve, direct differentiation yields

\[
\frac{d}{dx}r_0(x,Y_3(x))=-\frac{12}{5}\frac{(Y_3(x)-x)(x+Y_3(x)-2xY_3(x))}{Y_3(x)^2}<0.
\]

At `x_L=113/500`, exact checks show `617/1000<Y3(x_L)<618/1000` and `r0(x_L,618/1000)=529033/625000000>0`. At `x_H=227/1000`, `616/1000<Y3(x_H)<617/1000` and `r0(x_H,616/1000)=-516807/1250000000<0`. By strict monotonicity, there is exactly one double-zero `q*=(x*,y*)` with

\[
\boxed{113/500<x_*<227/1000,\quad 616/1000<y_*<618/1000,\quad r_0(q_*)=r_3(q_*)=0.}
\]

### Step A4: strict dominance in all three exhaustive cases

If `x<x*`, then `r0>0`. Increase `x` by a sufficiently small positive `h` while keeping `y` fixed. Nearby, `r0>0, r1<0, r2>0, r3>0`; weighted conservation gives `b=-(15/16)r1`. Since `r1,x>0` and `c_x<0`, **both** `b` and `c` decrease strictly.

If `x>x*`, then `r0<0`. Decrease `y` by a sufficiently small `h>0` while keeping `x` fixed. Nearby, `r0<0, r1<0, r2>0, r3<0`; weighted conservation gives `b=(15/16)r2`. Because `r2,y=y(2-3y)/5>0` and `c_y>0`, both `b` and `c` decrease strictly when `y` decreases.

If `x=x*`, both `r0` and `r3` vanish. The implicit-function theorem for `r0=0`, since `r0,y=-(3/5)(1-y)^2<0`, supplies a local graph `y=Y0(x)` with

\[
Y_0'(x)=-4\frac{(1-x)^2}{(1-y)^2}<0.
\]

An infinitesimal increase of `x` along this graph decreases `y`, strictly decreases `c`, and makes `r3<0` since

\[
\frac{d}{dx}r_3(x,Y_0(x))=\frac{12}{5}\frac{(x-y)(x+y-2xy)}{(1-y)^2}<0.
\]

Define `f(t)=t(2-3t)/(1-t)^2`. Differentiation gives

\[
\frac{d}{dx}r_2(x,Y_0(x))=\frac45(1-x)^2\,[f(x)-f(y)],\qquad
f'(t)=\frac{2(2t-1)}{(t-1)^3}.
\]

For `x∈[113/500,227/1000]`, `y∈[61/100,63/100]`, `f(x)≤f(227/1000)=299413/597529 < 693/1369=f(63/100)≤f(y)`. Hence `r2` decreases strictly along that graph near `q*`. With `r0=0,r1<0,r2>0,r3<0` after the move, `b=(15/16)r2` decreases too. This covers the double-zero without discarding any absolute-value boundary.

Together the three cases prove the universal theorem.

## Theorem B — quantitative descent on a nontrivial r0-zero subarc

For every real

\[
q=(x,y)\in [21/100,6/25]\times(1/2,5/8]
\]

satisfying `r0(q)=0`, `r1(q)<0`, and `r3(q)≤0`, there is an arbitrarily close point `q'` on the **same** `r0=0` curve with `b(q')<b(q)` and `c(q')<c(q)`. Moreover, along a sufficiently short rightward parameter interval maintaining the strict residual signs, the derivatives satisfy

\[
\boxed{\frac{d}{dx}b(x,Y_0(x))<-\frac{77}{7500},\qquad
\frac{d}{dx}c(x,Y_0(x))<-\frac{68913}{160000}}
\]

at smooth tagged points; the same strict integrated bounds hold across the single tagged cusp by piecewise integration.

**Proof.** The identity `r0=0` gives `Y0'<0`, while the displayed derivative of `r3` along `Y0` is negative because `x<y`. The mass identity and `r1<0,r3≤0` force `r2>0`. The condition excludes `x=6/25` because `r0(6/25,1/2)<0` and `r0` decreases in `y`. Choose a sufficiently small increase of `x`, keeping `y>1/2`, `r1<0`, `r2>0`, and now `r3<0`.

`f` is increasing on `(0,1/2)` and decreasing on `(1/2,1)`; thus

\[
f(y)\ge f(5/8)=5/9>192/361=f(6/25)\ge f(x),
\quad f(y)-f(x)\ge 77/3249.
\]

As `(1-x)^2≥(19/25)^2=361/625`, the displayed exact derivative identity implies

\[
\frac{d}{dx}b=\frac{15}{16}\frac{d}{dx}r_2
=\frac34(1-x)^2[f(x)-f(y)]\le-77/7500,
\]

and strict inequality holds because the bounds cannot be attained simultaneously on this subarc. For the tagged cost, the same 16 comparison signs give `c_x=-p(x)` with `p(x)≥p(6/25)=68913/160000`; on `1/2<y≤5/8`, `c_y>0` on both sides of `y_\dagger=(1+\sqrt{13})/8`, with the two exact formulas

\[
c_y=3y(1-y)/64\ (y<y_\dagger),\quad
c_y=3y(18-25y)/256\ (y>y_\dagger).
\]

Since `Y0'<0`, `d c(x,Y0(x))/dx=c_x+c_yY0'<-68913/160000` wherever differentiable, and integrating across the algebraic cusp preserves the bound. The strict decreases finish the proof.

The double-zero in Theorem A lies on this subarc (`y*∈(0.616,0.618)`), giving a second, quantitative proof of its exclusion.

## Validation certificate and limits

`REPRO_STAGE336B.py` uses Python `Fraction` and SymPy exact polynomial simplification. It checks conservation, all word derivatives, all 16 tagged sign patterns and resulting gradient formulas, the rational endpoint root brackets, the `r0/r3` crossing, the two implicit derivative identities, and both exact descent margins. It ran twice with byte-identical stdout; the logged result ends:

`STAGE336B_R0_R3_COMPLETE_ZERO_STRATUM_EXCLUSION_EXACT_PASS`.

**Proof coverage:** all real points of the specified `r3=0` stratum in `R`, and all points of the stated `r0=0` subarc. Continuous quantifiers follow from the analytic monotonicity, implicit derivative, exact rational inequalities and absolute-value sign analysis above; they do not follow from checking finitely many points. SymPy algebra checking is author verification, not formal or independent theorem admission.

**Conditional project-wide use:** Stage332-B's author-proved low-error enclosure `b≤61/10000 => q∈R`, if independently validated, combines with Theorem A to remove the entire `r3=0` stratum from the low-error two-source Pareto search. This paper does not re-prove that enclosure. The currently unreviewed Stage335-B `r1=0` rectangular uniqueness theorem remains a complementary candidate result. No assertion about the first *global* eight-parameter optimum transition or about native P000 physics follows yet.

## Exact next question

Stage337-B should classify the **remaining** `r0=0` arcs with `r1≥0` or `r3>0`, and the `r1=0` arc including intersections with `r0=0` and the tagged cusp. Test their one-sided KKT/dominance inequalities against the surviving `-+-` interior. Then construct a verified outside-R exclusion or an explicit earlier two-source competing point. Keep 16 tags and multiplicities, distinguish a branch-restricted optimum from global Pareto, and require a separate lossless P000/X6/BRC/native observer bridge before native physical attribution.
