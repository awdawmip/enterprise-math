# Gregory–Machin continuation: complete one-correction classification and fixed-budget refinement law

Status: `FREE_RESEARCH / EXACT_CLASSIFICATION + COMPLETION_COST_THEOREMS / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Predecessor: `research_notes/GREGORY_LEIBNIZ_MACHIN_DISCRETE_TURN_COMPOSITION_20260903.md`

## 1. Frontier

The predecessor proved the exact rational-turn law, the relative-turn theorem, the Farey–Machin path theorem, the mediant refinement identity, and the criterion

\[
\operatorname{prim}((q+i)^k)=(A,B),\qquad
\text{one reciprocal-integer correction to }(1,1)
\iff |A-B|\in\{1,2\}.
\]

It left two questions open:

1. whether the bounded census
   \[(q,k)=(2,1),(2,2),(3,1),(3,2),(5,4)\]
   is globally complete;
2. what remains true when Farey refinement is charged a **fixed total series-term budget**, rather than equal truncation depth on every factor.

Both questions are resolved below at the stated layers.

No historical novelty is claimed for the classical Diophantine theorems, Størmer's classification, or Lehmer's computational measure. The project-level result is the exact bridge from the native integer turn/fan data to those completion-layer facts.

---

## 2. Exact gcd of a repeated reciprocal turn

Write

\[
(q+i)^k=X_k+iY_k,
\qquad
G_k:=\gcd(|X_k|,|Y_k|).
\]

### Theorem 2.1 — primitive-scale law

For every integer \(q\ge2\), \(k\ge1\),

\[
\boxed{
G_k=
\begin{cases}
1,&q\text{ even},\\[2mm]
2^{\lfloor k/2\rfloor},&q\text{ odd}.
\end{cases}}
\]

#### Proof

No odd rational prime can divide both \(X_k\) and \(Y_k\). If an odd prime \(p\) divided both, then the rational Gaussian integer \(p\) would divide \((q+i)^k\) in \(\mathbf Z[i]\).

- If \(p\equiv3\pmod4\), then \(p\) is Gaussian prime, so \(p\mid(q+i)\), impossible because its imaginary coordinate is \(1\).
- If \(p\equiv1\pmod4\), write \(p=\pi\bar\pi\). Rational divisibility by \(p\) forces both \(\pi\) and \(\bar\pi\) to divide \((q+i)^k\), hence both divide \(q+i\). Thus \(p\mid(q+i)\) as a rational Gaussian integer, again impossible.

So the common gcd is a power of two.

In \(\mathbf Z[i]\), \(2\) is associated to \((1+i)^2\). The criterion \((1+i)\mid(a+bi)\) is that \(a,b\) have the same parity. Therefore

\[
v_{1+i}(q+i)=
\begin{cases}
0,&q\text{ even},\\
1,&q\text{ odd}.
\end{cases}
\]

Hence \(v_{1+i}((q+i)^k)=0\) for even \(q\), and equals \(k\) for odd \(q\). A rational factor \(2^t\) contributes exactly \(2t\) factors of \(1+i\). Thus the greatest common rational power of two is \(2^{\lfloor k/2\rfloor}\) in the odd-\(q\) case. ∎

---

## 3. Reduction of the one-correction condition to two classical exponential equations

Let

\[
(A,B)=\frac1{G_k}(X_k,Y_k)
\]

be the primitive first-quadrant direction, so \(A,B>0\), \(\gcd(A,B)=1\). Assume the one-correction criterion

\[
|A-B|\in\{1,2\}.
\]

Set

\[
c:=|A-B|,
\qquad
S:=A+B,
\qquad
r:=S/c.
\]

The primitive norm is

\[
N:=A^2+B^2=\frac{(q^2+1)^k}{G_k^2}.
\]

### 3.1 Parity forces the value of \(c\)

If \(q\) is even, \(N=(q^2+1)^k\) is odd, so \(A,B\) have opposite parity and \(c\) is odd. Hence \(c=1\).

If \(q\) is odd, put

\[
M:=\frac{q^2+1}{2},
\]

which is odd. Then

\[
N=
\begin{cases}
M^k,&k\text{ even},\\
2M^k,&k\text{ odd}.
\end{cases}
\]

For even \(k\), \(N\) is odd, so again \(c=1\). For odd \(k\), \(N\equiv2\pmod4\), hence primitive \(A,B\) are both odd and \(c\) is even; therefore \(c=2\).

Thus:

\[
\boxed{
\begin{array}{c|c|c}
\text{case}&c&\text{exponential equation}\\ \hline
q\text{ even}&1&r^2+1=2(q^2+1)^k\\
q\text{ odd},\ k\text{ even}&1&r^2+1=2\left(\frac{q^2+1}{2}\right)^k\\
q\text{ odd},\ k\text{ odd}&2&r^2+1=\left(\frac{q^2+1}{2}\right)^k
\end{array}}
\]

The norm identities follow from

\[
A^2+B^2=\frac{S^2+c^2}{2}.
\]

This is the decisive reduction: the repeated-turn geometry has become a pair of classical Lebesgue–Nagell type equations, only after the native integer classification problem itself has been derived.

---

## 4. Global classification theorem

We use two classical facts at the number-theory audit layer:

1. **Lebesgue:** \(x^2+1=y^n\) has no positive nontrivial solution for \(n>1\).
2. **Størmer/Ljunggren/Cohn form:** for \(x>1,y>1,n>2\),
   \[
   x^2+1=2y^n
   \]
   has the unique solution
   \[
   (x,y,n)=(239,13,4).
   \]
   A modern source is H. Zhu, M. Le, A. Togbé, *On the exponential Diophantine equation* \(x^2+p^{2m}=2y^n\), Bull. Austral. Math. Soc. 86 (2012), 303–314, Lemmas 2.4 and 2.6, DOI `10.1017/S000497271200010X`.

### Theorem 4.1 — complete repeated-turn / one-correction classification

Let \(q\ge2\), \(k\ge1\), and suppose

\[
\operatorname{prim}((q+i)^k)=(A,B),
\qquad A,B>0.
\]

There exists one primitive reciprocal-integer correction from \((A,B)\) to the diagonal \((1,1)\) iff

\[
\boxed{(q,k)\in\{(2,1),(2,2),(3,1),(3,2),(5,4)\}.}
\]

#### Proof

For \(k=1\), direct use of \(|A-B|\in\{1,2\}\) gives

- even \(q\): \(q-1=1\), so \(q=2\);
- odd \(q\): \(q-1=2\), so \(q=3\).

For \(k=2\),

\[
(q+i)^2=(q^2-1)+2qi.
\]

If \(q\) is even, the primitive difference is

\[
q^2-2q-1,
\]

which has absolute value one only at \(q=2\). If \(q\) is odd, divide by \(2\); the primitive difference is

\[
\frac{q^2-2q-1}{2},
\]

whose absolute value is one only at \(q=3\).

Now let \(k>2\).

- In the even-\(q\) case and the odd-\(q\), even-\(k\) case, Section 3 gives \(r^2+1=2M^k\) with \(M>1\). The classical uniqueness theorem forces
  \[
  (r,M,k)=(239,13,4).
  \]
  The even-\(q\) branch would require \(q^2+1=13\), impossible in integers. The odd-\(q\) branch requires
  \[
  \frac{q^2+1}{2}=13,
  \]
  so \(q=5\), and \(k=4\).
- In the odd-\(q\), odd-\(k\) branch, Section 3 gives \(r^2+1=M^k\), excluded by Lebesgue for \(k>1\).

This leaves exactly the five stated ordered repeated-turn seeds. ∎

### Corollary 4.2 — four distinct two-term formulas

The five ordered seeds collapse to four distinct identities:

\[
\boxed{\frac\pi4=\arctan\frac12+\arctan\frac13,}
\]

\[
\boxed{\frac\pi4=2\arctan\frac12-\arctan\frac17,}
\]

\[
\boxed{\frac\pi4=2\arctan\frac13+\arctan\frac17,}
\]

\[
\boxed{\frac\pi4=4\arctan\frac15-\arctan\frac1{239}.}
\]

The \((2,1)\) and \((3,1)\) seeds are the same first identity with the two factors exchanged.

### Prior-art audit

C. Størmer gave a complete integral classification of

\[
m\arctan(1/x)+n\arctan(1/y)=k\pi/4
\]

in 1899: *Solution complète en nombres entiers de l'équation* \(m\arctan(1/x)+n\arctan(1/y)=k\pi/4\), Bull. Soc. Math. France 27 (1899), 160–170, DOI `10.24033/bsmf.603`.

Modern summaries explicitly identify the four displayed identities as the four nontrivial integral two-term cases. Therefore **historical novelty is not claimed for the list**.

What is structurally useful for #1160 is stronger in a different direction: the native repeated-turn/one-correction ansatz, derived without arctangent at input, lands on all four classical nontrivial two-term identities. Størmer's theorem then shows that this apparently special native ansatz loses no nontrivial two-term integral reciprocal-arctangent identity after completion.

Freeze:

`NATIVE_ONE_CORRECTION_COMPLETENESS_WITHIN_TWO_TERM_INTEGER_COMPLETION != HISTORICALLY_NEW_STORMER_CLASSIFICATION`.

---

## 5. Fixed total series-term budget

For \(D\ge2\), let the \(t\)-term arctangent truncation be

\[
A_t(D)=\sum_{n=0}^{t-1}\frac{(-1)^n}{(2n+1)D^{2n+1}},
\qquad t\ge1.
\]

The alternating remainder satisfies

\[
\left|\arctan\frac1D-A_t(D)\right|
< R_D(t),
\qquad
\boxed{R_D(t):=\frac1{(2t+1)D^{2t+1}}.}
\]

Consider a completed Machin-type identity with **distinct** denominators

\[
\frac\pi4=\sum_{j=1}^m c_j\arctan\frac1{D_j},
\qquad c_j\in\mathbf Z\setminus\{0\},\ D_j>1.
\]

If the \(j\)-th distinct series receives \(t_j\ge1\) terms, define the robust certified error proxy

\[
\boxed{
E(\mathbf t)=\sum_{j=1}^m |c_j|R_{D_j}(t_j),
\qquad
T=\sum_j t_j.
}
\]

The cost model counts one term evaluation per distinct arctangent series; multiplication by a fixed integer coefficient is treated as lower-order overhead. This is a completion-layer computation model, not a native geometric primitive.

### Theorem 5.1 — exact greedy allocation

Define the marginal certified-error reduction from adding one further term to component \((c,D)\) after \(t\) terms:

\[
\Delta_{c,D}(t)
:=|c|\bigl(R_D(t)-R_D(t+1)\bigr).
\]

Then \(\Delta_{c,D}(t)\) is strictly decreasing in \(t\). Consequently, after assigning the mandatory first term to every distinct series, the globally optimal allocation for every fixed integer budget \(T\ge m\) is obtained by repeatedly assigning the next term to the component with the currently largest \(\Delta\).

#### Proof

The remainder ratio is

\[
\frac{R_D(t+1)}{R_D(t)}
=\frac{2t+1}{2t+3}D^{-2}.
\]

Hence

\[
\Delta_{c,D}(t)
=|c|R_D(t)
\left(1-\frac{2t+1}{2t+3}D^{-2}\right).
\]

As \(t\) increases, both positive factors on the right strictly decrease: \(R_D(t)\) decreases, while the subtracted ratio increases. Therefore the marginal gains are strictly diminishing.

The objective is a sum of independent one-dimensional decreasing sequences with diminishing marginal gains. The standard exchange argument now applies: if an allocation contains an added term with smaller marginal gain while omitting an available larger marginal gain on another component, exchanging those two choices strictly lowers \(E\). Repeating removes every inversion and yields exactly the greedy allocation. ∎

---

## 6. Lehmer measure is the asymptotic fixed-budget exponent

Let

\[
E^*(T)=\min_{t_j\ge1,\ \sum t_j=T}E(\mathbf t).
\]

### Theorem 6.1 — asymptotic allocation law

For fixed distinct \(D_j>1\),

\[
\boxed{
\frac{t_j^*(T)}{T}
\longrightarrow
\frac{1/\ln D_j}{\sum_{\ell=1}^m1/\ln D_\ell}.}
\]

Moreover,

\[
\boxed{
-\frac1T\ln E^*(T)
\longrightarrow
\Gamma(D_1,\ldots,D_m)
:=\frac{2}{\sum_{j=1}^m1/\ln D_j}.}
\]

#### Proof sketch

At an optimal large-budget allocation every component receives unboundedly many terms; otherwise its nonvanishing fixed remainder would dominate an allocation in which all components are refined.

The greedy threshold implies that occupied marginal gains are equal up to the ratio of one neighboring marginal step. Since

\[
\Delta_{c,D}(t)
=\Theta\!\left(\frac{|c|}{t}D^{-2t}\right),
\]

taking logarithms gives, uniformly across components,

\[
2t_j\ln D_j=\Lambda_T+O(\ln T).
\]

Summing \(t_j=T\) yields

\[
\Lambda_T
=\frac{2T}{\sum_j1/\ln D_j}+O(\ln T),
\]

which gives the allocation fractions and the exponential rate. The integer coefficients affect only the lower-order logarithmic correction, not the leading exponent. ∎

D. H. Lehmer's classical measure for reciprocal-integer Machin formulas is

\[
\mu=\sum_j\frac1{\log_{10}D_j}
=\ln(10)\sum_j\frac1{\ln D_j}.
\]

Therefore the theorem gives the exact bridge

\[
\boxed{
\Gamma=\frac{2\ln10}{\mu}.}
\]

So Lehmer's denominator-only measure appears naturally as the reciprocal leading exponent of the exact fixed-total-term allocation problem. This also explains why the integer coefficients do not enter Lehmer's leading measure: they change constants and finite-budget allocation thresholds, but not the exponential rate.

Historical boundary: Lehmer's measure itself is classical (D. H. Lehmer, *On Arccotangent Relations for* \(\pi\), Amer. Math. Monthly 45 (1938), 657–664). No novelty claim is made for the measure.

---

## 7. Machin is finite-budget dominant among the complete Størmer four

For the four nontrivial completed identities, use the robust objective above. Let

\[
E_F^*(T)
\]

denote the optimal certified bound at total budget \(T\ge2\).

### Theorem 7.1

For every integer \(T\ge2\), the original Machin formula

\[
4\arctan(1/5)-\arctan(1/239)
\]

has a strictly smaller optimal absolute alternating-remainder bound than each of the other three Størmer identities, under the stated two-distinct-series term-count model.

#### Proof

For every \(t\ge1\),

\[
4R_5(t)<R_2(t),
\]

because

\[
\frac{4R_5(t)}{R_2(t)}
=4\left(\frac25\right)^{2t+1}
\le4\left(\frac25\right)^3
=\frac{32}{125}<1.
\]

Therefore also \(4R_5(t)<2R_2(t)\). Likewise

\[
\frac{4R_5(t)}{2R_3(t)}
=2\left(\frac35\right)^{2t+1}
\le2\left(\frac35\right)^3
=\frac{54}{125}<1.
\]

For every \(s\ge1\),

\[
R_{239}(s)<R_3(s),\qquad R_{239}(s)<R_7(s).
\]

Thus, for **every common allocation** \((t,s)\), Machin's bound is strictly below the corresponding bound of

- \(\arctan(1/2)+\arctan(1/3)\),
- \(2\arctan(1/2)-\arctan(1/7)\),
- \(2\arctan(1/3)+\arctan(1/7)\).

Apply this pointwise inequality to an optimal allocation of each competitor. Machin can use the same allocation, so its optimum is strictly smaller. ∎

This is stronger than merely comparing asymptotic Lehmer measures: it holds for every finite total budget \(T\ge2\) under the declared error-bound model.

---

## 8. Fixed-depth refinement and fixed-budget refinement point in different directions

The predecessor proved that every mediant refinement of a positive unimodular edge

\[
u\to v,
\qquad D=u\cdot v,
\]

with \(w=u+v\) and

\[
D_1=D+\|u\|^2,
\qquad
D_2=D+\|v\|^2,
\]

strictly lowers

\[
D^{-p}\mapsto D_1^{-p}+D_2^{-p}
\]

for every \(p\ge1\). Hence **equal truncation depth per edge always benefits from refinement**.

Under a fixed total term budget, however, splitting one series into two consumes two refinement channels. The correct asymptotic comparison is via

\[
\Gamma_{\rm old}=2\ln D,
\qquad
\Gamma_{\rm split}
=\frac{2}{1/\ln D_1+1/\ln D_2}.
\]

### Lemma 8.1 — logarithmic product maximization

For all \(x,y>0\),

\[
\boxed{
\ln(1+x)\ln(1+y)
\le
\ln^2(1+\sqrt{xy}).}
\]

Proof: fix \(xy=c\), write \(x=\sqrt c\,e^t\), \(y=\sqrt c\,e^{-t}\), and

\[
F(t)=\ln(1+\sqrt c\,e^t)\ln(1+\sqrt c\,e^{-t}).
\]

For \(z>0\),

\[
\phi(z):=\frac{z}{(1+z)\ln(1+z)}
\]

is strictly decreasing because

\[
\frac{d}{dz}\ln\phi(z)
=\frac{\ln(1+z)-z}{z(1+z)\ln(1+z)}<0.
\]

Hence \(F'(t)/F(t)=\phi(\sqrt c\,e^t)-\phi(\sqrt c\,e^{-t})<0\) for \(t>0\). Since \(F\) is even, its maximum is at \(t=0\). ∎

### Theorem 8.2 — local fixed-budget refinement phase boundary

For an isolated positive unimodular edge:

- \(D=1\): mediant refinement changes the Gregory boundary into the \((2,3)\) pair and upgrades polynomial convergence to exponential convergence;
- \(D=2\): the unique label split is \((3,7)\), and fixed-budget asymptotic efficiency **improves**;
- every \(D\ge3\): fixed-budget asymptotic efficiency **strictly worsens** under one mediant split.

#### Proof for \(D\ge3\)

Set

\[
a=\|u\|^2,\qquad b=\|v\|^2.
\]

Lagrange's determinant-one identity gives

\[
ab=D^2+1.
\]

Thus with \(x=a/D\), \(y=b/D\),

\[
xy=1+D^{-2}\le\frac{10}{9}.
\]

The split is asymptotically better iff

\[
\frac1{\ln D_1}+\frac1{\ln D_2}<\frac1{\ln D},
\]

which is equivalent to

\[
\ln(D_1/D)\ln(D_2/D)>(\ln D)^2.
\]

But Lemma 8.1 gives

\[
\ln(D_1/D)\ln(D_2/D)
=\ln(1+x)\ln(1+y)
\le\ln^2\left(1+\sqrt{10/9}\right)
<\ln^2 3
\le\ln^2D.
\]

So the improvement inequality is impossible; the split strictly worsens the exponent.

#### Proof for \(D=2\)

Here \(ab=D^2+1=5\). Since \(a,b\) are positive integers, \(\{a,b\}=\{1,5\}\), so \(\{D_1,D_2\}=\{3,7\}\).

We need

\[
\frac1{\ln3}+\frac1{\ln7}<\frac1{\ln2}.
\]

Equivalently,

\[
\log_2(3/2)\,\log_2(7/2)>1.
\]

Now

\[
\log_2(3/2)>\frac7{12}
\]

because \(3^{12}>2^{19}\), and

\[
\log_2(7/2)>\frac{12}{7}
\]

because \(7^7>2^{19}\). Their product is therefore strictly greater than one. ∎

### Interpretation

There are now two rigorously distinct monotonicities:

\[
\boxed{
\text{equal depth per edge: every mediant refinement helps};}
\]

\[
\boxed{
\text{fixed total terms: only the }D=1,2\text{ local refinements help asymptotically}.}
\]

This is the first sharp compute-sensitive boundary in the #1160 refinement hierarchy.

Boundary: the theorem is **local to an isolated denominator component**. If a refinement creates a denominator already present elsewhere in the completed formula, duplicate-series compression can change the global term-count comparison and must be analyzed separately.

---

## 9. Structural synthesis

The #1160 hierarchy now separates into four layers:

\[
\boxed{
\text{integer/Gaussian turn composition}
\to
\text{unimodular/Farey finite resolution}
\to
\text{Diophantine factorization constraints}
\to
\text{analytic completion + compute allocation}.}
\]

New exact statements from this continuation:

1. \(\gcd(\Re(q+i)^k,\Im(q+i)^k)\) is completely controlled by the ramified prime \(1+i\);
2. the five bounded census hits are globally complete;
3. they collapse to the classical four nontrivial Størmer two-term identities;
4. the native repeated-turn/one-correction ansatz reaches all of those classical cases;
5. finite series-budget allocation has an exact greedy law;
6. Lehmer's measure is exactly the reciprocal leading exponent of that allocation problem;
7. Machin's \((5,239)\) formula is finite-budget dominant among the complete Størmer four under the robust alternating-remainder objective;
8. mediant refinement has a compute-sensitive phase boundary at edge label \(D=2\): equal-depth monotonicity survives everywhere, but fixed-total-work asymptotic monotonicity does not.

## 10. Next frontier

The remaining high-value question is no longer the one-correction classification. It is the **multi-correction signed factorization problem**:

> among exact integer/Gaussian turn words whose product lands on the diagonal, classify or optimize the denominator multiset before analytic completion, with winding and coefficient reuse typed explicitly.

A natural completion-layer objective is the Lehmer functional, but the native search should retain the exact denominator multiset / signed Gaussian certificate and must not define the native path by logarithms or by the target numerical value of \(\pi\).

Potential next theorem target:

\[
\texttt{SIGNED\_UNIMODULAR\_FACTORIZATION\_PARETO\_FRONTIER}
\]

with exact endpoint certificate, finite winding class, coefficient reuse, and a proof/counterexample for whether a canonical shortest native factorization exists independently of the chosen completion-cost functional.
