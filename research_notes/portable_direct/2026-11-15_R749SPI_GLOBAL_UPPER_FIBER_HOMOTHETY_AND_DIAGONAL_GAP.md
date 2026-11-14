# R749SPI — exact upper Walsh fiber homothety and an entire positive-gap diagonal

Date: 2026-11-15. Scientific status: AUTHOR_EXACT_NOT_REVIEWED. Domain: auxiliary 16-atom Walsh compatible-source fiber, with frozen scientific input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is independent portable research; the native X6/V29/V39 correspondence remains a separately typed question.

This proof strengthens R749SPH (same Draft PR #2438): all upper-triangle fibers reduce exactly, in a source-law-preserving affine way, to the anti-diagonal \(t+s=1\). Consequently **both** the free and calibrated minimax radii, and their difference, scale along every ray ending at \((1,1)\). From the previously certified R749SPF radius at \((3/5,3/5)\), it produces closed exact formulas for the *whole* upper unit diagonal.

## 1. Definitions and global fiber theorem

Let \(K=\mathbb F_2^4\), \(\chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}\), and
\[
p_{t,s,h,u,v,w,z}(k)
=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
Let \(F(t,s)\) be the set of all such normalized nonnegative laws with \(t,s\) fixed, and let \(\operatorname{TV}(p,q)=\frac12\sum_k|p(k)-q(k)|\). Let \(\rho(t,s)\) denote the minimax radius with any probability-law center and \(\rho^{\rm cal}(t,s)\) the minimax radius with its center in \(F(t,s)\); put \(g=\rho^{\rm cal}-\rho\).

Write \(P_\star=p_{1,1,1,0,0,0,0}\). This is the unique element of \(F(1,1)\): positive mass occupies exactly the \(a=b=+1\) block, uniformly across its four atoms.

**Global upper-fiber homothety theorem (all real parameters):** For every \(0\le t,s\le1\) with \(1\le t+s<2\), set
\[
\nu=t+s-1,\qquad \alpha=2-t-s=1-\nu,\qquad
t'=\frac{1-s}{\alpha},\qquad s'=\frac{1-t}{\alpha}.
\]
Then \(0<\alpha\le1\), \(t',s'\in[0,1]\), \(t'+s'=1\), and
\[
\boxed{F(t,s)=\nu P_\star+\alpha F(t',s').}
\]
The right side means the affine image \(\{\nu P_\star+\alpha p':p'\in F(t',s')\}\), as a set of **complete sixteen-atom probability laws**. For \(t=s=1\), the fiber is the singleton \(F(1,1)=\{P_\star\}\).

## 2. Proof of exact equality of source fibers

Use the retained four-branch BRC carrier coordinates
\[
a=\chi_3,\quad b=\chi_{12},\quad c=\chi_1,\quad d=\chi_4,\qquad
16p_{abcd}=M_{ab}+cU_a+dV_b,
\]
where
\[
M_{ab}=1+ta+sb+hab,\qquad U_a=u+av,\qquad V_b=w+bz.
\]
Source positivity is **equivalent** to the four inequalities
\[
M_{ab}\ge |U_a|+|V_b|\quad(a,b=\pm1).
\]
This formulation retains the composite coefficient \(h\) and each signed source component.

The inclusion \(\nu P_\star+\alpha F(t',s')\subseteq F(t,s)\) follows immediately from positivity and Walsh-linearity: \(t=\nu+\alpha t'\), \(s=\nu+\alpha s'\), and every other allowed Walsh coefficient is a corresponding affine combination.

For the reverse inclusion take arbitrary \(p=p_{t,s,h,u,v,w,z}\in F(t,s)\), and define \(p'=(p-\nu P_\star)/\alpha\). It has total mass one, and its Walsh coefficients are exactly
\[
(t',s',h',u',v',w',z')
=\left(\frac{t-\nu}{\alpha},\frac{s-\nu}{\alpha},
       \frac{h-\nu}{\alpha},\frac{u}{\alpha},
       \frac{v}{\alpha},\frac{w}{\alpha},\frac{z}{\alpha}\right).
\]
Thus it remains only to prove \(p'\ge0\) atomwise. In the three blocks other than \(a=b=+1\), the law \(P_\star\) is zero, so positivity of \(p'\) is immediate.

In the \(++\) block, \(16P_\star=4\). We must prove
\[
M_{++}-4\nu\ge |U_+|+|V_+|.
\]
The \(+-\) and \(-+\) block constraints give
\[
|U_+|\le M_{+-},\qquad |V_+|\le M_{-+}.
\]
The \(--\) block gives \(M_{--}=h-\nu\ge0\). Finally, the exact algebraic identity
\[
M_{++}-4\nu-(M_{+-}+M_{-+})=3(h-\nu)\ge0
\]
yields the required \(++\) inequality. Therefore every atom of \(p'\) is nonnegative, \(p'\in F(t',s')\), and the reverse inclusion follows. The proof covers all real upper-triangle parameters without a finite search or approximation.

## 3. Scaling theorem for both minimax problems

For any nonempty set \(S\) of finite probability laws, define
\[
\rho_\Delta(S)=\inf_{q\in\Delta_{15}}\sup_{p\in S}\operatorname{TV}(p,q).
\]
The probability-center constraint can be replaced by the full affine hyperplane \(H=\{q\in\mathbb R^{16}:\sum_iq_i=1\}\) without changing this radius.

To prove this, take arbitrary signed \(q\in H\), let \(N=\sum_i\max(-q_i,0)\), let \(q^+_i=\max(q_i,0)\), and define \(q'_i=q^+_i/(1+N)\). Then \(q'\in\Delta_{15}\) and, for every probability law \(p\),
\[
\|p-q'\|_1
\le\|p-q^+\|_1+\|q^+-q'\|_1
=\|p-q^+\|_1+N
=\|p-q\|_1.
\]
Hence replacing an affine signed center by a probability center never enlarges any source distance.

For \(0<\alpha\le1\), the map \(T(q)=\nu P_\star+\alpha q\) bijects \(H\) to itself, and
\[
\operatorname{TV}(Tp,Tq)=\alpha\operatorname{TV}(p,q).
\]
It also bijects the calibrated center set \(F(t',s')\) to \(F(t,s)\) by Section 2. Both minimax optimizations therefore obey
\[
\boxed{
\rho(t,s)=\alpha\,\rho(t',s'),\quad
\rho^{\rm cal}(t,s)=\alpha\,\rho^{\rm cal}(t',s'),\quad
g(t,s)=\alpha\,g(t',s')
}
\]
for **every real** \(t,s\in[0,1]\) with \(1\le t+s<2\). At \((1,1)\) all three radii vanish.

**Geometric consequence:** every exact minimax phase boundary in the upper parameter triangle is the affine cone from \((1,1)\) over its intersection with \(t'+s'=1\); any extra zero-gap chamber must likewise descend to a zero-gap point on that anti-diagonal. This reduces the unresolved entire upper-triangle free/calibrated minimax classification to a one-real-parameter problem on the boundary.

## 4. New exact positive-gap formulas on the entire upper diagonal

R749SPF (Draft PR #2428, commit 67f37c7d78ffebff210015b60ba08778ac5b828f) previously proved, on the fixed slice \(s=3/5\), the point
\[
\rho(\tfrac35,\tfrac35)=\frac8{25},\qquad
\rho^{\rm cal}(\tfrac35,\tfrac35)=\frac{18}{55},\qquad
g(\tfrac35,\tfrac35)=\frac2{275}.
\]
For this point \(\alpha=4/5\), and \(t'=s'=1/2\). The scaling theorem therefore gives exact base-point values
\[
\boxed{\rho(\tfrac12,\tfrac12)=\frac25,\quad
       \rho^{\rm cal}(\tfrac12,\tfrac12)=\frac9{22},\quad
       g(\tfrac12,\tfrac12)=\frac1{110}.}
\]

For every real \(r\in[1/2,1]\), the parameter point \((r,r)\) corresponds to boundary point \((1/2,1/2)\) with \(\alpha=2(1-r)\). Consequently
\[
\boxed{
\rho(r,r)=\frac{4(1-r)}5,\qquad
\rho^{\rm cal}(r,r)=\frac{9(1-r)}{11},\qquad
g(r,r)=\frac{1-r}{55}.
}
\]
In particular, \(g(r,r)>0\) for **every** \(1/2\le r<1\), and \(g(1,1)=0\). Thus a whole nontrivial real-parameter diagonal segment has strictly positive calibration penalty, shrinking linearly toward the singleton corner. The point \(r=3/4\) gives \(\rho=1/5,\rho^{\rm cal}=9/44,g=1/220\) exactly.

This diagonal theorem reuses the predecessor's complete exact certificate for one base point, together with the new analytic fiber-homothety and minimax-scaling proofs; it does not infer an infinite family from finite sample agreement.

## 5. Exact sanity check, evidence, remaining research

The standard-library Python Fraction file R749SPI_UPPER_WALSH_FIBER_HOMOTHETY_CHECK.py checks the universal block algebra identity at exact rational inputs, 64 exact forward/inverse sixteen-atom mixture cases, and the diagonal rational identities at four rational points. The companion JSON records PASS and exact fractions. The **load-bearing all-real proof is Sections 2–4**, not those finite cases.

The original source model's sixteen atoms, the composite Walsh interaction, and signed branch coefficients are retained throughout the theorem. The affine mixture statement is a probability-law representation under this auxiliary observer; it does not assert a provenance-preserving native X6 or causal-token observer equivalence.

**Next:** determine the exact one-dimensional free and calibrated radii on the residual anti-diagonal segment \(t'+s'=1,\ 2/5<t'<3/5\) (with its endpoint certificates); then lift the resulting exact phase diagram to the entire upper parameter triangle by the proved homothety. Existing R749SPG already identifies zero penalty on its anti-diagonal outer segments; the midpoint has penalty \(1/110\).
