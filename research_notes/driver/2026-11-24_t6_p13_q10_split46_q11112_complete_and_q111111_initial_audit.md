# T6 p13 q10 split(4,6): complete q11112 and initial q111111 independent smooth-domain audit
2026-11-24. Driver historical lane EM-DVR-DEBB5E, original author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Separate local exact calculation with shared scientific inputs and saturation method; not clean blind independence or native Review.
## Scope
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, both side caps 2331; under high-prime and common named atom elimination and six necessary p-adic congruences. Reuse r547 audit@440f937ed341b839549f6e98f84901259da085e7 and nearest decoder proof@01e1ae8e6118e439b0da0481c692ff1fdb55ac21. Author full q11112 certificate@3a1157d24d3575aca373e23b8a154538c50f4a13:research_checks/T6_P13_Q10_SPLIT4_6_NEG11112_FULL_AUTHOR_EXACT_CERT_20261124.json. Author r124 also provides q111111 [0,1024)@39720b3397910eab09c54a540cd6f6b5ce8021f0.
## New exact searches
Reconstructed lattice with sequential congruence saturation, HNF, weighted rational LLL delta=3/4 from pinned kernel a466be736446891b423809b0ba23cb37ec123502:research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py. Both original and reduced determinants equal 13^21; all reduced basis rows satisfy six homogeneous congruences. All q1..4 particular solutions verified. Q=4826809; exact dmin=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349 > 4*4402474. Each pair additionally checked 4R<dmin. Use positive partitions (4),(1,3),(2,2),(1,1,2),(1,1,1,1), 2535 literal, 907 smooth. Negative literal q11112 roster combinations_with_replacement(1..12,4) then q2 label 1..12; q111111 combinations_with_replacement(1..12,6). For a distinct q1 labels and b remaining q2 labels (11 or 12), literal disjoint count =12+(12-a)*12+C(b+1,2)+b*C(13-a,2)+C(15-a,4). All counts and SHA256 of newline-separated Python repr of literal negative rosters match exact author segment certificates below.
| interval | literal disjoint | smooth negative rosters | decoded | leaves | loop seconds |
|---|---:|---:|---:|---:|---:|
| q11112 [9216,10240) |1074912|276|79608|0|0.32026|
| [10240,12288) |2320668|53|18182|0|0.07170|
| [12288,14336) |2446080|392|135023|0|0.48851|
| [14336,16380) |2561064|490|192535|1|0.69932|
| q111111 [0,1024) |1004954|369|105514|0|0.49702|
No vertical budget skips. Exact roster SHA256 in order:
0c023cd0e810a463def4f868ab7590f07ce6bd3f907c5d749fe3ff1542e66633
17dfdc6f702c0775a6d7d9fbfc8e88c5d7fcd5efb01408093d694e67d9a18573
b808513360fdc74fe9bf346083386079b4afac787a9ce32bd0a04c86e1
3abb761c3371195865149c38878b4ac9c50b9521bd38e6b420185f3e637460d5
808b800030ca1b97e8a66bc5e9f43e50dc1523e2f9947fcfdd3ca90d4f1e568d
Author commits in order 106492577fda7ffab2f7211de0fd45a0d5d7227d, 88aea76796deedb9079049e16412ff163d01a873, 2b2feff7e967318c7cdf8e37d72c3315856a966e, 906cbde6f2ce8c44593446a8b6d92863cfb465cc, 39720b3397910eab09c54a540cd6f6b5ce8021f0, paths research_checks/T6_P13_Q10_SPLIT4_6_NEG11112_<start>_<end>_AUTHOR_EXACT_CERT_20261124.json (last NEG111111).
All disjoint smooth pairs decoded via exact integer scaling L,B,T,K as in earlier notes: z=(pc-nc) mod Q; center=z[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j>i); nearest tr=(-2*center+L[i])//(2*L[i]); accumulate T[i]*(center+tr*L[i])^2; reject if >R*K; otherwise z[i]+=tr*Q. Recover u=zU/Q with exact divisibility and check residues, norm, original side masses. No floating decisions. All four newly reported author literal sphere witnesses independently checked:
- q11112 ni10482: masses 3682/3446, norm 2745868 <=3036100; cofactor17 excludes from smooth domain.
- ni11644: masses 3503/3403, norm2237828 <=2876900; cofactors29,17,19,23,31 exclude.
- ni16177/pi1985: sole smooth leaf, pos=((1,3),(1,7),(1,7),(1,8)), neg=((1,9),(1,11),(1,12),(1,12),(2,2)), u=[15,22,-4,-3,5,4,-1,-3,8,-1,-2,0]; norm1640739 <=2303732; masses3283/2724, both exceed 2331.
- q111111 ni365: masses2546/4348, norm2796655 <=3137441; cofactor17 excludes.
All six congruences zero in each direct recheck. No budget-valid vector. Author cumulative GS-node bookkeeping correction -233000 through 9216 acknowledged; no impact on coverage or witnesses.
## Frontier
q11112 added 425348, cumulative 1144899/1144899, complete conditional finite exclusion. split46 now 10/11 complete families, cumulative 2896599 decoded including new q111111 [0,1024) (new total 530862). Only q111111 remaining family, next audit verified author ranges after 1024. Author r124 working next range; backlog r466 retains choices, no positively available worker.
## Control recovery
r547 read; original T6 child request dvr-20261124-1200-t6-child-current-read-v1 SUCCEEDED, historical child already accepted. Exact credential catalog entry enterprise-math-d25-permanent-driver-20261110 matches historical lane EM-DVR-DEBB5E, SID MCP-9b4714dc46b948afa4875a86c89c713c, DA-2C461358FCCA215C8753. Owner custody status verified unrevoked/unexpired and underlying session open. Own recovery dvr-20261124-1900-own-recovery-read-v1 returns same SID and historical dvr requests, no in-flight request in returned recent set. Original T6 review-flow dvr-20261124-0559-t6-rr-c428-flow-read-v1 SUCCEEDED, DA matches, RR-C428294CF760BD8D99AA has nonterminal RETURN_TO_OWNER and existing p17 followup; not a new p13 Result. Preserve old F7 failed request without replay. Recovery establishes existing identity/transport and historical review view, not fresh write authority. Need exact newly frozen p13 Result before scoped formal review; do not apply new proof to unrelated old RR or claim on behalf of author. No formal Review/Result/Task/mother completion in this round.
