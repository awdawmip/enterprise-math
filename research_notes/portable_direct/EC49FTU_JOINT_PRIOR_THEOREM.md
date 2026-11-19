# EC49FTU — Jointly varied continuous-kernel and clipping-atom sharp stochastic-order transition

**Status:** AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.
**Date:** 2026-11-19. **Route:** independent portable research, not a native Task CLAIM.

## Provenance and scope

Frozen BRC16943 scientific input: \`awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. The native 228-observer/141-profile Bellman optimum is inherited, author-proved and **not independently reviewed** (EC49FTH PR #2774, commit \`999bf1069403306b3813e0e390dae4435d7b4b8c\`). Reuse the inherited high-gap coordinate map of EC49FTS PR #2797, the mixed TP2/top-atom criterion of EC49FTR PR #2795, and the earlier **unchanged** continuous-kernel sharp threshold of EC49FTT PR #2799, \`d3cdbff82125e422b7de00eb26ad89689fe1a4b7\`.

This is a new **external price-prior** theorem conditional on that native Bellman result. It changes the normalized continuous optimizer law and the clipped top-atom mass simultaneously; unlike EC49FTT, it does not merely retain an identical continuous fiber. No new native heartbeat dynamics, six-axis geometry or Bellman enumeration is asserted. The continuum price prior is an effective probabilistic observer, not a new native spatial coordinate.

## 1. Inherited exact high-gap coordinate map

Price box \`a in [3/4,49/64]\`, \`b in [7/16,57/128]\`. Write
\[
I=(1469/64,187/8),\quad m\in I,\quad t=187/8-m\in(0,27/64),\quad U=3/4,
\]
\[
L(m)=(8m+173)/480,\quad
a(m,z)=(47-m)/945+(44/45)z,\quad
b(m,z)=1/27-m/54+(10/9)z,\quad L(m)<z<U.
\]
The clipping boundary is
\[
a_c(b)=(77+6b)/105,\qquad b_m=(47-m)/54,\qquad
\delta(b)=49/64-a_c(b)>0,\qquad m(b)=47-54b.
\]
For a strictly positive joint external-price density \`h(a,b)\` (unnormalized), the inherited change of variables yields
\[
K_h(m,z)=(16/945)h(a(m,z),b(m,z)),\quad
A_h(m)=\int_{L(m)}^U K_h(m,z)\,dz,
\]
\[
B_h(m)=(1/54)\int_{a_c(b_m)}^{49/64}h(a,b_m)\,da.
\]
Here \`M\` is the inherited optimized exchange-cost difference and \`Z\` its optimizing q140 discount. The conditional law \`Z|M=m\` consists of the continuous kernel \`K_h\` with weight \`A_h/(A_h+B_h)\` and an atom at \`Z=U\` with weight \`B_h/(A_h+B_h)\`. The common prior normalization cancels.

## 2. A genuinely changed strictly TP2 continuous kernel

Define
\[
h_1(a,b)=(1+a+b)(1+a-a_c(b)).
\]
Both factors are positive on the price box. Indeed
\[
1+a-a_c(b)\ge 6661/6720>0.
\]
On a nonclipped fiber,
\[
a(m,z)-a_c(b(m,z))=8(4z-3)/35,
\quad 1+a-a_c(b)=(11+32z)/35,
\]
and therefore
\[
\boxed{K_1(m,z)=\frac{16}{945}[1+a(m,z)+b(m,z)]\frac{11+32z}{35}.}
\]
The ratio \`K_1/K_0=(11+32z)/35\` strictly depends on \`z\`, so the normalized continuous conditional distribution is genuinely different from EC49FTT's.

Since the new \`z\` factor is positive and independent of \`m\`,
\[
\partial_m\partial_z \log K_1 =
\frac{(37/1890)(94/45)}
     {[1+a(m,z)+b(m,z)]^2}>0.
\]
Consequently \`K_1\` is strictly TP2 on common fiber rectangles. Together with the increasing lower endpoint \`L(m)\`, its **normalized continuous conditional law** is stochastically increasing with \`m\`: the likelihood ratio on shared support is increasing in \`z\`, and removal of an initial interval only shifts the smaller-\`z\` mass to the right.

Direct exact integration, with \`t=187/8-m\`, yields
\[
\boxed{A_1(t)=\frac{t\,Q(t)}{421954312500},
\qquad Q(t)=3296t^2-1733760t+261457875,}
\]
\[
\boxed{B_1(t)=
\frac{(64t-441)(109568t^2-196996464t-24224009607)}
{35838544379904000}.}
\]
For \`0<t<27/64\` both masses are positive. Let \`r_1(m)=B_1(t)/A_1(t)\`.

## 3. A smooth independent clipping-atom parameter

Let
\[
J=\int_0^1e^{-1/s^2}ds>0,\quad
\psi(s)=\begin{cases}0&s\le0,\\e^{-1/s^2}/J&s>0.\end{cases}
\quad\int_0^1\psi(s)ds=1.
\]
For each \`\lambda\ge0\`, define
\[
t(b)=187/8-m(b),\qquad
f_\lambda(b)=\frac{54\lambda\,t(b)\,A_1(t(b))}{\delta(b)},
\]
\[
\boxed{h_{1,\lambda}(a,b)=h_1(a,b)+
f_\lambda(b)\psi\left(\frac{a-a_c(b)}{\delta(b)}\right).}
\]
This is a strictly positive \`C^\infty\` joint density after ordinary normalization. The bump is flat and identically zero for \`a\le a_c(b)\`, and \`t(b)\ge0\` on the price box. It changes no nonclipped density but adds precisely \`\lambda t A_1(t)\` to the clipped mass:
\[
K_{1,\lambda}=K_1,\qquad A_{1,\lambda}=A_1,\qquad
B_{1,\lambda}=B_1+\lambda t A_1,
\]
\[
\boxed{r_{1,\lambda}(m)=r_1(m)+\lambda(187/8-m).}
\]
Thus the passage from the prior EC49FTT baseline to \`h_1\` **changes both** the continuous conditional distribution and the atom, while \`\lambda\` independently adjusts the atom within this newly changed family.

## 4. Exact sharp phase transition

**Theorem.** For the explicit \`h_{1,\lambda}\` family, all \`m<m'\` in \`I=(1469/64,187/8)\` satisfy
\[
Z\mid M=m\preceq_{\mathrm{st}}Z\mid M=m'
\]
**if and only if**
\[
\boxed{0\le\lambda\le\Lambda_1,\qquad
\Lambda_1=\frac{3011497578173713436500}{1113761136900667642209}
\simeq2.703898958581007.}
\]

**Atom criterion.** The full law is the stochastically increasing normalized continuous law mixed with a top-endpoint atom \`\delta_U\` of weight \`p(m)=r(m)/(1+r(m))\`. A nondecreasing \`r(m)\` is sufficient by monotone coupling. It is also necessary: the probability of the upper event \`{Z=U}\` must be nondecreasing under first-order stochastic increase. Therefore full order is equivalent to nondecreasing \`r\` here.

**Sharp derivative.** Differentiate the rational function \`r_1=B_1/A_1\` with \`t=187/8-m\`. Its \`m\` derivative has exact left endpoint value
\[
\lim_{m\downarrow1469/64}r_1'(m)
=\Lambda_1.
\]
The second derivative has the exact identity
\[
r_1''(m)=-\frac{875P(t)}{589824\,t^3Q(t)^3},
\]
where
\[
\begin{aligned}
P(t)={}&1546333976526848t^6
+1044832421089787904t^5\\
&-928647468742788716544t^4
+141015426401077236933120t^3\\
&-1967509591224525617119200t^2\\
&+230598262640418705763920000t
-11591710449861527147026265625.
\end{aligned}
\]
The discriminant of \`Q\` is \`-441136886400<0\`, and its leading coefficient is positive, so \`Q(t)>0\`. For \`0<t<27/64<1\`, discard negative nonconstant monomials of \`P\` and bound positive \`t^k\` by 1. The sum of positive coefficients is exactly
\[
230739279113198538067167872
<11591710449861527147026265625,
\]
the magnitude of the negative constant coefficient. Thus \`P(t)<0\` and \`r_1''(m)>0\` throughout the interval. Hence \`r_1'(m)\` is strictly increasing, its infimum is \`\Lambda_1\`, and
\[
r_{1,\lambda}'(m)=r_1'(m)-\lambda.
\]
It is nonnegative everywhere precisely for \`0\le\lambda\le\Lambda_1\`. Above that threshold it is negative on an interior left neighborhood. The atom criterion concludes the theorem, including the endpoint \`\lambda=\Lambda_1\`.

## 5. Exact rational violation beyond the threshold

Choose \`\lambda=3\`, \`p=2939/128=1469/64+1/128\`, and
\`q=735/32=1469/64+1/64\`, with \`p<q\` both interior. The exact atom ratios satisfy
\[
r_{1,3}(p)-r_{1,3}(q)
=\frac{1922825655930000265002959}{1768321928463564335718115584}>0.
\]
Consequently
\[
\boxed{\Pr(Z=U\mid M=p)-\Pr(Z=U\mid M=q)
=\frac{179422707606140184727956110208}
{1841092654109728505799184921900171}>0.}
\]
The top-atom probability *decreases* as \`m\` increases, contradicting stochastic increase. No floating point or finite sampling is needed for the violation.

## 6. Quantified difference from EC49FTT

For the unchanged continuous-kernel family EC49FTT, the sharp threshold was
\[
\Lambda_0=\frac{171167905504400}{63545784776721}.
\]
Changing the continuous conditional law and baseline atom together shifts it by the **exact positive quantity**
\[
\boxed{\Lambda_1-\Lambda_0=
\frac{998375751380971275021576456100}
{97084808639459423130625334129241}>0.}
\]
This measures their combined change; attribution to either factor alone is not claimed.

## 7. Verification, exact limits, and next research

The companion Python standard-library \`Fraction\` verifier independently evaluates the new conditional and clipped integrals, checks the second-derivative rational polynomial identity, global positivity certificate, 107 exact interior points, four strict TP2 determinants, and the explicit atom-probability reversal. Its finite tests are regression checks; the all-real theorem follows from the analytic proof.

- **New author result:** analytic sharp external-price-prior order threshold and exact counterexample conditional on the inherited Bellman mapping.
- **Parent status:** the original native 228-observer optimum and branch remain AUTHOR_PROVED/NOT_REVIEWED, with no new native Bellman execution.
- **Control:** independent portable scientific artifact only. No new Researcher ID, formal Task CLAIM, Result, Review or Source Activity asserted by this file.
- **Next mathematical unit:** for \`0\le\theta\le1\`, let \`h_\theta=(1+a+b)(1+\theta(a-a_c(b)))\` and add normalized smooth clipping bumps. Determine whether the exact threshold function \`\Lambda(\theta)=\inf_I\partial_m(B_\theta/A_\theta)\` is strictly increasing and whether its minimizer always remains \`m=1469/64\`. Keep the native Bellman \`z<11/16\` phase as a separate open unit.

The source pin, P000/X6 ontology, scientific evidence grade and joint-observer provenance remain unchanged. The price density is an external effective observer, not an identification of the BRC carrier with a continuum physical state.
