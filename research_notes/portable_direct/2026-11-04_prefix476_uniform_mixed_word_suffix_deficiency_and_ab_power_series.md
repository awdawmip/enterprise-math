# PREFIX-476: Uniform mixed-gate KMP suffix deficiency and exact ab^(k-1) BRC series

Date: 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. This is author-side portable research, not a native Result or Review. Continuation of PREFIX-475. Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Current normative rules were read separately.

## Model and inherited law

In a native X6 signed chart use x=+E1, ten ordinary signed directions a,A,b,B,c,C,d,D,e,E (axes E2 through E6). Any ordinary step is legal; x is legal as the first step or immediately after the ordinary word w of length k>=1. For a length-n legal path, retain the positive-BRC base support observation f=(s,y1,...,y5,V,W): s=#x, signed displacements y_i and cancellation numbers p_i=min(c_{i,+},c_{i,-}), with V=p2+2p4+p5 and W=p3+p5. Count different f values, not ordered paths or signed amplitudes. Let S_n be the base f-support, B_n=|S_n|, S_(n,j) the support with KMP longest-suffix/prefix state j (0<=j<=k), and F_n=sum_j |S_(n,j)|. Put B_m=0 for m<0.

The inherited exact PREFIX-470/471 base law, used at precisely its declared scope, is

G_k(z)=sum_(n>=0) B_n z^n=(1+2z^2)(1+z)^2(1+z-z^(k+1))/((1-z)^8(1-z^(k+1))),

B_n=n^8/[3360(k+1)]+O_k(n^7) for fixed k.

For a fixed ordinary suffix u, appending u induces an injective base-observer map T_u. On each paired axis let u have total r_i and displacement d_i: then y'_i=y_i+d_i and p'_i-p_i=(r_i+|y_i|-|y'_i|)/2. Consequently V',W' are determined by f and u, and inversion uses known u and new y. This does not retain full path provenance.

## Theorem A: arbitrary mixed signs and self-overlaps have uniformly bounded state-0 holes

Let a be the first symbol of any fixed ordinary gate word w of length k. For every n>=0,

0 <= h_w(n):=|S_n \ S_(n,0)| <= 2k^9.

Proof. Fix any realizable full count vector. If it has s>=2 occurrences of x, disjoint immediately preceding w-blocks before x after the first one imply that the ordinary counts contain (s-1) copies of w. The explicit legal rearrangement x (wx)^(s-2) [all ordinary residual letters] w x ends in KMP state 0 with the same counts and f. For s=0 or 1, if an ordinary direction c != a occurs at least k times, place c^k last (and, when s=1, place x first). The final suffix c^k has no nonempty suffix equal to a prefix of w, because every prefix of w starts a. Thus a missing q0 observation can have a Parikh representative only with s in {0,1} and each of the other nine ordinary counts in {0,...,k-1}. At fixed n the remaining count of a is uniquely determined; at most 2k^9 such count vectors and therefore at most 2k^9 distinct f exist. QED.

This resolves the PREFIX-475 growth question for fixed w: q0 deficiency cannot grow with path length n, including genuinely overlapping gates such as ababa and mixed-sign gates such as aAa. The bound may be much sharper for a selected word.

## Theorem B: every KMP suffix differs from fixed-prefix padding by uniformly few observations

Write u_j for the length-j prefix of w. For n>=j and 1<=j<k,

T_(u_j)(S_(n-j,0)) subset S_(n,j) subset T_(u_j)(S_(n-j)).

Any state-j word ends in u_j, giving the second inclusion by deleting the last j ordinary letters. Conversely, append u_j to a KMP state-0 word; an unexpectedly longer matching suffix would require a nonempty boundary suffix equal to an initial prefix of w, contradicting state 0. No whole gate occurs inside u_j because j<k. Thus the first inclusion holds. Full-match paths satisfy S_(n,k)=T_w(S_(n-k)) exactly, since their last k letters are w and any legal prefix may append w. Each T is injective as shown above.

Therefore for j=0,...,k-1, 0<=B_(n-j)-|S_(n,j)|<=2k^9, while |S_(n,k)|=B_(n-k). It follows for all n>=0 that

F_n=sum_(j=0)^k B_(n-j) - D_w(n),  0<=D_w(n)<=2k^10,

and, for fixed word w, F_n=n^8/3360+O_w(n^7). The leading full-history support coefficient is universal across fixed gate words in this model. The same assertion is not made for ordered multiplicity, provenance, mass or other future observers.

## Theorem C: fully explicit formulas for w=a b^(k-1)

Assume a,b are distinct ordinary signed native directions, k>=1, with k=1 understood as w=a. For this word, appending a always sets the KMP state to 1, regardless of previous state; appending the subsequent b^(j-1) sets state j for every 1<=j<=k. Thus |S_(n,j)|=B_(n-j) for every j>=1, including full match.

For n>=1, precisely the following f fibers have no q0 representative:
(1) s=0, ordinary counts a=n-r>=1 and b=r for 0<=r<=k-1;
(2) s=1, ordinary counts a=n-1-r>=1 and b=r for 0<=r<=k-2;
all other ordinary counts zero.

Indeed, if an ordinary symbol outside {a,b} occurs, place it last; s>=2 admits the ending-x construction. For s=0 and only a,b, a last leaves state 1, while b last has a suffix a b^t with 1<=t<=k-1 unless at least k b's are available, when b^k last yields q0. For s=1, if at least one a and k-1 b's are available, use an ending w x. Otherwise the unique x must be first and the same nonzero-suffix obstruction applies. If no a exists, b-only words finish in q0. The listed exceptional f have n=s+sum|y_i|, so every cancellation p_i=0 and no alternative count vector maps to the same f; they are genuinely distinct holes. QED.

Consequently h_k(0)=0 and for every n>=1,

h_k(n)=min(k,n)+min(k-1,n-1), hence h_k(n)=2k-1 for n>=k.

Writing H_k(z)=sum_n h_k(n)z^n, one has

H_k(z)=(z+z^2-2z^(k+1))/(1-z)^2,

F_k(z)=(1+z+...+z^k)G_k(z)-H_k(z).

The formulas include all small-n boundary terms. This gives an explicit mixed-letter family whose correction can grow linearly in gate length k, but stays bounded in path length n.

For Boolean future legality and final f under all continuations of length <=H, the shortest additional x from KMP q=j>=1 has length k-j+1; from q0 length k+1. For 1<=H<k the states q<=k-H form one observational class, while q>k-H are pairwise distinguished. Every q0-hole f has a q1 representative (put the available a last), so S_(n,0) union S_(n,1)=S_n. Hence for all n>=0,

N_k(n,0)=B_n,
N_k(n,H)=B_n+sum_(j=k-H+1)^k B_(n-j)  for 1<=H<k,
N_k(n,H)=F_n for H>=k.

The exact fixed-width state-code lower bound is ceil(log2 N_k(n,H)) bits. The fast ranking implementation for general mixed words and the full source-provenance carrier remain separate questions.

## Executed exact certificate

The Python 3 stdlib companion source performs independent (Parikh count vector,KMP state) dynamic-programming reachability, computes the exact positive-BRC observer, compares base G_k coefficients by integer-binomial convolution, checks the q0 candidate theorem and both prefix-padding inclusions, and verifies every full-match set. For w=a,ab,abb,abbb,abbbb it also checks the explicit holes, all suffix support sizes, and every future quotient H=0,...,k+1 against direct support unions. Tested words: a,aa,ab,aba,aab,abb,abab,abbb,abbbb,aAa,ababa; every n=0,...,7. All checks pass with exact integer/set arithmetic; no sampling or floating point.

At n=7: aa B=15863 q0 holes=1, D=2; ab B=15863 holes=3,D=3; aba B=15697 holes=3,D=3; aab B=15697 holes=3,D=5; abb B=15697 holes=5,D=5; abab B=15652 holes=4,D=4; abbb B=15652 holes=7,D=7; abbbb B=15643 holes=9,D=9; aAa B=15697 holes=3,D=3; ababa B=15643 holes=4,D=4. The complete locally executed raw log SHA-256 is 36db03b2b4120f6cc955b3b92091fb1e355715057c192bb71243bce0c5e54f78. The GitHub accompanying execution excerpt records the actual n=7 rows and pass checks; full raw evidence and source also exist in the same-run local evidence bundle.

A useful contrast: PREFIX-475's pure-run a^k family has <=2 q0 holes per n, whereas the mixed-letter word abbbb has exactly 9 at n=7. The general boundedness result supersedes extending the specific pure-run numerical bound to all words; no earlier exact pure-run result is changed.

## Related literature and next frontier

Anthony Widjaja To, Parikh Images of Regular Languages: Complexity and Applications (2010), https://arxiv.org/abs/1002.1464, and Kevin Woods, Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials (Journal of Symbolic Logic 80, 2015, 433-449), DOI 10.1017/jsl.2015.4, provide established related theory. Neither is used as a proof of the explicit X6 counting laws.

Next PREFIX-477: seek an effective pattern-sensitive correction for self-overlapping mixed words; determine whether D_w(n) eventually stabilizes or becomes periodic, using exact semilinear predicates under this f observer. Then develop bounded-exception rank/unrank over PREFIX-472 and account for preprocessing, bit complexity and source-sensitive outputs.

BRC reuse: COMPOSE_APPLIED; signed native X6 paths and exact positive valuation f; the KMP state is path history, not a new spatial axis. Runtime control read returned CONTROL_QUOTA; native research session returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. This note does not assert active TASK owner, CLAIM, independent review or admission.
