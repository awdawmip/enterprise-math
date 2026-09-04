# Free Research — Fourth-Order Stopped-Transposition Chamber Audit

Status: `FREE_RESEARCH_FRONTIER / EXACT EIGHT-CHAMBER DECOMPOSITION / NO NEW OBSERVABLE TYPE / ALL MIXED CUTOFF TERMS EXPLICIT / COEFFICIENT-SAFE INTEGRATION TARGET / DECAY OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_CENTERED_FOURTH_ORDER_TRANSPOSITION_GATE_V20_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Setup

Fix a state `n`, a suffix action `c`, and write

\[
g(x):=\delta_cf(x)=f(x)+f(q_cx).
\]

For ordered actions `(a,b)`, let

\[
v_{ab}:=\mathbf1_{ab\le n},
\qquad s_{ab}:=1-v_{ab},
\]

and define the stopped fold

\[
\Phi(a,b)=
\begin{cases}
q_{ab}(n),&v_{ab}=1,\\
q_a(n),&s_{ab}=1.
\end{cases}
\]

The pair field is

\[
F(a,b)=g(\Phi(a,b)).
\]

Its pair-valued `S_3` Dirichlet form is

\[
\mathcal D^{(2)}(F)
=\frac16\mathbb E_{a,b,d}
\left[
|F(a,b)-F(b,a)|^2
+|F(a,b)-F(d,b)|^2
+|F(a,b)-F(a,d)|^2
\right].
\tag{1.1}
\]

All expectations use the product prime-winding probability at the parent state.

---

## 2. Swap chamber

Because `ab=ba`, the valid endpoints coincide.  Therefore

\[
\boxed{
|F(a,b)-F(b,a)|^2
=s_{ab}|g(q_a n)-g(q_b n)|^2.
}
\tag{2.1}
\]

The swap channel vanishes identically on the valid chamber and is exactly the stopped first-label relation field on the complement.

---

## 3. First-slot replacement chambers

For the difference

\[
F(a,b)-F(d,b),
\]

there are four disjoint status chambers:

\[
\boxed{
\begin{aligned}
|F(a,b)-F(d,b)|^2={}&
 v_{ab}v_{db}
 |g(q_{ab}n)-g(q_{db}n)|^2\\
&+s_{ab}s_{db}
 |g(q_an)-g(q_dn)|^2\\
&+v_{ab}s_{db}
 |g(q_{ab}n)-g(q_dn)|^2\\
&+s_{ab}v_{db}
 |g(q_an)-g(q_{db}n)|^2.
\end{aligned}}
\tag{3.1}
\]

The four terms are respectively:

1. valid/valid common-second-slot curvature;
2. stopped/stopped first-label relation;
3. valid/stopped moving-cutoff boundary relation;
4. stopped/valid moving-cutoff boundary relation.

No cross term appears because the four indicators are disjoint and sum to one.

---

## 4. Second-slot replacement chambers

For

\[
F(a,b)-F(a,d),
\]

the both-stopped endpoints are both `q_a(n)`, so that chamber vanishes.  The remaining three positive chambers are

\[
\boxed{
\begin{aligned}
|F(a,b)-F(a,d)|^2={}&
 v_{ab}v_{ad}
 |g(q_{ab}n)-g(q_{ad}n)|^2\\
&+v_{ab}s_{ad}
 |g(q_{ab}n)-g(q_an)|^2\\
&+s_{ab}v_{ad}
 |g(q_an)-g(q_{ad}n)|^2.
\end{aligned}}
\tag{4.1}
\]

These are:

1. valid/valid common-first-slot curvature;
2. valid/stopped boundary edge;
3. stopped/valid boundary edge.

Together with (2.1) and (3.1), this yields exactly eight nonzero positive chamber terms.

---

## 5. Signless suffix splitting

For any two endpoints `x,y`,

\[
\boxed{
|g(x)-g(y)|^2
\le
2|f(x)-f(y)|^2
+2|f(q_cx)-f(q_cy)|^2.
}
\tag{5.1}
\]

Thus every one of the eight chambers splits into:

1. an ordinary ordered relation field between retained fold endpoints;
2. its deterministic common-suffix transport by `c`.

The first part is already present in the V14/V15 relation-state carrier.  The second part is the rectangular common-suffix transport, whose weighted energy is nonexpansive before the moving-cutoff recanonicalization step.

---

## 6. Exact scale locations

Every prime-power action is at least `2`.  Therefore:

- a stopped endpoint `q_a(n)` lies at most at `n/2`;
- a valid endpoint `q_(ab)(n)` lies at most at `n/4`;
- after the additional suffix `c`, the corresponding endpoints lie at most at `n/4` and `n/8`.

Hence the fourth-order packet has no literal parent-scale value channel.  Its obstruction is not failure to descend in arithmetic size; it is preservation of relation energy under nonuniform recanonicalization.

The mixed chambers in (3.1) and (4.1) are precisely where valid and stopped histories descend by different amounts.  They are the coefficient-safe location of the V14 moving-cutoff tail terms.

---

## 7. Coefficient-safe aggregate form

Let

\[
\mathcal R_{\rm fold}(g;n)
\]

denote the sum of the eight chamber relation energies in (2.1), (3.1), and (4.1), with the common factor `1/6` and product action probabilities.

Then equality holds:

\[
\boxed{
\mathcal D_n^{(2)}(F)=
\mathcal R_{\rm fold}(g;n).
}
\tag{7.1}
\]

Using (5.1) and averaging over the suffix action,

\[
\boxed{
\mathfrak D_4(f;n)
\le
2\mathfrak R_3(f;n)
+2\mathfrak T_4(f;n),
}
\tag{7.2}
\]

where:

- `mathfrak R_3` is the eight-chamber stopped-fold relation packet for the base field `f`;
- `mathfrak T_4` is its common-suffix transported copy.

Both are positive.  No product label is recoalesced before its relation difference is formed.

---

## 8. What is now closed

The centered fourth-order gate introduces no new primitive observable.  It is exactly a finite assembly of:

1. stopped first-label relations;
2. valid common-suffix curvature;
3. valid/stopped moving-cutoff boundary relations;
4. one further deterministic common-suffix transport.

The remaining proof is therefore not one of representation or carrier discovery.  It is a coefficient audit across scale recanonicalization:

\[
\boxed{
\text{show that the eight chamber masses, after V14 tail-potential absorption, yield a strict or summably defective recurrence.}
}
\]

The both-stopped second-slot chamber vanishes exactly, and the valid swap chamber vanishes exactly; these two structural zeros should be retained in any optimized coefficient calculation.

No native decay, quantitative prime remainder, Working Truth, Foundation status, or RH-scale conclusion is asserted.
