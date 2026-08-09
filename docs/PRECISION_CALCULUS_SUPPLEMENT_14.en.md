# P018 — Finite-Precision Proof Calculus: Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: finite coalescence time, P020 stabilization kernels, eventual kernels, integer ultrametrics, and finite-time saturation of P011 spectra  
Depends on: P010, P011, P012, P018-T110–T128, P020  
Prior-art boundary: see `docs/PRIOR_ART_P018_COALESCENCE.en.md`. General hierarchy/dendrogram/coalescent connections with ultrametrics are mature structures; this stage studies their exact finite interface with Enterprise Math deterministic kernel/stabilization dynamics.

---

## 1. From whether trajectories merge to when they merge

For a deterministic endomap

\[
F:X\to X,
\]

write its `n`-fold iterate as

\[
F^{[n]}.
\]

Two states `(x,y)` **eventually coalesce** when some `n` satisfies

\[
F^{[n]}(x)=F^{[n]}(y).
\]

Define the first coalescence time by

\[
\boxed{
\tau_F(x,y)
=
\min\{n\in\mathbb N:F^{[n]}(x)=F^{[n]}(y)\}.
}
\]

If no such `n` exists, write `∞`.

This definition lives entirely at the State Pair / diagonal layer and requires no subtraction, distance, or probability.

---

## 2. P018-T129 — Eventual coalescence is an equivalence relation

Status: `PROVED`

Define

\[
x\sim_\infty y
\iff
\exists n,\ F^{[n]}(x)=F^{[n]}(y).
\]

Then `~∞` is an equivalence relation.

- Reflexivity: choose `n=0`.
- Symmetry: equality is symmetric.
- Transitivity: if `x,y` agree after `a` steps and `y,z` agree after `b` steps, then at

\[
N=\max(a,b)
\]

common deterministic suffixes preserve both equalities, so

\[
F^{[N]}x=F^{[N]}y=F^{[N]}z.
\]

Hence `x~∞z`. ∎

Deterministic dynamics therefore partitions the state space into eventual-coalescence classes.

---

## 3. P018-T130 — First coalescence time is ultrametric on each coalescence class

Status: `PROVED / ESTABLISHED STRUCTURAL PATTERN`

Inside one `~∞` class,

\[
\tau_F(x,x)=0,
\]

\[
\tau_F(x,y)=\tau_F(y,x),
\]

and for all `x,y,z`,

\[
\boxed{
\tau_F(x,z)
\le
\max\bigl(\tau_F(x,y),\tau_F(y,z)\bigr).
}
\]

### Proof

Let

\[
a=\tau_F(x,y),
\qquad
b=\tau_F(y,z),
\qquad
N=\max(a,b).
\]

After step `a`, the `x,y` trajectories are identical forever; after step `b`, the `y,z` trajectories are identical forever. Thus at step `N`,

\[
F^{[N]}x=F^{[N]}y=F^{[N]}z.
\]

Therefore the first coalescence of `x,z` is no later than `N`. ∎

Hence on every eventual-coalescence class,

\[
\boxed{
\tau_F\text{ is an }\mathbb N\text{-valued ultrametric.}
}
\]

This is not a novelty claim for the general coalescent-ultrametric phenomenon. Its role here is that the ultrametric is generated directly from Enterprise Math deterministic Pair/kernel dynamics rather than imposed as an external distance.

---

## 4. P018-T131 — The common-time kernel chain grows monotonically

Status: `PROVED`

Define

\[
K_n=\kerpair(F^{[n]}).
\]

If

\[
(x,y)\in K_n,
\]

then one more common application of `F` preserves equality, so

\[
\boxed{
K_n\subseteq K_{n+1}.
}
\]

Moreover,

\[
\boxed{
x\sim_\infty y
\iff
(x,y)\in\bigcup_{n\in\mathbb N}K_n.
}
\]

The union does not require an infinite computation: every concrete included pair has a finite witness `n`.

---

## 5. Add the P020 hypotheses

Now let `X` be a well-founded partial order and assume

\[
F:X\to X
\]

is monotone and reductive:

\[
F(x)\le x.
\]

P020 proves that each state reaches in finitely many steps its canonical greatest fixed point

\[
S(x)=\operatorname{stabilize}_F(x),
\]

with a finite witness

\[
s(x)=\operatorname{stabilizationSteps}_F(x)
\]

such that

\[
F^{[s(x)]}(x)=S(x),
\qquad
F(S(x))=S(x).
\]

---

## 6. P018-T132 — Under P020, eventual coalescence iff stabilization is equal

Status: `PROVED`

Under the P020 hypotheses,

\[
\boxed{
x\sim_\infty y
\iff
S(x)=S(y).
}
\]

### Forward direction

Suppose some `n` satisfies

\[
F^{[n]}x=F^{[n]}y.
\]

The trajectories are identical from step `n` onward. P020 also says that each trajectory reaches and then remains at its stabilized fixed point in finite time. At a common time no smaller than `n`, `s(x)`, and `s(y)`, the two trajectories are both identical and already equal to their respective fixed endpoints, hence

\[
S(x)=S(y).
\]

### Reverse direction

If

\[
S(x)=S(y)=z,
\]

let

\[
N=\max(s(x),s(y)).
\]

Because `z` is fixed, each trajectory remains at `z` after reaching it. Hence

\[
F^{[N]}x=z=F^{[N]}y.
\]

So the pair coalesces in finite time. ∎

Therefore

\[
\boxed{
\kerpair(S)
=
\bigcup_{n\in\mathbb N}\kerpair(F^{[n]}).
}
\]

---

## 7. P018-T133 — Canonical finite coalescence bound

Status: `PROVED`

If `S(x)=S(y)`, then

\[
\boxed{
\tau_F(x,y)
\le
\max(s(x),s(y)).
}
\]

This is a direct finite integer bound from the P020 witnesses, not an asymptotic estimate.

---

## 8. P018-C11 — An infinite state space need not have a uniform global coalescence bound

Status: `COUNTEREXAMPLE / DESIGN WARNING`

Take

\[
F(n)=\max(n-1,0)
\]

on `N`.

It is monotone and reductive, and every state stabilizes at `0`, but state `n` requires at least `n` steps. For every proposed finite global bound `B`, choosing `n>B` violates it.

Therefore

\[
\boxed{
\text{a finite pair-specific bound for every pair}
\not\Rightarrow
\text{one uniform finite bound on the whole infinite state space}.
}
\]

P020 pointwise finite stabilization must not be silently upgraded to uniform convergence.

---

## 9. P018-T134 — Every finite observation set has a finite saturation time

Status: `PROVED`

For a finite state set

\[
H\subseteq X,
\]

define

\[
\boxed{
N_H=\max_{x\in H}s(x).
}
\]

Then for every `x∈H`,

\[
F^{[N_H]}x=S(x).
\]

Hence on `H`,

\[
\boxed{
\kerpair(F^{[N_H]}|_H)
=
\kerpair(S|_H).
}
\]

For every `n≥N_H`, the kernel partition no longer changes.

Thus even when the global state space is infinite, every finite observation set reaches its complete indistinguishability structure after a finite integer time.

---

## 10. P018-T135 — The P011 collision spectrum saturates in finite time on finite observations

Status: `DERIVED FROM P011 + T134`

P011 collision polynomials and all `J_k` depend only on finite-map fiber sizes.

On finite `H`, T134 shows that

\[
F^{[N_H]}|_H
\]

and

\[
S|_H
\]

induce exactly the same kernel partition and fibers. Therefore

\[
\boxed{
K_{F^{[N_H]}|_H}(t)
=
K_{S|_H}(t).
}
\]

P011 deterministic postcomposition monotonicity also gives

\[
K_{F^{[n]}|_H}(t)
\preceq_{\rm coeff}
K_{F^{[n+1]}|_H}(t).
\]

So the entire integer collision spectrum stops changing after the finite time `N_H`.

This is a finite-time irreversibility saturation theorem requiring neither Shannon entropy nor a continuous limit.

---

## 11. P018-T136 — Stabilization fibers are exactly coalescence-ultrametric components

Status: `PROVED SYNTHESIS`

By T132,

\[
S(x)=S(y)
\iff
\tau_F(x,y)<\infty.
\]

Thus every stabilization fiber

\[
S^{-1}(z)
\]

is exactly one eventual-coalescence class.

By T130, `τ_F` is an integer-valued ultrametric on that fiber.

The P020 canonical fixed points therefore simultaneously provide:

1. stable normal forms of the dynamics;
2. labels for P010 eventual-kernel equivalence classes;
3. an ultrametric geometry on each basin generated by first-merger time.

This gives a strong feedback route into P012: some geometry can be **derived** from deterministic irreversibility history rather than postulated as a continuous background.

It does not replace the P012 primitive-step graph metric. The two metrics have different meanings:

- P012 graph distance measures shortest primitive-step path length;
- `τ_F` measures the first time two states lose distinguishability under common dynamics.

Their relation requires separate theorems and counterexamples.

---

## 12. A refined discrete-time layer

P010 originally expresses the time arrow mainly through monotone coarsening of kernel partitions.

The combined structure is now

\[
\boxed{
\text{State Pair}
\to
\text{kernel chain }K_0\subseteq K_1\subseteq\cdots
\to
\text{first diagonal-entry time }\tau
\to
\text{stabilization fiber}
\to
\text{finite collision-spectrum saturation}.
}
\]

Time here is an integer sequence of events, not a continuous parameter.

---

## 13. Executable pressure tests

Added:

- `src/enterprise_math/coalescence_time.py`
- `tests/test_coalescence_time.py`

The tests cover:

1. explicit stabilization steps for decrement dynamics;
2. finite exhaustive checks of same stabilized state iff finite coalescence;
3. kernel-chain monotonicity;
4. exact finite-observation saturation at the maximum stabilization time;
5. regression showing no uniform saturation bound on all of `N`;
6. exhaustive checks of the coalescence-time ultrametric inequality.

---

## 14. Next questions

### P018-Q105 — Relation between coalescence ultrametric and P012 graph metric

Find exact equivalence conditions, bounds, and counterexamples. Treat the two metrics as different by default.

### P018-Q106 — Grid cancellation and coalescence time

Study whether Supplement 13 local-defect cancellation changes outer coalescence time and whether an integer certificate separates local cancellation from genuine local flatness.

### P018-Q107 — Time-increment formula for finite-history collision polynomials

P011 gives the polynomial increment of one fiber merge. Determine whether

\[
K_{n+1}(t)-K_n(t)
\]

can be computed directly from pairs/higher tuples newly entering the diagonal at that step, and whether these increments sum exactly to the stabilization spectrum.

### P018-Q108 — Nondeterministic dynamics

The ultrametric proof relies crucially on the fact that once a pair enters the diagonal, a common deterministic suffix can never split it. Relations/spans would require a fresh analysis rather than automatic reuse.

---

## 15. Current conclusion

Combining P020 with the Pair/kernel layer gives a completely finite closure:

\[
\boxed{
S(x)=S(y)
\iff
\tau_F(x,y)<\infty,
\qquad
\tau_F(x,y)
\le
\max(s(x),s(y)).
}
\]

and on every stabilization fiber,

\[
\boxed{
\tau_F(x,z)
\le
\max(\tau_F(x,y),\tau_F(y,z)).
}
\]

Thus every canonical stabilization basin carries an integer ultrametric generated by first coalescence time, while every finite observation set reaches exact kernel and P011 collision-spectrum saturation in finite time.

This connects time, irreversibility, and geometry inside Enterprise Math through the same finite Pair/kernel mechanism rather than through a continuous limit or an external probabilistic model.
