# R1/N14 Stage129 — exact full-real affine optimum, right-sharp support

**Evidence grade:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two separately written author-side exact arithmetic implementations passed locally. No independent Research Driver review, native session/CLAIM or Result. This is an external iid finite auxiliary model, not a P000 six-dimensional Cell-space or physics result.

## Theorem and scope

Let N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Randomized policies on every literal ordered ternary history must stop by 14 and declare P or Q. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha) as minimum max(tP,tQ) subject to both errors <=alpha.

At the author-proved Stage128 endpoint
alpha128=18348272658534259499/52808422392537808896,
V128=330193261759082895695/26404211196268904448,

for **every real** 0<=delta<=22082607358633/11735204976119513088 we prove

\[
\boxed{V_{14}(\alpha_{128}+\delta)=V_{128}-\frac{28770619656425014}{22082607358633}\delta.}
\]

The new endpoint is

\[
\boxed{\alpha_{129}=\frac{36696744060534746695}{105616844785075617792}},\qquad
\boxed{V_{129}=\frac{660257055729711878827}{52808422392537808896}}.
\]

The *same* affine support cannot hold at any alpha>alpha129; no global infeasibility beyond this point is claimed.

## Exact dual bound

Set K=14874456845932398/22082607358633, L=13896162810492616/22082607358633, S=K+L=28770619656425014/22082607358633. At count state (n,a,b), a is the number of zeros and b the number of ones, so Q(prefix)/P(prefix)=2^(a+b)/3^a. P-weighted Bellman costs for declare P, declare Q and continue are K*r, L and 1+sum_j P_j H(child_j), respectively (continuation omitted at n=14). Fraction backward induction over all 680 count states finds exactly 1238 strictly positive nonchosen action gaps, no negatives, least positive 2569217935604737/48294662293330371. Exactly two ties:

B=(11,0,1), announce Q / continue;
F=(2,0,2), announce Q / continue.

The root dual H(0)=2605243537319692868583967737169/5600447868272894163950764032. The conditional iid suffix is count-sufficient for these four observers, hence this Bellman bound also applies to the unrestricted literal ordered-history policy class:

\[
H(0)\le t_P+L e_P+K e_Q \le \max(t_P,t_Q)+S\alpha.
\]

## BRC branch provenance and exact affine moments

Keep ordered branch identity and positive rational P/Q prefix mass until the four-observer quotient is justified. Separately implemented literal integer-weight prefix DFS obtains true first-hit masses under the tie-continuation policy:

B: 11 ordered first hits; P=107421875/1451188224; Q=107421875/725594112.
F: 1 ordered first hit; P=1/576; Q=1/144.

F already contains two symbol-1 observations whereas B contains only one, so F cannot precede B on the same path; B at depth11 cannot precede F at depth2. Their complete descendant cones are disjoint and cross terms are identically zero.

Let w=probability of stopping Q at B, v=probability of stopping Q at F. Else take the unique dual minimizers. For all real w,v in [0,1],

M(w,v)=(eP,eQ,tP,tQ)=M00+w*dB+v*dF,

M00=(1215975494277297853/3505953353861431296,
223393082271829/641959232274432,
5492431069566649363/438244169232678912,
641566363810993/53496602689536);

dB=(4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128);

dF=(5582837024069/259700248434180096,
-2161086713/142657607172096,
-11988973910605/3606947894919168,
-1108405160653/106993205379072).

A bottom-up exact Bellman/moment implementation and an independently written top-down ordered integer-weight DFS agree on all four corners and the identity M11=M00+dB+dF.

## Entire-real primal attainment and right endpoint sharpness

Error equality eP=eQ gives the unique relation

\[
\boxed{w(v)=12145777109752777/40719360000000000-(256958333767239/27146240000000000)v},\quad0\le v\le1.
\]

Both endpoints are legal: 0<w(1)=23520679218203837/81438720000000000<w(0)<1. At each real v, eP=eQ=alpha128+eta129*v and tP=V128-S*eta129*v, with eta129=22082607358633/11735204976119513088. At v=0 and v=1 respectively,

tP-tQ=44666593671513535531/79212633588806713344 >0,
tP-tQ=90328531682230099607/158425267177613426688 >0.

Affineness preserves tP>tQ throughout. Each reached action is a Bellman minimizer. Thus the above randomized tests attain the universal dual bound for the *whole real interval*.

For right-sharpness, if the same affine line were equal to V14 at alpha>alpha129, compactness of finite-horizon behavioral randomized policies gives a minimizer. Positivity K,L forces both error constraints to bind and dual equality forces all reached decisions to have zero Bellman gap. The exhaustive gap enumeration leaves only B and F available for randomization; same-count iid suffix observers and P/Q ratio permit mass-weighting arbitrary history-dependent tie coins into effective w,v in [0,1] without altering the four observer values. Disjoint cones give the exact affine law above, so alpha=alpha128+eta129*v<=alpha129, a contradiction. It is the *support line*, not the feasible region, that terminates.

## Checks, provenance and next question

Local primary Fraction verification: PASS; independent full literal ordered integer-weight DFS: PASS. Prefix node visits for 00/10/01/11=789445/789313/775522/775390. Both are author checks, not independent Research Driver review. GitHub storage and source readback do not mean remote program execution. Complete local executed scripts and outputs are retained in the run evidence archive.

Stage130 is presently **DUAL_CANDIDATE_ONLY**. Along dK=-1,dL=-112/129, with F=Q after its saturation and B Q/continue tied, the first new gap closure occurs at terminal G=(14,7,4) (declare Q/P). Exact candidate K130=522693/802, L130=244736/401, root=52838467869186182216021/117157274574869495808; exactly two ties B Q/C and G P/Q, 1238 strictly positive gaps, least 517/28872. No Stage130 primal interval is yet proved.

Source: GLOBAL_KNOWLEDGE_V1 main@363cc21deb56c429a3d1304e62bde6fd4c35452e; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math fixed read main@939439efe36bd219e21840887fdf97bc04785856. Verified GitHub user awdawmip. Native owner inventory CONTROL_QUOTA; session start denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). This is ordinary author-side source publication, not a native CLAIM, Result, independent review or P000 transfer.
