#!/usr/bin/env node
'use strict';
const result = (function verify(){
  const mod=(x,m)=>((x%m)+m)%m;
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const inv=(a,m)=>{for(let i=1;i<m;i++)if(mod(a*i,m)===1)return i;throw Error("inverse")};
  const test=(p,msg)=>{if(!p)throw Error(msg)};
  const F={"00":[3],"01":[0,3,4,"inf"],"10":[2,3,4,"inf"],"11":[2,3]};
  const P=(h,n)=>{
    h=mod(h,10);n=mod(n,10);
    if(h%5===0&&n%5===0)return false;
    const slope=h%5===0?"inf":mod(n*inv(h%5,5),5);
    return F[`${h%2}${n%2}`].includes(slope);
  };
  test(Array.from({length:100},(_,i)=>P(Math.floor(i/10),i%10)).filter(Boolean).length===44,"44-cell source");
  const get=(a,b,m,full)=>{
    let base=null;
    for(let h=0;h<m&&base===null;h++)for(let n=0;n<m;n++){
      if(mod((b-a)*h-a*n+1,m)===0){base=[h,n];break}
    }
    test(base!==null,"primitive affine base");
    const s=new Set();
    for(let t=0;t<m;t++){
      const h=base[0]+a*t,n=base[1]+(b-a)*t;
      if(P(h,n)&&(!full||mod(9*h+10*n,11)!==0))s.add(t);
    }
    return s;
  };
  const xor=(s,t)=>new Set([...s,...t].filter(x=>s.has(x)!==t.has(x)));
  const opt=(s,m)=>{
    const dif=Array.from({length:m},(_,c)=>xor(s,new Set([...s].map(t=>mod(c-t,m)))));
    const D=Math.min(...dif.map(x=>x.size));
    return {D,centers:dif.flatMap((x,c)=>x.size===D?[c]:[]),dif};
  };
  const graph=(s,o,m)=>{
    const edges=[];
    for(const c of o.centers){
      if(o.D===0)continue;
      test(o.D===2,"two-site base mismatch");
      const p=[...o.dif[c]].find(x=>s.has(x)),q=[...o.dif[c]].find(x=>!s.has(x));
      test(p!==undefined&&q!==undefined&&mod(p+q,m)===c,"signed edge");
      edges.push([p,q,c]);
    }
    const adj=new Map();
    for(const [p,q] of edges){
      if(!adj.has(p))adj.set(p,new Set());
      if(!adj.has(q))adj.set(q,new Set());
      adj.get(p).add(q);adj.get(q).add(p);
    }
    const seen=new Set(),sizes=[];
    for(const x of adj.keys())if(!seen.has(x)){
      let q=[x],size=0;seen.add(x);
      while(q.length){
        const p=q.pop();size++;
        for(const y of adj.get(p))if(!seen.has(y)){seen.add(y);q.push(y)}
      }
      sizes.push(size);
    }
    sizes.sort((a,b)=>a-b);
    return {edges,sizes};
  };
  const census={D0:0,D2_N1_P2:0,D2_N2_2P2:0,D2_N4_2P3:0};
  for(let a=0;a<10;a++)for(let b=0;b<10;b++){
    if(gcd(gcd(a,b),10)!==1)continue;
    const s=get(a,b,10,false),o=opt(s,10),g=graph(s,o,10);
    const key=o.D===0?"D0":`D2_N${o.centers.length}_${g.sizes.join(",")==="2"?"P2":g.sizes.join(",")==="2,2"?"2P2":"2P3"}`;
    test(Object.prototype.hasOwnProperty.call(census,key),"unexpected graph "+key);
    census[key]++;
  }
  test(JSON.stringify(census)===JSON.stringify({D0:8,D2_N1_P2:24,D2_N2_2P2:24,D2_N4_2P3:16}),"72-class census");
  const sample={};
  for(const [a,b] of [[1,2],[1,7],[1,10],[5,6],[2,9],[3,11],[7,17],[13,22]]){
    const s10=get(a,b,10,false),o10=opt(s10,10),g10=graph(s10,o10,10);
    const s=get(a,b,110,true),o=opt(s,110);
    const f=(a+b)%11===0?11:10;
    test(o.D===o10.D*f&&o.centers.length===o10.centers.length*(f===11?11:1),`CRT defect ${a}/${b}`);
    const v=new Set([...s].map(x=>x%11));test(v.size===f,"11-factor");
    test([...Array(110).keys()].every(t=>s.has(t)===(s10.has(t%10)&&v.has(t%11))),"CRT product");
    const edges=[];
    for(const c of o.centers){
      if(o.D===0)continue;
      const c10=c%10;
      test(o10.centers.includes(c10),"optimal center mod10");
      if(f===10){const hole=[...Array(11).keys()].find(z=>!v.has(z));test(c%11===(2*hole)%11,"unique mod11 center");}
      for(const t of o.dif[c]){
        test(o10.dif[c10].has(t%10)&&v.has(t%11),"signed difference product");
        if(s.has(t)){const q=mod(c-t,110);test(o.dif[c].has(q)&&!s.has(q),"directed edge");edges.push([t,q]);}
      }
    }
    const unique=new Set(edges.map(e=>e.join(":")));
    test(unique.size===g10.edges.length*(f===10?10:121),"lifted edge count");
    if(f===11)for(const [p,q] of g10.edges){
      for(let u=0;u<11;u++)for(let v2=0;v2<11;v2++){
        const x=[...Array(110).keys()].find(t=>t%10===p&&t%11===u);
        const y=[...Array(110).keys()].find(t=>t%10===q&&t%11===v2);
        test(unique.has(`${x}:${y}`),"complete bipartite edge");
      }
    }
    sample[`${a}/${b}`]={F:f,D10:o10.D,N10:o10.centers.length,D110:o.D,N110:o.centers.length,edges:unique.size,base_components:g10.sizes};
  }
  test(sample["1/10"].edges===121&&sample["1/7"].edges===20,"named witnesses");
  return {status:"ALL PASS",source:"BRC16943 frozen P10 four-fiber decoder + original mod11 linear exclusion",P10_cells:44,primitive_directions:72,census,full_mod110_direction_class_lifts:{one_hole_per_P10_class:110,constant_per_P10_class:10,total:8640},full_110_sample_cases:sample,verification:"exact integer arithmetic; 72 mod10 direction classes; 8 full 110-position masks, all optimal centers and signed mismatches",scope:"Auxiliary certificate model; inherited upstream reduction and global moving Farey problem not re-proved."};
})();
console.log(JSON.stringify(result,null,2));
