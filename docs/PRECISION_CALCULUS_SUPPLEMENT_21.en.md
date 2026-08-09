# P018 — Finite-Precision Proof Calculus: Supplement 21

Status: `ACTIVE RESEARCH NOTE`  
Scope: labelled operation-context separation depth, shortest distinguishing-context certificates, higher-order split spectra, and the boundary of precision–time bifiltration  
Depends on: P011, P018-T169–T182  
Prior-art boundary: nested partition hierarchies and ultrametric representations are established; term/context distinguishability and syntactic congruence are established universal algebra / machine algebra. See `docs/PRIOR_ART_P018_COALESCENCE.en.md` and `docs/PRIOR_ART_P018_PREDICTIVE_CLOSURE.en.md`. [SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC] [SRC-CLARK-DAVEY-FREESE-JACKSON-2004-SYNTACTIC]

---

## 1. Why the fixed point is not the whole story

Supplement 19 identifies the canonical exact state relation

\[
R_*=\operatorname{Syn}_\Sigma(E)
\]

for a finite operation signature `Sigma` and static observation equivalence `E`.

But the finite refinement algorithm contains additional proof information:

\[
\boxed{
R_0=E
\supseteq
R_1
\supseteq
\cdots
\supseteq
R_h=R_*.
}
\]

A pair may be separated immediately, after one elementary operation context, only after several nested contexts, or never. This depth is useful because it answers a concrete proof question:

> **How complicated must an allowed operation context be before the current precision is forced to distinguish these two labelled states?**

---

## 2. P018-T183 — Extended labelled context-separation depth

Status: `PROVED / EXECUTABLE`

For labelled states `x,y`, define

\[
\boxed{
\sigma_\Sigma(x,y)
=
\min\{n\in\mathbb N:(x,y)\notin R_n\},
}
\]

when the set is nonempty, and put

\[
\boxed{
\sigma_\Sigma(x,y)=\infty
}
\]

when `(x,y) in R_*`.

Thus:

- `sigma=0` means the raw observation already separates the pair;
- `sigma=n>0` means the pair survives every context test of smaller depth but is forced apart at depth `n`;
- `sigma=infinity` means no finite term/context in the declared operation language separates the pair.

This is a labelled temporal coordinate on the **refinement process**, not physical time.

---

## 3. P018-T184 — The separation matrix and the whole refinement filtration are losslessly equivalent

Status: `PROVED / EXECUTABLE`

Because the relations are nested,

\[
\boxed{
(x,y)\in R_n
\iff
\sigma_\Sigma(x,y)>n
\text{ or }\sigma_\Sigma(x,y)=\infty.
}
\]

Therefore the labelled extended matrix

\[
\boxed{
\bigl(\sigma_\Sigma(x,y)\bigr)_{x,y\in X}
}
\]

reconstructs every `R_n` exactly.

Conversely, the filtration determines the first depth at which every labelled pair leaves the relation. Hence the two representations are losslessly equivalent.

As in the earlier kernel-time result, this keeps **who separates and when** at the Pair layer before any aggregate spectrum is taken.

---

## 4. P018-T185 — Reverse strong triangle law and quotient ultrametric

Status: `PROVED / EXECUTABLE / PRIOR-ART STRUCTURAL PATTERN`

For any three states,

\[
\boxed{
\sigma_\Sigma(x,z)
\ge
\min\bigl(
\sigma_\Sigma(x,y),
\sigma_\Sigma(y,z)
\bigr),
}
\]

with `infinity` treated as larger than every finite depth.

Proof: before the smaller of the two right-hand separation depths, both

\[
x\,R_n\,y,
\qquad
y\,R_n\,z
\]

hold. Since every `R_n` is an equivalence relation, transitivity gives

\[
x\,R_n\,z.
\]

So `x,z` cannot separate earlier.

Let `h` be the first stable depth and define

\[
d_{\mathrm{ctx}}(x,y)
=
\begin{cases}
0,&\sigma(x,y)=\infty,\\
h+1-\sigma(x,y),&\sigma(x,y)<\infty.
\end{cases}
\]

Then

\[
\boxed{
d_{\mathrm{ctx}}(x,z)
\le
\max(d_{\mathrm{ctx}}(x,y),d_{\mathrm{ctx}}(y,z)).}
\]

On `X`, this is an integer-valued pseudoultrametric whose zero classes are exactly the contextual-closure blocks. Therefore it becomes a genuine ultrametric on

\[
X/R_*.
\]

Hierarchy-to-ultrametric structure is established mathematics and is not claimed as novel.

---

## 5. P018-T186 — First separation depth equals shortest distinguishing-context length

Status: `PROVED / EXECUTABLE`

Let an elementary context be one one-hole translation of a basic operation. A context path of length `m` is a composition

\[
c=\tau_m\circ\cdots\circ\tau_1.
\]

The refinement recurrence implies by induction:

\[
\boxed{
(x,y)\in R_n
\iff
O(c(x))=O(c(y))
\text{ for every elementary-context path }c
\text{ of length at most }n.
}
\]

Therefore, whenever `sigma(x,y)` is finite,

\[
\boxed{
\sigma_\Sigma(x,y)
=
\min\{\operatorname{len}(c):O(c(x))\ne O(c(y))\}.
}
\]

If `sigma=infinity`, no finite context path distinguishes the pair.

Thus every required state distinction has a finite proof certificate of minimal context depth at most `h<=N-c0`.

The reference implementation finds one shortest certificate by breadth-first search on labelled state pairs.

---

## 6. P018-T187 — Pairwise separation depth determines every finite subset depth

Status: `PROVED / EXECUTABLE`

For a finite subset `A` with at least two states, define its first common-block failure depth as the least `n` such that `A` is no longer contained in one `R_n` block.

Then

\[
\boxed{
\sigma_\Sigma(A)
=
\min_{\{x,y\}\subseteq A}
\sigma_\Sigma(x,y),
}
\]

again with `infinity` larger than all finite depths.

Proof: `A` lies in one equivalence class exactly when every pair in `A` does.

So a separate higher-order context-depth object contains no additional deterministic depth information beyond the labelled pair matrix.

This is the refinement-side counterpart of the earlier result that higher coalescence time is the maximum of pairwise coalescence times, but no categorical duality is claimed.

---

## 7. P018-T188 — Exact per-depth collision-spectrum loss

Status: `PROVED / EXECUTABLE`

For a finite partition `P`, retain the P011 collision polynomial

\[
K_P(t)
=
\sum_{B\in P}
\bigl((1+t)^{|B|}-1\bigr).
\]

Suppose one parent block of size

\[
m=\sum_i m_i
\]

is refined into child blocks of sizes `m_i`.

The exact collision loss is

\[
\boxed{
\Delta^-_P(t)
=
(1+t)^m-1
-
\sum_i\bigl((1+t)^{m_i}-1\bigr).
}
\]

Its degree-`k` coefficient is

\[
\boxed{
\binom{m}{k}-\sum_i\binom{m_i}{k}\ge0.
}
\]

This counts exactly the labelled `k`-subsets that were contained in one parent block before the refinement but are no longer contained in one child block afterward.

Summing over all parent blocks in the step `R_n -> R_(n+1)` therefore gives:

\[
\boxed{
[t^k]\bigl(K_{R_n}(t)-K_{R_{n+1}}(t)\bigr)
=
\#\{A:|A|=k,\ \sigma_\Sigma(A)=n+1\}.
}
\]

Thus the P011 polynomial has an exact **split-spectrum** interpretation along the operation-context refinement axis.

---

## 8. P018-T189 — Split increments telescope exactly

Status: `PROVED / EXECUTABLE`

Because the chain is finite,

\[
\boxed{
K_{R_0}(t)-K_{R_*}(t)
=
\sum_{n=0}^{h-1}
\bigl(K_{R_n}(t)-K_{R_{n+1}}(t)\bigr).
}
\]

Every coefficient is a nonnegative integer.

So the total ambiguity removed when raw precision is repaired into an exact operation state decomposes exactly by **first distinguishing context depth** and subset order.

---

## 9. P018-T190 — Pair separation reconstructs the entire higher split spectrum

Status: `PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

T184 reconstructs every partition `R_n` from the labelled pair separation matrix. T188 then computes every degree of every split increment from those partitions.

Equivalently, T187 directly says the first separation depth of a labelled `k`-subset is the minimum pairwise separation depth inside it.

Hence

\[
\boxed{
\text{labelled pair separation matrix}
\Longrightarrow
\text{complete context-resolved P011 split spectrum}.
}
\]

The higher polynomial is a downstream counting image; it is not a replacement for labelled pair history.

---

## 10. P018-C20 — The unlabelled split spectrum does not recover labelled distinctions

Status: `COUNTEREXAMPLE / INFORMATION-LOSS BOUNDARY`

Take

\[
X=\{0,1,2,3,4\}
\]

with raw observation blocks

\[
\{0,1,2,3\},\qquad\{4\}.
\]

Consider two unary operation systems:

\[
F_A=(0,0,4,4,4),
\qquad
F_B=(0,4,0,4,4).
\]

Both refinement chains have the same block-size trajectory:

\[
(4,1)
\longrightarrow
(2,2,1).
\]

Therefore their complete collision-polynomial trajectories and split spectra are identical.

But the labelled pairs are different:

- under `F_A`, `0` remains grouped with `1` and separates from `2`;
- under `F_B`, `0` remains grouped with `2` and separates from `1`.

So

\[
\boxed{
\text{same context-resolved P011 spectrum}
\not\Rightarrow
\text{same labelled separation geometry}.
}
\]

Aggregate irreversibility/ambiguity observables still do not recover identity-level structure.

---

## 11. P018-T191 — Enlarging the operation language can only separate earlier

Status: `PROVED / EXECUTABLE`

If

\[
\Sigma\subseteq\Sigma',
\]

then induction on the refinement recurrence gives

\[
R_n^{\Sigma'}\subseteq R_n^{\Sigma}
\quad\forall n.
\]

Therefore, for every labelled pair,

\[
\boxed{
\sigma_{\Sigma'}(x,y)
\le
\sigma_\Sigma(x,y)
}
\]

whenever the right-hand side is finite; a pair that was never separated under the smaller language may become finitely separated under the larger language.

Thus adding exact operational obligations can only make missing detail become visible at the same or smaller context depth.

---

## 12. P018-T192 — The contextual fixed point is a canonical time-monotone row

Status: `PROVED / EXECUTABLE`

Let a declared unary operation

\[
F:X\to X
\]

belong to the operation language used to construct `R_*`.

Because `R_*` is a congruence,

\[
x\,R_*\,y
\implies
F(x)\,R_*\,F(y).
\]

Define the labelled-history kernel at time `t` by

\[
K_{*,t}
=
\{(x,y):F^{[t]}x\,R_*\,F^{[t]}y\}.
\]

Then

\[
\boxed{
K_{*,t}\subseteq K_{*,t+1}.
}
\]

So after the minimal contextual repair is complete, deterministic time again has the P010/P011 irreversible merge direction.

No extra time axiom is needed: time monotonicity is inherited from operation congruence.

---

## 13. P018-C21 — Before contextual closure, the naive precision–time grid need not be a bifiltration

Status: `COUNTEREXAMPLE / FOUNDATIONAL BOUNDARY`

Take

\[
X=\{0,1,2\},
\qquad
E=\{\{0,1\},\{2\}\},
\]

and unary operation

\[
F=(0,2,2).
\]

At raw precision, `0` and `1` are observationally equal. After one step,

\[
F(0)=0,
\qquad
F(1)=2,
\]

so the pair splits. Meanwhile `1` and `2`, which were initially distinct, now meet.

Thus the raw history partition changes from

\[
\{\{0,1\},\{2\}\}
\]

to

\[
\{\{0\},\{1,2\}\},
\]

and neither partition refines the other.

Therefore the raw time axis is not monotone.

Contextual refinement for the language `{F}` repairs `E` to equality, which is `F`-compatible; on that stable row the time kernels become monotone.

Hence:

\[
\boxed{
\text{nested precision refinement alone does not imply a precision–time bifiltration.}
}
\]

Each time row/precision relation must satisfy the relevant operation-congruence condition, or the grid can tear.

---

## 14. P018-T193 — Exact saddle monotonicity after closure

Status: `PROVED / EXECUTABLE`

For a chosen unary time operation `F`, define

\[
B_{n,t}
=
\{(x,y):F^{[t]}x\,R_n\,F^{[t]}y\}.
\]

For every fixed `t`, contextual refinement always gives

\[
\boxed{
B_{n+1,t}\subseteq B_{n,t},
}
\]

because `R_(n+1) subseteq R_n`.

Therefore the P011 collision polynomial is coefficientwise **nonincreasing** along context/refinement depth.

On the stable row `n=h`, T192 gives

\[
\boxed{
B_{h,t}\subseteq B_{h,t+1},
}
\]

so the same polynomial is coefficientwise **nondecreasing** along deterministic time.

This produces a finite saddle-shaped monotonicity law:

\[
\boxed{
\text{context depth removes apparent collisions;}
\qquad
\text{closed deterministic time creates genuine history collisions.}
}
\]

The two directions act on the same Pair/partition substrate but should not be identified.

---

## 15. P018-T194 — Q118 boundary classification

Status: `RESOLVED AS A FINITE STRUCTURAL BOUNDARY`

The precision/context axis now has a canonical labelled invariant:

\[
\boxed{
\sigma_\Sigma(x,y)
=
\text{shortest distinguishing-context depth},
}
\]

which losslessly reconstructs the contextual refinement filtration and all higher split spectra.

The deterministic closed-time axis has the earlier merger-time invariant

\[
\tau_F(x,y).
\]

A naive full two-dimensional precision–time grid is **not** automatically a bifiltration: C21 shows that pre-closure observation relations can tear under time.

The canonical statement is instead:

1. contextual refinement is monotone toward the greatest operation congruence;
2. the stable contextual row is the coarsest exact row on which every declared unary operation has monotone time kernels;
3. if a whole family of precision relations is already operation-congruent, the stronger bifiltration of T155 applies level by level;
4. `sigma` and `tau` are distinct labelled Pair coordinates for refinement and irreversible merge respectively.

Therefore Q118 is resolved as a **finite closure/bifiltration boundary classification**, not as a claim of universal time–precision duality.

---

## 16. What remains open

The principal open transport question remains Q119 from Supplement 19:

> once the minimal exact contextual state is known, when can its operation interactions be implemented through smaller structured composable transport data, and what is the minimum transport complexity?

A second derived direction is now available:

> can the shortest distinguishing-context certificates from T186 be compiled into reusable proof certificates for P017/P018 arguments without materializing the entire contextual quotient?

This is a proof-engineering question, not a new foundational primitive.

---

## 17. Executable pressure tests

Added:

- `src/enterprise_math/context_separation.py`
- `tests/test_context_separation.py`

The tests verify:

1. reconstruction of every contextual filtration level from the labelled separation matrix;
2. shortest distinguishing-context length equals first separation depth;
3. exhaustive two-state binary-operation certificate checks;
4. the reverse strong triangle / ultrametric inequality;
5. higher subset depth equals minimum pairwise depth;
6. exact degree-`k` split-spectrum counts;
7. finite telescoping of split increments;
8. C20 identical unlabelled spectra with different labelled separation histories;
9. operation-language monotonicity of separation depth;
10. C21 failure of raw time monotonicity and restoration on the stable contextual row;
11. opposite coefficientwise monotonicity of context depth and closed deterministic time.

A separate exhaustive audit over all 19,683 binary operations on three labelled states and all five equivalence partitions (98,415 algebra/observation cases; 295,245 unordered pair checks) found no counterexample to the separation-depth strong triangle law, shortest-context equality, or split-spectrum interpretation.
