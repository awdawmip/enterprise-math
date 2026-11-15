"use strict";
// PREFIX-795 exact integer / GF(2) incidence rank verifier. Node.js, no dependencies.
function verify() {
  "use strict";
  let checks=0, subsetCases=0, stateCases=0, indistinguishableWitnesses=0, sampleCases=0;
  const assert=(c,msg)=>{checks++;if(!c)throw Error("CHECK_FAILED: "+msg)};
  const index=(i,j,c)=>i*c+j;
  function countComponents(b,c,edges){
    const adjacency=Array.from({length:b+c},()=>[]);
    for(const e of edges){const i=Math.floor(e/c), j=e%c;adjacency[i].push(b+j);adjacency[b+j].push(i)}
    const seen=new Set();let cc=0;
    for(let v=0;v<b+c;v++)if(!seen.has(v)){cc++;const q=[v];seen.add(v);for(let k=0;k<q.length;k++)for(const w of adjacency[q[k]])if(!seen.has(w)){seen.add(w);q.push(w)}}
    return cc;
  }
  function rankGF2(b,c,selected){
    const n=b*c,rows=[];
    for(let i=0;i<b;i++){let r=0n;for(let j=0;j<c;j++)r|=1n<<BigInt(index(i,j,c));rows.push(r)}
    for(let j=0;j<c;j++){let r=0n;for(let i=0;i<b;i++)r|=1n<<BigInt(index(i,j,c));rows.push(r)}
    for(const e of selected)rows.push(1n<<BigInt(e));
    const basis=Array(n).fill(0n);let rank=0;
    for(let row of rows){for(let p=0;p<n;p++){if((row&(1n<<BigInt(p)))===0n)continue;if(basis[p])row^=basis[p];else{basis[p]=row;rank++;break}}}
    return rank;
  }
  function analyze(b,c,selected){
    const n=b*c,sel=new Set(selected),remaining=[];
    for(let e=0;e<n;e++)if(!sel.has(e))remaining.push(e);
    const mu=remaining.length-(b+c)+countComponents(b,c,remaining);
    const rk=rankGF2(b,c,selected);
    assert(mu>=0,"nonnegative cycle rank");
    assert(rk+mu===n,`cycle rank and observer rank ${b}x${c}`);
    return mu;
  }
  function observer(b,c,K,x){
    const r0=Array(b).fill(0),r1=Array(b).fill(0),q0=Array(c).fill(0),q1=Array(c).fill(0);
    for(let i=0;i<b;i++)for(let j=0;j<c;j++){const e=index(i,j,c),v=x[e],w=K[e]-v;r0[i]+=v;r1[i]+=w;q0[j]+=v;q1[j]+=w}
    return {r0,r1,q0,q1,K:K.slice()};
  }
  function reconstruct(b,c,y0,measured){
    const n=b*c,row=y0.r0.slice(),col=y0.q0.slice(),known=Array(n).fill(null),remaining=new Set();
    for(let e=0;e<n;e++)remaining.add(e);
    for(const [e,x] of measured){const i=Math.floor(e/c),j=e%c;assert(known[e]===null,"unique toggles");known[e]=x;row[i]-=x;col[j]-=x;remaining.delete(e)}
    while(remaining.size){
      const rowDeg=Array(b).fill(0),colDeg=Array(c).fill(0);
      for(const e of remaining){rowDeg[Math.floor(e/c)]++;colDeg[e%c]++}
      let leaf=-1,kind="";
      for(let i=0;i<b;i++)if(rowDeg[i]===1){leaf=i;kind="r";break}
      if(leaf<0)for(let j=0;j<c;j++)if(colDeg[j]===1){leaf=j;kind="c";break}
      assert(leaf>=0,"complement forest peelable");
      let e=-1;for(const t of remaining)if((kind==="r"&&Math.floor(t/c)===leaf)||(kind==="c"&&t%c===leaf)){e=t;break}
      const i=Math.floor(e/c),j=e%c,val=kind==="r"?row[i]:col[j];
      assert(Number.isInteger(val)&&val>=0&&val<=y0.K[e],"recovered integral capacity");
      known[e]=val;row[i]-=val;col[j]-=val;remaining.delete(e);
    }
    assert(row.every(t=>t===0)&&col.every(t=>t===0),"all marginals exhausted");
    return known;
  }
  let seed=0x51A7F00D;
  function rand(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed}
  for(const [b,c] of [[2,2],[2,3],[3,3],[3,4]]){
    const n=b*c;
    for(let mask=0;mask<(1<<n);mask++){
      let S=[];for(let e=0;e<n;e++)if(mask&(1<<e))S.push(e);
      analyze(b,c,S);subsetCases++;
    }
  }
  for(let a=0;a<256;a++){
    const b=4,c=4,n=b*c,mask=rand()&((1<<n)-1),S=[];
    for(let e=0;e<n;e++)if(mask&(1<<e))S.push(e);
    analyze(b,c,S);sampleCases++;
  }
  for(const [b,c] of [[2,3],[3,3]]){
    const n=b*c,K=Array(n).fill(2),S=[];
    for(let i=0;i<b-1;i++)for(let j=0;j<c-1;j++)S.push(index(i,j,c));
    assert(analyze(b,c,S)===0,"basis complement a spanning tree");
    const total=3**n;
    for(let code=0;code<total;code++){
      let v=code,x=Array(n);for(let e=0;e<n;e++){x[e]=v%3;v=Math.floor(v/3)}
      const initial=observer(b,c,K,x),current=x.slice(),measured=[];let prev=initial;
      for(const e of S){
        const i=Math.floor(e/c),j=e%c;
        current[e]=K[e]-current[e];
        const next=observer(b,c,K,current);
        const delta=next.r0[i]-prev.r0[i];
        assert(delta===next.q0[j]-prev.q0[j],"row and column delta agree");
        const recovered=(K[e]-delta)/2;
        assert(Number.isInteger(recovered)&&recovered===x[e],"sequential toggle inverts exact cell");
        measured.push([e,recovered]);prev=next;
      }
      const recovered=reconstruct(b,c,initial,measured);
      assert(recovered.every((t,e)=>t===x[e]),"one trajectory exact reconstruction");
      stateCases++;
    }
  }
  function complementCycle(b,c,selected){
    const n=b*c,sel=new Set(selected),adj=Array.from({length:b+c},()=>[]);
    for(let e=0;e<n;e++)if(!sel.has(e)){
      const start=Math.floor(e/c),end=b+(e%c),queue=[start],seen=new Set([start]),pv={},pe={};
      for(let k=0;k<queue.length&&!seen.has(end);k++)for(const [v,edge] of adj[queue[k]])if(!seen.has(v)){seen.add(v);pv[v]=queue[k];pe[v]=edge;queue.push(v)}
      if(seen.has(end)){const cycle=[];let v=end;while(v!==start){cycle.push(pe[v]);v=pv[v]}cycle.push(e);return cycle}
      adj[start].push([end,e]);adj[end].push([start,e]);
    }
    return null;
  }
  {
    const b=3,c=4,n=b*c,d=(b-1)*(c-1),K=Array(n).fill(2);
    for(let t=0;t<300;t++){
      const edges=Array.from({length:n},(_,i)=>i);
      for(let j=n-1;j>0;j--){const k=rand()%(j+1);[edges[j],edges[k]]=[edges[k],edges[j]]}
      const S=edges.slice(0,t%d),cyc=complementCycle(b,c,S);
      assert(cyc!==null&&cyc.length>=4&&cyc.length%2===0,"remaining cycle for fewer than d probes");
      const x=Array(n).fill(1),xp=x.slice();
      cyc.forEach((e,i)=>xp[e]+=i%2===0?1:-1);
      assert(xp.every(v=>v>=0&&v<=2),"cycle perturbation respects capacity");
      let y=observer(b,c,K,x),yp=observer(b,c,K,xp);
      assert(JSON.stringify(y)===JSON.stringify(yp),"cycle pair indistinguishable initially");
      const u=x.slice(),up=xp.slice();
      for(const e of S){
        u[e]=2-u[e];up[e]=2-up[e];
        y=observer(b,c,K,u);yp=observer(b,c,K,up);
        assert(JSON.stringify(y)===JSON.stringify(yp),"cycle pair indistinguishable after intervention");
      }
      assert(x.some((v,i)=>v!==xp[i]),"distinct source states");
      indistinguishableWitnesses++;
    }
  }
  return {status:"ALL_CHECKS_PASS PREFIX795 SEQUENTIAL_TOGGLE_CYCLE_RANK",
    exact_arithmetic:"bounded integer + GF(2) incidence/identity rank (totally unimodular, equal to rational rank)",
    subset_cases:subsetCases,random_4x4_cases:sampleCases,
    exhaustive_histogram_states:stateCases,
    indistinguishable_cycle_witnesses:indistinguishableWitnesses,
    exact_assertions:checks,
    domains:"all selected-edge subsets for 2x2,2x3,3x3,3x4; deterministic sampled 4x4; all x in {0,1,2}^(2x3) and {0,1,2}^(3x3); 300 3x4 indistinguishability witnesses",
    proof_scope:"symbolic theorem: all b,c >=2, all nonnegative integer 2xbc histograms and one sequential observation after each exact local toggle"};
}
console.log(JSON.stringify(verify(), null, 2));
