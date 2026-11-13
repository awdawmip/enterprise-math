// R693 derives exact S3 spectral BRC invariants from the verified R692C E* source.
// Upstream commit: 3dacca5010104893d96301af4d61608d5a5a0879; blob: 0c6d51f99eac5903a30770c8c393c972a68d93ad
const R692_MASK_RESULT = (function R692MaskExact(){
  "use strict";
  const n={
    0:[{"012":6,"021":9},{"012":6,"021":6,"120":3},{"012":6,"021":3,"201":6},{"012":6,"120":3,"201":6}],
    1:[{"012":6,"120":6,"201":3},{"012":9,"120":6},{"012":12,"201":3},{"012":15}],
    2:[{"012":15},{"012":12,"021":3},{"012":9,"021":6},{"012":6,"021":9}]
  };
  function assert(ok,msg){if(!ok)throw Error(msg);}
  function mul(g,p){return [...p].map(i=>g[+i]).join("");}
  function gcd(x,y){while(y){[x,y]=[y,x%y]}return x;}
  function reduce(x,y){let d=gcd(x,y);return x/d+"/"+y/d;}
  const cases=[],classifications=[];
  for(let a=0;a<3;a++){
    let signatures=[];
    for(let mask=1;mask<16;mask++){
      let count={},pop=0;
      for(let j=0;j<4;j++)if(mask&(1<<j)){
        pop++;
        for(let [g,w] of Object.entries(n[a][j]))count[g]=(count[g]||0)+w;
      }
      let D=15*pop;
      assert(Object.values(count).reduce((u,v)=>u+v,0)===D,"kernel mass");
      let v={"012":1},p=["1/1"];
      for(let k=1;k<=6;k++){
        let w={};
        for(let [s,u] of Object.entries(v))for(let [g,mass] of Object.entries(count)){
          let dest=mul(g,s);w[dest]=(w[dest]||0)+u*mass;
        }
        assert(Object.values(w).reduce((u,x)=>u+x,0)===D**k,"convolution mass");
        v=w;
        p.push(reduce(v["012"]||0,D**k));
      }
      cases.push({root_phase_a:a,allowed_direction_mask:mask,denominator_per_macro:D,group_counts:count,return_probabilities_k0_to_k6:p});
      signatures.push({mask,sequence:p.slice(1)});
    }
    let map=new Map();
    for(let s of signatures){
      const key=s.sequence.join("|");
      if(!map.has(key))map.set(key,[]);
      map.get(key).push(s.mask);
    }
    let expected=(a===2?9:12);
    assert(map.size===expected,"future class count");
    let horizons=[];
    for(let h=1;h<=6;h++){
      horizons.push(new Set(signatures.map(s=>s.sequence.slice(0,h).join("|"))).size);
    }
    assert(horizons.join(",")===[[1,11,12,12,12,12],[9,12,12,12,12,12],[9,9,9,9,9,9]][a].join(","),"horizon counts");
    let multiples=[...map.values()].filter(x=>x.length>1).sort((x,y)=>x[0]-y[0]);
    let expectMult=[[[2,5],[6,9,15]],[[4,10],[6,9,15]],[[2,5,7],[4,10,14],[6,9,15]]][a];
    assert(JSON.stringify(multiples)===JSON.stringify(expectMult),"class mask membership");
    classifications.push({root_phase_a:a,return_observer_future_equivalence_classes:[...map.values()].sort((x,y)=>x[0]-y[0]),
      non_singleton_classes:multiples,class_count:map.size,distinct_class_counts_by_horizon_k1_to_k6:horizons,
      least_complete_horizon:horizons.indexOf(map.size)+1});
  }
  const a0m2=cases.find(x=>x.root_phase_a===0&&x.allowed_direction_mask===2);
  const a0m5=cases.find(x=>x.root_phase_a===0&&x.allowed_direction_mask===5);
  assert(JSON.stringify(a0m2.group_counts)!==JSON.stringify(a0m5.group_counts),"full group distributions distinct");
  assert(JSON.stringify(a0m2.return_probabilities_k0_to_k6)===JSON.stringify(a0m5.return_probabilities_k0_to_k6),"return traces same");
  return {status:"ALL_EXACT_ASSERTIONS_PASS",model:"frozen R691 E* X6 group kernels, persistent nonempty allowed-direction subset M with equal mass for 15*|M| labeled square paths",numeric_semantics:"integers exact; max denominator^6 = 60^6 < 2^53",enumerated_mask_models:45,cases,classifications,
    explicit_full_group_lossy_pair:"a=0, masks 2 and 5: distributions differ by conjugation by tau (c vs c^2), but all return probabilities coincide",limits:"author E* candidate; not native V29/Link/Port permitted-mask dynamics"};
})();

// R693 extension over unchanged frozen R692C source above.
// Integer formula 6*C_k=D^k+S^k+2H_k, H0=2,H1=T,H(k+2)=T H(k+1)-Delta H(k).
const R693_INTEGER_RESULT=(function(){
"use strict";
const G=["012","021","102","120","201","210"];
function assert(x,s){if(!x)throw Error(s);}
function mul(a,b){return [...b].map(j=>a[+j]).join("");}
function sign(g){let n=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)n+=g[i]>g[j]?1:0;return n%2?-1n:1n;}
function std(g){
 function col(i){const v=[0n,0n,0n];v[+g[i]]++;v[+g[2]]--;return [v[0],v[1]];}
 const a=col(0),b=col(1);return [[a[0],b[0]],[a[1],b[1]]];
}
function mm(a,b){return [[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],
 [a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]];}
for(const g of G)for(const h of G){
 const a=std(mul(g,h)),b=mm(std(g),std(h));
 assert(a.every((row,i)=>row.every((x,j)=>x===b[i][j])),"representation multiplication");
}
function gcd(a,b){a=a<0n?-a:a;while(b!==0n){let t=a%b;a=b;b=t;}return a;}
function frac(a,b){const d=gcd(a,b);return String(a/d)+"/"+String(b/d);}
const rows=[],classes=[];
for(const src of R692_MASK_RESULT.cases){
 const counts=Object.fromEntries(Object.entries(src.group_counts).map(([g,x])=>[g,BigInt(x)]));
 const D=BigInt(src.denominator_per_macro),a=src.root_phase_a,mask=src.allowed_direction_mask;
 let S=0n,M=[[0n,0n],[0n,0n]];
 for(const [g,c] of Object.entries(counts)){
  S+=c*sign(g);const A=std(g);
  for(let i=0;i<2;i++)for(let j=0;j<2;j++)M[i][j]+=c*A[i][j];
 }
 const T=M[0][0]+M[1][1],Delta=M[0][0]*M[1][1]-M[0][1]*M[1][0];
 let distribution={"012":1n},powD=1n,h0=2n,h1=T,c20;
 for(let k=0;k<=20;k++){
  if(k>0){
   const nxt={};
   for(const [g,n] of Object.entries(distribution))for(const [h,w] of Object.entries(counts)){
    const q=mul(g,h);nxt[q]=(nxt[q]||0n)+n*w;
   }
   distribution=nxt;powD*=D;
  }
  let H;
  if(k===0)H=2n;
  else if(k===1)H=T;
  else {H=T*h1-Delta*h0;h0=h1;h1=H;}
  const C=distribution["012"]||0n;
  assert(Object.values(distribution).reduce((u,v)=>u+v,0n)===powD,"native mass");
  assert(6n*C===powD+S**BigInt(k)+2n*H,"integer S3 identity a="+a+" mask="+mask+" k="+k);
  if(k<=6)assert(frac(C,powD)===src.return_probabilities_k0_to_k6[k],"R692C matching");
  if(k===20)c20=frac(C,powD);
 }
 if(a===1)assert(S===D,"A3 support");
 if(a===2)assert(T===D+S&&Delta===D*S,"C2 support");
 rows.push({a,mask,D:String(D),S:String(S),T:String(T),Delta:String(Delta),
  invariant:[frac(S,D),frac(T,D),frac(Delta,D*D)],return_k20:c20});
}
for(let a=0;a<3;a++){
 const x=rows.filter(v=>v.a===a),mp=new Map();
 for(const v of x){let key=v.invariant.join("|");if(!mp.has(key))mp.set(key,[]);mp.get(key).push(v.mask);}
 const grp=[...mp.values()].sort((u,v)=>u[0]-v[0]);
 assert(JSON.stringify(grp)===JSON.stringify(R692_MASK_RESULT.classifications[a].return_observer_future_equivalence_classes),"full-time partition");
 classes.push({a,count:mp.size,classes:grp});
}
return {status:"R693_ALL_INTEGER_ASSERTIONS_PASS",source_git_blob:"0c6d51f99eac5903a30770c8c393c972a68d93ad",
 models:45,representation_law_checks:36,exact_convolution_spectral_equalities:945,
 algebraic_formula:"6 C_k = D^k+S^k+2 H_k; H_0=2; H_1=T; H_(k+2)=T H_(k+1)-Delta H_k",
 classes,rows};
})();

console.log(JSON.stringify(R693_INTEGER_RESULT,null,2));
