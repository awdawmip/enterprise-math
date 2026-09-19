# 倒数壳层迁移到 X6 原生坐标 / Native X6 reciprocal-shell migration

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `reciprocal-native-x6-20260919-AD0416`
Status: `RESEARCH_NOTE / DERIVED_IDENTITIES / EXACT_COUNTEREXAMPLE / FINITE_CHECKS`
Authority: no formal Task-ID, CLAIM, independent review, Working Truth or Foundation promotion.
Question: 用户要求将上一轮倒数 FCC 壳层实验“挪到进取原生坐标系试试”。
Read snapshots: GLOBAL_KNOWLEDGE `fc09356869f2dfd9d9c4c3c65ef9d7baa38c55bf`; EM `00a52a999cb14ace6a77d57c8c35fdc91edfb645`.
Continuation: existing activity/session `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b`; this is a locally assigned conversation key, not a platform-authenticated ID.

## 1. Exact source and experiment scope

Current EM sources at the above immutable revision:
- `p000_reality_foundation.json`;
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, especially sections 2-12;
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.

The admitted native spatial Cell-center model is a torsor over Z^6 with signed primitive directions +/-e_i. Choose one native Cell anchor c_*; z denotes raw relative displacement coordinates, not a final Cell address. No absolute ontic origin, new spatial axis, change of P000 120-degree orthogonality, or FCC kernel quotient is introduced.

The source distinguishes minimum primitive step count N_min(z)=sum|z_i| from component length L_E(z)=sqrt(sum z_i^2). To migrate the SAME previous experiment, index shells by minimum primitive step count, not by component-metric radius:

S_n={z in Z^6: ||z||_1=n}, R_n={z/n:z in S_n}, n>=1.

All R_n lie on the rational observation surface sum|q_i|=1. This is scalar reciprocal normalization by 1/n, not coordinatewise reciprocals, physical subdivision of Cells, or a final address codec. Retain (n,z,path/branch data) behind q. Endpoint coordinate identity is not full decorated packet identity.

BRC resolution: REUSE_APPLIED, using exact native source sections 10-12: ordered shortest paths have multiplicity n!/product |z_i|!, and path identity/weights remain richer than endpoints. Population and future operations: signed-axis paths from one anchor, shell scaling, exact coordinate comparison, common-depth observation, and declared positive reciprocal weighting. No compression is certified for arbitrary later hidden-state operations. All integer layers, including composites, are retained.

## 2. Native gcd overlap survives

In the fixed native lattice chart,

(1/m)Z^6 intersect (1/n)Z^6 = (1/g)Z^6, g=gcd(m,n).

For one coordinate, write m=ga,n=gb with gcd(a,b)=1. If x/m=y/n then bx=ay, so x=ak,y=bk and the common value is k/g. The reverse inclusion is immediate. Apply independently to six components, then intersect with the common surface ||q||_1=1:

R_m intersect R_n = R_gcd(m,n).

Also m|n iff R_m subseteq R_n. The forward direction is scaling; the reverse follows from the intersection identity and strictly increasing shell counts proved below.

If z in S_n and t=gcd(|z_1|,...,|z_6|), then t divides n. Write z=t*a and d=n/t=||a||_1. The exact birth denominator of q=z/n=a/d is d, since gcd(a_1,...,a_6)=1. Hence q occurs precisely at layers d,2d,3d,... . This is an equality of normalized coordinate observations, not identification of actual Cells at different layers.

The admitted S6 positive-axis permutation skeleton preserves these sets and formulas. No claim about complete native rotations, independent backgrounds, channel state or time dynamics follows.

## 3. Native shell and birth counts

To count S_n, choose s nonzero axes, their signs, and a positive composition of n into s parts:

C6(n)=sum_{s=1}^{min(6,n)} 2^s binom(6,s) binom(n-1,s-1)
     =(8n^5+80n^3+92n)/15, n>=1.

Strict increase follows, for example, by injecting each signed s-part composition into the next layer by increasing its first part; the two-axis stratum supplies strict growth. In particular C6(1)=12, C6(2)=72, C6(3)=292. The previous FCC formula 10n^2+2 is not a native X6 count. The fifth-degree boundary growth follows from the declared six-coordinate step shell, not a redefinition of native dimension or metric.

Let B_n be normalized points first born at n, P6(n)=|B_n|. Exact denominators give the disjoint decomposition R_n=disjoint_union_{d|n} B_d. Thus C6(n)=sum_{d|n}P6(d). Mobius inversion yields

P6(n)=[8J_5(n)+80J_3(n)+92J_1(n)]/15,
J_k(n)=n^k product_{p|n}(1-p^(-k)).

This holds also at n=1, with J_k(1)=1 and P6(1)=12. It is NOT just a constant times J_5(n). Existing visible-point/Jordan-totient theory is prior-art background, not a novelty claim; abstract checked: https://arxiv.org/abs/1212.2818 .

For n>1, n is prime iff exactly twelve R_n points are inherited. Prime layers inherit only R_1. A composite n has a proper divisor d>=2, and inherits the larger R_d. This is not a complexity-efficient primality algorithm claim, and does not erase composite layers or their joint relations.

|n|C6(n)|P6(n)|inherited|
|--:|--:|--:|--:|
|1|12|12|0|
|2|72|60|12|
|3|292|280|12|
|4|912|840|72|
|5|2364|2352|12|
|6|5336|4984|352|
|7|10836|10824|12|
|8|20256|19344|912|
|12|142000|135824|6176|

The spatial support kernel is K_mn=C6(gcd(m,n)). If A_nd=1[d|n], then K=A diag(P6(d)) A^T. This supplies positive definiteness and determinant product P6(d) for any finite initial block, without granting other spectral/arithmetic conclusions.

## 4. Exact information-loss witness: common depth is indispensable

Extend the source's raw min-zero observer to normalized rational readouts:

r(q)=q-min(q)*D, h(q)=min(q), D=(1,1,1,1,1,1).

(q -> (r,h)) is lossless; q -> r alone is not. This is an auxiliary readout extension, not a new native Cell or final-address codec.

Take
u=(3,-1,-1,-1,-1,-1)/8 in R_8,
v=(7,1,1,1,1,1)/12 in R_12.

Both have L1 norm one and are distinct. Yet
r(u)=r(v)=(1/2,0,0,0,0,0),
h(u)=-1/8, h(v)=1/12,
v-u=(5/24)D !=0.

All twenty normalized min-zero three-axis observations also agree, because their inputs differ by one common offset. But this shared relative readout is not in r(R_4). A putative lift in layer four would require integer z=(k+2,k,k,k,k,k) with |k+2|+5|k|=4. For k>=0 the left side is 6k+2; k=-1 gives 6; k<=-2 gives at least 10. No integer k works.

Consequently
r(R_8) intersect r(R_12) strictly contains r(R_4),
although R_8 intersect R_12=R_4.

This is a finite exact counterexample to descending the native gcd identity through the joint relative observer. Repair by retaining h, or full q. It is not a counterexample to P000, full X6 or the proven native formula.

## 5. BRC path multiplicity changes reciprocal accumulation

For q=a/d born at d=||a||_1, the layer n=kd endpoint is k*a. The existing native shortest-path law gives

M_k(a)=(kd)! / product_i (k|a_i|)!.

If every endpoint occurrence is assigned weight 1/(kd) ONCE, its accumulated mass through N remains H_floor(N/d)/d.

If instead EVERY ordered shortest path receives that weight, the exact mass is

W_N^path(q)=sum_{k=1}^{floor(N/d)} M_k(a)/(kd).

These are different declared observers; the second is not a probability normalization or a physical mass assertion. Keep branch IDs/steps for later order-sensitive questions; M_k alone only certifies the present equal-weight count.

For q=(1/2,1/2,0,0,0,0), d=2, M_k=binom(2k,k). At layers 2,4,6,8,10,12 the path counts are 2,6,20,70,252,924; per-layer reciprocal masses are 1,3/2,10/3,35/4,126/5,77. Through layer12, endpoint-once mass is 49/40, path mass is 7007/60.

For a single-axis direction, d=1 and M_k=1, so the path and endpoint observers coincide. For any primitive a supported on at least two axes, choose two active axes and interleave their first k steps in 2^k distinct ordered adjacent pairs, while fixing all remaining steps. This injects 2^k paths into the minimum-path family. Therefore M_k>=2^k: reciprocal weighting does not suppress the combinatorial growth under the unnormalized path observer.

Even the unweighted path-multiplicity Gram kernel ceases to depend on gcd alone. Define
T_mn=sum_{q in R_m intersect R_n} M_m(q)M_n(q),
where M_n(q)=n!/product |nq_i|!.
Then T_2,2=252 but T_2,4=732, though both gcds are 2. There are 12 axis points of multiplicity1 and 60 two-axis points: multiplicities2 at layer2 and6 at layer4. Multiplying path masses by 1/n changes these entries to T_mn/(mn), but does not remove their structural distinction.

## 6. Executed finite certificates

Standard-library exact checker `verify_native_reciprocals.py`:
- direct signed-six-coordinate shell enumeration through n=12;
- 369304 shell incidences; 369305 ball points including the chosen anchor;
- 359016 distinct reciprocal-normalized points;
- all 78 unordered layer intersections, shell/birth counts and denominator strata checked;
- independent ordered-walk dynamic programming through length8, checking 40080 shortest-endpoint multiplicities and twelve-choice walk totals;
- common-depth failure witness and exact reconstruction checked;
- endpoint/path mass contrast and Gram entries 252/732 checked.

All assertions passed. The all-n conclusions follow from the written proofs, not finite enumeration. No independent reviewer, Lean formalization, global prior-art audit, complete native dynamics or theorem admission is claimed.

Checker SHA256: `6bf0c461a90532f21b365305be6d4cfa0343d572168a00d597a25ee80313fe4b`.
Results SHA256: `6c2cb982cf971233ff6f3631f1d280d6cf1e853398c847f6fceeb979ee4e04db`.
Local files and JSON results are supplied together as the reproducibility package; this note is the project durable mathematical frontier.

## 7. Next exact frontier

The requested step-shell migration is completed. The nontrivial next question is to classify the path-weighted layer kernel with retained native direction/common-depth data: which part is determined by divisor incidence and which part requires multipath interaction coordinates? Do not replace it by a gcd-only support kernel. Component-metric-radius shells ||z||_2=n would constitute a distinct next experiment with a different counting problem, not an unreported change to this one.
