'use strict';
// EC49FXH — independent exact integer verifier for r=7 interval theorem.
// Frozen science BRC16943; inherits CRT observer reduction from FXF–FXG.
const mod=(x,n)=>(x%n+n)%n;
function distance(S,d,i,j){
 let v=0;
 for(const t of S){
  v+=Number(t%5===i && t%11!==j);
  v+=Number(mod(d-t,5)===i && mod(d-t,11)!==j);
 }
 return v;
}
function optimal(k){return 25-Math.min(5,Math.max(0,Math.floor((26-k)/2)))}
function construct(k){
 const s=Math.min(5,Math.max(0,Math.floor((26-k)/2)));
 const lightColors=new Set(),sites=[];
 for(let x=13-s;x<=12;x++){
  lightColors.add(x%5);
  for(let j=0;j<4;j++)sites.push(x+5*j);
 }
 for(let i=0;i<5;i++)if(!lightColors.has(i))
  for(let j=0;j<5;j++)sites.push(i+5*j);
 return sites.sort((a,b)=>a-b);
}
function choose4(a,out=[],start=0,ret=[]){
 if(out.length===4){ret.push([...out]);return ret}
 for(let p=start;p<=a.length-(4-out.length);p++)
  choose4(a,out.concat([a[p]]),p+1,ret);
 return ret;
}
function lightMax(k){
 const lists=Array.from({length:5},(_,i)=>
  choose4(Array.from({length:11},(_,j)=>i+5*j))
   .filter(T=>T.every(x=>T.every(y=>mod(x+y,55)>=k)))
 );
 let best=[];
 function go(i,points,chosen){
  if(chosen.length>best.length)best=chosen.slice();
  if(i===5 || chosen.length+5-i<=best.length)return;
  go(i+1,points,chosen);
  for(const T of lists[i])
   if(T.every(x=>points.every(y=>mod(x+y,55)>=k)))
    go(i+1,points.concat(T),chosen.concat([{color:i,sites:T}]));
 }
 go(0,[],[]);
 return {k,raw_candidate_count:5*330,filtered_counts:lists.map(x=>x.length),
         max_compatible_light_colors:best.length,example_max_family:best};
}
const thresholds=[17,19,21,23,25],expected=[4,3,2,1,0];
const lower_certificates=thresholds.map((k,z)=>{
 const ans=lightMax(k);
 if(ans.max_compatible_light_colors!==expected[z])
  throw Error('lower finite count mismatch '+JSON.stringify(ans));
 return ans;
});
let checks=0;const rows=[];
for(let k=1;k<=55;k++){
 const S=construct(k);let min=Infinity;
 if(new Set(S).size!==S.length || S.length!==optimal(k) ||
    S.some(t=>t<0||t>=110))throw Error('bad construction at k='+k);
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
  const f=distance(S,d,i,j);checks++;min=Math.min(min,f);
  if(f<7)throw Error('CRT observer condition violated '+[k,d,i,j,f]);
 }
 rows.push({k,optimal_activations:S.length,min_sampled_bit_distance:min,
            physical_sites:S});
}
if(checks!==84700)throw Error('wrong coverage '+checks);
const result={
 schema:'EC49FXH_R7_CONSECUTIVE_PHASE_EXACT_V1',
 frozen_science:'BRC16943',
 model:'110-periodic P10/one-hole CRT auxiliary two-channel observer, D_k=0..k-1',
 metric:'channel-bit Hamming distance r=7; one activation reads two separate bits',
 proof_status:'AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED',
 formula:'25-min(5,max(0,floor((26-k)/2))) for all integers 1<=k<=55',
 all_pass:true,checks,intervals:rows.length,
 lower_certificates,rows
};
console.log(JSON.stringify(result,null,2));
