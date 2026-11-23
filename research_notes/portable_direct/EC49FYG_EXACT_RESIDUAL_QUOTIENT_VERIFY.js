'use strict';
// EC49FYG. Frozen P10/C11 support atlas BRC16943.
// Standard Node.js: node EC49FYG_EXACT_RESIDUAL_QUOTIENT_VERIFY.js
// Exact BigInt arithmetic. Full 600-state oracle is independent of residual updates.
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,
327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,
613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
if(F.length!==50||new Set(F).size!==50)throw Error('frozen atlas mismatch');
const U50=(1n<<50n)-1n, S600=(1n<<600n)-1n;
const rows=Array.from({length:10},(_,t)=>F.reduce(
 (a,u,i)=>((u>>t)&1)?a|(1n<<BigInt(i)):a,0n));
const oracleYes=Array.from({length:10},(_,t)=>Array.from({length:11},(_,j)=>
 F.reduce((a,u,i)=>{
  if(!((u>>t)&1))return a;
  for(let z=-1;z<11;z++)if(z!==j)a|=1n<<BigInt(i*12+z+1);
  return a;
 },0n)));
function expand(o){
 let v=0n;
 for(let i=0;i<50;i++){
  const ubit=1n<<BigInt(i),offset=12*i;
  if(o.A&ubit){
   v|=1n<<BigInt(offset);
   for(let j=o.k;j<11;j++)v|=1n<<BigInt(offset+j+1);
  }
  for(let j=0;j<o.k;j++)if(o.B[j]&ubit)v|=1n<<BigInt(offset+j+1);
 }
 return v;
}
function update(o,t,j,b){
 if(j>o.k||j>=11)throw Error('noncanonical query');
 const old=j<o.k, good=b?rows[t]:(U50^rows[t]);
 const B=o.B.map((x,h)=>old&&h===j?(b?0n:x):(x&good));
 if(!old)B.push(b?0n:o.A);
 return {k:o.k+(old?0:1),A:o.A&good,B};
}
function key(o){return o.k+':'+o.A.toString(16)+':'+o.B.map(x=>x.toString(16)).join(',')}
function pop(v){let n=0;for(;v;v&=v-1n)n++;return n}
let level=[{k:0,A:U50,B:[],oracle:S600}],summary=[],edges=0,checks=0;
for(let depth=0;depth<=3;depth++){
 const bySeenColumns={},size=[];
 for(const o of level){
  if(expand(o)!==o.oracle)throw Error('state mismatch at depth '+depth);
  checks++;bySeenColumns[o.k]=(bySeenColumns[o.k]||0)+1;
  size.push(pop(o.oracle));
 }
 summary.push({depth,nodes:level.length,bySeenColumns,
  minCandidates:Math.min(...size),maxCandidates:Math.max(...size)});
 if(depth===3)break;
 const next=new Map();
 for(const o of level)for(let t=0;t<10;t++)
 for(let j=0;j<=Math.min(o.k,10);j++)for(let bit=0;bit<=1;bit++){
  const c=update(o,t,j,bit);
  c.oracle=o.oracle&(bit?oracleYes[t][j]:(S600^oracleYes[t][j]));
  if(c.oracle===0n)continue;
  if(expand(c)!==c.oracle)throw Error('transition mismatch '+[depth,t,j,bit]);
  edges++;next.set(key(c),c);
 }
 level=[...next.values()];
}
if(summary.map(x=>x.nodes).join(',')!=='1,20,555,11639')throw Error('layer census mismatch');
if(edges!==28614||checks!==12215)throw Error('verification count mismatch');
console.log(JSON.stringify({
 schema:'EC49FYG_EXACT_RESIDUAL_FIBRE_QUOTIENT_V1',
 science_pin:'BRC16943',status:'ALL_PASS',original_states:600,
 original_physical_sites:110,support_masks:50,
 states_checked_through_depth:3,quotient_layers:summary,
 nonempty_transitions_checked:edges,reconstructions_checked:checks,
 arithmetic:'BigInt exact',independent_oracle:'600-bit state subset',
 claim:'Exact candidate-state quotient and Bellman recursion; Q=14 versus Q=15 remains unresolved'
},null,2));
