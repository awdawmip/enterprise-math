# PREFIX-478 — Exact stabilization constants for three mixed BRC/KMP gates

Date: 2026-11-04 (Asia/Shanghai).
Scientific status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Source predecessor: PREFIX-477@161bf4917ec852f2dcde242e014e77c224cf0449.
Current applicable account rules independently read at awdawmip/chatgpt-global-knowledge@669e857abe5c381e212f3ab16a333f9f9b1dc1f9.

## Model

Work in the frozen native six-axis X6 positive BRC support slice, not in the full physical event state. The legal alphabet is x=+E1 and the ten signed ordinary directions aAbBcCdDeE on axes E2..E6. All ordinary moves are legal; x is legal initially or immediately after the gate word w of length k. For paths of length n, f=(s,y2..y6,V,W) is the base observation: s=#x, y_i are signed displacements, p_i are same-axis opposite-direction cancellation counts; V=p3+2p5+p6, W=p4+p6. KMP state q in 0..k is the maximal suffix matching a prefix of w since the last x; x resets q=0.

Define S_nq=base observations achievable with KMP q, S_n=union_q S_nq, B_n=|S_n|, F_n=sum_q |S_nq|, B_m=0 for m<0. The exact inherited base generating function is G_k(z)=(1+2z^2)(1+z)^2(1+z-z^(k+1))/((1-z)^8(1-z^(k+1))). For a fixed ordinary suffix u_j=w[:j], its observer update T_(u_j) is injective. From PREFIX-476, for 0<=j<k, T_(u_j)(S_(n-j,0)) subset S_nj subset T_(u_j)(S_(n-j)); S_nk=T_w(S_(n-k)). Thus delta_j(n)=B_(n-j)-|S_nj|, D_w(n)=sum_(j=0)^(k-1) delta_j(n), F_n=sum_(j=0)^k B_(n-j)-D_w(n).

## Theorem: exact zero-state holes

For the words aab, aAa (k=3) and ababa (k=5), write beta=b, A, b respectively. Define U_(s,r)(m) as the base observer of the Parikh count profile having s copies of x, r copies of beta, m-s-r copies of a, and all other ordinary counts zero. Let R_m=S_m minus S_(m,0).

For all m>=2k+2, exactly:

aab: R_m = {U_(0,0)(m),U_(0,1)(m),U_(1,0)(m)}, cardinality 3.
aAa: R_m = {U_(0,0)(m),U_(0,1)(m),U_(1,0)(m)}, cardinality 3.
ababa: R_m = {U_(0,0)(m),U_(0,1)(m),U_(1,0)(m),U_(1,1)(m)}, cardinality 4.

Proof. The proven PREFIX-476 rearrangement lemma states that every count representative of a zero-state hole has s<=1 and each letter other than a occurs fewer than k times. For these three words, if an ordinary letter other than a or beta appears, rearrange it to the final position, with x initially if needed, yielding KMP zero. If two beta letters appear, end in beta-beta, which is not a suffix equal to any nonempty prefix of any of these three words, again KMP zero. Thus every hole representative has only a, at most one beta, and at most one x. Since m>=2k+2, ample a letters exist.

With no beta, every path is all-a, optionally with x initially, and ends in a nonzero prefix state. With one beta and s=0, ending in a has nonzero state, and ending in beta produces respectively q=3 for aab, q=2 for aAa, q=2 for ababa. With one beta and s=1, aab and aAa may end in the legal suffix w x, realizing q=0. For ababa, one b cannot authorize noninitial x, so x is initial and all such paths end in nonzero suffix state. The displayed count profiles give genuine, pairwise distinct observer holes: in all but one case they have no cancellation and Parikh is uniquely recovered from n,s,y. For aAa with one A, the total cancellation is 1 and (V,W)=(1,0), which uniquely forces the a/A-axis pair cancellation and excludes a different full-X6 Parikh fiber. This proves equality. QED.

## Theorem: exact correction constants and shorter proven cutoffs

For n>=3k+1, the full suffix correction vectors are:

aab: (delta_0,delta_1,delta_2)=(3,2,0), so
F_n(aab)=B_n(3)+B_(n-1)(3)+B_(n-2)(3)+B_(n-3)(3)-5, n>=10.

aAa: (3,0,0), so the same four B-values minus 3, n>=10.

ababa: (4,0,0,0,0), so
F_n(ababa)=sum_(j=0)^5 B_(n-j)(5)-4, n>=16.

Proof. By the two-sided injective padding inclusions, delta_j for j>0 counts exactly the source holes f in R_(n-j) whose T_(u_j)(f) cannot realize q=j. Because n-j>=2k+2, only the three or four explicit source holes need be tested. For aab, j=1: padding a after either a-only source (with or without initial x) produces an all-a tail with suffix state 2 rather than 1, and their no-cancellation profiles admit no alternate ordering. Padding a after the unique b-containing source admits terminal state1 via ending ba. Hence delta_1=2. For j=2, place any extra b earlier and end in aa, giving q=2 for all three sources. For aAa, padding a admits q1 if an A is placed early followed by at least two a; padding aA admits q2 since the full gate ends in a; the two j>0 defects vanish. For ababa, every padded prefix u_j, 1<=j<=4, can realize exactly q=j by placing any extra b early, allowing at least two a letters before the appended u_j; place x initially if present. There is no longer crossing suffix because of this buffer, and the j4 suffix ends in b while the full gate ends in a. Hence the four j>0 defects vanish. In each case delta_0=|R_n|. QED.

The previous all-word 15k cutoff was (45,45,75) for these words. The proved sufficient cutoff is now (10,10,16). Whether any smaller bound is optimal is a separate finite-boundary question.

## Exact finite-exception joint-state codec

Let the existing PREFIX-472 base encoder/decoder rank all f in S_m without a complete state dictionary. For n above the proved cutoff:

aab: S_n0=S_n minus R_n; S_n1=T_a(S_(n-1) minus {U_(0,0)(n-1),U_(1,0)(n-1)}); S_n2=T_aa(S_(n-2)); S_n3=T_aab(S_(n-3)).
aAa: S_n0=S_n minus R_n; S_nj=T_(w[:j])(S_(n-j)) for j=1,2,3.
ababa: S_n0=S_n minus R_n; S_nj=T_(w[:j])(S_(n-j)) for j=1,...,5.

Rank a joint state by its q block, inverting T_(u_j) when j>0, applying base_rank and subtracting the number of excluded base ranks preceding it (at most 4). Unrank by selecting a q block, inserting skipped excluded base ranks, base_unrank and reapplying the fixed T. This constructs a bijection to [0,F_n-1] and optimal ceil(log2 F_n) fixed-width code. For these three *fixed* words it preserves the inherited O(log(n+1)) exact-arithmetic search-operation bound. Small n below the cutoff require separate finite boundary handling. Ordered path multiplicity, amplitudes and provenance are not quotiented by this support-only theorem.

## Executed certificate

The companion Python 3 source is the actual executed standard-library program; log is its exact output. It enumerates **all 11-direction X6 Parikh/KMP states** for n=0,...,8 in each of the three gate models, checks exact base-series coefficients, full-suffix supports, and all defect/full-history identities. At n=8 the triples (B,F,delta-vector) are:
aab (33295,58496,(3,2,0));
aAa (33295,58498,(3,0,0));
ababa (33085,59429,(4,0,0,0,0)).
A second independently generated *restricted* a,beta,x Parikh/KMP DP, with s<=1, checks each possible zero-state hole and every padded candidate for every n=10..75 (k=3) or n=16..75 (k=5). This second loop is not a full-X6 large-n enumeration. All executed checks passed (ALL_CHECKS_PASS). From the proved formula, F_10(aab)=238858, F_10(aAa)=238860 and F_16(ababa)=5973939.

External context checked 2026-11-04: Anthony Widjaja To, Parikh Images of Regular Languages: Complexity and Applications (2010), https://arxiv.org/abs/1002.1464; Kevin Woods, Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials, J. Symbolic Logic 80(2), 433–449 (2015), DOI:10.1017/jsl.2015.4. The particular constants here arise from the above model-specific construction, not from those articles.

## Boundary, authority, continuation

The live GitHub connector authenticates awdawmip with enterprise-math push/admin. Native task listing failed CONTROL_QUOTA; a current native session attempt returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Active Owner, native Researcher-ID and formal CLAIM are not verified. This author-side Source research material is neither a native Result nor a Review or Admission. No P000/worldview/scientific-pin or native protected state changes are requested or made.

PREFIX-479: characterize which mixed words have constant-size hole families based on the beta-letter threshold for a legal final x and the KMP prefix overlap. Then implement and round-trip a reusable joint rank/unrank algorithm against independently enumerated finite full-X6 data. Continue the separate arbitrary-order X6 moment-rank route when appropriate.
