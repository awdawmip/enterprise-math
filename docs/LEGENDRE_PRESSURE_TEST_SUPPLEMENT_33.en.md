# Legendre Pressure Test — Supplement 33

Status: `PROVED RESEARCH NOTE`  
Scope: finite fixed-prime split bits form an exact Boolean precision cube  
Depends on: P017 L074 finite-pattern law and P023-S13–S19 incidence/closure/scheduling calculus  
Discipline: this is a deterministic natural-density theorem about the moving square-basin index. It does not assert stochastic independence as an ontological model.

## 1. Split indicators as precision tasks on basin index

Fix distinct primes

\[
p_1,\ldots,p_m.
\]

On the state space of sufficiently large basin indices `k`, define binary tasks

\[
I_i(k)=I_{p_i}(k)
\in\{0,1\},
\]

where `1` means the actual least-prime shell `p_i` splits across two cofactor-root classes.

L074 proves that every binary pattern

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_m)
\in\{0,1\}^m
\]

occurs with positive natural density

\[
\prod_i
p_i^{-\varepsilon_i/2}
\left(1-p_i^{-1/2}\right)^{1-\varepsilon_i}.
\]

Hence every one of the `2^m` patterns occurs infinitely often.

## 2. P017-L076-A — The realized joint split state is the full Boolean cube

Status: `PROVED`.

The joint task map

\[
\boxed{
I(k)=(I_1(k),\ldots,I_m(k))
}
\]

has image

\[
\boxed{
\operatorname{im} I=\{0,1\}^m.
}
\]

Indeed each pattern has positive density by L074 and therefore occurs.

Consequently the joint precision quotient has exactly

\[
\boxed{2^m}
\]

classes.

Moreover, because there are only finitely many patterns, there exists a finite basin threshold `K_0(p_1,...,p_m)` after which the finite prefix up to any sufficiently large bound has already witnessed every joint class at least once.

The theorem is existential; L074 does not provide an optimal effective threshold.

## 3. P017-L076-B — No fixed split bit is determined by the others

Status: `PROVED`.

Fix one coordinate `I_j` and any assignment to the other `m-1` coordinates.

The two full patterns obtained by setting

\[
I_j=0
\]

and

\[
I_j=1
\]

both have positive density by L074.

Therefore the context given by all other split bits does not determine `I_j`.

In P023 language,

\[
\boxed{
\rho(I_j\mid I_1,\ldots,\widehat{I_j},\ldots,I_m)=2.
}
\]

Thus no split-bit task lies in the dependency closure of the others.

More generally, any proper subset of the coordinates leaves every omitted coordinate genuinely binary.

## 4. P017-L076-C — Dependency closure is trivial on the fixed-prime split family

Status: `PROVED`.

Let `T={I_1,...,I_m}`. For every subset `S subseteq T`,

\[
\boxed{
\operatorname{cl}(S)=S.
}
\]

### Proof

Every omitted split coordinate realizes both values inside every realized context pattern on `S`, because all full Boolean patterns occur. Hence its conditional repair factor is two rather than one. By S15 it is not in closure. ∎

Therefore the only task basis is the full set `T` itself.

In particular,

\[
\boxed{g(\mathcal T)=m.}
\]

Here, unlike the generic S19 counterexample, coordinate generator count is forced by the realized arithmetic state.

## 5. P017-L076-D — Every acquisition order has exact binary cost m

Status: `PROVED`.

Start from the universal context and add the `m` split-bit tasks in any order.

At every stage, every current Boolean prefix has both extensions by the next bit. Thus

\[
\boxed{
\rho_j=2
\quad\text{for every stage }j.
}
\]

Hence every order has binary depth

\[
\boxed{
C_2=m.
}
\]

The final joint class count is `2^m`, so

\[
L_2(2^m)=m.
\]

Therefore every order exactly reaches the semantic lower bound.

No scheduling optimization is needed for this particular task family.

## 6. P017-L076-E — Both S17 slack terms vanish

The stagewise product capacity is

\[
P_\sigma=2^m,
\]

which equals the realized joint class count.

Also the separate binary stage depths sum to exactly `m`, equal to

\[
L_2(P_\sigma).
\]

Therefore

\[
\boxed{
S_{\rm radix}=0,
\qquad
S_{\rm inc}=0.
}
\]

The fixed-prime split-bit subsystem is already a perfectly packed, fully realized Boolean product precision.

## 7. P017-L076-F — S19's three size notions coincide here

For this declared task family,

\[
D_2=L_2(2^m)=m,
\]

\[
g(\mathcal T)=m,
\]

and

\[
A_2(\mathcal T)=m.
\]

Thus

\[
\boxed{
D_2=g=A_2=m.
}
\]

This is a positive boundary complementary to S19:

- generic precision systems do **not** have an intrinsic coordinate-count dimension;
- a fully realized independent Boolean product does.

The equality is a theorem of the realized incidence structure, not a foundational axiom imposed in advance.

## 8. No finite Boolean law among fixed-prime split bits

Because every pattern occurs with positive density, no nontrivial Boolean relation among the fixed indicators can hold for all sufficiently large `k`.

For example, for distinct fixed primes `p,q`, all four combinations

\[
(0,0),(0,1),(1,0),(1,1)
\]

occur with positive density.

Thus neither split implication

\[
I_p\Rightarrow I_q
\]

nor exclusion

\[
I_p I_q=0
\]

can become an eventual law.

This is a strong negative boundary against reducing the global split spectrum to finitely many fixed-prime anchor rules.

## 9. Relation to the density-one divergence of S(k)

L075 says that the total number `S(k)` of active split shells tends to infinity in natural density.

L076 explains one mechanism behind that proliferation: every finite collection of fixed split bits behaves as a free realized Boolean subsystem, with no zero-cost dependency compression.

As more fixed prime tasks are admitted, each contributes a genuinely new Boolean coordinate to this finite subsystem.

This does not mean the full infinite family is an infinite product state in the foundational ontology. Every theorem here is finite-family first, with asymptotic density used only over the basin-index parameter.

## 10. Research-tool consequence

A coordinate-count dimension should be accepted only after testing realized product completeness.

The fixed-prime split family passes the strongest possible test:

\[
\boxed{
\text{formal Boolean product}
=
\text{realized joint state}.
}
\]

By contrast, many earlier P023/P017 examples had missing product tuples, dependencies, or unequal minimal bases.

So full-product realization is a natural sufficient condition under which raw coordinate count becomes a genuine finite precision dimension.

## 11. Executable audit

- `src/enterprise_math/p017_split_pattern.py`
- `tests/test_p017_split_pattern.py`

The bounded audit checks simultaneous split patterns for small prime families and verifies that pattern counts partition finite basin ranges. The full Boolean-cube theorem itself follows from the positive-density formula of L074.

## 12. Foundation feedback

The project now has both a negative and a positive dimension result:

\[
\boxed{
\text{generic closure system: basis size need not be invariant}
}
\]

but

\[
\boxed{
\text{fully realized independent Boolean incidence: }D_2=g=A_2=m.
}
\]

This suggests that “dimension” should be derived from proved incidence/product structure rather than attached to a list of coordinates by convention.
