# All-round single residual-growth episode in the auxiliary four-label BRC observer

**Author-side proof, 2026-10-23. UNREVIEWED / NOT ADMITTED / NOT NATIVE X6.** This is a theorem inside an explicitly specified positive-mass auxiliary observer, not a theorem of the locked P000 native six-dimensional Cell dynamics. The new proof step is the all-round zero-action single-crossing inequality. The one-episode result combines it with two earlier author-side laws, whose load-bearing algebra is also reproduced here.

## Exact model

Independent hidden-label draws in successive public actions 0 or 2 use respectively

\[
q_0=(0,1+z,1-z,1)/3,\quad q_2=(1,1,0,1)/3,\quad z\in[0,1].
\]

Let the set of labels ever seen by round t be \(D_t\). The good **exact** occupancy sets are \(\{0,1\},\{1,2\},\{1,3\},\{2,3\}\). Let \(\delta_t=\Pr(D_t\text{ is good})\), with \(\delta_0=\delta_1=0\); define \(\Delta_t=\delta_t-\delta_{t-1}\), \(M_t=\max_{0\le s\le t}\delta_s\), and \(R_t=\sum_{j=2}^t[\Delta_j]_+-M_t\). A strict residual-growth episode is a maximal consecutive set of t with \(R_t>R_{t-1}\). We ask whether a word over \(\{0,2\}\) can have two separated such episodes.

For a prefix with a copies of action 2 and b copies of action 0, the probability \(\delta_{a+b}=N(a,b;z)/3^{a+b}\) obeys:

\[
\begin{aligned}
N(0,b)&=2^b+(2+z)^b+(2-z)^b-2(1+z)^b-2(1-z)^b-2 && (b\ge1),\\
N(a,0)&=2^{a+1}-4 &&(a\ge1),\\
N(a,b)&=(2^a-3)(1+z)^b+2^a(2+z)^b+2^b+(2-z)^b-2 &&(a,b\ge1).
\end{aligned}
\]

These follow by summing, over good pairs \(\{i,j\}\), the probability of occupying exactly the pair:
\(\prod_{r}(q_{r,i}+q_{r,j})-\prod_r q_{r,i}-\prod_rq_{r,j}\). Independent 16-mask rational dynamic programming checks these count formulas. The one-time \(\delta_n\) depends on counts, but \(R_n\) retains prefix history and cannot be reduced to counts alone.

## Lemma A (NEW): zero-action increment contraction

Write \(d_n(z)=\delta_n(0^n;z)\), \(E_n=3^n(d_n-d_{n-1})\) for \(n\ge2\), and set \(r=1+z,s=1-z,u=1+r=2+z,v=1+s=2-z\). Then

\[
E_n=4-2^{n-1}-s u^{n-1}-r v^{n-1}+2v r^{n-1}+2u s^{n-1}.
\]

For every real \(z\in[0,1]\) and integer \(n\ge2\):

\[
\boxed{E_{n+1}-2E_n\le-4+2z^2\le-2.}
\]

**Proof.** With \(m=n-1\ge1\), a direct exact subtraction gives

\[
E_{n+1}-2E_n=-4+z(rv^m-su^m)-2vsr^m-2urs^m.
\]

For \(H_m=rv^m-su^m\),

\[
H_{m+1}-H_m=rs(v^m-u^m)\le0,\qquad
H_m\le H_1=r(1+s)-s(1+r)=r-s=2z.
\]

The last two terms in the exact subtraction are nonpositive; the claimed bound follows. Also \(E_2=6-2z^2>0\), while the bound forces \(E_{n+1}<0\) whenever \(E_n\le0\). Hence the zero-action occupancy probability has no negative-to-positive increment transition. For \(z<1\), its three available hidden labels each have positive mass and exactly-two-label occupancy tends to 0, so an eventual negative increment exists; for \(z=1\), \(d_n=1-(2/3)^n-(1/3)^n\) rises strictly. Therefore zero-action occupancy is unimodal (allowing one flat step), and

\[
\boxed{R_n(0^n;z)=0\quad\text{for all }n,z.}
\]

## Lemma B: one-2 suffix positive increments cannot return

After exactly one action 2 has occurred, appending action 0 gives, for length \(n\ge3\), the occupancy increment \(Z_n/3^n\), where

\[
Z_n=4-2^{n-2}-2(1-z)(2+z)^{n-2}-(1+z)(2-z)^{n-2}+(2-z)(1+z)^{n-2}.
\]

Writing \(m=n-2\ge1\), direct algebra yields

\[
Z_n-Z_{n+1}=2^m+(1-z^2)\left[2(2+z)^m+(2-z)^m\right]-z(2-z)(1+z)^m.
\]

For \(z<1\), \(z(2-z)(1+z)^m<2^m\), so \(Z_{n+1}<Z_n\); at \(z=1\), \(Z_n=2\) for all \(n\ge3\). Thus these positive suffix increments, if present, form one initial consecutive block, never return after turning nonpositive. The lone exceptional length-2 prefix 20 has \(\delta_2(20)=5/9>0\); it also cannot create a separated positive block.

## Lemma C: second action 2 absorbs all future residual growth

For prior counts \(a,b\ge1\), appending 0 has increment numerator

\[
F_0=(3-2^a)(2-z)(1+z)^b-2^a(1-z)(2+z)^b-2^b-(1+z)(2-z)^b+4.
\]

If \(a\ge2\), then \((2-z)(1+z)^b\ge2\), \((1+z)(2-z)^b\ge2\), \(2^b\ge2\), whence \(F_0\le-2\). Appending 2 has numerator

\[
F_2=(6-2^a)(1+z)^b-2^a(2+z)^b-2^{b+1}-2(2-z)^b+4.
\]

If \(a\ge2\), its first two terms are at most \(-2(1+z)^b\), giving \(F_2\le-4\). If \(a=1,b\ge2\), convexity \((2+z)^b+(2-z)^b\ge2^{b+1}\) gives \(F_2\le4-2^{b+1}<0\). When \(b=0,a\ge3\), appending 2 yields \(8-2^{a+1}<0\); appending 0 yields \(2^a(2z-3)+11-4z\le7-2^a<0\). Therefore any length \(n\ge4\) prefix containing at least two action-2 symbols has \(\Delta_n<0\).

At lengths 2 and 3 the exceptional words are 22, 220, 202, 022 and 222. Word 22 has \(\delta_2=4/9=M_2\). At round 3, increments for 220, 202, 022 and 222 are, respectively, \((4z-1)/27\), \(4(z-1)/27\), \(4(z-1)/27\) and 0. For 220 a positive increment raises the running maximum by the same amount; the other exceptions have nonpositive increments. Consequently **the second 2 and all later rounds contribute zero to \(R\)**. This lemma agrees with the earlier author note pinned at e371b5bd3d6134769b352dbf9b3b03a335658e9a.

## Theorem (NEW combined all-word result)

For every finite public action word \(p\in\{0,2\}^n\) and every \(z\in[0,1]\), the strict residual growth-time set

\[
G(p,z)=\{t\in\{2,\ldots,n\}:R_t(p_{1:t};z)>R_{t-1}(p_{1:t-1};z)\}
\]

is either empty or **one interval of consecutive integers**. In particular a **second separated strict residual-growth episode is impossible at any word length in this four-label auxiliary model**.

**Proof.** The exact residual definition implies, setting \(h_{t-1}=M_{t-1}-\delta_{t-1}\ge0\),

\[
\boxed{R_t-R_{t-1}=\min\{[\Delta_t]_+,h_{t-1}\}.}
\]

Within a block of positive \(\Delta_t\), \(h_t=\max(0,h_{t-1}-\Delta_t)\); hence its strictly positive \(R\)-increments form an initial part of that block, and can never resume after first reaching zero there. Before the first 2, Lemma A gives \(R=0\). After the first 2, Lemma B ensures at most one positive \(\Delta\)-block (the first-2 step is a single possible boundary, and 20 is a positive length-2 exception). By the displayed identity, the positive residual increments during this phase form at most one consecutive interval. Lemma C excludes residual increments from the second 2 onward, including all small-round exceptions. Thus \(G(p,z)\) is empty or one consecutive interval. QED.

## Scope, exact checks, and continuation

Finite verification in the companion independent checker uses Python standard-library exact Fraction arithmetic. It checks the zero-action inequality and closed numerator identity at 1,027 rational cases, post-first-2 sign order at 1,014, 6,630 independent 16-state occupied-mask crosschecks, and all 53,222 binary words of lengths 1 through 11 at 13 rational parameter values (673 cases have nonempty residual growth, all one interval). Those checks are *not* the proof of the infinite theorem; the above symbolic argument is.

This closes the **second separated growth episode** question **inside the stated auxiliary observer only**. It does not close native X6 dynamics, any different BRC label/branch carrier, or the user-selected P000 worldview; the full native-state/readout/future-operation observer-preservation bridge is still unproved. No mathematical review, working truth or Foundation promotion follows from GitHub storage.

**Next discriminating problem:** find a smallest typed extension of the occupied-label observer admitting two separated positive-residual episodes, or give a precise P000 X6 restricted-state embedding, its full hidden-relation readout and a future-operation preservation theorem. Do not assume either outcome.

**Provenance:** GLOBAL_KNOWLEDGE_V1 main@bf441dbd96e3aff7f1df531c6569d56fa048a10b; Enterprise Math selection-time main@d20e28116f8a9a1df78f5641d70f72e797a4856d; earlier auxiliary two-2 proof @e371b5bd3d6134769b352dbf9b3b03a335658e9a. Current Source identity/CLAIM: not verified (control quota; static read-only service rejected session start with operation_sent=false). Role status: direct unreviewed author-side evidence only.
