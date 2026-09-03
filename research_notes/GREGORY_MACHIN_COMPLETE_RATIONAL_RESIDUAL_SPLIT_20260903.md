# Gregory–Machin continuation: complete rational-residual split theorem and blind recovery of the 1.48912 six-term identity

Status: `FREE_RESEARCH / EXACT_RESIDUAL_FACTORIZATION THEOREM + LOCAL_LEHMER_OPTIMALITY + EXECUTABLE_BLIND_PIPELINE / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_h7m_support5_residual_surgery_census_20260903.py`
Depends on: exact rational-turn group, relative-turn theorem, Gaussian valuation-circuit endpoint theorem.

## 1. Why another layer is needed

The H=7M smooth support-six census blindly rediscovers Hwang's 1997 formula with Lehmer measure about `1.51244`.  A subsequent historical audit located a 2010 paper by Amrik Singh Nimbran reporting the six-term identity

\[
\frac\pi4
=83\arctan\frac1{107}
+17\arctan\frac1{4443}
+34\arctan\frac1{5726}
-5\arctan\frac1{110443}
+5\arctan\frac1{4841182}
-34\arctan\frac1{1737720807},
\]

with Lehmer measure about `1.48912`.

Modern formula compilations still commonly list Hwang's `1.51244` formula as the best known integer-reciprocal Machin formula.  The project therefore treats the literature status as inconsistent and does not use either source as mathematical authority.  Instead, the native endpoint and winding calculus is used to verify the smaller-measure identity exactly and to reconstruct its derivation without numerical pi fitting.

No historical novelty is claimed for Nimbran's formula or for classical Gaussian-integer manipulation.

## 2. Complete two-reciprocal decomposition theorem for a rational residual

Let

\[
R=[A+iB],\qquad A>B>0,\qquad\gcd(A,B)=1
\]

be a primitive positive rational-turn direction, and put

\[
N=A^2+B^2.
\]

We seek all decompositions into two positive reciprocal integer turns with opposite signs:

\[
\boxed{R=[m+i][n-i]},\qquad 1\le m<n.
\]

Raw multiplication gives

\[
(m+i)(n-i)=(mn+1)+(n-m)i.
\]

The two pairs are positively proportional iff

\[
B(mn+1)=A(n-m).
\]

Rearranging and factoring yields the exact Diophantine law

\[
\boxed{(Bm-A)(Bn+A)=-(A^2+B^2).}
\]

This is the complete residual-split equation.

### Theorem 2.1 — divisor parametrization

Positive solutions `1<=m<n` are in bijection with divisors `d` of `N` satisfying

\[
\boxed{
0<d<A<N/d,
\qquad
d\equiv A\pmod B.
}
\]

For each such `d`,

\[
\boxed{
m=\frac{A-d}{B},
\qquad
n=\frac{N/d-A}{B}.
}
\]

Proof: put

\[
Bm-A=-d,
\qquad
Bn+A=N/d.
\]

The displayed formulas follow.  Conversely they reconstruct the factorization equation.  The second congruence is automatic: since `gcd(A,B)=1`, also `gcd(d,B)=1`, and from `d|N` with `N\equiv A^2 (mod B)` and `d\equiv A (mod B)` one gets `N/d\equiv A (mod B)`.  Thus the one divisor congruence is sufficient. ∎

The positive scale is

\[
\lambda=\frac{n-m}{B}
=\frac{m^2+1}{d}\in\mathbf N,
\]

so exactly

\[
(m+i)(n-i)=\lambda(A+iB).
\]

## 3. The unit-neighbor split is a hidden relative-turn theorem

If

\[
A\equiv1\pmod B,
\]

then `d=1` is admissible whenever the resulting `m>=1`.  Set

\[
\boxed{m=\frac{A-1}{B}}.
\]

Then

\[
A-mB=1,
\]

so the primitive rays

\[
(m,1),\qquad(A,B)
\]

are unimodular neighbors.  Their dot product is

\[
\boxed{n=mA+B}.
\]

The relative-turn theorem therefore gives immediately

\[
\boxed{[A+iB]=[m+i][n-i]}.
\]

At raw Gaussian-integer level,

\[
\boxed{(m+i)(n-i)=(m^2+1)(A+iB).}
\]

Thus the apparently separate residual-splitting operation is not a new native primitive.  It is a specialization of the already-proved unimodular relative-turn calculus.

## 4. Local Lehmer-optimality theorem

For fixed primitive residual `(A,B)`, write the split attached to an admissible positive divisor `d` as `(m_d,n_d)`.

If

\[
d_1<d_2,
\]

then directly from the divisor formulas,

\[
m_{d_1}>m_{d_2},
\qquad
n_{d_1}>n_{d_2}.
\]

Since

\[
D\mapsto\frac1{\log_{10}D}
\]

is strictly decreasing for `D>1`, one obtains:

### Theorem 4.1 — smallest admissible divisor minimizes two-factor completion cost

Among all positive two-reciprocal decompositions of the same primitive residual,

\[
\boxed{
\frac1{\log_{10}m_d}+\frac1{\log_{10}n_d}
}
\]

is strictly minimized by the **smallest admissible divisor** `d`.

In particular, whenever the unimodular `d=1` split exists, it is automatically the Lehmer-optimal positive two-reciprocal split of that residual.

This explains why a huge tail denominator can be an optimization consequence rather than an arithmetic pathology: the smallest divisor makes **both** new reciprocal denominators as large as possible.

## 5. The residual behind the 1.48912 formula

Consider the exact native residual

\[
U_{53}U_{107}^{-2}.
\]

Raw Gaussian multiplication gives

\[
(53+i)(107-i)^2=606958+106i,
\]

so the primitive direction is

\[
\boxed{(A,B)=(303479,53)}.
\]

Its norm is

\[
N=303479^2+53^2=92099506250.
\]

The complete divisor theorem finds exactly three positive two-reciprocal splits:

\[
\boxed{(m,n,d)=(5726,1737720807,1)},
\]

\[
\boxed{(5673,612682,2810)},
\]

\[
\boxed{(5618,297807,5725)}.
\]

For the first one,

\[
303479=5726\cdot53+1,
\]

so it is the unimodular split.  The forced second denominator is

\[
\boxed{
1737720807=5726\cdot303479+53.
}
\]

At raw integer level,

\[
\boxed{
(5726+i)(1737720807-i)
=32787077(303479+53i).
}
\]

Therefore

\[
\boxed{
U_{53}U_{107}^{-2}
=U_{5726}U_{1737720807}^{-1}.
}
\]

No inverse tangent is needed to verify this relation.

## 6. Blind support-five precursor census

To test whether the 2010 relation can be reached without inserting Hwang's 1995 five-term precursor, the checker reuses the same declared arithmetic box

\[
D\le7{,}000{,}000,
\qquad
p_{\rm split}\le1300,
\]

and asks for five-term, five-free-prime, rank-four endpoint circuits below the round cutoff

\[
\boxed{\mu<1.70}.
\]

The two searched palette classes are:

1. a full five-prime-support denominator is present;
2. the five-prime palette is generated by the union of two support sets of size at most four.

The smooth universe again contains exactly `17741` denominators.

### Full-support class

- distinct full five-prime palettes: `6364`;
- cost-promising five-tuples: `5773`;
- exact endpoint circuits: `2`.

### Pair-generated class

- five-prime palettes: `311403`;
- cost-promising exact-union five-tuples: `62743`;
- exact endpoint circuits: `3`.

Thus only

\[
\boxed{5}
\]

endpoint circuits occur in these declared classes below the round `1.70` cutoff.

Ordered by Lehmer measure they are:

1. `(114,239,682,12943,740943)`, coefficients `(88,7,-12,24,-44)`, `mu≈1.67305604536`;
2. `(114,239,268,247057,740943)`, coefficients `(76,7,24,-12,-32)`, `mu≈1.67425372721`;
3. `(57,239,757,110443,5055058)`, coefficients `(44,7,-12,12,12)`, `mu≈1.68475902749`;
4. `(53,107,4443,110443,4841182)`, coefficients `(34,15,17,-5,5)`, `mu≈1.69474010260`;
5. `(68,117,1252,110443,4841182)`, coefficients `(34,32,15,-5,5)`, `mu≈1.69992455416`.

The fourth entry is Hwang's 1995 five-term identity, but it was not seeded into the census.

## 7. Systematic residual-surgery scan recovers the 1.48912 identity

For **all five** blindly recovered endpoint circuits, the checker performs the same post-processing:

- every ordered pair of distinct supported denominators `(a,b)`;
- every exponent `1<=k<=4`;
- primitive residual `U_a U_b^{-k}`;
- **every** positive two-reciprocal split from the complete norm-divisor theorem;
- exact endpoint-preserving coefficient substitution;
- Lehmer comparison only afterward.

Exactly

\[
\boxed{3}
\]

strictly improving surgeries occur.

All three come from the single residual

\[
U_{53}U_{107}^{-2}
\]

inside the blindly recovered Hwang 1995 circuit, corresponding exactly to the three admissible divisors `d=1,2810,5725` above.

The three resulting Lehmer measures are

\[
\boxed{1.489121359283479},
\qquad
1.553976397640384,
\qquad
1.564166855592715.
\]

By Theorem 4.1 the `d=1` result is necessarily best among all positive two-reciprocal splits of that residual.

Substituting

\[
U_{53}=U_{107}^{2}U_{5726}U_{1737720807}^{-1}
\]

into the blindly recovered Hwang 1995 endpoint gives

\[
\boxed{
U_{107}^{83}
U_{4443}^{17}
U_{5726}^{34}
U_{110443}^{-5}
U_{4841182}^{5}
U_{1737720807}^{-34}
=\tau.
}
\]

Its exact finite tangent-sheet certificate is

\[
\boxed{\text{endpoint}=(1,1),\quad\text{sheet}=0,\quad\text{crossings}=0.}
\]

Only then does analytic completion yield Nimbran's 2010 six-term `pi/4` identity.

## 8. Prior-art correction and source conflict

Prior-art audit after the native result shows:

- current MathWorld / derivative compilations continue to list Hwang 1997, `mu≈1.51244`, as the best currently known integer-reciprocal Machin formula;
- Amrik Singh Nimbran, *On the Derivation of Machin-Like Arctangent Identities for Computing Pi*, The Mathematics Student 79 (2010), pp.171–186, explicitly reports the `mu≈1.48912` six-term identity and states that it was discovered on 13 June 2009 from the same `[53]-2[107]` relation.

The project does not resolve bibliographic uptake by authority assertion.  It records instead the exact mathematical fact established independently here:

\[
\boxed{
\text{the 1.489121359... integer-reciprocal identity is a valid native endpoint circuit with zero winding.}
}
\]

Therefore any present-day statement that `1.51244` is globally minimal among all known integer-reciprocal identities requires qualification or a narrower catalog scope.

## 9. Structural consequence

The complete local mechanism is now:

\[
\text{endpoint circuit}
\to
\text{shared-term residual}
\to
\text{primitive rational direction }(A,B)
\to
\text{factor }A^2+B^2
\to
\text{all reciprocal two-factor splits}
\to
\text{smallest admissible divisor}
\to
\text{locally optimal Lehmer surgery}.
\]

The extreme denominator in the best split is therefore not arbitrary.  It is the arithmetic image of choosing the smallest admissible norm divisor, and in the unit-neighbor case it is precisely the dot-product label supplied by the existing relative-turn theorem.

## 10. Next frontier

The current native carrier already allows general rational direction pairs, while the completion search has so far ranked mostly integer reciprocal generators `[D+i]`.

The next natural extension is to allow primitive rational-slope generators

\[
[b+ai],\qquad\gcd(a,b)=1,
\]

with analytic completion cost based on `b/a`.  This keeps the native layer entirely integral and brings half-integer/generalized Machin formulas into the same valuation-circuit/Pareto framework without changing the underlying turn algebra.
