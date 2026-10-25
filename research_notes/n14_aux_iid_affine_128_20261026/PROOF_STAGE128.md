# N14 auxiliary iid Stage128: exact full-real affine optimum, author-side proof

**Evidence grade:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two distinct author-side exact calculations passed locally. No independent Driver review, native CLAIM, Result freeze, or P000/X6/Heartbeat transfer is claimed.

## Theorem

Finite ternary iid observation model: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), max stopping time N=14. Arbitrary randomized tests on all *literal ordered histories* are admitted. Write eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=minimum max(tP,tQ) subject to eP,eQ<=alpha.

From Stage127 author-proved endpoint
alpha127=18340838418534259499/52808422392537808896,
V127=335278957759082895695/26404211196268904448,
take K128=7794/11, L128=7256/11, S128=15050/11, eta128=1181640625/8393672687616.

For **every real** 0<=delta<=eta128,

\[
\boxed{V_{14}(\alpha_{127}+\delta)=V_{127}-\frac{15050}{11}\delta.}
\]

Exact endpoint:

\[
\boxed{\alpha_{128}=\frac{18348272658534259499}{52808422392537808896}},
\quad
\boxed{V_{128}=\frac{330193261759082895695}{26404211196268904448}}.
\]

The same affine supporting line cannot coincide with V14 at any alpha>alpha128 (right-sharp support; not global infeasibility).

## Dual lower bound for the full ordered-history class

At count s=(n,a,b), a=#symbol0,b=#symbol1, each ordered prefix has likelihood ratio r=Q(prefix)/P(prefix)=2^(a+b)/3^a. Set terminal costs: choose P, K128*r; choose Q, L128; continue, 1+sum_j P_j H(child_j) if n<14. Backward Fraction Bellman recursion gives **680** states, **1238 strictly positive nonchosen action gaps**, **zero negative gaps**, min strict gap=71/8748, exactly two ties:

B=(11,0,1), Q/continue; D=(12,2,0), P/continue.

Root dual:
H(0)=5444247642339796165/11158995049906176.

Same-count literal prefixes have the same conditional iid suffix distribution and Q/P ratio, so the Bellman bound is valid for **unrestricted ordered-prefix randomized policies**. For every such test:

\[
H(0)\le t_P+L_{128}e_P+K_{128}e_Q
\le\max(t_P,t_Q)+(K_{128}+L_{128})\alpha.
\]

Hence V14(alpha)>=H(0)-S128*alpha.

## Literal ordered BRC carriers and four moments

Keep ordered positive P/Q branch weights, multiplicity and transition provenance before the four-observer iid quotient. Under the strict Bellman actions and tie continuations, exact first-hit ordered-history masses are:

B: 11 words; P=107421875/1451188224, Q=107421875/725594112.
D: 66 words; P=107421875/644972544, Q=107421875/1451188224.

Their descendant cones cannot intersect: B at depth 11 already has one symbol1, D at depth12 has zero symbol1; this count never decreases. D cannot precede B by depth. Thus no mixed randomization term.

Let w be the Q-stop probability at B, u the P-stop probability at D, continuing otherwise. Every other reached action is the unique Bellman minimizer. For **every real** w,u in [0,1], observer M=(eP,eQ,tP,tQ) is exactly

\[
M(w,u)=M_{00}+w\,d_B+u\,d_D,
\]

where

M00=(
1216989254277297853/3505953353861431296,
223063082271829/641959232274432,
5568463069566649363/438244169232678912,
645856363810993/53496602689536);

dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128);

dD=(
-107421875/371504185344,
107421875/208971104256,
-2685546875/15479341056,
-1396484375/17414258688).

These values and M11=M00+dB+dD are confirmed by two differently written author programs: bottom-up rational Bellman/moment recurrence, and top-down literal ordered-history DFS with integer P/Q branch numerators. Negative entries in signed moment **differences** do not make positive branch mass a signed amplitude.

## Full-real optimal primal family

Exact error balance eP=eQ requires

\[
\boxed{w(u)=3697777109752777/40719360000000000+(50/241)u,\quad0\le u\le1.}
\]

All probabilities are valid: 0<w(0)<w(1)=12145777109752777/40719360000000000<1. Exact substitution yields eP=eQ=alpha127+eta128*u and tP=V127-S128*eta128*u. The values of tP-tQ at u=0 and u=1 are, respectively,

50749829511513535531/79212633588806713344 >0,
44666593671513535531/79212633588806713344 >0.

Affineness implies tP>tQ for every real u in [0,1]; this is a true continuous family, not rational-grid interpolation. All used actions are dual Bellman minima, so every policy attains the universal bound and establishes the theorem.

## Right-sharpness

Finite-horizon randomized behavioral policies form a compact space, so every feasible optimal value is attained. If the *same* supporting affine line were attained at alpha>alpha128, strict positivity K,L forces both error bounds to bind (eP=eQ=alpha), every positively reached action to have zero Bellman gap, and max(tP,tQ)=tP. Exhaustive gaps leave only B and D as variable actions. For all prefixes of the same count the ratio Q/P and conditional suffix outcomes coincide, so all possible prefix-specific tie coins can be mass-averaged into effective (w,u) in [0,1]^2 without changing the four observers. The cones are disjoint. Error balance then forces the stated w(u), so alpha=alpha127+eta128*u<=alpha128, contradiction.

## Evidence and next unit

Executed locally: primary exact Fraction checker PASS; independently implemented ordered integer-weight DFS PASS, four corner visit totals 00/01/10/11 = 789841/789445/789709/789313, all moments/first-hit weights agree. Github code publication is storage, not claimed Github-side execution or independent Research Driver review.

Stage129 **dual candidate only**: K129=14874456845932398/22082607358633, L129=13896162810492616/22082607358633; B Q/continue and F=(2,0,2) Q/continue tie; 1238 positive gaps, smallest 2569217935604737/48294662293330371. Its primal real interval remains open.

Sources frozen: GLOBAL_KNOWLEDGE_V1 main@8c38dfefccb02323723a85f214d31bcf844bbdec, P000 locked original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, prior Stage127 proof Git blob 3f31a6e1d02797456398fa5628f885451e1630e6. Authenticated Github actor awdawmip; researcher local identity EM-DIRECT-5A72C1. Native inventory CONTROL_QUOTA, session-start STATIC_READONLY_SCOPE_DENIED/operation_sent=false: active owner/CLAIM/Result/Driver review **unverified**. This theorem is only for an external iid finite auxiliary model.
