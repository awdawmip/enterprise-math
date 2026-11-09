# BRC-X6 original-native D511: ten-dimensional eleven-policy compression family

Date: 2026-11-10 Asia/Hong_Kong. Status: **AUTHOR_PROVED / EXACT_SYMBOLIC_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. No formal Source CLAIM, Task Result, independent review or Foundation admission is asserted. Frozen science SHA256: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Native input and honest reuse

Use the original 96 native ports, six labeled actions, original four source ports (6,7,28,29) with signs (+,-,-,+), and all nine frozen fully signed seven-variable joint next-port/reward root observers. Exhaustive original check of all 6^4=1296 source-action tuples yields exactly 38 valid deterministic policies. Order these policies lexicographically and form their 24-by-38 source/action indicator matrix C, rank 13.

**Inherited source (not claimed as new):** 2026-11-10 author-portable proof at commit `362ddf73ac063699974221df822787e6bc3e0a9f`, Git blob `c08177e6524188a7fbb4ed82fd4485286556ee11`, defines 13 independent policy indices
`I=(2,8,15,21,24,28,29,31,37,0,1,3,5)`
and fixed eleven-policy support
`S4=(0,1,3,6,8,12,17,28,29,30,31)`. It establishes exact integral J with `C[:,I] J=C[:,S4]`, ranks 13 and 11 respectively, and an earlier five-dimensional 183,121,078,608-member subfamily. Preserve that authorship and the earlier 199 D511 candidate reductions.

For zero-based S4 weights v0,...,v10, the complete inherited map w=Jv is:

```text
w0=v9; w1=v4; w2=v5; w3=v6; w4=2*v3+v6;
w5=-v3-v6+v7; w6=-v3+v8; w7=-v3+v9+v10;
w8=v3; w9=v0-v3+v5; w10=v1+v3;
w11=v2-v5; w12=v3-v9.
```

## NEW theorem: ten-dimensional integer parameter slice

Let t,s,r,q,h,k,j,m,n,p,u be **nonnegative integers** satisfying

```text
5(t+s) + 2(r+k) + q+h+j+m+n+p+u = 490.  (1)
```

Set the strictly positive eleven-policy integer weights

```text
v = (m+s+t+3, n+1, j+k+2, s+t+2, p+1,
     k+1, r+1, q+r+s+t+4, h+s+t+3, t+1, s+u+2)  on S4
```

and the 13-chart integer weights

```text
w = (t+1, p+1, k+1, r+1, r+2s+2t+5, q+1, h+1,
     u+1, s+t+2, k+m+2, n+s+t+3, j+1, s+1)  on I.
```

For **every** tuple satisfying (1), direct substitution into the prior exact J proves the full **24-dimensional original-native integer equality**:

```text
C[:,I] w = C[:,S4] v = B;  sum(v)=sum(w)=511.
```

The complete four-source six-action numerator matrix B is:

```text
[j+k+m+n+2s+2t+8, p+1, k+1, r+1, h+q+r+2s+2t+7, s+t+u+3]
[j+k+m+n+p+s+2t+8, s+u+2, k+1, r+1, q+r+2s+2t+6, h+s+t+3]
[h+k+m+r+2s+2t+8, n+s+t+u+4, s+t+2, p+1, j+k+2, q+r+s+t+4]
[k+m+r+2s+2t+7, h+n+s+t+4, p+t+2, s+u+2, j+k+2, q+r+s+t+4]
```

Every B entry is positive and each row sums to 511. Because all 11 S4 policies separately pass all nine signed native joint-root constraints and **equality precedes any observer projection**, the pair of representations preserves the original full signed joint observer. Thus each normalized X=B/511 has **minimum support at most 11** in the original native model.

## Exact number of distinct instances

The generating function and explicit finite sum give

```text
N = [x^490] (1-x^5)^(-2) (1-x^2)^(-2) (1-x)^(-7)
  = Σ_{a=0}^{98} Σ_{b=0}^{floor((490-5a)/2)}
      (a+1)(b+1)*binom(490-5a-2b+6,6)
  = 2,715,533,292,923,099,825.
```

Different parameter vectors yield different v, since one recovers t=v9-1, s=v3-t-2, then r=v6-1, q=v7-r-s-t-4, h=v8-s-t-3, k=v5-1, j=v2-k-2, m=v0-s-t-3, n=v1-1, p=v4-1, u=v10-s-2. Because C[:,S4] has column rank 11, different v give different B. Therefore N counts **distinct exact native probability vectors**, not the number of program runs.

For the large subfamily p=0, the first source's action-1 numerator B[0,1]=1. Consequently 1/511 occurs as one exact probability coordinate, so the common denominator is *irreducibly* 511 (nine bits). Its exact cardinality is:

```text
[x^490] (1-x^5)^(-2)(1-x^2)^(-2)(1-x)^(-6)
= 53,781,563,553,469,025.
```

The total family has display denominator 511; other members can sometimes reduce it. None of these counts proves global absence of nine-bit 13-minimal strategies. We assert `minSupport(X)<=11`, not `minSupport(X)=11`.

## Explicit endpoint and reproducibility

Choose p=490 and all other ten parameters 0. Then

```text
v=(3,1,2,2,491,1,1,4,3,1,2)
w=(1,491,1,1,5,1,1,1,2,2,3,1,1)
B=[8,491,1,1,7,3;
   498,2,1,1,6,3;
   8,4,2,491,2,4;
   7,4,492,2,2,4].
```

Rows sum 511; all entries positive; full signed native observer checks pass; gcd(511,B coordinates)=1.

A separately packaged exact verifier `verify_10dim.py` re-enumerates 1296 original actions, 38 legal policies, 9 signed roots, checks ranks 13/13/11, original map J, all 24 affine coordinates and positivity, injectivity and sample. Two *different* exact cardinality methods (bounded integer dynamic programming and finite binomial double sums) agree on both totals. No float arithmetic and no simulated/native research execution claimed. Reproduction archive SHA256 `6e01dd2b8e4ebebf6042cbfc7e8bf825a774600e146ce35ba42044aafed6fe30` has original frozen kernel, full Chinese proof, JSON certificate, script and README, clean extraction self-test PASS.

Source continuation: D25/H0-B0 native divided-power and [X]U mod p^2, Frobenius/eta/kappa and signed Hesse/Green remain with authorized Source owner. Original UR V2 four-file target remains 94,687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, not recovered; completed UR mathematics must not be recomputed. Next: classify other fixed supports and seek a target-specific exact full <=12 separation certificate for any nine-bit 13-minimal candidate outside this compression family, preserving Research1 deduplication.

**Proof scope / provenance:** new result is the ten-dimensional parameter construction and the exact counting/irreducible nine-bit subfamily. Prior C/J/S4 and historical reductions are inherited. All evidence remains author-only, unreviewed and not admitted.
