# P022 — Barlow Precision Fibers and Optimal Checkpoint Scheduling

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE QUOTIENT SPECTRUM / NOVELTY_UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Cross-route relation: exact P022 specialization of P011 fiber/collision spectra and P023/P024 task-relative quotient safety

## 1. The stacking-prefix quotient has an exact microscopic fiber structure

A length-`N` close-packed stacking prefix is a microscopic word

\[
\sigma=(\sigma_1,\ldots,\sigma_N)
\in\{-1,+1\}^N.
\]

For the complete coordinate-sensitive root-to-layer-`N` distance language, the preceding Barlow theorem showed that the entire word may be replaced exactly by one integer

\[
\delta_N=\sum_{j=1}^{N}\sigma_j.
\]

The legal quotient is therefore

\[
q_N:\{-1,+1\}^N\to\{-N,-N+2,\ldots,N\},
\qquad
q_N(\sigma)=\delta_N.
\]

This note asks a different but equally important precision question:

> **how many microscopic histories have been legally collapsed into each observable state?**

The answer is completely binomial.

## 2. P022-PF01 — final-imbalance fiber spectrum

If

\[
\delta=2k-N,
\]

then a word has imbalance `delta` exactly when it contains `k` plus signs and `N-k` minus signs.

Therefore

\[
\boxed{
|q_N^{-1}(\delta)|=\binom Nk.}
\]

The complete quotient-fiber spectrum is

\[
\boxed{
\left(
-N:\binom N0,
-N+2:\binom N1,
\ldots,
N:\binom NN
\right).}
\]

The fibers are highly nonuniform. Extreme drift states have fiber size one, while balanced drift states have the largest fibers.

Thus the same exact future language collapses many more microscopic words near zero drift than near constant drift.

## 3. P022-PF02 — exact pair-collision count

Count ordered microscopic word pairs with the same final imbalance:

\[
\sum_{k=0}^{N}\binom Nk^2.
\]

Vandermonde's identity gives

\[
\boxed{
\sum_{k=0}^{N}\binom Nk^2
=\binom{2N}{N}.}
\]

Among these ordered pairs, `2^N` lie on the diagonal and represent identical microscopic words.

Therefore the number of **distinct unordered word pairs** identified by the final-imbalance quotient is

\[
\boxed{
C_N
=\frac{\binom{2N}{N}-2^N}{2}.}
\]

This is exactly the order-two collision statistic of the quotient map.

More generally, the P011-style order-`r` collision count is

\[
\boxed{
J_r(N)
=\sum_{k=0}^{N}
\binom{\binom Nk}{r}.}
\]

No new generic irreversibility theory is claimed here; this is a closed Barlow specialization of the existing finite fiber/collision framework.

## 4. Selected-layer future language

Now let the future language observe only the prefix imbalances at selected layers

\[
0<k_1<\cdots<k_m\le N.
\]

Define constrained segment lengths

\[
\ell_1=k_1,
\qquad
\ell_j=k_j-k_{j-1}\quad(j>1),
\]

and an unobserved final tail

\[
u=N-k_m
\]

if the last selected layer is not `N`.

The observation is

\[
O_J(\sigma)
=(\delta_{k_1},\ldots,\delta_{k_m}).
\]

Because disjoint stacking segments are independent finite words, every fiber factorizes segment by segment.

## 5. P022-PF03 — image size of a selected checkpoint language

A segment of length `ell` can have exactly

\[
\ell+1
\]

possible net imbalances.

Segment increments determine the checkpoint trajectory bijectively. Therefore

\[
\boxed{
|O_J(\{-1,+1\}^N)|
=\prod_{j=1}^{m}(\ell_j+1).}
\]

The unobserved tail creates no new observation coordinate.

Special cases:

- no queried layer: image size `1`;
- only final layer: image size `N+1`;
- every prefix layer queried: image size `2^N`, so the observation is injective.

## 6. P022-PF04 — exact fiber size for one observed trajectory

Suppose the observed checkpoint imbalances are

\[
d_1,\ldots,d_m,
\qquad d_0=0.
\]

The `j`th segment has net increment

\[
h_j=d_j-d_{j-1}.
\]

The number of microscopic words realizing that segment is

\[
\binom{\ell_j}{(\ell_j+h_j)/2}
\]

when the parity/range constraints are legal, and zero otherwise.

The final unobserved tail is arbitrary. Hence

\[
\boxed{
|O_J^{-1}(d_1,\ldots,d_m)|
=2^u
\prod_{j=1}^{m}
\binom{\ell_j}{(\ell_j+h_j)/2}.}
\]

This formula gives the exact microscopic ambiguity of every represented precision state.

## 7. P022-PF05 — global equal-observation pair count

Instead of fixing one observed trajectory, sum squared fiber sizes over all trajectories.

For one segment of length `ell`, Vandermonde gives

\[
\sum_h
\binom{\ell}{(\ell+h)/2}^2
=\binom{2\ell}{\ell}.
\]

Segments factor, and the unobserved tail contributes `4^u` ordered pairs. Therefore

\[
\boxed{
P_J
:=\#\{(\sigma,\tau):O_J(\sigma)=O_J(\tau)\}
=4^u\prod_{j=1}^{m}\binom{2\ell_j}{\ell_j}.}
\]

Subtract the `2^N` identical pairs and divide by two:

\[
\boxed{
C_J
=\frac{
4^u\prod_j\binom{2\ell_j}{\ell_j}-2^N
}{2}.}
\]

This is the exact number of distinct microscopic word pairs collapsed by the declared checkpoint language.

The formula interpolates continuously between the two extremes:

### Only the final layer

\[
C_J
=\frac{\binom{2N}{N}-2^N}{2}.
\]

### Every layer

Every segment has length `1`, so

\[
P_J=2^N
\]

and

\[
\boxed{C_J=0.}
\]

No microscopic history is collapsed.

## 8. Query density is not enough; checkpoint placement matters

Fix `N` and a number `m` of checkpoint observations.

Even with the same observation count, different placements produce different segment lengths and therefore different collision ambiguity.

The relevant factor is the central binomial sequence

\[
f(n)=\binom{2n}{n}.
\]

Its consecutive ratio is

\[
\boxed{
\frac{f(n)}{f(n-1)}
=4-\frac2n,}
\]

which is strictly increasing in `n`.

This one integer monotonicity identity completely solves the scheduling problem.

## 9. P022-PF06 — balanced checkpoints minimize ambiguity when the final layer must be visible

Assume `m>=1` checkpoints are allowed and layer `N` must be among them.

Then all constrained segment lengths are positive and satisfy

\[
\ell_1+\cdots+\ell_m=N.
\]

Suppose two segment lengths satisfy

\[
a\ge b+2.
\]

Compare the product before and after transferring one step from the longer segment to the shorter one:

\[
\frac{f(a)f(b)}{f(a-1)f(b+1)}
=
\frac{4-2/a}{4-2/(b+1)}
>1.
\]

Therefore balancing the pair strictly reduces the equal-observation pair count.

Iterating this exchange proves:

\[
\boxed{
\text{collision ambiguity is minimized exactly when all segment lengths differ by at most one.}}
\]

Write

\[
N=am+r,
\qquad0\le r<m.
\]

Then the optimal segment multiset is

\[
\boxed{
\underbrace{a,\ldots,a}_{m-r},
\underbrace{a+1,\ldots,a+1}_{r}.}
\]

Any ordering of these segment lengths has the same collision count. A canonical schedule is obtained by placing the shorter segments first.

The minimum ordered equal-observation pair count is

\[
\boxed{
P_{\min}
=inom{2a}{a}^{m-r}
\binom{2a+2}{a+1}^{r}.}
\]

Thus near-uniform checkpoint spacing is not a heuristic recommendation. It is the exact optimizer for this quotient-collision objective.

## 10. P022-PF07 — most uneven final-visible schedule maximizes ambiguity

Under the same constraint that the final layer is visible, strict log-convexity gives the reverse extremum as well.

Ambiguity is maximized by making `m-1` segments as short as possible and placing the remaining length into one segment:

\[
\boxed{
(1,\ldots,1,N-m+1).}
\]

Then

\[
\boxed{
P_{\max}^{\mathrm{final}}
=2^{m-1}
\binom{2(N-m+1)}{N-m+1}.}
\]

So two schedules with the same number of checkpoints can differ substantially in how many histories they legally collapse.

## 11. P022-PF08 — if the final layer need not be observed, front-loading is worst

Now allow the last checkpoint to occur before `N`, leaving an unobserved tail of length `u`.

That tail contributes

\[
4^u
\]

to the ordered equal-observation pair count.

If one hidden tail step is moved into the last observed segment of current length `ell`, the ambiguity factor changes by

\[
\frac{f(\ell+1)/f(\ell)}{4}
=
1-\frac{1}{2(\ell+1)}
<1.
\]

So observing later always reduces ambiguity.

For a fixed number `m` of checkpoints, the maximum ambiguity occurs when the checkpoints are the first `m` layers, leaving the largest possible invisible tail `N-m`:

\[
\boxed{
P_{\max}
=2^m4^{N-m}.}
\]

Thus, for reconstructing an entire finite prefix, early observations cannot compensate for leaving the terminal part completely unseen.

## 12. A finite precision-scheduling interpretation

This Barlow quotient supplies an exact toy model for precision placement.

- each queried layer is a finite observation;
- unqueried interface identities are microscopic detail;
- quotient fibers count how much detail remains legally invisible;
- collision counts quantify global ambiguity;
- checkpoint placement changes ambiguity even at fixed observation count.

The resulting design rule is precise:

> **for a fixed checkpoint budget and a final-state requirement, distribute observations as evenly as possible across the hidden evolution.**

This conclusion is specific to the present ±1 prefix-imbalance language. It should not be promoted as a generic engineering sampling theorem without proving analogous log-convex fiber structure in the target system.

## 13. Cross-route meaning

### P011

The binomial fibers give a closed functional collision spectrum for one exact quotient map. P011 remains the mother home for generic fiber/collision statistics.

### P023/P024

The checkpoint set is part of the future observation language. Changing it changes the coarsest legal quotient and its fiber structure. The extreme `every layer` case makes the quotient injective.

### P022

P022 owns the concrete close-packed stacking specialization and its exact checkpoint optimization.

## 14. Executable assets

Added:

- `src/enterprise_math/p022_barlow_precision_fibers.py`;
- `tests/test_p022_barlow_precision_fibers.py`.

The tests exhaustively compare fiber formulas against all short ±1 words, verify pair-collision formulas, and brute-force every checkpoint placement for small `N` to confirm the balanced/minimum and front-loaded/maximum scheduling theorems.
