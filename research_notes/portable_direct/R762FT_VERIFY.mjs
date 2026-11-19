#!/usr/bin/env node
// R762FT exact six-axis S6 and signed BRC path-formal test; no dependencies.
const assert = (condition,label) => { if (!condition) throw Error(label); };
const equal = (a,b) => a.length===b.length && a.every((v,i)=>v===b[i]);
const perms = (xs) => xs.length===0 ? [[]] :
  xs.flatMap((v,i)=>perms(xs.slice(0,i).concat(xs.slice(i+1))).map(t=>[v,...t]));
const triads = [];
for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)triads.push([a,b,c]);
const id=[0,1,2,3,4,5];
const inv=p=>{const q=Array(6);p.forEach((v,i)=>q[v]=i);return q;};
const comp=(p,q)=>q.map(i=>p[i]);
const conj=(g,s)=>comp(s,comp(g,inv(s)));
const cycle=(T,eps)=>{
  const [a,b,c]=T,p=id.slice();
  if(eps===1){p[a]=b;p[b]=c;p[c]=a;}
  else{p[a]=c;p[c]=b;p[b]=a;}
  return p;
};
const change=(z,p)=>inv(p).map(i=>z[i]);
const rotate=(z,c,g)=>{const u=change(z.map((v,i)=>v-c[i]),g);return c.map((v,i)=>v+u[i]);};
const word=(T,sgn)=>T.map((axis,i)=>({axis,sign:sgn[i],source:"src"+i,numerator:i+1,denominator:7}));
const apply=(w,p)=>w.map(x=>({...x,axis:p[x.axis]}));
const endpoint=w=>{const z=[0,0,0,0,0,0];for(const x of w)z[x.axis]+=x.sign;return z;};
const all=perms(id);
assert(all.length===720 && triads.length===20,"group size");
const c=[1,0,-1,2,0,0],z=[2,-1,0,3,1,-2];
let covariance=0,brc=0,cell=0,signsChecked=0,obstructions=0,witnesses=0;
for(const T of triads){
  const [a,b]=T,trans=id.slice();trans[a]=b;trans[b]=a;
  assert(equal(conj(cycle(T,1),trans),cycle(T,-1)),"stabilizer no-go");
  obstructions++;
  const w=word(T,[1,1,1]);
  const wp=apply(w,cycle(T,1)),wm=apply(w,cycle(T,-1));
  assert(!equal(wp.map(x=>x.axis),wm.map(x=>x.axis)),"BRC oriented trace witness");
  assert(equal(endpoint(wp),endpoint(wm)),"identical terminal endpoint");
  witnesses++;
  for(const orientation of [1,-1]){
    const g=cycle(T,orientation);
    for(const s of all){
      const U=T.map(i=>s[i]).sort((x,y)=>x-y);
      const h=conj(g,s);
      assert(equal(h,cycle(U,1)) || equal(h,cycle(U,-1)),"orientation conjugation");
      assert(equal(change(rotate(z,c,g),s),rotate(change(z,s),change(c,s),h)),"full Cell covariance");
      assert(equal(apply(apply(w,g),s).map(x=>x.axis),apply(apply(w,s),h).map(x=>x.axis)),"BRC path covariance");
      assert(equal(endpoint(apply(w,g)),change(endpoint(w),g)),"BRC endpoint naturality");
      covariance++;brc++;cell++;
      for(let mask=0;mask<8;mask++){
        const sg=T.map((_,i)=>(mask>>i)&1?-1:1);
        const prod=sg.reduce((v,x)=>v*x,1);
        const transported=U.map(i=>sg[T.indexOf(inv(s)[i])]);
        const p2=transported.reduce((v,x)=>v*x,1);
        for(const omega of [-1,1]){
          assert((prod===omega)===(p2===omega),"signed parity closure");
          signsChecked++;
        }
      }
    }
  }
}
const evidence={
  schema:"R762FT_EXACT_EVIDENCE_V1",
  date:"2026-11-19",
  carrier:"native X6 signed directions and source-ordered typed BRC path words",
  counts:{triads:20,orientations:2,six_axis_permutations:720,
    conjugacy_and_orientation:covariance,
    cell_transport:cell,brc_path_and_endpoint:brc,
    signed_closure_truth:signsChecked,
    stabilizer_no_go:obstructions,
    oriented_path_fiber_witnesses:witnesses},
  information_bits:{free_oriented_triad:6,pinned_axis:5,unordered_visible_pair:3,extra_orientation_bit:1},
  scientific_status:"AUTHOR_PROVED; NOT_REVIEWED; CANDIDATE_ROTATION_ONLY",
  pass:true
};
assert(covariance===28800 && cell===28800 && brc===28800 &&
       signsChecked===460800 && obstructions===20 && witnesses===20,"counts");
process.stdout.write(JSON.stringify(evidence,null,2)+"\n");
