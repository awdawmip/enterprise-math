# R159 — Complement gauge, reversal width duality, and a sharp all-length slope-support width theorem

Date: 2026-11-15 (Asia/Shanghai). Status: **AUTHOR_PROVED**, exact finite checker through length 13, **NOT_REVIEWED**. Observer: external tied-phase integer-intercept finite Sturmian scalar S23; no native X6 embedding or Foundation promotion is claimed. Scientific inputs remain at the R146–R158 frozen pin \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.

Predecessor: R158 commit \`c96a9e24905566bba302ed82b45590f3c3812668\`, \`research_notes/portable_direct/R158_RESIDUE_THRESHOLD_CERTIFICATE_20261115.md\`. R159 concerns the *maximum* possible slope-support interval width and exact symmetries; R158's width-envelope question concerns the intercept-cut quotient by that width.

## 1. Precise model

Let \`w=w_1...w_m\` be an admitted binary word, \`m>=1\`, \`p_0=0\`, \`p_j=sum_{i=1}^j w_i\`, and \`n=p_m\`. Its open slope support \`(alpha,beta)\` is the intersection with \`(0,1)\` of the strict constraints \`(q-1)/k < theta < (q+1)/k\` for each contiguous factor of length \`k\` containing \`q\` ones. Write reduced \`alpha=a/b < beta=c/d\` (\`0<=alpha<beta<=1\`) and define

\`\`\`
A=min_{0<=j<=m}(p_j-j*alpha)
B=max_{0<=j<=m}(p_j-j*beta)
U=b*(1+A), V=d*B, Delta=beta-alpha.
C_w(L+1)=#{z in Z: L*alpha-U/b < z < L*beta-V/d}, L>=1.
W_w=(B-A)/Delta=(bd+bV-dU)/(bc-ad).
\`\`\`

\`U,V\` are integers, and \`W_w>=0\` because \`A<=0<=B\` (the empty prefix is zero). The R158 integer width cutoff is \`H_w=floor(W_w)\`; the actual final absence can be earlier, as its residue certificate computes.

## 2. R159A — exact all-length bit-complement gauge

**Theorem.** For every admitted \`w\`, its bitwise complement \`bar(w)\` is admitted with signature
\`\`\`
alpha_bar=1-beta, beta_bar=1-alpha,
U_bar=d-V, V_bar=b-U.
\`\`\`
For every integer \`L>=1\`, \`C_bar(L+1)=C_w(L+1)\` and \`W_bar=W_w\`. Consequently, their entire sets of absent coefficient positions and permanent thresholds are identical.

**Proof.** A contiguous factor count transforms \`(k,q)->(k,k-q)\`, hence the slope inequalities are mapped by \`theta->1-theta\`. The complementary prefix sums satisfy \`pbar_j=j-p_j\`. Thus at \`alpha_bar=1-beta\`, the minimum prefix cut is \`-B\`; at \`beta_bar=1-alpha\`, the maximum is \`-A\`. These yield the displayed \`U_bar,V_bar\`.

Put \`x=L*alpha-U/b\`, \`y=L*beta-V/d\`. The complemented open interval is exactly \`(L-1-y,L-1-x)\`. The integer involution \`z -> L-1-z\` bijects the integer points of \`(x,y)\` and the complemented interval, establishing count equality at every L. Equal interval lengths yield \`W_bar=W_w\`. QED.

**Information consequence.** The complete scalar count sequence is invariant under complementing the original source word. For every \`m>=1\`, the original word is therefore not identifiable from that scalar sequence alone; preserving original source identity requires a separate coordinate. This is an exact word-level alias, distinct from same-signature non-complement collisions in R153–R156.

## 3. R159B — reversal width duality

**Theorem.** Let \`w\` be a nonconstant admitted word of length \`m>=2\`, with total number of ones \`n\`; let \`w^R\` denote its reversal. Reversal preserves the slope endpoints and obeys
\`\`\`
U_R=b*(n+1)-m*a-U
V_R=d*(n+1)-m*c-V
W_w + W_(w^R) = 2/Delta - m.
\`\`\`
For a nonconstant palindrome, \`W_w=1/Delta-m/2\` exactly.

**Proof.** Reversal preserves the multiset of contiguous factors, hence the slope support. Put \`X_j=p_j-j*alpha\`, \`Y_j=p_j-j*beta\`. At each slope endpoint, the defining factor constraints imply the associated prefix range is at most one. For a nonconstant word it is exactly one: an interior endpoint is attained by a defining factor, and at the possible outer endpoint \`alpha=0\` or \`beta=1\`, respectively, the one-letter factor \`1\` or \`0\` attains the same range. Thus \`max X=A+1\` and \`min Y=B-1\`.

The reversed prefixes are \`p^R_j=n-p_(m-j)\`, so \`X^R_j=n-m*alpha-X_(m-j)\` and \`Y^R_j=n-m*beta-Y_(m-j)\`. Consequently,
\`\`\`
A_R=n-m*alpha-A-1
B_R=n-m*beta-B+1
B_R-A_R=2-m*Delta-(B-A).
\`\`\`
The signature and width formulas follow directly. For a palindrome \`W_R=W\`, giving the final formula. QED.

Constant words have \`W=0\`; their endpoint ranges are not both one, so the nonconstant condition is essential.

## 4. R159C — sharp maximum slope-support width and complete equality classification

**Theorem.** Among nonconstant admitted binary words of every fixed length \`m>=2\`,
\`\`\`
max_w (beta_w-alpha_w)=2/m.
\`\`\`
The equality words are precisely those with a **single 1 in a central position**, and their bitwise complements. The one-position indices are \`i=(m+1)/2\` when m is odd, and \`i=m/2\` or \`i=m/2+1\` when m is even. Hence the equality set contains two words for odd m, four words for even m. Constant words have gap \`1/m\`.

**Proof.** Let \`1<=n<=m-1\` be the total number of ones. The whole-word factor gives \`alpha>=(n-1)/m\` and \`beta<=(n+1)/m\`, so \`Delta<=2/m\`. Equality requires both endpoint equalities.

Suppose \`2<=n<=m-2\`. Consider the suffix of length \`m-1\`. If the first bit is zero, the suffix still contains n ones and forces \`alpha>=(n-1)/(m-1)>(n-1)/m\`. If the first bit is one, the suffix has \`n-1\` ones and forces \`beta<=n/(m-1)<(n+1)/m\`. Neither is compatible with equality. Thus equality requires \`n=1\` or \`n=m-1\`.

Complement symmetry reduces to \`n=1\`. Write \`w=0^a 1 0^b\` where \`a+b=m-1\`. Every factor containing the unique one has upper candidate \`2/k>=2/m\` and lower candidate zero, while the all-zero factors have upper candidates \`1/k\`. Thus
\`\`\`
alpha=0, beta=min(2/m,1/max(a,b))
\`\`\`
(with \`1/0=+infinity\` by convention). Equality \`beta=2/m\` holds exactly when \`max(a,b)<=m/2\`. Setting \`i=a+1\`, this is equivalent to \`m/2<=i<=m/2+1\`, yielding the asserted central index sets. Complementation produces the \`n=m-1\` cases; all such words exist for m>=2. A constant word has interval \`(0,1/m)\` or \`((m-1)/m,1)\`, hence gap \`1/m\`. QED.

**Connection to R158.** The real-width reversal skew \`W_w-(1/Delta-m/2)\` changes sign under reversal and vanishes for palindromes. This gives an exact residual coordinate for investigating R158's still-open maximum of \`H_w=floor((B-A)/Delta)\`. The sharp **upper** gap bound here is a different quantity from the needed small-gap and cut-ratio control.

## 5. Exact verification

Adjacent files: \`R159_check.py\`, \`R159_verification.json\`. The standalone checker uses Python arbitrary-precision integer and \`fractions.Fraction\` arithmetic, recomputes every factor inequality and prefix cut, and checks all signatures directly.

All **16,382 binary candidates of lengths 1 through 13** were covered, of which **1,142** are admitted and **1,116** are nonconstant admitted. Tests: **35,402** phase-count equalities at \`L=1..31\`, **1,116** reversal-signature and width identities, **148** palindrome specializations, and complete equality-word classifications for every \`m=2..13\`. Every assertion passed. The general results above rest on symbolic proofs; independent mathematical review is \`NOT_REVIEWED\`.

## 6. Next research questions

1. Classify the **minimum** possible gap \`Delta_w\` for every length, including denominator and Farey witnesses. R159C identifies the opposite extremum.
2. Prove or falsify R158's uniform envelope \`max_w floor((B-A)/Delta)=m*(m-3)/2\` for all m>=5, distinguishing reversal-odd skew from the palindromic term.
3. Combine the eventual width estimate with R158's exact residue certificates to close the even-length modular gap and the proposed universal permanent threshold.

Control: independent portable research under the frozen S23 observer. Prior exact Source lookup of \`RS-S23-AV\` found no canonical publication directory; this proof creates no CLAIM/Result/Review or Source activity authority.