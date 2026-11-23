#!/usr/bin/env node
"use strict";
function verify() {
 "use strict";
 const mod=(x,m)=>((x%m)+m)%m;
 const gcd=(a,b)=>{while(b){let t=a%b;a=b;b=t;}return a;};
 const inv=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error("inverse:"+a+","+m);};
 const check=(b,s)=>{if(!b)throw Error(s);};
 const slopes={"0,0":[3],"0,1":[0,3,4,5],"1,0":[2,3,4,5],"1,1":[2,3]};
 function P(h,n){
  h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
  const s=h%5===0?5:mod(n*inv(h%5,5),5);
  return slopes[`${h%2},${n%2}`].includes(s);
 }
 const reps=new Map();
 for(let a=0;a<10;a++)for(let c=0;c<10;c++){
  if(gcd(gcd(a,c),10)!==1)continue;
  let xy=null;for(let x=0;x<10&&xy===null;x++)for(let y=0;y<10;y++)if(mod(c*x-a*y+1,10)===0){xy=[x,y];break;}
  check(xy!==null,"missing representative");const [x,y]=xy;
  let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
  reps.set(`${a},${c}`,{x,y,u});
 }
 check(reps.size===72&&new Set([...reps.values()].map(r=>r.u)).size===50,"frozen 50 masks");
 function normalize(a,c){
  const b=a+c,e=inv(a,b),h0=(a*e-1)/b,n0=e-h0,r=reps.get(`${a%10},${c%10}`);
  check(Number.isInteger(h0)&&r,"determinant-or-direction");
  let t0=-1;for(let t=0;t<10;t++)if(mod(h0+a*t-r.x,10)===0&&mod(n0+c*t-r.y,10)===0){t0=t;break;}
  check(t0>=0,"rephasing");
  const L0=9*(h0+a*t0)+10*(n0+c*t0),L1=9*a+10*c;
  const hole=mod(L1,11)===0?null:mod(-L0*inv(mod(L1,11),11),11);
  if(hole===null)check(mod(L0,11)!==0,"linear-form-degenerate");
  return {u:r.u,hole,a,b,c,t0,h0,n0};
 }
 const states=new Map(),key=s=>`${s.u}/${s.hole===null?"full":s.hole}`;
 for(let b=2;b<=139;b++)for(let a=1;a<b;a++){
  if(gcd(a,b)!==1)continue;
  const s=normalize(a,b-a);if(!states.has(key(s)))states.set(key(s),s);
 }
 check(states.size===600,"600-state surjection");const ss=[...states.values()];
 function spectrum(s){
  const A=Array.from({length:10},(_,i)=>(s.u>>i)&1);
  const V=Array.from({length:11},(_,i)=>Number(s.hole!==i));
  const Acount=A.reduce((s,x)=>s+x,0),Vcount=V.reduce((s,x)=>s+x,0);
  const av=Array.from({length:10},(_,t)=>A.reduce((z,x,i)=>z+x*A[mod(t-i,10)],0));
  const vv=Array.from({length:11},(_,t)=>V.reduce((z,x,i)=>z+x*V[mod(t-i,11)],0));
  let out=[];for(let i=0;i<10;i++)for(let j=0;j<11;j++)out.push(2*(Acount*Vcount-av[i]*vv[j]));
  return out.join(",");
 }
 const fibers=new Map();
 for(const s of ss){const k=spectrum(s);if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(s);}
 const fs=[...fibers.values()];
 check(fs.length===478&&fs.filter(f=>f.length===1).length===356&&fs.filter(f=>f.length===2).length===122&&fs.every(f=>f.length<=2),"spectra census");
 const pairs=fs.filter(f=>f.length===2).map(([a,b])=>{
  check(a.hole===b.hole,"factor mismatch");
  return {u0:a.u,u1:b.u,hole:a.hole,support:a.u^b.u,onset:Math.max(a.b,b.b)};
 });
 const mask=rr=>rr.reduce((v,r)=>v|(1<<r),0);
 const A=mask([1,4,6,9]),B=mask([2,7]),C=mask([3,8]),D=mask([1,2,6,7]),E=mask([2,4,7,9]),F=mask([3,4,8,9]);
 const group=(m,h)=>pairs.filter(p=>p.support===m&&p.onset<=h);
 const holes=(m,h)=>new Set(group(m,h).map(p=>p.hole).filter(x=>x!==null));
 check(group(F,13).length===0&&group(F,14).length>0&&group(D,15).length>0&&((F&D)===0),"early heights 14/15");
 check([C,A,D,E].every(m=>group(m,17).length>0)&&(C&A)===0&&(C&D)===0&&(C&E)===0&&(A&D&E)===0,"3-probe obstruction at B=17");
 for(const [name,m,h] of [["A",A,52],["B",B,58],["C",C,64]])
  check(holes(m,h-1).size<11&&holes(m,h).size===11,"11-hole threshold "+name);
 const plans={
  0:[],
  1:[[9,10]],
  2:[[7,9],[8,10]],
  3:[[7,6],[8,6],[9,9]],
  4:[[7,6],[8,0],[9,8],[9,9]],
  5:[[7,4],[7,5],[8,0],[9,0],[9,1]],
  6:[[1,0],[1,1],[2,0],[2,1],[3,0],[3,1]]
 };
 const minimum=h=>h<=13?0:h===14?1:h<=16?2:h<=51?3:h<=57?4:h<=63?5:6;
 let directChecks=0,layoutChecks=0;
 for(const s of ss)for(let t=0;t<110;t++){
  const h=s.h0+s.a*(s.t0+t),n=s.n0+s.c*(s.t0+t);
  const direct=Number(P(h,n)&&mod(9*h+10*n,11)!==0);
  const factored=Number(Boolean(s.u&(1<<(t%10)))&&(s.hole===null||t%11!==s.hole));
  check(direct===factored,"direct C11 trace mismatch");directChecks++;
 }
 const census=[];
 for(let H=2;H<=139;H++){
  const sites=plans[minimum(H)];
  for(const p of pairs)if(p.onset<=H){
   check(sites.some(([j,v])=>(p.support&(1<<j))!==0&&(p.hole===null||v!==p.hole)),`layout failure B=${H}`);
   layoutChecks++;
  }
  census.push({B:H,states:ss.filter(s=>s.b<=H).length,doubletons:pairs.filter(p=>p.onset<=H).length,min_sites:minimum(H)});
 }
 check(census[136].states===599&&census[137].states===600,"sharp state saturation at 139");
 check(Math.max(...pairs.map(p=>p.onset))===109,"ambiguity saturation at 109");
 const support_summary=[...new Set(pairs.map(p=>p.support))].sort((a,b)=>a-b).map(m=>{
  const p=pairs.filter(x=>x.support===m);
  return {rows:Array.from({length:10},(_,i)=>i).filter(i=>(m>>i)&1),doubletons:p.length,first_B:Math.min(...p.map(x=>x.onset)),last_B:Math.max(...p.map(x=>x.onset))};
 });
 return {
  schema:"EM_EC49FXV_HEIGHT_BOUNDED_FAREY_EXACT_CERTIFICATE_V1",
  result:"ALL_PASS",frozen_input:"BRC16943",
  model:"positive reduced anchor a/b in (0,1), b<=B; normalized left determinant-one C11, full indexed reflection spectrum known, fixed Boolean sites chosen before spectrum; minimum Hamming separation 1",
  exact_theorem:[{range:"2..13",N:0},{range:"14",N:1},{range:"15..16",N:2},{range:"17..51",N:3},{range:"52..57",N:4},{range:"58..63",N:5},{range:"64..infinity",N:6}],
  optimal_layouts:plans,
  primitive_directions:72,ten_bit_supports:50,full_product_states:600,indexed_spectra:478,singleton_fibers:356,doubleton_fibers:122,
  first_ambiguous_height:14,all_doubletons_present_by_height:109,all_product_states_present_by_height:139,
  eleven_hole_completion_B:{A:52,B:58,C:64},
  equality_supports:support_summary,
  direct_original_C11_bit_checks:directChecks,
  all_height_doubleton_layout_checks:layoutChecks,
  all_height_census:census,
  first_appearance_witnesses:ss.map(s=>({u:s.u,hole:s.hole,a:s.a,b:s.b,t0:s.t0})).sort((a,b)=>a.u-b.u||((a.hole??-1)-(b.hole??-1))),
  doubleton_constraints:pairs.sort((a,b)=>a.onset-b.onset||a.support-b.support||a.u0-b.u0),
  scope_note:"Finite exact auxiliary observer theorem only; no new native P000 X6 dynamics claim",
  independent_review:"NOT_REVIEWED"
 };
}
process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
