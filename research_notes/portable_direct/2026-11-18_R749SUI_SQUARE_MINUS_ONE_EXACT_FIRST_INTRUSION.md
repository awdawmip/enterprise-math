# R749SUI — Exact first noncanonical two-Port threshold for every square-minus-one bound

2026-11-18 (Asia/Shanghai). **AUTHOR_EXACT_NOT_REVIEWED.**

## Scientific scope and immutable provenance

Continue R749SUH (Draft PR #2692, exact paper commit 03e7f84252e49636364754a5073ced7a68dca227) and R749SUF/SUG. Freeze the WBRC-T30–T32 scientific input at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Preserve all labeled Port orientations and the positive-rational stable feedback observer. This is a theorem about that observer's integer threshold spectrum, not a native X6 Cell/Link/Port event permission.

Fix an integer t>=4 and M=t²-1. The domain consists of *ordered labeled* integer quadruples (a,u,v,d), 1<=a,u,v,d<=M, ad-uv=1. Set tau=max(u,v)ad. Prior SUH identifies the canonical family, for j=1,...,M-2, of exactly two orientations (a,d)=(M-j,M-j), (u,v)=(M-j+1,M-j-1) or its swap; its strictly decreasing thresholds are F_j=(M-j+1)(M-j)². A configuration outside this family is called noncanonical.

## Theorem (sharp first intrusion, exact multiplicity and rank)

For **every** integer t>=4, the greatest noncanonical threshold equals

\[
\boxed{T_*(t^2-1)=M(M-t)^2,\qquad M=t^2-1.}
\]

Exactly two labeled noncanonical matrices attain it:

\[
\boxed{(a,u,v,d)=(M-t,M,t(t-2),M-t)}
\]

and the Port-reversed tuple (M-t,t(t-2),M,M-t). The number of canonical threshold *levels strictly above* the first noncanonical threshold is exactly

\[
\boxed{J(t^2-1)=\left\lfloor\frac{2t+1}{3}\right\rfloor.}
\]

Consequently the first noncanonical intrusion has exact distinct-threshold rank J+1, multiplicity two, with no tie to a canonical level.

### Proof, part A: exact maximization inside the q=1 defect family

Orient the Port entries as u=max(u,v). Use the *same* deficiency chart as SUH:
z=M-u, x=M-a, y=M-d, w=M-v, S=x+y+z and q=x+y-z-w. Put U=M-z. The determinant-one identity is

\[
(x-z)(y-z)=1+Uq,\qquad w=x+y-z-q.
\]

SUH proved q=0 precisely characterizes canonical configurations. If q>=1, set p=x-z, r=y-z. The two factors must both be positive: if both were negative then a,d>=U+1, contradicting ad=uv+1<=U²+1<(U+1)². Thus p,r>=1, with a=U-p>0, d=U-r>0.

For q=1, pr=U+1 and AM–GM gives p+r>=2sqrt(U+1), hence

\[
\tau=U(U-p)(U-r)
=U\{U^2-U(p+r)+(U+1)\}
\le U(U-\sqrt{U+1})^2.
\]

Every feasible q=1 configuration has U>=3. On [3,infinity), both U and U-sqrt(U+1) are positive and strictly increasing, so the right side increases with U. Since U<=M=t²-1, its maximum is M(M-t)². Equality requires U=M and p=r=t. Then z=0, x=y=t, w=2t-1, so a=d=M-t, u=M, v=M-2t+1=t(t-2). Both Port orientations are admissible for all t>=4, and those are the only equality cases in q=1.

### Proof, part B: all q<=-1 and q>=2 are strictly smaller

SUH's integer defect argument supplies these bounds on S for U>=2:

- If q>=2, then p,r>0 and pr>=2U+1; consequently S>=3z+2sqrt(2(M-z)+1)>=2sqrt(2M+1).
- If q<=-1, the factors x-z,y-z have opposite signs. Writing p=x-z>=1 and r=z-y>=1 (after exchanging a,d), one has r<=z and pr>=U-1. Hence S=3z+p-r>=2r-1+(M-1)/r>=2sqrt(2(M-1))-1.

Both inequalities are valid by monotonicity/AM–GM exactly as in the SUH deficiency lemma. The degenerate U=1 case has u=v=1, ad=2 and S=3M-4.

For M=t²-1 and t>=4, **all these configurations obey S>=5t/2**. For q>=2 this follows from 2sqrt(2t²-1)>5t/2. For q<=-1 and t>=5, it follows from

\[
\frac74t^2-5t-17\ge0.
\]

At t=4 the lower bound is 2sqrt(28)-1>9, so integer S>=10=5t/2. The U=1 case satisfies it directly.

AM–GM on a=M-x, d=M-y, u=M-z yields

\[
\tau=adu\le(M-S/3)^3\le(M-5t/6)^3.
\]

For every integer t>=4 this is *strictly* below the q=1 witness, since the exact difference is

\[
216\left[M(M-t)^2-(M-5t/6)^3\right]
=t\left(108t^4-234t^3-91t^2+234t+108\right)>0.
\]

Indeed, for t>=4, the first two terms of the quartic give t³(108t-234)>=198t³>91t², with 234t+108>0. Thus the global noncanonical maximum is the q=1 witness, with the two claimed labeled realizations.

### Proof, part C: exact rank

The canonical sequence F_j decreases strictly. Set J=floor((2t+1)/3). It suffices to prove F_J>W>F_{J+1}, where W=M(M-t)².

Writing t=3k+r with r=0,1,2 and integer k>=1, direct expansion gives the following strictly positive *exact integer polynomials* (all valid t>=4):

| r | F_J-W | W-F_(J+1) |
|---|---|---|
| 0 | (2k-1)(54k³+5k²-6k-1) | 135k⁴-64k³-34k²+10k+3 |
| 1 | k(27k³+28k²+4k-2) | (8k²+4k-1)(27k²+10k-4) |
| 2 | 189k⁴+424k³+322k²+94k+9 | (k+1)(54k³+62k²+15k+1) |

All factors are positive for k>=1; the first row's second expression is >0 since 135k⁴>64k³+34k² for k>=1. Therefore exactly F_1,...,F_J exceed W, while F_(J+1)<W. Together with parts A–B this establishes the exact first-intrusion rank and multiplicity. QED.

## Exact finite certificate

The accompanying dependency-free JavaScript verifier enumerates every labeled (a,u,v,d) in [1,M]^4 satisfying ad-uv=1 for each t=4,...,15 by solving v=(ad-1)/u in integer arithmetic. It independently checks the noncanonical maximum, its *two exact winner tuples*, and the rank J. Executed result: **PASS**; 212,532 admissible labeled matrices examined, including 210,152 noncanonical configurations. Every number in the checked range is exactly representable in IEEE-754 integer arithmetic. This exhaustive finite regression supplements the unrestricted t>=4 hand proof above.

## Consequence, scope and next questions

This sharpens SUH's T_*(M)=M³-2M^(5/2)+O(M²) along M=t²-1 to an *exact* formula and determines the previously unknown first-intrusion rank and multiplicity for this infinite sequence. It is not a universal classification for all M. A natural next number-theoretic question is to determine which defect q and which Farey/factor layer attains T_*(M) when M+1 is nonsquare, including the observed q=-1 winners at small bounds. In parallel, the P000 triadic closure, native X6 resource guard and causal-time admission remain separate correspondence questions; keep every Port-source and orientation label until a scope-typed safe observer quotient has been proved.

**Evidence:** R749SUH exact immutable paper as above; frozen WBRC-T30–T32 input at a72226e2430ffa4786321ac86e7f0c599d5f0389; this paper's accompanying JS certificate and JSON output. No independent review or formal checker is asserted.