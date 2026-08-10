# P025 Supplement 73 — Centered-Prime Duality for the `(2,2)` Difference Atom

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplement 72; canonical P018 centered-prime-radius layer  
Hard block: `NONE`

## 1. Switch from prime bases to centered-prime coordinates

Take the cutoff-five `(2,2)` difference shell with distinct odd primes

\[
p>q.
\]

The two prime-power complements are

\[
q^2,\qquad p^2,
\]

and the active difference component is

\[
N=p^2-q^2.
\]

Introduce the centered-prime coordinates already used by P018:

\[
\boxed{
B=\frac{p+q}{2},
\qquad
A=\frac{p-q}{2}.
}
\]

Then

\[
q=B-A,
\qquad
p=B+A.
\]

Because `p,q` are distinct odd primes,

\[
\boxed{\gcd(A,B)=1}
\]

and `A,B` have opposite parity.

## 2. P025-T142 — exact closed projective value

The P025 active component becomes

\[
\boxed{N=4AB.}
\]

Since `A,B` are coprime and exactly one is even,

\[
\operatorname{rad}(4AB)
=
\operatorname{rad}(A)\operatorname{rad}(B),
\]

so

\[
\boxed{
m(4AB)=4m(A)m(B).}
\]

The two complement capacities are both two. Hence their cross-capacity is

\[
K=2p+2q=4B.
\]

Therefore the active side projective term is

\[
\rho_{(2,2),-}
=
\frac{m(4AB)}{4B}
=
\boxed{\frac{m(A)}{\operatorname{rad}(B)}}.
\]

Thus threshold `T` is exact in centered coordinates:

\[
\boxed{
\rho_{(2,2),-}\ge T
\iff
m(A)\ge T\operatorname{rad}(B).
}
\]

No factorization of the large component `p^2-q^2` is needed once `(A,B)` is known.

## 3. P018 and P025 read dual quadratic coordinates

The same centered prime pair gives the P018 difference-of-squares shell

\[
\boxed{
(B-A)(B+A)=B^2-A^2=pq.
}
\]

P025 instead reads the difference of the **prime squares**:

\[
\boxed{
(B+A)^2-(B-A)^2=4AB=p^2-q^2.
}
\]

So the two routes share one coordinate chart but observe complementary quadratic forms:

\[
\boxed{
(B,A)
\mapsto
(B^2-A^2,\ 4AB).
}
\]

This is a concrete cross-route bridge rather than a notation coincidence.

## 4. Boundary: shared coordinates do not mean shared minimal radius

P018's canonical factor-proof-slack theorem identifies its special radius only under additional hypotheses, including

\[
q=B-A>A^2,
\]

and, for the exact slack equivalence, minimality of the centered prime radius.

P025-T142 needs neither condition. Any odd centered prime pair gives the projective identity.

Therefore P025 must **not** identify its radius `A` with P018 factor-proof slack merely because the coordinates agree.

The valid relation is:

- common centered-prime coordinate system: always;
- P018 centered shell data: when `q>A^2`;
- P018 minimal-slack identification: only when the stronger canonical P018 hypotheses are also satisfied.

## 5. Exact working examples

### Outside the P018 size range

Take

\[
q=5,\qquad p=59.
\]

Then

\[
(B,A)=(32,27).
\]

P018's underlying product coordinate is

\[
B^2-A^2=295=5\cdot59.
\]

P025's active component is

\[
4AB=3456=59^2-5^2.
\]

The projective value is

\[
\boxed{
\rho=\frac{m(27)}{\operatorname{rad}(32)}
=\frac92.
}
\]

The radius is far outside `q>A^2`, so no P018 factor-slack claim is made.

### Inside the canonical P018 size range

Take

\[
q=73,\qquad p=89.
\]

Then

\[
(B,A)=(81,8),
\qquad
73>8^2.
\]

The P018 shell state is

\[
\boxed{81^2-8^2=6497=73\cdot89.}
\]

The P025 active component is

\[
\boxed{89^2-73^2=2592=4\cdot81\cdot8.}
\]

and

\[
\boxed{
\rho=\frac{m(8)}{\operatorname{rad}(81)}
=\frac43>1.
}
\]

Thus an activated P025 `(2,2)` atom occurs genuinely inside the P018 centered theorem range.

Another example is

\[
(q,p)=(503,521),
\quad
(B,A)=(512,9),
\]

with

\[
\rho=3/2.
\]

## 6. Precision interpretation

Stage 72 said exponent precision was exhausted and a new coordinate family was required. P025-T142 shows one successful switch:

\[
(p,q,e=f=2)
\to
(B,A)
\to
(m(A),\operatorname{rad}(B)).
\]

For the projective-threshold query, the full prime bases `p,q` are no longer needed once the centered radius residual and center radical are known.

At the same time, P018 uses the same `(B,A)` to answer a different shell/factor question. This is another example where one coordinate chart supports multiple future languages with different minimal derived states.

## 7. Prior-art / ownership boundary

Centered prime pairs, difference-of-squares algebra and the P018 centered-prime-radius machinery are established/canonical in their respective scopes. P025 claims no new coordinate system.

The project-specific result is the exact reduction of the `(2,2)` projective difference atom to `m(A)/rad(B)` and its cross-route comparison with P018's quadratic shell. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_prime_square_centered_bridge.py`;
- `tests/test_abc_prime_square_centered_bridge.py`.

The executable bridge calls the canonical P018 centered-prime helper when its explicit size hypothesis is satisfied and preserves the boundary otherwise.

## 9. Next frontier

No hard block exists. Continue with:

1. exploit the P018 size inequality `A^2<q<B` together with `m(A)>=T rad(B)` to sharpen counting on the overlap slice;
2. compare whether P018's factor-proof slack or P025's projective ratio gives the cheaper future state on centered pairs satisfying both routes;
3. search analogous coordinate switches for `(3,3)` through sum/difference-of-cubes factorization;
4. Relay this bridge to P018 as `COMPOSABLE_INDEPENDENT`, not as a mother-theorem ownership transfer.
