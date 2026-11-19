/** Unit172 independent frozen K4 orientation-cover geodesic BRC checker.
 * Run: node research_checks/X6_UNIT172_K4_COVER_GEODESIC_BRC_CHECK_20261120.js
 * Reference scientific code: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3
 * Finite derived graph; does not rerun R063 native benchmark.
 */
const runUnit172 = function runUnit172(){
  const edges=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],faces=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
  const states=Array.from({length:4},(_,i)=>[[i,0],[i,1]]).flat();
  const idx=(a,b)=>edges.findIndex(([x,y])=>x===Math.min(a,b)&&y===Math.max(a,b));
  const assignments=Array.from({length:64},(_,k)=>Array.from({length:6},(_,j)=>(k>>j)&1));
  const gauges=Array.from({length:16},(_,k)=>Array.from({length:4},(_,j)=>(k>>j)&1));
  function check(ok,why){if(!ok)throw new Error(why)}
  function hol(E){return faces.map(f=>E[idx(f[0],f[1])]^E[idx(f[0],f[2])]^E[idx(f[1],f[2])])}
  function neighbors(E,u){const [i,s]=u;return [0,1,2,3].filter(j=>j!==i).map(j=>[j,s^E[idx(i,j)]])}
  const key=u=>`${u[0]},${u[1]}`;
  function bfs(E,src){
    const D=new Map([[key(src),0]]),B=new Map([[key(src),1]]),Q=[src];
    for(let z=0;z<Q.length;z++){let u=Q[z],du=D.get(key(u));
      for(const v of neighbors(E,u)){let vkey=key(v);
        if(!D.has(vkey)){D.set(vkey,du+1);B.set(vkey,B.get(key(u)));Q.push(v)}
        else if(D.get(vkey)===du+1)B.set(vkey,B.get(vkey)+B.get(key(u)))
      }}
    return {D,B}
  }
  function histkey(d,b){return `${d}|${b}`}
  function histAdd(H,d,b){let k=histkey(d,b);H.set(k,(H.get(k)||0)+1)}
  function asItems(H){
    return Array.from(H.entries()).map(([k,n])=>{const [d,b]=k.split("|");return [d==="unreachable"?"unreachable":Number(d),Number(b),n]})
      .sort((a,b)=>(a[0]==="unreachable"?999:a[0])-(b[0]==="unreachable"?999:b[0])||a[1]-b[1])
  }
  const expected={
    0:[[1,1,12],["unreachable",0,16]],
    2:[[1,1,12],[2,1,8],[2,2,2],[3,2,4],[3,4,2]],
    4:[[1,1,12],[2,2,12],[3,6,4]]
  };
  const expectedRow={
    0:[["[[0,1,1],[1,1,3],[\"unreachable\",0,4]]",8]],
    2:[["[[0,1,1],[1,1,3],[2,1,2],[3,2,2]]",4],["[[0,1,1],[1,1,3],[2,1,2],[2,2,1],[3,4,1]]",4]],
    4:[["[[0,1,1],[1,1,3],[2,2,3],[3,6,1]]",8]]
  };
  const strata={0:0,2:0,4:0},patterns=new Map(),samples={},gaugeCounters={assignments:0,pairs:0};
  for(const E of assignments){
    const h=hol(E),w=h.reduce((a,b)=>a+b,0);check(w in strata,"face parity");
    strata[w]++;let hk=h.join("");patterns.set(hk,(patterns.get(hk)||0)+1);
    let profiles=new Map(),pairs=new Map(),mass=0;
    const runs=states.map(u=>bfs(E,u));
    for(let i=0;i<8;i++){
      let row=new Map();
      for(let j=0;j<8;j++){
        const vkey=key(states[j]),D=runs[i].D.get(vkey),B=runs[i].B.get(vkey);
        let d=D===undefined?"unreachable":D,b=B===undefined?0:B;
        histAdd(row,d,b);if(j>i)histAdd(pairs,d,b);if(B!==undefined)mass+=B;
      }
      let p=JSON.stringify(asItems(row));profiles.set(p,(profiles.get(p)||0)+1);
      check(neighbors(E,states[i]).length===3,"degree");
    }
    check(JSON.stringify(asItems(pairs))===JSON.stringify(expected[w]),"global pair spectrum "+E);
    const profEntries=Array.from(profiles.entries()).sort((a,b)=>a[0].localeCompare(b[0]));
    check(JSON.stringify(profEntries)===JSON.stringify(expectedRow[w].slice().sort((a,b)=>a[0].localeCompare(b[0]))),"row profiles "+E);
    for(const g of gauges){
      let T=E.map((bit,k)=>bit^g[edges[k][0]]^g[edges[k][1]]);
      check(hol(T).join("")===hk,"gauge face holonomy");
      gaugeCounters.assignments++;
      const transformed=states.map(u=>bfs(T,[u[0],u[1]^g[u[0]]]));
      for(let i=0;i<8;i++)for(let j=0;j<8;j++){
        const orig=runs[i],target=key(states[j]),label=key([states[j][0],states[j][1]^g[states[j][0]]]);
        check(orig.D.get(target)===transformed[i].D.get(label) && orig.B.get(target)===transformed[i].B.get(label),"gauge-BRC covariance");
        gaugeCounters.pairs++
      }
    }
    if(!samples[w])samples[w]={edge_bits:E,face_holonomy:h,unordered_pairs:asItems(pairs),source_profile_counts:profEntries.map(([p,count])=>({source_count:count,profile:JSON.parse(p)})),ordered_path_mass_with_identity:mass}
  }
  check(JSON.stringify(strata)===JSON.stringify({0:8,2:48,4:8}),"strata");
  check(patterns.size===8&&[...patterns.values()].every(c=>c===8),"holonomy class size");
  check(gaugeCounters.assignments===1024&&gaugeCounters.pairs===65536,"gauge coverage");
  check(samples[0].ordered_path_mass_with_identity===32&&samples[2].ordered_path_mass_with_identity===88&&samples[4].ordered_path_mass_with_identity===128,"mass");
  return {schema:"X6_UNIT172_K4_COVER_BRC_EXACT_FINITE_CERTIFICATE_V1",scientific_input_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",historical_comparison_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",scope:"K4 orientation-cover geodesic multiplicities, NOT native X6 N-BRC",edge_assignments:64,face_holonomy_patterns:8,strata, gauge_checks:gaugeCounters,classes:samples,violations:0,review:"UNREVIEWED",admission:"NOT_ADMITTED"}
};
console.log(JSON.stringify(runUnit172(),null,2));
