# OAI7 r353 — Uniform ordered margins: twin-compressed exact optimizer and a strict entropy gap

2026-11-19. Author-side finite theorem, depending on the exact r347–r352 cyclic-group minimax certificates. Original OAI7 researcher and contribution history retained; no Native independent review claimed.

## Setting

Let \(C\subset\mathbb F_{29}\) be a random 5-element set, and \(H=(H_1,\ldots,H_5)\) an ordered realization of its five distinct elements. Impose two simultaneous conditions:

1. The law of the unordered set \(C\) attains the **exact unrestricted** minimax value \(q^* = 2024467747/3324255613\) in the fixed 4-test loss game \(b_K(C)=\mathbf1\{|K-C|\le16\}\).
2. Each of the **five ordered coordinates** \(H_i\) is individually uniform on \(\mathbb F_{29}\).

The second is a stronger property than merely having identical positional margins. Set \(D=474893659\), \(N=28D=13297022452\), and \(\alpha=34177518/D\). By r352, every exact optimizer has the same probability law on its 350 complete loss-profile fibers, with Shannon entropy
\[
H_*=H_{\min}=7.869745624309653\ldots\ \text{bits}.
\]
Each fixed fiber mass is an integer multiple of \(1/N\).

## New theorem: a constructive improvement and a strict lower bound

**Constructive upper bound.** There is an exact minimax ordered shared-shift law with all five positional margins uniform and joint entropy
\[
\boxed{H(H)=H_*+\log_2 29
=12.727726619437224\ldots\ \text{bits}.}
\]
This improves r347's previously exhibited exactly uniform-margin law of \(12.799695400978694\ldots\) bits by exactly
\[
\boxed{\alpha=\frac{34177518}{474893659}
=0.07196878154\ldots\ \text{bits}.}
\]
It uses 350 times 29 = **10,150** possible ordered sequences, rather than r347's 10,962 underlying shift sets, and uses no independent random sorting seed.

**Strict lower bound for all such laws.** For every exact minimax ordered law with even just its *first* positional margin uniform on the 29 symbols,
\[
\boxed{H(H)\ \ge\ H_*+
\frac{204}{29\cdot 28D\ln 2}
=H_*+7.632245059159493\ldots\times10^{-10}\ \text{bits}.}
\]
In particular, the unrestricted entropy-minimizing r352 350-atom law cannot itself be given deterministic ordering with a perfectly uniform first-position margin. Thus the minimum entropy under all five uniform positional margins is attained strictly above \(H_*\), and is at most \(H_*+\log_2 29\). The exact constrained minimum within these bounds is open.

## Proof of construction

Choose exactly one representative \(c_x\) of each of the 350 positive loss-profile fibers characterized in r352. Choose profile \(X=x\) with its uniquely forced mass \(q_x\), then choose \(T\) independently and uniformly in \(\mathbb F_{29}\). Fix any deterministic ordering \((c_{x,1},\ldots,c_{x,5})\) of the five elements and output
\[
H=(c_{x,1}+T,\ldots,c_{x,5}+T).
\]
For each i, conditional on X, \(H_i\) is uniform in the field. Therefore all five unconditional margins are exactly uniform. Translation invariance of each \(b_K\) preserves *all* fixed-test failure probabilities, so the original exact minimax value remains attained. The translation action of the prime-order group is free on each proper nonempty five-set. The unordered output uniquely determines its translation class X and translation T, hence the map \((X,T)\mapsto H\) is injective. Consequently \(H(H)=H(X,T)=H_*+\log_2 29\). The 28 r350 twin pairs have already been merged, accounting for the exact \(\alpha\)-bit improvement.

## Proof of strict lower bound

Let \(X=\sigma(C)\) denote the complete 819-test loss profile of the unordered set. r352 proves its distribution is fixed for **every** exact minimax law; write \(q_x=n_x/N\), integers \(n_x>0\), \(\sum n_x=N\).

For each x, choose an ordered tuple \(h_x\) maximizing the conditional probability \(\Pr(H=h\mid X=x)\). Let \(e_x=1-\Pr(H=h_x\mid X=x)\) and \(E=\sum_xq_xe_x\). Put \(Z=(h_X)_1\), the first coordinate of the deterministic modal representative. Its distribution has integer/N probabilities: \(\Pr(Z=a)=m_a/N\), where integers \(m_a\ge0\) sum to N. Coupling Z with the actual first coordinate gives
\[
\operatorname{TV}(\mathcal L(Z),\mathcal L(H_1))\le E.
\]

Because \(N\equiv17\pmod{29}\), the exact smallest total-variation distance between the 29-point uniform distribution and any integer/N probability vector is
\[
\delta_N=\frac{17(29-17)}{29N}=\frac{204}{29N}.
\]
Indeed, round the ideal count \(N/29\) down in 12 bins and up in 17 bins; no integer counts can attain a smaller absolute discrepancy. Uniformity of \(H_1\) therefore forces \(E\ge\delta_N\).

For each conditional distribution, Shannon entropy dominates min-entropy, and
\[
H(H\mid X=x)\ge-\log_2(1-e_x)\ge e_x/\ln2.
\]
Average this inequality. Since X is a deterministic function of H, the entropy chain rule gives
\[
H(H)=H(X)+H(H\mid X)\ge H_*+\delta_N/\ln2,
\]
as asserted. All denominators, class masses and 29-symbol integrality statements are exact; displayed decimal bounds are approximations only.

## Small exact-parameter certificate

Python 3 standard library; arithmetic establishing the rational mass grid and its residue is integer exact. The entropy numbers are display checks only.

~~~python
from math import log2, log
a={1:16479487,2:17698031,5:90390274,6:10843621,
   7:139525152,11:6049484,23:10138260,25:26578050,
   30:14514456,37:22809640,47:3118488,50:39221480,
   114:53586612,115:23940624}
S=list(a)
D=474893659
assert sum(a.values())==D
t={j:(14 if j==6 else 28) for j in S}
N=28*D
profile_numerators=[]
for j in S:
    count=t[j]//(2 if j in (1,2) else 1)
    weight=(28//t[j])*a[j]*(2 if j in (1,2) else 1)
    profile_numerators += [weight]*count
assert len(profile_numerators)==350
assert sum(profile_numerators)==N
assert all(n>0 for n in profile_numerators)
assert N==13297022452 and N%29==17
alpha=(a[1]+a[2])/D
Hstar=-sum((n/N)*log2(n/N) for n in profile_numerators)
upper=Hstar+log2(29)
gap=(17*12)/(29*N*log(2))
assert abs(Hstar-7.869745624309653)<1e-12
assert abs(upper-12.727726619437224)<1e-12
assert abs(alpha-0.07196878154146927)<1e-14
print("r353 PASS: 350 positive profile masses, denominator",N,
      "uniform-position upper",upper,"strict gap",gap)
~~~

## Provenance and limits

Dependencies: r347 at 12bd331ea2aef70cc844682db432a623b235e726; r348 at f41c2690daba467ecbde99615a1337e67be46ffd; r350 at 2737a8ea300816066714ef0ff8d72b62c6df2e46; r351 at 6a9da64ae349c647744773f92c80753a6f9ffb23; r352 at c660dc487bbb5f96789a3b2876ed82c32245eecf.

Original contributor EM-EMF6D046-5A2844; Task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19. Results concern the declared finite prime-29 coverage model and do not claim independent Native review, Source/Activity admission, native X6 safety transfer, Task completion or parent-goal completion.
