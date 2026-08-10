# Legendre Pressure Test — Supplement 23

Status: `PROVED RESEARCH NOTE`  
Scope: directed precision geometry between least-prime shell identity and stripped-cofactor root  
Depends on: P018 all-power two-basin quotient theorem, P017 exact p-rough cofactor windows, P023-S12 directed repair geometry  
Discipline: this is a structural theorem about finite square-basin state representations. It does not prove Legendre's conjecture and does not by itself prescribe a globally optimal factoring algorithm.

## 1. Two task coordinates on the same composite states

For a composite state

\[
k^2<n<(k+1)^2,
\]

write

\[
p=\operatorname{spf}(n),
\qquad
q=n/p.
\]

Compare two retained task coordinates:

\[
P(n)=p
\]

and

\[
R(n)=R_2(q).
\]

`P` records the least-prime shell; `R` records the integer square-root basin of the exact stripped cofactor.

P023-S12 gives two different directed repair factors:

\[
\rho(P,R)
\]

for adding root after factor identity is known, and

\[
\rho(R,P)
\]

for recovering factor identity after only the root is retained.

There is no reason for these directions to have the same cost.

## 2. L064-A — Factor-to-root repair is universally binary

Status: `PROVED`.

For every square basin with at least one composite state,

\[
\boxed{
\rho(P,R)\le2.
}
\]

Equivalently, once the least prime `p` is known, the stripped cofactor root needs at most one additional binary repair symbol.

### Proof

Fix one least-prime shell `p`.

Every state in that shell has the form

\[
n=pq
\]

with `n` inside the single source square basin indexed by `k`.

Forget the p-rough restriction for a moment and apply the P018 all-power quotient theorem with exponent `2` and divisor `p` to the whole source basin. It says

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
\in\{j_p,j_p+1\}
\]

for one base target root `j_p` depending only on `k,p`.

On an actual `p` shell, `n` is divisible by `p`, so

\[
\left\lfloor\frac np\right\rfloor=q.
\]

The p-rough realizability filter only removes quotient states; it cannot create a third root value. Thus every `P=p` block meets at most two `R` blocks.

Taking the maximum incidence degree gives

\[
\rho(P,R)\le2.
\]

∎

## 3. L064-B — The binary bound is sharp

Status: `PROVED BY EXPLICIT WITNESS`.

Take

\[
k=18,
\qquad
p=7.
\]

Both

\[
329=7\cdot47
\]

and

\[
343=7\cdot49
\]

lie in

\[
(18^2,19^2)=(324,361),
\]

and both have least prime factor `7`.

But

\[
R_2(47)=6,
\qquad
R_2(49)=7.
\]

Therefore one factor block meets two root blocks and

\[
\boxed{
\rho(P,R)=2
}
\]

for this basin.

So the universal one-bit upper bound cannot be improved to zero repair.

## 4. L064-C — The reverse direction can require at least eight symbols

Status: `PROVED BY EXPLICIT WITNESS`.

At

\[
k=1737,
\qquad
R=45,
\]

the same cofactor-root fiber contains the following eight realized least-prime shells:

\[
\boxed{
1429,1439,1447,1451,1459,1471,1481,1489.
}
\]

Explicit witnesses are:

| `p` | prime cofactor `q` | `n=pq` | `R_2(q)` |
|---:|---:|---:|---:|
| 1429 | 2113 | 3019477 | 45 |
| 1439 | 2099 | 3020461 | 45 |
| 1447 | 2087 | 3019889 | 45 |
| 1451 | 2081 | 3019531 | 45 |
| 1459 | 2069 | 3018671 | 45 |
| 1471 | 2053 | 3019963 | 45 |
| 1481 | 2039 | 3019759 | 45 |
| 1489 | 2027 | 3018203 | 45 |

All listed `p,q` are prime, `p<q`, and every product lies in

\[
(1737^2,1738^2)
=(3017169,3020644).
\]

Hence every product has least prime factor `p`, and all stripped cofactors lie in root basin `45`.

Therefore

\[
\boxed{
\rho(R,P)\ge8.
}
\]

The executable full-basin audit shows that `8` is in fact the maximum at this `k`.

## 5. Directed binary depth asymmetry

Using the S12 base-two depth

\[
d_2(E,F)=L_2(\rho(E,F)),
\]

L064-A and the `k=1737` witness give

\[
\boxed{
d_2(P,R)=1,}
\]

while

\[
\boxed{
d_2(R,P)=3.}
\]

Thus the same pair of task coordinates can have a threefold difference in directed binary symbol depth.

This is a strict number-theoretic instance of the general S12 statement that precision geometry is directed before symmetrization.

## 6. Raw-envelope reverse burden is provably unbounded

Supplement 21 proves that if the p-rough realizability filter is dropped and every exact cofactor-window label is treated as possible, then along the square-of-square diagonal the root-to-factor raw burden is unbounded.

Therefore

\[
\boxed{
\sup \rho(R,P)_{\rm raw}=\infty.
}
\]

For **realized** least-prime shells, Supplement 22 reduces diagonal unboundedness to two restricted Goldbach slices and leaves that question open.

So the current hierarchy is:

- factor-to-root actual repair: universally at most `2`;
- root-to-factor actual repair: at least `8` by explicit witness, unboundedness open;
- root-to-factor raw-window repair: provably unbounded.

## 7. Why the asymmetry matters for P017 recursion

Once a least-prime shell is already known, passing to the cofactor root is a uniformly bounded operation: at most one bit of residual root ambiguity remains.

The reverse move is qualitatively different. Root collapse can merge many distinct factor shells, so reconstructing shell identity afterward may require a much larger alphabet.

Hence

\[
\boxed{
\text{factor known}\to\text{root}
\quad\text{is uniformly cheap,}
}
\]

while

\[
\boxed{
\text{root known}\to\text{factor identity}
\quad\text{need not be.}
}
\]

This gives a concrete theorem-level reason to preserve shell identity before aggressive root compression when later recursion still needs that identity.

## 8. Scheduling boundary

The directed inequality does **not** by itself prove that a full algorithm should always compute least-prime identity before root.

S14 shows that total acquisition cost depends on the entire task family and current context. The initial cost of obtaining `P` may differ from the initial cost of obtaining `R`.

L064 only proves the conditional translation costs once one of those coordinates is already known.

This distinction is essential:

\[
\boxed{
\text{cheap conditional repair}
\neq
\text{globally optimal first task}.
}
\]

## 9. Executable specification

- `src/enterprise_math/p017_directional_root_factor_precision.py`
- `tests/test_p017_directional_root_factor_precision.py`

Regression verifies `rho(P,R)<=2` through a broad finite range, pins the sharp `k=18,p=7` two-root witness, and checks the exact `k=1737` directed factors `2` and `8`, hence binary depths `1` and `3`.

## 10. Tool feedback

This result closes another research-tool loop:

\[
\boxed{
\text{P018 two-basin transport}
\to
\text{P023 incidence geometry}
\to
\text{P017 directed precision theorem}.
}
\]

The abstract repair metric is therefore not merely a bookkeeping device. It exposes a concrete asymmetry in number-theoretic state compression that was not explicit in the original quotient-window formulation.
