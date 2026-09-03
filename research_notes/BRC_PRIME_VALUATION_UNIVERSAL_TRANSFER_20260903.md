# BRC Prime-Valuation Universal Weight-Histogram Transfer

Status: `RESEARCH CANDIDATE / EXACT POSITIVE-RATIONAL EXPLICIT-BRANCH / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents:
- positive-rational prime-valuation holonomy `WBRC-T22/T23`;
- recurrent explicit-branch moment lift / finite moment completeness;
- moment/length-safe port transfer `E_m(z)`.

## 1. Motivation

The recurrent moment lift introduces infinitely many scalar characters

\[
P_m(H)=\sum_q c_q q^m,
\qquad m=0,1,2,\ldots
\]

for explicit positive-rational branch families. Primitive edge cells with bounded parallel multiplicity admit a finite Newton reconstruction, but after hidden path composition a finite moment cutoff need not remain complete at the port level.

The right exact carrier is not the moment sequence itself. It is the finite **histogram of exact positive-rational weights** from which all moments are derived.

Integral group semirings/algebras, Laurent polynomial rings, weighted automata/transfer series and rational formal series are classical mathematics. No generic novelty claim is made for them. The project-specific synthesis proposed here is their exact identification as the common parent carrier for BRC CWM, prime valuations, moments, recurrent generating functions and length-aware port collapse.

## 2. Exact positive-rational histogram semiring

Let

\[
G=\mathbb Q_{>0}^{\times}
\]

be the multiplicative group of positive rationals.

Define

\[
\boxed{\mathcal H=\mathbb N[G]}
\]

as the finite-support functions

\[
H:G\to\mathbb N_0.
\]

Write

\[
H=\sum_{q\in G}c_q[q].
\]

Interpretation: `c_q` is the number of explicit alternatives with exact positive rational weight `q`.

Addition is coefficientwise:

\[
(H\oplus K)(r)=H(r)+K(r).
\]

Multiplication is positive convolution:

\[
\boxed{
(H\otimes K)(r)
=\sum_{ab=r}H(a)K(b).
}
\]

Thus recoalescence unions alternatives and serial composition multiplies path weights while multiplying multiplicities.

The zero histogram is empty; the serial identity is `[1]`.

Because coefficients are non-negative, there is no cancellation and no zero-divisor support failure.

## 3. Exact branch-family embedding

A finite explicit branch family with weights

\[
q_1,\ldots,q_r
\]

maps to

\[
\boxed{
\eta(q_1,\ldots,q_r)
=\sum_{i=1}^r[q_i]
\in\mathcal H.
}
\]

Equal-weight parallel branches accumulate coefficient multiplicity.

This carrier forgets labels among branches with the same endpoint and exact weight, but it preserves the complete **weight multiset**. Hence

```text
full labeled provenance
-> exact weight histogram
-> CWM / moments / Boolean support
```

is a strict information hierarchy in general.

## 4. CWM as three histogram readouts

For nonzero `H`, define

\[
\boxed{C(H)=\sum_qc_q},
\]

\[
\boxed{W(H)=\sum_qc_qq},
\]

\[
\boxed{M(H)=\max\{q:c_q>0\}}.
\]

Use `C=W=M=0` on the zero histogram.

### Candidate BRC-U1

These are exact semiring readouts:

- `C` maps `H` to the natural count semiring `(+,*)`;
- `W` maps `H` to non-negative rational `(+,*)`;
- `M` maps `H` to max-times `(​max,*)`.

Therefore

\[
\boxed{
(C,W,M)
}

is a three-coordinate projection of one richer exact positive branch histogram carrier.

The existing finite positive-path realizability inequalities follow automatically from finite histogram support.

## 5. All integer moments are characters of the same carrier

For every integer `m>=0`, define

\[
\boxed{
\Phi_m(H)=\sum_qc_qq^m.
}
\]

Then

\[
\Phi_m(H\oplus K)=\Phi_m(H)+\Phi_m(K),
\]

\[
\Phi_m(H\otimes K)=\Phi_m(H)\Phi_m(K).
\]

Thus the recurrent branch-moment characters are not separate carriers; they are semiring homomorphisms out of `H`.

Special cases:

\[
\Phi_0=C,
\qquad
\Phi_1=W.
\]

For any finite nonzero histogram,

\[
\lim_{m\to\infty}\Phi_m(H)^{1/m}=M(H).
\]

Hence CWM is exactly the `(m=0,m=1,m=infinity/max)` boundary of the universal histogram carrier.

## 6. Prime-valuation Laurent form

Unique factorization gives

\[
G\cong\bigoplus_p\mathbb Z,
\qquad
q\longmapsto(v_p(q))_p.
\]

For a finite graph only finitely many primes occur in primitive branch weights. Let that finite set be `P`.

Introduce one Laurent variable `x_p` for each `p in P` and encode

\[
[q]
\longmapsto
X^{v(q)}
=\prod_{p\in P}x_p^{v_p(q)}.
\]

Then the exact positive histogram semiring is realized inside

\[
\boxed{
\mathbb N[x_p^{\pm1}:p\in P].
}
\]

Moment specialization is simply

\[
\boxed{x_p\mapsto p^m}.
\]

Indeed

\[
X^{v(q)}\mapsto\prod_pp^{mv_p(q)}=q^m.
\]

Count specialization is `x_p->1`; ordinary total mass is `x_p->p`.

This makes logarithm visibly derived: it is not needed to store or compose the exact carrier.

## 7. Universal weighted multigraph matrix

For an explicit positive-rational directed multigraph define

\[
\boxed{
\mathcal W_{ij}
=\sum_{e:i\to j}[q_e]
\in\mathcal H.
}
\]

Matrix multiplication is over the histogram semiring.

### Candidate BRC-U2 — exact fixed-length weight histogram

For every `n>=0`,

\[
\boxed{
(\mathcal W^n)_{ij}
=\sum_{q}c_{n,ij}(q)[q],
}
\]

where `c_{n,ij}(q)` is exactly the number of length-n paths from `i` to `j` whose total rational path weight is `q`.

Therefore each coefficient contains the complete path-weight multiset/histogram at that length.

Applying the readouts gives immediately:

\[
C_n=C(\mathcal W^n),
\]

\[
W_n=W(\mathcal W^n),
\]

\[
M_n=M(\mathcal W^n),
\]

and for every integer `m`,

\[
\boxed{
\Phi_m(\mathcal W^n)
=(W^{(m)})^n.
}
\]

Thus the universal histogram matrix simultaneously carries all fixed-length CWM and moment semantics.

## 8. Formal recurrent universal star

Introduce original-length marker `z` and define

\[
\boxed{
\mathcal G(z)
=\sum_{n\ge0}z^n\mathcal W^n.
}
\]

This is a matrix over

\[
\mathcal H[[z]],
\]

whose `z^n` coefficient is always a finite non-negative rational-weight histogram even when all-depth numerical count/mass diverges.

Formally,

\[
\boxed{
\mathcal G(z)=(I-z\mathcal W)^{-1}.
}
\]

This inverse is valid in formal power series because the constant term is `I`.

### Finite rational representation

Pass only for algebraic compression to the Laurent polynomial ring

\[
R_P=\mathbb Z[x_p^{\pm1}:p\in P]
\]

and its fraction field. Since the graph is finite,

\[
\det(I-z\mathcal W)
\]

is a finite polynomial in `z` with Laurent-polynomial coefficients and constant term `1`. The adjugate is finite as well. Hence every entry of `G(z)` has a finite rational-function representation.

The determinant/adjugate expression may contain negative coefficients from algebraic elimination. Those signs are compression/inclusion-exclusion only; the formal path-series coefficients remain non-negative histograms and no signed/amplitude BRC semantics is introduced.

## 9. All moment generating matrices are specializations

Because every `Phi_m` is a semiring homomorphism, coefficientwise formal specialization commutes with powers and the star:

\[
\boxed{
\Phi_m(\mathcal G(z))
=\sum_{n\ge0}z^n(W^{(m)})^n
=G_m(z).
}
\]

This is unconditional as a formal coefficient statement.

For rational-function evaluation, a specialization is valid algebraically wherever the specialized denominator is nonzero. It has positive recurrent-sum meaning only inside the corresponding stable region.

Thus the previously infinite moment tower is a family of readouts of one finite symbolic transfer object.

## 10. Universal port transfer

Partition the universal histogram matrix into hidden/port blocks:

\[
\mathcal W
=\begin{pmatrix}
\mathcal A&\mathcal X\\
\mathcal Y&\mathcal B
\end{pmatrix}.
\]

Define the formal universal port kernel

\[
\boxed{
\mathcal E(z)
=z\mathcal B
+z^2\mathcal Y(I-z\mathcal A)^{-1}\mathcal X.
}
\]

Its coefficient of `z^ell` is the exact histogram of rational weights of irreducible port-to-port path segments of original length `ell`.

### Candidate BRC-U3 — universal port boundary star

\[
\boxed{
(I-z\mathcal W)^{-1}[B,B]
=(I-\mathcal E(z))^{-1}
}
\]

as a formal histogram series.

Therefore `mathcal E(z)` is a finite symbolic black-box carrier that preserves **all exact path-weight histogram information by length** visible at the retained ports.

For every integer `m>=0`,

\[
\boxed{
\Phi_m(\mathcal E(z))
=E_m(z),
}
\]

where `E_m(z)` is the moment/length-safe port kernel derived in the parent research.

This solves the open all-moment port problem in a stronger representation: the infinite scalar family `E_m(z)` is generated by one finite prime-valuation/Laurent rational transfer object.

## 11. Contextual semantics

An external explicit positive-rational context attached only through the retained ports has its own universal histogram transfer entries. Schur elimination in the formal series algebra is unchanged.

Hence equality of universal port kernels `mathcal E(z)` implies equality of every visible exact path-weight histogram by length in every allowed finite explicit positive-rational context.

Conversely, the empty-context visible universal star recovers

\[
\boxed{
\mathcal E(z)=I-\mathcal G_B(z)^{-1}.
}
\]

Thus `mathcal E(z)` is the complete/minimal black-box signature, up to bijective re-encoding, for the observer that sees exact path-weight histograms by original length.

This is strictly stronger than total-mass `W_eff` and every fixed finite moment prefix in general.

## 12. CWM and moment readout after port collapse

For a fixed pair of ports and original length `n`, let

\[
H_{n,uv}=[z^n](I-\mathcal E(z))^{-1}_{uv}.
\]

Then exactly:

\[
C_{n,uv}=C(H_{n,uv}),
\]

\[
W_{n,uv}=W(H_{n,uv}),
\]

\[
M_{n,uv}=M(H_{n,uv}),
\]

and every moment is

\[
S_{m,n,uv}=\Phi_m(H_{n,uv}).
\]

Thus the universal port transfer is **CWM-safe coefficientwise in original length**, unlike ordinary total-mass Schur collapse.

It still does not preserve semantic labels distinguishing two paths of the same endpoints, length and exact rational weight.

## 13. Gauge naturality

Under positive rational vertex gauge

\[
q'_e=q_e\frac{h_t}{h_s},
\]

encode each vertex scale by its histogram/Laurent monomial `[h_i]`. Let

\[
\mathcal H=\operatorname{diag}([h_i]).
\]

Then

\[
\mathcal W'=\mathcal H^{-1}\mathcal W\mathcal H
\]

and

\[
\boxed{
\mathcal E'(z)
=\mathcal H_B^{-1}\mathcal E(z)\mathcal H_B.
}
\]

Moment specialization sends `[h_i]` to `h_i^m`, recovering the previously derived `H_m` gauge law. Count specialization sends every `[h_i]` to `1`, recovering exact gauge blindness at `m=0`.

This is the direct bridge between prime-valuation holonomy and the complete recurrent path-weight transfer.

## 14. Relation to finite moment completeness

For primitive edge cells with maximum parallel multiplicity `R`, Newton identities show that `W^(0)..W^(R)` reconstruct each primitive edge-weight multiset. That is one finite **scalar-coordinate compression** of `mathcal W`.

But after hidden path composition, a finite moment prefix of the collapsed port transfer need not remain complete because path multiplicity grows.

The universal histogram/Laurent transfer avoids that loss by preserving exact weight monomials before moment specialization.

Therefore the two finite representations solve different problems:

```text
primitive edge cell:
    finite moment prefix may reconstruct local histogram;

collapsed recurrent port:
    universal histogram/Laurent rational transfer preserves all moments directly.
```

## 15. Sharp witness resolving the port-prefix failure

Consider two modules with no parallel primitive edges, each having two disjoint length-2 internal routes from port `u` to port `v`.

Module A path weights:

\[
\{1/3,2/3\}.
\]

Module B path weights:

\[
\{1/4,3/4\}.
\]

Their universal port coefficients are

\[
[z^2]\mathcal E_A
=[1/3]+[2/3],
\]

\[
[z^2]\mathcal E_B
=[1/4]+[3/4],
\]

so the universal signature distinguishes them immediately.

But count and total-mass specializations coincide:

\[
\Phi_0=2,
\qquad
\Phi_1=1.
\]

The `m=2` specialization distinguishes them:

\[
5/9\ne5/8.
\]

Thus the universal carrier is exactly the missing information behind the earlier finite-prefix counterexample.

## 16. Prime-variable example

For the branch family

\[
\{1/3,2/3\},
\]

using variables `x_2,x_3`, the histogram is

\[
\boxed{x_3^{-1}+x_2x_3^{-1}}.
\]

Then:

- count: `x_2=x_3=1` gives `2`;
- total mass: `x_2=2,x_3=3` gives `1`;
- second moment: `x_2=4,x_3=9` gives `5/9`;
- in general `x_p=p^m` gives the exact m-th power sum.

No logarithm is needed.

## 17. Boundaries

This candidate does not claim:

- preservation of labeled path provenance beyond exact weight histogram multiplicity;
- efficient symbolic size in worst case — finite rational representability is not a complexity theorem;
- factoring speedup when constructing prime valuations;
- applicability to arbitrary irrational/complex/signed branch weights;
- that negative determinant/adjugate coefficients are signed BRC amplitudes;
- positive recurrent-sum meaning for specializations outside their stable region;
- that a finite scalar moment prefix is always complete after recurrent port collapse.

## 18. Prior-art boundary

Group semirings/algebras, Laurent polynomial representations of free abelian groups, weighted automata/rational series, transfer matrices, formal power series and Schur elimination are classical/general mathematics.

Enterprise Math does not claim those generic objects as novel.

The project-specific reusable synthesis proposed here is the identification

\[
\boxed{
\mathbb N[\mathbb Q_{>0}^{\times}]
}
\]

as the exact common BRC parent carrier whose readouts recover CWM and all integer moments and whose formal recurrent/port transfer provides a finite symbolic solution to the all-moment/all-length positive-rational black-box problem.

## 19. Validation plan

Use exact finite dictionaries keyed by `Fraction` for the positive histogram semiring and cross-check prime-valuation Laurent coordinates through the existing rational-holonomy tool.

1. Exhaust small histograms built from `{1/3,1/2,2/3,1,3/2}` and verify addition/convolution semiring laws plus count/total/max/moment readout homomorphisms.
2. On an explicit 3-state multigraph with parallel rational branches, compare histogram-matrix powers through length 5 with direct walk enumeration; verify CWM and moments `m=0..6` read from the same histogram.
3. Verify every histogram weight round-trips through prime valuations and that `x_p->p^m` matches direct `q^m` for `m=0..6`.
4. Build `det(I-z mathcal W)` for a small graph in the signed group-ring polynomial completion and verify the adjugate identity exactly, demonstrating finite rational representation while formal path coefficients remain non-negative.
5. On a 4-state hidden/port graph, compute universal port-segment histogram coefficients through length 7 and verify the reconstructed boundary histogram star equals the full histogram-matrix powers coefficientwise.
6. Specialize the universal port coefficients at `m=0..5` and verify they equal the independently computed moment/length port coefficients.
7. Verify rational vertex-gauge naturality of universal histogram transfer and its moment specializations.
8. Verify the `{1/3,2/3}` vs `{1/4,3/4}` port witness: universal signatures differ while m=0 and m=1 readouts coincide.

A dedicated research CI gate must pass before Foundation backflow.
