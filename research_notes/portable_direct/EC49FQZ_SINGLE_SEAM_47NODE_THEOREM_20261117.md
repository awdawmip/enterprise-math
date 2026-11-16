# EC49FQZ — Single-seam exact BRC continuation and 47-node certification

Date: 2026-11-17 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Immutable scientific object

Frozen scientific Source: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This is the positive-weighted native BRC sensing experiment of class 16943, with 310 original configurations, 141 distinguishable complete named-root profiles, 144 terminal observations, 84 named-root observations, 228 physically labeled first observations (209 distinct response partitions). Root/source identities, response branches, multiplicity and complete provenance are retained. P000 / six-axis Heartbeat World remains the project premise; the result concerns this exact finite sensing problem, not a signed-amplitude or physical-dynamics model.

Predecessor: EC49FQY PR #2587, immutable head 67ed797fd858cebd8639c816ab3ff6223ac951ed, with 45 certified prices. Original frozen master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; original root-profile CSV SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

Terminal observation price t>0; root observation price xt, x>=1. Prior p_lambda(i)=(1-lambda)/141+lambda*m_i/310, 0<=lambda<=1. An unrestricted legal finite adaptive tree must separate all 141 complete profiles, without a depth cap. V(x,lambda) is its minimum normalized expected cost. Previously constructed fixed feasible complete-tree strategy costs are

A=(1-lambda)*(6*x+290)/141+lambda*(6*x+751)/310,
B=(1-lambda)*(5*x+293)/141+lambda*(5*x+704)/310,
C=(1-lambda)*(5*x+295)/141+lambda*(5*x+685)/310.

Define K(x)=7557-169x, G(x)=310(3-x)/K(x), beta=620/3299.

## Theorem 1: a single Bellman seam suffices for a complete new price slice

Let a<b be adjacent prices whose full real-prior exact BRC certificates establish V(a,lambda)=min(A,B,C) and V(b,lambda)=min(A,B,C), with complete physical first-label classifications and 0<=G(b)<G(a)<beta. For any c in (a,b), assume the *one* unrestricted, exhaustive Bellman computation at the seam (c,G(c)) certifies V=A=B there. Then V(c,lambda)=min(A,B,C) for **all real lambda in [0,1]**. If the seam's complete optimal physical first-label set is {32,34,140,142} and the predecessor endpoint first-label phases have the established pattern, the full price slice has exactly {32,34} for lambda<G(c), {32,34,140,142} at G(c), {140,142} for G(c)<lambda<beta, {16,23,140,142} at beta, and {16,23} for lambda>beta.

Proof: for any fixed complete separating tree, normalized cost is bilinear in (x,lambda); for fixed lambda it is affine in x. For any competing full tree T, the difference cost(T)-A is affine in x and is nonnegative at both a and b whenever lambda<=G(b). Hence A is globally optimal for every intermediate price and 0<=lambda<=G(b). The same unrestricted all-tree argument gives B for G(a)<=lambda<=beta and C for beta<=lambda<=1. This is a cost comparison against *every* legal finite decision tree, not merely a stored candidate family.

For fixed price c, V(c,lambda), a minimum of affine tree-cost functions, is concave in lambda. It equals the feasible affine A at lambda=G(b) and, by the new seam certificate, at lambda=G(c). Concavity and feasibility imply equality with A throughout [G(b),G(c)]. The identical argument for B between G(c) and G(a) completes all real priors. The borderline G(b)=0 is included.

To classify **all** physical first labels, fix a first query q and let V_q be the best expected cost among complete legal trees beginning with q. V_q is concave in lambda at fixed price, and concave in x at fixed lambda; on any region where a fixed A/B/C affine branch F is globally optimal, V_q-F is nonnegative and concave in the variable being interpolated. A nonnegative concave function that is strictly positive at either endpoint is strictly positive throughout its open interval. In the inherited regions, the endpoint physical-label sets therefore exclude every extra q at the interior price. At the intermediate seam-adjacent prior intervals, the inherited boundary's strict gaps and the exact new seam tie set likewise exclude extras. The existing complete A/B/C witnesses provide all asserted optimal labels, while at beta the inherited endpoint ties give exactly {16,23,140,142}. At the seam the native enumeration gives exactly four labels. QED.

Thus an inserted price can be proved over its full continuous real-prior axis with **one rather than four** new exhaustive Bellman anchors, when its two neighboring full-prior endpoint certificates and labeled witness trees already exist.

## Theorem 2: two new exact price slices

Insert c=73/32 between 9/4 and 37/16, and c=191/64 between 95/32 and 3. The exact seams are G(73/32)=7130/229487 and G(191/64)=310/451369. Exhaustive original native Bellman calculations at those two seams, followed by a structurally separate weighted-subset implementation, give:

| Price c | Lambda seam | Exact unnormalized weighted Bellman optimum | Every optimal physically labeled first query | Independent Bellman subset states |
|---|---|---:|---|---:|
| 73/32 | 7130/229487 | 694468676160 | 32,34,140,142 | 5929 |
| 191/64 | 310/451369 | 2757607251840 | 32,34,140,142 | 5932 |

Unnormalized mass uses integer weights w_i=310*(denominator-numerator)+141*numerator*m_i; terminal/root prices are the respective integer pair (32,73) and (64,191). Both exact objectives equal the normalized A=B formula after applying this mass/price scale. Each complete certificate enumerates all 228 original first queries, proves its exact minimum with unrestricted subset Bellman recursion and replays all four tied full trees. The independent verifier reconstructs the complete original profile observations. Theorem 1 proves both complete all-real-prior slices and all first-label transitions.

New native seam witness SHA256: 73/32 c95a3b6fbb284a6ab10cc68a3ef88a0935218c701685d7c5b621db15343647ba; 191/64 cb0db5642cb81bc274ea21b1f0cda9825dca061f6a9c48551fda5316283d7e7d.

## Theorem 3: 47 exact price nodes, whole-domain guarantees

Adding the two certified prices to the inherited 45-node grid produces 47 nodes, 46 adjacent intervals. For each adjacent a,b, the portion not yet globally certified lies within G(b)<lambda<G(a). The containing-strip area S(a,b)=(b-a)*(G(a)-G(b))=2185500*(b-a)^2/(K(a)*K(b)) is rational. The exact total over [1,3] is

S_47=5959469197718386554712955/1505500161665693064580080288.

Therefore the rigorous *lower bound* on the certified global-optimality fraction of [1,3] x [0,1] is

1-S_47/2=3005040854133667742605447621/3011000323331386129160160576
=99.8020767665967966615581977... percent,

improved from 99.7968541704326089... percent. The previously proven x>=3 exact regime remains unchanged.

The inherited all-tree chord/concavity regret certificate for each interval is
R(a,b)/t=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2.
The exact maximum across the 46 new intervals is now attained by the *certificate envelope* at [35/16,9/4]. For all lambda in [0,1], x>=1 and t>0,

0<=C_strategy-C_optimal<=
50*(9/4-35/16)/(sqrt(K(35/16))+sqrt(K(9/4)))^2 * t
=0.0001087784330666855807751029523... * t.

This is a proved uniform **guarantee**, not a claim of an attained worst-case true regret. Each radical is bounded by exact rational integer-square-root brackets of width 10^-20, and the winning interval's lower bound is strictly above all other intervals' upper bounds. The previous upper guarantee was 0.000108938647459392...t.

The local area decrease from inserting c between a,b is exactly
DeltaS=2185500*(c-a)*(b-c)/K(c) * (1/K(a)+1/K(b))>0.
For new c=73/32, DeltaS=182125/2194343942. For c=191/64, DeltaS=155/7224608. Their sum is 827952521505/7926637399062368.

## Original implementation bug found and corrected

The inherited native Bellman solver initialized its weighted optimum with the arbitrary integer INF=10**12. At the legitimate input (191/64,310/451369) the correct weighted optimum 2757607251840 exceeds this sentinel, causing the original code to emit an erroneous 1000000000000 with weighted first query -1 and then fail tree construction with AssertionError. The failed diagnostic is not a proof or a scientific counterexample. We replaced it with the exact dynamically sized upper bound

INF=(N+1)*max(query_prices)*(N+sum(integer_weights))+1,

where N=141. Each legal nontrivial query refines the remaining finite support, so a complete separating path contains at most N-1 observations. This expression strictly dominates any complete-tree uniform or unnormalized weighted cost, without a fixed cap. Regenerated seam certificates with this replacement and independently recomputed the exact values and complete label sets.

The unrelated attempted 73/32 prior=1 calculation did not complete and is excluded from the theorem; the seam-only theorem makes that experiment unnecessary. Two additional 73/32 native anchors at prior 0 and beta are auxiliary, not proof dependencies.

## Evidence and next research frontier

The complete original full witness JSONs, independent reconstruction/checker source, frozen input files, native generator with dynamic INF repair, exact 47-grid rational/radical checker, successful verifier logs, inherited complete 45-node evidence archive and all-file SHA256 manifest are packaged in the self-contained conversation artifact EC49FQZ_TWO_SINGLE_SEAM_47GRID_FULL_EVIDENCE_20261117.tar.xz, SHA256 ad0b4e53a0feac5e5b9f177c45147bdc7ab03996208a8a3bbcaf43aeafc1b5ff.

The compact GitHub proof, executable geometry checker and certificate index document the artifact, not a claim that its full raw machine witnesses are included as repository blobs. Results are AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED; GitHub-only portable evidence, without an asserted canonical Task CLAIM, Result, reviewer acceptance or Activity checkpoint.

Open problem: close the remaining 46 thin bands by a parameterized native all-branch Bellman lower bound, or find one fully native physically labeled legal adaptive tree beating min(A,B,C) at a rational interior parameter. A verified strict positive rational improvement would be a counterexample to the candidate global phase diagram, while preserving the already certified regions.
