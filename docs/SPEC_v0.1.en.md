# Enterprise Math v0.1 Core Specification

Status: Research Beta  
Scope: mathematical core only

## 1. Design boundary

The v0.1 core is a discrete arithmetic experiment. It does not assume a complete real line as a hidden semantic layer.

The primitive state domain is

\[
\mathbb N=\{0,1,2,\ldots\}.
\]

Scale is represented by integers and integer bases. No decimal or floating-point object is required by the core.

## 2. Integer root

For \(n\in\mathbb N\) and integer \(p\ge1\), define

\[
R_p(n)=\max\{k\in\mathbb N:k^p\le n\}.
\]

Equivalently, \(R_p(n)=k\) exactly when

\[
k^p\le n<(k+1)^p.
\]

This definition is primary. The phrase "floor of a real root" may be used only as an external comparison, not as the internal definition.

## 3. Collapse

Define the perfect-power collapse

\[
C_p(n)=R_p(n)^p.
\]

The output is the greatest perfect \(p\)-th power not exceeding \(n\).

For \(p=2\),

\[
C_2(20000)=141^2=19881.
\]

## 4. Collapse basin

For root state \(k\), define the basin

\[
B_{p,k}=\{n\in\mathbb N:k^p\le n<(k+1)^p\}.
\]

Every element of \(B_{p,k}\) has the same collapse image \(k^p\).

Its cardinality is

\[
|B_{p,k}|=(k+1)^p-k^p.
\]

This cardinality is a property of the map. The v0.1 ontology does not require a hidden remainder state to survive after collapse.

## 5. Scale refinement

Let \(b\ge2\) be an integer scale base and \(s\ge0\) an integer level.

Define the scaled root state

\[
R_{p,b,s}(n)=R_p\left(n\,b^{ps}\right).
\]

One result digit of root resolution requires \(p\) powers of input-scale refinement.

The coarse projection of an integer state is integer division by the base:

\[
P_b(m)=m\operatorname{//}b.
\]

The scale-compatibility theorem states

\[
P_b\!\left(R_{p,b,s+1}(n)\right)=R_{p,b,s}(n).
\]

No infinite refinement limit is part of v0.1.

## 6. Forward dynamics

A state evolution step is a function

\[
T:X\to X
\]

that is not required to be injective or invertible.

A sequence of forward steps is

\[
F_t=T_t\circ T_{t-1}\circ\cdots\circ T_1.
\]

For an initial state \(x\), define its merged-history class at step \(t\):

\[
[x]_t=\{y:F_t(y)=F_t(x)\}.
\]

If \(x\) and \(y\) have merged at time \(t\), deterministic forward composition cannot separate them at time \(t+1\). Thus

\[
[x]_t\subseteq[x]_{t+1}.
\]

## 7. First irreversibility observable

For finite state domains, define the preimage multiplicity

\[
M_t(x)=|[x]_t|.
\]

It is integer-valued and nondecreasing under deterministic forward composition.

No logarithm is a primitive in v0.1. Relations to Shannon entropy, preimage entropy, folding entropy, and thermodynamic entropy are research questions, not definitions.

## 8. Claim-status discipline

Every material statement belongs to one of these classes:

- `DEFINITION`
- `PROVED`
- `CONJECTURE`
- `COUNTEREXAMPLE`
- `COMPUTATIONAL`
- `PHYSICAL-HYPOTHESIS`

A physical interpretation must never silently upgrade a mathematical conjecture into a theorem, and a mathematical analogy must never silently become a physical result.

## 9. Explicit non-goals

v0.1 does not yet define:

- a complete signed-number system;
- general division;
- a final scale algebra;
- geometry;
- calculus;
- probability;
- quantum mechanics;
- thermodynamic entropy;
- a fundamental law of time.

Those belong to later research only after the core survives proof and counterexample pressure.

## 10. Reference implementation rule

The executable core must use integer operations only. Floating-point constants and true division are prohibited in the core module.

The implementation exists to reproduce definitions, enumerate finite examples, and search for counterexamples. Mathematical proof remains authoritative for `PROVED` status.
