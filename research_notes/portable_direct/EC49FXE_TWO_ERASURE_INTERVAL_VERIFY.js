'use strict';
// Self-contained exact integer CRT verification for EC49FXE.
const result=(function check(){
 const a=[56,58,63,65,75,81,89,92,94,97,98,104,105];
 const b=[64,65,66,71,73,76,79,82,90,98,103,104,105,107];
 const c=Array.from({length:15},(_,i)=>i);
 const mod=(x,n)=>(x%n+n)%n;
 const val=(S,d,i,j)=>S.reduce((z,t)=>z+(t%5===i&&t%11!==j?1:0)+(mod(d-t,5)===i&&mod(d-t,11)!==j?1:0),0);
 const rows=[];let checks=0;
 for(let k=1;k<=55;k++){
   const sites=k<=2?a:k<=4?b:c,expected=k<=2?13:k<=4?14:15;
   if(sites.length!==expected||new Set(sites).size!==expected)throw Error("bad layout at "+k);
   let minimum=Infinity;
   for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
     const f=val(sites,d,i,j);checks++;minimum=Math.min(f,minimum);
     if(f<4)throw Error("distance violation "+[k,d,i,j,f]);
   }
   rows.push({k,optimal_activations:expected,minimum_sampled_distance:minimum,sites});
 }
 if(checks!==84700)throw Error("wrong check count "+checks);
 const minMatrix=(S,k)=>Array.from({length:k},(_,d)=>Array.from({length:5},(_,i)=>Math.min(...Array.from({length:11},(_,j)=>val(S,d,i,j)))));
 const m13=minMatrix(a,2),m14=minMatrix(b,4);
 if(JSON.stringify(m13)!==JSON.stringify([[5,4,4,4,4],[4,4,4,5,4]])||JSON.stringify(m14)!==JSON.stringify([[5,5,4,4,5],[4,4,4,5,4],[4,5,4,4,4],[4,4,4,4,4]]))throw Error("witness minima differ");
 return {schema:"EC49FXE_R4_INTERVAL_EXACT_V1",frozen_input:"BRC16943",model:"110-CRT two-channel, consecutive D_k, sampled Hamming r=4",all_pass:true,exact_distance_checks:checks,minimum_S13_for_k2:m13,minimum_S14_for_k4:m14,rows};
})();
console.log(JSON.stringify(result,null,2));
