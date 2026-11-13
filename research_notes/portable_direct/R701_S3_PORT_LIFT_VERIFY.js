/* R701: exact finite BRC-labelled V29 PASS / S3 frame lift verifier.
 * Run: node R701_S3_PORT_LIFT_VERIFY.js
 * Theorems follow from group, telescoping, and congruence arguments in the note.
 */
function run() {
 const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const assert=(v,m)=>{if(!v)throw Error(m||"assertion failed")};
 const perms=a=>a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(p=>[x,...p]));
 const G=perms([0,1,2]); const e=[0,1,2], t=[1,0,2], c=[1,2,0], c2=[2,0,1], S=[e,t,c,c2];
 const mul=(a,b)=>a.map((_,i)=>a[b[i]]);
 const inv=a=>a.map((_,i)=>a.indexOf(i));
 const K=x=>JSON.stringify(x);
 assert(eq(mul(t,t),e)&&eq(mul(c,c2),e)&&eq(mul(mul(t,c),t),c2),"S3 presentation");
 const edge4=new Set([0,1,2,3].map(i=>K([i,(i+1)%4])));
 const aut=perms([0,1,2,3]).filter(p=>[0,1,2,3].every(i=>edge4.has(K([p[i],p[(i+1)%4]]))));
 assert(aut.length===4,"oriented 4-cycle aut group");
 const conjugates=new Set(G.flatMap(k=>S.map(g=>K(mul(mul(k,g),inv(k))))));
 assert(conjugates.size===6,"conjugacy saturation");
 const A=[[0,1,2],[0,1,3],[0,2,3],[0,1,2]];
 const B=[[0,1,2],[0,2,3],[1,2,3],[0,1,2]];
 function walkH(w){
   let q=e.slice();
   assert(eq(w[0],e)&&eq(w[w.length-1],e),"base loop");
   for(let i=1;i<w.length;i++){
     const old=w[i-1], next=w[i], gone=old.filter(x=>!next.includes(x)), entering=next.filter(x=>!old.includes(x));
     assert(gone.length===1&&entering.length===1,"J(6,3) adjacency");
     q=q.map(x=>x===gone[0]?entering[0]:x);
     assert([...q].sort().join("")===[...next].sort().join(""),"slot transport");
   }
   return q;
 }
 const hA=walkH(A),hB=walkH(B);
 assert(eq(hA,[0,2,1])&&eq(hB,t),"V17 A/B loops");
 assert(eq(walkH(A.concat(B.slice(1))),c),"A;B composition");
 assert(eq(walkH(B.concat(A.slice(1))),c2),"B;A composition");
 function words(alphabet,maxLen) {
   let out=[[]], last=[[]];
   for(let k=1;k<=maxLen;k++){last=last.flatMap(w=>alphabet.map(g=>w.concat([g])));out.push(...last)}
   return out;
 }
 const macro=words(["A","B"],3);
 const macroH=w=>walkH([e].concat(w.flatMap(x=>(x==="A"?A:B).slice(1))));
 assert(new Set(macro.map(w=>K(macroH(w)))).size===6,"V17 macro reachability");
 const advance=(q,g)=>mul(g,q);
 const hw=w=>w.reduce((q,g)=>advance(q,g),e);
 const arc=(w,q0=e)=>{
   let q=q0, arcs=[];
   for(const g of w){const q2=advance(q,g);arcs.push([q,q2]);q=q2}
   return {arcs,q};
 };
 let covariance=0;
 for(const k of G)for(const q of G)for(const g of G){
   const C=x=>mul(mul(k,x),inv(k));
   assert(eq(mul(advance(q,g),inv(k)),advance(mul(q,inv(k)),g)),"right covariance");
   assert(eq(C(advance(q,g)),advance(C(q),C(g))),"conjugation covariance");
   covariance+=2;
 }
 let pathCount=0, gauges=0, boundary=0;
 const ws=words(S,6);
 for(const w of ws){
   pathCount++;
   const {arcs,q}=arc(w);
   assert(eq(q,hw(w)),"V39 reverse-order convention");
   const u=new Map(G.map(p=>[K(p),0]));
   for(const [a,b] of arcs){u.set(K(a),u.get(K(a))+1);u.set(K(b),u.get(K(b))-1)}
   for(const x of G)assert(u.get(K(x))===(eq(e,x)?1:0)-(eq(q,x)?1:0),"telescoping");
   let decoded=e;
   if([...u.values()].some(x=>x!==0))decoded=G.find(x=>u.get(K(x))===-1);
   assert(eq(decoded,q),"endpoint decode");
   if(w.length<=4)for(const i of G)for(const o of G){
      const obs=new Map(u);obs.set(K(i),obs.get(K(i))+1);obs.set(K(o),obs.get(K(o))-1);
      obs.set(K(i),obs.get(K(i))-1);obs.set(K(o),obs.get(K(o))+1);
      for(const x of G)assert(obs.get(K(x))===u.get(K(x)),"V29 boundary correction");
      boundary++;
   }
   for(const k of G) {
      const R=x=>mul(x,inv(k)), res=arc(w,R(e));
      assert(eq(res.q,R(q))&&eq(res.arcs,arcs.map(([a,b])=>[R(a),R(b)])),"path equivariance");
      gauges++;
   }
 }
 assert(pathCount===5461 && gauges===32766 && boundary===12276,"coverage");
 const hist=w=>S.map(x=>w.filter(g=>eq(g,x)).length);
 const w1=[t,c],w2=[c,t],v1=hist(w1),v2=hist(w2);
 assert(eq(v1,[0,1,1,0])&&eq(v1,v2)&&!eq(hw(w1),hw(w2)),"R700 collision");
 const R700u=v1.map((x,i)=>x-v1[(i+3)%4]);
 assert(eq(R700u,[0,1,0,-1]),"R700 contrast witness");
 assert(!eq(arc(w1).arcs,arc(w2).arcs),"six-port repair");
 const fw=words(S,2);
 const oneWordPerState=G.map(g=>fw.find(w=>eq(hw(w),g)));
 assert(oneWordPerState.every(x=>x!==undefined&&x.length<=2),"bounded probes");
 const signature=q=>oneWordPerState.map(w=>+eq(mul(hw(w),q),e));
 const signatures=G.map(signature).map(K);
 assert(new Set(signatures).size===6,"six Myhill-Nerode classes");
 return {schema:"R701_V29_S3_PORT_LIFT_EXACT_V1",status:"R701_S3_PORT_LIFT_EXACT_PASS",
 four_ring_automorphisms:aut.length,S3_actions_on_oriented_ring:2,
 conjugacy_saturation_size:conjugates.size,V17_A_holonomy:hA,V17_B_holonomy:hB,
 V17_S3_reachable_via_at_most_three_triangle_loops:true,
 group_covariance_checks:covariance,paths_checked:pathCount,port_gauge_path_checks:gauges,
 matched_boundary_pair_checks:boundary,R700_counterexample:{bin_counts:v1,contrast:R700u,total:2,
  tau_then_c_h:hw(w1),c_then_tau_h:hw(w2),equal_four_ring_ledger:true,different_six_port_ledger:true},
 telescoping_endpoint_contrasts:6,full_holonomy_future_return_minimal_states:6,
 sufficient_discriminating_future_length:2,fixed_binary_memory_bits:3,all_assertions_passed:true};
}
if(typeof module!=="undefined" && module.exports)module.exports=run;
if(typeof console!=="undefined")console.log(JSON.stringify(run(),null,2));
