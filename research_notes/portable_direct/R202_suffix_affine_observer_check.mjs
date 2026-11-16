// R202 exact GF(2) affine suffix descriptor checks; Node.js, no dependencies.
"use strict";
function log2ceil(n){let b=0,v=1;while(v<n){v*=2;b++}return b}
function identity(d){return {pick:Array.from({length:d},(_,i)=>i),c:Array(d).fill(0)}}
function generator(a,L,x,offset){
  if(!Number.isInteger(a)||a<2||a>65535||!Number.isInteger(L)||L<1||L>8||x<0||x>=a)throw Error("invalid bounded-test input");
  const b=log2ceil(a+offset),d=b*L,pick=Array(d).fill(-1),c=Array(d).fill(0);
  for(let slot=0;slot<L-1;slot++)for(let bit=0;bit<b;bit++)
    pick[slot*b+bit]=(slot+1)*b+bit;
  for(let bit=0;bit<b;bit++)c[(L-1)*b+bit]=((x+offset)>>bit)&1;
  return {pick,c};
}
function then(f,g){const d=f.pick.length,pick=[],c=[];
  if(g.pick.length!==d)throw Error("dimension mismatch");
  for(let i=0;i<d;i++){const j=g.pick[i];
    if(j===-1){pick.push(-1);c.push(g.c[i]);}
    else if(f.pick[j]===-1){pick.push(-1);c.push(f.c[j]^g.c[i]);}
    else {pick.push(f.pick[j]);c.push(f.c[j]^g.c[i]);}
  }return {pick,c};
}
function wordAction(a,L,word,offset){
  let f=identity(L*log2ceil(a+offset));
  for(const x of word)f=then(f,generator(a,L,x,offset));
  return f;
}
function sig(f){return f.pick.join(",")+"|"+f.c.join(",")}
function atZero(f){return f.c.join("")}
function rankGF2(vectors,d){const basis=Array(d).fill(0n);let r=0;
  for(let v of vectors){for(let bit=d-1;bit>=0;bit--)if((v>>BigInt(bit))&1n){
    if(basis[bit]===0n){basis[bit]=v;r++;break}v^=basis[bit];
  }}return r;
}
function bitVector(v){return v.reduce((z,x,i)=>z|(BigInt(x)<<BigInt(i)),0n)}
function run(){
  const models=[{a:2,L:2},{a:4,L:2},{a:3,L:2},{a:84,L:2},{a:5,L:1}];
  const results=[];
  for(const {a,L} of models){
    const sets=[[[]],...Array.from({length:L},()=>[])];
    for(let h=1;h<=L;h++){const total=a**h;for(let z=0;z<total;z++){
      let v=z,w=[];for(let j=0;j<h;j++){w.unshift(v%a);v=Math.floor(v/a)}sets[h].push(w);
    }}
    const all=sets.flat(),n=all.length,widths=[];
    for(const offset of [0,1]){
      const actions=new Set(),orbits=new Set();
      for(const w of all){const f=wordAction(a,L,w,offset);
        actions.add(sig(f));orbits.add(atZero(f));}
      if(actions.size!==n)throw Error("unfaithful action:"+a+","+L+","+offset);
      if(offset===1&&orbits.size!==n)throw Error("noninjective orbit:"+a+","+L);
      widths.push({offset,dimension:L*log2ceil(a+offset),action_count:actions.size,zero_orbit_count:orbits.size});
    }
    results.push({a,L,states:n,information_bits:log2ceil(n),widths});
  }
  const a=84,L=2,offset=1,b=log2ceil(a+offset),d=b*L;
  const p0=wordAction(a,L,[0],offset).c,U=[],AU=[];
  const g=generator(a,L,1,offset);
  for(let x=1;x<a;x++){
    const p=wordAction(a,L,[x],offset).c;
    const v=p.map((z,i)=>z^p0[i]);
    U.push(bitVector(v));
    AU.push(bitVector(g.pick.map(j=>j<0?0:v[j])));
  }
  const ranks={U:rankGF2(U,d),A_U:rankGF2(AU,d),sum:rankGF2([...U,...AU],d)};
  if(ranks.U!==7||ranks.A_U!==7||ranks.sum!==14)throw Error("rank certificate failed");
  let associative=0,absorption=0,seed=0x51f15e;
  const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed};
  const randomWord=()=>Array.from({length:rand()%5},()=>rand()%a);
  for(let i=0;i<3000;i++){
    const w=randomWord(),v=randomWord(),z=randomWord();
    const f=wordAction(a,L,w,1),g=wordAction(a,L,v,1),h=wordAction(a,L,z,1);
    if(sig(then(then(f,g),h))!==sig(then(f,then(g,h))))throw Error("assoc failed");
    const concatenated=wordAction(a,L,[...w,...v],1);
    if(sig(then(f,g))!==sig(concatenated))throw Error("concat failed");
    const suffix=[...w,...v].slice(-L);
    if([...w,...v].length>=L&&sig(concatenated)!==sig(wordAction(a,L,suffix,1)))throw Error("suffix absorption failed");
    associative++;absorption++;
  }
  return {status:"PASS",method:"EXACT_GF2_ROW_SELECTOR_DESCRIPTOR",
   models:results,rank_certificate_a84_L2:ranks,
   checks:{associativity_and_concatenation:associative,suffix_absorption:absorption},
   scientific_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34"};
}
if(typeof process!=="undefined"&&process.argv[1]&&process.argv[1].endsWith(".mjs"))
 console.log(JSON.stringify(run(),null,2));
