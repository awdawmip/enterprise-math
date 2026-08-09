# P022 — Checkpoint Compositions Collapse to Integer Partitions

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE STATE COUNT / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: collision-polynomial geometry inversion, segment-order repair  
Prior-art boundary: integer compositions and partitions are classical

## 1. From local order loss to the whole schedule space

For a final-observing checkpoint schedule of total horizon `N`, let

\[
(\ell_1,\ldots,\ell_m),
\qquad
\ell_j\ge1,
\qquad
\sum_j\ell_j=N
\]

be its ordered segment lengths.

The complete P011 collision polynomial recovers the **multiset**

\[
\{\ell_1,\ldots,\ell_m\}
\]

but forgets their order.

Therefore the geometry quotient can be identified with one of the most basic classical combinatorial maps:

\[
\boxed{
\text{positive compositions}
\longrightarrow
\text{integer partitions}.
}
\]

This note records the exact finite state counts produced by that identification.

---

## 2. P022-SP01 — fixed `N,m`: compositions versus partitions

The number of ordered positive compositions of `N` into exactly `m` parts is

\[
\boxed{
C_{N,m}
=
\binom{N-1}{m-1}.
}
\]

This is exactly the number of final-observing ordered checkpoint schedules with `m` checkpoints.

Let

\[
p_m(N)
\]

be the classical number of integer partitions of `N` into exactly `m` positive parts.

The collision-polynomial inversion theorem gives a bijection

\[
\boxed{
\{\text{complete collision states at fixed }N,m\}
\longleftrightarrow
\{\text{partitions of }N\text{ into }m\text{ parts}\}.
}
\]

Hence

\[
\boxed{
|\operatorname{im}K_{N,m}|=p_m(N).
}
\]

The full ordered schedule space has size `C_(N,m)`, while the complete collision state space has size `p_m(N)`.

---

## 3. P022-SP02 — the fiber decomposition recovers the composition count

Take one partition with part multiplicities

\[
t_\ell.
\]

The order-repair theorem gives its ordered-geometry fiber size

\[
M_{\rm ord}
=
\frac{m!}{\prod_\ell t_\ell!}.
\]

Summing these multinomial fibers over all partitions of `N` into `m` parts must recover all compositions:

\[
\boxed{
\binom{N-1}{m-1}
=
\sum_{\lambda\vdash N\atop \ell(\lambda)=m}
\frac{m!}{\prod_j t_j(\lambda)!}.
}
\]

This identity is simply the partition of the ordered composition space into collision-polynomial fibers.

So the quotient is fully accounted for:

\[
\boxed{
\text{composition count}
=
\sum
\text{order-repair fiber sizes over partition states}.
}
\]

---

## 4. P022-SP03 — all final-observing schedules

If the checkpoint count `m` is allowed to vary from `1` to `N`, every subset of the `N-1` internal boundaries chooses one positive composition. Therefore

\[
\boxed{
\#\{\text{all final-observing ordered schedules}\}
=2^{N-1}.
}
\]

The complete collision polynomial reveals `m` and the partition itself, so distinct collision states across all final-observing schedules are indexed by ordinary integer partitions of `N`:

\[
\boxed{
\#\{\text{complete collision states}\}
=p(N).
}
\]

Thus the entire final-observing schedule quotient is

\[
\boxed{
2^{N-1}\text{ ordered compositions}
\longrightarrow
p(N)\text{ partition states}.
}
\]

The project-specific content is the proof that the complete P011 collision state realizes exactly this quotient for Barlow checkpoint geometry; the composition/partition counts themselves are classical.

---

## 5. P022-SP04 — arbitrary selected-layer schedules with hidden tail

Now allow an arbitrary subset of layers

\[
\{1,\ldots,N\}
\]

to be observed, including the empty set and schedules that do not observe the final layer.

There are

\[
\boxed{2^N}
\]

such checkpoint subsets.

Let `L` be the last observed layer, with `L=0` for the empty schedule.  Then:

- the hidden tail length is `u=N-L`;
- the observed prefix segmentation is a positive composition of `L` when `L>0`;
- the complete collision polynomial recovers `u` and the **partition** of `L` given by the segment multiset.

Therefore the complete collision-polynomial states are indexed exactly by

\[
\boxed{
(u,\lambda),
\qquad
u=N-|\lambda|,
\qquad
\lambda\vdash L,
\quad0\le L\le N.
}
\]

and their number is

\[
\boxed{
I_N
=
\sum_{L=0}^{N}p(L),
}
\]

with `p(0)=1` representing the empty checkpoint schedule.

So the arbitrary-checkpoint quotient is

\[
\boxed{
2^N\text{ ordered checkpoint subsets}
\longrightarrow
\sum_{L=0}^{N}p(L)
\text{ complete collision states}.
}
\]

---

## 6. Average order ambiguity over collision states

If complete collision states rather than microscopic schedules are weighted equally, the mean number of ordered final-observing geometries represented by one fixed-`N,m` collision state is

\[
\boxed{
\frac{\binom{N-1}{m-1}}{p_m(N)}.
}
\]

Across all arbitrary checkpoint subsets it is

\[
\boxed{
\frac{2^N}{\sum_{L=0}^{N}p(L)}.
}
\]

These are exact rational state-count ratios.

They are **not** microscopic-weighted averages.  As elsewhere in P022, quotient-state weighting and source-state weighting are different observation languages and should remain distinguished.

---

## 7. Relation to collision completeness

The map

\[
\text{ordered schedule}
\to
K_O(t)
\]

therefore has a particularly transparent structure:

1. ordered segment sequence becomes a composition;
2. commutative fiber convolution forgets order;
3. the complete collision polynomial still recovers the resulting partition and hidden tail exactly;
4. low-order collision shadows may then merge distinct partitions again.

So there are two qualitatively different losses:

\[
\boxed{
\text{composition}
\to
\text{partition}
\to
\text{low-order collision shadow}.
}
\]

The first loss is **ordering information**.  The second loss is **fiber-profile information**.

Their repairs are different:

- order repair uses one state among `m!/prod t_ell!` possibilities;
- low-order repair requires additional collision/fiber information and can involve entirely different segment multisets.

This separation is another concrete example of typed precision.

---

## 8. Prior-art boundary

Integer compositions, integer partitions, the counts `C(N-1,m-1)`, `p_m(N)`, `p(N)`, and their classical asymptotics are established mathematics.

P022 does not claim those combinatorial facts as new.

The project-specific result is the exact identification of the Barlow complete collision-polynomial quotient with the composition-to-partition map, including hidden-tail routing and the previously proved inverse from collision data to partition geometry.

---

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_schedule_partition.py`;
- `tests/test_p022_barlow_schedule_partition.py`.

The tests enumerate small positive compositions and checkpoint subsets, verify that distinct complete collision-polynomial states are counted by the corresponding partition numbers, and verify the exact state-count ratios.
