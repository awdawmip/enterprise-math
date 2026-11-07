"use strict";
// Stage497-B portable JavaScript exact finite-observer verifier.
// Node: append console.log(JSON.stringify(run(),null,2)) to execute.
function run(){
const ABC="ABC", LETTERS="ABCDEFGHIJKL";
function F(w){
 let d=[0,0,0,0,0,0], e=Array(144).fill(0);
 for(let i=0;i<w.length;i++){let j=LETTERS.indexOf(w[i]);if(j<0)throw Error("invalid token");d[j%6]+=j<6?1:-1;if(i){let k=LETTERS.indexOf(w[i-1]);e[k*12+j]++}}
 return JSON.stringify([d,e]);
}
function op(w,k){
 if(k==="POP")return w? w.slice(0,-1):null;
 if(k==="SET_END_MINUS_2_TO_C")return w.length>=3?w.slice(0,w.length-3)+"C"+w.slice(w.length-2):null;
 throw Error(k);
}
let operations=["POP","SET_END_MINUS_2_TO_C"];
function shortest(a,b,cap){
 if(F(a)!==F(b))throw Error("not same F");
 let q=[[a,b,[]]],seen=new Set([a+"|"+b]),transitions=0;
 for(let i=0;i<q.length;i++){
  let [x,y,t]=q[i];if(t.length>=cap)continue;
  for(let k of operations){let xx=op(x,k),yy=op(y,k);if(xx===null||yy===null)continue;
   transitions++;let tr=t.concat(k);
   if(F(xx)!==F(yy))return {depth:tr.length,trace:tr,final_pair:[xx,yy],pairs_seen:seen.size,transitions};
   let key=xx+"|"+yy;
   if(!seen.has(key)){seen.add(key);q.push([xx,yy,tr]);}
  }
 }
 return {depth:null,pairs_seen:seen.size,transitions};
}
let ladder=[];
for(let s=2;s<=7;s++){
 let x="AABA"+"A".repeat(s),y="ABAA"+"A".repeat(s);
 let z=shortest(x,y,s+2);
 if(z.depth!==s-1)throw Error("wrong distinguishing depth");
 ladder.push({suffix_length:s,word_length:x.length,...z});
}
let groups=new Map(),words=0;
for(let n=1;n<=5;n++){
 for(let i=0;i<3**n;i++){
  let k=i,w="";
  for(let j=0;j<n;j++){w=ABC[k%3]+w;k=Math.floor(k/3)}
  words++;let key=n+"|"+F(w);
  if(!groups.has(key))groups.set(key,[]);
  groups.get(key).push(w);
 }
}
let pairs=[];
for(let a of groups.values())for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)pairs.push([a[i],a[j]]);
function nextOuter(p,s){
 let out=[["PREPEND_C","C"+p,s],["APPEND_B",p,s+"B"],["INSERT_LEFT_A",p+"A",s],["INSERT_RIGHT_C",p,"C"+s]];
 if(p){out.push(["DELETE_FIRST_PUBLIC",p.slice(1),s],["SET_FIRST_PUBLIC_B","B"+p.slice(1),s]);}
 if(s){out.push(["POP_PUBLIC",p,s.slice(0,-1)],["SET_LAST_PUBLIC_C",p,s.slice(0,-1)+"C"]);}
 return out;
}
let contexts=0,states=0,transitions=0;
for(let [u,v] of pairs)for(let p of ["","A","B","C"])for(let s of ["","A","B","C"]){
 contexts++;
 let queue=[[p,s,0]],seen=new Set([JSON.stringify(queue[0])]);
 for(let i=0;i<queue.length;i++){
  let [pp,ss,h]=queue[i];
  states++;if(F(pp+u+ss)!==F(pp+v+ss))throw Error("guarded quotient failed");
  if(h===3)continue;
  for(let [action,p2,s2] of nextOuter(pp,ss)){
   transitions++;if(F(p2+u+s2)!==F(p2+v+s2))throw Error("guarded edit failure "+action);
   let key=JSON.stringify([p2,s2,h+1]);
   if(!seen.has(key)){seen.add(key);queue.push([p2,s2,h+1]);}
  }
 }
}
if(words!==363||pairs.length!==69||contexts!==1104)throw Error("coverage mismatch");
return {model:"six_signed_components_and_all_144_ordered_edges",word_count:words,
 equal_F_pairs:pairs.length,public_contexts:contexts,guarded_state_checks:states,
 guarded_transitions:transitions,max_guarded_depth:3,
 ladder,claim:"exhaustive declared finite checks, full general horizon depth is separately proved"};
}
if (typeof module!=='undefined' && require.main===module)console.log(JSON.stringify(run(),null,2));
