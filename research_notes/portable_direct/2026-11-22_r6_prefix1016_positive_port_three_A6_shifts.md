# PREFIX-1016 — Positive terminal-port contrast reduces to three A6 shifts

Date: 2026-11-22 (+08). Status: AUTHOR_EXACT_FORMAL_SERIES_PROOF / SYMBOLIC_AND_INTEGER_CHECKED / NOT_REVIEWED. This is an independent portable continuation of PREFIX-1015, within the frozen candidate Stage46 signed BRC model.

## Typed input and exact question

Preserve scientific P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. The six-axis Cell/port model has 12 signed primitive directions, incoming-neighbour port h, integer BRC weight w(h,d)=1−6[h=d], new incoming port −d, initial chart-relative Cell 0 and port −e1. Both orientations of Link {0,e1} are absorbed without renormalization; grade k=1 means exactly one negative native step. Terminal amplitudes interfere only in the same joint Cell/port fibre before their squares are added.

Use the precisely defined Q⁺_{n,1}, Q⁺_{n,*} positive-terminal squared numerator masses of [PREFIX-1014](https://github.com/awdawmip/enterprise-math/blob/599f5d5306abae0101769432d6ff8da77517bf3e/research_notes/portable_direct/2026-11-22_r6_prefix1014_four_port_gram_orbits.md), where * is any single fixed axis j=2,...,6, not their sum. Set Δ⁺_n=Q⁺_{n,1}−Q⁺_{n,*}; its probability contrast is Δ⁺_n/36^n.

## Exact all-length theorem

For every integer n≥5, put m=n−4 and

A6(r) = Σ_{a1+⋯+a6=r} [r!/(a1!⋯a6!)]².

Then the following three-shift formula is exact:

Δ⁺_n = c1(m) A6(m+1) + c2(m) A6(m+2) + c3(m) A6(m+3),

c1(m) = −72(72m²+163m+80)/[5(m+1)],

c2(m) = 2(144m³+1135m²+2367m+1310)/[5(m+1)(m+2)],

c3(m) = −2(m+8)(2m+5)/[5(m+2)].

The three rational terms sum to an integer. The A6(m) term cancels exactly. All eleven marked-collision coefficients of the positive-port *contrast* are linear in n; their quadratic n² terms cancel, although either individual positive-port squared mass has quadratic coefficients.

## Derivation and symbolic certificate

First, retain the inherited exact joint-port Laurent packet: S=Σ_i z_i, U=Σ_i z_i⁻¹, a=z1, and

F⁺_{n,j} = S^{n−4} B⁺_{n,j},
B⁺_{n,j} = zj(S A_{n,j}−a A_{n−1,j}+25a),
A_{n,j} = (n−1)SU−36(n−3)−6S/a−6S/zj.

Writing T=S−a, this is B⁺_{n,j}=zj C_n−6ST with common
C_n=(n−1)S²U−(n−2)aSU−(36n−114)S+(36n−119)a−6S²/a.
Because monomial multiplication preserves the coefficient square norm, the ||S^{n−4} zj C_n||² terms agree for every j and cancel in the positive-port contrast; hence the n² coefficients cancel at each fixed collision signature.

Subtracting the PREFIX-1014 eleven signature columns gives Δ⁺_n=Σσ(aσ n+bσ)H_m(σ). In ascending absolute-signature order the pairs (aσ,bσ) are:

000000:(−1344,7788); 000011:(−1584,27132); 000022:(−1152,4836); 000033:(48,−108); 000112:(−2304,9312); 000123:(576,−2016); 001111:(7776,−30960); 001113:(288,−1728); 001122:(0,−6480); 011112:(−1728,−6912); 111111:(−576,−864).

Use PREFIX-1007's exactly proved collision generating series for each zero-sum signed representative δ of signature σ:

hσ(t)=Σ_m H_m(σ)t^m/(m!)²=t^p ∏_{i=1}^6 g_{|δ_i|}(t), p=Σ_i|δ_i|/2,
g_k(t)=Σ_{r≥0} t^r/[r!(r+k)!].

In the rational formal-series ring, g1=g0', t g2=g0−g1, t²g3=(t+2)g1−2g0. Put f=g0^6=Σ_m A6(m)t^m/(m!)² and u_j=g0^{6−j}g1^j. The seven-state differential module is

u1=f'/6; u_{j+1}=[t u_j'+j u_j−j u_{j−1}]/[(6−j)t], j=1,...,5.

Apply (aσ t∂t+4aσ+bσ) to each hσ; this corresponds exactly to multiplying H_m(σ) by aσ n+bσ with n=m+4. Substitution of g2,g3 and the seven-state module yields 12 exact Laurent differential terms t^q f^(r) with (q,r): coefficient:

(0,1):−1152; (0,2):524; (0,3):−48; (1,2):−3384; (1,3):7292/5; (1,4):−768/5; (2,3):−5184/5; (2,4):3134/5; (2,5):−462/5; (3,5):288/5; (3,6):−82/5; (4,7):−4/5.

For each term, (m!)²[t^m](t^q f^(r)) = (m!)² A6(m−q+r)/[(m−q)!(m−q+r)!] at an existing formal-series term. Collect by shift s=r−q. All terms have s in {1,2,3}. Their exactly simplified rational coefficients are c1,c2,c3 displayed above. This is an all-order identity by algebraic derivation, not polynomial interpolation from test values. The m≥1 bound has no final denominator singularity.

## Executed validation and scope

The independently implemented six-axis integer binomial splitting computes all eleven H_m signatures. A SymPy rational differential-operator generator checks all three rational functions as identities. A separate integer Laurent implementation of the inherited B⁺_{n,j} packet compares the *two individual port mass numerators* with the eleven-collision contrast and the three-shift result at each n=5,6,7,8,9. Full eleven-collision versus three-shift equality was checked for every n=5,...,50 and n=75,100. The known native signed BRC per-port comparison at n=5,...,8 is inherited from PREFIX-1014, not re-executed here.

Exact contrast values: n=5:25620; n=6:386028; n=7:7124592; n=8:149251656; n=10:81969197100; n=20:22995412496524439204257560; n=30:19259750715384614026293091913776702107120. All checked contrasts are positive; the universal sign remains an OPEN QUESTION.

This reduction is exact for the specified terminal coherent square observer only. For later native propagation retain the joint Cell–port, branch, sign and link history carrier. No independent Stage46 kernel re-run, Result/Review admission, or physical heartbeat-time assertion is made.

## Source / next research

Historical contributor provenance: EM-DIRECT-FBEA5D; Activity RA-3FB2D033BE6048D8712FF056. Do not infer current CLAIM/PROGRESS or portable Activity write rights from historical labels. Preserve existing author, pending Activity association and NOT_REVIEWED status.

Next: prove or disprove Δ⁺_n>0 for all n≥5 by an exact positive Gram representation or an admissible A6 recurrence inequality; compare its complexity with the three-shift formula. The mother problem B_fix,odd(32)∈{19,20} remains open.
