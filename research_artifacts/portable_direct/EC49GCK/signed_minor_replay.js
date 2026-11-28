function replayMinor(){
 let seed=20261129>>>0;
 const rand=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;seed>>>=0;return seed%n};
 const pc=x=>{let c=0;while(x){x&=x-1;c++}return c}, sub=(x,y)=>(x&y)===x;
 const bits=x=>{let a=[];while(x){let b=x&-x;a.push(b);x^=b}return a};
 function* subsets(m){for(let x=m;;x=(x-1)&m){yield x;if(!x)break}}
 let o={seed:20261129,models:200,originalSubsets:0,initialComponents:0,initialTerms:0,visitedStates:0,childTransitions:0,illegalSelections:0,allLabelQueryChecks:0,canonicalCoefficientChecks:0,termCountChecks:0,removedTerms:0,mergedTerms:0,maxTerms:0,disagreements:0};
 function add(map,A,w){let v=(map.get(A)||0)+w;if(v)map.set(A,v);else map.delete(A)}
 function q(map,X){let v=0;for(const [A,w] of map)if(sub(A,X))v+=w;return v}
 function initial(F,r){
  let B=0;for(const x of bits(F))if(r(B|x)>r(B))B|=x;
  let gs=bits(F);
  for(const x of bits(F^B)){let C=x;for(const y of bits(B))if(r((B^y)|x)===pc(B))C|=y;
   let next=[];for(const G of gs)if(G&C)C|=G;else next.push(G);next.push(C);gs=next}
  o.initialComponents+=gs.length;
  let map=new Map();
  for(const C of gs){let d=pc(C)-r(C);if(!d)continue;const dual=X=>pc(X)-r(C)+r(C^X);
   let flats=new Map();for(const X of subsets(C)){let k=dual(X);if(k>=d)continue;let L=X;for(const b of bits(C^X))if(dual(X|b)===k)L|=b;flats.set(L,k)}
   let weights=[];for(const [L,k] of [...flats].sort((a,b)=>pc(b[0])-pc(a[0]))){let w=d-k;for(const [H,z] of weights)if(sub(L,H))w-=z;weights.push([L,w]);add(map,C^L,w)}
  }o.initialTerms+=map.size;return map
 }
 function child(map,R,D){let v=new Map();for(const [A,w] of map){if(A&D){o.removedTerms++;continue}let K=A&~R;if(v.has(K))o.mergedTerms++;add(v,K,w)}if(v.has(0))throw Error("nonzero empty term");if(v.size>map.size)throw Error("term growth");o.termCountChecks++;return v}
 function check(map,F,S,r){o.maxTerms=Math.max(o.maxTerms,map.size);let coef=new Map();
  for(const X of [...subsets(F)].sort((a,b)=>pc(a)-pc(b))){let v=pc(X)-r(S|X)+pc(S);if(q(map,X)!==v)throw Error("label query");o.allLabelQueryChecks++;
   let c=v;for(const [Y,w] of coef)if(sub(Y,X))c-=w;if(c)coef.set(X,c);
  }
  if(coef.size!==map.size)throw Error("coeff size");for(const [A,w] of coef){if(map.get(A)!==w)throw Error("coeff mismatch");o.canonicalCoefficientChecks++}
 }
 for(let i=0;i<o.models;i++){
  let p=2+rand(5),m=4+rand(7),F=(1<<m)-1,E=Array.from({length:m},()=>1+rand((1<<p)-1)),cap=Array.from({length:p},()=>1+rand(3)),u=new Int32Array(F+1),ranks=new Int8Array(F+1),ind=new Uint8Array(F+1);ind[0]=1;
  for(let X=1;X<=F;X++){o.originalSubsets++;let b=X&-X;u[X]=u[X^b]|E[31-Math.clz32(b)];let c=0;for(const a of bits(u[X]))c+=cap[31-Math.clz32(a)];let best=0,ok=pc(X)<c;for(const y of bits(X)){best=Math.max(best,ranks[X^y]);if(!ind[X^y])ok=false}ind[X]=+ok;ranks[X]=ok?pc(X):best}
  const r=X=>ranks[X];let S=0,map=initial(F,r);
  while(true){o.visitedStates++;check(map,F,S,r);if(!F)break;
   // A randomly chosen nonempty block is fully processed. Test every quantity/label branch.
   let H=0;for(const b of bits(F))if(rand(3)===0)H|=b;if(!H)H=F&-F;
   let legal=[];
   for(const R of subsets(H)){let ok=q(map,R)===0;if(ok!==Boolean(ind[S|R]))throw Error("selection feasibility");if(!ok){o.illegalSelections++;continue}
    let D=H^R,nm=child(map,R,D);o.childTransitions++;check(nm,F^H,S|R,r);legal.push([R,nm])
   }
   let [R,nm]=legal[rand(legal.length)];S|=R;F^=H;map=nm
  }
 }
 return o
}
console.log(JSON.stringify(replayMinor(),null,2));
