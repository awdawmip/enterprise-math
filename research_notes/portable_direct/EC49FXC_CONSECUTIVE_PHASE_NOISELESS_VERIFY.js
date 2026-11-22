"use strict";
// EC49FXC: all 55 noiseless D_k auxiliary CRT layouts, exact integer crosscheck.
function sites(k){
  const start=Math.max(23,Math.ceil(k/2));
  const S=[];for(let t=start;t<=27;t++)S.push(t);
  const occupied=new Set(S.map(t=>t%5));
  for(let i=0;i<5;i++)if(!occupied.has(i))S.push(i,i+5);
  return S.sort((a,b)=>a-b);
}
function count(S,d,i,j){
  let n=0;
  for(const t of S){
    if(t%5===i&&t%11!==j)n++;
    if(((d-t)%5+5)%5===i&&((d-t)%11+11)%11!==j)n++;
  }
  return n;
}
const rows=[];let checks=0;
for(let k=1;k<=55;k++){
  const S=sites(k), optimum=Math.max(5,10-Math.ceil((55-k)/2));
  if(S.length!==optimum||new Set(S).size!==S.length)throw Error('size k='+k);
  let minimum=Infinity;
  for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
    const n=count(S,d,i,j);checks++;minimum=Math.min(minimum,n);
    if(n<1)throw Error('fails k='+k+', d='+d+', i='+i+', j='+j);
  }
  rows.push({k,optimal_activations:optimum,sites:S,min_sampled_distance:minimum});
}
if(checks!==84700)throw Error('incorrect check count '+checks);
console.log(JSON.stringify({schema:'EC49FXC_EXACT_INTEGER_VERIFY_V1',frozen_input:'BRC16943',model:'110-CRT two-channel r=1, D_k=[0,k-1]',all_pass:true,checks,rows},null,2));
