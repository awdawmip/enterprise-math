# RSA Exponent-Collision CRT Collapse — Research Return

Status: `PASS / EXACT_EXTRACTION_AND_BARRIER_FROZEN`

Researcher-ID: `EM-RSACOL-C76042`  
Task: `RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE`  
Publication: `TP2-301CA54924787090237D`  
Claim: `chatgpt-rsacol-20260827-2313-c76042`

Hard target:

`RSA_EXPONENT_COLLISION_2ADIC_COLLAPSE_FACTOR_EXTRACTION_OR_EXACT_BARRIER_FROZEN`

## Executive result

The task closes positively at its stated scope.

For a valid local collision
\[
x^\Delta\equiv 1\pmod n,\qquad n=pq,\qquad \Delta>0,
\]
write
\[
\Delta=2^s u,\quad u\text{ odd},
\]
and
\[
\operatorname{ord}_p(x)=2^a m_p,\qquad
\operatorname{ord}_q(x)=2^b m_q,
\]
with \(m_p,m_q\) odd. The extractor-visible chain
\[
z_j=x^{u2^j}\pmod n
\]
produces a nontrivial CRT square root of \(1\), and hence a factor of \(n\), **if and only if**
\[
\boxed{a\ne b.}
\]

For a uniformly random unit, with
\[
A=v_2(p-1),\qquad B=v_2(q-1),\qquad m=\min(A,B),
\]
the exact single-certificate failure and success probabilities are
\[
\boxed{
F_1=\frac{4^m+2}{3\cdot 2^{A+B}}
}
\]
and
\[
\boxed{
P_1=1-\frac{4^m+2}{3\cdot 2^{A+B}}\ge \frac12.
}
\]
The lower bound is sharp at \(A=B=1\), including Blum-prime pairs.

A global exponent-map collision exposes a nonzero multiple of
\[
\lambda(n)=\operatorname{lcm}(p-1,q-1),
\]
so random-base collapse becomes the classical known-annihilating-exponent/order-to-factor reduction.

Multiple local certificates can do strictly more than separate attempts: their lcm safely annihilates the generated subgroup, and combinations of individually failing units can split \(n\). The exact multi-certificate obstruction is that the generated 2-primary subgroup is the graph of an isomorphism between its two local cyclic projections.

## 1. Collision kernels

Let
\[
G=(\mathbb Z/n\mathbb Z)^\times.
\]

For one fixed unit \(x\), the map
\[
\phi_x:\mathbb Z\to \langle x\rangle,\qquad e\mapsto x^e
\]
has kernel
\[
\boxed{
\ker\phi_x=\operatorname{ord}_n(x)\mathbb Z.
}
\]
Therefore
\[
x^e\equiv x^{e'}\pmod n
\iff
\operatorname{ord}_n(x)\mid(e-e').
\]

For a finite sample \(S=\{x_1,\ldots,x_r\}\), the simultaneous exponent map
\[
e\mapsto (x_1^e,\ldots,x_r^e)
\]
has kernel
\[
\boxed{
\operatorname{lcm}_i\operatorname{ord}_n(x_i)\,\mathbb Z.
}
\]
This lcm is exactly the exponent of the subgroup
\[
H=\langle x_1,\ldots,x_r\rangle.
\]

Under CRT,
\[
\operatorname{ord}_n(x)
=
\operatorname{lcm}\!\left(
\operatorname{ord}_p(x),
\operatorname{ord}_q(x)
\right).
\]

## 2. Exact single-collision collapse theorem

Assume the transcript supplies only
\[
(n,x,\Delta)
\]
with
\[
\gcd(x,n)=1,\qquad x^\Delta\equiv1\pmod n.
\]
The extractor is not given \(p,q,\lambda(n)\), or any hidden order.

Write
\[
\Delta=2^s u,\qquad u\text{ odd},
\]
and proof-side local orders as
\[
r_p=\operatorname{ord}_p(x)=2^a m_p,\qquad
r_q=\operatorname{ord}_q(x)=2^b m_q,
\]
where \(m_p,m_q\) are odd.

Since \(r_p,r_q\mid\Delta\),
\[
m_p\mid u,\qquad m_q\mid u,\qquad a,b\le s.
\]
Hence \(x^u\) has exact order \(2^a\) modulo \(p\) and exact order \(2^b\) modulo \(q\).

Define
\[
z_j=x^{u2^j}\pmod n,\qquad 0\le j\le s.
\]
Then
\[
z_j\equiv1\pmod p\iff j\ge a,
\qquad
z_j\equiv1\pmod q\iff j\ge b.
\]
If \(a>0\),
\[
z_{a-1}\equiv-1\pmod p,
\]
and similarly at \(q\).

Thus the first global index with \(z_t=1\pmod n\) is
\[
t=\max(a,b).
\]

If \(a<b\), then
\[
z_{t-1}\equiv(1,-1)
\]
under CRT, so
\[
z_{t-1}^2\equiv1\pmod n,\qquad z_{t-1}\not\equiv\pm1\pmod n,
\]
and
\[
\gcd(z_{t-1}-1,n)=p,\qquad
\gcd(z_{t-1}+1,n)=q.
\]
The case \(b<a\) is symmetric.

If \(a=b=t>0\), then
\[
z_{t-1}\equiv(-1,-1)\equiv-1\pmod n,
\]
so the first pre-\(1\) root is trivial. If \(a=b=0\), already \(z_0=1\).

Therefore:
\[
\boxed{
\text{2-adic collapse splits }n
\iff
v_2(\operatorname{ord}_p(x))
\ne
v_2(\operatorname{ord}_q(x)).
}
\]

A valid extractor is:

1. verify \(\gcd(x,n)=1\) and \(x^\Delta\equiv1\pmod n\);
2. strip all powers of \(2\) from \(\Delta\), obtaining \(u\);
3. set \(z=x^u\bmod n\);
4. square until the next square is \(1\);
5. at the preceding state test \(\gcd(z-1,n)\) and \(\gcd(z+1,n)\).

No hidden factor or order is consumed.

## 3. Exact random-unit success probability

Let
\[
A=v_2(p-1),\qquad B=v_2(q-1).
\]

For a uniform element of the cyclic group \(\mathbb F_p^\times\), its 2-primary component is uniform in \(C_{2^A}\). Therefore, for
\[
a=v_2(\operatorname{ord}_p(x)),
\]
\[
\Pr(a=0)=2^{-A},
\]
and for \(1\le t\le A\),
\[
\Pr(a=t)=2^{t-1-A}.
\]
The \(p\)- and \(q\)-components are independent.

The collapse fails exactly when \(a=b\). With
\[
m=\min(A,B),
\]
\[
\begin{aligned}
\Pr(\mathrm{fail})
&=
2^{-A-B}
+
\sum_{t=1}^m
2^{t-1-A}2^{t-1-B}\\
&=
\boxed{
\frac{4^m+2}{3\cdot2^{A+B}}
}.
\end{aligned}
\]

Hence
\[
\boxed{
\Pr(\mathrm{split})
=
1-\frac{4^m+2}{3\cdot2^{A+B}}.
}
\]

The largest failure probability over \(A,B\ge1\) is \(1/2\), attained at \(A=B=1\). Thus
\[
\boxed{\Pr(\mathrm{split})\ge\frac12}
\]
is the best uniform lower bound.

## 4. Global fake-exponent collision

Two exponents induce the same power map on every unit exactly when their difference annihilates \(G\). Since the exponent of \(G\) is Carmichael's value
\[
\lambda(n)=\operatorname{lcm}(p-1,q-1),
\]
we have
\[
\boxed{
x^e=x^{e'}\ \forall x\in G
\iff
\lambda(n)\mid(e-e').
}
\]

Therefore one exposed nonzero global collision difference is already a known multiple of \(\lambda(n)\). For every subsequently chosen unit \(x\),
\[
x^\Delta=1\pmod n,
\]
so the same 2-adic descent gives a factor with the exact probability in Section 3, at least \(1/2\) per independent random base.

This does not generate a collision and does not beat the classical reduction from a known multiple of the group exponent/order to factoring. It identifies precisely what a global fake exponent leaks.

## 5. Independent certificates and safe aggregation

For independent random units \(x_1,\ldots,x_k\) with valid local collision differences \(\Delta_i\), separate single-certificate attempts fail independently with probability
\[
\boxed{
F_1^k
=
\left(
\frac{4^m+2}{3\cdot2^{A+B}}
\right)^k.
}
\]
Therefore separate attempts alone succeed with probability at least
\[
1-2^{-k}.
\]

There is also a safe transcript-level aggregate:
\[
L=\operatorname{lcm}(\Delta_1,\ldots,\Delta_k).
\]
Because
\[
\operatorname{ord}_n(x_i)\mid\Delta_i\mid L,
\]
\(L\) annihilates every \(x_i\), hence the whole subgroup
\[
H=\langle x_1,\ldots,x_k\rangle.
\]
Every combination
\[
y=x_1^{c_1}\cdots x_k^{c_k}
\]
therefore satisfies
\[
y^L=1\pmod n
\]
and can be fed to the same collapse.

By contrast, \(\gcd(\Delta_1,\ldots,\Delta_k)\) need not annihilate any individual \(x_i\); it has no universal safe-aggregation property.

### Strict amplification witness

Take
\[
n=65=5\cdot13,\qquad
x_1=57,\qquad x_2=47,\qquad
\Delta_1=\Delta_2=4.
\]
Each unit has local 2-depth pair \((2,2)\), so each single collapse fails at the trivial root \(-1\).

But
\[
y=x_1x_2\equiv14\pmod{65},
\qquad
y^2\equiv1\pmod{65},
\]
with nontrivial CRT signs, and
\[
\boxed{
\gcd(14-1,65)=13.
}
\]

Thus lcm-plus-subgroup combination can expose leakage that is absent from every supplied unit when treated separately.

## 6. Exact multi-certificate barrier

Let
\[
P_2\cong C_{2^A},\qquad
Q_2\cong C_{2^B}
\]
be the local Sylow-2 factors, and let \(H_2\) be the 2-primary component of \(H\).

Every combination in \(H\) fails the depth test exactly when
\[
v_2(\operatorname{ord}(\pi_p h))
=
v_2(\operatorname{ord}(\pi_q h))
\quad
\text{for every }h\in H_2.
\]

If that equality holds for every \(h\), both coordinate projections on \(H_2\) are injective: a nonidentity element in one projection kernel would have local depth \(0\) on one side and positive depth on the other. Since \(H_2\) injects into a cyclic 2-group, \(H_2\) is cyclic. Its two images have the same order, and
\[
H_2
\]
is the graph of an isomorphism between those two cyclic image subgroups.

Conversely, any graph of an isomorphism preserves element orders, so every element has equal local 2-depth.

Hence:
\[
\boxed{
\text{no }H\text{-combination can split by this 2-adic mechanism}
\iff
H_2\text{ is a graph of an isomorphism between its local projections}.
}
\]

This is the exact multi-certificate diagonal barrier.

## 7. Exact aggregate-barrier probability

For \(0\le t\le m=\min(A,B)\), each local cyclic 2-group has a unique subgroup of order \(2^t\). For \(t\ge1\), there are
\[
\varphi(2^t)=2^{t-1}
\]
isomorphisms between the two order-\(2^t\) subgroups.

A fixed graph has order \(2^t\). The number of ordered \(k\)-tuples generating that graph is
\[
2^{tk}-2^{(t-1)k},
\]
because a tuple fails to generate it exactly when all entries lie in its unique maximal subgroup.

The \(t=0\) graph contributes one all-identity tuple. Therefore the probability that the generated 2-primary subgroup remains wholly trapped is
\[
\boxed{
F_k^{\mathrm{agg}}
=
\frac{
1+\displaystyle\sum_{t=1}^m
\varphi(2^t)
\left(2^{tk}-2^{(t-1)k}\right)
}{
2^{(A+B)k}
}.
}
\]

At \(k=1\), this reduces to \(F_1\). Also
\[
F_k^{\mathrm{agg}}\le F_1^k\le2^{-k}.
\]
For \(k\ge2\) and \(m\ge2\), the first inclusion can be strict; the \(n=65\) witness exhibits the mechanism.

Because \(L\) annihilates \(H\), choosing coefficient vectors uniformly modulo \(L\) maps uniformly onto \(H\). Thus an extractor can search combinations without knowing the CRT factors.

## 8. Barrier scope

For one local certificate, the exact barrier is
\[
\boxed{a=b.}
\]

For several certificates with lcm aggregation, the exact barrier is
\[
\boxed{
H_2\text{ is a diagonal graph of a local cyclic-subgroup isomorphism}.
}
\]

The smallest useful additional collision is one whose 2-primary component enlarges the generated subgroup away from this graph. It may split directly, or only after a combination.

These are barriers for the collision-driven 2-adic CRT-square-root mechanism, not information-theoretic lower bounds against factoring the public integer \(n\) by unrelated algorithms.

## 9. Exposure-model separation

1. **Single local collision:** exposes a known multiple of \(\operatorname{ord}_n(x)\). It splits exactly when the local 2-depths differ.
2. **Finite sample:** a common collision period is the exponent of the generated subgroup; separate periods may be lcm-aggregated safely.
3. **Global fake exponent:** exposes a known nonzero multiple of \(\lambda(n)\), enough for the classical random-base factor reduction.

Collision exposure and collision generation remain separate. This task proves no efficient way to produce the collision transcript from \(n\) alone.

## 10. Regression and recovery audit

Task-local checker:

`python scripts/check_rsa_exponent_collision_crt_collapse.py`

Re-executed during state-machine recovery on 2026-08-28 with exact-integer arithmetic:

```text
SINGLE_COLLISION_THEOREM=PASS
EXHAUSTIVE_SEMIPRIMES=210
EXHAUSTIVE_UNITS=274904
GLOBAL_MULTIPLE_TESTS=PASS
STRICT_AGGREGATION_WITNESS=n65:x57,x47,delta4->product14
AGGREGATE_FORMULA_CASES=18
FINITE_REGRESSION_IS_NOT_A_GENERAL_PROOF=TRUE
```

An additional recovery audit exhaustively checked the aggregate-barrier formula for
\[
A,B\in\{1,2\},\qquad k\in\{1,2,3\},
\]
covering 12 exact parameter triples, with zero failures.

The factors are used only by the regression harness as hidden ground truth. The extractor itself consumes only public transcript data \((n,x,\Delta)\) or safe lcm-generated subgroup certificates.

Finite checks are regression/falsification evidence only; the general statements above are proved algebraically.

## Terminal disposition

`PASS / HARD_TARGET_MET / EXACT_SINGLE_COLLISION_CRITERION / EXACT_RANDOM_PROBABILITY / GLOBAL_KERNEL / STRICT_MULTI_CERTIFICATE_AMPLIFICATION / DIAGONAL_GRAPH_BARRIER`

Unresolved residue inside task scope: `NONE`.

Out-of-scope residue: efficient collision generation is a separate research question and is not implied by this result.

Control-plane recommendation: Driver-review this frozen result and close the current task generation if accepted. Open no collision-generation successor unless separately justified and immutably published.
