# P018 — Finite-Precision Proof Calculus: Supplement 16

Status: `ACTIVE RESEARCH NOTE`  
Scope: labelled extended merger time, exact reconstruction of the kernel filtration, higher-subset merger times, reconstruction of the time-resolved P011 spectrum, and the boundary with P012 graph geometry  
Depends on: P010, P011, P012, P018-T129–T142, P020  
Prior-art boundary: hierarchy/dendrogram/ultrametric equivalences are established mathematics; see `docs/PRIOR_ART_P018_COALESCENCE.en.md`. This note studies the exact finite deterministic Enterprise Math interface and does not claim the abstract hierarchy-ultrametric correspondence as new.

---

## 1. Why the next step should reduce, not enlarge, the foundation

Supplement 15 left three time-resolved objects:

- the labelled kernel filtration, which records **who** has merged;
- pairwise first coalescence time `tau`, which records **when** a pair first merges;
- the P011 step collision polynomial, which records **how many** newly merged subsets occur at every order.

A natural but dangerous next move would be to introduce an independent first-merger time for every triple, quadruple, and higher finite set.

The correct question is instead:

> Does deterministic pairwise merger time already determine every higher common-fiber event?

It does.

---

## 2. Extended labelled merger time

For one deterministic endomap

\[
F:X\to X,
\]

define

\[
\boxed{
\bar\tau_F(x,y)
=
\begin{cases}
\min\{n:F^{[n]}x=F^{[n]}y\},&\text{if such }n\text{ exists},\\
\infty,&\text{otherwise}.
\end{cases}}
\]

The bar distinguishes this globally defined extended value from Supplement 14's finite `tau` restricted to one eventual-coalescence class.

It is a **labelled** object: the value remains attached to the ordered/unordered state pair `(x,y)`. Forgetting labels loses information.

---

## 3. P018-T143 — A finite subset merges exactly at its maximum pairwise merger time

Status: `PROVED / EXECUTABLE`

Let `A` be a finite nonempty subset of one eventual-coalescence class. Define its first common-fiber time by

\[
\tau_F(A)
=
\min\{n:\ F^{[n]}x=F^{[n]}y\ \text{for all }x,y\in A\}.
\]

For a singleton set define `tau_F(A)=0`.

Then

\[
\boxed{
\tau_F(A)
=
\max_{\{x,y\}\subseteq A}\tau_F(x,y).
}
\]

### Proof

Let the maximum pairwise time be `N`.

At time `N`, every pair in `A` has already coalesced, because equality persists under every later common deterministic suffix. Hence all images of elements of `A` are equal at time `N`, so

\[
\tau_F(A)\le N.
\]

Conversely, if all of `A` lies in one fiber at time `n`, every pair in `A` lies in that fiber at time `n`, so every pairwise first merger time is at most `n`. Therefore

\[
N\le\tau_F(A).
\]

The two inequalities give equality. ∎

### Consequence

There is no independent higher-order first-merger-time datum in deterministic dynamics:

\[
\boxed{
\text{all finite-subset merger times are determined by pairwise merger times.}
}
\]

This is a foundational minimization result, not a reason to create a new primitive object.

---

## 4. P018-T144 — Thresholding merger time reconstructs every kernel level exactly

Status: `PROVED / EXECUTABLE`

Recall

\[
K_n=\kerpair(F^{[n]}).
\]

By definition of first merger time and persistence of equality,

\[
\boxed{
(x,y)\in K_n
\iff
\bar\tau_F(x,y)\le n.
}
\]

Here `infinity <= n` is false.

Thus every finite-time kernel relation is recovered by thresholding one labelled extended merger-time object.

Similarly,

\[
\boxed{
(x,y)\in K_\infty
\iff
\bar\tau_F(x,y)<\infty,
}
\]

where `K_infinity` denotes eventual coalescence.

---

## 5. P018-T145 — The labelled merger-time matrix and the full kernel filtration are losslessly equivalent

Status: `PROVED STRUCTURAL EQUIVALENCE`

T144 reconstructs the entire increasing family

\[
K_0\subseteq K_1\subseteq\cdots
\]

from `bar tau`.

Conversely, given the labelled kernel filtration, recover

\[
\boxed{
\bar\tau_F(x,y)
=
\min\{n:(x,y)\in K_n\}
}
\]

when the set is nonempty, and `infinity` otherwise.

Therefore

\[
\boxed{
\text{labelled kernel filtration}
\quad\longleftrightarrow\quad
\text{labelled extended pairwise merger-time matrix}
}
\]

is a lossless change of representation.

This does **not** make `bar tau` ontologically more primitive than Pair/kernel logic. Pair/kernel remains the subtraction-free static relation; `bar tau` is a compact temporal encoding of the whole filtration.

---

## 6. P018-T146 — The proposed labelled higher-order time complex contains no new deterministic time information

Status: `PROVED NEGATIVE / MINIMALITY RESULT`

Suppose one attempts to store, for every finite nonempty subset `A`, its first common-fiber time `tau_F(A)`.

T143 gives

\[
\boxed{
\tau_F(A)
=
\operatorname{diam}_{\bar\tau_F}(A)
:=
\max_{x,y\in A}\bar\tau_F(x,y)
}
\]

whenever the value is finite, with `infinity` if `A` crosses eventual-coalescence components.

Hence the entire labelled higher-order merger-time complex is a deterministic function of the pairwise matrix.

So P018-Q109 is resolved negatively in the sense relevant to foundational minimality:

> a separate higher-order time object is unnecessary for deterministic common-fiber history; pairwise labelled merger time already determines it.

Higher-order **counts** remain useful observables, but they are not independent merger-time ontology.

---

## 7. P018-T147 — P011 degree-k collision counts are threshold counts of subset merger time

Status: `PROVED / EXECUTABLE`

Fix a finite labelled observation set `H`. At time `n`, a `k`-subset `A` contributes to P011's `J_k(F^[n]|_H)` exactly when all of `A` lies in one fiber of `F^[n]`.

By T143–T144, this is equivalent to

\[
\tau_F(A)\le n.
\]

Therefore

\[
\boxed{
J_k(F^{[n]}|_H)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)\le n\}.
}
\]

Taking the difference of two consecutive times gives the exact first-merger distribution:

\[
\boxed{
[t^k]\Delta_n(t)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)=n\}.
}
\]

This resolves P018-Q110 for every finite `k`, not only for pairs.

At `k=2`, it reduces to the number of labelled unordered pairs whose pairwise `tau` equals `n`.

---

## 8. P018-T148 — The labelled pairwise merger-time matrix reconstructs the complete time-resolved P011 spectrum

Status: `PROVED SYNTHESIS / EXECUTABLE`

By T143, every subset time is the maximum of its pairwise entries. By T147, P011 coefficients are counts of subsets whose maximum pairwise entry lies below a time threshold.

Therefore, on a finite labelled observation set `H`, the matrix

\[
\boxed{
(\bar\tau_F(x,y))_{x,y\in H}
}
\]

reconstructs:

1. every finite-time kernel partition;
2. every first-merger time of every finite subset;
3. every `J_k` at every time;
4. every step increment polynomial `Delta_n(t)`;
5. the final stabilization collision spectrum whenever P020 finite saturation applies.

Thus the earlier three-way language

`kernel = who; tau = when; Delta K = how many`

can now be refined:

- the **labelled temporal structure** is already complete at pairwise `bar tau`;
- the kernel filtration is its threshold representation;
- P011 spectra are aggregate integer observables derived from it.

---

## 9. P018-C12 — The collision-spectrum trajectory does not recover labelled merger time

Status: `COUNTEREXAMPLE / INFORMATION BOUNDARY`

Let the labelled finite state set be

\[
H=\{0,1,2,3\}.
\]

Consider two deterministic maps:

\[
F(1)=0,
\quad F(0)=0,
\quad F(2)=2,
\quad F(3)=3,
\]

and

\[
G(2)=0,
\quad G(0)=0,
\quad G(1)=1,
\quad G(3)=3.
\]

After one step, both maps have fiber-size multiset

\[
\{2,1,1\}
\]

and remain fixed thereafter. Hence their complete time trajectories of P011 collision polynomials are identical.

But their labelled first-merger matrices differ:

- under `F`, pair `{0,1}` merges at time `1` while `{0,2}` never merges;
- under `G`, pair `{0,2}` merges at time `1` while `{0,1}` never merges.

Therefore

\[
\boxed{
\text{time-resolved collision spectra do not recover labelled merger history.}
}
\]

This is why the aggregate P011 polynomial cannot replace the Pair/kernel layer.

---

## 10. P018-T149 — Global extended merger time is an extended ultrametric

Status: `PROVED / ESTABLISHED HIERARCHICAL PATTERN`

Allow the value `infinity`. Then on the whole state set:

\[
\bar\tau_F(x,x)=0,
\qquad
\bar\tau_F(x,y)=\bar\tau_F(y,x),
\]

and

\[
\boxed{
\bar\tau_F(x,z)
\le
\max(\bar\tau_F(x,y),\bar\tau_F(y,z)).
}
\]

with the usual order convention that every finite integer is below `infinity`.

If both right-hand terms are finite, Supplement 14 T130 proves the inequality. If either is infinite, the inequality is automatic.

Thus one deterministic many-to-one history induces a labelled **extended integer ultrametric** without first postulating a metric background.

Under P020, T132 identifies its finite-distance components exactly with fibers of the canonical stabilization map.

The hierarchy/ultrametric correspondence itself is established prior art and is not claimed as an Enterprise Math invention.

---

## 11. P018-C13 — P012 primitive graph distance and merger-time ultrametric are different structures

Status: `COUNTEREXAMPLE / DESIGN BOUNDARY`

Take the generic deterministic endomap on natural coordinates

\[
F(n)=n//2
\]

and, only for comparison, ordinary nearest-neighbor graph distance

\[
d_G(x,y)=|x-y|.
\]

Then

\[
d_G(8,9)=d_G(7,8)=1,
\]

but

\[
\tau_F(8,9)=1,
\qquad
\tau_F(7,8)=4.
\]

So equal graph distance need not imply equal merger time.

Moreover

\[
d_G(7,8)=1<7=d_G(0,7),
\]

while

\[
\tau_F(7,8)=4>3=\tau_F(0,7).
\]

Thus even monotone ordering between the two distances fails in general.

Important typing warning: repeated `n -> n//2` here is used only as a generic deterministic endomap for a counterexample. It is **not** interpreted as repeated application of one P005 typed scale-projection arrow; P009's type-erasure warning remains fully in force.

Therefore P012 graph distance and coalescence ultrametric must remain separate geometry routes until an explicit compatibility theorem supplies additional hypotheses.

---

## 12. Feedback into the bottom logic

The time/irreversibility layer can now be compressed without losing labelled deterministic information:

\[
\boxed{
\text{typed State + deterministic evolution}
\to
\text{Pair/kernel filtration}
\longleftrightarrow
\text{labelled extended merger-time matrix}
\to
\text{higher collision spectra}.
}
\]

The two middle objects have different roles:

- kernel filtration is weaker in prerequisites and keeps the relational meaning explicit;
- `bar tau` compresses the entire temporal filtration into one labelled integer/infinity coordinate object.

P011 statistics are downstream aggregates and therefore cannot replace the labelled layer.

This is a reduction of primitives: deterministic higher-order merger time does not require a new independent foundation.

---

## 13. Executable pressure tests

Added:

- `src/enterprise_math/merge_time_complex.py`
- `tests/test_merge_time_complex.py`

They test:

1. finite-subset first common time equals maximum pairwise merger time;
2. thresholding labelled pair times exactly reconstructs every tested kernel level;
3. degree-`k` collision increments equal the number of labelled `k`-subsets whose first common time is that step;
4. higher subset times add no information beyond pair times;
5. equal graph distance can have different coalescence time;
6. graph distance and merger time are not monotone in either obvious sense;
7. identical time-resolved collision spectra can hide different labelled merger histories.

---

## 14. Next questions

### P018-Q112 — Precision-atlas invariance of labelled merger time

When two legitimate mixed-radix charts represent the same underlying precision fiber, determine exactly when the induced labelled kernel filtration and merger-time matrix are conjugate/invariant.

### P018-Q113 — Operation scheduling versus merger-time geometry

Supplement 13 shows local defects can cancel while outer endpoints coincide. Determine how cancellation rearranges pairwise first-merger times and which properties survive chart changes.

### P018-Q114 — P017 certificate filtration

Test whether P017's local-support information can be organized as a finite filtration with a first certificate-validity time, while keeping every existing Legendre route intact and without identifying proof-state aggregation with physical irreversibility.

### P018-Q115 — Nondeterministic boundary

For relations or correspondences, a pair that meets once may later split along different branches. Determine which part of the kernel/merger-time compression survives and which must be replaced.

---

## 15. Current conclusion

For deterministic evolution, the labelled pairwise extended merger-time object is already complete for the entire time-dependent indistinguishability structure:

\[
\boxed{
K_n
=
\{(x,y):\bar\tau_F(x,y)\le n\}.
}
\]

Every finite higher-order common-fiber time is its pairwise diameter, and on finite observations

\[
\boxed{
[t^k]\Delta_n(t)
=
\#\{A\subseteq H:|A|=k,\ \tau_F(A)=n\}.
}
\]

So deterministic irreversibility does not require separate independent primitives for pair merger, higher merger time, and collision spectra. The labelled Pair/kernel history is primary; extended merger time is its lossless temporal coordinate; P011 spectra are finite integer summaries of that same structure.
