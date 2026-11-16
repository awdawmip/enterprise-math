# PREFIX-834 — Exact source-count threshold for one-frame Q re-aliasing at every late time

**Date:** 2026-11-16. **Research status:** AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen science:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
**Antecedents:** PREFIX-832 all-time histogram difference formula, PREFIX-833 first-difference and full-collision criterion. This is a positive, unnormalized, named-source auxiliary BRC count system and **not** a native X6 time/Cell/Link/Port authorization claim.

## Precise question and model

Let p=q initial distinct *named* unmarked sources fill capacity p; their individual **positive integer** removal weights form a multiset A (or B). Initially the marked source is absent. A single Q=R+A step sums all legal weighted transitions: removing any available unmarked source with its fixed weight, removing the marked source with b>0, and inserting that source (if absent and there is room) with a>0. The observer Y(t) is the entire unnormalized integer histogram of occupancy 0,...,p after t Q steps. Both profiles use the same a,b,p. For two distinct weight multisets define Δ_j=e_j(A)-e_j(B), Δ_0=0 and Δ_{p+1}=0. Define n=min{j≥1:Δ_j≠0}. A **positive-time re-aliasing at T** means Y^A(T)=Y^B(T), with some Y^A(t)≠Y^B(t) for 1≤t<T.

## Theorem 834.1 — Exact minimum source count, all T≥3, one fixed Q operator

Fix a=1 and b=2, for all constructions and all time targets. For **every integer T≥3**, there are two different positive-integer weight profiles with full histograms equal again at precisely t=T after having separated. The smallest possible number of initial unmarked sources is

\[
\boxed{p_{\min}^{\rm re-alias}(T)=
\begin{cases}2,&T\ge3\text{ odd},\\3,&T\ge4\text{ even}.
\end{cases}}
\]

For any positive a,b (even if they may be chosen per instance) no re-aliasing after a previous positive-time separation is possible at T=1 or T=2. Hence three initial named sources suffice to cover **both parities** for a single fixed operator, while two suffice for all odd T and are impossible for any even T.

### Explicit 2-source odd-time construction (PREFIX-833, reused)

For T odd, T≥3, p=2:
\[
A=(1,2T+1),\qquad B=(2,T+1).
\]
Here (Δ_1,Δ_2)=(T-1,-1). Theorem 833.3 proves equality exactly at t=0,T; in particular all other positive times are distinct. The maximum weight is 2T+1.

### NEW 3-source even-time construction

For every even T≥4, set L=3T-2, p=q=3:
\[
\boxed{A_T=(1,4,L),\qquad B_T=(2,2,L+1).}
\]
The elementary symmetric differences are
\[
(\Delta_1,\Delta_2,\Delta_3)=(0,L-4,-4)=(0,3(T-2),-4).
\]
Thus the first separation time is n=2 and is nonzero: ΔY_{1}(2)=2!\Delta_2=6(T-2).
For even T the full-collision test of Theorem 833.2 has **only** k=2 (since p=3), and reads
\[
2b\Delta_2+3(T-2)\Delta_3
=4\cdot3(T-2)-12(T-2)=0.
\]
Consequently **every** occupancy histogram coordinate matches at step T. The first-index separation theorem (PREFIX-833.1) ensures no other time t≥2 can match, because the only potential even-parity zero is t=T and all odd-parity t≥3 have a forced nonzero witness. Time t=1 matches because Δ_1=0. The full equality-time set is exactly {0,1,T}. The largest source weight is L+1=3T-1, linear in T. The same fixed operator a=1,b=2 works for all even T.

### NEW 3-source odd-time construction (same capacity p=q=3)

For every odd T≥3, let K=4T-1 and set
\[
\boxed{A_T=(1,2K,2K),\qquad B_T=(2,2,K^2).}
\]
Their differences are
\[
\Delta_1=-(K-1)(K-3),\quad
\Delta_2=4(K-1),\quad
\Delta_3=0.
\]
Here n=1. At odd T≥3, the full equality criterion has k=1 and k=3. Its k=3 equation is automatically satisfied because Δ_3=Δ_4=0; the k=1 equation is
\[
b\Delta_1+2(T-1)\Delta_2
=2(K-1)[-(K-3)+4(T-1)]=0.
\]
Therefore the full histogram re-aliases exactly at t=T after first separating at t=1, and differs at every other positive integer time by PREFIX-833.1. The maximal source weight K² grows quadratically; the earlier two-source odd construction gives the stronger linear-size option when p is not fixed at 3.

### Source-count minimality and absence of T≤2

For p=1, n=1=p and PREFIX-833.1 gives no positive-time re-aliasing. For p=2, n=2 implies p=n, again impossible; n=1 implies any exceptional time must satisfy T≥n+2=3 and T≡n (mod 2), hence T is odd. For arbitrary p, n≥1 and any positive-time exceptional coincidence requires T≥n+2≥3. These facts prove the claimed minimum counts for each T.

## Theorem 834.2 — Full p=3 algebraic classification of possible re-aliasing

For any fixed positive integers a,b and two different 3-source positive-integer multisets:

* **n=3:** re-aliasing after separation is impossible.
* **n=2:** re-aliasing is possible only at an even integer T≥4. It happens **if and only if** `2b Δ_2 + 3(T-2) Δ_3 = 0`. At this T all bins match, and at all other times t≥2 they differ.
* **n=1:** re-aliasing is possible only at an odd integer T≥3. It happens **if and only if** `Δ_3=0` and `b Δ_1 + 2(T-1) Δ_2 = 0`. At all other positive times the histograms differ.

**Proof:** With p=3, the exact criterion of PREFIX-833.2 has index set K_T={k:n≤k≤min(3,T), k≡T (mod 2)}. For n=2, T even≥4, this set is {2}; it imposes exactly the first displayed equation. For n=1, T odd≥3, this set is {1,3}; the k=3 condition requires Δ_3=0 (if T=3 it is the terminal condition Δ_T=0, and if T≥5 it is b·3·Δ_3=0); k=1 yields the second equation. n=3=p has no later equality by PREFIX-833.1. Completeness follows because the criterion checks all occupancy bins, and uniqueness of the exceptional time is guaranteed by PREFIX-833.1. QED.

## Independent exact integer verification

The accompanying Python check evolves every legal **named subset plus marked flag** state and aggregates complete occupancy histograms. It does not use the closed formula to perform its transitions. It separately compares with the independent PREFIX-832 elementary-symmetric closed formula, checks first separation, the full equality set through T+4, and opposite-parity witnesses.

Verified p=3 targets T=3,4,5,6,7,8,9,10,11,12,17,20,21,30,40; two-source targets T=3,5,7,11,21,31. Run `python3 PREFIX834_R6_PARITY_RECOLLISION_CHECK.py`. The exact local run returned `ALL_EXACT_ASSERTIONS_PASSED`: 15 three-source profile pairs, 1,112 histogram scalar comparisons, 8,638 named-state edge updates (including two-source subtests), 120 opposite-parity witness checks and 96 two-source frame checks. The numerical range is finite; the any-T statements follow from the displayed identities and PREFIX-833's proof.

**Caveat / scope:** p counts *named initial sources*, not distinct numeric weight values. Relative signed Δ's are differences between positive integer masses, not signed amplitudes. Auxiliary Q steps do not assert physical heartbeat time, native X6 event license, or a Foundation theorem. No independent mathematical review or promotion has occurred.

## Progress and next discriminating question

The odd-time minimal threshold 2 was established in PREFIX-833; new is the even-time threshold 3, all-time parity-complete p=3 fixed-operator realizations, and complete p=3 algebraic classification. Next: derive exact bit/weight lower bounds for same-operator even-time p=3 re-aliasing (is linear max weight optimal?), then test finite-window observer minimization under these explicit aliases, and independently retain q≥5, b>0 minimal positive Q-carrier as an open branch. Preserve the same frozen scientific pin.