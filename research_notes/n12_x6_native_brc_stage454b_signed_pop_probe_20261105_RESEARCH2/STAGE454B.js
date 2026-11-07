// Stage454-B: exact future-tree audit of a signed-alphabet POP/APPEND quotient.
// Node.js: node STAGE454B.js . No third-party packages, all comparisons exact.
// A=+E1, B=+E2, C=+E3; append all 12 signed X6 directions.
"use strict";
const A=0, B=1, C=2, DIRECTIONS=12, alphabet=[A,B,C];
function V(w) {
  let z=Array(6).fill(0);
  for(const x of w)z[x%6]+=x<6?1:-1;
  return z;
}
function J(w) {
  let z=Array(144).fill(0);
  for(let i=1;i<w.length;i++)z[12*w[i-1]+w[i]]++;
  return z;
}
function K(p,q) {
  let z=0;
  for(let i=0;i<Math.min(p.length,q.length);i++)z+=p[i]===q[i]?1:0;
  return z;
}
function O(p,q) {return JSON.stringify([p.length,q.length,V(p),V(q),J(p),J(q),K(p,q)]);}
function key(p,q,pops,apps) {
  let a=Math.min(pops,p.length),m=p.length,n=q.length;
  let pt=p.slice(Math.max(0,m-a-1),m-1);
  if(apps===0)
    return JSON.stringify([pt,p.slice(m-a,m).map((x,j)=>+(x===q[m-a+j]))]);
  return JSON.stringify([pt,q.slice(m-a,Math.min(n,m+apps))]);
}
// Exact canonical tree interning; no probabilistic hashes.
function tree(p,q,pops,apps,cache,intern,seq) {
  let mkey=JSON.stringify([p,q,pops,apps]);
  if(cache.has(mkey))return cache.get(mkey);
  let children=[];
  if(pops>0 && p.length)
    children.push(["POP",tree(p.slice(0,-1),q,pops-1,apps,cache,intern,seq)]);
  if(apps>0)for(let z=0;z<DIRECTIONS;z++)
    children.push(["APPEND_"+z,tree(p.concat([z]),q,pops,apps-1,cache,intern,seq)]);
  let repr=JSON.stringify([O(p,q),children]);
  let id=intern.get(repr);
  if(id===undefined){id=seq.next++;intern.set(repr,id);}
  cache.set(mkey,id);
  return id;
}
function words(n) {
  let out=[];
  function walk(w) {
    if(w.length===n){if(w[n-1]===A)out.push(w);return;}
    for(let x of alphabet)
      if(!(w.length && w[w.length-1]!==A && x!==A))walk(w.concat([x]));
  }
  walk([A]);
  return out;
}
function run(){
  let total={configurations:0,fibers:0,histories:0,pairs:0,nodes:0,distinctTrees:0,allPassed:true};
  let example={p:[A,A,A,A,A],q1:[A,B,A,C,A,A,A],q2:[A,C,A,B,A,A,A]};
  let cache=new Map(),intern=new Map(),seq={next:0};
  for(const [m,n,popts,ropts] of [[4,6,[0,1,2],[0,1,2]],[5,7,[0,1,2],[0,1]],[5,8,[0,1],[0,1]]]){
    let hs=[];
    for(let p of words(m))for(let q of words(n))hs.push({p,q,obs:O(p,q)});
    let fibers=new Map();
    for(let h of hs){
      if(!fibers.has(h.obs))fibers.set(h.obs,[]);
      fibers.get(h.obs).push(h);
    }
    for(let a of popts)for(let r of ropts){
      total.configurations++;
      for(let fiber of fibers.values()){
        total.fibers++;total.histories+=fiber.length;
        for(let h of fiber){h.k=key(h.p,h.q,a,r);h.s=tree(h.p,h.q,a,r,cache,intern,seq);}
        for(let i=0;i<fiber.length;i++)for(let j=i+1;j<fiber.length;j++){
          total.pairs++;
          if((fiber[i].k===fiber[j].k)!==(fiber[i].s===fiber[j].s))
            throw Error("EXACT_QUOTIENT_FAILURE "+JSON.stringify([m,n,a,r,fiber[i],fiber[j]]));
        }
      }
    }
  }
  const ex=example;
  const equalInitial=O(ex.p,ex.q1)===O(ex.p,ex.q2);
  const sameFuture=tree(ex.p,ex.q1,2,0,cache,intern,seq)===tree(ex.p,ex.q2,2,0,cache,intern,seq);
  const rawDifferent=ex.q1[3]!==ex.q2[3];
  if(!equalInitial||!sameFuture||!rawDifferent)throw Error("TERNARY_COUNTEREXAMPLE_FAILED");
  total.nodes=cache.size;total.distinctTrees=intern.size;
  total.example={P:"AAAAA",Q1:"ABACAAA",Q2:"ACABAAA",pops:2,appends:0,
    initialK:K(ex.p,ex.q1),postPopK1:[K(ex.p,ex.q1),K(ex.p.slice(0,-1),ex.q1),K(ex.p.slice(0,-2),ex.q1)],
    postPopK2:[K(ex.p,ex.q2),K(ex.p.slice(0,-1),ex.q2),K(ex.p.slice(0,-2),ex.q2)],
    rawQ4Different:rawDifferent,initialObserverEqual:equalInitial,futureTreeEqual:sameFuture};
  total.verdict="STAGE454B_SIGNED_POP_PROBE_IFF_FINITE_PASS";
  return total;
}
if(require.main===module)process.stdout.write(JSON.stringify(run(),null,2)+"\n");
module.exports={run,key,O,K,V,J};
