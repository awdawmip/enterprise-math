# P023 — Label Erasure and Image Separation, Supplement 08

Status: `PROVED`  
Owner: A2 / P023 future-compatible quotient  
Pressure source: P017 L054/L052/L055 and P024 future-safe precision  
Discipline: set images, injectivity, decoder existence, and subset monotonicity are elementary mathematics. The project contribution here is a reusable zero-repair and realizability-audit interface.

## 1. When can an auxiliary label actually be erased?

Write a tagged state as

\[
(i,x),
\qquad x\in S_i,
\]

where `i` is a shell/factor/residue label and `x` is the retained coordinate.

The future-safe question is not whether the label was once useful, but whether it remains uniquely recoverable from the retained state after every declared future map.

## 2. Setup

Let the tagged state space be

\[
S=\{(i,x):x\in S_i\}.
\]

The current erasure is

\[
E(i,x)=x,
\]

and let

\[
G:X\to Y
\]

be a later deterministic map.

The sets `S_i` in the theorem are the **actual admissible states** of each label. If only larger envelopes are known, Section 7 gives the correct one-way logic.

## 3. P023-S8-T01 — Current label-erasure criterion

Status: `PROVED`.

The map `E` is injective on the tagged state space if and only if

\[
\boxed{S_i\cap S_j=\varnothing\qquad(i\ne j).}
\]

### Proof

If two labels share the same retained state `x`, then `(i,x)` and `(j,x)` are distinct tagged states erased to the same value. Conversely, if the actual shell sets are pairwise disjoint, equality of retained coordinates forces equality of labels and then equality of tagged states. ∎

### Meaning

When the retained coordinate already determines the shell, the explicit label is a redundant state dimension.

## 4. P023-S8-T02 — Label recovery after a future map

Status: `PROVED`.

A decoder

\[
D:G\!\left(\bigcup_iS_i\right)\to I
\]

with

\[
D(G(x))=i\qquad(x\in S_i)
\]

exists if and only if

\[
\boxed{
G(S_i)\cap G(S_j)=\varnothing
\qquad(i\ne j).
}
\]

### Proof

A common future image would require the decoder to return two different labels at one value. If the images are disjoint, every reachable output belongs to a unique shell image, which defines the decoder. ∎

Thus future-safe label deletion is exactly an image-separation test.

## 5. P023-S8-T03 — Label recovery is weaker than full-state recovery

Status: `PROVED`.

The map

\[
H(i,x)=G(x)
\]

is injective on the full tagged state space if and only if both conditions hold:

1. distinct shell images are pairwise disjoint;
2. each restriction \(G|_{S_i}\) is injective.

### Proof

Cross-shell collisions destroy label recovery; within-shell collisions merge distinct fine states even when the label remains known. If neither type occurs, the tagged state is uniquely recovered. ∎

Therefore

\[
\boxed{
\text{label recoverable}
\not\Rightarrow
\text{full state recoverable}.
}
\]

## 6. P023-S8-T04 — Context-safe label erasure

Status: `PROVED`.

For a declared context family

\[
\mathcal G=\{G_c:X\to Y_c\}_{c\in C},
\]

the label can be erased while remaining recoverable after every context if and only if

\[
\boxed{
G_c(S_i)\cap G_c(S_j)=\varnothing
\quad\text{for every }c\text{ and }i\ne j.
}
\]

Any nonempty overlap is an exact witness that zero repair fails for that context.

## 7. P023-S8-T05 — Admissibility-filtered envelope principle

Status: `PROVED`.

Suppose the true admissible shell is not immediately convenient, but one knows an envelope

\[
S_i\subseteq U_i.
\]

Then for every deterministic map `G`,

\[
G(S_i)\subseteq G(U_i).
\]

Hence

\[
\boxed{
G(U_i)\cap G(U_j)=\varnothing
\Longrightarrow
G(S_i)\cap G(S_j)=\varnothing.
}
\]

### Proof

Images preserve set inclusion. If the larger image sets are already disjoint, their subsets must also be disjoint. ∎

### Logical direction

The converse is false in general. An overlap of envelopes proves only a **candidate collision**. It need not survive the realizability/admissibility filter.

Therefore the safe research rule is

\[
\boxed{
\text{envelope noncollision descends; envelope collision does not.}
}
\]

This creates a three-level audit whenever both a coarse candidate and an exact arithmetic envelope are present:

\[
\text{candidate superset}
\supseteq
\text{exact envelope}
\supseteq
\text{actual admissible state}.
\]

## 8. P017 L054 reinterpretation

In the open square basin, the true least-prime shell coordinate set is

\[
S_p(k)=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

Its exact raw cofactor envelope is

\[
U_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

L054 proves that the envelopes `U_p(k)` are pairwise disjoint for `k>=4`. Since

\[
S_p(k)\subseteq U_p(k),
\]

T05 implies the true shell coordinate sets are disjoint as well. Consequently least-prime label `p` is a function of the stripped cofactor `q` from `k>=4` onward.

Within a fixed shell, `n=pq`, so retaining `q` also recovers the composite state once its unique shell is decoded.

## 9. Root projection and the three-layer P017 hierarchy

After retaining only

\[
G(q)=R_2(q),
\]

three different objects must not be conflated:

1. L052's enlarged candidate root pair;
2. the root image of the exact raw cofactor window;
3. the root image actually realized by the `p`-rough least-prime shell.

L055 proves the stronger middle-layer statement that distinct lower-band **exact-window** root images are disjoint for `k>=9`; the realized shell images inherit this immediately.

The difference is real. At `k=6`, the exact `p=3` window reaches root 4 only through `q=16`, but `3*16=48` has least prime factor 2, so that root is not actually realized by the `p=3` shell.

Thus actual-image discipline must include the admissibility filter, not merely exact interval endpoints.

## 10. Repair interpretation

If actual images overlap, one should not automatically restore the whole original label. The required extra state is the coarsest repair that separates the **realized** conflicting fibers for the declared task.

The zero-repair fast path is

\[
\boxed{
G(S_i)\cap G(S_j)=\varnothing\ \forall i\ne j
\Longrightarrow
\text{shell-label repair cost}=0.
}
\]

P023 Supplement 09 supplies the finite minimum-alphabet counting layer when zero repair fails.

## 11. Research-tool workflow

For shell, residue, geometric-sector, collision-mode, or other auxiliary labels:

1. write the actual admissible fine sets `S_i`;
2. if only envelopes `U_i` are easy, record explicitly that `S_i subset U_i`;
3. use envelope disjointness only as a sufficient certificate;
4. if envelopes overlap, filter to actual admissible states before declaring a collision;
5. apply each declared future map to the actual sets;
6. delete the label when actual images stay disjoint;
7. otherwise compile only the minimum repair needed on realized overlaps.

Executable assets:
- `src/enterprise_math/label_erasure.py`
- `tests/test_p023_label_erasure.py`
- P017 specialization: `src/enterprise_math/p017_actual_root_separation.py`

## 12. Prior art and novelty discipline

Disjoint images iff a label decoder exists, and image monotonicity under subset inclusion, are elementary set theory rather than new mathematics.

Enterprise Math uses them as a disciplined future-safe precision compiler and, crucially, as a guard against promoting candidate/envelope collisions into claims about states that are not actually realizable.
