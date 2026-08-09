# Foundations Under Test

This document records the current mathematical core of Enterprise Math. The statements below are not all established theorems of nature. They are separated into definitions, immediate mathematical consequences, and research hypotheses so that the project can be falsified or revised without losing provenance.

## 1. Primitive state space

The initial numerical state space is the set of nonnegative integers

\[
\mathbb N_0=\{0,1,2,\ldots\}.
\]

**Canonical natural-number convention.** Throughout canonical Enterprise Math mathematics,

\[
\mathbb N=\mathbb N_0=\{0,1,2,\ldots\},
\qquad
\mathbb N_{>0}=\{1,2,3,\ldots\}.
\]

Thus a bare \(\mathbb N\) includes zero. Statements requiring positivity use \(\mathbb N_{>0}\), `positive integer`, or an explicit inequality. This convention matches Python's non-negative natural-state inputs and Lean's `Nat` carrier.

Integers are not encodings of hidden real numbers. They are primitive states of the theory.

A scale may be attached to an integer state when comparing different resolutions, but scale is metadata of the state system, not permission to assume an infinitely refinable continuum.

## 2. Exact integer inverse operations

The **primitive nontrivial root/collapse family** uses integer exponents \(p\ge2\). For such an exponent, define the integer root

\[
R_p(n)=\max\{k\in\mathbb N_0:k^p\le n\}.
\]

This is an exact operation in the theory. It is not defined as an approximation to a hidden real root.

For algebraic closure, theorem reuse, and formalization, the same notation is extended to every positive exponent \(p\in\mathbb N_{>0}\). The only added case is

\[
R_1(n)=n.
\]

Accordingly, \(p=1\) is the identity member of the positive-exponent algebra; it is **not** an additional nontrivial primitive collapse. Unless a statement explicitly says `primitive` or `nontrivial`, theorem/Python/Lean statements quantified over positive exponents may include \(p=1\).

For \(p=2\):

\[
R_2(2)=1,
\qquad
R_2(200)=14,
\qquad
R_2(20000)=141.
\]

For every positive exponent, the defining relation is

\[
k^p\le n<(k+1)^p
\quad\Longleftrightarrow\quad
R_p(n)=k.
\]

## 3. Collapse operators

Define the power-collapse operator

\[
C_p(n)=R_p(n)^p.
\]

In the positive-exponent extension,

\[
C_1=\operatorname{id}.
\]

For squares,

\[
C_2(20000)=19881.
\]

Because

\[
141^2=19881,
\qquad
142^2=20164,
\]

we have

\[
19881\le n\le20163
\quad\Longrightarrow\quad
C_2(n)=19881.
\]

Therefore the state 19881 has 283 direct preimages under this collapse map.

### Immediate properties

For every positive exponent \(p\ge1\), \(C_p\) is:

- reductive: \(C_p(n)\le n\);
- monotone: \(n\le m\Rightarrow C_p(n)\le C_p(m)\);
- idempotent: \(C_p(C_p(n))=C_p(n)\).

Its fixed points are exactly the perfect \(p\)-th powers. At \(p=1\) every state is a fixed point and every basin has one state, so all of these laws reduce to the identity case. The physically nontrivial many-to-one collapse discussion below therefore concerns \(p\ge2\) unless another map is explicitly supplied.

This is structurally close to an interior operator on an ordered set. That mathematical similarity is useful prior art; it does not by itself establish the physical interpretation proposed here.

## 4. No hidden remainder axiom candidate

The current physical interpretation under test is stronger than ordinary quantization or coarse-graining.

If a nontrivial collapse

\[
n\rightarrow C_p(n),\qquad p\ge2,
\]

occurs, the difference

\[
n-C_p(n)
\]

is not assumed to remain in nature as a hidden state variable. It can be computed externally by comparing two states, but it is not part of the post-transition state unless a separate law explicitly carries it forward.

Thus the map is ontologically many-to-one, not merely observationally many-to-one.

This is a research hypothesis, not a theorem derived from the arithmetic definition alone.

## 5. Scale compatibility

Let \(B\ge2\) be an integer scale base. A refined square-root query may be represented by

\[
R_{2,s}(n)=R_2(nB^{2s}).
\]

The states are integers at every scale. No decimal expansion is introduced.

A desired compatibility condition is

\[
Q_B(R_{2,s+1}(n))=R_{2,s}(n),
\]

where the integer quotient operator is defined directly by

\[
Q_B(a)=\max\{q\in\mathbb N_0:qB\le a\}.
\]

For example,

\[
1\leftarrow14\leftarrow141\leftarrow1414
\]

is a compatible family of integer states for progressively refined square-root queries based on the state 2.

If nature has a maximum resolution, this chain terminates. No infinite completion is required inside the theory.

## 5A. Represented precision and future-safe precision

### Classical functional-kernel interface

For the generic mathematical interface, let \(X\) be a typed state carrier. This does **not** replace the project-specific integer specialization \(X=\mathbb N_0\) where the primitive arithmetic/physical hypothesis applies.

Any deterministic map

\[
f:X\to Y
\]

induces its ordinary functional kernel (fiber equivalence)

\[
x\sim_f y
\quad\Longleftrightarrow\quad
f(x)=f(y).
\]

For a current observation \(O:X\to A\), equality in \(\ker(O)\) is therefore **observational equality**, not exact state equality unless \(O\) is injective.

Now declare a family/language \(W\) of deterministic future experiments together with the observations that are required after them. Package the required future outputs into a signature

\[
\Sigma_W:X\to S_W.
\]

The equality relation

\[
x\sim_W y
\quad\Longleftrightarrow\quad
\Sigma_W(x)=\Sigma_W(y)
\]

is the functional kernel for that **declared** future language. If the current observation is included among the outputs represented by \(\Sigma_W\), then, writing \(\Delta_X\) for exact equality,

\[
\boxed{
\Delta_X\subseteq\ker(\Sigma_W)\subseteq\ker(O).
}
\]

Thus exact state equality, current observational equality, and future-safe equality are distinct layers unless additional hypotheses make them coincide.

Deterministic postcomposition cannot split a functional kernel: for any \(g\),

\[
\boxed{
\ker(f)\subseteq\ker(g\circ f).
}
\]

This is the generic kernel form of the history-merging law used in A1/T012.

A coordinate \(\delta:X\to D\), or a pair coordinate \(\delta:X\times X\to D\), may replace the underlying state information for a declared task only after an explicit sufficiency/factorization theorem. For example,

\[
O=h\circ\delta
\]

is exact sufficiency for the current observation, while

\[
\Sigma_W=H\circ\delta
\]

is exact sufficiency for the declared future signature. Without such a factorization, a difference, defect, critical-grid coordinate, or other compressed diagnostic is not automatically a dynamically complete state.

A **state pair** at this layer is simply an element of the ordinary product \(X\times X\); it is not a separate primitive ontology.

This lower interface is deliberately functional. A3 structured/weighted relation-state may retain information beyond functional-kernel membership, and A4 multivalued support/correspondence may admit several future images. Neither is identified with one functional kernel without an explicit selection/factorization theorem.

These kernel/fiber, factorization, future-distinguishability, and partition-refinement ideas are classical prior mathematics. Enterprise Math makes no novelty claim for the generic abstraction; P023/P024 and other owners provide the project-specific exact arithmetic specializations and repair results.

A represented precision is an explicit many-to-one partition of the current fine state space. It says which current states are represented as the same state at the declared resolution.

That partition is not automatically sufficient for every future computation.

Given a declared family of future operations and observations, define the **future-safe precision** to be the coarsest refinement of the represented precision for which all required future behavior descends to the retained state.

Therefore Enterprise Math distinguishes

\[
\boxed{
\text{represented precision}
\neq
\text{future-safe precision in general}.
}
\]

P023 gives the generic quotient/congruence criterion for this distinction. P024 gives an exact integer-translation specialization: when observations are cut by integer boundaries `B` and the declared future action language has reachable cumulative translations `M`, the present distinctions that can still be read by the future are the pulled-back boundary orbit

\[
\boxed{B-M.}
\]

The resulting precision cells need not be globally uniform. A uniform scale is one possible precision geometry, not a foundational requirement.

In particular, action language and state topology can change the minimal safe precision even when the nominal measurement scale is unchanged. This is a mathematical statement about predictive sufficiency, not by itself a claim that nature selects a task-dependent physical ontology.

## 6. Classical identities are not assumed

Because integer root is not a two-sided inverse of exponentiation, classical real identities must be re-proved rather than imported.

For example,

\[
R_2(n^2)=n
\]

for nonnegative integers \(n\), but generally

\[
R_2(n)^2\ne n.
\]

Likewise, generally

\[
R_2(a)R_2(b)\ne R_2(ab).
\]

These are not numerical errors. They are algebraic features of a different operation.

## 7. Forward dynamics

Time indices lie in \(\mathbb N_0\). Let

\[
T_t:X_t\to X_{t+1}
\]

be the transition carrying the state from time \(t\) to time \(t+1\), so

\[
X_{t+1}=T_t(X_t).
\]

The maps are allowed to be non-injective. No inverse map is required.

The canonical cumulative-map convention is

\[
F_0=\operatorname{id},
\]

and, for \(t\ge1\),

\[
F_t=T_{t-1}\circ\cdots\circ T_0.
\]

Equivalently,

\[
F_{t+1}=T_t\circ F_t,
\qquad
X_t=F_t(X_0).
\]

For two initial states, define

\[
x\sim_t y
\quad\Longleftrightarrow\quad
F_t(x)=F_t(y).
\]

If \(x\sim_t y\), then necessarily \(x\sim_{t+1}y\). Once two histories merge under deterministic forward evolution, later function composition cannot separate them again.

Therefore the equivalence class

\[
[x]_t=\{y:F_t(y)=F_t(x)\}
\]

can only remain the same size or grow.

When two histories eventually merge, their **merge time** is the least

\[
\tau(x,y)=\min\{t\in\mathbb N_0:F_t(x)=F_t(y)\}.
\]

Hence histories equal initially have merge time \(0\); a collision caused by the first transition \(T_0\) has merge time \(1\). Any historical one-based transition notation is translated by \(T_j^{\mathrm{old}}=T_{j-1}\) while retaining the same cumulative time label \(F_t\).

## 8. Integer irreversibility measures

The primary internal quantity should remain integer-valued:

\[
M_t(x)=|[x]_t|.
\]

Then

\[
M_{t+1}(x)\ge M_t(x).
\]

This gives a discrete monotone measure of historical merging without introducing logarithms or real-valued entropy as primitive objects.

If a logarithmic entropy is useful for comparison with conventional information theory, it should initially be treated as an external derived representation, not as part of the primitive arithmetic.

An integer information level can instead be defined, for example, by

\[
L_B(m)=\min\{\ell\in\mathbb N_0:m\le B^\ell\},
\]

which remains an integer map.

## 9. Open foundational questions

1. Which operations should be primitive and which should be derived?
2. Should signed integers be primitive, or should direction/sign be a separate state component?
3. What is the correct discrete replacement for division, ratios, and dimensional analysis?
4. Which notion of distance produces a useful geometry without silently restoring real-valued Euclidean distance?
5. Which families of collapse maps generate nontrivial forward dynamics rather than reaching fixed points immediately?
6. Can the monotonic growth of preimage classes be connected to thermodynamic entropy under explicit physical assumptions?
7. Which observed physical laws contradict an ontologically non-invertible foundation?
8. Which parts of calculus can be reconstructed as finite-scale difference and accumulation operators?
9. Which future-safe precision objects admit compact structured representations, and when must a nonuniform boundary/detail layer be retained?

## 10. Status discipline

A proposed physical interpretation must not be promoted to a theorem merely because the integer mathematics is consistent. The repository should keep the following categories separate:

- definition;
- theorem;
- computational observation;
- conjecture;
- physical hypothesis;
- external analogy.
