"use strict";
// Stage397-B exact verifier. Node.js 18+; no external dependencies.
// Native X6 signed paths, exact integral N-BRC / Weighted-BRC recurrences.
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
const A=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6];
function endpoint(w){const z=Array(6).fill(0);for(const d of w)z[Math.abs(d)-1]+=Math.sign(d);return z}
function brc(n){
 let dp=new Map([["0,0,0,0,0,0",[1n,1n]]]), samples={};
 for(let m=1;m<=n;m++){
  let next=new Map();
  for(const [k,[c,b]] of dp){const v=k.split(",").map(Number);
   for(const d of A){const u=v.slice();u[Math.abs(d)-1]+=Math.sign(d);const ku=u.join(",");
    let e=next.get(ku);if(!e){e=[0n,0n];next.set(ku,e)}
    const weight=d===1?2n:d===-1?3n:1n;e[0]+=c;e[1]+=b*weight;
   }
  }dp=next;
  if(m===2||m===4){const at0=dp.get("0,0,0,0,0,0");samples["return"+m]=String(at0?.[0]??0n)}
 }
 samples.target=dp.get("4,0,0,0,0,0").map(String);
 assert(samples.return2==="12"&&samples.return4==="396"&&samples.target[0]==="156"&&samples.target[1]==="2976","native BRC recurrence mismatch");
 return samples;
}
const alphabet=[1,-1,2,-2], idx=new Map(alphabet.map((x,i)=>[x,i]));
const omega=new Map([[1,2],[-1,-3],[2,5],[-2,-7]]);
function observation(w){
 const J=Array(16).fill(0);let turn=0,prod=1;
 for(let i=0;i<w.length;i++){
  prod*=omega.get(w[i]);
  if(i){J[idx.get(w[i-1])*4+idx.get(w[i])]++;turn+=+(w[i-1]!==w[i])}
 }
 // z,m determine all 20 three-component X6 readouts, h and native BRC endpoint N_m/W_m.
 return JSON.stringify([w.length,endpoint(w),turn,J,prod]);
}
function kappa(w){
 const m=w.length;if(m<=2)return JSON.stringify(w);
 const last=w.slice(-2);return JSON.stringify(last[0]===-last[1]?w.slice(-3):last);
}
function runPair(w,v,limit=4){
 const open=[{w,v,c:1,dep:0}],visited=new Set();let edges=0;
 while(open.length){
  const s=open.pop(),k=JSON.stringify([s.w,s.v,s.c,s.dep]);
  if(visited.has(k))continue;visited.add(k);
  if(observation(s.w)!==observation(s.v))return {different:true,states:visited.size,edges};
  if(s.dep===limit)continue;
  for(const d of alphabet){open.push({w:[...s.w,d],v:[...s.v,d],c:s.c,dep:s.dep+1});edges++}
  if(s.c>0){
   const yes=x=>x.length>=2&&x[x.length-2]===-x[x.length-1];
   if(yes(s.w)!==yes(s.v))return {different:true,states:visited.size,edges};
   if(yes(s.w)){open.push({w:s.w.slice(0,-2),v:s.v.slice(0,-2),c:0,dep:s.dep+1});edges++}
  }
 }
 return {different:false,states:visited.size,edges};
}
function runVerification(){
 const brc_samples=brc(6),groups=new Map();
 for(let m=0;m<=5;m++){
  for(let x=0;x<4**m;x++){let y=x,w=[];
   for(let j=0;j<m;j++){w.push(alphabet[y%4]);y=Math.floor(y/4)}
   const k=observation(w);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(w)
  }
 }
 let pairs=0,edges=0,states=0,equal=0,distinct=0;
 for(const family of groups.values()){
  for(let i=0;i<family.length;i++)for(let j=i+1;j<family.length;j++){
   const pred=kappa(family[i])===kappa(family[j]);
   const test=runPair(family[i],family[j]);pairs++;edges+=test.edges;states+=test.states;
   if(pred===test.different)throw Error("finite mismatch "+JSON.stringify([family[i],family[j],pred,test]));
   if(pred)equal++;else distinct++;
  }
 }
 const fiber=[];
 for(let i=2;i<=5;i++){let w=Array(6).fill(1);w[i-1]=-1;fiber.push(w)}
 const o=observation(fiber[0]);assert(fiber.every(w=>observation(w)===o),"J fiber not equal");
 const suffix_classes=new Set(fiber.map(w=>JSON.stringify(w.slice(-3)))).size;
 const minimal_classes=new Set(fiber.map(kappa)).size;
 assert(suffix_classes===3&&minimal_classes===2,"strict quotient check");
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
  const r=runPair(fiber[i],fiber[j],5);
  assert(r.different===(kappa(fiber[i])!==kappa(fiber[j])),"fiber future mismatch");
 }
 // Within words using ±E1, the exact joint-observer fiber has precisely these four words.
 let exact_fiber=0;
 for(let x=0;x<64;x++){let w=Array.from({length:6},(_,i)=>(x&(1<<i))?-1:1);
  if(observation(w)===o)exact_fiber++;
 }
 assert(exact_fiber===4,"joint observer fiber cardinality mismatch");
 return {status:"STAGE397B_JOINT_EXACT_QUOTIENT_PASS",brc_samples,
  alphabet:"12 native signed directions; finite crosscheck uses ±E1,±E2",
  short_words_through:5,fiber_path_length:6,initial_observer_groups:groups.size,
  pairs_tested:pairs,future_transitions_tested:edges,future_pair_states_visited:states,
  equivalent_pairs:equal,distinguishable_pairs:distinct,
  strict_fiber:{number_of_histories:exact_fiber,uniform_suffix_classes:suffix_classes,
   minimal_future_classes:minimal_classes,bits_uniform:2,bits_minimal:1}};
}
console.log(JSON.stringify(runVerification(),null,2));
