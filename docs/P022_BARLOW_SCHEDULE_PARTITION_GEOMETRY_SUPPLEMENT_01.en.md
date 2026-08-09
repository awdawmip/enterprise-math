# P022 — Exponential Ordered-Schedule Collapse into Subexponential Partition States

Status: `ACTIVE RESEARCH NOTE / ASYMPTOTIC STATE-COUNT CONSEQUENCE / CLASSICAL PARTITION INPUT`  
Owner: `program/p022-geometry-v2`  
Depends on: composition-to-partition collision geometry  
Prior-art boundary: Hardy–Ramanujan partition asymptotics are classical

## 1. Exact finite state counts

For final-observing schedules of total horizon `N`, the previous theorem gives

\[
\boxed{
\#\text{ordered schedules}=2^{N-1}
}
\]

and

\[
\boxed{
\#\text{complete collision states}=p(N),
}
\]

where `p(N)` is the ordinary integer partition number.

Thus the complete collision state preserves the unordered segment multiset but quotients out all segment permutations.

---

## 2. P022-SP05 — partition-state image is subexponential

The classical Hardy–Ramanujan asymptotic is

\[
\boxed{
p(N)
\sim
\frac1{4N\sqrt3}
\exp\left(\pi\sqrt{\frac{2N}{3}}\right).
}
\]

Hence

\[
\log p(N)
=
\pi\sqrt{\frac{2N}{3}}
+O(\log N),
\]

which is sublinear in `N`.

By contrast,

\[
\log 2^{N-1}
=(N-1)\log2.
\]

Therefore

\[
\boxed{
\frac{p(N)}{2^{N-1}}
=
\exp\bigl(-N\log2+O(\sqrt N)\bigr)
\longrightarrow0.
}
\]

So the complete collision-polynomial image occupies an exponentially vanishing fraction of the ordered final-observing schedule space.

This does **not** mean the collision state is incomplete for its declared fiber-statistics language.  It means that commutative aggregation has deliberately removed an exponentially large amount of **ordering geometry**.

---

## 3. P022-SP06 — mean order-repair fiber over collision states is exponential

When collision states are weighted equally, the mean number of ordered final-observing schedules represented by one complete collision state is

\[
\frac{2^{N-1}}{p(N)}.
\]

Substituting the classical partition asymptotic gives

\[
\boxed{
\frac{2^{N-1}}{p(N)}
\sim
2^{N+1}N\sqrt3
\exp\left(-\pi\sqrt{\frac{2N}{3}}\right).
}
\]

Thus the mean residual order-repair cardinality is exponential in `N` up to a subexponential correction.

Again this is a **collision-state-weighted geometry fiber average**, not a microscopic Barlow-history average and not a bit count unless an external coding convention is added.

---

## 4. Arbitrary checkpoint subsets

If the final layer need not be observed, exact finite state counts are

\[
\boxed{
\#\text{checkpoint subsets}=2^N,
}
\]

and

\[
\boxed{
I_N
=
\sum_{L=0}^{N}p(L)
}
\]

complete collision states.

Since `p(L)` is increasing,

\[
p(N)
\le
I_N
\le
(N+1)p(N).
\]

Therefore the same Hardy–Ramanujan estimate immediately gives

\[
\boxed{
\log I_N
=
\pi\sqrt{\frac{2N}{3}}
+O(\log N),
}
\]

and hence

\[
\boxed{
\frac{I_N}{2^N}
=
\exp\bigl(-N\log2+O(\sqrt N)\bigr)
\longrightarrow0.
}
\]

So allowing a hidden tail changes exact finite routing but not the exponential-versus-subexponential separation.

---

## 5. Precision interpretation

This gives a particularly clean example of legal task-relative collapse:

\[
\boxed{
\text{ordered schedule geometry}
\to
\text{complete collision state}
}
\]

removes exponentially many order arrangements while retaining exactly the segment multiset and hidden tail required by the complete fiber-statistics language.

If a later task suddenly asks for checkpoint order, the removed information is not “noise”.  It returns as the exact order-repair fiber

\[
M_{\rm ord}=m!/\prod t_\ell!.
\]

So an aggressive state-space collapse can be perfectly legal for one future language and extremely expensive to reverse for another.

That is the P022 geometric instance of the general future-compatible quotient principle.

---

## 6. Prior-art boundary

The partition asymptotic is classical and no novelty claim is made for it.

The P022-specific result is the previously proved exact bijection between complete Barlow collision states and partition geometry, which lets the classical partition growth law quantify the amount of ordered checkpoint structure erased by the collision quotient.
