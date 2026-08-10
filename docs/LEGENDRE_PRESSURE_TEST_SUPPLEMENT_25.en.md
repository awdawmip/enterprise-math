# Legendre Pressure Test — Supplement 25

Status: `PROVED RESEARCH NOTE`  
Scope: universal one-symbol near-optimality of factor-first root/factor precision acquisition  
Depends on: P017 L064–L065 and P023-S16 bounded-repair scheduling approximation  
Discipline: this is a finite representation-cost theorem, not a complexity theorem for integer factorization and not a proof of Legendre's conjecture.

## 1. L065 removes universal exact optimality but leaves a stronger robust question

L065 proves that neither factor-first nor root-first is exactly optimal in every square basin.

However L064 also proves a universal structural bound:

\[
\boxed{
\rho(P,R)\le2.
}
\]

This asks a different question:

> even when factor-first is not exactly optimal, how far from optimal can it be?

The answer is uniformly one binary symbol.

## 2. L066-A — Factor-first is universally within one binary symbol of the final lower bound

Status: `PROVED`.

Let

\[
N_P=|X/P|,
\qquad
N_*=|X/(P\cap R)|.
\]

The factor-first binary depth is

\[
C_{P\to R}
=L_2(N_P)+L_2(\rho(P,R)).
\]

Because the joint precision refines the factor partition,

\[
N_P\le N_*.
\]

By L064,

\[
L_2(\rho(P,R))\le1.
\]

Therefore

\[
\boxed{
C_{P\to R}
\le
L_2(N_*)+1.
}
\]

So factor-first is universally at most one bit above the absolute joint-class cardinality lower bound.

## 3. L066-B — Factor-first is universally one-bit competitive with the optimal two-task order

Status: `PROVED`.

Let

\[
C_{\rm opt}
=
\min(C_{P\to R},C_{R\to P}).
\]

Any exact schedule must satisfy

\[
C_{\rm opt}\ge L_2(N_*).
\]

Combining with L066-A,

\[
\boxed{
C_{P\to R}-C_{\rm opt}
\le1.
}
\]

Thus the factor-first strategy is a certified additive-one approximation to the optimal two-task precision schedule in every square basin.

This is strictly stronger than a heuristic recommendation because the approximation gap is proved exactly.

## 4. L066-C — Every strict root-first advantage is exactly one bit

Status: `PROVED`.

Suppose root-first is strictly better:

\[
C_{R\to P}<C_{P\to R}.
\]

Both costs are integers. L066-A gives

\[
C_{P\to R}\le L_2(N_*)+1,
\]

while every exact schedule satisfies

\[
C_{R\to P}\ge L_2(N_*).
\]

Strict inequality leaves only one possibility:

\[
\boxed{
C_{R\to P}=L_2(N_*),
\qquad
C_{P\to R}=L_2(N_*)+1.
}
\]

Hence root-first can beat factor-first, but never by more than one binary symbol.

The `k=11` witness from L065 realizes this equality case.

## 5. L066-D — Base-B form

Status: `PROVED`.

Because

\[
2\le B
\]

for every integer base `B>=2`, L064 also gives

\[
L_B(\rho(P,R))\le1.
\]

Therefore

\[
\boxed{
C^{(B)}_{P\to R}
\le
L_B(N_*)+1
}
\]

in every base `B>=2`.

Thus the robust approximation theorem is not specifically binary; binary coding is simply the sharp smallest-alphabet instance.

## 6. Relation to L065's opposite witnesses

At `k=11`,

\[
C_{R\to P}=3,
\qquad
C_{P\to R}=4,
\qquad
L_2(N_*)=3.
\]

So root-first attains the lower bound and factor-first is exactly one bit above it.

At `k=1737`,

\[
C_{P\to R}=9,
\qquad
C_{R\to P}=10,
\qquad
L_2(N_*)=8.
\]

Here factor-first wins, although it still has one bit of unavoidable stagewise worst-case slack relative to the raw final-class bound.

Together these examples show:

\[
\boxed{
\text{no universal exact optimum}
\quad\text{but}\quad
\text{universal factor-first additive-one guarantee}.
}
\]

## 7. Why this is a stronger research-tool outcome

A common failure mode is to react to a counterexample to exact optimality by abandoning all structural guidance.

L066 shows the better response:

1. keep the counterexample — exact optimality is false;
2. identify the structural directed bound — `rho(P,R)<=2`;
3. convert it into a certified approximation theorem;
4. reserve exact scheduling only for basins where one bit matters to the downstream proof.

This separates theorem-backed near-optimality from brittle universal heuristics.

## 8. Consequence for P017 proof architecture

If later P017 recursion needs both least-prime shell and cofactor-root coordinates, factor-first is always a safe representation choice in the following precise sense:

\[
\boxed{
\text{its binary acquisition depth is at most optimum}+1.
}
\]

Therefore one may use factor-first as a robust default in proof architecture without claiming it is exactly optimal in every basin.

Where exact one-bit savings matter, L065/S14 can still choose root-first instance by instance.

## 9. Executable audit

`tests/test_p017_root_factor_schedule.py` checks both opposite-optimum witnesses and verifies on a bounded range that both schedule costs respect the final lower bound.

A future regression may additionally assert the universal bounded-range version

\[
C_{P\to R}\le L_2(N_*)+1
\]

as an implementation guard; the theorem itself follows immediately from L064 and does not depend on finite enumeration.

## 10. Tool feedback

The result is the P017 specialization of P023-S16:

\[
\boxed{
\text{bounded directed repair}
\Longrightarrow
\text{certified additive scheduling approximation}.
}
\]

This closes another abstraction loop: a number-theoretic two-basin transport theorem becomes a general precision bound, which returns as a robust number-theoretic scheduling guarantee.
