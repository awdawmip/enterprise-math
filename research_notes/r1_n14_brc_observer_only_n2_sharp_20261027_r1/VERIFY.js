"use strict";
// Exact rational certificate: run node VERIFY.js; all probabilities are reduced BigInt fractions.
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
class F{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(x){return new F(this.n*x.d+x.n*this.d,this.d*x.d);}
 sub(x){return new F(this.n*x.d-x.n*this.d,this.d*x.d);}
 mul(x){return new F(this.n*x.n,this.d*x.d);}
 div(x){return new F(this.n*x.d,this.d*x.n);}
 eq(x){return this.n===x.n&&this.d===x.d;}
 lt(x){return this.n*x.d<x.n*this.d;}
 str(){return this.d===1n?this.n.toString():this.n+"/"+this.d;}
}
const f=(n,d=1)=>new F(n,d),sum=xs=>xs.reduce((a,b)=>a.add(b),f(0));
const check=(x,name)=>{if(!x)throw Error("FAIL "+name);};
const P=[[f(1,4),f(1,4),f(1,2)],[f(1,12),f(3,4),f(1,6)],[f(1,6),f(1,2),f(1,3)]];
const ratio=[f(2),f(1),f(1,2)],Q=P.map(row=>row.map((x,j)=>x.mul(ratio[j])));
for(const row of P.concat(Q)){check(row.every(x=>x.n>0n),"positive");check(sum(row).eq(f(1)),"row normalized");}
for(let i=0;i<3;i++)for(let j=0;j<3;j++)check(Q[i][j].div(P[i][j]).eq(ratio[j]),"LR fiber");
const avgP=[0,1,2].map(j=>sum(P.map(row=>row[j])).div(f(3)));
const avgQ=[0,1,2].map(j=>sum(Q.map(row=>row[j])).div(f(3)));
check(avgP.map(x=>x.str()).join(",")==="1/6,1/2,1/3","P marginals");
check(avgQ.map(x=>x.str()).join(",")==="1/3,1/2,1/6","Q marginals");
const t2=f(1,3),pHit=t2.mul(P[0][0]),qHit=t2.mul(Q[0][0]);
const fullContrast=qHit.sub(pHit),coarseBound=t2.mul(avgQ[0].sub(avgP[0]));
const gap=fullContrast.sub(coarseBound);
check(pHit.eq(f(1,12))&&qHit.eq(f(1,6)),"full law");
check(coarseBound.eq(f(1,18))&&gap.eq(f(1,36)),"separation gap");
check(new Set(P.map(row=>row[0].str())).size===3,"distinct rows");
function maxContrast(groups,k){
 const bins=groups.map(g=>({weight:f(g.length),value:sum(g.map(i=>P[i][0]))}));
 bins.sort((a,b)=>a.value.div(a.weight).lt(b.value.div(b.weight))?1:-1);
 let rem=f(k),value=f(0);
 for(const b of bins){if(rem.eq(f(0)))break;const rate=rem.lt(b.weight)?rem.div(b.weight):f(1);
  value=value.add(b.value.mul(rate));rem=rem.sub(b.weight.mul(rate));}
 check(rem.eq(f(0)),"knapsack mass");return value.div(f(3));
}
const k1=maxContrast([[0],[1],[2]],1),k2=maxContrast([[0],[1],[2]],2);
check(k1.eq(f(1,12))&&k2.eq(f(5,36)),"top-k max");
const parts=[
 {name:"all_merged",groups:[[0,1,2]]},
 {name:"merge_0_1",groups:[[0,1],[2]]},
 {name:"merge_0_2",groups:[[0,2],[1]]},
 {name:"merge_1_2",groups:[[1,2],[0]]},
 {name:"all_distinct",groups:[[0],[1],[2]]}];
const partitions=parts.map(x=>{const a=maxContrast(x.groups,1),b=maxContrast(x.groups,2);return{
 partition:x.name,k1_upper:a.str(),k1_gap:k1.sub(a).str(),
 k2_upper:b.str(),k2_gap:k2.sub(b).str()};});
check(partitions.filter(x=>x.partition!=="all_distinct").every(x=>x.k1_gap!=="0"||x.k2_gap!=="0"),"all merged prefixes excluded");
check(new Set(ratio.map(x=>x.str())).size===3,"terminal slopes");
const result={status:"PASS_EXACT_BIGINT_RATIONAL",model:"ternary_two_law_nonIID_horizon_2",
 ordered_prefixes:13,source_scope:"GLOBAL_KNOWLEDGE_V1 main@c2658a2945f4deca; Enterprise Math science input main@72bdcc67b5a8bc5",
 first_symbol_P_Q:["1/3","1/3","1/3"],
 P_second:P.map(row=>row.map(x=>x.str())),Q_second:Q.map(row=>row.map(x=>x.str())),
 LR_terminal:ratio.map(x=>x.str()),mean_P_last:avgP.map(x=>x.str()),mean_Q_last:avgQ.map(x=>x.str()),
 full:{P_T2:t2.str(),Q_T2:t2.str(),P_T2_D1:pHit.str(),Q_T2_D1:qHit.str(),P_T1_D0:f(2,3).str(),Q_T1_D0:f(2,3).str()},
 separation:{full_Q_minus_P:fullContrast.str(),coarse_bound:coarseBound.str(),strict_gap:gap.str()},
 first_state_partition_defects:partitions,terminal_distinct_LR:3,
 observer_only_minimum_time_typed_profile:[1,3,3],observer_only_minimum_total_states:7,
 proof_scope:"Author universal exclusion and seven-state minimality proof. This executable certifies one finite positive rational model; no independent Driver, Lean, or P000 transfer."};
console.log(JSON.stringify(result,null,2));
