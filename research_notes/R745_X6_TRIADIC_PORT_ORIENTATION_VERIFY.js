"use strict";
// R745: deterministic exact finite checker; Node.js standard runtime, no dependencies.
function verifyR745(){
 const assert=(x,msg)=>{if(!x)throw Error(msg)};
 const permute=(a)=>{if(a.length===0)return [[]];let o=[];for(let i=0;i<a.length;i++)for(const rest of permute([...a.slice(0,i),...a.slice(i+1)]))o.push([a[i],...rest]);return o};
 const choose3=(n)=>{let r=[];for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)for(let c=b+1;c<n;c++)r.push([a,b,c]);return r};
 const parity=(x)=>{let s=1;for(let i=0;i<x.length;i++)for(let j=i+1;j<x.length;j++)if(x[i]>x[j])s=-s;return s};
 const key=(a,o)=>JSON.stringify([a,o]);
 const action=(pi,conf,epsilon)=>{let x=conf.map(([i,s])=>[pi[i],s]).sort((a,b)=>a[0]-b[0]);let old=conf.map(t=>t[0]);let newSorted=old.map(i=>pi[i]).sort((a,b)=>a-b);let imageRanks=old.map(i=>newSorted.indexOf(pi[i]));return [x,epsilon*parity(imageRanks)]};
 const ps=permute([0,1,2,3,4,5]), configs=[];
 for(const a of choose3(6))for(let mask=0;mask<8;mask++)configs.push(a.map((i,k)=>[i,(mask>>k)&1?1:-1]));
 assert(configs.length===160,"signed state count");
 const stateSet=new Set(configs.flatMap(c=>[-1,1].map(o=>key(c,o))));
 assert(stateSet.size===320,"oriented state count");
 let covariance=0,stab=0;
 for(const c of configs){
   const eq=[];for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(c[i][1]===c[j][1])eq.push([c[i][0],c[j][0]]);
   assert(eq.length>0,"pigeonhole");
   const swap=[0,1,2,3,4,5];const [i,j]=eq[0];[swap[i],swap[j]]=[swap[j],swap[i]];
   assert(key(...action(swap,c,1))===key(c,-1),"stabilizer transposition must reverse cycle");stab++;
   for(const o of [-1,1])for(const pi of ps){
     const [c1,o1]=action(pi,c,o);
     assert(stateSet.has(key(c1,o1)),"rotation covariance");covariance++;
   }
 }
 const orbit_sizes={};
 for(let k=0;k<4;k++){
   const sample=configs.find(c=>c.filter(z=>z[1]===1).length===k);
   const orb=new Set(ps.map(pi=>{let [c,o]=action(pi,sample,1);return key(c,o)}));
   const want=40*(k===1||k===2?3:1);
   assert(orb.size===want,"orbit cardinality k="+k);orbit_sizes[k]=want;
 }
 const loop=[[4,1],[5,1],[4,-1],[5,-1]];
 const current=(word)=>{
   const x=[0,0,0,0,0,0],j=new Map();
   for(const [i,s] of word){
     const base=x.slice();if(s===-1)base[i]-=1;
     const edge=JSON.stringify([base,i]);j.set(edge,(j.get(edge)||0)+s);x[i]+=s;
   }
   assert(x.every(v=>v===0),"loop does not close");
   return JSON.stringify([...j].filter(x=>x[1]!==0).sort((a,b)=>a[0].localeCompare(b[0])));
 };
 let currents=new Set(), signs={"1":0,"-1":0},routes=0, nonback=0;
 for(const sigma of permute([0,1,2,3])){
   const w=[...sigma.map(i=>[i,1]),...loop,...sigma.slice().reverse().map(i=>[i,-1])];
   assert(w.length===12,"path length");
   if(w.every((z,k)=>!k||z[0]!==w[k-1][0]||z[1]!==-w[k-1][1]))nonback++;
   currents.add(current(w));
   const order=sigma.filter(i=>i<3);signs[String(parity(order))]++;routes++;
 }
 assert(routes===24&&nonback===24&&currents.size===1&&signs["1"]===12&&signs["-1"]===12,"connector path bridge");
 return {schema:"EM_R745_EXACT_ENUM_V1",status:"PASS",N_axis:6,signed_triad_configs:configs.length,oriented_triad_states:stateSet.size,S6_permutations:ps.length,covariance_cases:covariance,stabilizer_no_section_witnesses:stab,oriented_orbits_by_positive_count:orbit_sizes,connector_paths:routes,connector_length:12,connector_non_backtracking:nonback,distinct_edge_currents:currents.size,orientations_from_24_connector_paths:signs,arithmetic:"exact integers and finite permutations",proof_status:"finite complete enumeration + independent stabilizer theorem",native_v39_executed:false};
}
console.log(JSON.stringify(verifyR745(), null, 2));
