'use strict';
// EC49FXI r=8 exact verifier; frozen BRC16943.
const mod=(x,n)=>(x%n+n)%n;
const F=(S,d,i,j)=>S.reduce((v,t)=>v+Number(t%5===i&&t%11!==j)+Number(mod(d-t,5)===i&&mod(d-t,11)!==j),0);
const optimal=k=>k<=2?23:k<=4?24:25;
const construct=k=>Array.from({length:optimal(k)},(_,t)=>t+(k<=4?3:0));
let checks=0;const rows=[];
for(let k=1;k<=55;k++){
 const S=construct(k);let min=Infinity;
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
  const v=F(S,d,i,j);checks++;min=Math.min(min,v);
  if(v<8)throw Error('r8 violation '+[k,d,i,j,v]);
 }
 rows.push({k,optimal_activations:S.length,minimum_sampled_bit_distance:min,physical_sites:S});
}
const small_case_tables={};
for(const [key,S,limit] of [[2,construct(2),2],[4,construct(4),4]])
 small_case_tables['k='+key]=Array.from({length:limit},(_,d)=>Array.from({length:5},(_,i)=>Math.min(...Array.from({length:11},(_,j)=>F(S,d,i,j)))));
if(checks!==84700||rows.length!==55||rows[0].optimal_activations!==23||rows[2].optimal_activations!==24||rows[4].optimal_activations!==25)
 throw Error('coverage or formula mismatch');
console.log(JSON.stringify({
 schema:'EC49FXI_R8_CONSECUTIVE_PHASE_EXACT_V1',
 frozen_science:'BRC16943',
 model:'110-periodic P10/one-hole CRT auxiliary two-channel observer; D_k=[0,k-1]',
 metric:'separately counted channel-bit Hamming distance >=8',
 status:'AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED',
 formula:'23 for k=1,2; 24 for k=3,4; 25 for k=5..55',
 all_pass:true,checks,intervals:55,small_case_tables,rows
},null,2));
