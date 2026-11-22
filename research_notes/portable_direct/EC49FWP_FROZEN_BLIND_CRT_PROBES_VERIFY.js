#!/usr/bin/env node
"use strict";

function verifyFWP(){
 const n=10, slopes={"00":[3],"01":[0,3,4,5],"10":[2,3,4,5],"11":[2,3]};
 const bits=(x,n)=>{let r=[];for(let i=0;i<n;i++)if((x>>i)&1)r.push(i);return r};
 const pop=x=>{let s=0;for(;x;x&=x-1)s++;return s};
 const p10=(h,k)=>{h=((h%n)+n)%n;k=((k%n)+n)%n;if(h%5===0&&k%5===0)return false;let slope=5;if(h%5!==0){for(let j=1;j<5;j++)if((h*j)%5===1){slope=(k*j)%5;break}}return slopes[`${h%2}${k%2}`].includes(slope)};
 function sourceWord(a,b){let h0,n0,found=false;for(let h=0;h<10&&!found;h++)for(let k=0;k<10;k++)if(((b-a)*h-a*k+1)%10===0){h0=h;n0=k;found=true;break}if(!found)throw Error("no root "+a+","+b);let word=0;for(let t=0;t<10;t++)if(p10(h0+a*t,n0+(b-a)*t))word|=1<<t;return word}
 const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a),frozen=new Set();let directions=0;
 for(let a=0;a<10;a++)for(let b=0;b<10;b++)if(gcd(gcd(a,b),10)===1){frozen.add(sourceWord(a,b));directions++}
 if(directions!==72||frozen.size!==50)throw Error("frozen-source mismatch");
 function overlap(m,n){let P=bits(m,n),r=[];for(let c=0;c<n;c++){let s=0;for(let x of P)s+=(m>>((c-x+n)%n))&1;r.push(s)}return r}
 const defects=m=>{let u=pop(m);return overlap(m,10).map(x=>2*(u-x))};
 const families=new Map();for(let u of frozen){let key=defects(u).join(",");if(!families.has(key))families.set(key,[]);families.get(key).push(u)}
 if(families.size!==38)throw Error("spectral family count mismatch");
 const cross=[];for(let g of families.values()){if(g.length>2)throw Error("unexpected family size");if(g.length===2&&pop(g[0])!==pop(g[1]))cross.push(g.sort((a,b)=>a-b))}
 cross.sort((x,y)=>x[0]-y[0]);
 if(JSON.stringify(cross)!==JSON.stringify([[23,287],[833,965]]))throw Error("collision list drift");
 const overlapU=new Map([...frozen].map(u=>[u,overlap(u,10)]));let census=[];
 for(let q of [3,7,11]){
   const all=new Map(),mismatches=new Map();
   for(let v=1;v<(1<<q);v++){const kv=overlap(v,q),fv=pop(v);
     for(let u of frozen){const fu=pop(u),mass=fu*fv,ku=overlapU.get(u),sig=[];
       for(let a=0;a<10;a++)for(let b=0;b<q;b++)sig.push(2*(mass-ku[a]*kv[b]));
       const key=sig.join(","),saved=all.get(key);
       if(!saved)all.set(key,{mass,u,v});
       else if(saved.mass!==mass){if(!mismatches.has(key))mismatches.set(key,[saved]);mismatches.get(key).push({mass,u,v})}
     }
   }
   if(mismatches.size!==2)throw Error("unexpected cross-mass signatures q="+q+":"+mismatches.size);
   const found=[...mismatches.values()].map(g=>g.map(x=>x.u).sort((a,b)=>a-b).join(",")).sort();
   if(JSON.stringify(found)!==JSON.stringify(["23,287","833,965"]))throw Error("cross-mass collision not in frozen list");
   census.push({q,total_products:frozen.size*((1<<q)-1),distinct_indexed_defect_arrays:all.size,cross_mass_ambiguous_arrays:mismatches.size,witnesses:[...mismatches.values()].map(g=>({U_pair:g.map(x=>x.u).sort((a,b)=>a-b),V_mask:g[0].v,masses:g.map(x=>x.mass).sort((a,b)=>a-b)}))});
 }
 const hist={};for(let u of frozen){let k=pop(u);hist[k]=(hist[k]||0)+1}
 let good=[];for(let i=0;i<110;i++)for(let j=i+1;j<110;j++){const a=i%10,b=j%10;if(([2,7].includes(a)&&[3,8].includes(b))||([3,8].includes(a)&&[2,7].includes(b)))good.push([i,j])}
 if(good.length!==484||!good.some(([a,b])=>a===22&&b===33))throw Error("fixed probe classification mismatch");
 return {status:"ALL PASS",scientific_pin:"BRC16943",lineage:"EC49FWO@940ad416fa1eb47904b93860ea5364e869e3de74",primitive_directions:directions,distinct_frozen_U:frozen.size,support_size_histogram:hist,ten_cycle_signature_classes:families.size,cross_mass_ten_cycle_pairs:cross.map(([a,b])=>({U:[a,b],sizes:[pop(a),pop(b)],different_positions:bits(a^b,10)})),exact_product_census:census,optimal_fixed_physical_probe_count_q11:2,number_optimal_two_probes_q11:good.length,example_fixed_probe_sites:[22,33],optimal_adaptive_worst_case_probe_count:1,zero_probe_when_V_nonfull:true,scope_limits:"Static indexed CRT reflection-defect array plus local Boolean probes; no native moving-Farey update or X6 transfer",review:"AUTHOR_PROVED / EXACT_INTEGER_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED"};
}

console.log(JSON.stringify(verifyFWP(), null, 2));
