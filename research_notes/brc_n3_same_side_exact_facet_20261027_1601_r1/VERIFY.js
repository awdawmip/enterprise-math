function verify(){
 const N={
  "":{t:0,s:0,p:240,q:240,c:["a","b"]},
  a:{t:1,s:2,p:180,q:120,c:["ax","ay"]},
  b:{t:1,s:1,p:60,q:120,c:["bu","bv"]},
  ax:{t:2,s:4,p:60,q:60,c:["axL","axM","axH"]},
  ay:{t:2,s:5,p:120,q:60,c:["ayT"]},
  bu:{t:2,s:4,p:30,q:30,c:["buL","buM","buH"]},
  bv:{t:2,s:3,p:30,q:90,c:["bvT"]},
  axL:{t:3,s:7,p:5,q:10,c:[]},
  axM:{t:3,s:8,p:40,q:40,c:[]},
  axH:{t:3,s:9,p:15,q:10,c:[]},
  ayT:{t:3,s:10,p:120,q:60,c:[]},
  buL:{t:3,s:7,p:3,q:6,c:[]},
  buM:{t:3,s:8,p:18,q:18,c:[]},
  buH:{t:3,s:9,p:9,q:6,c:[]},
  bvT:{t:3,s:6,p:30,q:90,c:[]}
 };
 const ok=(x,msg)=>{if(!x)throw Error(msg)};
 const L=[302,363,28,-12], J=v=>v.reduce((a,x,i)=>a+x*L[i],0);
 const names=Object.keys(N),leaves=names.filter(h=>N[h].c.length===0);
 ok(names.length===15&&leaves.length===8,"tree size");
 for(const h of names){
  const u=N[h];ok(u.p>0&&u.q>0,"positive mass");
  if(u.c.length)for(const law of ["p","q"])
   ok(u.c.reduce((a,v)=>a+N[v][law],0)===u[law],"mass conservation "+h);
 }
 const evaluation=policy=>{
  const recurse=h=>{
   const u=N[h],a=policy[h]??policy[u.s];
   if(a==="C"){
    ok(u.c.length>0,"terminal continuation");
    const z=[0,0,0,0];
    for(const child of u.c){const y=recurse(child);for(let i=0;i<4;i++)z[i]+=y[i]}
    return z;
   }
   ok(a==="P"||a==="Q","bad action");
   return [a==="Q"?u.p:0,a==="P"?u.q:0,u.t*u.p,u.t*u.q];
  };
  return recurse("");
 };
 const vectors=new Map();
 for(let n=0;n<729;n++){
  let a=n;const pol=[];
  for(let i=0;i<6;i++){pol[i]="PQC"[a%3];a=Math.floor(a/3)}
  for(let m=0;m<32;m++){
   for(let i=0;i<5;i++)pol[6+i]=((m>>i)&1)?"Q":"P";
   const v=evaluation(pol);vectors.set(v.join(","),v);
  }
 }
 ok(vectors.size===326,"distinct vector count");
 for(const v of vectors.values())ok(J(v)>=65460,"facet violated by compressed policy");
 const active=[...vectors.values()].filter(v=>J(v)===65460);
 const eq=[[120,60,420,360],[51,126,360,480],[120,60,510,570],[96,76,600,660]];
 ok(active.length===4,"equality count");
 for(const v of eq)ok(vectors.has(v.join(",")),"missing equality point");
 function det(A){
  if(A.length===1)return A[0][0];
  let z=0n;
  for(let k=0;k<A.length;k++)
   z+=((k%2)?-1n:1n)*A[0][k]*det(A.slice(1).map(row=>row.filter((_,i)=>i!==k)));
  return z;
 }
 const diff=(a,b)=>a.map((x,i)=>BigInt(x-b[i]));
 const aff=[[0,240,0,0],[240,0,0,0],[0,240,240,240],[180,120,240,240],[0,240,420,360]];
 for(const v of aff)ok(vectors.has(v.join(",")),"missing dimension point");
 ok(det(aff.slice(1).map(v=>diff(v,aff[0])))!==0n,"affine dimension");
 const faceRows=eq.slice(1).map(v=>diff(v,eq[0]));
 ok([0,1,2,3].some(k=>det(faceRows.map(row=>row.filter((_,i)=>i!==k)))!==0n),"face dimension");
 const full={"":"C",a:"C",b:"C",ax:"Q",ay:"P",bu:"C",bv:"C",axL:"Q",axM:"Q",axH:"P",ayT:"P",buL:"Q",buM:"Q",buH:"P",bvT:"Q"};
 const w=evaluation(full);ok(w.join(",")==="111,66,540,600"&&J(w)===65400,"full witness");
 function bellman(force){
  const cost=h=>{
   const u=N[h],elapsed=u.t*(L[2]*u.p+L[3]*u.q);
   const P=L[1]*u.q+elapsed,Q=L[0]*u.p+elapsed;
   const C=u.c.length?u.c.reduce((s,v)=>s+cost(v),0):Infinity;
   if(force&&(h==="ax"||h==="bu"))return {P,Q,C}[force];
   return Math.min(P,Q,C);
  };
  return cost("");
 }
 const f=bellman(null),cp=bellman("P"),cq=bellman("Q"),cc=bellman("C");
 ok(f===65400&&cp===65520&&cq===65460&&cc===65460,"Bellman minima");
 return {
  status:"PASS_EXACT_INTEGER_240",model:"strictly positive non-IID 15-prefix/8-leaf P-Q tree at sa=1/6,sb=1/5",
  exact_integer_scale:240,ordered_prefixes:15,terminal_leaves:8,
  compressed_nonterminal_classes:6,compressed_terminal_classes:5,
  deterministic_policy_tables:23328,distinct_observer_vectors:326,
  facet_support_min_lambda:[302,363,28,-12],compressed_min:"1091/4",full_min:"545/2",
  strict_facet_gap:"1/4",compressed_polytope_affine_dimension:4,
  facet_affine_dimension:3,facet_equality_points:4,
  full_history_witness:["37/80","11/40","9/4","5/2"],
  forced_collision_actions_min:{"P":"273","Q":"1091/4","C":"1091/4"},
  coverage:"Complete pure compressed-policy class, exact integer face/rank proof, exact full-history Bellman recursion and witness; random fresh local actions covered by multi-affinity argument in PROOF.md"
 };
}
console.log(JSON.stringify(verify(), null, 2));
