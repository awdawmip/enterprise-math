# T6 p13 q10 split(5,5): complete smooth-domain exact Driver audit
2026-11-24. Continuation of Driver lane EM-DVR-DEBB5E, historical r549; author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Shared author evidence and basis method, separately implemented and executed finite decoder; no clean-blind independence claim or native Review.
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, each side mass <=2331. Conditional on prior high-prime/higher-valuation elimination and common named atom reduction. Author full certificate 3cde57d1c792f4272c521ec583b951703e251eea:research_checks/T6_P13_Q10_SPLIT5_5_FULL_AUTHOR_EXACT_CERT_20261124.json, blob 191a26caf59212949eae9fc5f59ed130d5fc8fca, actually fetched. Previous Driver completed split(4,6) note b429e11a91f3ebdc33476d39b54e70e942adfe7e actually fetched.
## Executed full independent enumeration
Reconstructed six-step modular saturation, determinant 13^21, HNF then weighted LLL delta=3/4, all homogeneous rows verified against six prime-power congruences, rational GS dmin=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349. All particular vectors for smooth atoms verified. Q=4826809, integer-scaled GS coefficients checked exactly. Reuse unique nearest-plane lemma 01e1ae8e6118e439b0da0481c692ff1fdb55ac21: 4*4345352<dmin. For equal q totals 5, sign reversal swaps rosters and negates u; enumerate i<j in a common ordered roster list, excluding common named atoms. Diagonal has common atoms and is covered by prior reduction.
|negative partition|literal rosters|raw sign pairs|literal disjoint|smooth rosters|smooth disjoint decoded|sphere leaves|
|---|---:|---:|---:|---:|---:|---:|
|5|12|130818|130818|5|15570|0|
|14|144|1558584|1193688|54|117558|0|
|23|144|1537848|1451880|49|134946|0|
|113|936|9490572|5636268|315|458892|0|
|122|936|8614476|5820804|252|374976|0|
|1112|4368|28616952|11540232|1155|679392|0|
|11111|4368|9537528|2098734|1287|135612|0|
|total|10908|59486778|27872424|3117|1916946|0|
All seven literal roster SHA256s match full author's manifest exactly (in order):
42254c6f88cd10d868bd6f22eb0316aec403a792431d854bd922daa85248eb79
7f30cc46e007ff580d9f8fd9ea606b817ccf47bc1a4c9df955357f9278c57262
8e75c1ddbe2e281a870a8d569315a14317f865125c025a7ea34334f6a706eee6
411bc33b9edc1950e3a40b0a9de32ff7ad3715799cc13bf47b59524944b7677f
383747d7027a1af29a2e6ce3ef3f75087c9712447842a8e0de42425f984c4529
5a7e77b62e43536b00f08a0e42b21d1354bd3be3f6826c24fd55e9b954c75046
705ec8805da377d05a02738564fd420098cb5dcc1862cf29de9d15540e695cf8
Literal disjoint counts independently computed by reverse-suffix inclusion-exclusion on support subsets; raw count n*(10908-offset-1)-n*(n-1)/2. Not full literal lattice replay. Loop times for seven actual smooth enumerations 0.113,0.863,0.975,3.298,2.690,4.892,1.000 seconds (excluding preparation and literal counts).
## Independent witness arithmetic
Recomputed masses, squared weighted norm, radius and all six congruences for every author relaxed witness, using separate integer modular inverse implementation; all match. Listed nonsmooth cofactor(s) (13q+r) exclude each witness from the genuine smooth domain independently of mass.
|ni/pi|masses|norm_sq|radius_sq|nonsmooth cofactors|
|---|---|---:|---:|---|
|271/6567|4269/2894|2824587|3320200|47|
|954/6543|3786/2678|2428619|3339869|17,19,23,46|
|1296/1618|4088/2688|2901987|2929921|37|
|1440/2010|3953/2777|2430661|2750365|23,31,37|
|2331/4938|3688/2716|2232320|3117476|17|
|2871/3386|2889/3371|2405113|3189925|17,19,29|
|3319/5718|2963/3257|1961295|2631185|19,23,34|
|5321/7025|3524/3536|2715670|2947492|17,17,17,23|
## Reproduction
Use exact saturation/HNF/LLL and integer scaling definitions of a466be736446891b423809b0ba23cb37ec123502:research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py; extend particular q to 1..5. Generate partitions in table order, within each sorted q group use combinations_with_replacement(1..12,multiplicity), Cartesian product across distinct q. Filter each atom by trial division of 13q+r by 2,3,5,7,11,13. The common smooth roster list contains 3117. Prepare each roster with cp=sum(169q+13r-1), coordinates as summed atom numerators modulo Q, and bitmask of distinct (q,r). For each i<j disjoint masks, run:
```python
radius=(2331-cp)**2+(2331-cn)**2
assert cp<=2331 and cn<=2331 and 4*radius<min(D)
z=[(a-b)%Q for a,b in zip(pc,nc)]
spent=0
for i in range(11,-1,-1):
    center=z[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j in range(i+1,12))
    t=(-2*center+L[i])//(2*L[i])
    spent+=T[i]*(center+t*L[i])**2
    if spent>radius*K: break
    z[i]+=t*Q
else:
    # recover u from z*U/Q and verify norm, masses, residues
    found.append(z)
```
Every smooth disjoint sign orbit has been decoded, no sphere leaf. Exact finite conditional exclusion of split(5,5). Prior completed split(3,7) and split(4,6) independent counts 2937072 and 3600371 (historical notes); combined 8454389, zero budget-valid vectors in these three splits. Other splits and full p13 scope require their own evidence; no mother closure. 
## Control
Current em_status succeeded, active_jobs=0 at observation, Source sync error null. checkpoint_list succeeded and confirms Driver revision549, last stored request dvr-20261124-2000-r549-q111111-4096-audit-v1. Following exact checkpoint_get failed BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. No protected mutation or new identity attempted. Preserve prior Driver note b429e11a and this new note; no native acceptance or new dispatch. Next: restore exact checkpoint, record both completed split46/split55, audit remaining p13 q10 split coverage and bind exact frozen Result with verified current own authority.
