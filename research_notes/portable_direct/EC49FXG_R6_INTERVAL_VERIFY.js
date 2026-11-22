'use strict';
const mod=(x,n)=>(x%n+n)%n;
const F=(S,d,i,j)=>S.reduce((v,t)=>v+Number(t%5===i&&t%11!==j)+Number(mod(d-t,5)===i&&mod(d-t,11)!==j),0);
const rows=[];let checks=0;
for(let k=1;k<=55;k++){
 const n=k<=2?18:k<=4?19:20;
 const S=k<=4?Array.from({length:n},(_,t)=>3+t):Array.from({length:20},(_,t)=>t);
 let minimum=Infinity;
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
  const f=F(S,d,i,j);checks++;minimum=Math.min(f,minimum);
  if(f<6)throw Error('r6 violation '+[k,d,i,j,f]);
 }
 rows.push({k,optimal_activations:n,minimum_sampled_distance:minimum,sites:S});
}
if(checks!==84700)throw Error('wrong check count');
const report={schema:'EC49FXG_R6_INTERVAL_EXACT_V1',frozen_input:'BRC16943',model:'110-periodic two-channel one-hole CRT auxiliary observer, D_k=[0,k-1], r=6',formula:'18 for k<=2; 19 for k=3,4; 20 for k>=5',all_pass:true,checks,rows};
console.log(JSON.stringify(report,null,2));
