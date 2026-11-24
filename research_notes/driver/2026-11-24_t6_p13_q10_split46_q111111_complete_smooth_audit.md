# T6 p13 q10 split(4,6), q111111 final five intervals: exact smooth-domain Driver audit
2026-11-24. Continuing historical Driver lane EM-DVR-DEBB5E. Original author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Shared scientific context and pinned saturation method, separately implemented and executed nearest-path enumeration; not a clean-blind independence assertion, native Review, or Result admission.
## Scope
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, each side mass <=2331, maximum prime 13, high-prime/higher-valuation elimination and common named atom cancellation as in earlier audit. Six congruences and weighted affine lattice as in 01e1ae8e6118e439b0da0481c692ff1fdb55ac21. Prior scope through index4096 read at 1b2e35b36651c9ee5a4d9bcf4498ddd8f906b488. Author now completed q111111, full immutable certificate 3ac87bfdd36981ee2ecf2898065e41a2da10c5f2:research_checks/T6_P13_Q10_SPLIT4_6_NEG111111_FULL_AUTHOR_EXACT_CERT_20261124.json.
## Executed computation
Reconstructed exact six-step saturation, HNF, weighted LLL delta=3/4 and rational GS from the pinned replay a466be736446891b423809b0ba23cb37ec123502. Both lattice determinants 13^21, all reduced rows satisfy all six homogeneous congruences, all smooth particular vectors verified. Q=4826809, dmin=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349 > 4*4402474. All 907 smooth positive rosters generated from partitions (4),(1,3),(2,2),(1,1,2),(1,1,1,1), all remaining negative rosters drawn from the lexicographic cwr(1..12,6) domain. Exact trial division by 2,3,5,7,11,13; skip common atoms. No vertical budget skips. Same integer scaled nearest decoder as earlier r548, with affine coordinates reduced modulo Q. No floating comparisons or recursive approximation.
|interval|literal disjoint|smooth negative rosters|smooth decoded|sphere leaves|
|---|---:|---:|---:|---:|
|4096-5120|1017527|363|106123|0|
|5120-7168|1715457|460|110482|0|
|7168-8192|1027874|305|91789|0|
|8192-10240|1842932|252|63846|0|
|10240-12376|2191917|462|152229|0|
|total|7795707|1842|524469|0|
All five source certificates fetched at their immutable commits in the full author certificate. Blob SHA1, literal counts, negative-roster SHA256 agree exactly:
- 78a985ef799d3c44fa3e7cbdbe3634bf8c430ad4dd408c2dd7e3d7579e0e8169
- 8274d939cf188fa7f5b0c66ef1d328a2f6634680fc01f8ff21c677172a4f34fa
- c7c885337e4ee22f9a34c844cdc5de4ddd3a75926259307bbd30fb208fabee36
- 63a559032baa57990798bcbd82fe7d2a2b912fec19f56ae59888b7ccda10b181
- 5a3a61758475b7dea6847f50cec6828f0b0d80b30a6889053a0d60b296263f33
Author witness ni5086/pi1202 separately recomputed: positive r=(1,1,3,12), negative r=(2,2,5,6,7,11), q=1 throughout, u=(48,-21,17,5,2,-5,0,-3,0,-3,-4,-4), vertical masses 893/1437, norm squared 2206625 <=2867080, six modular residues zero, original masses 2498/4231 both exceed 2331. Negative cofactor 19 excludes witness from smooth domain.
## Reproduction
Construct saturated homogeneous row lattice by sequential modular elimination, HNF and LLL as in pinned replay. For each smooth atom obtain particular solution, convert to basis coordinates modulo 1 and scale by Q. For each disjoint pair, R=(2331-cp)^2+(2331-cn)^2, z=(pc-nc) mod Q, then for i=11..0 compute center=z[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j>i), tr=(-2*center+L[i])//(2*L[i]), add T[i]*(center+tr*L[i])^2 to spent, reject if spent>R*K, else z[i]+=tr*Q. The unique path lemma ensures exhaustive search. Counts above are actual local execution. Loop times including roster counting and hashing: 0.677,0.705,0.625,0.643,1.375 seconds (not a full cost comparison).
## Frontier
q111111 complete 809286 smooth decoded (284817 previously,524469 new); full split(4,6) and reverse now conditional exclusion across all 11 families, cumulative 3600371 smooth decoded (prior 3075902 +524469), zero budget-valid vectors. Author full literal q111111 11302590 searches, three relaxed witnesses, zero budget-valid. Preserve all original author contributions. Next science: split(5,5) author-complete immutable scopes, plus formal linkage of exact new frozen Result when authorized. No formal Task or mother closure.
## Control observation
em_status returned current authenticated capability and active_jobs=0 at observation; Source sync error null, code upgrade available, not deployed assertion. Subsequent checkpoint_list returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Previous r549 not independently refreshed this round; no protected mutation attempted or new identity. Historical selection RS-DISC-COMPAT-20261026-11 retained; current owner/worker availability not verified. Preserve original requests; no claim or repeat dispatch. Formal admission pending.
