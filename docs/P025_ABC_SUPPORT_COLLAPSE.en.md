# P025 — ABC Radical-Support Collapse Pressure Test

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Scope: ordinary mathematics + Enterprise Math architecture pressure test  
Hard block: `NONE`

> This document does not claim a proof of the abc conjecture. No finite computation, empirical ranking, architectural analogy, or witness experiment may be promoted into an abc proof.

## 1. Entry point

For a positive integer `n`, define

\[
\operatorname{rad}(n)=\prod_{p\mid n}p.
\]

If the integer is represented by its valuation vector

\[
V(n)=(v_p(n))_p,
\]

then the radical retains only support:

\[
(v_p(n))_p\longmapsto (1_{v_p(n)>0})_p.
\]

Thus, in Enterprise Math language, `rad` is an aggressive multiplicative-support collapse: all repeated exponents are forgotten and only prime occurrence is retained.

Define the forgotten detail explicitly by

\[
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

Then

\[
\boxed{n=\operatorname{rad}(n)m(n)}
\]

exactly. We call `m(n)` the **multiplicity residual**. This decomposition is ordinary arithmetic, not a new project theorem.

## 2. P025-T01 — pairwise-disjoint support in a primitive abc triple

Assume

\[
a+b=c,\qquad \gcd(a,b)=1.
\]

Then

\[
\gcd(a,c)=\gcd(a,a+b)=1,
\qquad
\gcd(b,c)=\gcd(b,a+b)=1.
\]

Hence `a,b,c` are pairwise coprime and their prime supports are pairwise disjoint. Therefore

\[
\boxed{
\operatorname{rad}(abc)
=\operatorname{rad}(a)\operatorname{rad}(b)\operatorname{rad}(c)
}
\]

and

\[
\boxed{
abc=\operatorname{rad}(abc)m(a)m(b)m(c).
}
\]

### Architectural meaning

The difficulty of abc is not prime-support collision among the three inputs; primitivity already removes that collision. What remains is:

> **With completely separated support, how strongly can the additive relation `a+b=c` constrain the repeated prime multiplicities forgotten by radical collapse?**

This separates P025 from P017-style support-overlap counting.

## 3. P025-N01 — radical is not an exact addition-safe quotient

Consider

\[
(4,1),\qquad (8,1).
\]

Their radical input states are identical:

\[
(\operatorname{rad}(4),\operatorname{rad}(1))
=(2,1)
=(\operatorname{rad}(8),\operatorname{rad}(1)).
\]

But the radical output states differ:

\[
\operatorname{rad}(4+1)=5,
\qquad
\operatorname{rad}(8+1)=\operatorname{rad}(9)=3.
\]

Thus radical collapse fails P023's fiber-constant / operation-congruence criterion for binary addition:

\[
\boxed{\text{radical support alone does not make addition descend exactly.}}
\]

Any collapse-based account of abc therefore needs a weaker but controlled structure rather than an exact safe quotient.

## 4. P025-T02 — an exact integer defect coordinate for rational exponents

Fix positive integers

\[
u>v\ge1
\]

and define

\[
\boxed{
Q_{u,v}(a,b,c)
=\left\lceil
\frac{c^v}{\operatorname{rad}(abc)^u}
\right\rceil.
}
\]

For every positive integer `B`,

\[
\boxed{
Q_{u,v}(a,b,c)\le B
\iff
c^v\le B\operatorname{rad}(abc)^u.
}
\]

This is just the definition of positive integer ceiling division. Hence uniform boundedness of `Q_{u,v}` is exactly the corresponding rational-exponent abc bound, expressed using only integer powers, comparison, and division.

This does not strengthen abc; it replaces a real/logarithmic quality observable with an equivalent finite integer defect coordinate.

## 5. P025-T03 — high quality forces multiplicity pressure

Let

\[
R=\operatorname{rad}(abc),
\qquad
M=m(a)m(b)m(c)=\frac{abc}{R}.
\]

Fix `u>v>=1`. If

\[
\boxed{c^v>R^u,}
\]

then

\[
M^u
=\frac{(abc)^u}{R^u}
>\frac{(abc)^u}{c^v}
=(ab)^u c^{u-v}.
\]

Since positive integers satisfying `a+b=c` obey the sharp elementary bound

\[
ab\ge c-1,
\]

we obtain

\[
\boxed{
M^u>c^{u-v}(c-1)^u.
}
\]

So if support weight is too small compared with `c`, the missing scale must be stored as repeated prime multiplicity inside `m(a)m(b)m(c)`.

## 6. P025-T04 — multiplicity pressure localizes to at least one term

Let

\[
m_{\max}=\max\{m(a),m(b),m(c)\}.
\]

Because `M<=m_max^3`, P025-T03 gives

\[
\boxed{m_{\max}^{3u}>c^{u-v}(c-1)^u.}
\]

Using the project's canonical integer root

\[
R_r(N)=\max\{k\in\mathbb N:k^r\le N\},
\]

this becomes the exact finite threshold

\[
\boxed{
 m_{\max}>
 R_{3u}\!\left(c^{u-v}(c-1)^u\right).
}
\]

This is P025's first direct bridge back to the existing integer-root foundation: an abc-type high-quality event forces at least one multiplicity residual across an explicit integer root horizon.

A small working example is

\[
1+4374=4375,
\]

for which `rad(abc)=210` while the three residuals are `1,729,125`. This is only a structural example, not asymptotic evidence.

## 7. Mason–Stothers: the real bridge is more specific than the word “derivative”

The Mason–Stothers theorem is the classical polynomial/function-field analogue of abc. Baek and Lee's Lean 4 formalization exposes a short Wronskian proof [SRC-BAEK-LEE-2024-MASON-LEAN]:

1. `f/rad(f)` divides `f'`;
2. under `a+b+c=0`, the three Wronskians `W(a,b)`, `W(b,c)`, and `W(c,a)` agree;
3. each multiplicity residual divides the same common witness `W`;
4. pairwise coprimality lets the residual product divide `W`;
5. `deg W < deg a + deg b` provides witness capacity;
6. elimination yields `deg c + 1 <= deg rad(abc)`.

In the current architecture, the useful abstraction is therefore

\[
\boxed{
\text{hidden multiplicity residual}
\to
\text{relation-conditioned common witness}
\to
\text{witness capacity}
\to
\text{support bound}.
}
\]

`src/enterprise_math/abc_support.py::witness_capacity_elimination` implements only the final arithmetic elimination skeleton. The Wronskian witness construction is classical Mason–Stothers mathematics and is not owned by P025.

## 8. Critical prior-art collision: Pasten already transports this bridge to integers

Hector Pasten constructs arithmetic derivations on the integers that satisfy a Leibniz rule and are constrained to be additive for a chosen equation `a+b=c`; Geometry of Numbers supplies derivations with controlled size, and the existence of sufficiently small such derivations is shown to be tightly equivalent to the abc conjecture [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

The associated integer Wronskian reproduces the same absorber pattern: multiplicity residual enters a common witness and `abc` is then controlled by witness size times `rad(abc)`.

Therefore

\[
\boxed{\text{“find an integer Mason derivative” is not a new P025 direction.}}
\]

This prior-art collision narrows the genuinely useful architectural question.

## 9. P025-H01 — relation-conditioned witness space

P023 primarily asks whether a quotient makes a selected future observable or operation descend exactly.

Pasten's construction suggests an intermediate layer. Instead of demanding one global deterministic witness, or immediately refining the quotient until exact safety holds, associate to each task/relation state `x` an admissible witness family

\[
\mathcal W_R(x).
\]

Here:

- `R` is the active relation language, e.g. `a+b=c`;
- every `w in W_R(x)` satisfies structural constraints;
- `w` absorbs some residual forgotten by the quotient;
- witnesses have a discrete/integer cost `cost(w)`;
- the actual question is whether a sufficiently cheap witness exists:

\[
\boxed{
\min_{w\in\mathcal W_R(x)}\operatorname{cost}(w)
\le \text{required horizon}(x).
}
\]

For abc this is not merely new terminology for a new conjecture: Pasten already proves that a specific small-arithmetic-derivative formulation is tightly linked to abc. P025 asks whether **relation-conditioned witness-space semantics** can be made into a reusable interface broader than the specific derivative construction.

Current status: `CONJECTURAL ARCHITECTURE / NOVELTY_UNVERIFIED`.

## 10. A possible A2/A4 bridge, not a collapse of the layers

This candidate object touches two current layers that must remain explicitly distinct:

- A2 / P023: task-relative future-safe quotient, minimal repair, operation descent;
- A4: multivalued admissible support/correspondence witnesses.

The P025 bridge candidate is

\[
\text{coarse state}
\to
\text{relation-conditioned admissible witness family}
\to
\text{minimum witness precision/cost}
\to
\text{future bound/certificate}.
\]

This is consistent with the boundary requirement in Foundation issue `FQ-20260809-004`: functional kernels, relation-state, and multivalued support must remain distinguishable. P025 is a pressure test and does not directly modify Foundation.

## 11. P025-H02 — beyond binary safe/unsafe: failure magnitude and failure sparsity

Radical is not exact-safe for addition, so a binary `safe/unsafe` label discards structure too early.

Modern exceptional-set work supplies a mature comparison class. Bernert, Browning, Lichtman, and Teräväinen obtain a power-saving count for triples satisfying

\[
\operatorname{rad}(abc)<c^{1-\varepsilon}
\]

[SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]. Runbo Li subsequently gives the stronger exponent

\[
O\!\left(X^{56/85+\varepsilon}\right)
\]

[SRC-LI-2025-ABC-EXCEPTIONAL].

For rational `epsilon=r/s`, the exceptional predicate itself is exactly integer-valued:

\[
\boxed{
\operatorname{rad}(abc)^s<c^{s-r}.
}
\]

P025 therefore provisionally distinguishes at least three levels:

1. **exact descent** — future behavior is constant on quotient fibers;
2. **witness-mediated bounded defect** — exact descent fails, but an admissible bounded witness absorbs forgotten detail;
3. **sparse-exception descent** — bad states remain, but their incidence has a quantitative scale-dependent sparsity bound.

The third level is an architectural reinterpretation of established exceptional-set mathematics, not a novelty claim for the analytic methods themselves.

## 12. Prior-art boundary for derivation generalization

Derivative/Wronskian generalizations of Mason–Stothers are already broad; for example, Kikteva studies an ABC-type theorem for locally nilpotent derivations [SRC-KIKTEVA-2023-ABC-DERIVATION]. P025 therefore does not claim “abstract abc via derivations” as new.

Any future reusable mother theorem must identify a genuinely project-specific contribution such as:

- explicit finite-state quotient residual semantics;
- relation-conditioned multivalued witness families;
- witness precision/cost versus future-safe precision;
- strict migration criteria among exact, bounded-defect, and sparse-exception regimes;

rather than restating established derivation, Wronskian, or Geometry-of-Numbers results.

## 13. First-stage executable assets

The owner branch now contains:

- `src/enterprise_math/abc_support.py`
  - exact support / radical / multiplicity residual;
  - primitive abc support partition;
  - rational-exponent integer defect;
  - exact rational exceptional predicate;
  - executable residual-pressure check;
  - radical-addition negative boundary;
  - pure integer Mason witness-capacity elimination skeleton.
- `src/enterprise_math/abc_precision_bridge.py`
  - transport of residual pressure to the existing `integer_nth_root` horizon.
- `tests/test_abc_support.py`
- `tests/test_abc_precision_bridge.py`

Independent prototype regression covers the classical high-quality triple `2 + 3^10*109 = 23^5`, exact `Q_{3,2}=13`, the addition counterexample, exhaustive primitive triples with `c<120` for `(u,v)` in `{(2,1),(3,2),(4,3)}`, and the integer-root horizon bridge.

Enumeration validates implementation and elementary proved inequalities only; it is not evidence for the infinite abc statement.

## 14. Next frontier

The best next frontier has changed from “find an integer derivative” to:

1. reconstruct Pasten's witness space in finite support coordinates, separating prime-support coordinates, relation constraints, degrees of freedom, non-degeneracy, and norm;
2. study **witness precision** — how the admissible witness family shrinks under increasing precision/cost restrictions and whether it has monotone, stable, or minimally sufficient levels;
3. compare P023's “refine state until the operation descends” cost against “keep the coarse state and attach a bounded witness” cost;
4. test whether A4 admissible-support relations can express a state's multivalued witness family without importing false composition laws;
5. extract `bad-state count` as a finite/scale-dependent quotient-failure statistic from the abc exceptional-set specialization;
6. calibrate the whole witness-precision language first in the already-proved Mason–Stothers world before returning to integer abc.

If these steps merely recover Mason/Pasten structure, they must be recorded as `ADOPT/REINTERPRET`. Only a strictly more general, reusable, prior-art-audited interface should be considered for backflow into A2/P018 or Foundation.

## 15. Current conclusion

The first stage yields three reliable directional conclusions:

\[
\boxed{\text{radical is a support collapse, but not an addition congruence;}}
\]

\[
\boxed{\text{abc-type high quality forces large information into multiplicity residual;}}
\]

\[
\boxed{\text{successful prior-art bridges use relation-conditioned witnesses whose size matters.}}
\]

P025 should therefore study **task/relation-determined witness spaces and the precision/cost needed to control forgotten information**, rather than searching for a relation-free universal operation.
