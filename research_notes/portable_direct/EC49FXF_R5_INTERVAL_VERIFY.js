'use strict';
// Frozen BRC16943, auxiliary 110-CRT two-channel model; exact integer verification.
const mod=(a,n)=>(a%n+n)%n;
const F=(S,d,i,j)=>S.reduce((v,t)=>v+Number(t%5===i&&t%11!==j)+Number(mod(d-t,5)===i&&mod(d-t,11)!==j),0);
const maxLight=(k)=>{
  const byColor=Array.from({length:5},()=>[]);
  for(let i=0;i<5;i++){
    const R=Array.from({length:11},(_,q)=>i+5*q);
    for(let a=0;a<9;a++)for(let b=a+1;b<10;b++)for(let c=b+1;c<11;c++){
      const T=[R[a],R[b],R[c]];
      if(T.every(x=>T.every(y=>mod(x+y,55)>=k)))byColor[i].push(T);
    }
  }
  let best=0,bestColors=[],bestTriples=[];
  const dfs=(color,chosen,colors)=>{
    if(color===5){if(chosen.length>best){best=chosen.length;bestColors=colors.slice();bestTriples=chosen.map(x=>x.slice());}return;}
    dfs(color+1,chosen,colors);
    for(const T of byColor[color]){
      if(chosen.every(Q=>T.every(x=>Q.every(y=>mod(x+y,55)>=k)))){
        dfs(color+1,chosen.concat([T]),colors.concat([color]));
      }
    }
  };
  dfs(0,[],[]);
  return {k,triples_per_color:byColor.map(x=>x.length),triples:byColor,best_light_colors:best,best_colors:bestColors,best_triples:bestTriples};
};
const thresholdRows=[27,29,31,33,35].map(maxLight);
const expected=[4,3,2,1,0];
thresholdRows.forEach((v,i)=>{if(v.best_light_colors!==expected[i])throw Error('light upper bound at '+v.k)});
const rows=[];let checks=0;
for(let k=1;k<=55;k++){
 const s=Math.min(5,Math.max(0,Math.floor((36-k)/2)));
 const lights=Array.from({length:s},(_,a)=>18-s+a);
 const lightColors=new Set(lights.map(x=>x%5));
 const S=lights.flatMap(x=>[x,x+5,x+10]);
 for(let i=0;i<5;i++)if(!lightColors.has(i))S.push(i,i+5,i+10,i+15);
 S.sort((a,b)=>a-b);
 if(S.length!==20-s||new Set(S).size!==S.length)throw Error('layout count at '+k);
 let minimum=Infinity;
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
   const val=F(S,d,i,j);checks++;minimum=Math.min(minimum,val);
   if(val<5)throw Error('distance at '+[k,d,i,j,val]);
 }
 rows.push({k,optimal_activations:20-s,light_colors:s,minimum_sampled_distance:minimum,sites:S});
}
if(checks!==84700)throw Error('coverage '+checks);
const report={schema:'EC49FXF_R5_INTERVAL_EXACT_V1',frozen_input:'BRC16943',model:'110-periodic two-channel one-hole CRT auxiliary observer, D_k=[0,k-1], r=5',theorem:'N=20-min(5,max(0,floor((36-k)/2))) for k=1..55',all_pass:true,checks,enumerated_candidate_triples_per_threshold:825,thresholdRows,rows};
console.log(JSON.stringify(report,null,2));
