/* R762GD exact finite verifier. Runs under Node.js without dependencies. */
function verification(){
  const V=[0,1,2,3], E=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const stars=V.map(v=>E.map((e,i)=>e.includes(v)?i:-1).filter(i=>i>=0));
  function* comb(a,k,start=0,p=[]){if(k===0){yield p.slice();return;}for(let i=start;i<=a.length-k;i++)yield*comb(a,k-1,i+1,[...p,a[i]]);}
  function obs(z,axes){const vals=axes.map(i=>z[i]);const m=Math.min(...vals);return vals.map(x=>x-m);}
  const states=[];
  for(const S of comb([0,1,2,3,4,5],3))for(let bits=0;bits<8;bits++){const z=[0,0,0,0,0,0];S.forEach((e,j)=>z[e]=(bits>>j&1)?1:-1);states.push(z);}
  if(states.length!==160)throw Error("population");
  function fibers(obssets){const m=new Map();for(let i=0;i<states.length;i++){let s=JSON.stringify(obssets.map(q=>obs(states[i],q)));if(!m.has(s))m.set(s,[]);m.get(s).push(i);}return [...m.values()];}
  function spec(fs){const q={};for(const f of fs)q[f.length]=(q[f.length]||0)+1;return q;}
  const expected=[null,{"1":6,"6":6,"10":1,"18":6},{"1":60,"2":20,"3":20},{"1":120,"2":20},{"1":120,"2":20}];
  let kernelChecks=0,reconstructionChecks=0;
  const rows={};
  for(let k=1;k<=4;k++){const x=[];
    for(const A of comb(V,k)){
      const fs=fibers(A.map(v=>stars[v])), actual=spec(fs);
      if(JSON.stringify(actual)!==JSON.stringify(expected[k])){for(let size in expected[k])if(actual[size]!==expected[k][size])throw Error("spectrum "+k); if(Object.keys(actual).length!==Object.keys(expected[k]).length)throw Error("spectrum keys");}
      const selected=new Set(A.flatMap(v=>stars[v]));
      for(let idx=0;idx<729;idx++){let v=idx,delta=[];for(let j=0;j<6;j++){delta.push(v%3-1);v=Math.floor(v/3);}
        const actualZero=A.every(id=>obs(delta,stars[id]).every(t=>t===0));
        const predicted=new Set([...selected].map(i=>delta[i])).size===1;
        if(actualZero!==predicted)throw Error("kernel mismatch");
        kernelChecks++;
      }
      x.push({selected_vertices:A,classes:fs.length,fibre_sizes:actual,kernel_rank:1+6-selected.size});
      if(k===3)for(const z of states){
        const a=A[0], relative={[a]:0};
        const ya=obs(z,stars[a]);
        for(const other of A.slice(1)){const e=stars[a].find(e=>stars[other].includes(e));const yv=obs(z,stars[other]);relative[other]=ya[stars[a].indexOf(e)]-yv[stars[other].indexOf(e)];}
        const r=Array(6).fill(null);
        for(const v of A){const y=obs(z,stars[v]);for(let j=0;j<3;j++){let e=stars[v][j],val=y[j]+relative[v];if(r[e]!==null && r[e]!==val)throw Error("overlap");r[e]=val;}}
        if(r.includes(null))throw Error("incomplete reconstruction");
        const rm=Math.min(...r), zm=Math.min(...z);
        if(r.some((x,j)=>x-rm!==z[j]-zm))throw Error("reconstruction");
        reconstructionChecks++;
      }
    }
    rows[k]=x;
  }
  const allTriples=[...comb([0,1,2,3,4,5],3)];
  const all=fibers(allTriples), spectrum=spec(all);
  if(all.length!==140||spectrum[1]!==120||spectrum[2]!==20)throw Error("all20");
  const pairSupports=[];
  for(const ids of all.filter(v=>v.length===2)){
    let a=states[ids[0]],b=states[ids[1]];
    if(a.reduce((s,x)=>s+x,0)<0)[a,b]=[b,a];
    if(a.some((x,j)=>x-b[j]!==1))throw Error("not diagonal");
    pairSupports.push(a.map((x,i)=>x===1?i:-1).filter(i=>i>=0).join(","));
  }
  if(new Set(pairSupports).size!==20)throw Error("pair support");
  if(kernelChecks!==10935||reconstructionChecks!==640)throw Error("coverage");
  return {schema:"R762GD_EXACT_FINITE_EVIDENCE_V1",date:"2026-11-19",task:"RS-X6-TRIADIC-CLOSURE-DYNAMICS",frozen_source_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",axes_K4_edges:E,stars,endpoint_population:160,ordered_signed_BRC_paths:960,star_subfamily_partition:rows,all_twenty_triple_observers:{classes:140,fibre_sizes:spectrum},complementary_diagonal_pairs:20,complementary_pair_supports:pairSupports.sort(),finite_kernel_grid_checks:kernelChecks,three_star_reconstruction_checks:reconstructionChecks,integer_only:true,author_side:"PASS",independent_review:"NOT_REVIEWED",proof_boundary:"Universal full Z6 kernel proved by overlap argument in companion markdown; finite checker verifies 160 signed endpoints, all 15 STAR selections, and a 3^6 integer cube for each selection; no native TRIADIC_CLOSURE_E event-permission claim."};
}
const evidence=verification();
console.log(JSON.stringify(evidence,null,2));
