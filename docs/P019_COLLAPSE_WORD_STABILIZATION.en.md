# P019 — Exact stabilization of fixed collapse words

Status: `PROVED`  
Problem: `P019`  
Scope: ordinary mathematics

## 1. Question

P004 classifies the fixed points of a finite collapse word

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}.
\]

Let

\[
L=\operatorname{lcm}(p_1,\ldots,p_m),
\]

with the empty word assigned \(L=1\) and \(W=\operatorname{id}\).

P004 proves

\[
\operatorname{Fix}(W)=\operatorname{Fix}(C_L).
\]

P019 asks the stronger dynamical question:

> If the same word is iterated repeatedly from \(n_0\), which fixed point is reached?

The answer is exact:

\[
\boxed{
W^t(n_0)\text{ is eventually constant at }C_L(n_0).
}
\]

The proof is best understood through a more general order-theoretic mother theorem.

## 2. Mother theorem: iterative coreflection on a well-founded poset

Let \((X,\le)\) be a partial order whose strict order \(<\) is well founded. Let

\[
F:X\to X
\]

be monotone and reductive:

\[
x\le y\Longrightarrow F(x)\le F(y),
\qquad
F(x)\le x.
\]

For an initial state \(x_0\), define

\[
x_{t+1}=F(x_t).
\]

### P019-T01 — Finite stabilization

Status: `PROVED`

Every orbit stabilizes after finitely many strict decreases. There is a state \(z\) and an integer \(T\) such that

\[
x_t=z
\qquad(t\ge T),
\]

and

\[
F(z)=z.
\]

### Proof

Reductivity gives

\[
x_0\ge x_1\ge x_2\ge\cdots.
\]

Whenever \(x_{t+1}\ne x_t\), antisymmetry converts \(x_{t+1}\le x_t\) into the strict decrease

\[
x_{t+1}<x_t.
\]

An infinite sequence of strict decreases would contradict well-foundedness. Hence only finitely many strict decreases occur, after which the orbit is constant. The constant value is a fixed point. ∎

### P019-T02 — Greatest fixed point below the initial state

Status: `PROVED`

The stabilized state \(z\) is the greatest fixed point of \(F\) not exceeding \(x_0\):

\[
\boxed{
z=\max\{y\in X:F(y)=y,\ y\le x_0\}.}
\]

### Proof

Let \(y\) be any fixed point with \(y\le x_0\). We prove inductively that

\[
y\le x_t
\]

for every \(t\). It holds at \(t=0\). If \(y\le x_t\), monotonicity gives

\[
y=F(y)\le F(x_t)=x_{t+1}.
\]

When the orbit stabilizes at \(z\), this yields \(y\le z\). Since \(z\) itself is fixed and \(z\le x_0\), it is the greatest fixed point below the initial state. ∎

Thus repeated application of a monotone reductive map does not converge to an arbitrary fixed point. On a well-founded partial order it computes the canonical downward fixed-point projection determined by the fixed set.

## 3. Collapse words satisfy the mother theorem

Each positive-exponent collapse \(C_p\) is monotone by T009 and reductive by T004. Therefore every finite collapse word \(W\) is monotone and reductive.

The natural-number order is well founded in the required descending sense. Hence P019-T01 and P019-T02 apply directly.

P004 supplies the missing fixed-set identification:

\[
\operatorname{Fix}(W)=\operatorname{Fix}(C_L)
=\{a^L:a\in\mathbb N\}.
\]

The greatest member of this set below \(n_0\) is exactly \(C_L(n_0)\).

## 4. Exact collapse-word stabilization

### P019-T03 — Exact lcm-limit theorem

Status: `PROVED`

For every finite positive-exponent collapse word \(W\), every initial state \(n_0\in\mathbb N\), and

\[
L=\operatorname{lcm}(p_1,\ldots,p_m),
\]

there exists a finite \(T\) such that

\[
\boxed{
W^t(n_0)=C_L(n_0)
\qquad\text{for all }t\ge T.
}
\]

For the empty word, \(L=1\) and \(C_1=\operatorname{id}\), so the theorem remains valid.

### Proof

By P019-T02, iteration stabilizes at the greatest fixed point of \(W\) below \(n_0\). P004 identifies those fixed points as the perfect \(L\)-th powers. By definition, the greatest perfect \(L\)-th power below \(n_0\) is \(C_L(n_0)\). ∎

This is stronger than merely showing that every orbit eventually reaches some perfect \(L\)-th power.

## 5. Persistent lower-bound proof

The same theorem admits a useful specialized proof that makes the invariant explicit.

Set

\[
a=C_L(n_0).
\]

Every exponent \(p_i\) divides \(L\), so every perfect \(L\)-th power is a perfect \(p_i\)-th power. Hence each generator fixes \(a\), and therefore

\[
W(a)=a.
\]

Since \(a\le n_0\) and \(W\) is monotone,

\[
a=W(a)\le W(n_0)=n_1.
\]

Inductively,

\[
a\le n_t
\]

for every \(t\). Thus the entire orbit remains trapped inside

\[
[C_L(n_0),n_0].
\]

When the orbit stabilizes at a perfect \(L\)-th power \(z\), maximality of \(C_L(n_0)\) gives \(z\le C_L(n_0)\), while the invariant gives the reverse inequality. Hence \(z=C_L(n_0)\).

## 6. Convergence bound and cycles

### P019-T04 — Strict-decrease bound

Status: `PROVED`

The number of nonstationary iterations is at most

\[
n_0-C_L(n_0).
\]

### Proof

Every nonstationary iteration strictly decreases the natural-number state by at least one, while the persistent lower bound prevents the orbit from falling below \(C_L(n_0)\). ∎

The bound is deliberately coarse. Sharper word-sensitive convergence bounds remain a separate quantitative problem.

### P019-T05 — No nontrivial periodic cycles

Status: `PROVED`

Every periodic point of a fixed collapse word is already a fixed point.

### Proof

If an orbit forms a cycle

\[
n_0\mapsto n_1\mapsto\cdots\mapsto n_{r-1}\mapsto n_0,
\]

reductivity gives

\[
n_0\ge n_1\ge\cdots\ge n_{r-1}\ge n_0.
\]

Antisymmetry forces equality throughout. ∎

## 7. Exact eventual basins

### P019-T06 — Eventual basin theorem

Status: `PROVED`

For a fixed word with lcm exponent \(L\), the eventual attractor reached from \(n\) is \(C_L(n)\). Therefore the eventual basin of \(k^L\) is exactly

\[
\boxed{
\{n:k^L\le n<(k+1)^L\}=B_{L,k}.
}
\]

So the long-run basin partition of any fixed collapse word is the ordinary basin partition of the single collapse \(C_L\).

## 8. Transients remember order; stabilization forgets it

For incomparable exponents \(2\) and \(3\), one pass can depend on order. At \(n=8\),

\[
C_2(C_3(8))=4,
\qquad
C_3(C_2(8))=1.
\]

Both words nevertheless have lcm exponent \(6\), and repeated iteration stabilizes at

\[
C_6(8)=1.
\]

Thus there are two mathematically distinct layers:

1. **transient word action**, which can retain noncommutative order information;
2. **stable action**, which depends only on the lcm of the exponent support.

## 9. Stable normal form of a collapse word

Define the finite-stabilization operator of a word pointwise by

\[
\operatorname{Stab}(W)(n)
=
\text{the eventual constant value of }W^t(n).
\]

This notation refers to finite eventual stabilization for each state. It does **not** invoke a continuum limit or an infinite-precision completion.

### P019-T07 — Stable normal form

Status: `PROVED`

For every finite collapse word \(W\),

\[
\boxed{
\operatorname{Stab}(W)=C_{L(W)},
}
\]

where \(L(W)\) is the lcm of its exponents and \(L(\varnothing)=1\).

This is just P019-T03 viewed as equality of functions.

## 10. The asymptotic quotient is the lcm semilattice

Let words be equivalent when their stabilized functions agree:

\[
U\sim_{\mathrm{stab}}V
\iff
\operatorname{Stab}(U)=\operatorname{Stab}(V).
\]

### P019-T08 — Stable equivalence iff lcm agrees

Status: `PROVED`

For finite collapse words \(U,V\),

\[
\boxed{
U\sim_{\mathrm{stab}}V
\iff
L(U)=L(V).
}
\]

### Proof

If the lcms agree, P019-T07 gives the same stabilized collapse.

Conversely suppose \(L(U)\ne L(V)\). Without loss of generality let \(a=L(U)<b=L(V)\). At

\[
n=2^a,
\]

we have

\[
C_a(n)=n>1.
\]

But \(2^a<2^b\), so the greatest positive perfect \(b\)-th power not exceeding \(2^a\) is \(1\); hence

\[
C_b(n)=1.
\]

Therefore \(C_a\ne C_b\), so the stabilized functions are different. ∎

For concatenated words,

\[
L(UV)=\operatorname{lcm}(L(U),L(V)).
\]

Hence the quotient operation induced by word concatenation is exactly lcm.

### P019-T09 — Asymptotic semilattice theorem

Status: `PROVED`

The collapse-word semigroup modulo stable equivalence is canonically represented by

\[
(\mathbb N_{>0},\operatorname{lcm}),
\]

with identity \(1\) for the empty word.

Thus the transient collapse semigroup can be noncommutative, while its stable quotient is a commutative idempotent join-semilattice:

\[
\operatorname{lcm}(a,b)=\operatorname{lcm}(b,a),
\qquad
\operatorname{lcm}(a,a)=a.
\]

This sharpens the earlier observation that fixed-point semantics remembers only lcm: the **entire eventual input-output map** remembers only lcm.

## 11. Relationship to canonical P009

Canonical P009 concerns the minimal **typed collapse+coarsening** transition system. It proves termination/no nontrivial cycles for strict typed transitions, pure-projection target confluence, and generic nonconfluence of mixed collapse/projection schedules.

P019 is deliberately narrower in generators but stronger in asymptotic classification:

- only a fixed word of same-space perfect-power collapse endomaps is iterated;
- its exact eventual map is computed;
- the stable quotient of the collapse-word semigroup is identified with the lcm semilattice.

P019 therefore does not reopen, replace, or silently widen the resolved scope of P009.

## 12. Prior-art and novelty discipline

P019-T01 and P019-T02 are elementary consequences of well-founded descent, monotonicity, reductivity, and antisymmetry. The collapse specialization then uses P004 and the established perfect-power basin definitions. These underlying order-theoretic and arithmetic ingredients are mature mathematics.

The project does not claim those ingredients as inventions. The exact packaging as the stable quotient of the Enterprise Math collapse-word family remains `NOVELTY_UNVERIFIED` pending dedicated prior-art review. No “first”, “unprecedented”, or historical-priority claim is made.
