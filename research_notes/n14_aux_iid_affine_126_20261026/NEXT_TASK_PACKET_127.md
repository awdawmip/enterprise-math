# Stage127 next research: dual candidate only

Mother question: continue exact \(V_{14}(\alpha)\) for N=14 ternary iid P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), unrestricted full ordered-history randomized policies. This is an **external auxiliary model**, not native P000 X6 theorem.

Latest **author-proved** Stage126 endpoint (independent Driver review pending):
alpha126=18340838011402083499/52808422392537808896,
V126=335279238082246223695/26404211196268904448.
At that endpoint, old A=(9,3,0) P/continue has saturated P-stop (y=1); B=(11,0,1) remains Q-stop/continue mixed with w*=1232366013208259/13573120000000000. B is the remaining dual tie.

Maintain B's Q/continue tie while varying dK=-1 and dL=-(112/129); at A the previously zero nonselected continue gap opens at strictly positive slope 527153/288893952. Exact dual-ray scan of 1238 initially positive gaps gives first closure at
t=11764115784/554037803,
K127=8246448/11561, L127=7673768/11561.
New tie C=(11,6,2) P/continue while B=(11,0,1) Q/continue remains tied. Fresh exact 680-state Bellman gives 1238 positive gaps, no negative, min positive=71/9459, root=207290753323284460123369/422211736708250075136. **Stage127 DUAL_CANDIDATE_ONLY**; no primal interval proved.

Concrete first task: enumerate actual literal ordered first-hit B/C words and P/Q integer weights, retaining BRC order and provenance. As B,C are different count vectors at **the same depth 11**, first-hit ordered path cones cannot intersect. Obtain exact four-observer affine moments for B-stop Q and C-stop P, balance errors, check legal randomization interval and tP>tQ, prove full-real optimality plus support right-sharpness or an exact no-go. Cross-check with an independently implemented integer-weight DFS. Do not repeat Stage125/126 proofs or upgrade to P000 native world.

Sources: sibling Stage126 proof, two checkers, certificate, execution evidence and SCAN_STAGE127.py, frozen global-main 3c15f1c6 and starting EM main 658e1f3e; P000 original blob 770e1b157f. Native owner/CLAIM unavailable, author result only.