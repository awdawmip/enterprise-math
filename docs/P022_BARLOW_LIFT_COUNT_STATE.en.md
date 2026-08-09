# P022 — Lift-Count State Is Future-Sufficient for Count Queries but Not Mechanism Queries

Status: `ACTIVE RESEARCH NOTE / EXACT TASK-RELATIVE SUFFICIENCY + NEGATIVE BOUNDARY`  
Owner: `program/p022-geometry-v2`  
Depends on: higher-channel mixed-radix path lifting; rank-two binary boundary  
Cross-route relevance: A2/P023 future-compatible quotient; P024 typed observation precision; A4 witness-count semantics

## 1. The question created by mixed-radix repair

For a higher-channel quotient path

\[
h=(p_1,\ldots,p_N),
\]

let

\[
\mathcal M(h)=(m_1,\ldots,m_N)
\]

be its exact local lift-radix sequence and

\[
F(h)=\prod_{t=1}^Nm_t
\]

its total microscopic path-lift cardinality.

The prime-valuation theorem already shows that `F(h)` forgets how the product was assembled.

But whether that loss is legal depends on the future query.

This note separates two future languages:

1. **count language** — later queries ask only how many microscopic lifts realize a declared continuation;
2. **mechanism language** — later queries may inspect when/how local repair branches occurred.

---

## 2. P022-LC01 — the exact lift-count Markov state

For a nonempty coarse path define

\[
\boxed{
C(h)=(p_N,F(h)).
}

This keeps only:

- the current chamber state;
- the current total microscopic lift count.

Suppose the next declared coarse state is `r`.  The higher-channel transition theorem provides the local multiplicity

\[
m(p_N,r).
\]

Every existing lift of `h` has exactly this many microscopic one-step lifts realizing `r`. Therefore

\[
\boxed{
C(h\cdot r)
=
\bigl(r,\ F(h)m(p_N,r)\bigr).
}
\]

Iterating along any legal continuation

\[
c=(r_1,\ldots,r_k)
\]

gives

\[
\boxed{
F(h\cdot c)
=
F(h)
\prod_{j=1}^k
m(r_{j-1},r_j),
}
\]

where `r_0=p_N`.

Thus `C(h)` is an exact finite Markov state for every future query that depends only on total lift cardinalities of declared coarse continuations.

No local-radix history is required for that language.

---

## 3. P022-LC02 — same compressed state implies identical future count semantics

If two histories satisfy

\[
C(h)=C(h'),
\]

then they share the same current chamber state and current lift count.

For every common legal coarse continuation `c`, LC01 applies the same sequence of local multipliers to the same starting count. Hence

\[
\boxed{
F(h\cdot c)=F(h'\cdot c)
}
\]

and the final compressed states also agree.

So the equivalence relation

\[
h\sim_{\rm count}h'
\iff C(h)=C(h')
\]

is future-compatible for the entire total-lift-count language.

This is a concrete P022 specialization of A2/P023 quotient safety.

---

## 4. P022-LC03 — exact same-state/same-count mechanism alias

Rank three supplies a small explicit counterexample showing that this compression is not safe for a richer mechanism language.

Consider

\[
\begin{aligned}
h={}&
(1,1,1)
\to(0,0,0)
\to(1,1,1)
\to(0,2,2),\\
h'={}&
(1,1,1)
\to(0,0,2)
\to(1,1,3)
\to(0,2,2).
\end{aligned}
\]

Their local radix sequences are

\[
\boxed{
\mathcal M(h)=(8,1,8,3),
}
\]

and

\[
\boxed{
\mathcal M(h')=(8,3,4,2).
}
\]

They differ as time-labelled repair mechanisms.

But

\[
8\cdot1\cdot8\cdot3
=
8\cdot3\cdot4\cdot2
=192,
\]

and both terminate at

\[
(0,2,2).
\]

Therefore

\[
\boxed{
C(h)=C(h')=((0,2,2),192)
}
\]

while

\[
\boxed{
\mathcal M(h)\ne\mathcal M(h').
}
\]

So the mechanism observable is not constant on fibers of the lift-count state map and cannot factor through it.

---

## 5. The same alias survives every count-only future

Take any legal common continuation `c` from `(0,2,2)`.

By LC02,

\[
F(h\cdot c)=F(h'\cdot c).
\]

For example, continuing through

\[
(1,1,3)
\to(0,2,2)
\]

multiplies both histories by exactly the same local factors.

Thus the alias is not a one-time equality that immediately disappears. It defines a genuine future-compatible quotient for the declared count language.

This is the positive side of task-relative compression.

---

## 6. But the repair mechanism remains permanently different as history

The two local-radix sequences encode different branch timing:

- in `h`, the middle return to the origin collapses the local radix to one and later releases an eight-way branch;
- in `h'`, repair is distributed through factors `3,4,2` without that same reset structure.

The total fiber cardinality forgets this temporal organization.

Therefore any future query that asks, for example,

- which time carried an odd-prime repair factor;
- the maximum local radix;
- number of branching stages;
- typed wall/stabilizer mechanism;
- streaming resource needed at each stage;

cannot in general be answered from `(p,F)`.

The same compressed state is exact for one language and insufficient for another.

---

## 7. Prime signature has the same count-language status

The prime-valuation signature

\[
\nu(F)=\{(p,v_p(F))\}
\]

is equivalent to the positive integer `F`, so

\[
(p,F)
\longleftrightarrow
(p,\nu(F)).
\]

It provides an additive update rule

\[
\nu(Fm)=\nu(F)+\nu(m),
\]

but does not restore the local-radix sequence.

Thus prime coordinates are an exact arithmetic representation of the **count state**, not of the **mechanism state**.

---

## 8. Precision consequence

This example isolates the future-language distinction especially cleanly:

### Count future

\[
\boxed{
(\text{current chamber},\text{total lift count})
\text{ is exact and future-compatible.}
}
\]

### Mechanism future

\[
\boxed{
(\text{current chamber},\text{total lift count})
\text{ is insufficient.}
}
\]

So more microscopic history is not intrinsically “higher precision.” Its necessity is determined by the future observable.

This is precisely the project-wide rule that a compression is legal only relative to a declared future language, now realized in a higher-rank geometry where the repair state is genuinely mixed-radix.

---

## 9. Upstream ownership boundary

LC01–LC02 are instances of a broader statement:

> in a quotient transition system whose local lift multiplicity depends only on the current and next quotient states, current quotient state plus accumulated lift count is a sufficient state for future lift-count queries.

That statement no longer needs Barlow geometry.  If promoted as a mother theorem, it belongs to A2/P023 and/or A4 after ownership audit.

P022 retains:

- the exact `B_d` specialization;
- the rank-three same-state/same-count mechanism alias;
- the geometry-specific interpretation of local repair radices.

---

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_lift_count_state.py`;
- `tests/test_p022_barlow_lift_count_state.py`.

The tests verify the exact rank-three alias, recompute full extended path counts independently from the compressed update, and encode the negative factorization result for mechanism queries.
