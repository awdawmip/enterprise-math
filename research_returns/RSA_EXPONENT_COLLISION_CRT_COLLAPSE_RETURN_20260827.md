# RSA Exponent-Collision CRT Collapse — Research Return

Status: `PASS / EXACT_EXTRACTION_AND_BARRIER_FROZEN`

Researcher-ID: `EM-RSACOL-C76042`  
Task: `RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE`  
Publication: `TP2-301CA54924787090237D`  
Claim: `chatgpt-rsacol-20260827-2313-c76042`

Hard target:

`RSA_EXPONENT_COLLISION_2ADIC_COLLAPSE_FACTOR_EXTRACTION_OR_EXACT_BARRIER_FROZEN`

## 1. Collision kernels

Let \(n=pq\) with distinct odd primes and let \(G=(\mathbb Z/n\mathbb Z)^\times\).
For a fixed unit \(x\in G\), the exponent map

\[
\phi_x:\mathbb Z\to\langle x\rangle,\qquad e\mapsto x^e
\]

has kernel

\[
\boxed{\ker\phi_x=\operatorname{ord}_n(x)\mathbb Z.}
\]

Thus a local equality \(x^e=x^{e'}\pmod n\) is exactly the statement

\[
\operatorname{ord}_n(x)\mid(e-e').
\]

For a finite sample \(S=\{x_1,\ldots,x_r\}\), the simultaneous map

\[
e\mapsto(x_1^e,\ldots,x_r^e)
\]

has kernel

\[
\boxed{
\operatorname{lcm}_i\operatorname{ord}_n(x_i)\,\mathbb Z.
}
\]

The lcm is exactly the exponent of the subgroup \(H=\langle S\rangle\): every word in the generators is killed by the lcm, while the exponent of \(H\) must be divisible by every generator order.

Under CRT,

\[
\operatorname{ord}_n(x)=
\operatorname{lcm}(\operatorname{ord}_p(x),\operatorname{ord}_q(x)).
\]

No hidden factor or order is supplied to the extractor below; those quantities appear only in the proof-side characterization.

## 2. Exact single-collision collapse theorem

Suppose the exposed local collision gives

\[
\Delta=|e-e'|>0,\qquad x^\Delta\equiv1\pmod n.
\]

Write

\[
\Delta=2^s u,\qquad u\text{ odd},
\]

and on the hidden CRT components write

\[
\operatorname{ord}_p(x)=2^a m_p,
\qquad
\operatorname{ord}_q(x)=2^b m_q,
\]

with \(m_p,m_q\) odd. Since both local orders divide \(\Delta\),

\[
m_p\mid u,\qquad m_q\mid u,
\qquad a,b\le s.
\]

Define the extractor-visible chain

\[
z_j=x^{u2^j}\pmod n,\qquad 0\le j\le s.
\]

Modulo \(p\), the element \(x^u\) has exact order \(2^a\). Hence

\[
z_j\equiv1\pmod p\iff j\ge a,
\]

and, if \(a>0\),

\[
z_{a-1}\equiv-1\pmod p.
\]

The same statements hold modulo \(q\) with \(b\).
Therefore the first index at which the chain is globally \(1\) is

\[
t=\max(a,b).
\]

If \(a<b\), then at the first pre-\(1\) state

\[
z_{t-1}\equiv(1,-1)\quad\text{in }\mathbb F_p^\times\times\mathbb F_q^\times,
\]

so \(z_{t-1}^2=1\pmod n\) but \(z_{t-1}\ne\pm1\pmod n\), and

\[
\gcd(z_{t-1}-1,n)=p,
\qquad
\gcd(z_{t-1}+1,n)=q.
\]

The case \(b<a\) is symmetric.

If \(a=b=t>0\), then

\[
z_{t-1}\equiv(-1,-1)\equiv-1\pmod n,
\]

so the square root is trivial. If \(a=b=0\), then already \(z_0=1\pmod n\), so there is no pre-\(1\) square root.

Hence the proposed criterion is exactly correct:

\[
\boxed{
\text{single-collision 2-adic CRT split succeeds}
\iff
v_2(\operatorname{ord}_p(x))\ne
v_2(\operatorname{ord}_q(x)).
}
\]

An extractor needs only \((n,x,\Delta)\): strip the powers of two from \(\Delta\), compute the chain until the first global \(1\), and gcd the preceding state with \(n\). It never receives \(p,q,\lambda(n)\), or an order.

## 3. Exact random-unit success probability

Put

\[
A=v_2(p-1),\qquad B=v_2(q-1).
\]

For uniformly random \(x\pmod p\), its 2-primary component is uniform in the cyclic group \(C_{2^A}\). Therefore, for

\[
a=v_2(\operatorname{ord}_p(x)),
\]

\[
\Pr(a=0)=2^{-A},
\qquad
\Pr(a=t)=2^{t-1-A}\quad(1\le t\le A).
\]

The \(p\)- and \(q\)-components are independent under CRT. Let

\[
m=\min(A,B).
\]

The collapse fails exactly when \(a=b\), so

\[
\begin{aligned}
\Pr(\mathrm{fail})
&=2^{-A-B}
+\sum_{t=1}^{m}2^{t-1-A}2^{t-1-B}\\
&=\boxed{\frac{4^m+2}{3\cdot2^{A+B}}}.
\end{aligned}
\]

Thus

\[
\boxed{
\Pr(\mathrm{split})
=1-\frac{4^m+2}{3\cdot2^{A+B}}.
}
\]

The best uniform bound over all distinct odd primes is

\[
\boxed{\Pr(\mathrm{split})\ge\frac12.}
\]

It is sharp at \(A=B=1\), in particular for a Blum-prime pair \(p\equiv q\equiv3\pmod4\).

## 4. Global fake-\(e\) / fake-\(d\) collision

Two integer exponents induce the same power map on every unit iff their difference annihilates the whole unit group. For a finite abelian group this is equivalent to divisibility by its exponent. For \(n=pq\),

\[
\exp(G)=\lambda(n)=\operatorname{lcm}(p-1,q-1).
\]

Therefore

\[
\boxed{
x^e=x^{e'}\ \forall x\in G
\iff
\lambda(n)\mid(e-e').}
\]

So RSA exponents are naturally collision classes modulo \(\lambda(n)\) on the unit group. Distinct integer representatives separated by a multiple of \(\lambda(n)\) are not prevented from colliding; they are the same exponent action.

Consequently, one exposed nonzero **global** collision difference \(\Delta\) is already a known multiple of \(\lambda(n)\). For any independently chosen random unit \(x\), \(x^\Delta=1\), so the single-collision collapse above becomes the standard random-base factor extraction from a known group-exponent multiple, with exact success probability from Section 3 and at least \(1/2\) per base.

This does **not** solve collision generation. It is an exact reformulation of the classical multiple-of-order / multiple-of-group-exponent reduction to factoring.

The same statement applies to a purported global fake decryption exponent \(d'\): if \(x^{d'}=x^d\) for every unit, then \(d'-d\) is a multiple of \(\lambda(n)\). In the usual RSA key relation, different integer representatives of the inverse exponent likewise differ by multiples of \(\lambda(n)\).

## 5. Independent collision certificates: simple amplification

Suppose \(x_1,\ldots,x_k\) are independent uniform units and for each \(x_i\) a valid local collision difference \(\Delta_i\) is supplied. The validity of a certificate is enough; \(\Delta_i\) need not be the exact order.

Running the single-certificate collapse separately gives independent failures, hence

\[
\boxed{
\Pr(\text{all }k\text{ single collapses fail})=F_1^k,
\qquad
F_1=\frac{4^m+2}{3\cdot2^{A+B}}.
}
\]

In particular the uniform success guarantee is at least

\[
1-2^{-k}.
\]

## 6. LCM aggregation is strictly stronger in some transcripts

There is a safe aggregate that uses no factors:

\[
L=\operatorname{lcm}(\Delta_1,\ldots,\Delta_k).
\]

Because \(\operatorname{ord}_n(x_i)\mid\Delta_i\mid L\), \(L\) annihilates every generator and therefore the whole subgroup

\[
H=\langle x_1,\ldots,x_k\rangle.
\]

Thus every product

\[
y=x_1^{c_1}\cdots x_k^{c_k}
\]

comes with a valid collision certificate \(y^L=1\), and the same 2-adic collapse can be run on \(y\).

A gcd of the \(\Delta_i\) has no analogous universal guarantee: each local order divides its own \(\Delta_i\), but need not divide their gcd. A proposed smaller aggregate is usable only after its annihilation property is explicitly verified by modular exponentiation.

LCM aggregation can reveal a split even when every supplied unit fails individually. The smallest concrete witness is

\[
n=65=5\cdot13,
\qquad x_1=57,\quad x_2=47,\quad \Delta_1=\Delta_2=4.
\]

Both \(x_1\) and \(x_2\) have local 2-depth pair \((2,2)\), so both single collapses stop at the trivial root \(-1\). But

\[
y=x_1x_2\equiv14\pmod{65},
\qquad y^2\equiv1\pmod{65},
\]

with CRT signs \((-1,1)\), and

\[
\boxed{\gcd(14-1,65)=13.}
\]

So aggregation is not merely the probability \(F_1^k\) rewritten.

## 7. Exact multi-sample barrier and its probability

Let \(P_2\cong C_{2^A}\) and \(Q_2\cong C_{2^B}\) be the local Sylow-2 factors, and let \(H_2\) be the 2-primary component of the subgroup generated by the \(k\) sampled units.

Every \(H\)-combination fails the CRT-depth test exactly when

\[
v_2(\operatorname{ord}(\pi_p h))
=
v_2(\operatorname{ord}(\pi_q h))
\qquad\text{for every }h\in H_2.
\]

This has an exact structural form.

If the equality holds for every \(h\), then either projection kernel must be trivial: if \(1\ne h\in\ker\pi_p\), the two local depths would be \(0\) and \(>0\). Hence both projections are injective. Since \(H_2\) injects into a cyclic 2-group, \(H_2\) is cyclic, the two images have the same order, and \(H_2\) is the graph of an isomorphism between those two cyclic image subgroups.

Conversely, the graph of an isomorphism preserves element orders, so every element has equal local 2-depth. Thus

\[
\boxed{
\text{no combination in }H\text{ can split by 2-adic collapse}
\iff
H_2\text{ is a graph of an isomorphism between its local projections}.}
\]

This is the exact multi-certificate diagonal barrier.

It also gives an exact probability for \(k\) independent random units. For \(0\le t\le m=\min(A,B)\), each local cyclic group has a unique subgroup of order \(2^t\). For \(t\ge1\), there are

\[
\varphi(2^t)=2^{t-1}
\]

isomorphisms between the two order-\(2^t\) subgroups. A fixed graph is cyclic of order \(2^t\), and the number of ordered \(k\)-tuples generating it is

\[
2^{tk}-2^{(t-1)k}.
\]

The \(t=0\) graph contributes one all-identity tuple. Therefore the probability that the **entire generated subgroup** remains trapped in the diagonal barrier is

\[
\boxed{
F_k^{\rm agg}
=
\frac{
1+\displaystyle\sum_{t=1}^{m}
\varphi(2^t)\left(2^{tk}-2^{(t-1)k}\right)
}{2^{(A+B)k}}.
}
\]

For \(k=1\) this reduces exactly to

\[
\frac{4^m+2}{3\cdot2^{A+B}}.
\]

The aggregate-barrier event is contained in the event that every individual certificate fails, hence

\[
F_k^{\rm agg}\le F_1^k\le2^{-k},
\]

and the full-subgroup split probability is at least \(1-2^{-k}\). For \(k\ge2\) and \(m\ge2\), the inclusion is strict; the \(n=65\) example exhibits the mechanism explicitly.

An extractor does not need the hidden CRT description to exploit a non-barrier transcript. It knows \(L\), can form combinations of the exposed \(x_i\), and each such combination is automatically certified by \(L\). Random coefficients modulo \(L\) map uniformly onto \(H\), so repeated combination-and-collapse searches the splitter population of \(H\) without knowing \(p\) or \(q\).

## 8. Exact barrier classification and scope

For one local collision the barrier is

\[
\boxed{a=b.}
\]

For several local collisions plus safe lcm aggregation the barrier sharpens to

\[
\boxed{H_2\text{ is a diagonal graph of a local cyclic-subgroup isomorphism}.}
\]

The smallest additional collision that escapes the barrier is one whose 2-primary CRT component enlarges the generated subgroup away from that graph; it may succeed directly, or it may only make a product/combination succeed.

These are exact barriers for the **collision-driven 2-adic CRT-square-root mechanism**. They are not an information-theoretic statement that the public integer \(n\) cannot be factored by some unrelated algorithm. The task intentionally separates the leakage contained in an exposed collision from the harder problem of producing such a collision.

## 9. What the three exposure models leak

1. **Single local collision:** exposes one known multiple of \(\operatorname{ord}_n(x)\). It factors exactly when the local order 2-depths differ; otherwise that one 2-adic chain is trapped at a trivial root.
2. **Finite sample:** the common collision kernel is the exponent of the generated subgroup. Separate local certificates can be safely lcm-aggregated to obtain such a subgroup annihilator; combinations can strictly amplify leakage.
3. **Global fake exponent:** exposes a nonzero multiple of \(\lambda(n)\). That is sufficient to run the classical random-base order-multiple factor extraction with probability at least \(1/2\) per base.

Thus the positive bridge is real,

\[
\text{exposed exponent collision}
\to\text{annihilating exponent}
\to\text{2-adic chain}
\to\text{CRT square root}
\to\text{factor},
\]

but it is not a new method for generating RSA collisions and is not stronger than the classical order-to-factor reduction once a global annihilating exponent is already known.

## 10. Regression

Task-local checker:

`python scripts/check_rsa_exponent_collision_crt_collapse.py`

Exact local run:

```text
SINGLE_COLLISION_THEOREM=PASS
EXHAUSTIVE_SEMIPRIMES=210
EXHAUSTIVE_UNITS=274904
GLOBAL_MULTIPLE_TESTS=PASS
STRICT_AGGREGATION_WITNESS=n65:x57,x47,delta4->product14
AGGREGATE_FORMULA_CASES=18
FINITE_REGRESSION_IS_NOT_A_GENERAL_PROOF=TRUE
```

The exhaustive unit census uses the factors only as hidden regression ground truth. The extractor itself receives only \(n,x,\Delta\). The aggregate formula is independently checked for every \(A,B\in\{1,2,3\}\) and \(k\in\{1,2\}\). Finite checks are falsification/regression only; the general statements above are proved algebraically.

## Terminal disposition

`PASS / HARD_TARGET_MET / EXACT_SINGLE_COLLISION_CRITERION / EXACT_RANDOM_PROBABILITY / GLOBAL_KERNEL / STRICT_MULTI_CERTIFICATE_AMPLIFICATION / DIAGONAL_GRAPH_BARRIER`

No successor about efficient collision generation is authorized by this result; that is a separate research question.
