'use strict';
// R762BT: exact finite checks of the universal repeated-Link graph theorem.
// Run: node R762BT_REPEATED_LINK_VERIFY.js > R762BT_REPEATED_LINK_EVIDENCE.json
const certificate=(function computeCertificate(){
  const ensure=(p,msg)=>{if(!p)throw new Error(msg);};
  const permute=a=>a.length? a.flatMap((v,i)=>permute(a.filter((_,j)=>i!==j)).map(t=>[v,...t])):[[]];
  const cycleLens=p=>{const seen=new Set(), lengths=[];for(let i=1;i<=6;i++){if(seen.has(i))continue;let k=0,j=i;while(!seen.has(j)){seen.add(j);k++;j=p[j-1];}lengths.push(k);}return lengths.sort((a,b)=>a-b).join(",");};
  const full=permute([1,2,3,4,5,6]).filter(p=>cycleLens(p)==="3,3");
  const U=full.filter(p=>p[0]===2);
  ensure(full.length===40 && U.length===8,"wrong source family");
  const truthToNames=new Map();
  for(let a=1;a<=6;a++)for(let b=1;b<=6;b++)if(a!==b){
    const bits=U.map(p=>Number(p[a-1]===b));
    const n=bits.reduce((x,y)=>x+y,0);
    if(n!==0 && n!==8){
      ensure(n===2,"nonconstant atomic query is not a two-source predicate");
      const key=bits.join("");
      if(!truthToNames.has(key))truthToNames.set(key,[]);
      truthToNames.get(key).push(a+"->"+b);
    }
  }
  ensure(truthToNames.size===16 && [...truthToNames.values()].reduce((s,v)=>s+v.length,0)===20,"named query structure mismatch");
  const graph=Array.from({length:8},()=>[]);
  for(const bitkey of truthToNames.keys()){
    const vertices=[...bitkey].flatMap((c,i)=>c==="1"?[i]:[]);
    ensure(vertices.length===2,"not an edge predicate");
    const [u,v]=vertices;graph[u].push(v);graph[v].push(u);
  }
  const color=Array(8).fill(-1);color[0]=0;let queue=[0];
  for(let k=0;k<queue.length;k++)for(const v of graph[queue[k]]){
    if(color[v]<0){color[v]=1-color[queue[k]];queue.push(v);}
    else ensure(color[v]!==color[queue[k]],"graph not bipartite");
  }
  const L=[...color.keys()].filter(i=>color[i]===0),R=[...color.keys()].filter(i=>color[i]===1);
  ensure(L.length===4 && R.length===4 && graph.every(g=>g.length===4),"truth graph not K4,4");
  const queryName=Array.from({length:4},()=>Array(4).fill(null));
  for(let i=0;i<4;i++)for(let j=0;j<4;j++){
    const key=Array.from({length:8},(_,v)=>Number(v===L[i]||v===R[j])).join("");
    ensure(truthToNames.has(key),"missing K4,4 edge");
    queryName[i][j]=truthToNames.get(key)[0];
  }
  const allEdges=Array.from({length:16},(_,n)=>[Math.floor(n/4),n%4]);
  function witness(q){
    const k=Math.floor(q/6),r=q%6;
    const w=Array.from({length:4},()=>Array(4).fill(k));
    const add=es=>{for(const [i,j] of es)w[i][j]++;};
    if(r===1)add(k?allEdges.filter(([i])=>i===0):[[0,0],[1,0],[1,1],[2,2],[3,2]]);
    if(r===2)add([[0,1],[0,2],[0,3],[1,0],[2,0],[3,0]]);
    if(r===3)add([...allEdges.filter(([i,j])=>(i>=2&&j<=1)||(i<=1&&j>=2)),[0,0],[1,1]]);
    if(r===4)add(allEdges.filter(([i,j])=>i!==j));
    if(r===5)add(allEdges.filter(([i,j])=>i!==0||j!==0));
    return w;
  }
  function stats(w){
    const dr=w.map(row=>row.reduce((a,b)=>a+b,0));
    const dc=Array.from({length:4},(_,j)=>w.reduce((a,row)=>a+row[j],0));
    let cross=Infinity,same=Infinity;
    for(let i=0;i<4;i++)for(let j=0;j<4;j++)cross=Math.min(cross,dr[i]+dc[j]-2*w[i][j]);
    for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)same=Math.min(same,dr[i]+dr[j],dc[i]+dc[j]);
    return{query_count:dr.reduce((a,b)=>a+b,0),minimum_distance:Math.min(cross,same),cross_distance:cross,same_side_distance:same};
  }
  const reps=[];
  for(let q=1;q<=120;q++){
    const w=witness(q),s=stats(w);
    const k=Math.floor(q/6),r=q%6;
    const f=[0,k?4:5,6,10,12,15][r];
    ensure(s.minimum_distance===q && s.query_count===16*k+f,"incorrect construction at q="+q);
    if(q<=18)reps.push({required_distance:q,...s});
  }
  const brute=Array.from({length:7},()=>({min:Infinity,count:0}));
  for(let mask=0;mask<65536;mask++){
    const w=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>(mask>> (4*i+j))&1));
    const s=stats(w);
    for(let q=1;q<=6;q++)if(s.minimum_distance>=q){
      const v=brute[q];if(s.query_count<v.min){v.min=s.query_count;v.count=1;}
      else if(s.query_count===v.min)v.count++;
    }
  }
  const expected=[0,5,6,10,12,15,16];
  for(let q=1;q<=6;q++)ensure(brute[q].min===expected[q],"base exhaustive bound mismatch q="+q);
  const witness7=witness(7).flatMap((row,i)=>row.flatMap((n,j)=>n? [{name:queryName[i][j],repetitions:n}]:[]));
  const budgets=Array.from({length:13},(_,t)=>{const q=2*t+1,k=Math.floor(q/6),r=q%6;const links=16*k+[0,k?4:5,6,10,12,15][r];return{adversarial_flips:t,distance:q,repeated_link_calls:links,repeated_sign_calls:4*q,total_atomic_calls:links+4*q};});
  return{schema:"EM_R762BT_REPEATED_LINK_EXACT_CERTIFICATE_V1",model:"CONDITIONAL_TWO_DIRECTED_TRIADS_FIXED_ARROW_1_TO_2",source_branch_count:full.length,conditioned_branches:U.length,distinct_truth_sets:truthToNames.size,informative_named_link_queries:[...truthToNames.values()].reduce((a,v)=>a+v.length,0),bipartite_graph:"K4,4",nonnegative_integer_repetition_allowed:true,repeated_query_error_semantics:"ONE_ADVERSARIAL_BIT_FLIP_PER_RECORDED_QUERY_CALL",finite_simple_panels_examined:65536,finite_simple_panel_base_optima:brute.slice(1).map((x,i)=>({distance:i+1,min_calls:x.min,number_of_simple_optima:x.count})),constructive_exact_checks:120,constructive_examples:reps,repeated_seven_distance_named_witness:witness7,signed_fault_budgets:budgets,proof_scope:"ALL_INTEGER_DISTANCES_Q_AT_LEAST_ONE_BY_ANALYTIC_LOWER_BOUND_AND_CONSTRUCTION",native_closure_event_permission:"UNRESOLVED",independent_review:"NOT_REVIEWED"};
})();
console.log(JSON.stringify(certificate,null,2));
