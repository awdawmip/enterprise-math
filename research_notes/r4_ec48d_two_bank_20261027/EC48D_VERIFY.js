"use strict";
// EC48D exact finite checks. Node: node EC48D_VERIFY.js
// Positive integer arrays are bounded here so all cross-products are exact safe JS integers.
function assertion(x,msg){if(!x)throw Error(msg);}
function makeRng(seed){let s=seed>>>0;return function(n){s=(Math.imul(s,1664525)+1013904223)>>>0;return s%n;};}
function profileData(P,Q,H,Y){
  const N=H*Y, reps=[];
  for(let i=0;i<N;i++)if(!reps.some(j=>P[i]*Q[j]===P[j]*Q[i]))reps.push(i);
  let Kh=0,M=0,interpolations=0,forceMax=0;
  const hist={};
  for(const i of reps){
    const d=P.map((p,j)=>p*Q[i]-P[i]*Q[j]);
    const left=[],right=[];
    for(let h=0;h<H;h++){
      let l="",r="";
      for(let y=0;y<Y;y++){
        const v=d[h*Y+y];
        l+=v>=0?"1":"0";r+=v>0?"1":"0";
      }
      left.push(l);right.push(r);
    }
    const lset=new Set(left),rset=new Set(right),bank=[...new Set([...left,...right])];
    const lo=Math.max(lset.size,rset.size);
    Kh=Math.max(Kh,lo); M=Math.max(M,bank.length);
    hist[bank.length]=(hist[bank.length]||0)+1;
    const maxScore=d.reduce((a,x)=>a+Math.max(0,x),0);
    const qT=d.reduce((a,x,j)=>a+(x===0?Q[j]:0),0);
    for(const t of [0,1,2,3,5,7]){
      let val=0,tie=0,pnum=0,qnum=0;
      for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
        const j=h*Y+y;
        const wa=t*Number(left[h][y])+(7-t)*Number(right[h][y]);
        assertion(wa===(d[j]>0?7:d[j]<0?0:t),"interpolation mismatch");
        val+=d[j]*wa; if(d[j]===0)tie+=Q[j]*wa;
        pnum+=P[j]*wa; qnum+=Q[j]*wa;
      }
      assertion(val===7*maxScore,"not support optimal");
      assertion(tie===t*qT,"incorrect tied mass");
      assertion(pnum>=0&&pnum<=7*P.reduce((a,b)=>a+b,0),"invalid P probability");
      assertion(qnum>=0&&qnum<=7*Q.reduce((a,b)=>a+b,0),"invalid Q probability");
      interpolations++;
    }
  }
  assertion(M<=2*Kh&&Kh<=H,"cardinality bound fails");
  return {Kh,M,ratios:reps.length,interpolations:interpolations,bank_histogram:hist};
}
function exactFaceGraph(sign,Q,K){
  const H=sign.length,Y=sign[0].length,limit=K**H,powers=Array.from({length:H},(_,h)=>K**h);
  const valid=new Map();
  let Qt=0;for(let h=0;h<H;h++)for(let y=0;y<Y;y++)if(sign[h][y]===0)Qt+=Q[h*Y+y];
  for(let code=0;code<limit;code++){
    let tmp=code,ok=true;const f=[],mask=Array(K*Y).fill(0);
    for(let h=0;h<H;h++){
      const m=tmp%K;tmp=Math.floor(tmp/K);f.push(m);
      for(let y=0;y<Y;y++){
        const value=sign[h][y];
        mask[m*Y+y]|=value>0?1:value<0?2:0;
        if(mask[m*Y+y]===3){ok=false;break;}
      }
      if(!ok)break;
    }
    if(!ok)continue;
    let L=0,U=0;
    for(let h=0;h<H;h++)for(let y=0;y<Y;y++)if(sign[h][y]===0){
      const m=mask[f[h]*Y+y],q=Q[h*Y+y];
      if(m===1){L+=q;U+=q;}else if(m===0){U+=q;}
    }
    valid.set(code,{f,mask,L,U});
  }
  const left=new Set(valid.keys()),components=[];
  while(left.size){
    const root=left.values().next().value;
    left.delete(root);const stack=[root];let low=valid.get(root).L,up=valid.get(root).U,count=0;
    while(stack.length){
      const code=stack.pop(),a=valid.get(code);count++;
      low=Math.min(low,a.L);up=Math.max(up,a.U);
      for(let h=0;h<H;h++)for(let newm=0;newm<K;newm++){
        if(newm===a.f[h])continue;
        const z=code+(newm-a.f[h])*powers[h];
        if(!left.has(z))continue;
        const b=valid.get(z);
        let ok=true;
        for(let v=0;v<K*Y;v++)if((a.mask[v]|b.mask[v])===3){ok=false;break;}
        if(ok){left.delete(z);stack.push(z);}
      }
    }
    components.push({low,up,vertex_count:count});
  }
  const merged=[];
  for(const c of components.slice().sort((a,b)=>a.low-b.low||a.up-b.up)){
    const old=merged[merged.length-1];
    if(old&&c.low<=old[1])old[1]=Math.max(old[1],c.up);
    else merged.push([c.low,c.up]);
  }
  return {valid_encoders:valid.size,components:components.length,component_intervals:components.map(x=>[x.low,x.up]),covered:merged.length===1&&merged[0][0]===0&&merged[0][1]===Qt,Qt,merged};
}
function run(){
  const rng=makeRng(20261027);
  const report={
    schema:"EM_R4_EC48D_TWO_BANK_EXACT_V1",
    math_status:"AUTHOR_SIDE_PROVED_GENERAL_BOUND; FINITE_EXECUTED_CHECKS; NOT_NATIVE_ACCEPTANCE",
    exact_arithmetic:"All integer values/products are bounded below 2^53; no floating approximation in decisions.",
    source_model:"two-stage strictly positive separately normalized rational P,Q; binary terminal decisions",
    seed:20261027,coherent_interpolation:{models:0,thresholds:0,checks:0,Kh_max:0,M_max:0,
      examples:[],cardinality_histogram:{}},
    targeted_seedless_graph:{generated:0,eligible:0,face_checks:0,multicomponent:0,
      exact_missing_faces:0,configurations:[],largest_components:0}
  };
  function collect(P,Q,H,Y,label){
    const s=profileData(P,Q,H,Y), c=report.coherent_interpolation;
    c.models++;c.thresholds+=s.ratios;c.checks+=s.interpolations;
    c.Kh_max=Math.max(c.Kh_max,s.Kh);c.M_max=Math.max(c.M_max,s.M);
    const tag=s.Kh+":"+s.M;c.cardinality_histogram[tag]=(c.cardinality_histogram[tag]||0)+1;
    if(label)c.examples.push({label,H,Y,P,Q,K_hull:s.Kh,bank_bound:s.M,full_history_bound:Math.min(H,s.M),ratios:s.ratios});
    return s;
  }
  collect([3,2,2,3,1,2,2,1],Array(8).fill(1),4,2,"four-history crossing-square");
  for(const [H,Y,N] of [[6,3,250],[7,3,180],[6,4,180]]){
    for(let t=0;t<N;t++){
      const P=[],Q=[];for(let j=0;j<H*Y;j++){P.push(1+rng(9));Q.push(1+rng(9));}
      collect(P,Q,H,Y,null);
    }
  }
  const configs=[[2,7,4,240],[3,6,3,350],[3,7,3,240],[3,6,4,200]];
  for(const [K,H,Y,N] of configs){
    const words=Array.from({length:2**Y},(_,i)=>i);
    let eligible=0,multi=0,maxcomps=0,checks=0;
    for(let i=0;i<N;i++){
      function choose(){const pool=words.slice(),a=[];for(let j=0;j<K;j++){const z=rng(pool.length);a.push(pool[z]);pool.splice(z,1);}return a;}
      const left=choose(),right=choose();
      const pairs=[];
      for(const a of left)for(const b of right)if((a&b)===b)pairs.push([a,b]);
      if(!pairs.length)continue;
      const sign=[],P=[],Q=[];let anyTie=false;
      for(let h=0;h<H;h++){
        const [a,b]=pairs[rng(pairs.length)];const row=[];
        for(let y=0;y<Y;y++){
          const bit=1<<y,lv=(a&bit)?1:0,rv=(b&bit)?1:0;
          const v=lv===rv?(lv?1:-1):0;row.push(v);
          const q=1+rng(9);Q.push(q);P.push(q*(v+2));
          if(v===0)anyTie=true;
        }
        sign.push(row);
      }
      if(!anyTie)continue;
      eligible++;
      const s=collect(P,Q,H,Y,null);
      assertion(s.Kh<=K,"synthetic hull budget exceeded");
      const graph=exactFaceGraph(sign,Q,K);checks++;
      if(!graph.covered)throw Error("EXACT_GAP "+JSON.stringify({K,H,Y,P,Q,sign,graph}));
      if(graph.components>1)multi++;
      maxcomps=Math.max(maxcomps,graph.components);
    }
    report.targeted_seedless_graph.generated+=N;
    report.targeted_seedless_graph.eligible+=eligible;
    report.targeted_seedless_graph.face_checks+=checks;
    report.targeted_seedless_graph.multicomponent+=multi;
    report.targeted_seedless_graph.largest_components=Math.max(report.targeted_seedless_graph.largest_components,maxcomps);
    report.targeted_seedless_graph.configurations.push({K,H,Y,generated:N,eligible,face_checks:checks,multicomponent:multi,largest_components:maxcomps,gaps:0});
  }
  return report;
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module){
  console.log(JSON.stringify(run(),null,2));
}
