/* R695b exact integer port-gate affine-rank BRC certificate. Sources R692 PR #1985 and R692C. */
const result=(function verifyR695b(){
 const n=[24,18,6,12],assert=(p,msg)=>{if(!p)throw Error(msg)};
 assert(n.reduce((a,b)=>a+b)===60&&n.every(x=>x>0),"base BRC count");
 const single=n.map((_,g)=>n.map((x,h)=>x-(g===h?1:0)));
 assert(single.every(x=>x.reduce((a,b)=>a+b)===59),"one unique third-step gate removes one source");
 const base=single[3], delta=[0,1,2].map(g=>single[g].slice(0,3).map((v,i)=>v-base[i]));
 assert(JSON.stringify(delta)==='[[-1,0,0],[0,-1,0],[0,0,-1]]',"affine rank 3");
 const L=single[0].map((v,i)=>3*v+single[3][i]);
 const R=single[1].map((v,i)=>2*v+2*single[2][i]);
 assert(JSON.stringify(L)==="[93,72,24,47]","left mixed candidate");
 assert(JSON.stringify(R)==="[96,70,22,48]","right mixed candidate");
 assert(L.reduce((a,b)=>a+b)===236&&R.reduce((a,b)=>a+b)===236,"mixture mass");
 const probe1=x=>2*x[0]+3*x[1],probe4=x=>2*x[0]+x[1]+2*x[2];
 assert(probe1(L)===probe1(R)&&probe1(L)===402,"A=201/590");
 assert(probe4(L)===probe4(R)&&probe4(L)===306,"B=153/590");
 assert(R[0]-L[0]===3,"one-step contrast");
 assert(24*5-2*59===2,"one-port e return residual 2/295");
 for(let e=0;e<=236;e+=13)for(let t=0;t<=236-e;t+=17)for(let c=0;c<=236-e-t;c+=19){
  const z=236-e-t-c;
  const A=2*e+3*t,B=2*e+t+2*c;
  const xx=(A-2*e)/3,yy=(B-2*e-xx)/2;
  assert(xx===t&&yy===c&&236-e-xx-yy===z,"three-probe reconstruction");
 }
 return {schema:"R695B_STATIC_PORT_TOMOGRAPHY_V1",status:"R695B_ALL_EXACT_ASSERTIONS_PASS",
 upstream_port_source:"2b393a2f2df78faadf4dff69b9694742692d29d3",
 upstream_port_source_blob:"dea329fcac6e7fa8499452d761b9e2e23fd4f573",
 static_port_group_counts:n,one_gate_deletion_laws_numerator_over_59:single,rank_determinant:"-1/59^3",
 r1_full:"2/5",r1_after_deleting_c2:"24/59",r1_difference:"2/295",
 left_over_236:L,right_over_236:R,
 shared_probe1:"201/590",shared_probe4:"153/590",r1_witness_difference:"3/236",
 minimal_scalar_observations_for_convex_field_mixtures:3,
 scope:"E* candidate external suffix probe, not native V29/V39"};
})();
console.log(JSON.stringify(result,null,2));
