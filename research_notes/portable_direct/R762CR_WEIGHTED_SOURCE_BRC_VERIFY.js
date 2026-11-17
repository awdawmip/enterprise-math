"use strict";
// Reproducible with node R762CR_WEIGHTED_SOURCE_BRC_VERIFY.js > R762CR_WEIGHTED_SOURCE_BRC_EVIDENCE.json
// Finite positive N-BRC: matched swap of class j has w_j separate unit microbranches.
const verify = () => {
  const E=["01","02","03","12","13","23"], ALL=63;
  const subsets=[]; for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)subsets.push((1<<a)|(1<<b)|(1<<c));
  const S=[...new Set(subsets.map(m=>Math.min(m,m^ALL)))].sort((a,b)=>a-b),idx=new Map(S.map((m,i)=>[m,i]));
  const fs=new Set([0,1,2,3].map(v=>{let m=0;for(let i=0;i<6;i++)if(E[i].includes(String(v)))m|=1<<i;return Math.min(m,m^ALL)}));
  const F=S.map(m=>fs.has(m)?1:0),P=F.map(x=>1-x);
  function parts(){let out=[];function rec(a,k){if(a.length===6){out.push(a);return}for(let j=0;j<=k+1;j++)rec([...a,j],Math.max(k,j))}rec([0],0);return out}
  function adj(part){return S.map(m=>{let row=[];for(let x=0;x<6;x++)if(m&(1<<x))for(let y=0;y<6;y++)if(!(m&(1<<y))&&part[x]===part[y]){let b=(m^(1<<x)^(1<<y));row.push([idx.get(Math.min(b,b^ALL)),part[x],x,y])}return row})}
  const step=(rows,w,v)=>rows.map(row=>row.reduce((t,[target,j])=>t+w[j]*v[target],0));
  const histDepth={},histClasses={},histRepairBits={},histExtra={},regress={},per=[];
  let failed=0,total=0,failedPartitions=0,witness=null;
  for(const p of parts()){
    let k=Math.max(...p)+1, rows=adj(p), localFailed=0,localMax=0;
    function walkWeights(prefix){
      if(prefix.length<k){for(let a=1;a<=3;a++)walkWeights([...prefix,a]);return}
      const w=prefix; let f=F,pv=P,signatures=Array.from({length:10},(_,i)=>[f[i],pv[i]]), history=[];
      history.push(signatures.map(z=>z.join(",")));
      for(let t=1;t<=8;t++){f=step(rows,w,f);pv=step(rows,w,pv);signatures=signatures.map((z,i)=>[...z,f[i],pv[i]]);history.push(signatures.map(z=>z.join(",")))}
      const counts=history.map(x=>new Set(x).size);
      if(counts.some((x,i)=>i&&x<counts[i-1]))throw Error("non-refining signature");
      let depth=counts.indexOf(counts[8]), cls=counts[8];
      if(depth>8)throw Error("depth bound failed");
      histDepth[depth]=(histDepth[depth]||0)+1;histClasses[cls]=(histClasses[cls]||0)+1;
      const fibers=new Map(); for(let i=0;i<10;i++){const a=history[1][i],b=history[8][i];if(!fibers.has(a))fibers.set(a,new Set());fibers.get(a).add(b)}
      const extra=Math.max(...[...fibers.values()].map(s=>s.size)); histExtra[extra]=(histExtra[extra]||0)+1;
      let fClasses=new Set(),pClasses=new Set();for(let i=0;i<10;i++)(F[i]?fClasses:pClasses).add(history[8][i]);
      const bits=Math.ceil(Math.log2(Math.max(fClasses.size,pClasses.size)));
      histRepairBits[bits]=(histRepairBits[bits]||0)+1;
      if(w.every(x=>x===1)){regress[cls]=(regress[cls]||0)+1;if(depth>1)throw Error("unit regression");}
      if(depth>1){failed++;localFailed++;if(extra!==2||depth!==2)throw Error("unexpected failure shape");}
      localMax=Math.max(localMax,cls);total++;
      for(let i=0;i<10;i++){
        let occ=Array(k).fill(0), sizes=Array(k).fill(0);
        for(let j=0;j<6;j++){sizes[p[j]]++;if(S[i]&(1<<j))occ[p[j]]++}
        let d=occ.reduce((z,x,j)=>z+w[j]*x*(sizes[j]-x),0), actual=rows[i].reduce((z,e)=>z+w[e[1]],0);
        if(d!==actual)throw Error("degree conservation");
      }
      if(p.join("")==="001112"&&w.join("")==="2,1,1"){
        const sig1=history[1],sig2=history[2];if(sig1[2]!==sig1[6]||sig2[2]===sig2[6])throw Error("witness");
        witness={partition:"001112",source_classes:["01,02","03,12,13","23"],weights:w,s: {triple:["01","03","12"],O1:sig1[2],O2:sig2[2]},u:{triple:["02","03","13"],O1:sig1[6],O2:sig2[6]}};
      }
    }
    walkWeights([]);
    if(localFailed)failedPartitions++;
    per.push({partition:p.join(""),source_classes:k,weight_combinations:3**k,one_step_failures:localFailed,max_future_classes:localMax});
  }
  const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  if(total!==12351||failed!==72||failedPartitions!==24)throw Error("enumeration count");
  if(!eq(histDepth,{"0":735,"1":11544,"2":72}))throw Error("depth dist "+JSON.stringify(histDepth));
  if(!eq(histClasses,{"2":735,"3":1674,"4":1758,"5":4752,"6":648,"7":1440,"10":1344}))throw Error("class dist "+JSON.stringify(histClasses));
  if(!eq(histExtra,{"1":12279,"2":72}))throw Error("repair dist");
  if(!eq(histRepairBits,{"0":735,"1":1950,"2":7674,"3":1992}))throw Error("bit dist");
  if(!eq(regress,{"2":3,"3":30,"4":62,"5":36,"6":24,"7":48}))throw Error("unit regression");
  return {schema:"EM_R762CR_WEIGHTED_K4_BRC_EXACT_EVIDENCE_V1",status:"AUTHOR_FINITE_VERIFIED_NOT_INDEPENDENTLY_REVIEWED",
    frozen_task_commit:"e3f42efac29a2da2d95be391f3231a664e2fade0",frozen_p000_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    state_masks:S, F_masks:[...fs].sort((a,b)=>a-b),labels:E,
    scope:"source-equality-matched candidate swaps with positive unit N-BRC microbranch multiplicity; F/P future terminal counts; no native signed event admission",
    checked:{partitions:203,weighted_assignments:total,weight_alphabet:[1,2,3],insufficient_one_step:failed,affected_partitions:failedPartitions,
      shortest_full_future_depth:histDepth,full_future_classes:histClasses,
      one_step_fiber_to_future_max_subclasses:histExtra,optimal_extra_bits_after_current_F_P:histRepairBits,unit_weight_regression:regress},
    witness,per_partition:per,
    proof_status:"infinite a=2b witness and universal 8-step linear-span bound proved; finite domain exhaustively enumerated"};
};
console.log(JSON.stringify(verify(),null,2));
