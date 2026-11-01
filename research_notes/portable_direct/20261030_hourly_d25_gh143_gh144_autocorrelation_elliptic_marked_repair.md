# D25/LIFT GH-143–GH-144 — Signed-fibre autocorrelation as an elliptic trace, and exact marked repair

2026-10-30 Asia/Hong_Kong. Own TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923. Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). State: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## GH-143 — Exact autocorrelation-to-elliptic trace theorem

Let p≥5 be prime, K=F_(p²), q=p² and χ the quadratic character χ(0)=0. Reuse GH-141's F(t)=Σ_(x²+x+t=0)χ(x), with distinct roots, c=1/4, F(c−t)=F(t); and GH-142's exact histogram. Set the integer-valued C(h)=Σ_t F(t)F(t+h).

**Theorem.** C(0)=q−3, C(±1/4)=−3. For every h≠0,±1/4, E_(4h²): y²=x³+x²+4h²x is smooth and

  C(h)=−a_q(E_(4h²))−2, where a_q(E)=q+1−#E(K).

Thus |C(h)+2|≤2p by Hasse. This explicitly lands in the SAME elliptic family E_B as GH-121/124; it is not an assumption of CM or GH-83.

**Complete derivation.** In the autocorrelation pair t=−x²−x, t+h=−y²−y, use u=x−y, v=x+y+1, so uv=h and 4xy=(v−1)²−u². For h≠0 this gives

  C(h)=Σ_(u∈K×) χ(P_h(u)),  P_h(u)=(h−u)²−u⁴.

The omitted u=0 term has χ(P_h(0))=χ(h²)=1. Factor P_h=(h−u−u²)(h−u+u²). It is squarefree precisely off h∈{0,±1/4}. For generic h the smooth projective quartic V_h: z²=P_h(u) has genus 1 and two K-rational points at infinity because its leading coefficient −1 is a square in K. Hence #V_h(K)=q+2+Σ_uχ(P_h(u)).

There is an explicit birational transfer, not just an invocation of a quartic-Jacobian correspondence. Put

  X=(h−u+z)/u², Y=(X²+1)u+X, x_E=2hX, y_E=2hY.

The quartic equation gives (X²+1)u²+2Xu−2hX=0, whence Y²=2hX³+X²+2hX and y_E²=x_E³+x_E²+4h²x_E. On a dense open set the inverse is u=(Y−X)/(X²+1), z=Xu²−h+u. Both smooth projective genus-one curves are K-isomorphic, hence q+2+Σχ(P_h)=#E_(4h²)=q+1−a_q and C(h)=−a_q−2.

At h=c, P_c=−(u−1/2)²(u²+u−1/4); the quadratic character sum is −1 and the removed repeated-root value χ(1/2)=1, so Σχ(P_c)=−2, C(c)=−3. The h=−c case is symmetric. GH-142 yields C(0)=ΣF²=q−3.

**New global trace identity.** Since Σ_t F(t)=Σ_xχ(x)=0, Σ_h C(h)=0. Excluding the three singular shifts gives

  Σ_(h∈K\{0,±1/4}) a_q(E_(4h²))=−q−3.

Because ±h yield the same B=4h², this equivalently gives

  Σ_(B∈(K×)², B≠1/4) a_q(E_B)=−(q+3)/2.

Classically j(E_(4h²))=16(1−12h²)³/[h⁴(1−16h²)] in the smooth range. This is an explicit new-to-this-project transfer and trace-sum specialization; global literature priority has not been established.

## GH-144 — Minimal label-sensitive repair inside the declared fibre model

Let μ_B(y)=F(B−y) be GH-141's location-labelled signed pushforward and define field-valued first weighted correlation M_B(h)=Σ_y y μ_B(y)μ_B(y+h). The reflection involution t↦c−h−t preserves F(t)F(t+h), so

  2Σ_t tF(t)F(t+h)=(c−h)C(h).

Substitute t=B−y to obtain the exact identity

  M_B(h)=[B−(c+h)/2]C(h) in K.

In particular M_B(0)=(q−3)(B−1/8). Since q−3≡−3 (mod p) is a unit for p≥5,

  B=1/8+M_B(0)/(q−3).

**BRC scope:** The base carrier includes K, χ, the signed root fibres and provenance, and orientation B. Translation-invariant two-point C(h) removes B (so it cannot by itself recover a B-sensitive odd moment); one orientation-sensitive scalar M_B(0) restores the mark when the universal F is retained and future operations are functions of (F,B). This is not an automatic statement about an arbitrary BRC quotient or native six-dimensional P000 geometry. The extra scalar is not a proof of the originally missing S₁(B₀) special value.

## Fully executed exact certificates

At p=3347 take ρ²=2, B₀=(1+2ρ/3)/8=(2092,279), and h=(1370,685) with h²=(523,2580), 4h²=B₀. This is legitimate because Norm(B₀)=1/576 is a base-field square.

One C++17 executable enumerated ALL 11,202,409 pairs in F_(3347²) independently under the quartic P_h and cubic x³+x²+B₀x, and independently constructed every weighted fibre by direct root preimages. Precise integer outcomes:

- Quartic χ sum = 6105; χ counts (−1,0,+1)=(5,598,152,0,5,604,257).
- Cubic χ sum = 6106; χ counts (−1,0,+1)=(5,598,150,3,5,604,256).
- C(h)=6104, a_q(E_B₀)=−6106, #E_B₀(K)=11,208,516. This confirms the old CM trace by an independent exhaustive arithmetic path; it does not independently prove R_3347(9)=0.
- Signed fibre histogram F=−2:1,400,301; −1:0; 0:8,401,806; +1:2; +2:1,400,300.
- C(0)=11,202,406 and M_B₀(0)=2510ρ in K, recovering exactly B₀=(2092,279) from 1/8+M/(q−3).

The executed source d25_gh143_gh144_autocorrelation_check.cpp compiled with g++ -O2 -std=c++17 -Wall -Wextra -Werror and returned PASS_GH143_GH144_P3347_EXACT. A separate independently executed Python standard-library checker exhaustively verified all shifts and weighted correlations for p∈{5,7,11,13,19}, including singular shifts, the generic cubic trace relation and Σ_generic a=−q−3: PASS_GH143_GH144_SMALL_FIELD_ALL_EXACT. That extended checker, run logs and exact source SHA256 are retained in the same-turn portable reproduction bundle.

## Status, independence and next action

These are author-side exact derivations and computations; no independent review, formal Research CLAIM/open, Source checkpoint, native p=373 experiment, or Result/Working Truth admission is claimed. GH-121 already showed an unmarked CM/Frobenius trace is insufficient for the marked tail. This theorem creates a new **elliptic correlation** path to that trace, and GH-144 repairs orientation, but neither evaluates S₁(B₀) independently.

Next precise mathematics: seek a mark-sensitive rationally weighted signed-fibre correlation/resolvent on the explicit E_(4h²) whose CM/Jacobi/p-adic special value retains the normalized derivative required by S₁(B₀), then test against the independent central-moment source. Preserve GH-3/GH-83, original D25 H₀/B₀ divided-power, [X]U mod p², η/Frobenius and native p=373 obligations. No source pin or P000 modification. Existing control issue #1558 remains separate; no session/claim/staging mutation.
