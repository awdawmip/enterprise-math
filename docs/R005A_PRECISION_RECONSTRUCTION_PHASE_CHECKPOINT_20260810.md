# R005-A — Precision Reconstruction and Desert-Phase Checkpoint

Status: `PROVED STRUCTURAL CHECKPOINT / EXECUTABLE CHECKED / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`

This checkpoint continues the same R005-A owner generation. It does not open a new task and does not alter R005-B source ownership.

## 1. T-A38 — lattice-constrained cofactor reconstruction

Let

\[
A<n\le U,\qquad W=U-A,
\]

and suppose

\[
n=d\,c.
\]

If the future language knows

\[
c\equiv a\pmod m,
\]

then

\[
\boxed{dm\ge W}
\]

makes c unique.

Indeed two distinct same-residue cofactors differ by at least m, hence their
states differ by at least dm, while two states inside the half-open basin
differ by strictly less than W.

Let

\[
Q=\lfloor U/d\rfloor.
\]

The unique candidate is

\[
\boxed{
C_{U,d}^{m,a}
=
Q-((Q-a)\bmod m),
}
\]

and existence is exactly

\[
A<dC_{U,d}^{m,a}\le U.
\]

No primality assumption is used.

The local executable exhaustively checks **5,476,722** bounded parameter
tuples satisfying \(dm\ge W\), and separately records sharpness examples once
\(dm<W\).

## 2. T-A39 — exact square-basin reconstruction threshold

For

\[
A=k^2,\qquad U=k^2+2k,
\]

the width is \(W=2k\).

Residual cofactors are odd, so \(m=2\). Therefore

\[
\boxed{d\ge k}
\]

is enough to reconstruct the exact odd basin state from a known divisor
product d.

This unifies the earlier special closures:

- squarefree pair closure: \(d=ab\);
- repeated closure: \(d=q^2\).

The generic reason pair reconstruction works is therefore not “three primes”
by itself. It is:

\[
\boxed{
\text{partial divisor product}\times
\text{residue-lattice spacing}
\ge
\text{basin width}.
}
\]

The \(k=1781\) witness 101 remains an exact single-factor negative boundary:
one literal factor may alias several residual blocks, whereas its product with
a second residual factor crosses the reconstruction threshold.

## 3. T-A40 — reconstruction depth × collapse dimension

For a p-power basin

\[
A=k^p,\quad U=(k+1)^p-1,
\]

assume the r-root core is forced.

Every prime factor of a residual is then \(>U^{1/r}\). Knowing t such factor
coordinates gives divisor product

\[
d>U^{t/r}.
\]

With odd cofactor precision, a uniform sufficient reconstruction condition is

\[
2U^{t/r}\ge W.
\]

Asymptotically:

\[
\boxed{
\frac tr>1-\frac1p.
}
\]

At equality, the limiting ratio between available odd-lattice reconstruction
capacity and basin width is \(2/p\).

For a maximal residual of arity \(r-1\), reconstructing the final factor from
the first \(r-2\) therefore has generic asymptotic boundary

\[
\boxed{r>2p}.
\]

The critical line \(r=2p\) normally fails by constants for \(p>2\).

The square case is exceptional:

\[
\boxed{(p,r)=(2,4)}.
\]

Here the equality constant is exactly 1 and strict fourth-root factor
inequalities give

\[
ab>\sqrt U>k,
\]

so pair closure succeeds exactly.

Thus the unusually clean p=2 fourth-root pair geometry is a critical
alignment of:

- collapse width;
- root-core depth;
- residual arity;
- parity precision.

## 4. T-A41 — two-bottleneck prime-desert compression

For an ambient factor block \(N\), write

\[
h=N-A,\qquad W=U-A.
\]

For support witness q let

\[
M_q=N/q
\]

and define scaled prime clearances

\[
L_q=q(M_q-P^-(M_q)),
\]

\[
R_q=q(P^+(M_q)-M_q).
\]

The q-cofactor interval is prime-free exactly when

\[
h\le L_q,\qquad W-h<R_q.
\]

Define bottlenecks

\[
L_*=\min_q L_q,\qquad R_*=\min_q R_q.
\]

Then all e=1 witness deserts are simultaneous iff

\[
\boxed{
W-R_*<h\le L_*.
}
\]

Thus the full endpoint-clearance family factors through at most two
bottleneck witnesses.

## 5. T-A42/T-A43 — exact desert phase capacity

Define

\[
\boxed{\mu=L_*+R_*-W}.
\]

Because the phase interval has integer endpoints,

\[
W-R_*<h\le L_*
\]

contains exactly

\[
\boxed{\max(0,\mu)}
\]

integer phase values.

So \(\mu\) is an exact synchronized-desert **phase capacity**, not a heuristic
margin.

For an actual residual phase define

\[
\ell=h+R_*-W,\qquad u=L_*-h.
\]

Then

\[
\ell\ge1,\qquad u\ge0,
\]

and

\[
\boxed{\ell+u=\mu}.
\]

This gives a compact task-relative state for the e=1 layer.

## 6. Exact mechanism decomposition

Across the already-published 2497 ambient closure blocks in the 49 exact
certificate basins:

- 2440 have \(\mu\le0\): synchronized e=1 prime deserts are impossible;
- 57 have positive phase capacity;
- 7 of those miss the allowed phase interval;
- 50 survive and are exactly the residual blocks.

So the finite mechanism chain is

\[
\boxed{
2497
\to
57\text{ positive-capacity blocks}
\to
50\text{ residual blocks}.
}
\]

Among the 50 residuals:

- 30 use the same witness as both left and right bottleneck;
- 20 use different bottleneck witnesses.

This is finite evidence only; no density/asymptotic claim is made.

## 7. Relation to the existing closure-shadow normal form

The current p=2 stack is now:

\[
\text{ambient multiplicative closure}
\to
\text{lattice reconstruction threshold}
\to
\text{prime-clearance bottlenecks}
\to
\text{desert phase capacity}
\to
NF\text{ shadow}
\to
\text{residual repair}.
\]

The ambient pair/repeated closures are specializations of T-A38/T-A39, not
independent primitives.

The e=1 prime-gap data compress to T-A41/T-A43 only for the declared joint
prime-desert question. The discarded local gap data remain available for
other future languages.

## 8. Foundation feedback candidates

Candidate packets:

- **FF-R005A-11 — lattice cofactor reconstruction depth**
  - \(dm\ge W\) uniqueness;
  - p-power threshold \(t/r>1-1/p\);
  - maximal-residual boundary \(r>2p\);
  - exceptional exact point \((p,r)=(2,4)\).

- **FF-R005A-12 — synchronized desert phase capacity**
  - two-bottleneck compression;
  - \(\mu=L_*+R_*-W\) exact integer phase capacity;
  - \(\ell+u=\mu\) phase split.

Both are elementary arithmetic reductions. Novelty is unverified; any
Foundation value lies in the precision/future-language interface, not a claim
of new classical number theory.

## 9. Current boundary

Lean remains `LOCAL_LEAN_PENDING`.

No root import is added.

The next p=2 repair-complexity target remains the first basin with

\[
\tau(\mathcal R_k)\ge2.
\]

The useful search should now operate on **positive-capacity closure blocks**,
not all ambient blocks and not all composites.
