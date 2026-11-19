// X6 R41 typed finite BRC branch enumerator; Node.js >= 18. No external dependencies.
// Candidate one-shot whole-triad transfers; not native physical event admission.
function runR41() {
  const fact=n=>{let z=1;for(let i=2;i<=n;i++)z*=i;return z};
  const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
  const falling=(n,k)=>fact(n)/fact(n-k);
  const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
  function s2(n,r){if(n===0&&r===0)return 1;if(r<1||r>n)return 0;return r*s2(n-1,r)+s2(n-1,r-1)}
  const graphs=[], emptyGraph=[];
  for(let n=0;n<=4;n++){
    const possible=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)possible.push([i,j]);
    let summary={vertices:n,graphs_checked:0,paths_checked:0,conditional_failures:0,minimum_future_classes:null,maximum_future_classes:0};
    for(let g=0;g<(1<<possible.length);g++){
      const adj=Array(n).fill(0);for(let t=0;t<possible.length;t++)if(g&(1<<t)){let [i,j]=possible[t];adj[i]|=1<<j;adj[j]|=1<<i}
      const independent=mask=>{for(let i=0;i<n;i++)if((mask&(1<<i))&&(adj[i]&mask))return false;return true};
      const enabled=mask=>{let e=0;for(let i=0;i<n;i++)if(!(mask&(1<<i))&&!(adj[i]&mask))e|=1<<i;return e};
      const configs=Array.from({length:n+1},()=>new Map()),histories=Array(n+1).fill(0);
      let ports=Array(n).fill(-1);
      function visit(mask,k){
        histories[k]++;const key=ports.map(x=>x+1).join("");
        configs[k].set(key,(configs[k].get(key)||0)+1);
        let e=enabled(mask);
        for(let i=0;i<n;i++)if(e&(1<<i))for(let r=0;r<3;r++){ports[i]=r;visit(mask|(1<<i),k+1);ports[i]=-1}
      }
      visit(0,0);
      let futureStates=new Set();
      for(let mask=0;mask<(1<<n);mask++)if(independent(mask)){
        const e=enabled(mask);futureStates.add(e);
        for(let i=0;i<n;i++)if(e&(1<<i)){
          const after=enabled(mask|(1<<i));
          const predicted=e & ~(1<<i) & ~adj[i];
          if(after!==predicted)throw Error("non-congruent future enabled set");
        }
      }
      for(let k=0;k<=n;k++){
        let indepK=0;for(let mask=0;mask<(1<<n);mask++)if(pc(mask)===k&&independent(mask))indepK++;
        const cfg=indepK*3**k,hist=cfg*fact(k);
        if(configs[k].size!==cfg||histories[k]!==hist)throw Error("graph polynomial/serial mismatch n="+n+" g="+g+" k="+k);
        for(const multiplicity of configs[k].values())if(multiplicity!==fact(k))throw Error("fiber mismatch");
      }
      summary.graphs_checked++;summary.paths_checked+=histories.reduce((a,b)=>a+b,0);
      summary.minimum_future_classes=summary.minimum_future_classes===null?futureStates.size:Math.min(summary.minimum_future_classes,futureStates.size);
      summary.maximum_future_classes=Math.max(summary.maximum_future_classes,futureStates.size);
      if(n===3&&g===5){ /* tested as one selected graph; no special property inferred */ }
    }
    graphs.push(summary);
  }
  for(let m=0;m<=5;m++){
    let cfg=Array(m+1).fill(0),hist=Array(m+1).fill(0),rounds=[];
    for(let k=0;k<=m;k++){
      cfg[k]=choose(m,k)*3**k;hist[k]=cfg[k]*fact(k);
      let rows=[];
      for(let r=0;r<=k;r++){
        const v=(k===0&&r===0)?1:fact(r)*s2(k,r);
        let brute=0;if(k===0)brute=(r===0?1:0);
        else if(r>0)for(let a=0;a<r**k;a++){let v=a,mask=0;for(let j=0;j<k;j++){mask|=1<<(v%r);v=Math.floor(v/r)}if(mask===(1<<r)-1)brute++}
        if(brute!==(k===0&&r===0?1:v))throw Error("round surjection mismatch");
        if(v>0)rows.push({rounds:r,per_configuration:v,total_for_k:cfg[k]*v});
      }
      rounds.push({k,rows});
    }
    if(cfg.reduce((a,b)=>a+b,0)!==4**m)throw Error("4^m");
    let seen=0;for(let x=0;x<4**m;x++){let y=x,mask=0;for(let i=0;i<m;i++){let d=y%4;y=Math.floor(y/4);if(d===0)mask|=1<<i}seen|=1<<mask}
    if(m<=4&&seen!==((1<<(1<<m))-1))throw Error("missing ready masks");
    emptyGraph.push({m,decorated_configurations:4**m,named_future_language_classes:2**m,coarse_future_count_classes:m+1,configurations_by_departures:cfg,serial_histories_by_departures:hist,serialized_histories_total:hist.reduce((a,b)=>a+b,0),parallel_round_schedule_total:rounds.flatMap(x=>x.rows).reduce((a,b)=>a+b.total_for_k,0),rounds});
  }
  return {schema:"EM_X6_R41_GRAPH_GUARDED_BRC_EXACT_V1",status:"PASS",assumptions:"Permanent pairwise source exclusion G; each source carries a whole, positive, declared P000-closed triad; its three source-tagged ports are individually legal candidate transfers; static guards; disjoint moves commute; no target feedback or re-use.",observers:"Named future port event support, full current configuration, positive integer BRC serial path multiplicity, and ordered nonempty parallel batches separately typed.",graphs_exhausted_by_vertex_count:graphs,empty_graph_cases:emptyGraph,verification:"Exact integer enumeration of all graph masks n<=4 with ordered serial histories; all empty graphs n<=5 and all surjective round assignments k<=5; independent symbolic proof handles arbitrary finite n."};
}
process.stdout.write(JSON.stringify(runR41(), null, 2) + "\n");
