# Finite Recurrent Weighted-BRC — Exact Rational Gauge Stability

Status: `RESEARCH CANDIDATE / EXACT FINITE-MATRIX THEOREM PACKAGE / NO FOUNDATION MUTATION YET`

Researcher-ID: `EM-STW-B9F4C2`
Baseline: `main@8f53372633fd810f32d30f953ae617dc059888f0`
Global substrate: `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`
Prior boundary opened: `WBRC-N05-GENERAL-SCC-NOT-PROMOTED`

## 0. Result summary

The one-state recurrent Weighted-BRC stability law extends to arbitrary finite non-negative rational transition systems without requiring a floating spectral-radius oracle.

Let a finite positive weighted multigraph have total one-step mass matrix

\[
W=(W_{ij})\in M_n(\mathbb Q_{\ge0}),
\]

where \(W_{ij}\) is the sum of the weights of all one-step branches from state \(i\) to state \(j\).

Then the total mass of all length-\(k\) walks from \(i\) to \(j\) is exactly

\[
(W^k)_{ij}.
\]

The all-depth mass is stable exactly when any — hence all — of the following equivalent exact conditions hold:

1. \(\sum_{k\ge0}W^k\) converges entrywise;
2. there exists \(h\in\mathbb Q_{>0}^n\) with \(Wh<h\) coordinatewise;
3. \(I-W\) is invertible and the canonical potential
   \[
   x=(I-W)^{-1}\mathbf 1
   \]
   has strictly positive rational coordinates;
4. there exists a positive rational diagonal gauge \(H=\operatorname{diag}(h)\) such that every row sum of
   \[
   B=H^{-1}WH
   \]
   is strictly below one;
5. after clearing denominators \(W=A/D\), there exists \(h\in\mathbb N_{>0}^n\) with
   \[
   Ah<Dh.
   \]

Thus finite recurrent positive Weighted-BRC has a purely rational, and after denominator clearing purely integer, stability certificate.

Moreover there is a complementary integer divergence certificate: if no stable certificate exists, there is a nonzero \(y\in\mathbb N_0^n\) such that

\[
 y^\top A\ge D y^\top.
\]

Exactly one of the stable and divergent certificate classes exists.

Candidate typed names:

- `BRC_FINITE_RECURRENT_MASS_POTENTIAL_CERTIFICATE`;
- `BRC_INTEGER_GAUGE_STABILITY_ALTERNATIVE`;
- `BRC_CANONICAL_STAR_BUDGET`.

The package is classical in its matrix-analysis ingredients (Neumann series, non-negative matrices, M-matrix / positive-vector criteria, Gordan–Stiemke linear alternatives). The Enterprise-Math value claimed here is the exact integration with the typed Weighted-BRC carrier, the positive projective gauge already present in the Foundation, and an integer certificate interface that avoids making an eigenvalue a primitive research state.

## 1. Finite path mass collapses to one rational matrix

Let the directed branch multigraph have states \(1,\ldots,n\). For every individual edge \(e:i\to j\), let its positive rational weight be \(w_e\).

Define

\[
W_{ij}=\sum_{e:i\to j}w_e.
\]

### Theorem R1 — exact length-\(k\) mass matrix

For every \(k\ge0\), the total positive weight of all length-\(k\) walks from \(i\) to \(j\) is \((W^k)_{ij}\).

### Proof

At \(k=0\), the only empty walk contributes the identity matrix.

Assume the statement for \(k\). Every length-\(k+1\) walk from \(i\) to \(j\) has a unique penultimate state \(r\), and its weight is the product of a length-\(k\) prefix weight and one final edge weight. Summing over all prefixes, final parallel edges, and intermediate states gives

\[
\sum_r (W^k)_{ir}W_{rj}=(W^{k+1})_{ij}.
\]

So ordinary rational matrix multiplication is exactly the non-idempotent path-sum expansion for the total-mass coordinate. ∎

This is only the \(W\)-projection of CWM. Count and dominant-path observables still require their own coordinates. But for the question “does the total all-depth positive branch mass converge?”, \(W\) is sufficient.

## 2. Mass-stability definition

Define the partial star

\[
S_N=I+W+\cdots+W^N.
\]

Because every entry is non-negative, every entry of \(S_N\) is monotone in \(N\).

Call the finite recurrent branch system **mass-stable** when every entry has a finite limit:

\[
W^*=\sum_{k\ge0}W^k<\infty
\]

entrywise.

This is the natural finite-state extension of `WBRC-T09`, where the one-state matrix is simply \(W=[S]\).

## 3. Positive rational potential certificate

### Theorem R2 — potential criterion

For \(W\in M_n(\mathbb Q_{\ge0})\), the following are equivalent:

\[
\boxed{W^*\text{ is finite entrywise}}
\]

and

\[
\boxed{\exists h\in\mathbb Q_{>0}^n:\ Wh<h.}
\]

### Proof: potential implies stability

Assume \(Wh<h\). Define

\[
\alpha=\max_i\frac{(Wh)_i}{h_i}.
\]

All quantities are rational and

\[
0\le\alpha<1.
\]

Hence

\[
Wh\le\alpha h,
\qquad
W^k h\le\alpha^k h.
\]

For the \(j\)-th basis vector \(e_j\),

\[
e_j\le\frac{h}{h_j}.
\]

Because \(W\) is non-negative,

\[
W^k e_j\le\alpha^k\frac{h}{h_j}.
\]

Thus every entry satisfies

\[
0\le(W^k)_{ij}\le\alpha^k\frac{h_i}{h_j},
\]

and therefore

\[
\sum_{k\ge0}(W^k)_{ij}
\le
\frac{h_i/h_j}{1-\alpha}<\infty.
\]

### Proof: stability implies rational potential

If \(S_N\to S\) entrywise, then \(W^{N+1}\to0\) entrywise and

\[
(I-W)S_N=I-W^{N+1}\to I.
\]

Therefore

\[
(I-W)S=I,
\]

so \(I-W\) is invertible and

\[
S=(I-W)^{-1}.
\]

Since \(I-W\) has rational entries, its inverse is rational. Put

\[
h=S\mathbf1.
\]

Then \(h\in\mathbb Q_{>0}^n\) and

\[
Wh=(S-I)\mathbf1=h-\mathbf1<h.
\]

∎

This proof never requires numerical eigenvalue evaluation.

## 4. Canonical star budget

The previous proof gives a canonical stable potential:

\[
\boxed{x=(I-W)^{-1}\mathbf1=W^*\mathbf1.}
\]

Interpretation: \(x_i\) is exactly the total all-depth positive mass of all finite walks starting at state \(i\) and ending anywhere, including the empty walk.

It obeys

\[
Wx=x-\mathbf1.
\]

Hence every \(x_i\ge1\).

The star itself is exact and rational:

\[
\boxed{W^*=(I-W)^{-1}\in M_n(\mathbb Q_{\ge0}).}
\]

No infinite numerical summation is needed once stability is certified.

## 5. Gauge-local form of stability

Let \(h\in\mathbb Q_{>0}^n\) and

\[
H=\operatorname{diag}(h_1,\ldots,h_n).
\]

Define the state gauge

\[
B=H^{-1}WH,
\qquad
B_{ij}=W_{ij}\frac{h_j}{h_i}.
\]

Then

\[
\sum_jB_{ij}=\frac{(Wh)_i}{h_i}.
\]

Therefore:

### Theorem R3 — gauge-localization

\[
\boxed{
\exists h>0:\ Wh<h
\iff
\exists H>0\text{ diagonal rational}:\ \sum_j(H^{-1}WH)_{ij}<1\ \forall i.
}
\]

So global recurrent stability is equivalent to the existence of a gauge in which **every state is locally subcritical by ordinary outgoing total mass**.

This makes the raw row-sum test a special case: choosing \(h=(1,\ldots,1)\) tests the ungauged representation only.

### Canonical row deficits

For the canonical potential \(x=W^*\mathbf1\),

\[
\sum_j(X^{-1}WX)_{ij}
=
\frac{x_i-1}{x_i}
=1-\frac1{x_i}.
\]

Thus the canonical gauge has exact local deficit

\[
\boxed{\varepsilon_i=\frac1{x_i}.}
\]

The farther \(x_i\) is above one, the closer that normalized state is to the local mass threshold.

No probability interpretation is asserted; `deficit` is an algebraic budget coordinate.

## 6. Gauge does not change closed-cycle weight

For a path

\[
p:i_0\to i_1\to\cdots\to i_k,
\]

the gauged path product is

\[
\prod_{r=0}^{k-1}B_{i_ri_{r+1}}
=
\frac{h_{i_k}}{h_{i_0}}
\prod_{r=0}^{k-1}W_{i_ri_{r+1}}.
\]

All internal gauge factors telescope.

For a closed cycle \(i_k=i_0\),

\[
\boxed{\prod B_e=\prod W_e.}
\]

Therefore the stabilizing gauge does not “hide” a growing closed loop. It only redistributes absolute state scale, exactly in the spirit of the already-canonical projective/gauge Weighted-BRC layer.

## 7. Pure integer stability certificate

Let \(D\) be a positive common denominator of all entries of \(W\), and write

\[
W=\frac AD,
\qquad
A\in M_n(\mathbb N_0).
\]

Since every rational positive potential can be multiplied by a common denominator, Theorem R2 gives:

### Theorem R4 — integer gauge certificate

\[
\boxed{
W^*<\infty
\iff
\exists h\in\mathbb N_{>0}^n:\ Ah<Dh.
}
\]

Because both sides of each coordinate inequality are integers, this can equivalently be written

\[
(Ah)_i\le D h_i-1.
\]

This is an exact finite certificate over integers only.

For one state, \(W=[N/D]\), the certificate with \(h=1\) becomes exactly

\[
N<D,
\]

i.e. the previous one-state law \(S<1\).

## 8. Exact stable/divergent alternative

The integer certificate has a dual.

### Theorem R5 — integer stability alternative

Exactly one of the following holds:

**Stable certificate**

\[
\exists h\in\mathbb N_{>0}^n:\ Ah<Dh;
\]

**Divergence certificate**

\[
\exists y\in\mathbb N_0^n\setminus\{0\}:\ y^\top A\ge D y^\top.
\]

### Why the two cannot coexist

If both held, then multiplying the strict stable inequality by \(y^\top\ge0\) would give

\[
y^\top Ah<Dy^\top h,
\]

while the divergence inequality multiplied by \(h>0\) would give

\[
y^\top Ah\ge Dy^\top h,
\]

a contradiction.

### Completeness route

Put

\[
B=DI-A.
\]

The stable side asks for \(h\) such that simultaneously

\[
Bh>0,
\qquad h>0.
\]

Apply the finite-dimensional Gordan–Stiemke linear alternative to the stacked rational matrix

\[
\begin{pmatrix}B\\I\end{pmatrix}.
\]

If no such \(h\) exists, there are non-negative dual multipliers \((y,s)\ne0\) with

\[
B^\top y+s=0.
\]

Thus \(B^\top y\le0\), and necessarily \(y\ne0\), so

\[
y^\top A\ge Dy^\top.
\]

The feasible dual cone is rational, so a rational certificate can be chosen and scaled to an integer one.

### Divergence from the dual certificate

From

\[
y^\top W\ge y^\top
\]

and \(W\ge0\), induction gives

\[
y^\top W^k\ge y^\top
\]

for every \(k\). Hence the all-depth mass cannot converge.

So stable and divergent recurrent phases both admit finite exact integer witnesses.

## 9. A stable graph whose raw row sum looks supercritical

Consider

\[
W=
\begin{pmatrix}
0&1/2\\
1/2&2/3
\end{pmatrix}.
\]

Its raw row sums are

\[
1/2,\qquad 7/6.
\]

Thus a naive local row-sum test rejects the second state.

But

\[
(I-W)^{-1}
=
\begin{pmatrix}
4&6\\
6&12
\end{pmatrix},
\]

so the canonical potential is

\[
x=(10,18).
\]

Indeed

\[
Wx=(9,17)<(10,18).
\]

In the canonical gauge, the row sums become

\[
9/10,\qquad17/18.
\]

Thus the graph is globally stable even though one raw state looks locally supercritical. The gauge exposes the correct local budgets.

## 10. Dominant-path contraction is weaker than total-mass stability

Let \(M_{ij}\) denote the largest individual one-step branch weight from \(i\) to \(j\). Then

\[
0\le M_{ij}\le W_{ij}.
\]

If \(h\) is a total-mass stability potential, then in the same gauge

\[
M_{ij}\frac{h_j}{h_i}
\le
W_{ij}\frac{h_j}{h_i}
<1
\]

for every live edge, since the full row sum is below one.

Therefore total-mass stability forces strict contraction of every closed dominant cycle.

The converse fails.

Take the two-state complete graph with one branch of weight \(3/5\) for every ordered pair:

\[
W=M=
\begin{pmatrix}
3/5&3/5\\
3/5&3/5
\end{pmatrix}.
\]

Every individual length-\(k\) path has weight

\[
(3/5)^k\to0,
\]

so the dominant path strictly contracts.

But the total outgoing one-step mass is

\[
6/5>1
\]

at both states, and with \(y=(1,1)\)

\[
y^\top W=\frac65y^\top\ge y^\top.
\]

Hence total branch mass diverges.

This is the finite multi-state analogue of the previous two-loop \((3/5,3/5)\) witness.

The instability is purely multiplicity-driven: in the symmetric raw gauge, the max one-step log is \(\ln(3/5)\), while the two-way recoalescence adds \(\ln2\), producing

\[
\ln(3/5)+\ln2=\ln(6/5)>0.
\]

## 11. Exact decision without spectral materialization

The theorem package gives a direct exact decision routine for rational \(W\):

1. form \(I-W\) over `Fraction`;
2. if it is singular, the system is not mass-stable;
3. otherwise solve
   \[
   (I-W)x=\mathbf1;
   \]
4. the system is mass-stable iff every coordinate of \(x\) is positive;
5. on the stable side, return
   \[
   W^*=(I-W)^{-1},\quad x=W^*\mathbf1,
   \]
   plus an integer-scaled potential certificate;
6. on the unstable side, an independently supplied left superinvariant vector \(y\) is an exact divergence certificate.

This is not a claim that spectral radius is invalid. Classically, non-negative matrix stability is normally organized by Perron–Frobenius / spectral-radius / M-matrix language. The point is narrower:

> for the rational finite BRC carrier, the yes/no phase and the stable star admit finite exact rational/integer certificates without numerically materializing the spectrum.

## 12. Strong connectivity is not required

The proofs above did not use irreducibility or strong connectivity. Therefore the candidate theorem is stronger than the initial SCC target:

\[
\boxed{
\text{FINITE NON-NEGATIVE RATIONAL TRANSITION SYSTEM}
\Longrightarrow
\text{EXACT POTENTIAL/GAUGE STABILITY CRITERION}.
}
\]

Strong connectivity remains useful when interpreting the system as one recurrent communicating block, but it is not a theorem hypothesis.

This matters for future SCC decomposition: each recurrent block can be handled with the same certificate, while acyclic feed-forward structure can remain outside the recurrent core.

## 13. Boundaries

This result does **not** yet promote a new Foundation theorem.

It also does not claim:

- a novel matrix theorem independent of classical M-matrix / Neumann-series / Gordan–Stiemke theory;
- an exact algebraic value for the spectral radius;
- a probability or Markov interpretation of weights;
- signed/amplitude cancellation semantics;
- a finite natural path-count closure on a recurrent SCC;
- that dominant/max-path stability implies total-mass stability;
- an infinite-state theorem;
- a canonical minimal integer potential \(h\).

The finite path-count coordinate still diverges on recurrent components. The current result concerns the positive **total-mass** projection and its gauge-local certificate.

## 14. Tool reuse / gap classification

This route extends existing machinery rather than opening a new general family:

- `T0_BRC / t0.weighted_brc_cwm` supplies the positive weighted branch semantics and projective gauge boundary;
- `T12` max/idempotent path closure supplies the dominant-path comparison layer but not the non-idempotent total-mass criterion;
- the new exact finite-matrix experiment is a bounded research specialization of T0, not a new top-level toolbox family.

The semantic gap is precisely recurrent non-idempotent mass closure over a finite rational transition matrix.

## 15. Next

1. Build and validate an exact `Fraction` checker for R1–R5, including star, gauge, integer certificates and dual witnesses.
2. Test the stable-but-raw-supercritical and dominant-stable/total-unstable examples as regression guards.
3. If the theorem package survives exact CI, decide whether to extend `t0.weighted_brc_cwm` with a finite recurrent matrix subtool and backflow `WBRC-N05` into a proved finite-matrix theorem while retaining infinite-state and signed boundaries.
4. After that, study recurrent **future-safe quotient** using exact star rows/target columns rather than finite-DAG path counts.
