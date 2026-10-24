"use strict";
(function () {
  // Exact finite-horizon BRC certificates; no floating-point sign tests.
  function insist(x, why) { if (!x) throw Error(why); }
  function gcd(a,b) { while (b) { let t=a%b;a=b;b=t; } return a; }
  function rat(n,d) { insist(d>0n,"denominator"); const g=gcd(n,d);return {n:n/g,d:d/g}; }
  function max(a,b) { return a.n*b.d>=b.n*a.d?a:b; }
  function min(a,b) { return a.n*b.d<=b.n*a.d?a:b; }
  function fmt(a) { return a.n.toString()+(a.d===1n?"":"/"+a.d); }
  function example(name, raw, edges, route, expectedM, expectedN) {
    const weights=raw.map(row=>row.map(BigInt)), A=weights.length, V=weights[0].length;
    const den=weights.map(row=>row.reduce((s,t)=>s+t,0n));
    insist(A===2 && V>=3 && raw.every(row=>row.length===V && row.every(z=>z>0)), "positive finite model");
    const degree=Array.from({length:V}, (_,i)=>BigInt(edges.filter(e=>e.includes(i)).length));
    const used=[...new Set(route.filter(z=>z!==null))];
    insist(used.length>0,"nonempty good graph");
    const s=weights.map(row=>edges.map(e=>row[e[0]]+row[e[1]]));
    for(let b=0;b<A;b++)for(let e=0;e<edges.length;e++)
      insist(s[b][e]<den[b],"proper edge probability");
    let rho=rat(0n,1n), L=rat(0n,1n), eta=rat(1n,1n);
    for(let b=0;b<A;b++)for(let i=0;i<V;i++) if(degree[i]>0n) {
      const e=route[i];insist(e!==null && edges[e].includes(i),"incident assignment");
      rho=max(rho,rat(weights[b][i],s[b][e]));
    }
    for(let a=0;a<A;a++)for(const e of used) {
      let demand=0n;
      for(let i=0;i<V;i++)if(route[i]===e)demand+=degree[i]*(den[a]-weights[a][i]);
      L=max(L,rat(demand,den[a]));
      eta=min(eta,rat(den[a]-s[a][e],den[a]));
    }
    insist(rho.n<rho.d && eta.n>0n && L.n>0n,"strict exponential separation");
    let M=1;
    function certified(k) {
      return L.n*rho.n**BigInt(k)*eta.d <= eta.n*L.d*rho.d**BigInt(k);
    }
    while(!certified(M))M++;
    insist(M===1 || !certified(M-1),"least integer M");
    const N=A*(M-1)+1;
    insist(M===expectedM && N===expectedN,"expected reference thresholds");
    let slackChecks=0, positiveSlacks=0, incrementChecks=0;
    function powerBase(arr,x,y) { return arr[0]**BigInt(x)*arr[1]**BigInt(y); }
    function W(i,x,y) { return powerBase(weights.map(row=>row[i]),x,y); }
    function E(e,x,y) { return powerBase(s.map(row=>row[e]),x,y); }
    function occNum(x,y) {
      let v=0n;
      for(let e=0;e<edges.length;e++)v+=E(e,x,y);
      for(let i=0;i<V;i++)v-=degree[i]*W(i,x,y);
      return v;
    }
    function incNum(x,y,a) {
      let v=0n;
      for(let i=0;i<V;i++)v+=degree[i]*(den[a]-weights[a][i])*W(i,x,y);
      for(let e=0;e<edges.length;e++)v-=(den[a]-s[a][e])*E(e,x,y);
      return v;
    }
    // Every boundary count vector has an explicitly feasible incident-only flow.
    for(let x=0;x<=N;x++) {
      const y=N-x;
      for(let a=0;a<A;a++)for(const e of used) {
        let demand=0n;
        for(let i=0;i<V;i++)if(route[i]===e)
          demand+=degree[i]*(den[a]-weights[a][i])*W(i,x,y);
        const capacity=(den[a]-s[a][e])*E(e,x,y);
        insist(capacity>=demand,"boundary flow: "+name+" ("+x+","+y+")");
        slackChecks++;if(capacity>demand)positiveSlacks++;
      }
    }
    for(let n=1;n<=Math.min(N,8);n++)for(let x=0;x<=n;x++) {
      const y=n-x;
      for(let a=0;a<A;a++) {
        const nx=x+(a===0?1:0),ny=y+(a===1?1:0);
        insist(incNum(x,y,a)===occNum(nx,ny)-den[a]*occNum(x,y),"increment identity");
        incrementChecks++;
      }
    }
    return {name,weights:raw,good_edges:edges,assigned_edge_index:route,
      rho:fmt(rho),L:fmt(L),eta:fmt(eta),M,N,
      boundary_states:N+1,assigned_flow_checks:slackChecks,
      strictly_positive_slacks:positiveSlacks,
      increment_identities:incrementChecks};
  }
  const output={
    theorem:"Effective K0 cofinality and finite-horizon predecessor completeness",
    scope:"nonempty good-pair graph, >=3 finite labels, finite actions, all q_b(i)>0",
    exact_arithmetic:"BigInt rational cross multiplication, no floating point",
    examples:[
      example("three_label_two_action",[[1,1,1],[1,2,1]],[[0,1],[1,2]],[0,0,1],6,11),
      example("prior_four_label_two_action",[[1,1,1,7],[1,1,1,8]],
              [[0,1],[0,2],[0,3],[1,2]],[0,3,1,2],23,45)
    ],
    statement_status:"AUTHOR_ANALYTIC_PROOF_WITH_FINITE_REFERENCE_CHECKS__UNREVIEWED_NOT_ADMITTED"
  };
  if (typeof process !== "undefined" && process.stdout)
    process.stdout.write(JSON.stringify(output,null,2)+"\n");
  return output;
})()
