# Unrestricted-stock comparison above the 63-pair cut

This derivation uses the C62 positive three-state model, its balanced gaps, and its bounds for the canonical gap. All stocks and consumption are integers, with at least two fives held back for the final tail.

Let K=2r+1, n=K+c, s=c−r−1, and s′=s+1−m. For an m-five internal block let ρ=q1/q2, τ=7q0/q2, M=max(1,ρ), and

    L = τ |ρ−1|/(τ+M)².

This is its exact minimum derivative magnitude on [0,1]. Let G_r be the maximum derivative magnitude of the canonical m=1 map at c=r+1 for r≥2. C62 proves G_r ≤ 1/(100r²). Use the potential

    W(r,c) = 16^s                                      for s ≤ 0,
             16^(s−1) (2r+c+1)!/(3r+3)!                 for s ≥ 1.

The two starting surpluses s=0,1 have W=1. Negative starting s has W<1. Write Q=W(r−1,c−m)/W(r,c).

**High-scale lemma.** At r≥64, every noncanonical block (s,m)≠(0,1) has L/G_r > (21/10)Q. The canonical block retains its own exact minimum derivative.

We use (x)_j=x(x−1)⋯(x−j+1). All m≥1 inventory ratios satisfy 4^(−m)≤ρ≤4 and 7·16^(−m)≤τ≤448 from C62; the same upper bounds and the lower bounds at m=0 hold. In the product ρ=P/[4^m(n)_(m+1)], P is odd, and P≡4^m(n)_(m+1) modulo 3. Thus |ρ−1|≥3/[4^m(n)_(m+1)] for m≥1. The same estimate holds for m=0 as ρ−1=3c/n.

## 1. Empty gaps

For s≤0, Q≤16 and ρ−1=3c/(K+c)>1/r. For c≤r+1, the two last denominator ratios in τ give τ≤7·3·3=63, and τ≥7. Thus τ/(τ+4)²≥1/80 by checking 7,63, and L/G_r>100r/80>(21/10)·16.

For s≥1, Q=16(3r+3)_3/[(K+c)(K+c−1)]. Exact cancellation gives

    L = 168 c (c+2r)(2c+r)(c+2r+1)(c+8r+4)
        /[(4c+2r+1)(113c²+290cr+116c+128r²+64r)²].

The polynomial numerator of 100r²L−(21/10)Q at c=r+2+x, r=64+t has 52 nonzero coefficients, all positive, with positive constant. Its denominator is positive by the displayed formula for L and Q. The companion polynomial-check script verifies this finite algebra identity exactly.

## 2. Single fives

When m=1, Q≤1. At s≤−1 or s≥1 the gap |ρ−1| exceeds 1/(2r). Indeed ρ increases with c and

    ρ−1 = 3[4c(c−1)−K²]/[4(K+c)(K+c−1)].

Evaluate at c=r or c=r+2 to bound the respective sides. The minimum of t/(t+4)² on [7/16,448] is greater than 1/460, as may be checked at its endpoints. Hence L/G_r>100r/920>21/10. The single-five block at s=0 is the canonical one.

## 3. Two or more fives away from resonance

If m≥2, Q≤16^(2−m). When both endpoint surpluses are at least 1, the exact ratio is

    Q = 16^(1−m)(3r+3)_3/(K+c)_(m+2) ≤16^(1−m).

If both are nonpositive, Q=16^(1−m); if a supra-diagonal stock falls to nonpositive surplus, the initial factorial multiplier is at least 1, giving Q≤16^(2−m). A transition from nonpositive to positive surplus is impossible when m≥2.

For all m≥2, τ/(τ+M)²≥(2/5)16^(−m). Check t/(t+4)² at t=7·16^(−m) and 448, using 7/(4+7/256)²>2/5 and 256·448/452²>2/5. If |ρ−1|≥1/10, this yields L/G_r≥4r²16^(−m)>(21/10)Q.

## 4. Near resonance for two or more fives

Suppose 9/10<ρ<11/10. Both endpoints must have surplus ≥1. Otherwise c−m≤r (a nonpositive initial surplus gives this as well when m≥2). For m=2,3, c/K≤(r+3)/(2r+1)<3/5, and ρ≤(17/8)^(m+1)/4^m<9/10. For m≥4 use

    ρ ≤ 4 exp[−3Km/(4(K+c))]
      ≤ 4 exp[−3(2r+1)m/(4(3r+1+m))] < 4 exp(−9/5) < 9/10.

The first inequality follows by multiplying m factors (K+4n_j)/[4(K+n_j)], with n_j≤c, and a last factor ≤4. The exponent bound is increasing in m, and its value at m=4, r≥64 exceeds 9/5.

At high endpoints, c−m≥r+1 and the odd-integer gap and exact potential ratio imply

    (L/G_r)/Q ≥ [300 r² (2r+c−m)/(3r+3)_3] ·4^(m−2) τ/(τ+M)²
                > 32·4^(m−2) τ/(τ+11/10)².

Indeed (2r+c−m)≥3r+1 and 300r²/[(3r+3)(3r+2)]>32.

Set t=(c−m)/K>1/2 and h0(x)=(1+4x)/(16+4x). In τ, the likelihood ratio L0/L2 is the product of h0(n_j/K) at the m pre-consumption stocks. Thus τ≥7/6^m. Moreover ρ≥[(1+4t)/(1+t)]^(m+1)/4^m. The following elementary bounds complete the small cases.

| m | upper bound for t from ρ<11/10 | upper bound for τ | lower bound for τ/(τ+11/10)² |
|---|---|---|---|
| 2 | 6/5 | 8 | 1/12 |
| 3 | 2 | 27 | 1/60 |
| 4 | 3 | 14 | 1/240 |

For m=2, c/K<6/5+2/129 and h0(c/K)<29/100. The final ratios D2/D0<9/2 and (D2−1)/(D1−1)<27/10 give the claimed τ bound. For m=3, c/K<2+3/129 yields h0(c/K)<2/5 and final ratios at most 6 and 4, respectively. For m=4, c/K<3+4/129 yields h0(c/K)<1/2 and final ratios at most 8 and 4. In every row check τ/(τ+11/10)² at the lower endpoint 7/6^m and the tabulated upper endpoint. Multiplication by 32·4^(m−2) yields a strict factor >21/10 in each case.

For any m, h1(x)=(1+4x)/(4+4x) satisfies h0(x)≥h1(x)^5, by (1+z)^5≥1+5z at z=3/(1+4x). The last ratio D2/D1≤4. Hence τ≥7(ρ/4)^5 and near resonance τ∈[7(9/40)^5,448]. The endpoint test gives τ/(τ+11/10)²>1/460, so 32·4^(m−2)/460>21/10 for m≥5. This proves the high-scale lemma.

## 5. Factorial cancellation below the cut for large initial stock

For every r≥1, every c≥2 and 0≤m≤c−2, one has

    L ≥ 1/[460 · 4^m · (2r+c+1)_(m+1)].

For m=0,1 use τ∈[7/16,448], M≤4 and the integer gap above. For m≥2 near resonance use τ≥7(9/40)^5 directly as in §4 (high-scale assumptions are unnecessary here). For m≥2 away from resonance, L≥(1/25)16^(−m), and every descending product factor is at least 4. All arguments in this paragraph require only K≥3 and c−m≥2.

Consider any continuation with r remaining pairs and current stock c, ending at stock v≥2 before the terminal hidden-only gap of v−2 fives. Let c_j′ denote the stock after consuming the gap at remaining pair count j. Across the r edges, the successive falling products telescope, leaving precisely one factor per visible pair unconsumed:

    ∏(2j+c_j+1)_(m_j+1) = (2r+c+1)! /[(v+1)! ∏(2j+c_j′)].

In the final gap, l1=3/(v+1) and l0≤l1≤l2≤1. Its minimum TV derivative T=l2(7l0+l1)/(7l0+l2)² is ≥l1/64. Thus (v+1)!·4^v·T≥1 and ∏(2j+c_j′)≥2^r(r+1)!. At s≥1, multiplying by W gives the lower bound for every suffix absolute slope normalized by the canonical supremum U:

    (W/U)·T·∏L ≥ 4^c·(2/460)^r·(r+1)!/[16^(r+2)(3r+3)!·U].

Here U at r=63 is the exact supremum of the derivative of the *whole* canonical suffix into terminal TV. It is computed from its integer Möbius matrix, and is stored in cut63_full.json; it is not the product of individual suprema. At r=63 the displayed rational bound is strictly greater than 2 for c=319 and increases by a factor of 4 per additional stock unit. The integer verifier and cut63_extension.json include the exact ratio for c=319. Thus only the finite cut 2≤c≤318 remains to be checked.
