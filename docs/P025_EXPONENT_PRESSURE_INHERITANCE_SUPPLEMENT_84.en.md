# P025 Supplement 84 — Exact Projective-Pressure Inheritance on the Exponent Divisibility Poset

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 82–83  
Hard block: `NONE`

## 1. Composite-exponent pressure is a transport problem

Stage 83 shows that composite exponents may inherit projective pressure from proper cyclotomic divisor layers. The fourth- and ninth-power counterexamples suggest something stronger than a qualitative inheritance statement.

There is an exact multiplicative transport law along exponent divisibility.

## 2. Same-sign divisibility

Let

\[
2\le m<n,
\qquad
m\mid n,
\qquad
k:=\frac nm.
\]

For the difference sign,

\[
p^m-q^m\mid p^n-q^n
\]

for every `k`.

For the sum sign,

\[
p^m+q^m\mid p^n+q^n
\]

exactly along the same-sign divisibility route considered here when `k` is odd.

Write

\[
A_m:=p^m\pm q^m,
\qquad
A_n:=p^n\pm q^n,
\]

and

\[
\boxed{Q_{m\to n}:=\frac{A_n}{A_m}.}
\]

At the cyclotomic-index level, the corresponding low index set is contained in the high one, and `Q` is the product of the new layers.

## 3. P025-D28 — inheritance overlap and multiplier

Define the support-overlap factor

\[
\boxed{
\Gamma_{m\to n}
:=
\frac{\operatorname{rad}(A_m)\operatorname{rad}(Q_{m\to n})}
{\operatorname{rad}(A_n)}.
}
\]

This is an integer and is exactly the two-block overlap correction between the inherited active component and the new quotient.

Define the pressure inheritance multiplier

\[
\boxed{
\Lambda_{m\to n}
:=
\frac{\Gamma_{m\to n}\,m(Q_{m\to n})}{k}.
}
\]

The numerator has two distinct sources:

1. new multiplicity inside the quotient `m(Q)`;
2. reused support between the old component and the quotient `Gamma`.

The denominator `k=n/m` is the projective normalization cost of raising the exponent.

## 4. P025-T174 — exact projective-pressure inheritance law

The two-block residual identity gives

\[
\boxed{
m(A_n)
=
\Gamma_{m\to n}\,m(A_m)m(Q_{m\to n}).}
\]

The equal-exponent projective ratios are

\[
\rho_{m,\pm}
=
\frac{m(A_m)}{m(p+q)},
\]

and

\[
\rho_{n,\pm}
=
\frac{m(A_n)}{n(p+q)}.
\]

Substituting the residual identity and `n=km` yields

\[
\boxed{
\rho_{n,\pm}
=
\rho_{m,\pm}\Lambda_{m\to n}.
}
\]

Equivalently,

\[
\boxed{
\frac{\rho_{n,\pm}}{\rho_{m,\pm}}
=
\frac{\Gamma_{m\to n}m(Q_{m\to n})}{n/m}.
}
\]

This formula is exact. No asymptotic estimate or coprimality approximation enters.

## 5. P025-D29 — three transport classes

The multiplier gives a natural trichotomy:

\[
\boxed{
\Lambda<1:\ \text{attenuated},
\qquad
\Lambda=1:\ \text{resonant},
\qquad
\Lambda>1:\ \text{amplified}.
}
\]

Thus a composite exponent can:

- suppress a lower hard state;
- preserve it exactly;
- amplify a lower state, even promoting a subunit state across the activation threshold.

This is strictly richer than the statement "proper divisors matter."

## 6. P025-C26 — the fourth-power counterexample is an exact resonant lift

For

\[
(q,p)=(23,41),
\]

compare exponents

\[
2\to4.
\]

The quotient is

\[
Q_{2\to4}=p^2+q^2=\Phi_4(p,q),
\]

which is squarefree in this example, so

\[
m(Q)=1.
\]

The inherited square-difference component and the quotient share only the prime two, giving

\[
\Gamma_{2\to4}=2.
\]

Since

\[
k=2,
\]

we get

\[
\boxed{\Lambda_{2\to4}=1.}
\]

Therefore

\[
\boxed{
\rho_{4,-}(41,23)
=ho_{2,-}(41,23)
=\frac32.
}
\]

Stage 82's fourth-power top-squarefree activation is not newly generated pressure. It is an exact resonant lift of the prime-square centered hard state.

## 7. P025-C27 — ninth-power counterexamples are resonant cube lifts

### Difference

For

\[
(q,p)=(23,71),
\]

compare

\[
3\to9.
\]

The new quotient is the top layer `Phi_9`, which is squarefree, so `m(Q)=1`. It shares prime three with the inherited cube component, hence

\[
\Gamma_{3\to9}=3.
\]

Since `k=3`,

\[
\Lambda=1
\]

and

\[
\boxed{
\rho_{9,-}=\rho_{3,-}=\frac{1372}{47}.
}
\]

### Sum

For

\[
(q,p)=(11,13),
\]

the `3->9` sum quotient `Phi_18` is likewise squarefree and shares only the exponent prime three with the inherited component. Again

\[
\Gamma=3,
\qquad
k=3,
\qquad
\Lambda=1,
\]

so

\[
\boxed{
\rho_{9,+}=\rho_{3,+}=\frac76.
}
\]

These are exact resonant lifts.

## 8. P025-T175 — attenuation, resonance and amplification all occur

The same route

\[
3\to9
\]

already realizes all three transport classes.

### Attenuation

For

\[
(q,p)=(5,59)
\]

on the sum branch, the quotient is squarefree and has no support overlap with the inherited component:

\[
\Gamma=1,
\qquad
m(Q)=1.
\]

Thus

\[
\Lambda=\frac13.
\]

The activated cube state

\[
\rho_{3,+}=\frac{13}{6}>1
\]

falls to

\[
\boxed{
\rho_{9,+}=\frac{13}{18}<1.
}
\]

### Resonance

For `(q,p)=(11,13)`,

\[
\boxed{\Lambda=1.}
\]

### Amplification

For

\[
(q,p)=(7,29),
\]

the new quotient has residual

\[
m(Q)=19
\]

and overlap

\[
\Gamma=3.
\]

Therefore

\[
\Lambda=19.
\]

A subunit cube state

\[
\rho_{3,+}=\frac16
\]

is amplified to

\[
\boxed{
\rho_{9,+}=\frac{19}{6}>1.
}
\]

So high-exponent activation can be inherited, destroyed, or created by the quotient transport.

## 9. P025-T176 — inheritance multipliers form a multiplicative cocycle

Consider an admissible same-sign chain

\[
m\mid n\mid r.
\]

Repeated use of P025-T174 gives

\[
\rho_r
=ho_n\Lambda_{n\to r}
=ho_m\Lambda_{m\to n}\Lambda_{n\to r}.
\]

But direct transport also gives

\[
\rho_r=\rho_m\Lambda_{m\to r}.
\]

Since all projective ratios are positive,

\[
\boxed{
\Lambda_{m\to r}
=
\Lambda_{m\to n}\Lambda_{n\to r}.
}
\]

Thus `Lambda` is a multiplicative pressure cocycle on the admissible exponent-divisibility poset.

Taking logarithms converts the transport into additive pressure increments.

## 10. Primitive versus inherited hard states

Stage 84 suggests a sharper research classification.

A hard state at exponent `n` should not automatically be treated as new arithmetic complexity. First ask whether there exists a proper admissible divisor `m|n` for which

\[
\rho_m
\]

already carries substantial pressure and `Lambda_{m->n}` preserves or amplifies it.

This separates:

1. **inherited pressure** — already present at a proper exponent;
2. **quotient-generated pressure** — created by `m(Q)` or overlap in the new layers;
3. **primitive exponent pressure** — not explained by any proper-divisor transport.

The third class is the genuinely new exponent-level frontier.

## 11. Architectural meaning

Exponent is no longer merely a scalar shell label. It is a node in a divisibility poset carrying a multiplicative transport cocycle.

The future-safe precision state for composite exponents should therefore include at least:

\[
\boxed{
\text{ancestor pressure}
+
\text{new quotient residual}
+
\text{support overlap}
-
\text{exponent normalization cost}.
}
\]

This is a concrete example where a state at one scale is not independent of its lower-scale history. The correct abstraction is transport on a refinement/divisibility structure, not a flat family of unrelated exponent shells.

## 12. Prior-art / novelty discipline

Divisibility of `x^m±y^m`, radical identities and quotient factorizations are classical mathematics.

P025 claims none of those ingredients individually.

The project-side candidate is the exact projective-pressure multiplier, its attenuation/resonance/amplification classification, and the cocycle interpretation on exponent divisibility. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_exponent_pressure_inheritance.py`;
- `tests/test_abc_exponent_pressure_inheritance.py`.

The executable layer verifies the exact ratio transport, cyclotomic index inclusion, all three transport classes, the Stage-82/83 resonant counterexamples, and the cocycle law on an exponent chain.

## 14. Next frontier

No hard block exists. Continue with:

1. define the primitive pressure of an exponent after factoring out all admissible proper-divisor inheritance;
2. determine whether maximal ancestor pressure can be computed from a small antichain rather than every divisor;
3. test if the logarithmic cocycle admits a telescoping minimal path on the exponent lattice;
4. use the resulting primitive/inherited split to avoid recounting lifted hard states in future exceptional-set arguments;
5. relay the cocycle/transport abstraction to A2/P023 once the minimal-state theorem is proved.
