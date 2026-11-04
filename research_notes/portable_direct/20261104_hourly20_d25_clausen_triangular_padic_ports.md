# D25 — Clausen rank-two boundary port, exact unit-cancellation windows

Date 2026-11-04. Status: AUTHOR-DERIVED / ALGEBRAICALLY PROVED IN DECLARED SCOPE / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical lane chatgpt-research-hourly-enterprise-math-20260923; separate maintenance lane chatgpt-hourly-enterprise-math-20260921.

Existing D25 Green/two-seam source: commit aa7708f4887e92dc4f314b44ad23b63c5bd6da67. Another Research lane independently recorded a finite fourth-digit observation at commit 2d9b26653d549827ded0359d25d3fc7090b1ba3c. This note does not re-claim it. Guo–Zudilin (2019) already proved the quartic weighted V sum modulo p^3 (arxiv.org/abs/1803.01830); the W216 counterpart remains open here.

## 1. Exact rational rank-two convolution

For n>=0 define original a_n=binom(2n,n)^2 binom(3n,n)/216^n and b_n=binom(2n,n)^2 binom(4n,2n)/2304^n. Define u_k=(1/6)_k(1/3)_k/((k!)^2 2^k), v_k=(1/8)_k(3/8)_k/((k!)^2 9^k). Then, **for every integer n>=0 over Q**,

    a_n = sum_{i=0}^n u_i u_{n-i};     b_n = sum_{i=0}^n v_i v_{n-i}.   (1)

Proof: The *classical* Clausen square formula

    2F1(alpha,beta;alpha+beta+1/2;z)^2
      =3F2(2alpha,2beta,alpha+beta;2alpha+2beta,alpha+beta+1/2;z)

applied at (alpha,beta,z)=(1/6,1/3,t/2) and (1/8,3/8,t/9) respectively gives the two coefficient identities. Equivalently the squares solve the unique normalized symmetric-square ODE theta^3 - z(theta+1/2)(theta+2alpha)(theta+2beta); coefficient comparison proves (1). Clausen is established, not a claimed new theorem (https://mathworld.wolfram.com/ClausenFormula.html).

Consequently the **strict truncation**, not the untruncated rank-two square, is

    W_p = sum_{i+j<p} (6(i+j)+1) u_i u_j,
    V_p = sum_{i+j<p} (8(i+j)+1) v_i v_j.                      (2)

The index-p upper triangle must be retained separately at the p^3 target precision.

## 2. Sharp all-unit p-adic residue cancellation

**Theorem A.** For every prime p=6r+5>=11, all u_k with 0<=k<=4r+3 are p-adic units. Each of the n+1 terms in (1) is a unit, yet

    v_p(sum_{i=0}^n u_i u_{n-i}) =
      1   if 2r+2<=n<=3r+2,
      2   if 3r+3<=n<=4r+3.                                  (3)

**Theorem B.** For every prime p=8q+5>=13, all v_k with 0<=k<=5q+3 are units and all terms of the corresponding convolution are units, yet

    v_p(sum_{i=0}^n v_i v_{n-i}) =
      1   if 2q+2<=n<=4q+2,
      2   if 4q+3<=n<=5q+3.                                  (4)

Proof: For p=6r+5 the first p factors in (1/3)_k and (1/6)_k occur at numerator indices 4r+3 and 5r+4 respectively, so u_k are units through 4r+3. For p=8q+5 those in (1/8)_k and (3/8)_k occur at indices 5q+3 and 7q+4, so v_k are units through 5q+3. Denominators remain units for 0<=k<p. On the other hand Legendre's formula gives exactly v_p(a_n)=floor(2n/p)+floor(3n/p), v_p(b_n)=floor(4n/p) for n<p. Evaluating those floors on the stated intervals yields (3) and (4), including exactness. QED.

This is a BRC provenance/observer witness. Population: ordered indexed factor pairs (i,n-i). Future operation: rational convolution then p-adic mod p^3 observation. All input-term valuation coordinates are zero in the windows, while the sum valuation is 1 or 2. A valuations-only port cannot represent the residue cancellation; retain full modular residues and pair provenance. This is p-adic modular cancellation among rationally positive inputs, not a native X6 physical or signed-amplitude claim.

## 3. Exact quadratic triangle boundary and target-class repair

For factor x=u or v with weight w=6 or 8, define S_x=sum_{k=0}^{p-1}x_k, D_x=sum k x_k, and upper triangle T_x=sum_{0<=i,j<p,i+j>=p}(w(i+j)+1)x_i x_j. Exact coefficient separation over Q gives

    sum_{n=0}^{p-1}(wn+1) sum_{i=0}^n x_i x_{n-i}
        = S_x^2 + 2 w S_x D_x - T_x.                          (5)

**Theorem C.** For every prime p=6r+1>=7,

    T_u = 2 sum_{i=1}^r sum_{j=p-i}^{p-1} (6(i+j)+1) u_i u_j
          (mod p^3),     T_u = 0 (mod p^2).                   (6)

For every prime p=8q+3>=11,

    T_v = 2 sum_{i=1}^q sum_{j=p-i}^{p-1} (8(i+j)+1) v_i v_j
          (mod p^3),     T_v = 0 (mod p^2).                   (7)

Proof: In the first case v_p(u_k)=0 for k<=r, =1 for r<k<=2r, =2 for 2r<k<p. A pair i+j>=6r+1 necessarily has at least one index >2r. Thus every pair has valuation >=2. The only pairs which can have valuation exactly 2 have the other index <=r; their two orientations contribute the factor 2. All omitted pairs have valuation >=3. In the second case v_p(v_k)=0 for k<=q, =1 for q<k<=3q+1, =2 for 3q+1<k<p. Repeat the same argument. QED.

On the **mother target class p≡19 mod24**, both formulas apply. Writing C_u,C_v for their low/high right sides, the original unresolved signed sum has the newly verified *rank-two, p^3-exact* port

    W_p-V_p =
      (S_u^2+12 S_u D_u)-(S_v^2+16 S_v D_v)-C_u+C_v (mod p^3). (8)

For p≡13 mod24 only (6) follows from termwise valuation. The quartic factor is in the all-unit cancellation regime of Theorem B. An explicit discriminator: at p=13, T_v≡1170 mod 2197 has exact valuation ONE. Hence an indiscriminate T_v=0 (mod p^2) would fail on the frozen target class. At p=19, T_u/p^2≡12, T_v/p^2≡3 mod19; at p=43, they are 15 and 14 mod43.

Equation (8) is a reduction, not a final proof of W_p−V_p=0 mod p^3. The frozen D24 Delta_p−R_p bridge and native p=373 H0/B0/Frobenius experiment remain independently open.

## 4. Exact executed verification

The companion Python standard-library checker was executed locally, exhausting all 94 primes 5<=p<=503. It checked 44,068 original-vs-Clausen coefficient comparisons modulo p^3, 3,844 A unit-cancellation positions, 1,891 B positions, and both quadratic upper triangle reductions (6),(7) wherever applicable. For primes 11,13,17,19,23,29,37, it additionally independently reconstructed original coefficients with integer factorial/binomial arithmetic. Result: ALL PASS. This is finite exact validation of the stated range; universal statements (1),(3),(4),(6),(7) have the proofs above.

## 5. Continuation and native control

Next independent mathematical action: at p≡19 mod24, try a terminating Gauss-Green/WZ transformation of the two rank-two square-and-derivative ports that also reproduces the nonzero low/high boundary terms in (8), first checking p=19,43,67. For p≡13 mod24, seek a genuine residue cancellation formula for the all-unit quartic upper triangle, starting p=13,37,373. Do not repeat the existing rank-three Green proof or Guo–Zudilin's quartic theorem. The separate 2026-11-04 fourth-digit pattern stays finite-only.

Actual 2026-11-04 gateway read: UPSTREAM_CODE_REVIEW_REQUIRED; research_authority_granted=false; executor_binding_configured=false; active quota 5/5. Scoped checkpoint read returned ACCESS_DENIED. No new native CLAIM, OPEN, Source checkpoint, Result, review or mathematical admission, and no alteration to other lanes' identities or protected staging. Existing support #1558 (control) and #1559 (native-373) remain the applicable paths.