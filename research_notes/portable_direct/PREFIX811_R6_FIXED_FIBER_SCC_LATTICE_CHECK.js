"use strict";
function run() {
  "use strict";
  function gcd(a,b) { a=Math.abs(a);b=Math.abs(b);while(b){const t=a%b;a=b;b=t;}return a; }
  function assert(x,msg){if(!x)throw Error(msg);}
  function observerFamilies(m,n){
    const e=m*n, arr=[];
    if(e<=6){
      for(let code=0;code<3**e;code++){let q=code, w=[];for(let i=0;i<e;i++){w.push(q%3-1);q=Math.floor(q/3);}arr.push(w);}
    }else{
      arr.push(Array(e).fill(0),Array(e).fill(1));
      for(let j=0;j<e;j++)arr.push(Array.from({length:e},(_,i)=>i===j?1:0));
      for(let j=0;j<6;j++)arr.push(Array.from({length:e},(_,i)=>((i*7+j*3+i*j)%5)-2));
    }
    return arr;
  }
  function makeStructure(x,K,m,n){
    const N=m+n,adj=Array.from({length:N},()=>[]),rev=Array.from({length:N},()=>[]),arcs=[];
    function put(u,v,e,sgn){const i=arcs.length;arcs.push({u,v,e,sgn});adj[u].push(v);rev[v].push(u);}
    for(let e=0;e<K.length;e++){const u=Math.floor(e/n),v=m+e%n;if(x[e]<K[e])put(u,v,e,1);if(x[e]>0)put(v,u,e,-1);}
    const visited=Array(N).fill(false),order=[];
    function dfs(u){visited[u]=true;for(const v of adj[u])if(!visited[v])dfs(v);order.push(u);}
    for(let u=0;u<N;u++)if(!visited[u])dfs(u);
    const comp=Array(N).fill(-1);let cc=0;
    function assign(u){comp[u]=cc;for(const v of rev[u])if(comp[v]<0)assign(v);}
    for(let i=order.length-1;i>=0;i--){const u=order[i];if(comp[u]<0){assign(u);cc++;}}
    const parent=Array.from({length:N},(_,i)=>i);
    function root(u){while(parent[u]!==u){parent[u]=parent[parent[u]];u=parent[u];}return u;}
    const tree=Array.from({length:N},()=>[]),chords=[];
    for(let i=0;i<arcs.length;i++){
      const a=arcs[i];if(comp[a.u]!==comp[a.v])continue;
      const p=root(a.u),q=root(a.v);
      if(p!==q){parent[p]=q;tree[a.u].push({v:a.v,i,dir:1});tree[a.v].push({v:a.u,i,dir:-1});}
      else chords.push(i);
    }
    return {N,arcs,tree,chords,comp,componentCount:cc};
  }
  function predictedGCD(structure,w){
    const {N,arcs,tree,chords}=structure, p=Array(N).fill(null);
    for(let s=0;s<N;s++){if(p[s]!==null)continue;p[s]=0;const Q=[s];for(let h=0;h<Q.length;h++){const u=Q[h];for(const t of tree[u]){const c=arcs[t.i].sgn*w[arcs[t.i].e];const v=t.v;if(p[v]===null){p[v]=p[u]+t.dir*c;Q.push(v);}else assert(p[v]===p[u]+t.dir*c,"forest potential mismatch");}}}
    let g=0;for(const i of chords){const a=arcs[i];g=gcd(g,a.sgn*w[a.e]-(p[a.v]-p[a.u]));}
    return g;
  }
  const families=[{m:2,n:2,base:3},{m:2,n:3,base:2},{m:3,n:3,base:2}];
  const rows=[];let verified=0, invariant=0, varying=0, allTables=0, allFibers=0, potentialChecks=0, basepointChecks=0;
  for(const {m,n,base} of families){
    const E=m*n,ws=observerFamilies(m,n);let tests=0,cons=0,vari=0,fibers=0,tables=0,multifibers=0,bchecks=0;
    const patterns=base**E;
    for(let pattern=0;pattern<patterns;pattern++){
      let v=pattern;const K=Array(E);
      for(let e=0;e<E;e++){K[e]=v%base;v=Math.floor(v/base);}
      let total=1;for(const cap of K)total*=cap+1;
      const groups=new Map();
      for(let num=0;num<total;num++){
        let q=num;const x=Array(E),mr=Array(m+n).fill(0);
        for(let e=0;e<E;e++){x[e]=q%(K[e]+1);q=Math.floor(q/(K[e]+1));mr[Math.floor(e/n)]+=x[e];mr[m+e%n]+=x[e];}
        const key=mr.join(",");
        if(!groups.has(key))groups.set(key,[]);
        groups.get(key).push(x);tables++;
      }
      for(const xs of groups.values()){
        const x=xs[0],S=makeStructure(x,K,m,n);fibers++;if(xs.length>1)multifibers++;
        for(const w of ws){
          const g=predictedGCD(S,w);
          let observed=0;const wx=x.reduce((s,z,e)=>s+w[e]*z,0);
          for(let j=1;j<xs.length;j++){const y=xs[j];let wy=0;for(let e=0;e<E;e++)wy+=w[e]*y[e];observed=gcd(observed,wy-wx);}
          assert(g===observed,"GCD mismatch m="+m+" n="+n+" K="+K+" x="+x+" weights="+w+" g="+g+" obs="+observed);
          if(g===0)cons++;else vari++;
          tests++;verified++;
        }
        // Nontrivial basepoint-independence regression: reanchor at the last feasible table.
        if(xs.length>1){
          const Slast=makeStructure(xs[xs.length-1],K,m,n);
          for(const w of ws.slice(0,Math.min(8,ws.length))){assert(predictedGCD(Slast,w)===predictedGCD(S,w),"reanchoring changed lattice");bchecks++;}
        }
      }
    }
    rows.push({shape:`${m}x${n}`,capacities:`0..${base-1}`,capacity_patterns:patterns,observers_per_fiber:ws.length,margin_fibers:fibers,named_tables:tables,multi_table_fibers:multifibers,exact_lattice_comparisons:tests,constant_tests:cons,varying_tests:vari,reanchoring_checks:bchecks});
    invariant+=cons;varying+=vari;allTables+=tables;allFibers+=fibers;basepointChecks+=bchecks;
  }
  const fixed={capacity:[1,1,1,1,1,1],margins:{rows:[1,1],cols:[0,1,1]},x:[0,0,1,0,1,0],y:[0,1,0,0,0,1]};
  function linear(w,x){return w.reduce((s,z,e)=>s+z*x[e],0);}
  const wBlocked=[1,0,0,0,0,0],wActive=[0,1,0,0,0,0];
  assert(linear(wBlocked,fixed.x)===linear(wBlocked,fixed.y),"blocked witness");assert(linear(wActive,fixed.x)!==linear(wActive,fixed.y),"active witness");
  assert(predictedGCD(makeStructure(fixed.x,fixed.capacity,2,3),wBlocked)===0,"blocked GCD");assert(predictedGCD(makeStructure(fixed.x,fixed.capacity,2,3),wActive)===1,"active GCD");
  const diag={m:2,n:2,K:[1,1,1,1],x:[1,0,0,1],y:[0,1,1,0],w:[1,0,0,1]};
  assert(predictedGCD(makeStructure(diag.x,diag.K,2,2),diag.w)===2,"observer gap gcd 2");
  return {schema:"EM_PREFIX811_FIXED_FIBER_SCC_SIGNATURE_CHECK_V1",exact_integer_only:true,algorithm:"SCC residual-arc internal integral fundamental-cycle gcd vs exhaustive all-table observer differences",family_results:rows,totals:{capacity_patterns:rows.reduce((s,r)=>s+r.capacity_patterns,0),margin_fibers:allFibers,named_tables:allTables,exact_lattice_comparisons:verified,constant_tests:invariant,varying_tests:varying,basepoint_invariance_checks:basepointChecks},witnesses:{blocked_full_graph_curl:{...fixed,w_blocked:wBlocked,w_active:wActive,blocked_values:[linear(wBlocked,fixed.x),linear(wBlocked,fixed.y)],active_values:[linear(wActive,fixed.x),linear(wActive,fixed.y)]},observer_hole:{...diag,reachable_values:[0,2],difference_group_generator:2}},all_assertions_passed:true};
}
console.log(JSON.stringify(run(),null,2));
