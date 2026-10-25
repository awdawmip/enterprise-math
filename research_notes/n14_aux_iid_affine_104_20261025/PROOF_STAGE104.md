# Stage104: exact minimax affine interval and sharp right endpoint (external iid N=14)

**Status:** AUTHOR exact-rational, computation-assisted proof; two author implementations cross-check, not independent Driver admission or P000/X6 theorem. Prerequisite: Stage103 author proof, certificate, and NEXT_TASK_PACKET_104 at \`enterprise-math@7f1f1b7db3026c57e983c56b4f7d099f3de72a63\`. Read control sources: global-knowledge \`main@5ff6e3e527c6c501b9a3e77590f8899e7a440872\`, Enterprise Math \`main@c8edced92fd7c2e98d6cf7cb48c29f14dea40e6f\`. P000 locked and not modified.

## Exact theorem

Let the observations be iid with \`P=(1/8,1/24,5/6)\`, \`Q=(1/12,1/12,5/6)\`. Tests may randomize on any **complete ordered history**, stop by observation 14, and decide P or Q. Write \`eP=P(decide Q), eQ=Q(decide P)\`, \`tP=E_P tau, tQ=E_Q tau\` and \`V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)\`.

At the certified Stage103 author endpoint,
\`\`\`
alpha103 = 2586593886011416687/7450150876955541504
V103     = 3004643576828511655/232817214904860672
\`\`\`
the following formula is exact for **all real** \`0 <= delta <= eta104\`:
\`\`\`
V14(alpha103 + delta) = V103 - Gamma104*delta
Gamma104 = 9535248/4373
eta104   = 48103/275931513961316352
alpha104 = 646648471503178867/1862537719238885376
V104     = 6009287153480025269/465634429809721344
\`\`\`
Furthermore this particular supporting line is **strictly unattainable** beyond \`alpha104\`; its right endpoint is sharp. This does not determine Stage105.

## 1. Exact full-history Bellman dual

For prefix count state \`v=(n,a,b)\`, where a and b count outcomes 0 and 1, \`Q(prefix)/P(prefix)=2^(a+b)/3^a\`. Define
\`\`\`
K = lambda_Q = 4881384/4373
L = lambda_P = 72+(8/9)K = 4653864/4373
D(n,a,b)=min{ K*2^(a+b)/3^a, L,
              1+(1/8)D(n+1,a+1,b)+(1/24)D(n+1,a,b+1)
               +(5/6)D(n+1,a,b) },
\`\`\`
omitting the continue action when n=14. The respective actions are decide P, decide Q, and continue. Induction over **every ordered history**, without assuming the policy itself is count-dependent, gives \`D(root) <= tP + L*eP + K*eQ\`.

Exact values: \`D(root)=92221588169006115988373/119777609503406555136\`, and \`D(root)=V103+(L+K)*alpha103\`. There are 680 finite count states and 1240 nonselected-action comparisons: 1238 are strictly positive, 0 negative, 2 exact ties. The only ties are **A104=(11,8,3): decide P / continue** and **B=(12,0,1): decide Q / continue**. Minimum strictly positive gap is \`2872871/362714112\`. All pinned-policy action gaps are nonnegative at both \`K103=152847928260/128768917\` and K104; each is affine along \`L=72+8K/9\`, hence no earlier intervening dual policy change.

## 2. Genuine ordered first hits, positive branch carrier

Before either tie follow the unique strict Bellman action; at A use continuation when computing a suffix and at B use Q as the strict-policy tie resolution. Exact first-hit data:
\`\`\`
                        ordered words      P(first hit)          Q(first hit)
A=(11,8,3)              66                 11/38654705664       11/123834728448
B=(12,0,1)              12                 48828125/725594112  48828125/362797056
\`\`\`
Forced continuation at a tie, then strict Bellman actions, produces the tuple \`(conditional P-error, conditional Q-error, additional P-time, additional Q-time, number of ordered terminal suffixes)\`:
\`\`\`
RA = (41/13824, 569/576, 69/64, 167/144, 9)
RB = (63/64,   1/144,   9/8,   13/12, 5)
\`\`\`
The cones are **disjoint**: A has first-symbol count a=8 while B has a=0, so A cannot precede B; B lies at n=12 and cannot precede A at n=11. Hence there are no products of two mixing parameters. This is a typed BRC reuse restricted to exact positive-rational branch masses, multiplicities, and full ordered-history provenance, not a native BRC/X6 transfer.

## 3. Primal interpolation over every real cap

At the Stage103 endpoint continue at A and choose Q at B with probability \`s103=16415412204181171/20889600000000000\`. Let \`u in [0,1]\` be the new probability to decide **P** at A, and s the probability to decide **Q** at B.

Using the genuine first-hit masses and conditional suffix outputs, the **exact** error responses are
\`\`\`
eP = alpha103 + x*u + e*(s-s103)
eQ = alpha103 + y*u + f*(s-s103)
x = -451/534362651099136
y = 77/71328803586048
e = 48828125/46438023168
f = -48828125/52242776064
\`\`\`
Enforcing \`eP=eQ\` gives a unique affine balancing rule
\`\`\`
s(u)=s103+(1348743/1392640000000000)*u
s104=4103853056103079/5222400000000000
eP=eQ=alpha103+(48103/275931513961316352)*u.
\`\`\`
Both s endpoints lie strictly inside (0,1). The full policy family therefore uses legal randomization for every real u. Each played action at a reached state is a Bellman minimizer. The root outcome at u=0 is
\`\`\`
eP=eQ=alpha103
tP=V103=3004643576828511655/232817214904860672
tQ=22836168034496950505/1862537719238885376
\`\`\`
and at u=1 is
\`\`\`
eP=eQ=alpha104
tP=V104=6009287153480025269/465634429809721344
tQ=5709042008510518661/465634429809721344.
\`\`\`
Since the tie cones are disjoint, both durations are affine functions of u. \`tP>tQ\` at both endpoints and hence over the entire interval. For every real u, Bellman equality gives \`tP=D(root)-(L+K)*(alpha103+eta104*u)\`, which attains the universal lower bound for the worst expected stopping time. This proves the formula on the full real interval (not merely at sample points).

## 4. Sharpness among all ordered-history rules

For an error cap beyond alpha104, equality to the same support line requires \`eP=eQ=alpha\` (since L,K>0), \`tP>=tQ\`, and selecting a Bellman minimizer at each reached ordered prefix. Only A and B are tied. At the same count state all first-hit prefixes have the same P/Q likelihood ratio and conditional suffix outputs. Therefore any history-dependent tie randomization has the same errors and times as replacing the probabilities by their P-first-hit-weighted averages \`u,s in [0,1]\`. Because A and B's cones are disjoint, the exact equations above still apply; error equality forces \`s=s103+(1348743/1392640000000000)u\`, and then \`alpha=alpha103+eta104*u<=alpha104\`. Contradiction. Compactness of the finite randomized-policy space ensures the optimum exists, so the line is strictly unattainable to the right.

## 5. Reproducibility / next problem / permissions

Locally executed \`CHECKER_STAGE104.py\`: exact fractions, all 680 Bellman states and 1240 action comparisons, first-hit mass, conditional suffixes, endpoints, midpoint, dual gap interpolation, next candidate. Separately coded \`INDEPENDENT_ORDERED_STAGE104.py\`: top-down Bellman and actual ordered DFS; visits 1,014,064 nodes at u=0, 1,013,272 at u=1, and 1,014,064 at u=1/2; checks true prefix counts, suffixes, exact endpoints and midpoint. These are **two author checks**, not an independent review. The attached local ZIP preserves both full source programs, machine certificate, complete proof, run logs and hash manifest.

The next **dual-only** candidate is \`K105=2212824096/1992661\`, new \`A105=(8,5,1)\` P/continue tie. Its primal interval, path cone interaction and sharpness are NOT proved.

Authenticated GitHub principal: \`awdawmip\`; project write permission exists. Native \`em_control_tasks\` returned \`CONTROL_QUOTA\`, and \`em_session_start\` returned \`STATIC_READONLY_SCOPE_DENIED\` with \`operation_sent=false\`. Thus current owner and native Researcher/CLAIM/Result are not verified. This document is only ordinary GitHub-author evidence. No Google Drive workaround or sharing change is used.
