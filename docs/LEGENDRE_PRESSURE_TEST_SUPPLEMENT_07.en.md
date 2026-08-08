# Legendre Pressure Test — Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: cross-state mirror separation around the common square-basin center and the resulting transverse-prime resource condition.  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. A different kind of basin structure

The previous supplements studied support products, Möbius tails, and their half-scale duals. Those tools remain useful, but the next obstruction must involve more than one state at a time.

Write

\[
M=k(k+1).
\]

Then the square basin has the exact centered form

\[
I_k=M+\{1-k,\ldots,k\}.
\]

For every

\[
1\le r\le k-1,
\]

the two states

\[
M-r,\qquad M+r
\]

both lie strictly between \(k^2\) and \((k+1)^2\). These are the mirror pairs.

The two unpaired states are

\[
M=k(k+1)
\]

and

\[
M+k=k(k+2),
\]

which are both composite for \(k\ge2\). Therefore all possible prime witnesses, apart from the trivial \(k=1\) case, live in the mirror pairs.

## 2. L026 — Anchor survival is pairwise all-in or all-out

Status: `PROVED`

Let \(A_k\) be the product of the small anchor primes, i.e. the primes \(p\le k\) dividing \(M=k(k+1)\).

For every radius \(1\le r\le k-1\),

\[
\gcd(M-r,A_k)
=
\gcd(r,A_k)
=
\gcd(M+r,A_k).
\]

This is immediate from \(A_k\mid M\).

Hence

\[
\boxed{
\gcd(r,A_k)=1
\iff
\gcd(M-r,A_k)=\gcd(M+r,A_k)=1.
}
\]

So anchor elimination never removes only one side of a mirror pair. A mirror pair either survives the anchor sieve on both sides or fails it on both sides.

## 3. L027 — Transverse mirror-support separation

Status: `PROVED`

Let \(p\le k\) be a transverse prime:

\[
p\nmid M.
\]

Because \(M=k(k+1)\) is always even, \(p\neq2\), so \(p\) is odd.

Suppose, for contradiction, that \(p\) divides both mirror states:

\[
p\mid M-r,
\qquad
p\mid M+r.
\]

Then

\[
p\mid2r.
\]

Since \(p\) is odd,

\[
p\mid r.
\]

Combining this with \(p\mid M-r\) gives

\[
p\mid M,
\]

contradicting transversality.

Therefore

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(M-r)
\cap
\operatorname{Supp}_{\mathrm{tr}}(M+r)
=arnothing.
}
\]

This is stronger than saying a large modulus cannot hit twice. **No individual transverse small prime can occur on both sides of the same mirror pair**, regardless of how small that prime is.

## 4. L028 — A surviving composite mirror pair requires two distinct transverse resources

Status: `PROVED CONDITIONAL CONSEQUENCE`

Assume

\[
\gcd(r,A_k)=1,
\]

so the mirror pair survives anchor elimination.

If both

\[
M-r,\qquad M+r
\]

are composite, each lies inside the square basin, so the root-factor horizon gives each state at least one prime factor not exceeding \(k\).

Because the pair survives the anchor sieve, such a small factor cannot be an anchor prime. It must be transverse.

By L027, the two transverse supports are disjoint. Hence the pair requires at least two distinct transverse small-prime resources:

\[
\boxed{
\omega_{\mathrm{tr}}(M-r)
+
\omega_{\mathrm{tr}}(M+r)
\ge2.
}
\]

More strongly, the two nonempty supports are disjoint sets.

Example: for \(k=20\), \(M=420\), and \(r=17\),

\[
M-r=403=13\cdot31,
\qquad
M+r=437=19\cdot23.
\]

Only the small factors \(13\) and \(19\) lie below \(k\), and they are distinct transverse resources on opposite sides.

## 5. L029 — Basin-level transverse incidence necessary condition

Status: `PROVED AS A NECESSARY CONDITION; NOT A CONTRADICTION`

Define the surviving radii

\[
S_k
=
\{1\le r\le k-1:\gcd(r,A_k)=1\}.
\]

Define the total transverse small-prime incidence across all surviving mirror states:

\[
J_k
=
\sum_{r\in S_k}
\left(
\omega_{\mathrm{tr}}(M-r)
+
\omega_{\mathrm{tr}}(M+r)
\right).
\]

If Legendre's conjecture failed at this particular \(k\), every mirror state would be composite because the two unpaired basin states are already known composites. L028 would then force

\[
\boxed{
J_k\ge2|S_k|.
}
\]

This is only a necessary condition for a hypothetical counterexample. We do **not** currently prove an upper bound contradicting it.

### Prime-indexed reindexing

The same \(J_k\) can be counted by transverse primes instead of mirror states. For a transverse prime \(p\le k\), let

\[
N_p(k)
=
\#\left\{
r\in S_k:
 p\mid M-r\ \text{or}\ p\mid M+r
\right\}.
\]

L027 guarantees that for a fixed radius the two alternatives never occur simultaneously. Therefore

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

This is a genuine basin-level resource accounting identity: the left side is indexed by states, the right side by transverse primes.

A proof strategy based on L029 would need more than the first incidence moment. The naive capacity sum is expected to be too large. The missing ingredient is a second-order restriction on how different transverse primes can jointly cover the same side while respecting mirror separation on the opposite side.

## 6. Why this is different from the previous support formulas

L023–L025 use the common anchor to decide whether a large support product hits the basin. L026–L029 instead constrain **two different states at once**, even for very small prime factors.

The new structure is:

\[
\boxed{
\text{anchor survival of a radius}
\Longrightarrow
\text{two surviving states}
\Longrightarrow
\text{disjoint transverse supports}.
}
\]

This property cannot be seen by studying either state in isolation.

## 7. Next target

The first-moment inequality L029 is unlikely to be sufficient by itself. The next attack should therefore measure collision structure on each side of the mirror pair while preserving cross-side disjointness.

A concrete target is to define a pair-level collision gain

\[
\Gamma_r
=
\bigl(	ext{transverse incidences on both sides}\bigr)
-
\bigl(	ext{distinct covered sides}\bigr),
\]

then ask whether mirror separation forces a basin-level lower or upper bound on

\[
\sum_{r\in S_k}\Gamma_r
\]

stronger than ordinary one-interval inclusion-exclusion.

The four-support half-scale graph and smooth-cofactor closure remain available as local descriptions of high-collision states; mirror separation supplies the missing cross-state constraint.

## 8. Executable validation

`src/enterprise_math/mirror.py`, `src/enterprise_math/mirror_incidence.py`, and their tests verify over bounded domains that:

- the basin partitions into \(k-1\) mirror pairs plus the two known composite states;
- anchor gcd is identical on both sides and on the radius;
- transverse supports of every tested mirror pair are disjoint;
- a surviving composite pair has nonempty disjoint small-prime supports;
- state-indexed and prime-indexed transverse incidence totals agree exactly.

The proofs of L026–L029 are elementary integer arguments; bounded tests validate the executable reference implementation.
