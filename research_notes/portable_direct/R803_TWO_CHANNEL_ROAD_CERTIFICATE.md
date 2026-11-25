# R803 — Two-channel road certificate and sharp rank-one exponent

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R802, fixed source 0529f92c7063ba89115f344647451ac968f5a736:research_notes/portable_direct/R802_DEGREE_TWO_TRANSFER_AND_CERTIFIED_ROAD_CUT.md; R801 at 202e892e89ada1986fb673cb3ff25d68a5a65727:research_notes/portable_direct/R801_POSITIVE_CLUSTER_RESIDUAL_AND_LEAF_CONDENSATION.md. Prior line EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 is historical provenance; current private session possession unconfirmed. Owner inventory original request r3-20261126-0423-owner-read last observed RUNNING before this computation; no shared claim or control mutation. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read. ACTIVE worldview, current portable/continuation/method and relevant account rules read. Canonical account entries verified at ad6784650cf42c8052efb7450ac51520d6645baf. Auxiliary unsigned aligned positive observer only; preserve full ordered road and native signed/provenance/time/depth state separately.

## 1. Exact residual channels

R802 gives M(a)=[[2a,1,1],[1,1,0],[1,0,1]] for 7/8<=a<=1. For ell>=2 let P=product of M(a_i) in road order. In the symmetric (x,y,y) sector N(a)=[[2a,2],[1,1]], while the antisymmetric (0,1,-1) sector is exactly 1. Write N product=[[A,2B],[C,D]], and E=det(N product)=product_i(2a_i-2). Thus P=[[A,B,B],[C,(D+1)/2,(D-1)/2],[C,(D-1)/2,(D+1)/2]]. All entries positive for ell>=2. In particular AD-2BC=E.

Let R=P[:,0]P[0,:]/A, j=(0,1,-1)^T, h=(0,1,1)^T. Exact identity:
 P = R + jj^T/2 + (E/(2A)) hh^T.
This separates the anti-channel (not a physical signed amplitude) and the symmetric determinant residual exactly. Define T=R+jj^T/2. The residual is pointwise nonnegative for even ell and nonpositive for odd ell (zero if any a_i=1). R and T retain all row/column zero entries exactly. P has rank 2 if any a_i=1 and rank 3 otherwise, since antisymmetric eigenvalue is 1 and N determinant E. T is always rank 2.

## 2. Uniform certificates and optimal rank-one rate

Set u=7^(-ell) and d_ell=(N(7/8)^ell)_{22}, with d_0=d_1=1, d_l=(11/4)d_{l-1}+(1/4)d_{l-2} for l>=2. All matrices nonnegative and monotone in a, so D>=d_l. Also A>= (7/4)^ell and |E|<=(1/4)^ell, hence |E|/A<=u. Since 2BC/A=D-E/A>=d_l-u>1 (d_2=3), T is strictly positive. The exact worst entrywise relative errors, with respect to R and T respectively, are
 e1=(A+|E|)/(2BC),
 e2=|E|/(2BC-A).
These follow directly from the +/- block, whose smallest T entry is BC/A-1/2. Consequently
 |P_ij-R_ij|<=b1 R_ij, b1=(1+u)/(d_l-u);
 |P_ij-T_ij|<=b2 T_ij, b2=u/(d_l-u-1).
Both b<1 for ell>=2. These are rational certificates computable in O(ell) arithmetic operations, with bit cost separately accounted. For T, one can use the one-sided interval [T,(1+b2)T] if ell even and [(1-b2)T,T] if odd.

Let lambda=(11+sqrt(137))/8 be the larger characteristic root of the recurrence (the other root is negative and smaller in absolute value). d_l=Theta(lambda^l), as the coefficient of lambda^l is positive from d_0=d_1=1. Therefore b1=O(lambda^-ell) and b2=O((7lambda)^-ell), whereas R802's uniform bound decays like 3^(-ell/2). The rank-one exponential rate is sharp over all positive rank-one approximants in the worst-case activity sequence: take all a=7/8, then D=d_l; for any positive rank-one R' with R'/K<=P<=K R', the cross ratio on +/- rows and columns forces K^4 >= ((D+1)/(D-1))^2, because the cross ratio of R' is 1. Hence K>=sqrt((D+1)/(D-1)), which gives K-1=Omega(lambda^-ell). This establishes the sharp uniform exponential order, not the exact optimal constants. The symmetric determinant channel gives a substantially faster second approximation without falsely erasing the antisymmetric channel.

## 3. Nonnegative two-channel representation and network certificate

Write T as half the sum of two nonnegative outer products:
 u+=(A,2C,0)^T, u-=(A,0,2C)^T,
 v+=(1,B/A+1/(2C),B/A-1/(2C)),
 v-=(1,B/A-1/(2C),B/A+1/(2C)).
Then T=(u+ v+ + u- v-)/2. Positivity of the v entries follows from 2BC>A. This realizes a binary latent road label with nonnegative endpoint unaries, rather than nine endpoint combinations or a signed correction. Exact if any a_i=1. It retains a connection (unlike R), so only rank-one approximated roads split a network.

For a finite nonnegative tensor network of R802, select pairwise internally disjoint maximal roads, use R or T, and preserve the exact ordered road and all residual data. For each factor choose b_e=b1 or b2. Since every summand is nonnegative, product of (1-b_e) and (1+b_e) bounds the ratio of the exact to approximate contraction, including arbitrary nonnegative endpoint observations. For T use the tighter one-sided factors by parity, and for any unchanged road use 1. This certifies a mixed rank-one/rank-two resource allocation. Each T road needs one binary shared label, each R road contributes only independent endpoint unaries. With short unchanged roads treated by enumerating their endpoint incidence labels, the nonnegative contraction can be evaluated in O(poly(N) 2^r 3^h) arithmetic operations for r rank-two roads and h remaining incidences, or componentwise after R cuts. At a branching vertex, once incident shared states are fixed, its local unary contraction is prod(w0+w+)+prod(w0+w-)+(2a-2)prod(w0) (the all-zero assignment is counted twice and then corrected); this is the exact sum of nonnegative original local weights. Rank-two compression does not claim to remove treewidth in general. Input transformation and full exact P formation take O(N) fixed-size rational matrix operations; rational bit lengths depend on total input bit length and products. No runtime benchmark or native BRC physical claim.

## 4. Exact finite evidence

Executed the JavaScript BigInt checker below. It independently multiplies original three-state matrices scaled by 16, compares determinant product and exact residual identity, both uniform certificates by cross multiplication, and binary factorization. Exhausts all 3^ell sequences for ell 2..9 over {7/8,15/16,1}, checks one deterministic mixed sequence for each ell=10..80, plus homogeneous minimum cases. Finite checks support the analytic proof; no new native XOR execution. Decimal examples are display-only; assertions use exact integers.

```json
{
  "matrices": 29598,
  "entries": 266382,
  "channels": 266382,
  "exactRank2": 28571,
  "examples": [
    {
      "l": 2,
      "old": 2,
      "new1": 0.3424657534246575,
      "new2": 0.010309278350515464,
      "actual1": 0.33884297520661155,
      "actual2": 0.006211180124223602
    },
    {
      "l": 4,
      "old": 0.6666666666666666,
      "new1": 0.04146875708104492,
      "new2": 0.000018010838021779607,
      "actual1": 0.04145491494918704,
      "actual2": 0.0000041448694029367436
    },
    {
      "l": 8,
      "old": 0.07407407407407407,
      "new1": 0.0006388962182174668,
      "new2": 1.1089794020348955e-10,
      "actual1": 0.0006388961110089705,
      "actual2": 3.689400046681732e-12
    },
    {
      "l": 12,
      "old": 0.00823045267489712,
      "new1": 0.00000984752575526349,
      "new2": 7.114672635763971e-16,
      "actual1": 0.000009847525754555444,
      "actual2": 3.421655401222272e-18
    },
    {
      "l": 16,
      "old": 0.0009144947416552355,
      "new1": 1.5178330619867362e-7,
      "new2": 4.567256833367703e-21,
      "actual1": 1.5178330619866906e-7,
      "actual2": 3.175308013899881e-24
    },
    {
      "l": 24,
      "old": 0.000011290058538953524,
      "new1": 3.605934012842852e-11,
      "new2": 1.8821958638578091e-31,
      "actual1": 3.6059340128428524e-11,
      "actual2": 2.7345973960900763e-36
    },
    {
      "l": 32,
      "old": 1.3938343875251265e-7,
      "new1": 8.566660214897184e-15,
      "new2": 7.756651172981428e-42,
      "actual1": 8.566660214897186e-15,
      "actual2": 2.355054697203427e-48
    }
  ],
  "mismatches": 0
}
```

```javascript
function verify(){
 const assert=(x)=>{if(!x)throw Error("mismatch")}, abs=x=>x<0n?-x:x, I=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]], M=b=>[[2n*BigInt(b),16n,16n],[16n,16n,0n],[16n,0n,16n]], mul=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0n)));
 const min=[1n,4n];for(let i=2;i<=80;i++)min.push(11n*min[i-1]+4n*min[i-2]);
 let matrices=0,entries=0,channels=0,exactRank2=0;const examples=[];
 function check(P,l,detProduct){
  let S=16n**BigInt(l), A=P[0][0],B=P[0][1],C=P[1][0],D=P[1][1]+P[1][2],det=A*D-2n*B*C,U=7n**BigInt(l),V=4n**BigInt(l),d=min[l],E=abs(det),J=[0n,1n,-1n];
  assert(det===detProduct&&P[1][1]-P[1][2]===S&&P[1][1]===P[2][2]&&P[1][2]===P[2][1]&&P[0][2]===B&&P[2][0]===C);
  assert(E*U<=A*S&&D*V>=d*S&&2n*B*C>A*S);
  let b1num=(U+1n)*V,b1den=d*U-V,b2num=V,b2den=d*U-(U+1n)*V;
  let ul=[[A,2n*C,0n],[A,0n,2n*C]],vr=[[2n*A*C,2n*B*C+A*S,2n*B*C-A*S],[2n*A*C,2n*B*C-A*S,2n*B*C+A*S]];
  for(let i=0;i<3;i++)for(let j=0;j<3;j++){
   let p=2n*A*P[i][j],r=2n*P[i][0]*P[0][j],t=r+A*S*J[i]*J[j];
   assert(r>0n&&t>0n&&abs(p-r)*b1den<=r*b1num&&abs(p-t)*b2den<=t*b2num);
   assert(ul[0][i]*vr[0][j]+ul[1][i]*vr[1][j]===2n*C*t);
   assert(p-t===det*abs(J[i]*J[j]));entries++;channels++;
  }
  if(det===0n)exactRank2++;matrices++;
  return {l,old:2*3**(1-Math.floor(l/2)),new1:Number(b1num)/Number(b1den),new2:Number(b2num)/Number(b2den),actual1:Number(A*S+E)/Number(2n*B*C),actual2:Number(E)/Number(2n*B*C-A*S)};
 }
 function seq(P,l,det){if(l>=2)check(P,l,det);if(l<9)for(let b of [14,15,16])seq(mul(P,M(b)),l+1,det*(32n*BigInt(b)-512n))}
 seq(I,0,1n);
 for(let l=10;l<=80;l++){let P=I,d=1n;for(let i=0;i<l;i++){let b=14+(i*7+l)%3;P=mul(P,M(b));d*=32n*BigInt(b)-512n}check(P,l,d)}
 for(let l of [2,4,8,12,16,24,32]){let P=I,d=1n;for(let i=0;i<l;i++){P=mul(P,M(14));d*=-64n}examples.push(check(P,l,d))}
 return {matrices,entries,channels,exactRank2,examples,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Use the exact residual ratios e1,e2 to choose a globally budgeted cut/retain strategy under graph separation constraints; investigate whether branching-node tensor contractions yield a general direct approximation beyond the long-road regime. Retain raw road, P, E, rank-two and rank-one certificates for all later stronger observations. R802's Activity link remains pending; repair with actual identity/provenance without duplicating its proof.
