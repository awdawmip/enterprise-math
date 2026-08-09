# Legendre Pressure Test — Supplement 11

Status: `ACTIVE RESEARCH NOTE`  
Scope: centered mirror-pair separation and transverse-prime resource accounting across distinct basin states  
Depends on: P017 L001, anchor cancellation, and the canonical transverse-support language  
Discipline: **this note does not prove Legendre's conjecture.** The results below are exact cross-state constraints; the final incidence inequality is only a necessary condition for a hypothetical counterexample.

## 1. Centered mirror decomposition

Let

\[
M=k(k+1),
\qquad
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

Then

\[
I_k=M+\{1-k,\ldots,k\}.
\]

For each

\[
1\le r\le k-1,
\]

define the mirror pair

\[
M-r,\qquad M+r.
\]

These give exactly \(k-1\) pairs. The two unpaired states are

\[
M=k(k+1)
\]

and

\[
M+k=k(k+2),
\]

both composite for \(k\ge2\).

Thus any prime witness in the square basin must lie in one of the mirror pairs.

Let \(A_k\) be the product of the primes \(p\le k\) dividing \(M\). A prime \(p\le k\) is **transverse** when \(p\nmid M\).

---

## 2. L042 — Anchor survival is pairwise all-in or all-out

Status: `PROVED`.

Because \(A_k\mid M\), for every radius \(1\le r<k\),

\[
\boxed{
\gcd(M-r,A_k)
=
\gcd(r,A_k)
=
\gcd(M+r,A_k).
}
\]

Therefore

\[
\boxed{
\gcd(r,A_k)=1
\iff
\gcd(M-r,A_k)=\gcd(M+r,A_k)=1.
}
\]

So the anchor sieve never removes only one side of a centered mirror pair: both sides survive or both fail together.

### Proof

For any integer \(x\), \(\gcd(M\pm x,A_k)=\gcd(x,A_k)\) because \(A_k\mid M\). Set \(x=r\). ∎

---

## 3. L043 — Transverse mirror supports are disjoint

Status: `PROVED`.

For every radius \(1\le r<k\),

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(M-r)
\cap
\operatorname{Supp}_{\mathrm{tr}}(M+r)
=arnothing.
}
\]

This statement does not require anchor survival.

### Proof

Suppose a transverse prime \(p\le k\) divided both mirror states. Then

\[
p\mid(M+r)-(M-r)=2r.
\]

Since \(M=k(k+1)\) is even, the prime \(2\) divides \(M\) and is therefore not transverse. Hence \(p\) is odd, so \(p\mid r\). Combining \(p\mid r\) with \(p\mid M-r\) yields \(p\mid M\), contradicting transversality. ∎

Therefore no transverse small-prime resource can cover both sides of the same mirror pair.

### Stronger corollary: surviving mirror triples are pairwise coprime

If \(\gcd(r,A_k)=1\), then

\[
\boxed{
\gcd(M-r,M)=
\gcd(M,M+r)=
\gcd(M-r,M+r)=1.
}
\]

Indeed any prime dividing both \(M\) and \(r\) is at most \(r<k\), hence belongs to \(A_k\), contradicting anchor survival. Thus \(\gcd(M,r)=1\). Also \(2\mid A_k\), so a surviving \(r\) is odd; the two mirror states are odd. Any common divisor of \(M-r\) and \(M+r\) is therefore odd and divides both \(2M\) and \(2r\), hence divides \(M\) and \(r\), so it is one.

This stronger corollary will be the clean input to the later CRT/idempotent layer.

---

## 4. L044 — A surviving double-composite mirror pair consumes two distinct transverse resources

Status: `PROVED CONDITIONAL CONSEQUENCE`.

Assume

\[
\gcd(r,A_k)=1
\]

and both mirror states

\[
M-r,\qquad M+r
\]

are composite.

Each lies in the open square basin, so the root-factor horizon gives each state at least one prime divisor not exceeding \(k\). By L042 the two states survive the anchor sieve, so those small factors cannot be anchor primes; they are transverse. By L043 the two transverse supports are disjoint.

Therefore both supports are nonempty and disjoint, and in particular

\[
\boxed{
|\operatorname{Supp}_{\mathrm{tr}}(M-r)|
+
|\operatorname{Supp}_{\mathrm{tr}}(M+r)|
\ge2.
}
\]

Example: for \(k=20\), \(M=420\), \(r=17\),

\[
403=13\cdot31,
\qquad
437=19\cdot23.
\]

The small transverse factors are \(13\) and \(19\), one on each side.

---

## 5. L045 — Basin-level transverse-incidence necessary condition

Status: `PROVED AS A NECESSARY CONDITION; NOT A CONTRADICTION`.

Define the surviving radii

\[
S_k
=
\{r:1\le r<k,\ \gcd(r,A_k)=1\}.
\]

Define the total transverse small-prime incidence across surviving mirror states by

\[
J_k
=
\sum_{r\in S_k}
\left(
|\operatorname{Supp}_{\mathrm{tr}}(M-r)|
+
|\operatorname{Supp}_{\mathrm{tr}}(M+r)|
\right).
\]

If the open square basin contained no prime, then every mirror state would be composite; the two unpaired states are already composite. Applying L044 to every surviving radius gives

\[
\boxed{J_k\ge2|S_k|.}
\]

This is only a necessary condition for a hypothetical Legendre counterexample. No upper bound contradicting it is claimed.

### Prime-indexed reindexing

For a transverse prime \(p\le k\), define

\[
N_p(k)
=
\#\{r\in S_k:p\mid M-r\ \text{or}\ p\mid M+r\}.
\]

L043 guarantees that for a fixed pair \((p,r)\), the two alternatives cannot both occur. Hence ordinary double counting gives

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

The left side is state-indexed; the right side is prime-indexed. This is an exact cross-state resource identity.

---

## 6. What this adds beyond the current least-factor window route

The current high-band P017 results separate cofactor supports **within one least-factor shell**. L042–L045 instead relate two different basin states geometrically located at opposite centered offsets.

The new object is not another sieve count. It is the cross-state constraint

\[
\boxed{
\text{one surviving radius}
\longrightarrow
\text{two states}
\longrightarrow
\text{disjoint transverse supports}.
}
\]

This can be combined later with the exact-support closure of L041 and the bounded CRT sign-pattern capacity, but neither of those later tools is required for L042–L045 themselves.

The first incidence moment L045 is unlikely to prove Legendre by itself. The useful next question is whether second-order overlap/capacity constraints prevent enough distinct mirror pairs from all being double-composite simultaneously.

---

## 7. Executable validation

`src/enterprise_math/p017_mirror.py`, `src/enterprise_math/p017_mirror_incidence.py`, and their tests check that:

- the basin is exactly \(k-1\) mirror pairs plus the two known composite states;
- anchor survival is pairwise all-in/all-out;
- transverse supports on opposite sides are disjoint over bounded domains;
- every tested surviving double-composite pair has two nonempty disjoint transverse supports;
- the state-indexed and prime-indexed incidence totals agree;
- surviving mirror triples are pairwise coprime.

Finite tests audit the implementation; L042–L045 follow from the elementary integer proofs above.
