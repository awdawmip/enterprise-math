"use strict";
// PREFIX-518 exact integer certificate. Execute: node research_notes/portable_direct/prefix518_four_star_switch_certificate.js
function certificate(){
const S={A:[0,2,5],B:[0,3,4],C:[1,2,4],D:[1,3,5]}, names="ABCD";
const E={"0,1":0,"0,2":2,"0,3":5,"1,2":4,"1,3":3,"2,3":1};
const A=(b,m="assert")=>{if(!b)throw Error(m)},eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),ax=a=>Math.abs(a)-1,
v=a=>Array.from({length:6},(_,i)=>i===ax(a)?Math.sign(a):0),z=()=>Array(6).fill(0),
sum=(a,b)=>a.map((x,i)=>x+b[i]),dif=(a,b)=>a.map((x,i)=>x-b[i]);
const cycle=s=>{const[i,j,k]=S[s].map(x=>x+1);return[i,-k,j,-i,k,-j]};
const nb=(s,a)=>{const c=cycle(s),i=c.indexOf(a);A(i>=0);return[c[(i+5)%6],c[(i+1)%6]]};
const other=(s,a)=>{const x=names.split("").filter(t=>S[t].includes(ax(a)));A(x.length===2&&x.includes(s));return x.find(t=>t!==s)};
const move=([s,p,a])=>{A(nb(s,a).includes(p));const t=other(s,a);return[[s,nb(s,a).find(b=>b!==p),"STAY"],...nb(t,a).map(b=>[t,b,"SWITCH"])]};
const micro=(a,b,bit)=>{const x=v(a),y=v(b);return bit?[y,x.map(z=>-z)]:[x.map(z=>-z),y]};
const mid=(a,b,bit)=>bit?sum(v(a),v(b)):z();
const states=names.split("").flatMap(s=>cycle(s).flatMap(c=>nb(s,c).map(p=>[s,p,c])));A(states.length===48);
const p4=x=>x.length?x.flatMap((a,i)=>p4(x.filter((_,j)=>j!==i)).map(t=>[a,...t])):[[]];
const perms=p4([0,1,2,3]);A(perms.length===24);
const edgePerm=q=>{let p=Array(6).fill(-1);for(const [k,i] of Object.entries(E)){const[a,b]=k.split(",").map(Number);p[i]=E[[q[a],q[b]].sort((x,y)=>x-y).join(",")]}A(eq([...p].sort((x,y)=>x-y),[0,1,2,3,4,5]));return p};
const phase=(a,p)=>Math.sign(a)*(p[ax(a)]+1),tr=(w,p)=>{let out=z();for(let i=0;i<6;i++)out[p[i]]=w[i];return out};
const wedge=(u,v)=>{const x=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)x.push(u[i]*v[j]-u[j]*v[i]);return x};
const disp=w=>w.reduce((a,b)=>sum(a,b),z()),area=w=>{let y=z(),a=Array(15).fill(0);for(const s of w){a=sum(a,wedge(y,s));y=sum(y,s)}return a};
const pairs=w=>{const y=disp(w);return y.map((t,i)=>(w.reduce((q,x)=>q+Math.abs(x[i]),0)-Math.abs(t))/2)};
const cross=(u,w)=>{const y=disp(w);return disp(u).map((x,i)=>(Math.abs(x)+Math.abs(y[i])-Math.abs(x+y[i]))/2)};
let single=0,syms=0,hs=0;
for(const state of states){
 const [s,p,a]=state,m=move(state);A(m.length===3);A(new Set(m.map(x=>x[1])).size===3);
 const out=new Set();for(const[t,b,k]of m)for(const bit of[0,1]){
  const w=micro(a,b,bit);A(eq(sum(v(a),disp(w)),v(b)));
  A(eq(sum(v(a),w[0]),mid(a,b,bit)));
  out.add(JSON.stringify([b,mid(a,b,bit)]));single++;
 }
 A(out.size===6);
}
for(const q of perms){const p=edgePerm(q);for(const state of states){
 const[s,prev,cur]=state,T=[names[q[names.indexOf(s)]],phase(prev,p),phase(cur,p)];
 A(states.some(s=>eq(s,T)));
 const target=new Set(move(T).map(x=>JSON.stringify(x)));
 for(const[t,nxt,kind]of move(state)){
  A(target.has(JSON.stringify([names[q[names.indexOf(t)]],phase(nxt,p),kind])));
  for(const bit of[0,1]){
   A(eq(micro(phase(cur,p),phase(nxt,p),bit),micro(cur,nxt,bit).map(w=>tr(w,p))));
   A(eq(mid(phase(cur,p),phase(nxt,p),bit),tr(mid(cur,nxt,bit),p)));
   syms++;
  }
 }
}}
for(const state of states)for(let h=0;h<216;h++){
 let[s,prev,cur]=state,first=cur,word=[],M=[],num=h;
 for(let k=0;k<3;k++){
  const choice=num%6;num=Math.floor(num/6);
  const[t,b]=move([s,prev,cur])[Math.floor(choice/2)],bit=choice%2;
  word.push(...micro(cur,b,bit));M.push(mid(cur,b,bit));s=t;prev=cur;cur=b;
 }
 let offset=z(),observed=[];
 for(let k=0;k<3;k++){offset=sum(offset,word[2*k]);observed.push(sum(v(first),offset));offset=sum(offset,word[2*k+1])}
 A(eq(observed,M),"intermediate cell");A(eq(sum(v(first),offset),v(cur)),"endpoint");
 const u=word.slice(0,2),w=word.slice(2);
 A(eq(area(word),sum(sum(area(u),area(w)),wedge(disp(u),disp(w)))),"area");
 A(eq(pairs(word),sum(sum(pairs(u),pairs(w)),cross(u,w))),"BRC");
 const L=new Set([JSON.stringify(dif(M[0],v(first)))]),R=M.slice(1).map(m=>dif(m,sum(v(first),disp(u))));
 for(const r of R)L.add(JSON.stringify(sum(disp(u),r)));
 const full=new Set(M.map(m=>JSON.stringify(dif(m,v(first)))));A(eq([...L].sort(),[...full].sort()),"U");
 hs++;
}
const q=[2,3,0,1],p=edgePerm(q);
A(p[0]===1);
const w=[v(1),v(-1)],transformed=w.map(x=>tr(x,p)),col=x=>[x[1]+2*x[3]+x[4],x[2]+x[4]];
A(eq(col(pairs(w)),[0,0])&&eq(col(pairs(transformed)),[1,0]),"fixed-color counterexample");
return {status:"ALL_CHECKS_PASS",arithmetic:"exact integers",states:states.length,phase_successors:3,shortest_labeled_microtraces_per_state:6,microtraces_checked:single,S4_automorphisms:perms.length,covariant_microtraces_checked:syms,three_step_labeled_histories_checked:hs,fixed_color_counterexample:{word:"(+L1,-L1)",V_W_before:[0,0],V_W_after_permuting_L1_to_L2:[1,0]},scope:"declared one-pivot four-STAR switching candidate"};
}
console.log(JSON.stringify(certificate(),null,2));
