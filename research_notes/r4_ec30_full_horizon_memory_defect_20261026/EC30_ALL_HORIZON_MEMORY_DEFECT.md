# R4-EC30: exact all-horizon memory defect and rank-two certificate for X6 positive-source BRC

Date: 2026-10-26, Asia/Shanghai. Claim category: **author-side proved derivation**, finite exact tests, not an independent Driver review, accepted Result, or native physical theorem.

## Frozen sources, identity and boundaries

Account canonical read: awdawmip/chatgpt-global-knowledge main@8c38dfefccb02323723a85f214d31bcf844bbdec; both normative entrypoints, ACTIVE worldview, P000 ACTIVE_LOCKED, math/code/BRC/activity routing read at this same immutable snapshot. Project source: awdawmip/enterprise-math main@7f1913a4940bb97898f1c9c4e4cf542db3221eee, including P000 X6 V5, joint-observer preservation, portable research protocol and heartbeat BRC-only rule.

Direct predecessor: R4-EC29 source commit 1f112b4352e7162ed7afc67f8a6d32eae75530b6, note research_notes/r4_ec29_x6_future_safe_memory_20261026/R4_EC29_X6_BRC_FUTURE_SAFE_MEMORY.md. EC27 is the separate auxiliary unimodality theorem, not established as a native mapping.

GitHub authenticated user awdawmip has repository admin access. Native live-task query returned CONTROL_QUOTA, and native researcher session creation was rejected with STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No live owner or CLAIM has been asserted. This author-side note is not a formal native execution.

P000 is assumed without attempt to prove/change it. This is the **EC29 explicitly invented positive-branch test transition**, operating with chart-relative signed native X6 E1/E2/E3 displacements (E4/E5/E6 unchanged), in a restricted three-axis affine sub-torsor, not a certified whole crystal-packet layer. Depth h counts ordered operations, not heartbeat time. Source weights are positive integers, not phases or signed amplitudes. Raw six-coordinate displacements are not encoded final Cell addresses.

## 1. Source-letter law for every future word

Operations: A = +E1 (grade 0), B = +E2 (grade 1), C = +E3 (grade 0). Retained historical bit q is 1 precisely when the previous letter was A; otherwise q=0. A sets q=1; B/C set q=0. A and B always have exactly one source choice. C has two distinct source-labelled choices when q=1, one otherwise.

Let N_q(w) be the exact number of source-labelled realizations of a fixed future operation word w from initial q. Let ac(w) count adjacent occurrences of AC. Every word has finite length and w=empty is permitted.

**Theorem A (all word lengths).**

\[
N_0(w)=2^{ac(w)},\qquad
N_1(w)=2^{ac(w)+\mathbf1_{\{w\text{ begins with C}\}}}.
\]

Equivalently:

\[
N_1(w)-N_0(w)=
\begin{cases}
N_0(v),&w=Cv,\\
0,&w=\emptyset\text{ or begins with A or B}.
\end{cases}
\tag{A}
\]

Proof: distinct AC occurrences in an undecorated word correspond to exactly the C locations with two independently selectable source labels. Initial q=1 gives precisely one further binary choice at the first letter if that letter is C. After the first letter the two possible initial q values lead to the same next q, hence no later initial-history difference. Multiplication of these exact positive counts proves both equations without approximation. QED.

## 2. Sharp positive defect at every endpoint with a C component

Let F_q(t;x,y,z,u) sum source-labelled paths of all lengths, with monomial t^h x^a y^b z^c u^b for word counts a,b,c of A,B,C; the independent grade is b. EC29 proved:

\[
F_0=\frac{1}{1-t(x+uy+z)-t^2xz}.
\]

**Theorem B (all endpoints and depths).** The difference from forgetting the previous-A bit has the exact, nonnegative generating function

\[
\boxed{F_1-F_0=tzF_0
=\frac{tz}{1-t(x+uy+z)-t^2xz}.}\tag{B1}
\]

For every a,b,c>=0, put W_q(a,b,c)=[t^{a+b+c}x^ay^bz^cu^b]F_q and W=W_0. Then

\[
\boxed{W_1(a,b,c)-W_0(a,b,c)=
\begin{cases}W(a,b,c-1),&c>=1,\\0,&c=0.\end{cases}}\tag{B2}
\]

For every c>=1 the defect is **strictly positive**, and inserting EC29's positive-count factorial formula gives

\[
\boxed{\Delta W(a,b,c)
=\sum_{r=0}^{\min(a,c-1)}
\frac{(a+b+c-1-r)!}{r!\,(a-r)!\,b!\,(c-1-r)!}.}\tag{B3}
\]

Proof: by (A) the excess paths are *exactly* those whose first future step is an extra source-labelled C. Deleting that first C yields a bijection with all q=0 source-labelled continuation paths. The deletion removes one length step and one C endpoint increment, and preserves A/B counts and grade; this proves (B1) and (B2). The underlying unmarked word exists for every nonnegative count triple, so W(a,b,c-1)>0. EC29's direct source-atom bijection proves its factorial W identity, giving (B3). QED.

Thus a single missing relational/history bit creates nonzero positive-source count defects at **all** future endpoints involving C, not just the EC29 one-step witness. It is not an experimentally measured native physics residual.

## 3. Exponential lower bound in future operation depth

Set x=y=z=u=1, write H_h=[t^h]F_0, D_h=[t^h](F_1-F_0). Then

\[
H_0=1,\ H_1=3,\quad H_h=3H_{h-1}+H_{h-2}\ (h>=2)
\]

and

\[
\boxed{D_0=0,\quad D_h=H_{h-1}\ge3^{h-1}\ (h>=1),}
\tag{C}
\]

strictly above 3^(h-1) for h>=3.

Proof: specialization of (B1) gives F0=1/(1-3t-t^2), and F1-F0=t/(1-3t-t^2), yielding the exact recurrence and shift. H_n>=3^n follows by induction from H0=1,H1=3 and H_n=3H_(n-1)+H_(n-2)>3H_(n-1) for n>=2. This gives (C), including the strict case. QED.

This growth is in finite *suffix length*, not in physical elapsed time. The first H values are 1,3,10,33,109,360,1189; the corresponding D values are 0,1,3,10,33,109,360.

## 4. Stronger minimality: no one-dimensional linear weighted observer

Take the full source-word function f(w)=N_0(w). The infinite word-Hankel matrix has entries f(ps), indexed by prefixes p and suffixes s. Take two prefixes with the **same present X6 endpoint**, grade, depth and count: AB and BA. Take suffixes empty and C. Then

\[
\boxed{
\begin{pmatrix}f(AB)&f(ABC)\\f(BA)&f(BAC)\end{pmatrix}
=\begin{pmatrix}1&1\\1&2\end{pmatrix},
\quad\det=1.}\tag{D}
\]

For any d-dimensional linear weighted word representation over Q, f(ps)=alpha M_p M_s beta. Its Hankel factors through a d-dimensional vector space; therefore its rank is at most d. (D) implies d>=2. The existing q=0/q=1 source automaton is a two-dimensional exact realization, hence

\[
\boxed{\operatorname{rank}_{\mathbb Q}(\operatorname{Hankel} f)=2.}
\]

This rules out *any* single-scalar linear weighted state representation for this full future-word observer, a stronger class than merely merging deterministic q states. It does not exclude nonlinear encodings or fully labelled-history storage required by richer observers.

## 5. Verified implementation, audit note and next question

Attached EC30_verify.js performs exact positive-source BigInt endpoint-state recursion, independently checks all endpoints against EC29's factorial W and new defect through depth 15, and enumerates **individual labelled branches** for each word through depth 8 starting in both q states. It checks the total recurrence, exact D shift, quantitative bound and Hankel minor. Exact observed counts and trust boundary are in EC30_REPORT.json. Finite tests support implementation integrity; universal results follow from the proofs above, **not finite extrapolation**.

Author-side EC27 audit correction, **not independent Driver review**: its exposition describing all terms of its equation (9) as coefficientwise nonnegative overstates the situation. The polynomial (1-t)(1+t)^p has negative coefficients: for p=1 its t^2 coefficient is -1. But EC27's actual tail comparison only uses j>=p+2, where this polynomial has coefficient zero; the remaining terms are nonnegative. Thus this is a local phrasing repair, not a counterexample to EC27's universal unimodality conclusion, subject to independent review.

BRC reuse classification: REUSE_APPLIED to EC29 Path-formal/N-BRC exact positive-source carrier and W theorem; EXTEND_EXISTING_TOOL for full-horizon source-memory defect; COMPOSE_APPLIED for weighted Hankel source-minimality. No ordinary analytic propagator or trigonometric computation was used.

**Current native gap:** the pinned heartbeat world source contains fixed_heartbeat_program=null. A real source-labelled update, legitimate selected three-dimensional crystal-packet layer, third coordinate, separately typed time, observer scope and operation-commuting source-fibre correspondence have not been established. The EC27-to-native theorem is still UNPROVED, and no P000 heartbeat simulation or native Driver review was executed.

**Next precise question (EC31):** find the actual declared source-labelled native update and test operation/grade/endpoint/source-fibre preservation at two and three steps. If no update is fixed, classify the smallest additional independent branching rule needed for identification. Use equations (A)–(D) as exact regression/witness and independently audit the EC27 tail proof. Do not upgrade this test law to the real update merely because its steps lie on native X6 axes.
