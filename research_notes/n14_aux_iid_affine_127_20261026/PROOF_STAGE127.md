# R1/N14 Stage127 — exact real-interval optimum and right-sharp support

**Evidence grade: AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF.** Two separately written author implementations have passed local exact-arithmetic checks. This is a finite iid **external auxiliary model**, not a P000 native six-dimensional Cell-space theorem, independent Research Driver review, formal Result, Working Truth or Foundation acceptance.

## Statement

Let N=14 and P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) on the ordered ternary observation alphabet. A sequential randomized policy may use *all ordered prefixes*, stop by step 14, and declare P or Q. Put eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau); V14(alpha) is the minimum max(tP,tQ) subject to eP,eQ<=alpha.

From the author-proved Stage126 endpoint
alpha126=18340838011402083499/52808422392537808896,
V126=335279238082246223695/26404211196268904448,
this stage proves **for every real** 0<=delta<=eta127,
\[
\boxed{V_{14}(\alpha_{126}+\delta)=V_{126}-\frac{15920216}{11561}\delta},
\qquad
\eta_{127}=\frac{3180720125}{412565799941701632}.
\]
The new exact endpoint is
\[
\boxed{\alpha_{127}=\frac{18340838418534259499}{52808422392537808896},
\quad V_{127}=\frac{335278957759082895695}{26404211196268904448}}.
\]
The *same support line* is right-sharp at alpha127: it cannot equal the value function for any alpha>alpha127. This is not global infeasibility beyond that threshold.

## Complete dual Bellman lower bound

At count state (n,a,b), a=#symbol0 and b=#symbol1, each literal prefix has identical likelihood ratio r=Q(prefix)/P(prefix)=2^(a+b)/3^a. Fix K=8246448/11561, L=7673768/11561, S=K+L=15920216/11561. With H at the terminal horizon, the action costs are declaring P: K*r; declaring Q: L; continuing when n<14: 1+sum_j P_j H(child_j). Exact rational backwards recurrence covers 680 count states. Exactly 1238 nonselected action gaps are strictly positive, zero negative, min positive 71/9459. There are precisely two ties:
B=(11,0,1), declare Q/continue; C=(11,6,2), declare P/continue.
Root H=207290753323284460123369/422211736708250075136.
The conditional iid suffix and all four declared observables depend only on counts, so this dual bound applies to the *unrestricted literal ordered-history policy class*, not merely count-only tests. For any policy,
\[
H(0)\le t_P+L e_P+K e_Q\le\max(t_P,t_Q)+(K+L)\alpha.
\]
Thus V14(alpha)>=H(0)-S alpha.

## Exact ordered-branch first-hits and observer moments

BRC usage: positive rational P/Q branch carriers with **literal ordered prefix identity**, transition provenance and multiplicity are retained until the specific iid four-observer quotient is proven safe. The independent integer-weight ordered-history DFS finds actual first-hit counts and masses (excluding prefixes stopped earlier by unique optimal decisions):

| tie | literal first-hit words | P mass | Q mass |
|---|---:|---:|---:|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| C=(11,6,2) | 2201 | 275125/32614907904 | 275125/92876046336 |

B,C are distinct count vectors at the *same depth 11*, so no path visits both. Their ordered-prefix descendant cones are disjoint, eliminating all wu cross terms. Conditional iid suffixes and same-count P/Q mass ratios permit mass-weighted averaging of arbitrary prefix-specific randomization for precisely these four observables.

Let w=probability of stopping/declaration Q at B (else continue), u=probability of stopping/declaration P at C (else continue), all other actions the strict unique Bellman minimizers. Define M=(eP,eQ,tP,tQ). For all w,u in the **entire real square** [0,1]^2:
M(w,u)=M00+w*dB+u*dC, where
M00=(
1216989348409665853/3505953353861431296,
24784784228981/71328803586048,
5568467048798569363/438244169232678912,
645856546493993/53496602689536);
dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128);
dC=(
-3026375/112717121716224,
3026375/80244904034304,
-42644375/4696546738176,
-22835375/6687075336192).
Both an exact bottom-up moment recurrence and an independent top-down ordered integer-prefix DFS check all four corners and M11=M00+dB+dC exactly.

## Full-real primal construction

Setting eP=eQ gives the unique compensation law
\[
\boxed{w(u)=\frac{1232366013208259}{13573120000000000}+
\frac{3858353}{231360000000}u,\quad 0\le u\le1.}
\]
Both coefficients are positive and
0<w(0)<w(1)=3697777109752777/40719360000000000<1;
hence all real u between 0 and 1 yield legal randomized policies.
Exact substitution gives
eP=eQ=alpha126+eta127*u and tP=V126-S*eta127*u.
At the two endpoints, exact time gaps are
tP(0)-tQ(0)=16916724390710645177/26404211196268904448 >0,
tP(1)-tQ(1)=50749829511513535531/79212633588806713344 >0.
Affineness keeps tP>tQ for **every real** u in the interval. As every randomized action minimizes the dual Bellman cost, each such policy attains H(0)-S alpha. This proves equality with the lower bound throughout the stated interval.

## Right endpoint is sharp

At u=1 the new C P-stop randomization saturates, yet 0<w(1)<1 at B. Suppose equality with this *same affine support* occurred at some alpha>alpha127. An optimal policy exists in the compact finite-horizon behavioral-policy space. Since K,L>0, equality forces eP=eQ=alpha and the chosen actions at all positively reached histories to be Bellman minimizers. The exhaustive gap enumeration leaves just B,C as randomized choices. Their separate path cones and same-count iid laws reduce any history-specific tie coins to exact effective w,u in [0,1], with the same four-observer M. The equality eP=eQ forces w=w(u) above. Then alpha=alpha126+eta127*u<=alpha127, contradiction. No claim is made about the next distinct dual face.

## Checks, scope, continuation

VERIFY_STAGE127.py: exact bottom-up 680-state Bellman, 1238 positive gap enumeration, four-corner rational observer vectors, linear compensation and endpoint sharpness premises: **PASS locally**.
INDEPENDENT_ORDERED_STAGE127.py: separately written recursive Bellman plus literal ordered-prefix integer-weight DFS using P numerators (3,1,20)/24 and Q numerators (1,1,10)/12: **PASS locally**. Four-corner node visits 00/10/01/11 are 809650/809518/789841/789709; first-hit probabilities and every observer value agree. These are two author implementations, not independent formal Driver review. GitHub file storage/readback does not execute scripts remotely.

SCAN_STAGE128.py: **DUAL_CANDIDATE_ONLY** with K128=7794/11, L128=7256/11, ties B=(11,0,1) Q/continue and D=(12,2,0) P/continue, 1238 strictly positive gaps, minimum 71/8748, no primal interval proved. Next independent unit: exact real ordered first-hit B/D masses, legal affine error compensation, tP>tQ, right-sharpness.

Read snapshots: GLOBAL_KNOWLEDGE_V1 main@8c38dfefccb02323723a85f214d31bcf844bbdec; P000 original global blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; EM main@7f1913a4940bb97898f1c9c4e4cf542db3221eee; Stage126 proof and Stage127 task packet at that EM snapshot. Authenticated GitHub login awdawmip. Native control tasks: CONTROL_QUOTA. Native session registration: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active native owner and CLAIM unknown; only author-side research source publication is asserted.