# R035 — Polygonal Refinement Endpoint Dynamics

Researcher-ID: `EM-R035-6F2A91`  
Task: `RS-R035-POLYGONAL-REFINEMENT-ENDPOINT-DYNAMICS`  
Arm: `PROJECT`  
Taskbook source: `58346f6a473f681730f3ffc2f70ff2d5de899a14`  
Status: `L1/L2 RESEARCH SEMANTIC CHECKPOINT / DRAFT / NOT CANONICAL`

## Return classification

`POLYGONAL_ENDPOINT_DYNAMICS_STRUCTURE_FOUND / SHARP_FACTOR_BOUNDARIES_AND_EXACT_CARRIERS_FROZEN / PELL_COMPONENT_PRIOR_ART_ROOTED / NOT_CANONICAL`

The main result is an exact decomposition into a monotone lower-index map, an exact-hit bit, and ordered width-one child blocks, followed by two sharp factor classifications:

1. **Universal singleton-interval theorem.** For fixed `r>=1`, every singleton root `{k0}`, every `s>=3`, and every time has an integer-interval index support iff `r<=4`.
2. **Universal no-recoalescence theorem.** Distinct parents have disjoint endpoint child sets for every `s>=3` iff `r=1` or `r>=4`.

Thus `r=4` is a genuine arithmetic crossing point: the largest factor with universal singleton interval dynamics and the first nontrivial factor with universal parent-block separation.

The fixed-multiple exact-hit subproblem reduces to a generalized Pell equation. That component is prior-art rooted; the support-dynamical threshold, recoalescence, carrier and cardinality results below are the task-specific residue.

---

## 1. Frozen object and coordinates

Write

\[
a=s-2\ge1,\qquad c=s-4=a-2,
\]

so

\[
P_s(k)=P(k)=\frac{ak^2-ck}{2}=k+\frac{ak(k-1)}2,
\]

and the exact consecutive gap is

\[
g_k=P(k+1)-P(k)=ak+1.
\]

For fixed `r>=1`, define

\[
F(k)=L_s(rP_s(k)).
\]

Let `h(k)=1` when `rP(k)=P(F(k))` and `h(k)=0` otherwise, with `epsilon(k)=1-h(k)`. Then the complete child block of parent `k` is

\[
B(k)=E_s(rP_s(k))=\{F(k),\ldots,F(k)+\varepsilon(k)\}.
\]

Every parent block therefore has width 0 or 1. The set dynamics is

\[
S_{t+1}=\bigcup_{k\in S_t}B(k),\qquad S_0=\{k_0\}.
\]

Actual-value support remains distinct: `A_t={P_s(k):k in S_t}`.

### Discriminant coordinate

Define

\[
D_s(n)=c^2+8an,\qquad z_k=2ak-c.
\]

Then

\[
D_s(P_s(k))=z_k^2,
\]

and the exact lower index is

\[
L_s(n)=\left\lfloor\frac{c+\sqrt{c^2+8an}}{2a}\right\rfloor.
\]

The implementation uses integer `isqrt` plus defensive exact inequality correction only; theorem-critical paths do not use floating point.

For positive `k`, the real inverse coordinate is

\[
\phi(k)=\frac{c+\sqrt{r z_k^2-(r-1)c^2}}{2a},\qquad F(k)=\lfloor\phi(k)\rfloor.
\]

---

## 2. Exact executable surface

Artifacts:

- `experiments/r035_polygonal_dynamics.py` — exact oracle, incidence, cardinality, Pell residual and structural helpers;
- `experiments/r035_holdout.py` — independent lower-index implementation via monotone integer doubling/binary search;
- `tests/test_r035_polygonal_dynamics.py` — focused regression and mutation/boundary tests.

Final local validation:

- `25` focused unittest cases: PASS;
- independent holdout: PASS, `321,118` counted checks;
- full suggested one-step sanity window `3<=s<=12`, `1<=r<=40`, `0<=k<=200`: all `80,400` triples crosschecked against the independent oracle;
- holdout also reaches `n<=10^20`, `k<=10^8`, `s<=150`, `r<=200` on disjoint/larger parameter regions.

These checks guard the executable realization; the universal claims below are proof-backed, not inferred from finite scans.

---

## 3. Strict lower map and jump bound

### Theorem 3.1

For every `s>=3`, `r>=1`, `k>=0`,

\[
1\le F(k+1)-F(k)\le r.
\]

Sketch: with `m=F(k)`, monotonicity gives `m>=k`; moreover

\[
P(rk)-rP(k)=\frac{ar(r-1)k^2}{2}\ge0,
\]

so `m<=rk`. Hence

\[
g_m=am+1\le ark+1\le r(ak+1)=rg_k.
\]

From `P(m)<=rP(k)` this gives `P(m+1)<=rP(k+1)`, so the next lower index is at least `m+1`. Conversely, `rP(k)<P(m+1)` and the next `r` polygonal gaps after `m` sum to strictly more than `rg_k`; therefore `F(k+1)<=m+r`.

Consequences: `F` is strictly increasing and injective, and every finite parent set contributes distinct lower children, so support cardinality never decreases.

---

## 4. Local overlap/recoalescence law

Because `F` is strictly increasing and each parent block has diameter at most one:

- non-adjacent numerical parents cannot share a child;
- adjacent parents `k,k+1` overlap iff the left parent is non-hit and `F(k+1)-F(k)=1`;
- the shared child is exactly `F(k)+1`;
- triple collisions are impossible.

For finite support `S`, let:

- `N=|S|`;
- `H` = number of exact-hit parents in `S`;
- `C` = duplicate-edge excess, equivalently the number of local two-parent overlap events.

Then exactly

\[
|D(S)|=2N-H-C.
\]

This killed the initial rough “persistent binary doubling” expectation and replaced it with an exact accounting identity.

---

## 5. Positive jump lower bound and universal no-recoalescence classification

For `k>=1`, differentiation of `phi` gives

\[
\phi'(k)=\frac{r z_k}{\sqrt{r z_k^2-(r-1)c^2}}\ge\sqrt r.
\]

Therefore

\[
F(k+1)-F(k)\ge\lfloor\sqrt r\rfloor.
\]

For `r>=4`, every positive lower-map jump is at least 2, so adjacent width-one parent blocks are disjoint. The origin block `{0}` is also disjoint. For `r=1`, the dynamics is the identity.

The remaining two factors really do recoalesce:

- triangular `s=3`, `r=2`, parents `3,4`: `B(3)={4,5}`, `B(4)={5,6}`;
- triangular `s=3`, `r=3`, parents `8,9`: `B(8)={14,15}`, `B(9)={15,16}`.

Hence:

> **Distinct parent blocks are universally disjoint iff `r=1` or `r>=4`.**

For `r>=4`, the child relation is reverse-functional: every child has at most one parent globally. Thus set-union recoalescence does not erase parent-index genealogy in this regime.

---

## 6. Exact interval dynamics for r=2 and r=3

### r=2

Universal jump bound gives `Delta F in {1,2}`. If `k>=1` is an exact hit, `2P(k)=P(m)`, then `m>k` and

\[
P(m+2)-P(m)=2am+a+2>2ak+2=2g_k,
\]

so `F(k+1)=m+1`. Therefore every **positive** integer parent interval maps to an integer interval.

### r=3

A parity estimate yields a sharper lower bound on `F(k)` and implies `Delta F<=2`. If `k>=2` is an exact hit, one further comparison shows the next jump is 1; `k=1` is checked separately. Therefore every **positive** integer parent interval again maps to an interval.

The positivity hypothesis is real: the artificial support `{0,1}` at `(s,r)=(3,3)` maps to `{0,2}`. This does not affect default singleton dynamics because `k0=0` is fixed and positive roots never reach zero.

Thus for default positive roots under `r=2,3`, the exact future support can be carried by two integers `(ell_t,u_t)` with

\[
S_t=[\ell_t,u_t].
\]

---

## 7. Critical r=4 is completely explicit

Identity:

\[
P_s(2k)-4P_s(k)=(s-4)k.
\]

For `k>0`:

- `s=3`: `B(k)={2k,2k+1}`;
- `s=4`: `B(k)={2k}`;
- `s>=5`: `B(k)={2k-1,2k}`.

Therefore for `k0>0`:

- triangular: `S_t=[2^t k0, 2^t(k0+1)-1]`;
- square: `S_t={2^t k0}`;
- `s>=5`: `S_t=[2^t(k0-1)+1,2^t k0]`.

`k0=0` remains fixed.

This makes `r=4` an exact dyadic critical world, not merely an empirical boundary.

---

## 8. Sharp universal interval classification

Define `UI(r)` to mean: for every `s>=3`, every singleton `k0`, and every time, `S_t` is an integer interval.

The previous sections prove `UI(r)` for `r=1,2,3,4`.

For every `r>=5`, choose

\[
s=r+1,\qquad k_0=1.
\]

Since `P_s(1)=1` and `P_s(2)=s=r+1`, parent 1 has `B(1)={1,2}`, so `S_1={1,2}`. But

\[
rP_s(2)=r(r+1),\qquad P_s(4)=6r-2,
\]

and for `r>=5`,

\[
r(r+1)-(6r-2)=r^2-5r+2>0.
\]

Therefore parent 2's lower child is at least 4, while parent 1 again contributes `{1,2}`. Thus `S_2` misses index 3.

Hence:

> **`UI(r)` holds iff `1<=r<=4`.**

The smallest early witness found during search was triangular `(s,r,k0)=(3,5,1)`:

`{1} -> {2,3} -> {5,7,8}`.

---

## 9. Square control world s=4

Here `P_4(k)=k^2`.

If `r=q^2` is square, every positive parent is an exact hit and

\[
B(k)=\{qk\}.
\]

Any finite support simply scales by `q`.

If `r` is nonsquare, there are no positive exact hits and

\[
B(k)=\{\lfloor\sqrt r\,k\rfloor,\lfloor\sqrt r\,k\rfloor+1\}.
\]

For nonsquare `r>=5`, no exact hits plus no recoalescence implies exact binary cardinality growth from a positive singleton:

\[
|S_t|=2^t.
\]

---

## 10. Exact-hit Pell surface

Exact equality `rP_s(k)=P_s(m)` is equivalent to

\[
z_m^2-rz_k^2=(1-r)c^2,
\]

with congruence

\[
z_m,z_k\equiv -c\pmod{2a}.
\]

Consequences:

- `r=1`: every parent is a hit;
- `r=q^2>1`, `c=0` (`s=4`): every positive parent is a hit with `m=qk`;
- `r=q^2>1`, `c!=0`: factorization
  `(z_m-qz_k)(z_m+qz_k)=-(q^2-1)c^2` gives only finitely many positive hit states;
- nonsquare `r`, `c=0`: no positive hits;
- nonsquare `r`, `c!=0`: a congruence-compatible positive hit generates infinitely many through a suitable positive Pell unit power; hence the positive hit set is empty or infinite.

This fixed-multiple polygonal/Pell component overlaps classical/prior work and is not claimed as R035-new. Its role here is to classify unary nodes inside the endpoint-support dynamics.

For `r>=4`, because there is no recoalescence,

\[
N_{t+1}=2N_t-H_t,
\]

so exact-hit/Pell nodes are the only mechanism suppressing binary support growth.

---

## 11. Self-loops, drift, and absence of positive finite cycles

For `r>1`, a positive lower self-loop `F(k)=k` is equivalent to

\[
(r-1)P(k)<g_k.
\]

Since for `k>=3`, `P(k)-g_k>0`, the exact classification is:

- `k=1` with `r<s`;
- `k=2` with `r=2` and `s>=4`.

These are lower-map self-loops, not fixed singleton supports: when the target is non-polygonal the upper endpoint is also present.

For `r>1`, any finite support with positive maximum has strictly increasing maximum after one step. Therefore no nontrivial finite positive fixed support or periodic support exists. The singleton `{0}` is fixed; for `r=1`, every support is fixed.

---

## 12. Eventual two-letter jump alphabet

For `r>1`, `s!=4`,

\[
\phi''(k)=-\frac{2ar(r-1)c^2}{(r z_k^2-(r-1)c^2)^{3/2}}<0,
\]

so `phi'` decreases to `sqrt(r)`. Let `q=floor(sqrt(r))`. Eventually the real increment `phi(k+1)-phi(k)` lies strictly between `q` and `q+1`, hence

\[
F(k+1)-F(k)\in\{q,q+1\}.
\]

For `s=4`, `phi(k)=sqrt(r)k` exactly and the same two-letter statement holds for every positive `k` (one letter when `r` is square).

The oracle includes an integer-only sufficient transient `eventual_two_jump_start(s,r)` based on

\[
r((q+1)^2-r)z_k^2>(q+1)^2(r-1)c^2.
\]

A stronger exact Sturmian/generalized-Beatty identification for all `s!=4` is **not claimed**.

---

## 13. Bounded atlas observations (not universal theorems)

The full one-step taskbook window contains `80,400` `(s,r,k)` triples. Adjacent-parent overlap counts observed there were:

- `r=2`: `1161`;
- `r=3`: `523`;
- `r=1` and all `r>=4`: `0`.

A depth-10 sample over `s=3..12`, `r=1..40`, `k0=0..20` contained `8,400` trajectories and `92,400` levels:

- `1,280` trajectories stayed interval through depth 10;
- `7,120` fragmented by depth 10;
- first-gap depth counts: depth 2 = `6,618`, depth 3 = `457`, depth 4 = `45`;
- maximum observed support cardinality = `1024`.

These are bounded observations only. They are not used to prove the sharp classifications.

---

## 14. Representation boundary

### r=1
Identity carrier.

### r=2,3
For default positive singleton roots, exact support is an interval. The two endpoint integers `(ell,u)` are a future-sufficient lossless carrier for this declared dynamical family. Multiplicity/provenance is not retained.

### r=4
Closed-form dyadic interval/singleton carriers above.

### r>=5
Universal interval compression is impossible. However parent child blocks are globally separated, so the support is a forest of unary/binary nodes with unique parent per child. For `r>=4`, exact genealogy can be reconstructed from the current index support and the known one-step relation because reverse functionality holds.

This is task-specific arithmetic structure. Existing `EnterpriseMath/Relation/BranchRecoalescence.lean` roots the generic exact relation/direct-image/union semantics but does not supply these polygonal separation thresholds.

---

## 15. Productive failures and narrowed claims

1. **Persistent binary doubling** — killed by `r=2,3` recoalescence; replaced by `|D(S)|=2|S|-H-C`.
2. **All-r interval support** — killed at `r=5`; strengthened to the exact iff `r<=4` classification with a uniform counterexample family for every `r>=5`.
3. **Origin-inclusive r=2,3 interval-image theorem** — narrowed to positive parent intervals; `{0,1}` at `(3,3)` is the minimal boundary witness found.
4. **Novel Pell theorem family** — prior-art absorbed after independent discovery; retained only as a rooted arithmetic component of the new support dynamics.

The chronological discovery order is preserved separately in `EXPLORATION_TRACE.md`; it was not rewritten as if the final theorem decomposition were known in advance.

---

## 16. Prior-art rooting

After the initial independent checkpoint and arithmetic discovery, public prior art was checked.

- Chahal, Griffin, Priddis, *When are Multiples of Polygonal Numbers again Polygonal Numbers?* (`arXiv:1806.07981`): **ROOTED COMPONENT** for fixed-multiple polygonal equalities, generalized Pell reduction, congruence conditions, triangular infinite families and higher-polygonal compatible-solution propagation.
- Rozikov, Sattarov, Usmonov, *The dynamical system generated by the floor function floor(lambda x)* (`arXiv:1503.07129`): **RELATED CONTROL PRIOR ART** for deterministic floor-map dynamics.
- Allouche, Dekking, *Generalized Beatty sequences and complementary triples* (`arXiv:1809.03424`): **RELATED REPRESENTATION PRIOR ART** for Beatty/generalized-Beatty and two-letter difference words.
- `EnterpriseMath/Relation/BranchRecoalescence.lean`: **PROJECT ROOTED GENERIC SEMANTICS** for relational direct image, support preservation and exact union/recoalescence.

Surviving R035-specific residue includes the strict/jump bounds for this polygonal lower map, the exact factor classification of recoalescence, the iff `r<=4` universal interval law, the complete `r=4` orbit formulas, the support-cardinality law, self-loop/cycle boundary, separated-forest carrier, and eventual two-letter jump bound.

---

## 17. Evidence ledger

**Exact theorem/proof:** Sections 3–12 principal statements and the two iff factor classifications.

**Executable exact evidence:** integer oracle plus 25 tests.

**Independent holdout:** monotone integer binary-search oracle, 321,118 counted checks, PASS.

**Bounded atlas only:** Section 13 observations.

**Prior-art rooted fact:** fixed-multiple generalized Pell mechanism and related floor/Beatty background.

**Not claimed:** a global closed form for every `r>=5`; a universal support-cardinality exponent for nonsquare polygonal worlds; a full Sturmian classification of the transient/non-square jump word; canonical Enterprise Math integration.

---

## 18. Open frontiers

- classify reachable exact-hit/Pell-node statistics along a fixed positive root tree;
- determine asymptotic support-cardinality exponents for nonsquare `r>=5` outside the square control world;
- find the minimal future-sufficient run/gap carrier in the separated-forest regime;
- sharpen the sufficient transient `K(s,r)` for the two-letter jump alphabet;
- classify long consecutive unary exact-hit chains;
- formalize the principal arithmetic statements in Lean as a separate task if promoted.

---

## 19. Taskbook completion check

1. exact oracle credible: **YES** — integer inversion plus independent integer binary-search holdout;
2. conjecture -> attack -> survive/kill/narrow: **YES** — multiple productive failures and two exact iff replacements;
3. main findings independently held out: **YES** — 321,118 counted checks on disjoint/larger ranges plus full one-step sanity window;
4. exploration trace and evidence boundaries complete: **YES**.

`hard_block = NONE`

`CI_NOT_REQUIRED_FOR_RESEARCH`

This checkpoint remains `DRAFT / NOT CANONICAL`; canonical integration is outside R035.
