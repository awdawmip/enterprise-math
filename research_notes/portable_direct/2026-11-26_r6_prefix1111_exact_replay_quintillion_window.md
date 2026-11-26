# PREFIX-1111: raw amplitude replay and a contiguous integer-edge certificate through 1.073741824e18

Date: 2026-11-26. Author: EM-DIRECT-780BBE / TASK_RESEARCH; RA-0ABD84561C86E53067DB0322.
Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / RAW_DISPLAY_PREMISE_DISCHARGED / NOT_REVIEWED.
Scope: same frozen Stage46 X6 signed joint BRC observer as PREFIX-1100--1110, P000 V5@f42f2906d77f24085c123f3ccfe9667d41caa96d. Chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, subsequent incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives. No change in model, no new native propagation or classical physical comparison. The observer is D_m(k)=L[x^m(1-x)^k]. All conclusions inherit the model correspondence, effective edge band and infinite-tail monotonicity; the parent mother objective B_fix,odd(32) stays open.

## Sources and operation

- 1095@dc4fcdd14e85a886f07b6484ee67acd260e5081a
- 1099@a89442d139ce2bd37d3b51a1d16bdd153e486c31
- 1100 oracle@74b507708fa98cca4031924c9344e663f217ac0f; report@60f5d76fb61beaefbd9c479a0e96c9429c379513
- 1097 monotonicity@53d572769fe8745d7c60d93b92b28b182dabfa00
- 1107@7e95625df3a8c21b6d370246065d51469afa6345; 1107b@bd6e81d3baba1aa8bcea7caec629814475fe5ab6
- 1108@373ebdb904c3c2467718832e2ed354eb6c16712f
- 1109@f6cd6a43428786cbcc64f32baeba52eaf2e7be56
- 1110@cfdf96f06e7fbcb698d8b957139453eabe0b2729

Reproduction wrapper: 308fe4a28beb9dfadaccc1171514035cb95bc4d0:research_notes/portable_direct/2026-11-26_r6_prefix1111_replay_refine.py; blob 58586f813687c44ea209290fb7638c75b49da724. Wrapper assembled from the equivalent local executed reconstruction; wrapper itself was not separately executed. Local execution used Python exact integers/Fraction and the inherited signed density/dual oracle. Initial full Fraction anchor integration timed out; the exact-floor interval method below recovered it. Reconstructed 66 signed Laurent terms, checked 28x7 elimination matrix SHA256 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312, four 201-term bases, contraction and exact grouped occupation divisions through 5600. No high-m CT or giant factorials.

## 1. New exact-floor recovery lemma

The inherited incomplete-beta integration uses a=half/2, p_0=1, v_0=1/(a+1), p_j=(35/36)p_(j-1), v_j=(j v_(j-1)+p_j)/(a+j+1). For the next-degree recurrence at anchor k use v_(n+1)=36*((a+n+1)v_n-p_k*(35/36))/(a+n+k+2). Maintain lower/upper rational intervals on integer grid G=10^220, floor lower and ceil upper after each operation. Positive coefficients and denominators propagate endpoints monotonically; the subtracted edge uses upper edge for lower bound and lower edge for upper bound. For any signed exact coefficient, multiplication swaps endpoints if negative. For original H=10^100 matrix rounding, if floor(H*lower)=floor(H*upper), the exact original floor is uniquely recovered. Otherwise abort or raise grid precision. Induction from exact initialization proves containment and the floor equality proves the original rounded value, not an approximation to a different anchor. All required floors agreed in the executed anchors. This replaces expensive full rational denominators without changing anchor matrix semantics. Existing certified dual and coefficient box checks remain in force.

## 2. Raw replay discharges PREFIX-1110 display-enclosure premise

Anchor [3200,3600,4000,4400], cut=80, J=7, digits=55, R0=160427545/10^8, degree218. For each row below center is contained in [L/G,U/G], radius <= E/G; G=10^50. All four actual rational centers agree with the historical displayed values within 10^-26 and actual radii <=2*10^-17; strict signs and tail <10^-100 checked. Thus the conditional display assumption of 1110 is now discharged using raw replay, while inherited theorem assumptions and independent review status are retained.

m,k,L,U,E
1000000000000000000000,21440036720404643983373,-663790783285674699571610836653936341649,-663790783285674699571610836653936341648,1912761588809167602024352745534383
1000000000000000000000,21440036720404643983374,48780910080863015974617245383108901346,48780910080863015974617245383108901347,1912761588809167602023902258293839
10000000000000000000000,214400367204046439832847,-3301386868029894585905782111148479818,-3301386868029894585905782111148479817,1912761588809167602034197059329716
10000000000000000000000,214400367204046439832848,67955782468623876969429483298115640526,67955782468623876969429483298115640527,1912761588809167602034152010605661

Original total radius about 1.9127615888091676e-17, anchor contribution 1.74825194e-17, local 1.64509649e-18. Raw replay slope width 5.368615134794355e-27.

## 3. Refine anchor and reverse amplitude

Anchor [4000,4400,4800,5200], cut=120, J=7, digits=75, same R0, degree298. Total radius about 9.82086930e-27, anchor contribution 9.82086864e-27 and local 6.57604929e-34. All four signs remain strict. The following compact exact rational outward certificate uses G=10^70:

m,k,L,U,E
1000000000000000000000,21440036720404643983373,-66379078577065284814092982652151126496020231367155223137002,-66379078577065284814092982652151126496020231367155223137001,98208692987205459750423065319437852794625592
1000000000000000000000,21440036720404643983374,4878090759588486740529825551617468456944997947963499739038,4878090759588486740529825551617468456944997947963499739039,98208692987205459750397765840737824956147129
10000000000000000000000,214400367204046439832847,-330138935300804315522477199267322571568636539054761979666,-330138935300804315522477199267322571568636539054761979665,98208692987205459750976255221739574521937035
10000000000000000000000,214400367204046439832848,6795577998364572840011049341665496528241502667594645791387,6795577998364572840011049341665496528241502667594645791388,98208692987205459750973725273869571738089165

For normalized adjacent observations -a and b with positive interval bounds, the shared normalization cancels: ratio r=a/(a+b). Its rigorous interval is [a_l/(a_l+b_u),a_u/(a_u+b_l)]. Inherit 1110's residual payment epsilon=(2000/m+620/m^2)/(0.044^2). From f(m)=rho*m+c+d/m, |f(m)-k-r|<=epsilon, intersect rho with [(k+r_l-epsilon-c_u-d_u/m)/m,(k+r_u+epsilon-c_l-d_l/m)/m]. Keep c,d from 1107b. Actual exact slope intersection endpoints:

1848585155875637913581280831805631730688482994058055220586417730996181794032556018308718171362708363880457611571028667637220502543056639/86221174897351063581955671145287111077090315173424149470514300000000000000000000000000000000000000000000000000000000000000000000000
73943406235025516543251233272225269289626406601296694069481968639824919388733512258364337088154433833788333175958593585042786370361457/3448846995894042543278226845811484445532602145099660743558732000000000000000000000000000000000000000000000000000000000000000000000000

Width approximately 2.7779316462242506e-36, about 2.020737356e9 times smaller than 1110's 5.61347025e-27. The old thirteen candidates were regenerated (SHA256 37a7eae12d50510a319df882521a25ed9fa8854fc4f0fd107bf727e8e51cd391) and all excluded by refined strip; minimum positive gap 1.7250030558464826e-14. The old 39 candidate closures from 1110 now have raw-replay support.

## 4. Exact window extension and residual candidates

For each integer m in the declared range use L=rho_l*m+c_l+d_l/m-400000/m^2 and U=rho_u*m+c_u+d_u/m+400000/m^2. Inherited effective band and monotone tail determine Klast whenever there is no integer in [L,U]; at a unique candidate j, one strict sign determines j-1 (positive) or j (negative), with both outer neighboring signs determined by the band. The exact adaptive tangent/secant floor-sum sieve of 1108 was reused. Each dyadic window [M,2M) was exhausted by integer counts and bisection, not enumeration. Counts:

M,nodes,candidates
65536000000000,5,0
131072000000000,1,0
262144000000000,3,0
524288000000000,7,0
1048576000000000,3,0
2097152000000000,1,0
4194304000000000,1,0
8388608000000000,3,0
16777216000000000,1,0
33554432000000000,5,0
67108864000000000,5,0
134217728000000000,115,1
268435456000000000,343,3
536870912000000000,575,5

1068 nodes and 9 candidates, candidate-list SHA256 8ecd79980293bda22f6750ae91b58c9933d2a39cbe1f3c71f38a3d0d4641aa9e. Width <1 on the entire range by the inherited boxes and the explicit bound. Direct normalized signed BRC oracle determined seven candidates with the refined anchor. Two (m=311988139189266965 and m=508385525950586032) remained undecided at radius 9.82e-27, not exact zeros. New anchor [4400,4800,5200,5600], degree298, total radius about 2.145301926510913e-31 resolved both. Final exact outward certificate below: same G=10^70, L,U center endpoints and E radius upper endpoint. Thus positive iff L>E and negative iff U<-E in these rows.

m,j,L,U,E,sign
214701672941087809,4603211751789230861,-788730433492462895973033543284825111527895089,-788730433492462895973033543284825111527895088,98208692987205456766846586969140933867948277,-1
311988139189266965,6689037160548598982,70739846110743807486115457668869926997113010,70739846110743807486115457668869926997113011,2145301926510912856338471472613106822334,+1
409274605437446121,8774862569307967103,-643211032483585187074282385640662031286262517,-643211032483585187074282385640662031286262516,98208692987205458185559833467256002094588832,-1
508385525950586032,10899804344502792675,-56313401903510194910692244046783307223506406,-56313401903510194910692244046783307223506405,2145301926510912873617954050012819165222,-1
607496446463725943,13024746119697618247,162598407984846607521483135289828153795110201,162598407984846607521483135289828153795110202,98208692987205458696365129468254473524803952,+1
706607366976865854,15149687894892443819,232041968517654303789081483373340504582359049,232041968517654303789081483373340504582359050,98208692987205458844297096885846896820499630,+1
805718287490005765,17274629670087269391,235718293899294190677625090170249207480823906,235718293899294190677625090170249207480823907,98208692987205458955835020152616441669586553,+1
904829208003145676,19399571445282094963,209484121561603937067313432814710646965105186,209484121561603937067313432814710646965105187,98208692987205459042938218834269587658581906,+1
1003940128516285587,21524513220476920535,169966883870317373896135295488161243503530815,169966883870317373896135295488161243503530816,98208692987205459112843423420958351529254398,+1

## 5. Finite theorem with no remaining candidate exceptions

Under the inherited observer, band and monotonicity hypotheses, for all integers 100000000 <= m < 1073741824000000000,

Klast(m)=floor( (21440036720404643983274790532018959153833541/10^42)*m
                + 198282020875361309249001917399666/(2*10^30)
                + 19381725319283097639924876692052/(2*10^30*m) ).

The displayed slope is strictly inside the refined box; c,d are the previous midpoints. For points excluded by the strip, every point in the box has the same floor, so this representative is exact for that integer observation. All nine retained candidates were tested against this same formula with exact rational comparisons, zero overrides. Old certified windows remain covered by nesting of the new rho interval and inherited c,d intervals; 39 old 1110 closures supported by the raw replay, and all 13 further old candidates excluded. Thus the entire range is contiguous and contains 1073741823900000000 integer scales, zero remaining undecided. No extrapolation outside this finite interval. Independent review remains pending.

## 6. Local evidence provenance and next question

Actual local executed scripts/results SHA256:
a905181441adf83cedf6f2bf296fd55b16691fe142168e20c9ce74140bd72f1f replay.py
bd94300f4ad8756f900bd1233c97e837668749afbfcfffb47e112f5f5c645c60 refine.py
8eeba0346ca7274c5d9129dd5079bf0d06b1e52184d169b9a8f820697f442070 sieve.py
4d2bc6d581546b6183744925869ce1b3c001169edf08753058dcf5f7b246878b close.py
8e7c3cf48da6a7344665cab492bd3460d6f10112f43a89b7e0caaf6d535fc6cb final_close.py
81a7c3729d1bb304cd29183b03c88f4c87bcfb20e4a3b5ea5887094eec2de772 replay_result.json
c11a1e77d6eec573ce6b0308b4d222d82b0d5de254ea5dc9710fc0a959e87260 refine_result.json
c83a6758977a94782dbffd94d28c99bffd521e67e4bc3e6164fdf2339cefdf46 sieve_result.json
662210f01c721940934b5a64112c7b775d04d36478a96ffbdecbf975e715a299 close_result.json
b8e1502d50f0f5b505d4d11064d383d96631e3a8a87d77fa9e09a7428f3ff14b final_close_result.json

Next: derive joint correlated enclosure for rho,c,d (or higher-order expansion) from refined signed observations at multiple scales, instead of treating fixed c,d boxes as permanent limits. Establish quantitative precision/cost requirements and global arithmetic separation; exact-zero question, remaining spectrum zeros and mother objective open.

Owner read: r6-20261126-2150-owner-read-v1 SUCCEEDED/error=null, source 8eaa76b72b370162441ddc7914949a7971154976, as-of 2026-11-26T13:51:09.374823+00:00, LEASED tasks=[], next_cursor=null. Own identity original registration recovered, no new claim or shared task state changes.
