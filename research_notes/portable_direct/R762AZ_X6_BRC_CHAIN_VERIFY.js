#!/usr/bin/env node
"use strict";
function verifyR762AZ(){
 const fac=[1];for(let n=1;n<=10;n++)fac[n]=fac[n-1]*n;
 const perms=(n)=>{const a=[];function visit(x,remaining){if(!remaining.length){a.push(x);return}for(let j=0;j<remaining.length;j++)visit(x.concat(remaining[j]),remaining.slice(0,j).concat(remaining.slice(j+1)))}visit([],Array.from({length:n},(_,i)=>i));return a};
 const gapData=(m,S)=>{const ss=S.slice().sort((a,b)=>a-b),gaps=[],chains=[];if(!ss.length)return {gaps,chains};for(let i=0;i<ss.length;i++){let start=ss[i],next=ss[(i+1)%ss.length],len=(next-start+m)%m||m;gaps.push(len);chains.push(Array.from({length:len},(_,j)=>(start+j)%m))}return {gaps,chains}};
 const q=(m,g)=>g.length?fac[m]/g.reduce((p,x)=>p*fac[x],1):0;
 const encode=(path,chains)=>{const owner={},indices=new Array(chains.length).fill(0),out=[];for(let i=0;i<chains.length;i++)for(const e of chains[i])owner[e]=i;for(const edge of path){const j=owner[edge];if(chains[j][indices[j]++]!==edge)throw Error("wrong within-chain sequence");out.push(j)}return out};
 const decode=(colored,chains)=>{const indices=new Array(chains.length).fill(0);return colored.map(j=>{if(indices[j]>=chains[j].length)throw Error("too many j");return chains[j][indices[j]++]})};
 const colorWords=(mults)=>{const out=[],counts=mults.slice(),curr=[];function dfs(){if(curr.length===mults.reduce((a,b)=>a+b,0)){out.push(curr.slice());return}for(let j=0;j<counts.length;j++)if(counts[j]){counts[j]--;curr.push(j);dfs();curr.pop();counts[j]++}}dfs();return out};
 const all6=perms(6);let supports=0,paths=0,orbits=0,pairCases=0;
 const profs=[];
 for(let m=2;m<=6;m++){
  let vectors=[];
  for(let mask=1;mask<1<<m;mask++){
    const S=Array.from({length:m},(_,i)=>i).filter(i=>mask>>i&1),{gaps,chains}=gapData(m,S);
    const expected=q(m,gaps),encodings=colorWords(gaps);
    if(encodings.length!==expected)throw Error("multinomial mismatch");
    const seen=new Set();
    for(const colors of encodings){const word=decode(colors,chains);const reparsed=encode(word,chains);
      if(reparsed.join(",")!==colors.join(","))throw Error("non-bijective");
      const bag=new Set(word);
      if(bag.size!==m)throw Error("edge permutation violation");
      const K=Array.from({length:m},(_,i)=>mask>>i&1);
      for(const edge of word){if(!K[edge])throw Error("resource infeasible");K[edge]--;K[(edge+1)%m]++}
      if(K.some((x,i)=>x!==((mask>>i)&1)))throw Error("inventory mismatch");
      seen.add(word.join(","));
      paths++;
    }
    if(seen.size!==expected)throw Error("not an injection");
    supports++;
    vectors.push(gaps.concat(Array(6-gaps.length).fill(0)));
  }
  const sorted=(v)=>v.slice().sort((a,b)=>a-b).join(",");
  const oracle=(v,w)=>all6.some(p=>p.every((dest,i)=>v[i]===w[dest]));
  for(let i=0;i<vectors.length;i++)for(let j=i;j<vectors.length;j++){
   let eq=oracle(vectors[i],vectors[j]);
   if(eq!==(sorted(vectors[i])===sorted(vectors[j])))throw Error("S6 orbit mismatch");
   pairCases++;
  }
 }
 const left=[1,4,5],right=[2,2,6],leftQ=q(10,left),rightQ=q(10,right);
 if(leftQ!==1260||rightQ!==1260||left.slice().sort().join(",")===right.slice().sort().join(","))throw Error("equal-count distinct-orbit witness mismatch");
 const witness1=gapData(4,[0,1]).gaps,witness2=gapData(4,[0,2]).gaps;
 if(q(4,witness1)!==4||q(4,witness2)!==6)throw Error("frame obstruction witness mismatch");
 return {schema:"EM_R762AZ_X6_POSITIVE_BRC_BRIDGE_EVIDENCE_V1",all_assertions:"PASS",scope:"exact combinatorial encoding of conditional token PASS words to established P000 positive-only signed X6 axis-path BRC; NO native TRIADIC_CLOSURE_E event admission",axis_count:6,cycle_m_range:"2..6",positive_supports_tested:supports,constructed_and_inverse_checked_path_pairs:paths,S6_permutations_checked:all6.length,S6_orbit_pair_tests:pairCases,equal_q_notorbit_example:{m:10,h:3,gaps_a:left,gaps_b:right,q_a:leftQ,q_b:rightQ},frame_no_go_example:{m:4,port_support_before:[0,1],port_support_after:[0,2],gap_a:witness1,gap_b:witness2,q_before:4,q_after:6},exact_arithmetic:"integer factorials and explicit bijection and exhaustive finite permutations"};
}
const evidence=verifyR762AZ();
if (typeof process !== "undefined" && require.main===module) console.log(JSON.stringify(evidence,null,2));
module.exports={verifyR762AZ};
