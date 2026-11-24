# PREFIX-1061 — Exact rational generating packet for two-negative grade

Date: 2026-11-24. Parent PREFIX-1060. AUTHOR_CONDITIONAL_EXACT_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable research; no formal Task CLAIM asserted.

## Frozen input and scope
P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Parent d0093b79fd2642aad53e744fbcaccd53027402a3:research_notes/portable_direct/2026-11-24_r6_prefix1060_grade2_first_hit_counterexample.md, blob e831c4e398b0d63006798ccff24f7149d3b3c024. Reuse positive N[Z2] BRC phase-cover rule, PREFIX1004_R6_MARKED_COLLISION_CHECK.py@b5976b3fa4254309cb00a23f8f944cbe1845cfeb, grade ceiling extended to 2 in PREFIX-1060. Stage46 candidate, X6 affine torsor, chart anchor O, incoming -e1, signed weight 1-6[h=d], next incoming -d, both orientations of Link {O,e1} blocked without renormalization. Underlying labelled branch law retains order, Cell, port, grade, phase, multiplicity and provenance. The formulas are scoped exact terminal signed readouts, not a new geometric model or canonical native kernel revalidation. No external comparison or pi/trigonometric calculation.

## 1. Exact positive-block BRC factorization

Let z_i mark raw displacement +e_i, b_i=z_i^-1, S=sum_i z_i, t mark positive-step count P (not physical time), R=1-tS. Grade is exactly 2; n=P+2. Write w_i=1-6 delta_(i,1), v_ij=1-6 delta_(i,j), L_i=S-6z_i, K_ih=S-6(z_i+z_h)+36 delta_(i,h) z_i. All are formal Laurent readouts. Signs are taken by the multiplicative q->-1 character of N[Z2]; summations correspond to disjoint ordered branch families.

For a positive block before the first negative direction -e_i, the factor is w_i for length zero and L_i S^(a-1) for length a>=1. Its generating packet is A_i/R, A_i=w_i R+t L_i. For a nonempty final positive block after -e_h and with last positive direction +e_j, the factor is z_j v_hj at length one and z_j L_h S^(c-2) at length c>=2; its packet is z_j t C_hj/R, C_hj=v_hj R+t L_h. The middle positive block between -e_i and -e_h has weight 1 when absent, K_ih at length one, and L_i L_h S^(b-2) at length b>=2. Its packet is (R+B_ih)/R, B_ih=t K_ih R+t² L_i L_h. Each boundary factor is a reversal weight if the adjacent positive direction matches the negative axis, and all same-sign transitions have weight 1. For middle block length one both boundary weights attach to the same direction, giving K_ih rather than two independent factors. This is the joint residual lost by treating all separated negatives as independent.

L_i L_h-S K_ih=36(z_i z_h-delta_(i,h) S z_i), so B_ih has degree <=2 in t. Its diagonal correction is retained.

With U_j=sum_(i,h) b_i b_h A_i C_hj (R+B_ih), V_j=sum_i b_i A_i C_ij, the free positive-terminal grade-two packet is z_j t U_j/R³, and grade-one packet is z_j t V_j/R². A grade-zero suffix from initial +e1 has positive-port packet z_j t C_1j/R; from -e1 it is delta_(j,1)+z_j t/R, including the empty continuation whose incoming port remains -e1. The ordered decomposition into first positive block, negative, middle positive block, negative, last positive block is bijective; block expansion by the signed character gives the same terminal amplitudes. Grade-one/zero formulas follow by deleting the appropriate blocks. All six relative components remain in the monomials; full phase-cover remains in the underlying law. This readout is used only for the terminal coherent pair, not as replacement for history-dependent future operations.

## 2. Absorbing-link correction and bounded polynomial representation

Use the PREFIX-1060 first-hit signed kernel: forward grade 0 =1 at length 1, forward grade 1 =-25 at length 3, reverse grade 2 =10 at length 4, forward grade 2 =390 at length 5. Positive counts are respectively 1,2,2,3. Translate forward prefix by z_1 and use correct suffix incoming port. Subtract the disjoint first-hit prefix families to obtain masked positive-port packet

M_j(t,z)=z_j t N_j(t,z)/R³,

N_j=(1-z_1 t)U_j +25 z_1 t² R V_j -10 t² R² C_1j -390 z_1 t³ R² -390 delta_(j,1) t² R³.

The last term is essential at n=5: forward grade-two first hit with empty suffix is already a positive terminal port 1. The first checker attempt omitted that term and failed at n=5, port 1. It was corrected before publication. This term has no effect at n>=6. The identity is valid coefficientwise for P>=1. N_j has t-degree <=5. Expanding R^-3 gives exact finite formula, N_jd=[t^d]N_j:

M_(n,j)(z)=z_j sum_(0<=d<=min(5,n-3)) N_jd(z) binom(n-1-d,2) S^(n-3-d).

For n>=8 write M_(n,j)=z_j S^(n-8) H_(n,j), H_(n,j)=sum_(d=0)^5 N_jd binom(n-1-d,2) S^(5-d). H is Laurent polynomial of fixed finite support with polynomial coefficients of degree <=2 in n. This gives a single formula for adjacent and separated cases and all masked corrections. No path enumeration at larger n is mathematically necessary for the signed terminal packet. Not a claim of lower total bit complexity: computing coefficient contractions still has cost.

## 3. Exact reduction to finite shifted A6 coherent-pair family

Define star by z_i->z_i^-1 with integer coefficients unchanged. Q_(n,j)=CT(M_(n,j) M_(n,j)^star) follows by full six-coordinate equality of paired monomials, not a marginal projection. Put Y=S S^star. For n>=8,

Delta_n^(2)=CT[Y^(n-8) (H_(n,1) H_(n,1)^star-H_(n,2) H_(n,2)^star)].

Expand bracket as sum_(a=0)^4 n^a J_a(z), J_a fixed Laurent polynomials (rational coefficients allowed because binomials are polynomials in n). Thus exact grade-two observation is a fixed finite sum of shifted A6 moments CT(z^v Y^m), multiplied by polynomials in m=n-8 of degree <=4. The shifts retain six-coordinate pair relation. Eventual complete monotonicity reduces to analysis of this finite signed spectral family and polynomial-in-index operations. The sign of components and positive tail measure remain open.

## 4. Exact verification
Embedded JS implements Laurent block identity and independently traverses inherited positive N[Z2] phase-cover recurrence with explicit parity, all six coordinates, port and grade, n=5..9. It compares every nonzero signed terminal fibre at ports 1 and 2 (including support equality), and parent Delta n=5..9. For n=10..12 it evaluates proved formula only. It checks all differences with n>=5 and n+k<=12, common denominator 36^12; lists every nonpositive value. BigInt for weights and comparisons. Bounded binomial factors are exact small integers. Native canonical kernel execution and independent mathematical review pending.

```js
function check(){
 const D=6,zero=Array(7).fill(0),key=v=>v.join(","),vec=k=>k.split(",").map(Number),mon=(v,w=1n)=>new Map([[key(v),w]]),one=mon(zero),variable=i=>mon(zero.map((_,j)=>+(i===j))),t=variable(0),z=Array.from({length:D},(_,i)=>variable(i+1)),b=Array.from({length:D},(_,i)=>mon(zero.map((_,j)=>-(i+1===j))));
 function put(m,k,w){const v=(m.get(k)||0n)+w;if(v)m.set(k,v);else m.delete(k)}
 function sum(...ms){let o=new Map();for(const m of ms)for(const [k,w] of m)put(o,k,w);return o}
 function scale(m,c){return new Map([...m].filter(()=>c!==0n).map(([k,w])=>[k,w*c]))}
 function mul(...ms){let o=one;for(const m of ms){let p=new Map();for(const [k,w] of o)for(const [l,v] of m){let a=vec(k),b=vec(l);put(p,key(a.map((x,i)=>x+b[i])),w*v)}o=p}return o}
 const S=sum(...z),R=sum(one,scale(mul(t,S),-1n)),L=z.map(a=>sum(S,scale(a,-6n))),A=z.map((_,i)=>sum(scale(R,i===0?-5n:1n),mul(t,L[i])));
 const C=(i,j)=>sum(scale(R,i===j?-5n:1n),mul(t,L[i]));
 const K=(i,h)=>sum(S,scale(z[i],-6n),scale(z[h],-6n),i===h?scale(z[i],36n):new Map());
 const B=(i,h)=>sum(mul(t,K(i,h),R),mul(t,t,L[i],L[h]));
 function numerator(j){
  let u=new Map(),v=new Map();
  for(let i=0;i<D;i++){
   v=sum(v,mul(b[i],A[i],C(i,j)));
   for(let h=0;h<D;h++)u=sum(u,mul(b[i],b[h],A[i],C(h,j),sum(R,B(i,h))));
  }
  return sum(mul(sum(one,scale(mul(z[0],t),-1n)),u),
    scale(mul(z[0],t,t,R,v),25n),scale(mul(t,t,R,R,C(0,j)),-10n),scale(mul(z[0],t,t,t,R,R),-390n),
    j===0?scale(mul(t,t,R,R,R),-390n):new Map());
 }
 const N=[0,1].map(numerator),powers=[one];for(let i=1;i<=11;i++)powers.push(mul(powers[i-1],S));
 function predicted(n,j){
  let out=new Map();
  for(const [k,w] of N[j]){let a=vec(k),d=a[0],m=n-3-d;if(m<0)continue;
   let c=BigInt((m+1)*(m+2)/2);a[0]=0;a[j+1]++;
   for(const [l,v] of powers[m]){let h=vec(l);put(out,key(a.slice(1).map((x,i)=>x+h[i+1])),w*v*c)}
  }return out;
 }
 const O=Array(D).fill(0),E=[1,0,0,0,0,0],eq=(a,b)=>a.every((x,i)=>x===b[i]);
 let states=new Map([[key([...O,6,0,0]),1n]]);
 const rows=[];let fibres=0;
 for(let n=1;n<=12;n++){
  if(n<=9){
   const next=new Map();
   for(const [k,w] of states){const a=vec(k),x=a.slice(0,D),[h,g,p]=a.slice(D);
    for(let d=0;d<12;d++){let r=g+(d>=6?1:0);if(r>2||(d===0&&eq(x,O))||(d===6&&eq(x,E)))continue;
     let y=x.slice();y[d%6]+=d<6?1:-1;let rev=h===d;
     put(next,key([...y,(d+6)%12,r,p^(rev?1:0)]),w*(rev?5n:1n));
    }
   }states=next;
  }
  if(n<5)continue;
  let qs=[];
  for(let j=0;j<2;j++){
   const a=predicted(n,j);
   if(n<=9){let actual=new Map();for(const [k,w] of states){let v=vec(k);if(v[6]===j+6&&v[7]===2)put(actual,key(v.slice(0,6)),v[8]?-w:w)}
    if(a.size!==actual.size||[...actual].some(([k,v])=>a.get(k)!==v))throw Error("Mismatch "+n+" "+j+" "+a.size+" "+actual.size);
    fibres+=actual.size;
   }qs.push([...a.values()].reduce((s,v)=>s+v*v,0n));
  }rows.push([n,...qs.map(String),String(qs[0]-qs[1])]);
 }
 const expected=["-637488","703968","33444384","868556808","20857505436"];
 if(expected.some((v,i)=>rows[i][3]!==v))throw Error("Parent mismatch");
 let differences=rows.map(a=>BigInt(a[3])*36n**BigInt(12-a[0])),violations=[];
 for(let k=0;differences.length;k++){for(let i=0;i<differences.length;i++)if(differences[i]<=0n)violations.push([i+5,k,String(differences[i])]);differences=differences.slice(0,-1).map((v,i)=>v-differences[i+1]);}
 return {status:"PREFIX1061_GRADE2_RATIONAL_PACKET_CHECK_PASSED",numerator_terms:N.map(m=>m.size),max_t_degree:N.map(m=>Math.max(...[...m.keys()].map(k=>vec(k)[0]))),signed_fibres_checked:fibres,rows,nonpositive_differences_common_denominator_36_pow_12:violations};
}
console.log(JSON.stringify(check(),null,2));
```
Actual output:
```json
{
  "status": "PREFIX1061_GRADE2_RATIONAL_PACKET_CHECK_PASSED",
  "numerator_terms": [
    270,
    258
  ],
  "max_t_degree": [
    5,
    5
  ],
  "signed_fibres_checked": 14836,
  "rows": [
    [
      5,
      "266450",
      "903938",
      "-637488"
    ],
    [
      6,
      "10837540",
      "10133572",
      "703968"
    ],
    [
      7,
      "249963600",
      "216519216",
      "33444384"
    ],
    [
      8,
      "6109313340",
      "5240756532",
      "868556808"
    ],
    [
      9,
      "153545883900",
      "132688378464",
      "20857505436"
    ],
    [
      10,
      "3965127779880",
      "3461706785472",
      "503420994408"
    ],
    [
      11,
      "105133565912460",
      "92632139548620",
      "12501426363840"
    ],
    [
      12,
      "2858221141689660",
      "2537278032203124",
      "320943109486536"
    ]
  ],
  "nonpositive_differences_common_denominator_36_pow_12": [
    [
      5,
      0,
      "-49956214241230848"
    ],
    [
      5,
      1,
      "-51488599348740096"
    ],
    [
      6,
      1,
      "-489868901646336"
    ],
    [
      5,
      2,
      "-50998730447093760"
    ],
    [
      6,
      2,
      "-1053280999176192"
    ],
    [
      5,
      3,
      "-49945449447917568"
    ],
    [
      6,
      3,
      "-1130978958702336"
    ],
    [
      7,
      3,
      "-87322013608320"
    ],
    [
      5,
      4,
      "-48814470489215232"
    ],
    [
      6,
      4,
      "-1043656945094016"
    ],
    [
      7,
      4,
      "-134030081528064"
    ],
    [
      5,
      5,
      "-47770813544121216"
    ],
    [
      6,
      5,
      "-909626863565952"
    ],
    [
      7,
      5,
      "-135700264275912"
    ],
    [
      5,
      6,
      "-46861186680555264"
    ],
    [
      6,
      6,
      "-773926599290040"
    ],
    [
      5,
      7,
      "-46087260081265224"
    ]
  ]
}
```

## 5. Continuation
Derive/reuse exact signed A6 spectral identities for J_a shift family. Move polynomial-in-n factors into distributional Euler derivatives only with verified boundary terms. Determine whether resulting signed spectral distribution has negative interior part (no finite shift repairs that), or prove it nonnegative after some shift. Finite checks do not settle unbounded quantifiers. Mother B_fix,odd(32) in {19,20} and native kernel revalidation remain open. Historical session MCP-f6d93209fc8e4c5bb2c3b44f69a47174 and Activity RA-0ABD84561C86E53067DB0322 read on Source; current private session authority not inferred. Owner query r6-20261124-1950-sites-leased-observe-v1 RUNNING at last read before publication.
