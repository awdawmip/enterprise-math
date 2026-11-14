/* R762AP complete exact verifier. Usage: node R762AP_BASELINE_FREE_VERIFY.js */
const verify = function verify(){
 const assert=(b,msg)=>{if(!b)throw new Error(msg)};
 const E="012", C="120", T="102", U="!";
 const mul=(p,q)=>[...q].map(i=>p[+i]).join("");
 let frames=[E];for(let i=0;i<frames.length;i++)for(const g of [C,T]){
  let p=mul(g,frames[i]); if(!frames.includes(p))frames.push(p);
 }assert(frames.length===6,"S3");
 const live=[[0,E],[1,E],[2,E],...frames.filter(h=>h!==E).map(h=>[0,h])].sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b)));
 const states=[...live,U];assert(states.length===9,"states");
 const idx=new Map(states.map((s,i)=>[JSON.stringify(s),i]));
 const cycle=mul(C,C);
 const obs=s=>s===U?"U":(s[0]===0?"E":"C")+(s[1]===E?"E":(s[1]===C||s[1]===cycle?"C":"T"));
 const step=(s,a)=>{
   if(s===U)return U;
   let [n,h]=s;
   if(a==="S"&&h===E)return [(n+1)%3,h];
   if(a==="C"&&n===0)return [0,mul(C,h)];
   if(a==="T"&&n===0)return [0,mul(T,h)];
   return U
 };
 const os=states.map(obs);const I=states.map((_,i)=>i);
 const act=(f,a)=>f.map(i=>idx.get(JSON.stringify(step(states[i],a))));
 const maps=new Map([[I.join(","),{f:I,w:""}]]), queue=[I.join(",")];
 for(let z=0;z<queue.length;z++){
  const {f,w}=maps.get(queue[z]);
  for(const a of "SCT"){
   let g=act(f,a),key=g.join(",");
   if(!maps.has(key)){maps.set(key,{f:g,w:w+a});queue.push(key);}
  }
 }assert(maps.size===75,"monoid size");
 const V=new Map();
 for(const {f,w} of maps.values()){
  let v=f.map(i=>os[i]).join("|");
  if(!V.has(v)||w.length<V.get(v).length)V.set(v,w)
 }assert(V.size===43,"observer vectors");
 const pairs=[];const baselinePairs=[];
 for(let i=0;i<9;i++)for(let j=i+1;j<9;j++){pairs.push([i,j]);if(os[i]===os[j])baselinePairs.push([i,j]);}
 assert(pairs.length===36 && baselinePairs.length===5,"pairs");
 const bitmask=(v,ps)=>ps.reduce((mask,[i,j],k)=>mask+(v[i]===v[j]?0:2**k),0);
 const nonemptyMasks=new Map();
 for(let [v,w] of V){if(!w)continue;let m=bitmask(v.split("|"),baselinePairs);
  if(!nonemptyMasks.has(m)||w.length<nonemptyMasks.get(m).length)nonemptyMasks.set(m,w);
 }
 const M=Object.fromEntries(["S","C","T","CT","TC"].map(w=>{
  let f=I;for(const a of w)f=act(f,a);
  return [w,{mask:bitmask(f.map(i=>os[i]),baselinePairs),outputs:f.map(i=>os[i])}];
 }));
 const nonzero=[...nonemptyMasks.keys()].filter(x=>x>0);
 assert(nonzero.length===5,"five masks");
 assert(new Set(Object.values(M).map(x=>x.mask)).size===5,"five distinct representative masks");
 for(let w of Object.keys(M))assert(nonemptyMasks.get(M[w].mask).length===w.length,"minimum length "+w);
 const group=new Map();for(let i=0;i<states.length;i++){
  let k=M.S.outputs[i]+"/"+M.C.outputs[i];
  group.set(k,[...(group.get(k)||[]),i]);
 }
 assert(group.size===7,"S,C joint groups");
 const ambiguous=[...group.values()].filter(x=>x.length>1);
 assert(ambiguous.length===1 && ambiguous[0].length===3&&ambiguous[0].every(i=>os[i]==="ET"),"S,C resolve except ET");
 const first_action_collapses={};
 for(let a of "SCT"){
   let f=act(I,a),witness=null;
   for(let i=0;i<8&&!witness;i++)for(let j=i+1;j<8;j++)
     if(f[i]===f[j]&&f[i]===8){witness=[i,j];break;}
   assert(witness!==null,"first step irreversibility "+a);
   first_action_collapses[a]={pair:witness,common_successor:f[witness[0]],baseline_output_pair:witness.map(i=>os[i])};
 }
 const cases=[];
 for(let d=1;d<=20;d++){
  const k=Math.floor(d/2);
  const count=d%2?{S:d,C:d,T:k+1,CT:k+1,TC:k}:{S:d,C:d,T:k,CT:k,TC:k};
  const wordCount=Object.values(count).reduce((a,b)=>a+b,0);
  const letters=Object.entries(count).reduce((a,[w,n])=>a+w.length*n,0);
  assert(wordCount===Math.ceil(7*d/2),"count N "+d);
  assert(letters===Math.ceil(9*d/2),"count L "+d);
  let dist = pairs.map(([i,j])=>Object.entries(count).reduce((tot,[w,n])=>tot+n*(M[w].outputs[i]!==M[w].outputs[j]),0));
  let minDist=Math.min(...dist);
  assert(minDist>=d,"distance "+d);
  cases.push({d,counts:count,probes:wordCount,letters,minimum_pair_distance:minDist,maximum_pair_distance:Math.max(...dist)});
 }
 return {schema:"R762AP_BASELINE_FREE_ROBUST_BRC_V1",scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",source_model:"R762AO AK4 conditional partial source/frame observer",finite_completeness:{states:9,live_states:8,transformations:maps.size,terminal_vectors:V.size,nonempty_output_vectors:V.size-1,total_unordered_pairs:pairs.length,equal_baseline_pairs:baselinePairs.length,distinct_nonzero_equal_baseline_masks:nonzero.length},states:states.map((s,i)=>({index:i,state:s===U?"U":`${s[0]}:${s[1]}`,old_observation:os[i],S:M.S.outputs[i],C:M.C.outputs[i],T:M.T.outputs[i],CT:M.CT.outputs[i],TC:M.TC.outputs[i]})),joint_S_C_classes:[...group].map(([outputs,indices])=>({outputs,indices})),within_fiber_pairs:baselinePairs,shortest_witnesses:Object.fromEntries(Object.entries(M).map(([w,x])=>[w,{length:w.length,mask:x.mask.toString(2).padStart(5,"0")}])),first_action_absorbing_collisions:first_action_collapses,d_checks:cases,theorem:"No free baseline read is necessary for independent-reset fixed probes. d=e+2t+1; Nmin=ceil(7d/2); Lmin=ceil(9d/2). In one unreset trajectory with no initial read, every first letter merges distinct initial states, making zero-error recovery impossible.",status:"AUTHOR_CONDITIONAL_PROOF_EXACT_ENUMERATION_NOT_NATIVE_ADMITTED"}
};
console.log(JSON.stringify(verify(), null, 2));
