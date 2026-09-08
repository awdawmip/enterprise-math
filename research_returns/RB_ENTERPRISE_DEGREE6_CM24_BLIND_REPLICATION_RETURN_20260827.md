# RB Enterprise Degree-6 CM(-24) Blind Replication — Return

Task: `RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION`  
Publication: `TP2-9F1A3C0DEFAED8B6E247`  
Researcher: `EM-RBV2REP-A61F3C`  
Claim: `chatgpt-rbv2rep-degree6-cm24-20260908-1012-a61f3c`  
Phase-A verdict: **`BLIND_INCOMPLETE_EXACT_REDUCTION`**  
Raw freeze: **`BLIND_RECONSTRUCTION_FROZEN`**  
Raw-freeze SHA256: `cebc5192a77c063f08878f5176f2c8c3ae2928fa3c0c1e67c503f4a205eadbd7`

## 1. Scope and blind status

The Phase-A blind firewall remained intact through the raw freeze. I did not inspect the originating explicit degree-6 map, its common base point, target twist constant, exact symbolic replay, or the originating value of \((B_1/\Omega_P)^2\).

This return does **not** claim an explicit reconstruction or a refutation. It freezes a strict exact reduction: the original genus-4 mapping problem is reduced to two exhaustive finite algebraic systems on the genus-1 quotient, with a single load-bearing function-field identity and a forced Hurwitz fiber pattern.

The machine-readable freeze is:

`research_artifacts/rb_enterprise_degree6_cm24_blind_reconstruction_20260908.json`

The deterministic exact replay checker is:

`research_checks/rb_enterprise_degree6_cm24_blind_reconstruction_20260908.py`

## 2. Quotient curve and branch divisor

From the frozen coordinate
\[
t=\frac{w^2}{R+2}
\]
one has
\[
E_0:\quad t^2=R^3-3R,
\qquad
w^2=(R+2)t.
\]
Thus \(D\to E_0\) is the quadratic extension obtained by adjoining a square root of
\[
L=(R+2)t.
\]

Let \(O\) be the point at infinity on \(E_0\). Exact divisors are
\[
\operatorname{div}(R+2)=P_++P_- -2O,
\quad
P_\pm=(-2,\pm i\sqrt2),
\]
and
\[
\operatorname{div}(t)=T_0+T_++T_- -3O,
\quad
T_0=(0,0),\quad T_\pm=(\pm\sqrt3,0).
\]
Therefore the odd support of \(\operatorname{div}(L)\) is exactly
\[
B=\{O,T_0,T_+,T_-,P_+,P_-\}.
\]
These six and only these six points branch in \(D\to E_0\).

## 3. Exact zero divisor of the prescribed differential

Write
\[
\phi=\frac{dR}{w}\left(1+\frac{k}{t}\right)
=\frac{(t+k)\,dR}{wt},
\qquad
k=-i\,3^{1/4}(\sqrt6-2).
\]
The exact square is
\[
k^2=12\sqrt2-10\sqrt3.
\]

Local parameters at the six points of \(B\) show that the apparent poles in \(dR/w\) and \(1+k/t\) cancel: \(\phi\) is holomorphic and nonzero at every point of \(B\).

Away from \(B\), zeros are exactly where \(t=-k\), hence their \(R\)-coordinates satisfy
\[
R^3-3R-k^2=0.
\]
The discriminant of this cubic is
\[
216(-73+30\sqrt6)\ne0,
\]
so it has three distinct roots \(r_1,r_2,r_3\). Consequently the three points
\[
q_i=(r_i,-k)\in E_0
\]
are distinct and unbranched in \(D\to E_0\); each has two lifts to \(D\), and those six lifts are simple zeros of \(\phi\). Since \(D\) has genus \(4\), this already exhausts \(\deg K_D=6\).

Hence any map \(f:D\to E\) with
\[
f^*\eta=c\,\phi,\qquad c\ne0
\]
has ramification divisor equal to precisely those six simple zeros.

## 4. Equivariance and descent to a degree-6 function on \(E_0\)

Let \(\sigma(w)=-w\). Then \(\sigma^*\phi=-\phi\). Therefore
\[
(f\circ\sigma)^*\eta=(-1\circ f)^*\eta=-c\phi.
\]
Two maps from a smooth curve to an elliptic curve with the same pulled-back invariant differential differ by a translation. Thus
\[
f\circ\sigma=-f+Q
\]
for a constant \(Q\in E\). Choosing \(A\) with \(2A=Q\) and replacing \(f\) by \(f-A\) centers the involution:
\[
f\circ\sigma=-f.
\]

For the target \(x\)-coordinate, \(x\circ f\) is therefore \(\sigma\)-invariant. It descends to a function
\[
X:E_0\longrightarrow\mathbf P^1.
\]
Because \(\deg(x\circ f)=2\deg f=12\) and \(\deg(D\to E_0)=2\),
\[
\deg X=6.
\]

This reduces the original genus-4 map reconstruction to a genus-1 degree-6 Hurwitz problem.

## 5. Forced parity and complete ramification pattern

The target is a twist of
\[
Y^2=C\,X(X-1)(X-\lambda),
\]
where
\[
\lambda=35+24\sqrt2-20\sqrt3-14\sqrt6.
\]
Pulling this double cover of \(\mathbf P^1_X\) back along \(X:E_0\to\mathbf P^1\) must reproduce the quadratic extension \(D/E_0\). Therefore, for each of the four special values
\[
0,\;1,\;\lambda,\;\infty,
\]
points in \(B\) occur with odd multiplicity and all other points occur with even multiplicity.

The six points of \(B\) are unramified for \(X\): at those points \(f\) is unramified (because \(\phi\ne0\)), and after centering \(f(B)\subset E[2]\), so the ramification of the target \(x\)-map is exactly canceled by the ramification of \(D\to E_0\).

Let \(m_v\) denote the number of points of \(B\) over a special value \(v\). Then
\[
m_v\equiv0\pmod2,\qquad \sum_v m_v=6.
\]
The non-\(B\) part of the fiber has total multiplicity \(6-m_v\), with every multiplicity even, hence contributes at least \((6-m_v)/2\) to ramification. Summing over the four special values gives at least
\[
\frac{24-6}{2}=9.
\]

The three points \(q_i\) forced by the zero divisor of \(\phi\) contribute at least one ramification unit each. Riemann--Hurwitz for a degree-6 map from a genus-1 curve to \(\mathbf P^1\) gives total ramification exactly
\[
2\deg X=12.
\]
Therefore all lower bounds are equalities. It follows that:

1. every non-\(B\) point over \(0,1,\lambda,\infty\) has multiplicity exactly \(2\);
2. each \(q_i\) is a simple critical point of \(X\);
3. no \(q_i\) maps to a special value;
4. there is no other ramification.

This is the full ramification budget for any admissible reconstruction.

## 6. Single master identity

On \(E_0\), define the derivation
\[
\delta
=
2t\frac{\partial}{\partial R}
+
3(R^2-1)\frac{\partial}{\partial t}.
\]
Because \(t^2=R^3-3R\),
\[
dF=\frac{\delta F}{2t}\,dR
\]
for every \(F\in K(E_0)\).

Write
\[
X=\frac AB,
\qquad
W=(\delta A)B-A(\delta B).
\]
Then
\[
\delta X=\frac{W}{B^2}.
\]

Define
\[
\widetilde Y
=
\frac{w\,\delta X}{t+k}.
\]
The target equation
\[
\widetilde Y^2=C\,X(X-1)(X-\lambda)
\]
is equivalent, after clearing denominators, to the single exact identity
\[
\boxed{
(R+2)t\,W^2
=
C(t+k)^2\,A\,B\,(A-B)(A-\lambda B)
}
\tag{M}
\]
in \(K(E_0)\).

Moreover, whenever (M) holds and \(X\) is nonconstant,
\[
\frac{dX}{\widetilde Y}
=
\frac{t+k}{2tw}\,dR
=
\frac12\,\phi.
\]
Thus no separate differential fitting is required.

Consequently, **(M) plus \(\deg X=6\) and nondegeneracy is necessary and sufficient for the centered equivariant correspondence to an algebraic twist of the prescribed Legendre target.**

The checker exposes `master_residual(A,B,C)` as an exact candidate verifier modulo \(t^2-(R^3-3R)\).

## 7. Exact target \(j\)-invariant

The Legendre modulus factors exactly as
\[
\lambda=
\bigl((\sqrt3-\sqrt2)(2-\sqrt3)\bigr)^2.
\]
Direct substitution into
\[
j(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}
{\lambda^2(1-\lambda)^2}
\]
gives
\[
j=2417472+1707264\sqrt2.
\]
It satisfies
\[
j^2-4834944j+14670139392=0.
\]
Together with the frozen target-class input, this is the principal discriminant \(-24\) CM target.

## 8. Complete finite degree-6 search space

At \(O\),
\[
\operatorname{ord}_O(R)=-2,\qquad \operatorname{ord}_O(t)=-3.
\]

Every degree-6 line bundle on the elliptic curve \(E_0\) is uniquely of the form
\[
\mathcal O(5O+Q).
\]
Therefore there are only two presentation types.

### Case Z: \(Q=O\)

Here the line bundle is \(\mathcal O(6O)\), with basis
\[
L(6O)=
\langle
1,R,t,R^2,Rt,R^3
\rangle.
\]
Take \(A,B\in L(6O)\), remove common base points, impose
\[
\deg(A/B)=6
\]
and the master identity (M).

### Case Q: \(Q=(q,s)\ne O\)

Here
\[
s^2=q^3-3q.
\]
A sixth section beyond \(L(5O)\) can be taken as
\[
h=\frac{t+s}{R-q}.
\]
Multiplying both pencil generators by \(R-q\) sends them into
\[
L(7O)=
\langle
1,R,t,R^2,Rt,R^3,R^2t
\rangle
\]
and forces the single common finite base point
\[
-Q=(q,-s).
\]
Conversely, an \(L(7O)\) pencil with exactly this single common finite base point reduces, after division by \(R-q\), to a degree-6 pencil in \(\mathcal O(5O+Q)\).

Hence Case Z and Case Q exhaust the degree-6 function search. The residual task is a finite system of polynomial equations over the allowed coefficient field, augmented by the exact Hurwitz multiplicity pattern in §5.

This is a strict reduction from unrestricted algebraic-map reconstruction.

## 9. Period normalization

No explicit map was reconstructed in Phase A. Therefore \((B_1/\Omega_P)^2\) was **not derived**, and the originating value was not imported.

This absence is intentional: importing the answer merely to make the return complete would violate the blind protocol.

## 10. Exact replay

A dry replay of

`python research_checks/rb_enterprise_degree6_cm24_blind_reconstruction_20260908.py`

returned:

`status=PASS`

and reproduced:

- raw-freeze SHA256 `cebc5192a77c063f08878f5176f2c8c3ae2928fa3c0c1e67c503f4a205eadbd7`;
- \(k^2=12\sqrt2-10\sqrt3\);
- the exact \(\lambda\) factorization;
- \(j=2417472+1707264\sqrt2\) and its quadratic polynomial;
- cubic discriminant \(216(-73+30\sqrt6)\);
- preservation of the \(E_0\) relation by \(\delta\);
- the \(L(6O)\) and \(L(7O)\) pole-order bases;
- the exact \(\phi/2\) pullback algebra.

## 11. Phase-B comparison status

The raw freeze was completed before any attempt to locate the originating formula. After freeze, targeted repository searches for the originating Ramanujan--Borwein degree-6 / Fermat-24 formula did not surface an authoritative explicit-map artifact on the current default branch search surface.

Accordingly, this return does not fabricate a post-freeze coefficient comparison. The prior-art/dedup and exact originating-formula comparison remain **not completed** in this execution. This does not change the already frozen Phase-A verdict.

## 12. Terminal boundary and next exact action

Primary verdict:

**`BLIND_INCOMPLETE_EXACT_REDUCTION`**

What is proved here is the reduction, not the existence of the desired map.

The next exact action is now narrowly defined:

1. solve Case Z under (M) and the forced four special-fiber patterns;
2. if Case Z is inconsistent, solve Case Q with the one-base-point \(L(7O)\) presentation;
3. only an exact nonconstant degree-6 solution may be promoted to an explicit reconstruction;
4. only exact inconsistency of both exhaustive cases may be promoted to a refutation;
5. after an explicit reconstruction, derive the period ratio independently and then perform the withheld-formula comparison.

No Working Truth, Foundation, theorem-package promotion, or claim of completed degree-6 reconstruction is requested by this return.
