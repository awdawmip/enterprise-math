# D25: exact Clausen square and reflected p² convolution-corner certificate

2026-10-25 author-side research, **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; NOT the maintenance lane. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, frozen taskbook blob `53a3ef039325534e3715add837f0eee332289984`. Parent D24 first digit is accepted; the second-digit LIFT/JT2 is NOT solved. Previous author-side durable frontier: `b2049e0f8fc7c595260b4aedae50b16629523af3`, three-jet PF equations for the *original signed* Wp.

## New exact third-digit reduction

Let p=6m+1>=7 be prime and n<p. Set

```text
r_n = (1/6)_n (1/3)_n / (2^n (n!)²)
    = product_{i=0}^{n-1} ((6i+1)(3i+1)) / (36^n (n!)²)
a_n = (1/2)_n (1/3)_n (2/3)_n / (2^n (n!)³)
W_p = sum_{n=0}^{p-1} (6n+1) a_n
R_p = sum_{n=0}^{p-1} r_n
D_p = sum_{n=0}^{p-1} n*r_n
Q_p = sum_{0<=j,k<p; j+k>=p} (6(j+k)+1)*r_j*r_k
```

All denominators above are p-adic units. By the *classical* Clausen symmetric-square identity, a_n = sum_{j=0}^n r_j r_{n-j} **exactly in Q**. One direct proof: Y(x)=2F1(1/6,1/3;1;x) satisfies x(1-x)Y''+(1-3x/2)Y'-Y/18=0. Its square U satisfies [theta³-x(theta+1/2)(theta+1/3)(theta+2/3)]U=0 with U(0)=1; the coefficient recurrence uniquely gives the 3F2 numerator (1/2,1/3,2/3), and x=z/2 accounts for 2^{-n}. Prior-art reference: https://mathworld.wolfram.com/ClausenFormula.html .

Summing this convolution with the *unaltered* original cutoff gives the exact rational identity

```text
W_p = R_p² + 12 R_p D_p - Q_p.                    (A)
```

For 0<=n<p, v_p(r_n)=1_{n>m}+1_{n>2m}. Among the ordered pairs j+k>=p, the **only** contributions with combined valuation precisely two are the two symmetric corners 1<=j<=m, p-j<=k<=p-1. All other pairs have valuation >=3. Thus Q_p belongs to p² Z_(p).

**New universal reflection.** Put v_h=(r_{p-h}/p² mod p), 1<=h<=m. Wilson's theorem applied to the products 6i+1 and 3i+1 over 0<=i<=p-2, excluding their unique zeros at i=m and i=2m, gives

```text
v_1 = r_{p-1}/p² = 1/10   mod p,
v_{h+1}/v_h = 36 h² / [(6h+5)(3h+2)]   mod p.
```

Proof of v1: nonzero residue products are (-1)/(-5)=1/5 and (-1)/(-2)=1/2; the denominator 36^{p-1}((p-1)!)²=1 mod p. The backward ratio is the exact one-step ratio for r_{p-h-1}/r_{p-h}. All denominators are units for h<=m.

Define V_j=sum_{h=1}^j v_h and M_j=sum_{h=1}^j h v_h. The entire p²-truncation corner is now the finite **O(m)-arithmetic** certificate

```text
T_p := Q_p/p² mod p
     = 2 sum_{j=1}^m r_j [ (6j+1) V_j - 6 M_j ] mod p.     (B)
```

Consequently for every p=6m+1>=7,

```text
W_p = R_p(R_p+12D_p) - p² T_p   mod p³.          (C)
W_p = R_p(R_p+12D_p)            mod p².          (D)
```

The still-open D25 original signed scalar target on p=13,19 (mod24) is **strictly equivalent** (at the established author-side Wp interface) to the *single coupled moment condition*

```text
R_p(R_p+12D_p) = p + p² T_p   mod p³.           (E) [OPEN]
```

No independent seam or shift assumptions, first-digit reproof, or unsupported F_p-to-F_{p²} lifting are used.

Also, since 1/6=-m and 1/3=-2m modulo p and r_n=0 modp above m,

```text
R_p = sum_{j=0}^m binom(m,j) binom(2m,j) 2^{-j}
    = 2^{-2m} [x^{2m}](1+x)^m(1+2x)^{2m}    mod p.       (F)
```

Formula (F) is proven; all-target vanishing of this Hasse-like coefficient on p=13,19 (mod24) is NOT proven here. **Conditionally** if R_p=p U_p, (E) is equivalent to

```text
12 U_p D_p + p(U_p²-T_p) = 1  mod p².          (G) [OPEN]
```

D_p must be retained mod p², not only mod p.

## Falsifying the tempting but invalid tail deletion

At p=19, independent exact residue arithmetic gives T_19=12, hence Q_19=19²*12=4332 !=0 (mod19³). Therefore the corner cannot be suppressed at the third digit, although W_19=19 mod19³. T_13=0 is an exceptional checked case, not a general law.

## Exact verification, provenance, observer discipline

Local author-side script `d25_clausen_tail_reduction_20261025.py` computes r_n by the original ratio, a_n by an **independent** 3F2 ratio, and checks (C) for all 94 p=1 mod6 primes <=1200 plus p=19963. It also checks the reflected coefficient (B) rank-by-rank, confirms (F), and cross-checks (B) against the **independent full double-sum Q_p** for 15 primes <=139. Four m=1..4 rational Clausen coefficient cases are exact Fraction checks (m=4 yields composite 25, used only for a rational identity). Sample (p,T_p): (13,0),(19,12),(37,11),(43,15),(211,119),(19963,13363). All target primes within this finite corpus satisfy the hypothesized scalar, but a finite sample is not a universal proof. Native benchmark has NOT been run.

The genuine BRC/Enterprise carrier keeps ordered branch labels (j,k), signs, prime valuations, original cutoff predicate and the modulo-p³ weighted observer. Individual valuation >=3 certifies erasure *only at this declared precision*; the residual T_p is retained, not treated as positive mass. This is `COMPOSE_APPLIED` for BRC valuation/provenance with classical Clausen, not a native X6 or Heartbeat simulation. Auxiliary z, j, k are not spatial axes.

This GitHub document is neutral, author-side evidence; **not** Source-native research activity, CLAIM/run/checkpoint/Result/review. Source continuation read returned `CONTROL_QUOTA` during this run; the Site credential is read-only for Researcher writes and #1539 is the existing control-maintenance support path. No claimed own active session/claim/run, no unknown write request reissued, no maintenance-lane identity used. Original native benchmark, Source acceptance and independent review remain outstanding.

**Next exact scientific action:** evaluate R_p,D_p and the already exact T_p jointly through a genuine all-target finite-field Gauss/Jacobi-sum or Picard–Fuchs/Frobenius certificate proving (E), or produce a fully checked exact counterexample. Preserve source pins and the frozen Delta_p-R_p bridge. No automation or notification settings changed.
