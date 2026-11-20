// X6 R64 exact integer verifier. No dependencies; run: node x6_r64_shared_bias_minimax_verify.js
// The lattice enumeration is complete for each (D,p) listed; p>=D.
// Every high-degree delta with positive/negative support <= p is feasible.

const verify = function verify(){
 const maxP={2:8,3:8,4:11,5:8};
 const results=[], crosschecks=[];
 function calc(D,p){
  let checked=0,best=Number.POSITIVE_INFINITY,witness=null;
  const h=Array(D-1).fill(0);
  function rec(i,pos,neg){
   if(pos>p||neg>p)return;
   if(i===h.length){
    if(h.every(x=>x===0))return;
    checked++;
    let d=[0];
    for(let t=2;t<=D;t++){
      let val=0;
      for(let j=0;j<h.length;j++){const degree=j+2;val+=h[j]*(degree**t-degree)}
      d.push(val);
    }
    const gap=Math.max(...d)-Math.min(...d);
    if(gap<best){best=gap;witness={high_delta:h.slice(),difference_from_t1:d.slice(),positive_high:pos,negative_high:neg,minimum_ports:Math.max(pos,neg)}}
    return;
   }
   for(let v=-p;v<=p;v++){h[i]=v;rec(i+1,pos+Math.max(v,0),neg+Math.max(-v,0))}
  }
  rec(0,0,0);
  return {D,p,min_oscillation:best,critical_eta_num:best,critical_eta_denom:4,feasible_high_differences:checked,witness};
 }
 function checkDirect(D,p,expected){
   let groups=new Map(), hist=Array(D+1).fill(0);
   function rec(i,remain){
    if(i===D){hist[i]=remain;let m=[];for(let t=1;t<=D;t++){let v=0;for(let d=0;d<=D;d++)v+=hist[d]*d**t;m.push(v)}let key=m.slice(1).map((v,j)=>v-m[0]).join(",");const a=groups.get(key)||[];a.push({hist:hist.slice(),moments:m});groups.set(key,a);return}
    for(let v=0;v<=remain;v++){hist[i]=v;rec(i+1,remain-v)}
   }
   rec(0,p);
   let candidates=[];for(const arr of groups.values())candidates.push(...arr);
   let min=Infinity;
   for(let i=0;i<candidates.length;i++)for(let j=i+1;j<candidates.length;j++){
    const a=candidates[i],b=candidates[j];
    if(a.hist.slice(2).every((v,k)=>v===b.hist[k+2]))continue;
    const delta=a.moments.map((x,k)=>x-b.moments[k]);
    const gap=Math.max(...delta)-Math.min(...delta);if(gap<min)min=gap;
   }
   if(min!==expected)throw new Error("brute pair mismatch D="+D+" p="+p+" "+min+" vs "+expected);
   return {D,p,histograms:candidates.length,min_oscillation:min};
 }
 for(let D=2;D<=5;D++)for(let p=D;p<=maxP[D];p++){
  const r=calc(D,p);results.push(r);
  if(D<=4&&p<=4){crosschecks.push(checkDirect(D,p,r.min_oscillation))}
 }
 const expected={"2:2":2,"3:3":6,"3:4":2,"4:4":14,"4:5":12,"4:10":12,"4:11":2};
 for(const [key,v] of Object.entries(expected)){
  const got=results.find(r=>`${r.D}:${r.p}`===key);if(got.min_oscillation!==v)throw Error("expected mismatch "+key)
 }
 return {status:"PASS",arithmetic:"exact safe integers (JS Number; bounded inputs; no floats in integer operations)",model:"normalized positive BRC star moments, shared unknown additive offset; max absolute channel noise",formula:"critical_eta = minimum over pairs of histogram models with distinct high counts of (max_t delta_m[t]-min_t delta_m[t])/4",ranges:maxP,results,crosschecks};
};

console.log(JSON.stringify(verify(), null, 2));
