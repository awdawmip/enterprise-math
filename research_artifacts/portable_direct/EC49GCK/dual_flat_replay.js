function replay(){
 let seed=20261128>>>0;
 function rand(n){seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;seed>>>=0;return seed%n}
 const pc=x=>{let c=0;while(x){x&=x-1;c++}return c};
 const bits=x=>{let a=[];while(x){let b=x&-x;a.push(b);x^=b}return a};
 const sub=(x,y)=>(x&y)===x;
 const subsets=function*(m){for(let x=m;;x=(x-1)&m){yield x;if(!x)break}};
 const out={seed:20261128,models:0,originalLabelSubsets:0,states:0,componentRankChecks:0,dualFlatClosureChecks:0,dualFlatZetaChecks:0,portQueries:0,componentPortChecks:0,rankTwoComponents:0,rankTwoQueries:0,minorSplitChecks:0,signedTerms:0,negativeTerms:0,flatCountBoundChecks:0,maxTerms:0,friendship:[],theta:null,disagreements:0};
 function eq(a,b,tag){if(a!==b)throw Error(tag+" "+a+" != "+b)}
 function components(F,r){
  let B=0;for(const b of bits(F))if(r(B|b)>r(B))B|=b;
  let group=bits(F);
  for(const x of bits(F^B)){let C=x;for(const y of bits(B))if(r((B^y)|x)===pc(B))C|=y;
   let kept=[];for(const G of group)if(G&C)C|=G;else kept.push(G);kept.push(C);group=kept;
  }return group
 }
 function carrier(C,r,E){
  const m=pc(C),d=m-r(C);
  const dual=X=>pc(X)-r(C)+r(C^X);
  const closure=X=>{let Y=X,v=dual(X);for(const b of bits(C^X))if(dual(X|b)===v)Y|=b;return Y};
  let flat=new Map(),bs=bits(C);
  function gen(i,X,k){if(k>=d)return;let L=closure(X);flat.set(L,k);for(let j=i;j<bs.length;j++){let Y=X|bs[j];if(dual(Y)===k+1)gen(j+1,Y,k+1)}}
  if(d>0)gen(0,0,0);
  let fs=[...flat.entries()].sort((a,b)=>pc(b[0])-pc(a[0]));
  let weights=[], terms=new Map();
  const mask=X=>{let W=0;for(const b of bits(X))W|=E[31-Math.clz32(b)];return W};
  let bound=0,choose=1;for(let i=0;i<d;i++){bound+=choose;choose=choose*(m-i)/(i+1)}if(fs.length>bound)throw Error("flat bound");out.flatCountBoundChecks++;
  for(const [L,k] of fs){eq(closure(L),L,"flat");eq(dual(L),k,"flat rank");out.dualFlatClosureChecks++;
   let w=d-k;for(const [H,v] of weights)if(sub(L,H))w-=v;weights.push([L,w]);let W=mask(C^L);terms.set(W,(terms.get(W)||0)+w)
  }
  let ts=[...terms].filter(x=>x[1]!==0);out.signedTerms+=ts.length;out.negativeTerms+=ts.filter(x=>x[1]<0).length;out.maxTerms=Math.max(out.maxTerms,ts.length);
  for(const [L,k] of fs){let v=0;for(const [H,w] of weights)if(sub(L,H))v+=w;eq(v,d-k,"zeta");out.dualFlatZetaChecks++}
  let rank2=null;
  if(d===2){
   let loops=closure(0),parallel=[];for(const b of bits(C^loops)){let L=closure(b);if(!parallel.includes(L))parallel.push(L)}
   rank2={masks:parallel.map(L=>mask(C^L)),bottom:mask(C^loops),q:parallel.length};out.rankTwoComponents++;
  }
  return {C,d,ts,rank2}
 }
 function state(F,S,r,E,p,previous){
  out.states++;let N=X=>r(X|S)-pc(S),cs=components(F,N);
  if(previous){for(const C of cs)if(!previous.some(G=>sub(C,G)))throw Error("minor merge");out.minorSplitChecks++}
  for(const X of subsets(F)){let v=0;for(const C of cs)v+=N(X&C);eq(v,N(X),"component rank");out.componentRankChecks++}
  const cc=cs.map(C=>carrier(C,N,E));
  for(let W=0;W<1<<p;W++){
   let X=0;for(const b of bits(F))if(sub(E[31-Math.clz32(b)],W))X|=b;
   let total=0;
   for(const {C,ts,rank2} of cc){let v=0;for(const [A,w] of ts)if(sub(A,W))v+=w;eq(v,pc(C&X)-N(C&X),"component deficit");out.componentPortChecks++;total+=v;
    if(rank2){let z=0;for(const A of rank2.masks)if(sub(A,W))z++;if(sub(rank2.bottom,W))z+=2-rank2.q;eq(z,v,"rank2");out.rankTwoQueries++}
   }
   eq(total,pc(X)-N(X),"sum deficit");out.portQueries++
  }return cc
 }
 for(let i=0;i<250;i++){
  const p=2+rand(5),m=4+rand(7),E=Array.from({length:m},()=>1+rand((1<<p)-1)),cap=Array.from({length:p},()=>1+rand(3)),full=(1<<m)-1;
  let ranks=new Int8Array(full+1),ind=new Uint8Array(full+1),u=new Int32Array(full+1);ind[0]=1;
  for(let X=1;X<=full;X++){out.originalLabelSubsets++;let b=X&-X;u[X]=u[X^b]|E[31-Math.clz32(b)];let c=0;for(const a of bits(u[X]))c+=cap[31-Math.clz32(a)];
   let best=0,ok=pc(X)<c;for(const y of bits(X)){best=Math.max(best,ranks[X^y]);if(!ind[X^y])ok=false}
   ind[X]=+ok;ranks[X]=ok?pc(X):best
  }
  let F=full,S=0,prev=null,r=X=>ranks[X];
  while(true){let cs=state(F,S,r,E,p,prev);prev=cs.map(x=>x.C);if(!F)break;let bb=bits(F),b=bb[rand(bb.length)];if(ind[S|b]&&rand(2))S|=b;F^=b}
  out.models++
 }
 function graphRank(E,p){return X=>{let par=Array.from({length:p},(_,i)=>i),r=0;function root(x){while(par[x]!==x)x=par[x];return x}for(const b of bits(X)){let [a,c]=bits(E[31-Math.clz32(b)]).map(z=>31-Math.clz32(z));a=root(a);c=root(c);if(a!==c){par[a]=c;r++}}return r}}
 // Theta K_{2,3}: three internally disjoint two-edge paths between 0 and 1.
 let theta=[];for(let i=2;i<5;i++)theta.push(1|(1<<i),2|(1<<i));
 let tc=state(63,0,graphRank(theta,5),theta,5,null);eq(tc.length,1,"theta components");
 out.theta={components:tc.length,terms:tc[0].ts.sort((a,b)=>a[0]-b[0]),negativeFull:tc[0].ts.find(x=>x[0]===31)?.[1]};eq(out.theta.negativeFull,-1,"theta coefficient");
 // Friendship: avoid exponential global atom materialization; certify all port masks.
 for(let k=1;k<=7;k++){
  const p=2*k+1,E=[];for(let i=0;i<k;i++){let a=1<<(2*i+1),b=1<<(2*i+2);E.push(1|a,1|b,a|b)}
  const F=(1<<E.length)-1,r=graphRank(E,p),cs=components(F,r),cc=cs.map(C=>carrier(C,r,E));eq(cs.length,k,"friendship components");let terms=cc.reduce((s,c)=>s+c.ts.length,0);eq(terms,k,"friendship terms");
  for(let W=0;W<1<<p;W++){let X=0,v=0;for(let j=0;j<E.length;j++)if(sub(E[j],W))X|=1<<j;for(const c of cc)for(const [A,w] of c.ts)if(sub(A,W))v+=w;eq(v,pc(X)-r(X),"friendship query")}
  out.friendship.push({k,ports:p,labels:E.length,components:cs.length,terms,globalAtoms:2**k-1,queries:1<<p})
 }
 return out
}
console.log(JSON.stringify(replay(),null,2));
