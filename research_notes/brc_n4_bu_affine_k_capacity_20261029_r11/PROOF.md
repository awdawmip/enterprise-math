# BRC N=4 BU: affine-parameter event splice extends the curved capacity minimax region to b=37/250

**2026-10-29. Author-side analytic research, EXACT SYMBOLIC + RATIONAL WITNESSES, UNREVIEWED / NOT_ADMITTED.** This extends the merged result of Enterprise Math PR #1714, which reached `b<=73/500`. Research identity: this scheduled research conversation, GitHub actor `awdawmip` (not an authenticated native Researcher/CLAIM). Freeze: `GLOBAL_KNOWLEDGE_V1 main@137ea2eaed9f1bf446d3e8715bab98a389d70d0c`; Enterprise Math scientific input `main@f646634cd1a6c4f9f659180bf15a743b02871864`.

## Exactly preserved model and inherited results

Use the **external**, strictly-positive, 16-leaf two-probability-law BRC N=4 model, target `F=(a,b,1,0)`, the full terminal joint observer `(T,Decision,Z_BU)` and all lawful real randomized instantaneous causal `S2`/`S23` policies. Neither a different observation nor future/native-X6 operation is included. The author-side 16-leaf-to-four-atom reduction, legal TV event dual inequalities and attaining strategy come from:

- 16-leaf reduction: `1a4898a57e952245eeacb38be7adf109faa49f49`;
- curved capacity region: `d78e2b5729c824918126aec8ffb26ff3e5dc4cb5`;
- newest antecedent, `b<=73/500` via constant `k=9/25`: PR #1714, merge `e16b81cd664f1a1c69cf1447d55c91e6792440dc`.

Write

\[
\alpha(b)=\frac{\sqrt{121b^2+10b+25}-4b}{5},\quad
\delta=\frac{1-a}{3},\quad B_*=b-\delta,\quad
C=\frac{7-a-21b}{4a+12b+2},\quad E=\frac{B_*C}{4},
\]

\[
G=5a^2+8ab-21b^2-2b-5,
\quad L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)},
\quad L_3(u)=\frac{u[a-(a+3b)u]}{2(7-2u)}.
\]

The inherited *measurable terminal-event* TV bounds for every competitor with continuation `u in [0,1]` are

\[
e\ge L_0(u)\quad(0\le u\le3/7),\qquad
e\ge L_3(u)\quad(0\le u\le1),\qquad
e\ge B_*u/4\quad(B_*>0).
\]

Prior proofs establish `L0` decreasing on `[0,3/7]`, `L3` having **no interior minimum** on `[0,1]`, `L3(C)=E` and `E-delta=G/[8(2a+6b+1)]`. The four-atom reduction and these observable-event lemmas remain dependencies requiring independent review; the new conclusion is conditional on their exact source assertions.

## New theorem (continuous parameter domain)

For every real pair

\[
\boxed{0<b\le\frac{37}{250}=0.148,\qquad \alpha(b)\le a\le1,}
\]

the exact global minimax losses over **all lawful real randomized causal strategies** coincide and equal

\[
\boxed{d_2(a,b)=d_{23}(a,b)=E
=\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}.}
\]

The proof's new parameter-adaptive splice is

\[
\boxed{k(a)=\frac a4+\frac{11}{100}}.
\]

This strictly improves the proven upper endpoint from `73/500=0.146` to `37/250=0.148`. The new endpoint is a **sufficient certificate bound**, not a claim about the true minimax phase boundary. No reuse of the already completed `k=9/25` proof is needed.

## Exact analytic proof

Set `a0=9607/10000`, `b1=37/250`. The positive root of `G(a,b)=0` is `alpha(b)`. For fixed `a=a0`, `G(a0,b)` is a concave quadratic in `b`, globally maximized at

\[
b_v=(4a_0-1)/21=2369/17500,
\qquad G(a_0,b_v)=-310557/700000000<0.
\]

As `G_a=10a+8b>0` on the relevant positive quadrant, `alpha(b)>a0` for every `0<b<=b1`. Also `G(1-3b/5,b)=-24b^2<0`, so `alpha(b)>1-3b/5`. It follows that `B_*>4b/5>0`, `E>=delta>=0`, `C<1`. Because `G(1,b)=3b(2-7b)>0` for this b range, the admissible curved region is nonempty.

The function `C` strictly decreases with both `a` and `b`, by the exact derivatives

\[
\partial_a C=-\frac{30-72b}{(4a+12b+2)^2}<0,\qquad
\partial_b C=-\frac{72a+126}{(4a+12b+2)^2}<0.
\]

The splice `k(a)` increases with `a` and satisfies `0<k<=9/25<3/7`. Consequently throughout the rectangle `a0<=a<=1, 0<=b<=b1`,

\[
C-k\ge C(1,b_1)-k(1)=\frac{241}{648}-\frac9{25}=\frac{193}{16200}>0.
\]

**Gap for the L0 certificate.** Direct exact symbolic expansion gives

\[
L_0(k)-E=\frac{N(a,b)}{1200(25a-1139)(2a+6b+1)},
\]

\[
\begin{aligned}
N={}&3750a^4+22500a^3b+51425a^3+33750a^2b^2
+190425a^2b-262274a^2\\
&+108450ab^2-1230594ab+354613a-1061316b^2+2812989b-398650.
\end{aligned}
\]

The denominator is strictly negative for `a<=1`. We prove `N<0` on the *entire larger rational rectangle*. Its derivative has

\[
\partial_b N=3[7500a^3+22500a^2b+63475a^2+72300ab-410198a-707544b+937663]
\ge \frac{158530683}{125}>0,
\]

using `0<=b<=37/250` and `a<=1` and dropping nonnegative terms. At `b=b1`,

\[
\partial_aN=15000a^3+164265a^2-\frac{11667592}{25}a+\frac{218575721}{1250}
\le -\frac{1472447634}{15625}<0,
\]

using `a<=1` for its positive monomials and `a>=a0` for the negative monomial. Thus

\[
N(a,b)\le N(a,b_1)\le N(a_0,b_1)
=-\frac{9702523137476277}{8000000000000}<0.
\]

Therefore `L0(k)>E` throughout the claimed region.

**Gap for the L3 certificate.** Exact symbolic factoring gives

\[
L_3(k)-E=\frac{f_1(a,b)f_2(a,b)}{1200(25a-339)(2a+6b+1)},
\]

\[
f_1=50a^2+150ab+97a+1116b-339,
\quad f_2=75a^2+225ab-317a-951b+350.
\]

The denominator is strictly negative. Here `f1` increases in `a,b`, and `f2` decreases in `a,b` on the rectangle (`f2_a=150a+225b-317<0`; `f2_b=225a-951<0`), so

\[
f_1(a,b)\le f_1(1,b_1)=-579/125<0,
\qquad f_2(a,b)\ge f_2(1,b_1)=69/125>0.
\]

Hence `L3(k)>E`.

**Complete real continuation domain.** Every lawful competitor has some `u∈[0,1]`. For `0<=u<=k`, monotonicity gives `e>=L0(u)>=L0(k)>E`. For `k<=u<=C`, no-interior-minimum of `L3` gives `e>=L3(u)>=min(L3(k),L3(C))=E`. For `C<=u<=1`, the observed capacity-event certificate gives `e>=B_*u/4>=B_*C/4=E`. These three closed intervals cover all real `u`, with no sampling assumption.

**Matching lawful strategy.** Choose

\[
(A,B,u,U,V)=(1,B_*,C,B_*(1+C),B_*).
\]

It is valid: `0<B_*<=b<=37/250`, `0<C<1`, `U<2b<=74/250<1=A`, and `V=B`. Substitution in the full source-labelled four-atom differences gives

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]

Since `0<=delta<=E`, each law's TV equals `E`. The universal lower and lawful upper match, proving the theorem relative to the cited observer/event dependencies. QED.

## Exact new rational witness and executed checking

Take `a=481/500=0.962`, `b=37/250=0.148`; this is outside the prior `b<=73/500` proven strip. Here

\[
G=2561/250000>0,\qquad
C=1465/3812,\qquad
\boxed{\operatorname{TV}_P=\operatorname{TV}_Q=E=59479/4574400}.
\]

The accompanying `VERIFY.py` was actually executed in Python with SymPy and `fractions.Fraction`, passing **25 exact symbolic identities** (including signed-atom equalities and all decisive rational bounds), reconstructing all **16 strictly positive P/Q leaves** with both laws normalized, and checking **five rational parameter strategies under both full observation laws**. Exact stdout is `VERIFY_EVIDENCE.txt`. The script is algebraic validation and finite exact witnesses, not a substitute for the real-parameter inequality proof or independent scientific review.

## Authority, provenance, open problems

At the recorded read snapshot, the authenticated GitHub identity was `awdawmip`; native Site reported `research_authority_granted=false`. Its actual bounded owner query returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`; thus active task Owner/CLAIM could not be authenticated. This work is ordinary *author-side portable mathematics*, not a formal task mutation, native activity, Result, review, or Foundation admission. No native credentials or privileged session were used.

The theorem is internal to this **external finite BRC two-law observer model**. It does not establish a faithful embedding into P000 native six-dimensional Cell relations, three-dimensional slice, independent time, extra AU provenance, or future operations. The P000 and ACTIVE worldview were read and remain unchanged.

Next discriminator: push the adaptive splice beyond `b=37/250`; the present affine k(a) loses a uniform L3 gap near a=1 and L0 gap near the lower `alpha(b)` boundary around `b=149/1000`. Study a `k(a,b)` based on exact dual feasible intervals or find an exact rational P/Q 16-leaf competing strategy with both TVs < E. See NEXT_TASK.md.
