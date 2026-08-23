# Prime-BRC General Floor-Observable Signed Jump Theorem

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOVELTY AUDIT INCOMPLETE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Setup

For `x>=1`, let

\[
\mathcal F(x)=
\left\{\left\lfloor\frac{x}{n}\right\rfloor:1\le n\le x\right\}.
\]

Let `A` be any subset of the positive integers, with indicator `1_A`. Define

\[
C_A(x)=|\mathcal F(x)\cap A|.
\]

For a label `m>=1`, define

\[
J_x(m)=
\left\lfloor\frac xm\right\rfloor-
\left\lfloor\frac{x}{m+1}\right\rfloor.
\]

Then

\[
m\in\mathcal F(x)\iff J_x(m)>0
\]

and

\[
J_x(m)-J_{x-1}(m)
=
\mathbf1_{m|x}-\mathbf1_{m+1|x}.
\]

## 2. Entry and exit conditions for an arbitrary label

A label `m` enters `F(x)` at the step `x-1 -> x` iff

\[
\boxed{m|x,\qquad x/m\le m.}
\]

Equivalently,

\[
\boxed{m|x,\qquad m^2\ge x.}
\]

A label `m` exits at the same step iff

\[
\boxed{m+1|x,\qquad x/(m+1)<m.}
\]

Equivalently, putting `e=m+1`,

\[
\boxed{e|x,\qquad e(e-1)>x.}
\]

The proofs are the same exact integer-floor arguments used in the branch-birth and signed prime-jump notes; no property of primality is used.

## 3. Main theorem — arbitrary observable subset

For every subset `A` of the positive integers and every `x>=2`,

\[
\boxed{
C_A(x)-C_A(x-1)
=
\sum_{\substack{d|x\\d^2\ge x}}\mathbf1_A(d)
-
\sum_{\substack{e|x\\e(e-1)>x}}\mathbf1_A(e-1).
}
\]

Equivalently,

```text
observable support change
= frontier births in A
- adjacent-frontier deaths whose old label lies in A.
```

### Proof

For each label `m`, the membership indicator `1_{m in F(x)}` can change only because `J_x(m)-J_{x-1}(m)` is `+1` or `-1`.

The entry criterion above characterizes exactly when the change is `0 -> 1`, and the exit criterion characterizes exactly when it is `1 -> 0`. Summing these membership changes over `m in A` gives the formula. ∎

## 4. Odd-step monotonicity for odd observables

Suppose `x` is odd and `A` contains only odd integers.

If `m in A`, then `m+1` is even and cannot divide odd `x`. Thus the entire exit sum vanishes:

\[
\boxed{
C_A(x)-C_A(x-1)
=
\sum_{\substack{d|x\\d^2\ge x}}\mathbf1_A(d)
\ge0.
}
\]

Therefore every odd-only floor observable is monotone nondecreasing on each odd step, and its exact jump is the number of observable upper-frontier divisors.

## 5. Prime specialization

Take `A=P`, the primes.

For odd `x>=5`, every odd prime has even successor and therefore cannot exit. The exceptional even prime `2` is already permanently present at these sizes. Thus

\[
G(x)-G(x-1)
=
\#\{p|x:p\text{ prime},\ p^2\ge x\}.
\]

This is the owner-local odd floor-prime jump theorem and yields Heyman's published three-prime conjecture as a corollary.

## 6. Full-support specialization

Take `A=N`. Then

\[
C_N(x)=|\mathcal F(x)|.
\]

The theorem gives the exact cardinality jump as upper-frontier divisor births minus adjacent-frontier exits. In particular, restricting only to the birth set recovers

\[
\mathcal F(x)\setminus\mathcal F(x-1)
=\{d|x:d^2\ge x\}.
\]

## 7. BRC interpretation

The theorem is a general observable-transport law on the same floor-quotient transition skeleton:

\[
\boxed{
\text{current exact support}
\xrightarrow{x-1\to x}
\text{signed boundary birth/death measure}
\xrightarrow{1_A}
\text{observable support jump}.
}
\]

No prime-specific ontology is required. Choosing `A` selects the observable only after the exact branch transition has been defined.

This matches the BRC layering rule:

```text
exact transition first
-> observable projection second
-> only then forget/recoalesce if future-safe.
```

## 8. Novelty boundary

Heyman's 2022 paper explicitly studies general indicator conditions for floor-function sequences and separately proves prime/semiprime set results, but the current audit did not locate this exact one-step arbitrary-subset jump formula. That is not a certified novelty claim.

Freeze:

`GENERAL_FLOOR_OBSERVABLE_SIGNED_JUMP_FORMULA = PROVED_OWNER_LOCAL`.

`ODD_ONLY_OBSERVABLE_HAS_NO_EXIT_CHANNEL_ON_ODD_STEPS = true`.

`NOVELTY_STATUS = AUDIT_INCOMPLETE`.
