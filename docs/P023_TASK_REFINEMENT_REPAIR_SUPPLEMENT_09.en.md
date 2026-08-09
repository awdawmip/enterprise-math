# P023 — Task-Precision Refinement and Minimal Repair Counting, Supplement 09

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023 future-compatible quotient  
Depends on: P023 composition-safe repair formal core, P023-S8 actual-image separation, E002 predictive quotient  
Discipline: equivalence-relation lattices, kernel intersections, closure systems, and finite partition counting are established mathematics. This supplement does not claim historical priority for those general structures. Its project role is to fix them as a common quantitative interface for finite-precision research.

## 1. Problem

P023 already proves that if an old coarse state is

\[
q:X\to Q,
\]

and a new observable is

\[
h:X\to R,
\]

then the pair state

\[
(q,h):X\to Q\times R
\]

is the coarsest exact repair that retains both.

That existence/coarsest theorem does not yet answer three finite-precision questions: how many quotient classes are actually realized after tasks are combined; how many repair symbols are minimally required to upgrade an old task quotient; and how repair costs compose through several upgrades.

This supplement gives exact finite answers.

## 2. Task queries and precision relations

Let `X` be a finite nonempty state set. A declared query is a deterministic map

\[
f_\alpha:X\to Y_\alpha.
\]

For a query language \(\mathcal L\), define

\[
\boxed{
x\sim_{\mathcal L}y
\iff
f_\alpha(x)=f_\alpha(y)
\quad\text{for every }\alpha\in\mathcal L.
}
\]

Write the corresponding equivalence relation as \(E_{\mathcal L}\). For future dynamics one may take \(f_\alpha=O_j\circ T_w\), so bounded horizon, action language, and observation language are all specializations of the same definition.

## 3. P023-S9-T01 — Task language is antitone; task union is common refinement

Status: `PROVED`.

If \(\mathcal L_1\subseteq\mathcal L_2\), then

\[
\boxed{E_{\mathcal L_2}\subseteq E_{\mathcal L_1}.}
\]

For any family of task languages,

\[
\boxed{E_{\bigcup_i\mathcal L_i}=\bigcap_i E_{\mathcal L_i}.}
\]

### Proof

Two states are equivalent on the left exactly when they answer every query in the union identically, which is equivalent to lying in every individual relation. ∎

### Meaning

Thus increasing horizon, adding action generators, and adding observables are all the same order-theoretic move: the safe quotient can only refine.

## 4. P023-S9-T02 — Combined quotients count realized tuples, not a formal Cartesian product

Let \(\pi_1:X\to X/E_1\) and \(\pi_2:X\to X/E_2\) be two task quotients, and define

\[
\Pi(x)=(\pi_1(x),\pi_2(x)).
\]

Then \(\ker\Pi=E_1\cap E_2\), so

\[
\boxed{C_{12}=|\operatorname{im}\Pi|.}
\]

If \(C_i=|X/E_i|\), then

\[
\boxed{\max(C_1,C_2)\le C_{12}\le C_1C_2.}
\]

### Key point

The product is only the candidate Cartesian product. Actual combined states are the tuples reached by `X`.

\[
\boxed{\text{formal product candidates}\neq\text{realized combined states}.}
\]

### Many-task version

For finitely many quotients,

\[
\boxed{
\left|X/\bigcap_iE_i\right|
=
\left|\operatorname{im}\left(X\to\prod_iX/E_i\right)\right|.
}
\]

Class counts must not be multiplied without an independence or surjectivity proof. This is the same actual-image discipline used by P023-S8 and P017 L055.

## 5. Refinement chains and local split multiplicity

Assume \(F\subseteq E\). For each old block \(B\in X/E\), define

\[
\boxed{m_{E\to F}(B)=\#\{C\in X/F:C\subseteq B\}.}
\]

Set

\[
\boxed{R(E\to F)=\max_{B\in X/E}m_{E\to F}(B).}
\]

This is local. A global quotient-class ratio need not be an integer and need not equal the repair cost.

## 6. P023-S9-T03 — Minimal repair-alphabet theorem

Status: `PROVED`.

Let \(\rho:X\to A\) be a repair coordinate and require

\[
\boxed{F=E\cap\ker\rho.}
\]

Then

\[
\boxed{
\min|A|
=
R(E\to F)
=
\max_{B\in X/E}m_{E\to F}(B).
}
\]

### Necessity

Inside one old coarse block, distinct target blocks require distinct repair symbols. Otherwise the pigeonhole principle forces two target blocks to have the same old coarse label and the same repair symbol, contradicting \(F=E\cap\ker\rho\). Hence every repair alphabet has at least the maximum local split multiplicity.

### Sufficiency

Number the target subblocks locally inside each coarse block and reuse the same symbol alphabet across different coarse blocks. With exactly \(R(E\to F)\) symbols, equality of the old coarse label plus repair symbol is then exactly target equivalence. ∎

## 7. General criterion for a one-bit repair

T03 immediately gives

\[
\boxed{\text{binary repair is sufficient}\iff R(E\to F)\le2.}
\]

If some old block genuinely splits into two target blocks, two symbols are also necessary.

The P023 crossing bit, the E002 one-step carry repair, and the P017 L057 lower-band root-shell repair are therefore instances of the same local split-multiplicity law.

## 8. P023-S9-T04 — Repair-chain submultiplicativity

Status: `PROVED`.

For \(G\subseteq F\subseteq E\),

\[
\boxed{R(E\to G)\le R(E\to F)R(F\to G).}
\]

### Proof

An `E`-block contains at most \(R(E\to F)\) `F`-blocks, each containing at most \(R(F\to G)\) `G`-blocks. Taking the maximum proves the bound. ∎

### Strict inequality can occur

The inequality may be strict when the worst split at each stage occurs on different local branches. Stagewise worst cases therefore need not multiply to the exact direct repair cost.

## 9. P023-S9-T05 — Query-generated precision closure lattice

Status: `PROVED / STANDARD STRUCTURE`.

Fix an available query family `Q` and set

\[
\mathfrak P_Q=\{E_{\mathcal L}:\mathcal L\subseteq Q\}.
\]

The empty language gives the universal relation and arbitrary intersections stay in the family because

\[
\bigcap_iE_{\mathcal L_i}=E_{\cup_i\mathcal L_i}.
\]

Hence \(\mathfrak P_Q\) is a closure system inside the equivalence-relation lattice and therefore a complete lattice in its own right. In the refinement order where finer relations are smaller,

\[
\boxed{\bigwedge_iE_{\mathcal L_i}=E_{\cup_i\mathcal L_i}.}
\]

Its join is the intersection of all query-generated relations simultaneously coarser than the supplied relations.

### Project meaning

This suggests a more foundational proof-state notion:

\[
\boxed{\text{precision state}=\text{query-generated equivalence relation}.}
\]

Different tasks move through a refinement lattice rather than necessarily along one scalar digit axis. This remains a theorem about proof and predictive sufficiency, not a claim that physical ontology changes with a chosen task.

## 10. Exact relation to the P023 formal core

This supplement does not re-invent pair repair. `EnterpriseMath/Precision/CompositionSafeCollapse.lean` already proves that `(q,h)` is the coarsest repair retaining both `q` and `h`.

The new finite layer is

\[
\boxed{
\text{coarsest repair relation}
+\text{exact minimum repair-alphabet cardinality}.
}
\]

These answer different questions: which relation must be retained, and how many extra discrete repair states are minimally necessary.

## 11. New feedback into P017

For a P017 lower-band exact cofactor shell after integer-root projection, take the old coarse state to be the root index and the target to retain both root and least-prime shell identity. The split multiplicity of a root fiber is exactly the number of prime shells actually hitting that root.

P017 Supplement 20 proves

\[
\boxed{
R_{\min}(k)=
\begin{cases}
2,&k\in\{5,6,8\},\\
1,&k\ge4,\ k\notin\{5,6,8\}.
\end{cases}
}
\]

and constructs one uniform minimal repair bit.

## 12. Executable specification

- `src/enterprise_math/task_precision_refinement.py`
- `tests/test_task_precision_refinement.py`

Regression checks task-union/common-refinement identity, realized tuple counts below formal products, the exact maximum-local-split repair formula, exhaustive failure of smaller alphabets on a bounded model, and submultiplicative repair-chain cost with a strict example.

Finite enumeration is reconstruction/regression only; the proofs above are ordinary finite mathematics.
