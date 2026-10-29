# BRC N=4 BU: linear event-TV splice solves the full curved capacity strip up to b=3/20

**2026-10-30 · AUTHOR_ANALYTIC_PROOF / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.** This is a theorem inside the declared *external* strictly positive 16-leaf two-law finite model, not a native P000 X6 theorem. The 16-leaf-to-four-observable-atom causal reduction and lawful measurable event-TV lower bounds are inherited author-side results pending independent audit.

## Immutable source and novelty

GLOBAL_KNOWLEDGE_V1 snapshot: main@b5a4c88d7e9d5040ad4ab233b023720ea9b3070a; the P000 startup projection's canonical blob agrees with the actual V4 P000 original (770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc). Enterprise Math scientific input: main@03f29e14430084acec49ed472622fea120082c13. Previous exact continuum range: 0<b<=37/250=0.148, alpha(b)<=a<=1, from the author-side affine-splice proof (PR #1716; 8eba97da029cd4ef90feaecd34f6f4dd1f1da409). We improve b to 3/20=0.15 by constructing a **different parameter-adaptive linear k(a)**, while proving a new exact failure of the single-splice certificate at one rational point b=0.152.

Original 16-leaf reduction: 1a4898a57e952245eeacb38be7adf109faa49f49. Original observable event-TV duals: d78e2b5729c824918126aec8ffb26ff3e5dc4cb5. Target policy F=(a,b,1,0); terminal observer retains all of (T,Decision,Z_BU), P/Q full joint laws, and all legal real randomized instantaneous causal S2/S23 strategies. No compressed AU observer, future operation, primitive 3D plane, P000 physical time or native X6 correspondence is assumed.

## Theorem: a two-parameter continuous real region

Let

\[
\alpha(b)=\frac{\sqrt{121b^2+10b+25}-4b}{5},\quad
\delta=\frac{1-a}{3},\quad B_*=b-\delta,\quad
C=\frac{7-a-21b}{4a+12b+2},
\]
\[
E=\frac{B_*C}{4}
 =\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}.
\]

**For every real 0<b<=3/20 and alpha(b)<=a<=1**, the exact global minimax errors for all legal real randomized causal competitors coincide:

\[
\boxed{d_2(a,b)=d_{23}(a,b)=E(a,b).}
\]

The key new uniform splice is

\[
\boxed{k(a)=3a/5-59/250.}
\]

This region is a proved sufficient parameter domain for a valid dual-primal match, not an asserted sharp phase boundary.

## Allowed lower bounds, capacities, and domain

For an arbitrary competitor's continuation 0<=u<=1 and worst two-law TV e, the previously derived **source-preserving observable event** inequalities are

\[
e\ge L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)}
\quad(0\le u\le3/7),
\]
\[
e\ge L_3(u)=\frac{u[a-(a+3b)u]}{2(7-2u)}
\quad(0\le u\le1),\qquad
e\ge B_*u/4\quad(B_*>0).
\]

Reused exact lemmas (with the same model/observer): L0 is decreasing on [0,3/7], L3 has no interior minimum on [0,1], L3(C)=E, and

\[
G(a,b)=5a^2+8ab-21b^2-2b-5,\qquad
E-\delta=\frac{G}{8(2a+6b+1)}.
\]

alpha(b) is the positive root G=0. Let a0=9607/10000 and b1=3/20. Since G_a=10a+8b>0, and the concave function G(a0,b) has exact global maximum -310557/700000000<0 at b=(4a0-1)/21, every a>=alpha(b) exceeds a0. Also G(1-3b/5,b)=-24b^2<0; hence a>1-3b/5 and B_*>4b/5>0. The requirement a>=alpha(b) gives G>=0 and 0<=delta<=E. The numerator of C is >=57/20>0; C<1 follows from 5a+33b>5. Exact derivatives

\[
C_a=-(30-72b)/(4a+12b+2)^2<0,\qquad
C_b=-(72a+126)/(4a+12b+2)^2<0
\]

show C decreases with a,b. Meanwhile k rises with a and

\[
17021/50000\le k\le 91/250<3/7,\quad
C-k\ge C(1,3/20)-k(1)
=19/52-91/250=9/6500>0.
\]

Thus the three intervals [0,k], [k,C], [C,1] cover *every* legal real continuation.

## L0(k)>E by an exact polynomial sign certificate

Exact common-denominator elimination gives

\[
L_0(k)-E=\frac{N(a,b)}{6000(25a-489)(2a+6b+1)}
\]

where

\[
\begin{aligned}
N={}&45000a^4+270000a^3b+218350a^3
+405000a^2b^2+680100a^2b-658988a^2\\
&+75150ab^2-3223328ab+730981a
-2389092b^2+6019943b-855750.
\end{aligned}
\]

On the *larger rational rectangle* a0<=a<=1 and 0<=b<=3/20,

\[
N_b=270000a^3+810000a^2b+680100a^2+
150300ab-3223328a-4778184b+6019943
\]
\[
N_b\ge6019943-3223328-4778184(3/20)
=10399437/5>0.
\]

At b1=3/20,

\[
N_a(a,b_1)=
\frac{7200000a^3+31062000a^2-43828840a+9966907}{40}
\]
\[
N_a(a,b_1)\ge
\frac{7200000a_0^3+31062000a_0^2-43828840+9966907}{40}
=\frac{744132939681}{25000000}>0.
\]

Consequently N(a,b)<=N(a,b1)<=N(1,b1)=-270189/200<0. The displayed denominator is negative (25a-489<0), so **L0(k)>E** throughout the curved domain.

## L3(k)>E by factor signs

The other exact symbolic factorization is

\[
L_3(k)-E=
\frac{f_1(a,b)f_2(a,b)}
{6000(75a-467)(2a+6b+1)}
\]

where

\[
f_1=300a^2+900ab+157a+2271b-934,\quad
f_2=450a^2+1350ab-1052a-3156b+875.
\]

f1 increases in a and b, so f1(a,b)<=f1(1,3/20)=-27/20<0. Since (f2)_b=1350a-3156<0 for a<=1, f2(a,b)>=f2(a,3/20). On that upper edge (f2)_a=900a-1699/2>=1513/100>0 for a>=a0; therefore f2(a,b)>=f2(a0,3/20)=1620741/2000000>0. The denominator is negative (75a-467<0); hence **L3(k)>E**.

## All-real lower bound and exact lawful attainment

For u<=k: e>=L0(u)>=L0(k)>E. For k<=u<=C: no-interior-minimum L3 gives e>=L3(u)>=min[L3(k),L3(C)]=E. For u>=C: e>=B_*u/4>=B_*C/4=E.

An actually legal matching policy is (A,B,u,U,V)=(1,B_*,C,B_*(1+C),B_*). Indeed 0<B_*<=b<=3/20, 0<C<1, V=B, and U<2b<=3/10<1=A. Its four signed source-marked observable atom differences under the FULL joint observer are

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]

Since 0<=delta<=E, *both* law TVs equal E. The universal lower and lawful upper bounds match. QED, subject to the explicitly referenced causal-reduction/event-inequality dependencies.

## Exact new witness and rigorous method obstruction

At a=481/500, b=3/20, G=57/6250>0, C=361/956 and both full P and Q law TVs of the legal policy are exactly **37183/2868000**. This is outside the predecessor b<=37/250 domain. The actually executed SymPy/Fraction VERIFY.py checks **35 exact identities** and **7 reconstructed strictly positive 16-leaf rational two-law TV cases**; the stdout file records the checks. Finite exact checks are algebraic corroboration, not the all-real proof.

A distinct *limitation of this single-splice certificate*, NOT a minimax counterexample, is proved at

\[
a=481/500,\quad b=19/125=0.152,\quad
G=1957/250000>0,\quad C=1423/3836,\quad q=17/50.
\]

Here direct exact evaluation yields

\[
L_0(q)-E=-1201/26971875<0,\qquad
L_3(q)-E=-38597/2841037500<0.
\]

For these a,b, the derivative of L3 has the positive denominator 2(2u-7)^2 and numerator R(u)=a(2u²-14u+7)+b(6u²-42u). On [0,q], R decreases but R(q)=195101/625000>0, so L3 is increasing. For *any* proposed single splice k in [0,3/7], either k<=q and L3(k)<=L3(q)<E, or k>=q and L0(k)<=L0(q)<E. Thus **no single k can have both L0(k)>=E and L3(k)>=E** at this exact rational pair. Other lawful event duals, multi-splice certificates, and true minimax optimality remain unclassified there; never equate certificate failure with a strategy phase change.

## Source, authority, exact limits, next action

Authenticated GitHub actor awdawmip. Native Site reported research_authority_granted=false, owner not authenticated; no CLAIM, native Result, independent Driver review or admission. These are author-side portable proof files, not formal Source research-state writes. P000, ACTIVE worldview, native signed six-axis Cell, native 3D slice, discrete rotation and independent time/future observer-fidelity duties remain unchanged, unproved by the external BU model.

Next smallest discriminator: at a=481/500,b=19/125 find a **new valid measurable joint-event TV dual** or multi-location certificate proving E, or a legal rational strategy with BOTH complete 16-leaf P and Q TVs below E=297407/23016000. Precisely distinguish genuine minimax switch from the present strict single-splice dual obstruction. See NEXT_TASK.md.
