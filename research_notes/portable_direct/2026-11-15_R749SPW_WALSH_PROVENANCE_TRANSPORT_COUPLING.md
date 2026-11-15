# R749SPW — Constant provenance-transport separation despite identical reachable optimal Walsh centers

**2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED.** Independent portable TASK_RESEARCH continuation of R749SPR/SPU/SPV. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Auxiliary signed 16-atom Walsh model only; no shared native X6 claim. Researcher-ID: EM-DIRECT-43ACF9; own Activity RA-DBAE327C0325942911267FF9 (registered Source); publication of an Activity science checkpoint is tracked separately.

## 1. Precise objects and shared dependencies

Use the R749SPR full calibrated optimal-center polytope K at (t,s)=(1/10,1/2), with the eight facets copied in the executable certificate. A point X=(H,U,V) in K determines the signed 16-atom probability law

\[
q_X=p(1/10,1/2,H/10,U/10,V/10,0,0),
\quad
p(t,s,h,u,v,w,z)[i]=
\frac{1+t\chi_3(i)+s\chi_{12}(i)+h\chi_{15}(i)+u\chi_1(i)+v\chi_2(i)+w\chi_4(i)+z\chi_8(i)}{16}.
\]

The masks satisfy \(\chi_m(i)=(-1)^{\operatorname{popcount}(i\mathbin{\&}m)}\). For rational centers with averaged integer source totals, write \(q_{X/n}\). R749SPU proves that the 25 forced types F, defined as all letters participating in any uniquely represented unordered two-letter sum from P=K∩Z³, have exactly two 26-letter minimum universal extensions:

\[
A_0=F\cup\{o=(0,0,0)\},\qquad A_1=F\cup\{b=(-1,0,0)\}.
\]

For n≥2, both alphabets have the same set of reachable centers \(\{q_{X/n}:X\in nK\cap\mathbb Z^3\}\), all attaining calibrated minimax TV radius 9/20. This support/optimality statement inherits R749SPR/SPU, whose author proofs await independent review.

The present theorem studies a **specified probability experiment**, uniform over unordered length-n source multisets, i.e. uniform weak compositions of n into the 26 labeled source-type counts. This is not the experiment of independently sampling n uniformly chosen source letters, and it is not a native P000 Cell dynamics law.

## 2. All-n exact provenance coupling and coefficient identity

Identify each 25-type forced letter by the same label in both alphabets; identify their final optional letters by their slot, **not** by their unequal coordinates. For every source-count vector

\[
(c_f:f\in F;\ k)\in\mathbb Z_{\ge0}^{26},\qquad \sum_{f\in F}c_f+k=n,
\]

define the two observed sums:

\[
X_0=\sum_{f\in F}c_ff,\quad
X_1=\sum_{f\in F}c_ff-k e_H,\quad e_H=(1,0,0).
\]

Thus, pointwise and for every integer n≥1,

\[
\boxed{X_0-X_1=k e_H,\quad U_0=U_1,\quad V_0=V_1.}
\]

All paired multiset states are distinct labeled sources even if their averaged center readouts collide. This gives a monotone coupling in H without identifying source identities.

Let \(M_F(n,X)\) count weak compositions using exactly the 25 forced types, and \(M_j(n,X)\) count the two full-alphabet source fibers. With \(M_F(0,0)=1\), the exact **all-level convolution and finite-difference identities** are

\[
\boxed{M_0(n,X)=\sum_{k=0}^n M_F(n-k,X),\qquad
M_1(n,X)=\sum_{k=0}^n M_F(n-k,X+k e_H).}
\]

Equivalently,

\[
M_0(n,X)-M_0(n-1,X)
=
M_1(n,X)-M_1(n-1,X+e_H)
=M_F(n,X).
\]

The corresponding rational formal Laurent generating functions, with \(\mathbf x^a=x^{a_H}y^{a_U}z^{a_V}\), are

\[
G_0(\lambda,\mathbf x)=
\frac{1}{(1-\lambda)\prod_{f\in F}(1-\lambda\mathbf x^f)},\qquad
G_1(\lambda,\mathbf x)=
\frac{1}{(1-\lambda x^{-1})\prod_{f\in F}(1-\lambda\mathbf x^f)}.
\]

These identities follow by fixing the number k of the optional type, so they require no numerical or analytic continuation.

## 3. Exact distribution of the lost optional-slot count

Uniformity over all \(\binom{n+25}{25}\) weak compositions implies

\[
\boxed{\Pr(K_n=k)=\frac{\binom{n-k+24}{24}}{\binom{n+25}{25}},\quad 0\le k\le n.}
\]

The tail is obtained by subtracting r copies from the optional slot:

\[
\boxed{\Pr(K_n\ge r)=\frac{\binom{n-r+25}{25}}{\binom{n+25}{25}},\quad 0\le r\le n.}
\]

By the standard stars-and-bars/factorial-moment identities (or direct summation),

\[
\boxed{\mathbb E K_n=\frac n{26},\qquad
\operatorname{Var}(K_n)=\frac{25n(n+26)}{26^2\cdot27}.}
\]

For each real \(0\le a<1\), taking \(r=\lceil an\rceil\) in the exact tail shows

\[
\Pr(K_n/n\ge a)\longrightarrow (1-a)^{25}.
\]

Consequently \(K_n/n\Rightarrow\mathrm{Beta}(1,25)\), with a nondegenerate limit. This convergence concerns the declared uniform-*multiset* ensemble.

## 4. Exact transport gap for both signed-coordinate and Walsh-probability readouts

Equip the summed-coordinate space with the ordinary \(\ell^1\) metric and the space of 16-atom probability laws with the metric \(\operatorname{TV}(q,q')=\frac12\sum_i|q(i)-q'(i)|\). Let \(\mu_{j,n}\) denote the probability law of the corresponding readout under uniform source multisets.

By the common-count coupling, the coordinate distance between each pair equals \(K_n\). Therefore

\[
W_1^{\ell^1}(\mathcal L(X_0),\mathcal L(X_1))\le \mathbb E K_n=n/26.
\]

The function \(X\mapsto H\) is 1-Lipschitz for \(\ell^1\), and its expectation difference equals \(n/26\). The Kantorovich dual lower bound matches the coupling. Thus

\[
\boxed{W_1^{\ell^1}(\mathcal L(X_0),\mathcal L(X_1))=n/26.}
\]

For the **normalized optimal Walsh centers**, the only changing signed moment is \(h\):

\[
q_{X_0/n}-q_{X_1/n}
=\frac{K_n}{160n}\chi_{15},\qquad
\operatorname{TV}(q_{X_0/n},q_{X_1/n})=\frac{K_n}{20n}.
\]

This coupling gives \(W_1^{\operatorname{TV}}(\mu_{0,n},\mu_{1,n})\le 1/520\). The bounded Walsh-moment functional \(L(q)=\frac12\sum_i\chi_{15}(i)q(i)=h/2\) is 1-Lipschitz under atom TV. Its expectation difference is exactly \(1/520\), providing the matching lower bound:

\[
\boxed{W_1^{\operatorname{TV}}(\mu_{0,n},\mu_{1,n})=\frac1{520}
\quad\text{for every integer }n\ge1.}
\]

Moreover, all centers have \(H/n\in[-2,2]\), so \(h\in[-1/5,1/5]\). Since \(\mathbb E h_0-\mathbb E h_1=1/260\), the elementary bounded-test inequality also yields

\[
\boxed{\operatorname{TV}(\mu_{0,n},\mu_{1,n})\ge\frac1{104}\quad(n\ge1),}
\]

where the outer TV measures the **distributions of center readouts**, not the TV risk of a center against a source. Thus the two equally universal 26-type alphabets support the same optimal centers for n≥2 yet induce observably different sampling distributions at every resolution.

## 5. Sampling-law control experiment

If instead the original source sequence is sampled by n independent draws uniformly among the 26 types, the same slotwise coupling still gives \(X_0-X_1=K_n e_H\), but now \(K_n\sim\mathrm{Binomial}(n,1/26)\) and \(K_n/n\to1/26\) in probability. Exact expectation and the optimal-center transport identity \(W_1^{\operatorname{TV}}=1/520\) are unchanged; the fluctuation law is different. This distinguishes an actual provenance-ensemble assumption from a mathematical property of the Walsh center itself.

## 6. Exact reproduction, scope and next discriminating problem

Run the dependency-free verifier:

\`\`\`text
node R749SPW_WALSH_PROVENANCE_TRANSPORT_CERT.js > R749SPW_WALSH_PROVENANCE_TRANSPORT_RESULTS.json
\`\`\`

The verifier reconstructs the 33-point first-grid K from the eight integer facets, derives F using **all 561 unordered pairs**, checks the two optional letters, enumerates all 26-source unordered multisets for n=1,…,5 and verifies both fiber coefficient recurrences against independently enumerated forced-source fibers. It checks exact stars-and-bars count/moments and signed Walsh-atom difference identities with integer arithmetic. The five-level PASS covers 26+351+3276+23751+142506 = **169,910 paired multiset states** (339,820 underlying alphabet-specific multisets). The all-n theorems are proved combinatorially above; finite tests are an independent consistency certificate, not an extrapolation.

The proof uses the original signed Walsh probability law and integer source multiplicities. It is not a proof of native Heartbeat X6 Cell/Port/Link dynamics, a P000 transformation, or a formal Result/Review admission.

**Next question.** Locate the exact sign chambers and eventual extremal ordering of \(M_0(n,X)-M_1(n,X)\) and \(\max_X M_0(n,X)-\max_X M_1(n,X)\). The rational generating-function pair supplies a finite-difference entry; the transport coupling alone does not decide maximum-fiber order.