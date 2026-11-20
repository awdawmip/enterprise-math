/* X6 Unit190: exact source-equivalent integer checker (Node.js 18+). */
function runUnit190() {
  const NAX = 6;
  const caps = [[1,1,1,1,1,1],[1,2,1,2,1,2],[2,3,5,7,11,13]];
  function partitions(n) {
    const out=[];
    function rec(i,p) {
      if(i===n) {out.push(p.map(g=>g.slice())); return;}
      for(let j=0;j<p.length;j++){p[j].push(i);rec(i+1,p);p[j].pop();}
      p.push([i]); rec(i+1,p);p.pop();
    }
    rec(0,[]);
    return out;
  }
  function field(m,z) {
    return m.map((a,i)=>m.map((b,j)=>b*BigInt(z[i])-a*BigInt(z[j])));
  }
  function eqField(A,B) {
    return A.length===B.length&&A.every((r,i)=>r.every((v,j)=>v===B[i][j]));
  }
  function coarsen(m,F,p) {
    const M=p.map(g=>g.reduce((s,i)=>s+m[i],0n));
    const W=p.map(A=>p.map(B=>A.reduce((s,i)=>s+B.reduce((t,j)=>t+F[i][j],0n),0n)));
    return {M,W};
  }
  function treeEdges(p,F,mode) {
    const es=[];
    for(const g of p) for(let k=1;k<g.length;k++) {
      const i=mode==="star"?g[0]:g[k-1], j=g[k];
      es.push([i,j,F[i][j]]);
    }
    return es;
  }
  function invert(m,p,M,W,es) {
    const k=m.reduce((x,y)=>x*y,1n);
    const links=Array.from({length:6},()=>[]);
    for(const [i,j,E] of es) {
      const q=m[i]*m[j];
      if(k%q!==0n) throw Error("K not divisible by pair capacity product");
      const delta=k/q*E;
      links[i].push([j,-delta]);links[j].push([i,delta]);
    }
    const d=Array(6).fill(null);
    for(const g of p) {
      d[g[0]]=0n;
      const stack=[g[0]];
      while(stack.length) {
        const i=stack.pop();
        for(const [j,step] of links[i]) if(d[j]===null) {d[j]=d[i]+step;stack.push(j);}
      }
      for(const i of g) if(d[i]===null)throw Error("forest disconnected");
    }
    const blockId=Array(6);
    const weighted=p.map((g,A)=>{
      let t=0n;
      for(const i of g){blockId[i]=A;t+=m[i]*d[i];}
      return t;
    });
    const F=Array.from({length:6},()=>Array(6).fill(0n));
    for(let i=0;i<6;i++)for(let j=0;j<6;j++) {
      const A=blockId[i],B=blockId[j], MA=M[A],MB=M[B];
      const numerator=m[i]*m[j]*(k*W[A][B]+MA*MB*(d[i]-d[j])-MB*weighted[A]+MA*weighted[B]);
      const denominator=k*MA*MB;
      if(numerator%denominator!==0n)throw Error("non-integral reconstruction");
      F[i][j]=numerator/denominator;
    }
    return F;
  }
  function history(maxN) {
    let d=new Map([["0,0,0,0,0,0",1n]]);
    const out=[d];
    for(let n=1;n<=maxN;n++){
      const nx=new Map();
      for(const [key,v] of d) {
        const z=key.split(",").map(Number);
        for(let a=0;a<6;a++)for(const sign of [-1,1]){
          const w=z.slice();w[a]+=sign;
          const k=w.join(",");
          nx.set(k,(nx.get(k)||0n)+v);
        }
      }
      d=nx;out.push(d);
    }
    return out;
  }
  const ps=partitions(NAX), mass=history(4);
  if(ps.length!==203) throw Error("partition count");
  let forestChecks=0, srcCoarsenChecks=0, massChecks=0, treeChecks=0;
  let removalWitnesses=0, totalEndpoints=0, horizonMass=[];
  for(let n=0;n<mass.length;n++){
    const total=[...mass[n].values()].reduce((a,b)=>a+b,0n);
    if(total!==12n**BigInt(n))throw Error("native path mass");
    horizonMass.push({n,endpoints:mass[n].size,mass:String(total)});
  }
  for(const cv of caps) {
    const m=cv.map(BigInt);
    for(const p of ps){
      const baseZ=Array(6).fill(0);
      const originalZero=field(m,baseZ);
      const coarseZero=coarsen(m,originalZero,p);
      const edges=treeEdges(p,originalZero,"chain");
      for(let drop=0;drop<edges.length;drop++){
        const [u,v]=edges[drop],g=p.find(G=>G.includes(u));
        const kept=edges.filter((_,i)=>i!==drop).filter(([a])=>g.includes(a));
        const visited=new Set([u]),pending=[u];
        while(pending.length){
          const t=pending.pop();
          for(const [a,b] of kept){
            const to=a===t?b:b===t?a:null;
            if(to!==null&&!visited.has(to)){visited.add(to);pending.push(to);}
          }
        }
        if(visited.has(v))throw Error("removed edge did not split group");
        let ml=0n,mr=0n;
        for(const i of g) if(visited.has(i))ml+=m[i];else mr+=m[i];
        const delta=Array(6).fill(0n);
        for(const i of g) delta[i]=m[i]*(visited.has(i)?mr:-ml);
        if(delta.reduce((a,b)=>a+b,0n)!==0n)throw Error("witness changes total");
        const dZ=field(m,delta);
        if(!eqField(coarsen(m,dZ,p).W,coarseZero.W))throw Error("witness changes coarse field");
        for(let a=0;a<edges.length;a++){
          const [i,j]=edges[a];
          if(a===drop) {
            if(dZ[i][j]===0n)throw Error("missing edge did not change");
          } else if(dZ[i][j]!==0n) throw Error("witness changes retained relation");
        }
        const l1=delta.reduce((s,v)=>s+(v<0n?-v:v),0n);
        if(l1<=0n||l1%2n!==0n)throw Error("finite native witness invalid");
        removalWitnesses++;
      }
      for(let n=0;n<mass.length;n++){
        const fineMass=new Map(),backMass=new Map();
        for(const [key,count] of mass[n]){
          const z=key.split(",").map(Number);
          const F=field(m,z);
          const {M,W}=coarsen(m,F,p);
          const C=p.map(g=>g.reduce((s,i)=>s+BigInt(z[i]),0n));
          const direct=M.map((a,A)=>M.map((b,B)=>b*C[A]-a*C[B]));
          if(!eqField(direct,W))throw Error("source coarsen mismatch");
          srcCoarsenChecks++;
          const chain=treeEdges(p,F,"chain"),star=treeEdges(p,F,"star");
          const restored1=invert(m,p,M,W,chain),restored2=invert(m,p,M,W,star);
          if(!eqField(F,restored1)||!eqField(F,restored2))throw Error("forest inverse mismatch");
          forestChecks++;treeChecks++;
          const old=F.flat().map(String).join(",");
          const restored=restored1.flat().map(String).join(",");
          fineMass.set(old,(fineMass.get(old)||0n)+count);
          backMass.set(restored,(backMass.get(restored)||0n)+count);
          totalEndpoints++;
        }
        if(fineMass.size!==backMass.size)throw Error("BRC fiber support mismatch");
        for(const [key,value] of fineMass)if(backMass.get(key)!==value)throw Error("BRC fiber mass mismatch");
        massChecks+=fineMass.size;
      }
    }
  }
  return {
    schema:"X6_UNIT190_FOREST_REPAIR_EXACT_CHECK_V1",
    model:"signed_native_X6_path_count_and_frozen_A3_weighted_field",
    frozen_signed_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",
    frozen_source_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
    capacity_sets:caps,
    partitions:ps.length,
    horizons:horizonMass,
    source_coarsening_comparisons:srcCoarsenChecks,
    forest_inversion_comparisons:forestChecks,
    star_vs_chain_comparisons:treeChecks,
    all_fine_field_brc_mass_comparisons:massChecks,
    deleted_edge_independence_witnesses:removalWitnesses,
    violations:0,
    claim_scope:"source-equivalent independent BigInt finite execution, not actual frozen code import or R063 benchmark"
  };
}
if(typeof process!=='undefined' && process.stdout) process.stdout.write(JSON.stringify(runUnit190(),null,2)+'\n');
