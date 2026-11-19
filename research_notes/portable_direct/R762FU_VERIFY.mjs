#!/usr/bin/env node
// R762FU orientation-free two-branch positive-rational BRC kernel, exact checks.
const assert=(v,m)=>{if(!v)throw Error(m)};
const eq=(a,b)=>a.length===b.length&&a.every((x,i)=>x===b[i]);
const perm=xs=>xs.length===0?[[]]:xs.flatMap((x,i)=>perm(xs.slice(0,i).concat(xs.slice(i+1))).map(t=>[x,...t]));
const group=perm([0,1,2,3,4,5]);
const inverse=p=>{const r=Array(6);p.forEach((x,i)=>r[x]=i);return r};
const compose=(p,q)=>q.map(i=>p[i]);
const conj=(g,s)=>compose(s,compose(g,inverse(s)));
const cycle=(T,dir)=>{const g=[0,1,2,3,4,5], [a,b,c]=T;
  if(dir===1){g[a]=b;g[b]=c;g[c]=a}
  else{g[a]=c;g[b]=a;g[c]=b}
  return g;
};
const relabel=(w,g)=>w.map(x=>({...x,axis:g[x.axis]}));
const endpoint=w=>{const v=[0,0,0,0,0,0];for(const x of w)v[x.axis]+=x.sign;return v};
const change=(z,g)=>inverse(g).map(i=>z[i]);
let kernels=0,source_checks=0,minimality=0;
for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++){
  const T=[a,b,c], plus=cycle(T,1),minus=cycle(T,-1);
  const swap=[0,1,2,3,4,5];swap[a]=b;swap[b]=a;
  assert(eq(conj(plus,swap),minus),"stabilizer exchanges the two branches");minimality++;
  const w=T.map((axis,i)=>({axis,source:"src"+i,sign:i===1?-1:1,weight_num:i+1,weight_den:7}));
  for(const sigma of group){
    const U=T.map(i=>sigma[i]).sort((x,y)=>x-y);
    const left=[conj(plus,sigma),conj(minus,sigma)].map(x=>x.join(",")).sort();
    const right=[cycle(U,1),cycle(U,-1)].map(x=>x.join(",")).sort();
    assert(eq(left,right),"two-sheet kernel covariance");
    for(const g of [plus,minus]){
      const h=conj(g,sigma);
      assert(eq(relabel(relabel(w,g),sigma).map(x=>x.axis),relabel(relabel(w,sigma),h).map(x=>x.axis)),"BRC source-word functor");
      assert(eq(endpoint(relabel(w,g)),change(endpoint(w),g)),"signed BRC endpoint law");
      source_checks++;
    }
    kernels++;
  }
}
// Exact integer recurrence on the three group residues of C3.
let v=[1n,0n,0n],dpChecks=0;
for(let h=0;h<=64;h++){
  const two=2n**BigInt(h),parity=(h%2===0?1n:-1n);
  const formula=[(two+2n*parity)/3n,(two-parity)/3n,(two-parity)/3n];
  assert(eq(v,formula),"integer multiplicities vs closed form at depth "+h);
  assert(v.reduce((a,b)=>a+b,0n)===two,"total BRC paths");
  dpChecks++;
  const next=[0n,0n,0n];for(let i=0;i<3;i++){next[(i+1)%3]+=v[i];next[(i+2)%3]+=v[i]}
  v=next;
}
let explicitHistories=0;
for(let h=0;h<=12;h++){
  const counts=[0,0,0];
  for(let mask=0;mask<2**h;mask++){
    let residue=0;
    for(let j=0;j<h;j++)residue+=(mask&(1<<j))?1:2;
    counts[residue%3]++;explicitHistories++;
  }
  const two=2**h,e=h%2===0?1:-1;
  assert(eq(counts,[(two+2*e)/3,(two-e)/3,(two-e)/3]),"explicit history count h="+h);
}
assert(kernels===14400&&source_checks===28800&&minimality===20&&dpChecks===65&&explicitHistories===8191,"counts");
const evidence={schema:"R762FU_EXACT_EVIDENCE_V1",date:"2026-11-19",scope:"unordered triad T fixed across h steps; two equally weighted named rotation branches; signed BRC path provenance retained",counts:{S6_kernels:kernels,BRC_word_endpoint_checks:source_checks,branch_orbit_minimality:minimality,BigInt_dp_formula_depths:dpChecks,explicit_branch_histories:explicitHistories,explicit_depth_max:12,DP_depth_max:64},examples:{h1:[0,1,1],h2:[2,1,1],h6:[22,21,21]},formula:"n_h(0)=(2^h+2*(-1)^h)/3; n_h(1)=n_h(2)=(2^h-(-1)^h)/3",branch_mass:"each length-h path has positive rational weight 2^(-h)",pass:true,status:"AUTHOR_PROVED / NOT_REVIEWED; conditional S6 candidate kernel, no native event admission"};
process.stdout.write(JSON.stringify(evidence,null,2)+"\n");
