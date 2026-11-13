# Stage363-B — exact quantitative stability of the near-star two-source budget allocation

Date: 2026-11-02 (Asia/Shanghai). Research2 portable **author-side mathematical result**; no canonical CLAIM, Result or independent Driver acceptance. The task's scientific pins remain GLOBAL_KNOWLEDGE_V1 `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, and its original frozen P000 V4 premise. Current behavioral/control rules were separately checked at global `main@6fe5152374ea27cc2a7247434dfcbd5495c25d8a`, EM `main@9a1ea3ab71469ff6a4f645852d1be9f33b09fdc9`. The current P000 source is V5, ACTIVE_LOCKED; this static Bernoulli/BRC model remains an **external auxiliary observer**, not a native X6/three-dimensional-slice model.

## Exact input, original source-label fidelity, and question

Retain the four independently source-labeled Bernoulli word laws and **all 16 source/word label comparisons**. For `k=0,1,2,3`, `w=(1,3,3,1)`, `m=(61,21,9,9)`, let

\[
 B_k(z)=z^k(1-z)^{3-k},\quad
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},
\]
\[
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
 \quad D_3(a,z)=\frac12\sum_{k=0}^3 w_k|B_k(a)-B_k(z)|,
\]
\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

Let `q*=(x*,y*)` be the unique point with `r0=r1=0` in the central root box; `beta*=b(q*)`. For `s>=0`, let `q_s` on the increasing-x, `r1=0,r0<=0` near-star arc satisfy `b(q_s)=beta*+s`, and put `phi(s)=c(q_s)`. The Stage353-B source established the minimizer of `phi(s)+phi(t)` on the full right arc for budgets through `11/5000`; **this stage gives a new quantitative separation from nonoptimal allocations**, and supplies a short independent rational rectangle certificate for its central part.

## Theorem: explicit two-source allocation stability

For **every real** `0<=E<=1/5000` and `s,t>=0` with `s+t<=E`, these `q_s,q_t` are uniquely defined on the declared arc and

\[
\boxed{\phi(s)+\phi(t)-\phi(0)-\phi(E)
\ \ge\ \frac{352}{27}st+(E-s-t).}\tag{1}
\]

Equality holds **if and only if** `s+t=E` and `st=0`. Thus the unique minimizing allocations, up to swapping, are `(0,E)` and `(E,0)` for `E>0` (and `(0,0)` for `E=0`). For example, with `E=1/5000` and `s=t=1/10000`, the strict cost excess is greater than

\[
\frac{352}{27\cdot 10^8}=\frac{22}{168750000}>0.\tag{2}
\]

The constant `33/1024` in the full two-source objective cancels in this comparison. The theorem is quantitative **within the near-star right `r1=0` subarc**; the unrestricted four-parameter global problem and off-arc competitors remain for further work.

## Proof: full-real root isolation and Bernoulli identities

Work first in the rational rectangle

\[
 R=[229/1000,233/1000]\times[27/50,14/25].
\]

Here `B_1'(x)=(1-x)(1-3x)>0`, `B_1'(y)<0`; `r1=0` is equivalently

\[
4B_1(x)+B_1(y)=21/32.\tag{3}
\]

On `x in [231/1000,29/125]`, the expressions `r1(x,27/50)>0` and `r1(x,14/25)<0`; hence (3) has a unique smooth increasing graph `y=Y(x)` in R. Exact rational endpoint brackets are:

* At `x=231/1000`, `r1(x,555/1000)>0>r1(x,5555/10000)` and `r0(x,5555/10000)>0`.
* At `x=2311/10000`, `r1(x,55555/100000)>0>r1(x,55556/100000)` and `r0(x,55555/100000)<0`.
* At `x=29/125`, `r1(x,558/1000)>0>r1(x,559/1000)`.

As `r0_x=-12(1-x)^2/5<0`, `r0_y=-3(1-y)^2/5<0`, and `Y'(x)>0`, the derivative `d r0(x,Y(x))/dx<0`. Hence precisely one junction `q*` occurs, with `231/1000<x*<2311/10000`; to its right `r0<0`. Throughout R, exact Bernstein endpoint monotonicity gives `r2>0`, `r3<0`, and `sum_k w_k r_k=0`. On this `r1=0,r0<=0` arc,

\[
 b(x,Y(x))=\frac{15}{16}r_2(x,Y(x)).\tag{4}
\]

The original 16 labels keep the signs `(-,+,+,+),(-,-,+,+),(+,+,-,-),(-,-,+,+)` for the four audit-port blocks `(1/4,x),(3/4,x),(1/4,y),(3/4,y)`. Each of the four Bernstein basis functions is monotone on either coordinate interval, and their anchor-endpoint differences retain these exact signs. Expanding the full four-port expression, without collapsing any provenance, yields

\[
 c_x=-\frac{3(1-x)(63-61x)}{256},\qquad c_y=\frac{3y(1-y)}{64}.\tag{5}
\]

## Proof: uniform second-order certificate

Implicitly differentiating (3) gives

\[
 Y' = \frac{4(1-x)(1-3x)}{(1-y)(3y-1)},\qquad
 Y''=-\frac{4(4-6x)+(4-6y)(Y')^2}{(1-y)(3y-1)}.\tag{6}
\]

Here and below `y=Y(x)`. Exact rational endpoint bounds throughout **all R** establish

\[
3<Y'<7/2,\quad Y''<-53.\tag{7}
\]

For `B(x)=b(x,Y(x))` and `C(x)=c(x,Y(x))`, the chain rule and (4)–(6) yield

\[
 B'=\frac3{16}[4x(2-3x)+y(2-3y)Y'],
\]
\[
 B''=\frac3{16}[4(2-6x)+(2-6y)(Y')^2+y(2-3y)Y''],\tag{8}
\]
\[
 C'=c_x+c_yY',\quad
 C''=\frac{3(124-122x)}{256}+\frac{3(1-2y)}{64}(Y')^2+c_yY''.\tag{9}
\]

The following **strict, universal rational** bounds hold throughout R where these implicit derivatives are evaluated:

\[
 \boxed{9/40<B'<3/8,\quad C'<-3/8,\quad B''<-3,\quad C''<7/6.}\tag{10}
\]

For complete reproducibility, the checker establishes these inequalities using only the rectangle corners:

* `Y'` decreases with `x` and with `y` on R, so its minimum/maximum are at `(233/1000,14/25)` / `(229/1000,27/50)`; both endpoints satisfy (7).
* The denominator `(1-y)(3y-1)<3/10`, and the positive numerator of `-Y''` is greater than `4(4-6(233/1000))+(4-6(14/25))*9`, giving `Y''<-53`.
* `x(2-3x)` is increasing on the x interval and `y(2-3y)` is decreasing on the y interval. Their rational corners yield both `B'` bounds and `B''<-3` from (7).
* `c_x<-43/100`, `0<c_y<3/256`, and `Y'<7/2` give `C'<-3/8`. For `y>1/2`, the last two terms of `C''` are negative; the first term is `<7/6`.

Consequently, with `N=C''B'-C'B''`, positivity of `B'` and the strict bounds (10) give

\[
 N<\frac76\frac38-\frac38\cdot3=-\frac{11}{16}.\tag{11}
\]

Inverting the strictly increasing `B` and writing `\phi(s)=C(B^{-1}(\beta_*+s))` yields on the smooth pre-cusp arc

\[
\boxed{\phi'(s)=C'/B'<-1,\qquad
 \phi''(s)=N/(B')^3<-\frac{352}{27}.}\tag{12}
\]

Finally, `x*=x_star<2311/10000`, so between `x*` and `29/125`, using `B'>9/40`,

\[
 B(29/125)-\beta_* > \frac9{40}\left(\frac{29}{125}-\frac{2311}{10000}\right)
 =\frac{81}{400000}>\frac1{5000}.\tag{13}
\]

Thus every `0<=s<=1/5000` lies inside the certified arc; its ordinate stays below `559/1000` and below the later source-tag cusp.

## Proof: finite-distance (not merely infinitesimal) two-source gap

Write `u=s+t`. Because `phi''<-m` with `m=352/27`, the symmetric function `h(v)=phi(v)+phi(u-v)` satisfies `h''(v)<-2m` for `0<v<u`. Subtracting `m v(u-v)` gives a strictly concave function with equal endpoint values; therefore

\[
 \phi(s)+\phi(t)-\phi(0)-\phi(s+t)\ge m st,
\]

strict for `s,t>0`. Also `phi'<-1` gives `phi(s+t)-phi(E)>=E-s-t`, strict if `s+t<E`. Adding proves (1) and its **exact equality classification**.

The result quantitatively excludes arbitrary *finite* interior-interior allocations on this subarc, not just stationary points. It strengthens the earlier qualitative restricted-arc minimization with a certified cost margin and a budget-slack penalty. It does not independently establish unrestricted global optimality or a near-arc off-branch exclusion certificate.

## Validation, BRC usage, and next discrimination

`REPRO_STAGE363B.py` is a standalone Python `Fraction`/SymPy verifier. It re-expands all 16 labeled audit terms, checks rational endpoint signs and the implicit polynomial identities, and verifies every constant in (7)–(13). It executed twice with byte-identical stdout, culminating in `STAGE363B_NEAR_STAR_QUANTITATIVE_SPLIT_RIGIDITY_EXACT_PASS`. The real-parameter quantifiers and strong-concavity inequality are justified by the analytic arguments above, with the script checking their exact rational premises.

BRC resolution: `COMPOSE_APPLIED` to the existing provenance-preserving 16-label Bernoulli total-variation and four-port observer, with unchanged labels, coefficients and declared two-source additive budget; `REUSE_EXECUTED` for direct exact symbolic/ratio checks. No numerical global search, positive-mass collapse, or source merging enters the certificate. The observer's future-operation scope is the two-source additive-error/cost comparison on this fixed auxiliary family.

**Next Stage364-B:** distinguish the original unrestricted four-parameter problem from the right-arc allocation: construct a rigorous equal-error off-arc projection/dominance certificate near the cusp/near-star pair, or find an exact rational off-arc pair beating the Stage353-B cost at a precisely bounded budget. Quantitative slack (1) can constrain interior allocation competitors. Preserve P000 native X6, genuine three-dimensional slice, triadic closure, independently typed time and registered six-field Cell address as separate bridge obligations. Formal owner status remains unconfirmed because the native owner list returned `CONTROL_QUOTA`, and the current connector reports research authority false.
