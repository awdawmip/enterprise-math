'use strict';
// R4-EC43: exactly integer-scaled Bellman observer certificate.
// Node source probabilities are integers divided by 16.
// Source: local author proof, not native Heartbeat/X6 dynamics.
function ec43_verify(){
const ex={a:{P:[3,3,1,1],Q:[1,1,3,3]},b:{P:[3,1,3,1],Q:[1,3,1,3]}};
function build(coarse){
 const nodes=new Map();
 function put(id,t,p,q,parent){nodes.set(id,{id,t,p,q,parent,children:[]})}
 if(coarse)put("x",1,16,16,null);
 else for(const h of ["a","b"])put(h,1,8,8,null);
 for(const h of ["a","b"])for(let z=0;z<2;z++){
   put(h+z,2,ex[h].P[2*z]+ex[h].P[2*z+1],ex[h].Q[2*z]+ex[h].Q[2*z+1],coarse?"x":h);
   for(let v=0;v<2;v++){const j=2*z+v;put(h+z+v,3,ex[h].P[j],ex[h].Q[j],h+z)}
 }
 for(const n of nodes.values())if(n.parent!==null)nodes.get(n.parent).children.push(n.id);
 return {nodes,roots:coarse?["x"]:["a","b"]};
}
const full=build(false),comp=build(true);
for(const {nodes} of [full,comp])for(const n of nodes.values()){
  if(!(n.p>0&&n.q>0))throw Error("nonpositive weight");
  if(n.children.length){
    const ch=n.children.map(id=>nodes.get(id));
    if(ch.reduce((v,y)=>v+y.p,0)!==n.p||ch.reduce((v,y)=>v+y.q,0)!==n.q)throw Error("mass conservation");
  }
}
function score(t,l){
 const memo=new Map(),choice=new Map();
 function visit(id){
  if(memo.has(id))return memo.get(id);
  const n=t.nodes.get(id),d=n.t*(l[2]*n.p+l[3]*n.q);
  const actions=[["P",l[1]*n.q+d],["Q",l[0]*n.p+d]];
  if(n.children.length)actions.push(["C",n.children.reduce((sum,child)=>sum+visit(child),0)]);
  let best=actions[0];
  for(const a of actions)if(a[1]<best[1])best=a;
  choice.set(id,best[0]);memo.set(id,best[1]);return best[1];
 }
 const value=t.roots.reduce((sum,id)=>sum+visit(id),0);
 return {value,roots:Object.fromEntries(t.roots.map(id=>[id,memo.get(id)])),map:memo,choice};
}
let checked=0,gaps=0;
for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
 const l=[a,b,c,d],f=score(full,l).value,q=score(comp,l).value;
 const s=8*(Math.min(a,b)+c+d);
 const after=h=>score({nodes:full.nodes,roots:[h+"0",h+"1"]},l).value;
 const expectF=Math.min(s,after("a"))+Math.min(s,after("b"));
 const expectQ=Math.min(2*s,after("a")+after("b"));
 if(f!==expectF||q!==expectQ||q<f)throw Error("independent support mismatch "+l);
 if(q>f)gaps++;
 checked++;
}
const l=[6,6,1,1],f=score(full,l),q=score(comp,l);
if(f.value!==120||q.value!==128||f.roots.a!==56||f.roots.b!==64)throw Error("exact witness");
const par={P:[3,1],Q:[1,3]}; // denominators 4
if(par.P[1]===par.Q[1])throw Error("forgetful witness");
function certificate(t,v){
 return Object.fromEntries([...t.nodes.entries()].map(([id,n])=>[id,{depth:n.t,mass_P_over_16:n.p,mass_Q_over_16:n.q,children:n.children,U_scaled_96:v.map.get(id),min_action:v.choice.get(id)}]));
}
return {
 schema:"EM_R4_EC43_BELLMAN_VERIFICATION_V1",
 research_unit:"R4-EC43",test_status:"PASS",arithmetic:"exact integer source masses /16; integer normals, no floating point",
 node_counts:{full:full.nodes.size,compressed_first_stage:comp.nodes.size},
 normal_grid:{domain:"{-2,-1,0,1,2}^4",checked,strict_support_gaps:gaps,independent_first_stage_decomposition_checked:checked},
 witness:{normal_scaled_6:l,root_dual_scaled_96:{a:f.roots.a,b:f.roots.b,x:q.roots.x},V_full_scaled_96:f.value,V_compressed_scaled_96:q.value,support_gap:"1/12"},
 bellman_certificate:{full:certificate(full,f),compressed:certificate(comp,q)},
 nonprefix_obstruction:{initial_P_over_4:par.P,initial_Q_over_4:par.Q,actual_reach_P:"1/4",actual_reach_Q:"3/4",aggregated_uncontrolled_mass:["1","1"],common_survival_scalar_exists:false},
 theorem_scope:"finite prefix-respecting two-measure positive-rational labelled-source stopping trees",
 author_side_python_evidence:"Separate local Python Fraction verifier passed 625 normal checks, 200 rational randomized policy path/flow checks and 27 structural checks; Python source in local downloadable ZIP, not executed by this JavaScript file.",
 native_X6_test:"NOT_PERFORMED",independent_Driver_review:"NOT_PERFORMED",formal_proof_checker:"NOT_PERFORMED"
};
}
if(typeof module!=='undefined' && require.main===module){
 process.stdout.write(JSON.stringify(ec43_verify(),null,2)+'\n');
}
module.exports={ec43_verify};
