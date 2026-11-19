"use strict";
// R762FO: standalone Node.js checker, no dependencies.
const result = (function verify() {
  const factorial = n => { let v=1; for(let i=2;i<=n;i++)v*=i; return v; };
  const perms = n => {
    let out=[];
    function rec(a, left){if(!left.length){out.push(a);return;}
      for(let i=0;i<left.length;i++)rec([...a,left[i]],left.filter((_,j)=>j!==i));
    }
    rec([],Array.from({length:n},(_,i)=>i));return out;
  };
  function edges(n, mask) {
    let e=[],bit=0;
    for(let i=0;i<n;i++)for(let j=i+1;j<n;j++,bit++)if((mask&(1<<bit))!==0)e.push([i,j]);
    return e;
  }
  function ball(n, es, root, h) {
    const adj=Array.from({length:n},()=>[]);
    for(const [u,v] of es){adj[u].push(v);adj[v].push(u);}
    const distance=Array(n).fill(-1);distance[root]=0;
    const queue=[root];
    for(let i=0;i<queue.length;i++)for(const v of adj[queue[i]])
      if(distance[v]===-1){distance[v]=distance[queue[i]]+1;queue.push(v);}
    const reached=distance.map((d,i)=>(d>=0&&d<=h)?i:-1).filter(i=>i>=0);
    return {reached,distance};
  }
  function reachable(n,es,root,h) {
    const start=Array.from({length:n},(_,i)=>i);
    let frontier=[start],seen=new Set([start.join(",")]),indices=new Set([root]);
    for(let depth=0;depth<h;depth++){
      const next=[];
      for(const p of frontier)for(const [u,v] of es) {
        const q=p.slice();[q[u],q[v]]=[q[v],q[u]];
        indices.add(q[root]);
        const key=q.join(",");
        if(!seen.has(key)){seen.add(key);next.push(q);}
      }
      frontier=next;
    }
    return [...indices].sort((a,b)=>a-b);
  }
  let graphInstances=0, cases=0, historyChecks=0;
  for(let k=1;k<=4;k++){
    const ps=perms(k), states=[];
    for(const sigma of ps)for(const tau of ps)states.push([sigma,tau]);
    const graphCount=2**(k*(k-1)/2);
    for(let m=0;m<graphCount;m++){
      graphInstances++;
      const es=edges(k,m);
      for(let root=0;root<k;root++)for(let h=0;h<k;h++){
        const {reached}=ball(k,es,root,h), r=reached.length;
        const fromWords=reachable(k,es,root,h);
        if(JSON.stringify(fromWords)!==JSON.stringify(reached))throw Error("reachable/ball mismatch");
        const classes=new Map();
        for(const [sigma,tau] of states){
          const signature=reached.map(i=>sigma[i]+":"+tau[i]).join(";");
          classes.set(signature,(classes.get(signature)||0)+1);
          historyChecks++;
        }
        const falling=factorial(k)/factorial(k-r);
        const expectedCount=falling*falling, expectedFiber=factorial(k-r)**2;
        if(classes.size!==expectedCount||[...classes.values()].some(v=>v!==expectedFiber))
          throw Error(`fiber mismatch k=${k} mask=${m} root=${root} h=${h}`);
        if((expectedFiber===1)!==(r>=k-1))throw Error("recovery threshold mismatch");
        cases++;
      }
    }
  }
  return {
    schema:"R762FO_X6_GRAPH_HORIZON_OBSERVER_V1",
    source_model:"R762FN typed (sigma,tau) matching",
    update:"swaps entire B/C partner pairs between graph-adjacent A slots; logical candidate only",
    observer:"Q_root after any known <=h swap word",
    exhaustive_k:[1,2,3,4],
    all_simple_graphs:true,all_roots:true,horizons:"0<=h<k",
    graph_instances:graphInstances,graph_root_horizon_cases:cases,
    exact_history_case_comparisons:historyChecks,
    proven_formula:"number_of_classes=(k!/(k-r)!)^2; uniform_fiber=((k-r)!)^2; r=|ball_G(root,h)|",
    recovery_horizon:"second-largest extended graph distance from root for k>=2",
    example:{
      k:4,edges:[[1,2],[2,3],[3,4]],root:1,
      by_h:[{h:0,r:1,classes:16,fiber:36,bits:4},{h:1,r:2,classes:144,fiber:4,bits:8},{h:2,r:3,classes:576,fiber:1,bits:10}],
      witness:"sigma=1234 vs sigma'=1243, tau=1234; indistinguishable at h=1, distinct after swaps (2,3),(1,2)"
    },
    status:"PASS", review:"AUTHOR_SIDE_EXACT_ENUMERATION; NOT_REVIEWED"
  };
})();
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
