# P025 Supplement 04 — Mason Witness-Slack and Infinity Contact Depth

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-mason-witness-slack`  
Parent payload: `program/p025-abc-support-collapse@6c854aeb`  
Prior-art status: classical Mason--Stothers/Wronskian mathematics; architecture interpretation `NOVELTY_UNVERIFIED`

## 1. Goal

The first P025 generation extracted the classical Mason--Stothers route as

\[
\text{multiplicity residual}
\to
\text{common Wronskian witness}
\to
\text{witness capacity}
\to
\text{radical bound}.
\]

The present supplement asks a narrower question:

> Does the successful polynomial proof contain an exact finite **proof-slack state** that can be compared with P018/P023 precision language?

The answer is yes, but the underlying polynomial algebra remains classical. The reusable candidate is the accounting interface, not a new Mason theorem.

Throughout this note let `P_0,P_1,P_2` be nonzero pairwise-coprime polynomials over a characteristic-zero field satisfying

\[
P_0+P_1+P_2=0,
\]

and suppose the common cyclic Wronskian is nonzero. Write

\[
h_i=\deg P_i,
\qquad
R=\deg\operatorname{rad}(P_0P_1P_2),
\qquad
D=h_0+h_1+h_2-R.
\]

In the classical Wronskian proof, the product of multiplicity residuals divides the common Wronskian, so

\[
D\le w,
\qquad
w=\deg W.
\]

For any target index `i`, if `{j,k}` is its complementary pair, the ordinary derivative bound gives

\[
w\le h_j+h_k-1.
\]

These are established Mason--Stothers ingredients [SRC-BAEK-LEE-2024-MASON-LEAN].

## 2. P025-T11 — exact proof-margin decomposition

For target `i`, define

\[
A_i=w-D
\]

and

\[
C_i=h_j+h_k-1-w.
\]

Both are nonnegative under the classical proof inequalities. Then

\[
\boxed{
R-h_i-1=A_i+C_i.
}
\]

### Proof

Because

\[
D=h_0+h_1+h_2-R,
\]

we have

\[
R-h_i-1
=h_j+h_k-1-D.
\]

Insert and subtract `w`:

\[
h_j+h_k-1-D
=(w-D)+(h_j+h_k-1-w)
=A_i+C_i.
\]

No asymptotic argument is involved.

### Interpretation

`A_i` measures how much degree room remains after the multiplicity residual has been absorbed into the common witness:

\[
\boxed{A_i=\text{residual absorption slack}.}
\]

`C_i` measures how far the actual Wronskian lies below its elementary complementary-pair degree ceiling:

\[
\boxed{C_i=\text{witness capacity slack}.}
\]

The final Mason margin is not one undifferentiated number; it is the exact sum of these two proof-stage resources.

## 3. P025-T12 — Wronskian capacity slack equals infinity contact depth

Let `P,Q` be nonzero, non-proportional polynomials over a characteristic-zero field. Put

\[
p=\deg P,
\qquad
q=\deg Q,
\]

and

\[
W(P,Q)=P'Q-PQ'.
\]

Define the Wronskian capacity slack

\[
\boxed{
\kappa_\infty(P,Q)
=p+q-1-\deg W(P,Q).
}
\]

We now give this nonnegative integer an exact coefficient meaning.

### Unequal degrees

If `p neq q`, the leading term of `W(P,Q)` is

\[
(p-q)\operatorname{lc}(P)\operatorname{lc}(Q)x^{p+q-1},
\]

which is nonzero in characteristic zero. Hence

\[
\deg W(P,Q)=p+q-1
\]

and therefore

\[
\boxed{\kappa_\infty(P,Q)=0.}
\]

The two degree profiles are already separated at the first leading layer.

### Equal degrees

Now let

\[
p=q=d.
\]

Write `a=lc(P)` and `b=lc(Q)` and form the leading-cancellation polynomial

\[
E=bP-aQ.
\]

Since `P,Q` are not proportional,

\[
E\ne0,
\qquad
 e=\deg E<d.
\]

Moreover

\[
W(E,Q)=bW(P,Q),
\]

because the `Q,Q` Wronskian vanishes. Since `e neq d`, the unequal-degree case applied to `(E,Q)` gives

\[
\deg W(P,Q)=\deg W(E,Q)=e+d-1.
\]

Consequently

\[
\boxed{
\kappa_\infty(P,Q)=d-e.
}
\]

Define

\[
\boxed{
\delta_\infty(P,Q)=
\begin{cases}
0,&\deg P\ne\deg Q,\\
d-\deg(bP-aQ),&\deg P=\deg Q=d.
\end{cases}
}
\]

Then exactly

\[
\boxed{
\kappa_\infty(P,Q)=\delta_\infty(P,Q).
}
\]

### Finite-precision meaning

For equal degree `d`, divide conceptually by the leading terms and use the local coordinate `t=1/x`. The integer `delta_infinity` is the first positive coefficient depth at which the two normalized jets differ.

Thus the ordinary Wronskian degree loss is exactly a **collision depth at infinity**:

\[
\boxed{
\text{Wronskian capacity loss}
=
\text{normalized leading-jet coalescence depth}.
}
\]

The proof uses only finite coefficient comparison; no limiting continuum object is required by the executable interpretation.

## 4. P025-T13 — Mason margin as absorption slack plus contact depth

Substituting P025-T12 into P025-T11 gives, for target `i` and complementary pair `(P_j,P_k)`,

\[
\boxed{
R-h_i-1
=
(w-D)+\delta_\infty(P_j,P_k).
}
\]

This is the main calibration result of this supplement.

It exposes two logically different reasons that the final radical degree can exceed the target degree by more than the bare Mason unit:

1. the common witness may contain degree capacity not forced by multiplicity residuals;
2. the complementary polynomial pair may remain indistinguishable for several normalized leading coefficient layers before the Wronskian detects their split.

If the complementary degrees differ, then

\[
\delta_\infty=0,
\]

so the entire final margin beyond the Mason unit is residual absorption slack.

If the complementary degrees are equal and non-proportional, then

\[
\delta_\infty\ge1,
\]

so that orientation automatically has at least one extra unit of radical margin.

This is an elementary consequence of the Wronskian proof, not a historical novelty claim about Mason extremal cases.

## 5. P025-N03 — the final theorem margin can erase proof provenance

Consider the following two exact polynomial relations over characteristic zero.

### Example A

\[
P_0=x^2,
\qquad
P_1=x^2+1,
\qquad
P_2=-(2x^2+1).
\]

The three polynomials are pairwise coprime and have degrees `(2,2,2)`. Their radical degrees are `(1,2,2)`, so

\[
R=5,
\qquad
D=1.
\]

For target `P_2`,

\[
W(P_0,P_1)=2x,
\qquad
w=1.
\]

Hence

\[
A_2=w-D=0,
\qquad
\delta_\infty(P_0,P_1)=2,
\]

and

\[
R-h_2-1=2=0+2.
\]

### Example B

\[
P_0=x^2,
\qquad
P_1=x^2+x+1,
\qquad
P_2=-(2x^2+x+1).
\]

Again the degree triple is `(2,2,2)`, the three polynomials are pairwise coprime, and

\[
R=5,
\qquad
D=1.
\]

Now

\[
W(P_0,P_1)=x^2+2x,
\qquad
w=2.
\]

Thus

\[
A_2=1,
\qquad
\delta_\infty(P_0,P_1)=1,
\]

while the final theorem margin is still

\[
R-h_2-1=2=1+1.
\]

Therefore the coarse data

\[
(h_0,h_1,h_2,R,R-h_2-1)
\]

can be identical while the internal proof-resource decomposition differs.

So the final theorem truth/margin is not a complete state for questions about **why** the proof succeeded or where the unused capacity resides.

## 6. Architecture consequence — decision precision versus proof-provenance precision

P023 already says that required precision depends on the declared future observation. The two examples above give an already-proved mathematical calibration of the same principle at proof level.

If the task asks only for the final Mason inequality, the internal pair

\[
(A_i,\delta_\infty)
\]

may be safely erased once their sum is known.

If the future task asks any of the following, the final margin alone is insufficient:

- whether residual absorption was exact;
- whether the Wronskian lost degree through leading-jet collision;
- how many normalized coefficient layers coalesced;
- which proof stage supplied the spare margin.

This motivates a distinction:

\[
\boxed{\text{decision precision} \ne \text{proof-provenance precision}.}
\]

P025 does not propose putting all proof traces into foundational state. The lesson is the opposite: retain proof-stage coordinates only when later queries consume them, exactly as P023 requires.

## 7. Prior-art and novelty boundary

The Mason--Stothers theorem, polynomial radicals, derivative divisibility, cyclic Wronskian equality, and the Wronskian degree bound are established mathematics [SRC-BAEK-LEE-2024-MASON-LEAN]. Equality and extremal cases of polynomial `abc` also have a substantial prior literature, so this supplement makes no priority claim for extremal classification.

The identity

\[
U-D=(w-D)+(U-w)
\]

is elementary accounting. Likewise the equal-degree leading-cancellation proof of the Wronskian degree drop is elementary polynomial algebra.

The only project-side candidate is the integration:

\[
\text{proof residual}
\to
\text{witness absorption slack}
\to
\text{coefficient collision depth}
\to
\text{task-relative proof state}.
\]

Its historical novelty is `NOVELTY_UNVERIFIED`.

## 8. Executable assets and regression

This generation adds:

- `src/enterprise_math/mason_witness_slack.py`
  - exact integer polynomial arithmetic;
  - Wronskian degree and capacity slack;
  - exact infinity-contact depth;
  - Mason margin decomposition;
  - relation-level slack profile.
- `tests/test_mason_witness_slack.py`
  - unequal-degree zero contact depth;
  - equal-degree depth-one and depth-two examples;
  - the two same-final-margin/different-provenance Mason samples;
  - invalid-bound and proportional-pair guards;
  - exhaustive small-coefficient comparison of Wronskian capacity slack against infinity contact depth.

An independent pre-repository prototype checked 382,848 non-degenerate ordered polynomial pairs with degrees `1..3` and coefficients in `[-2,2]` and found no mismatch. This is regression evidence only; P025-T12 is proved above.

## 9. Next frontier

Three questions remain high value:

1. **P018 bridge:** determine whether `delta_infinity` is best understood as a specialization of an existing first-separation / collision-depth coordinate, or whether it exposes a missing general theorem about finite coefficient jets.
2. **P023 bridge:** classify precisely when the pair `(absorption_slack, contact_depth)` can be replaced by its sum for a declared proof-query language.
3. **Integer abc return:** ask whether Pasten's arithmetic Wronskian has an analogous finite slack decomposition whose components reveal more than its final norm bound; do not assume the polynomial degree identity transports automatically.

The preferred next step is to solve 1 and 2 in the already-proved polynomial world before returning to stronger integer-abc claims.
