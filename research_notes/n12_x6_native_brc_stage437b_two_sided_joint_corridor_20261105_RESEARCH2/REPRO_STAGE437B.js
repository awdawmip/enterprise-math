"use strict";
const D=[1,2,3,4,5,6,-1,-2,-3,-4,-5,-6],A=1,B=-1,C=2;
const ZERO={c:0,w:0,m:0}, ONE={c:1,w:1,m:1};
function coal(a,b){return !a.c?b:!b.c?a:{c:a.c+b.c,w:a.w+b.w,m:Math.max(a.m,b.m)}}
function unit(k){let z=ZERO;for(let i=0;i<k;i++)z=coal(z,ONE);return z}
function V(w){let v=[0,0,0,0,0,0];for(const d of w)v[Math.abs(d)-1]+=Math.sign(d);return v}
function J(w){let h={};for(let i=1;i<w.length;i++){let k=w[i-1]+":"+w[i];h[k]=(h[k]||0)+1}return h}
function normJ(j){return Object.keys(j).sort().map(k=>[k,j[k]])}
function K(p,q){return unit(p.reduce((a,x,i)=>a+(i<q.length&&x===q[i]?1:0),0)).c}
function obs(p,q){return JSON.stringify([p.length,q.length,V(p),V(q),normJ(J(p)),normJ(J(q)),K(p,q)])}
function state(P,Q,pP,rP,pQ,rQ){
 const c=Math.min(P.length-pP,Q.length-pQ);if(c<=0)throw Error("nonempty prefix required");
 const original={P,Q},bud={P:{POP:pP,APPEND:rP},Q:{POP:pQ,APPEND:rQ}};
 let z={c,bud,used:{P:{POP:0,APPEND:0},Q:{POP:0,APPEND:0}},
   N:{P:P.length,Q:Q.length},len:{P:P.length,Q:Q.length},
   ex:{P:[],Q:[]},corr:{P:{},Q:{}},suffix:{P:{},Q:{}},
   v:{P:V(P),Q:V(Q)},j:{P:J(P),Q:J(Q)},k:K(P,Q)};
 for(const s of ["P","Q"]){
   const other=s==="P"?"Q":"P", w=original[s], n=original[other].length,
     r_other=s==="P"?rQ:rP,p=s==="P"?pP:pQ;
   for(let i=c+1;i<=Math.min(w.length,n+r_other);i++)z.corr[s][i]=w[i-1];
   for(let i=w.length-p;i<=w.length;i++)z.suffix[s][i]=w[i-1];
 }
 z.get=(s,i)=>{
   if(i<1||i>z.len[s])throw Error("bad lookup "+s+":"+i);
   if(i>z.N[s])return z.ex[s][i-z.N[s]-1];
   const d=z.corr[s][i]??z.suffix[s][i];
   if(d===undefined)throw Error("lost original direction "+s+":"+i);
   return d;
 };
 z.do=(s,op,d)=>{
   if(z.used[s][op]>=z.bud[s][op])throw Error("operation budget");
   const other=s==="P"?"Q":"P", L=z.len[s];
   if(op==="APPEND"){
     if(!D.includes(d))throw Error("invalid signed axis");
     if(L<z.len[other]&&z.get(other,L+1)===d)z.k++;
     if(L){const edge=z.get(s,L)+":"+d;z.j[s][edge]=(z.j[s][edge]||0)+1}
     z.ex[s].push(d);z.len[s]++;z.v[s][Math.abs(d)-1]+=Math.sign(d);
   }else{
     if(L<=c)throw Error("POP into stable prefix");
     const old=z.get(s,L);
     if(L<=z.len[other]&&z.get(other,L)===old)z.k--;
     if(L>1){const edge=z.get(s,L-1)+":"+old;z.j[s][edge]--;if(!z.j[s][edge])delete z.j[s][edge]}
     if(z.ex[s].length)z.ex[s].pop();else z.N[s]--;
     z.len[s]--;z.v[s][Math.abs(old)-1]-=Math.sign(old);
   }
   z.used[s][op]++;
 };
 z.obs=()=>JSON.stringify([z.len.P,z.len.Q,z.v.P,z.v.Q,normJ(z.j.P),normJ(z.j.Q),z.k]);
 return z;
}
function full(p,q,s,op,d){let v=s==="P"?p:q,v2=op==="APPEND"?v.concat([d]):v.slice(0,-1);return s==="P"?[v2,q]:[p,v2]}
let cases=0,prefixes=0,comparisons=0,max_slots=0;
function test(P,Q,bs,maxDepth=99){
 const [pP,rP,pQ,rQ]=bs, z=state(P,Q,...bs), Btot=bs.reduce((a,b)=>a+b,0);
 const corridor=Object.keys(z.corr.P).length+Object.keys(z.corr.Q).length;
 if(corridor>2*(pP+pQ)+rP+rQ)throw Error("slot bound");
 max_slots=Math.max(max_slots,corridor+Object.keys(z.suffix.P).length+Object.keys(z.suffix.Q).length);
 let todo=[[]];
 while(todo.length){
   let seq=todo.pop(),p=P,q=Q,st=state(P,Q,...bs);
   for(const [s,op,d] of seq){
     [p,q]=full(p,q,s,op,d);st.do(s,op,d);comparisons++;
     if(st.obs()!==obs(p,q))throw Error("observer mismatch: "+JSON.stringify(seq));
   }
   prefixes++;
   if(seq.length>=Math.min(Btot,maxDepth))continue;
   for(const s of ["P","Q"])for(const op of ["POP","APPEND"]){
     if(st.used[s][op]>=st.bud[s][op])continue;
     if(op==="POP")todo.push(seq.concat([[s,op,null]]));
     else for(const d of D)todo.push(seq.concat([[s,op,d]]));
   }
 }
 cases++;
}
test([A,A,B,A],[C,C],[1,0,0,1]);
test([A,B,A,A,A],[C,C,C],[0,1,1,1]);
test([A,B,A,A],[A,A,A],[1,1,1,0]);
test([A,A,B,A,A],[C,C,C,C],[1,0,2,0]);
test([A,B,A,A,A],[C,C],[1,1,0,2],2);
let seed=437;function rnd(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n}
const choices=[[1,1,0,1],[0,1,1,1],[1,0,1,1],[2,0,1,0]];
for(let t=0;t<15;t++){let m=3+rnd(5),n=2+rnd(6),p=Array.from({length:m},()=>D[rnd(12)]),q=Array.from({length:n},()=>D[rnd(12)]);test(p,q,choices[rnd(4)])}
let p=[A,A,A,B,A,A,A],p2=[A,B,A,A,A,A,A],q=[C,C];
if(obs(p,q)!==obs(p2,q)||p.slice(-2).join()!==p2.slice(-2).join())throw Error("invalid witness");
let x=state(p,q,1,1,0,2),y=state(p2,q,1,1,0,2);
for(const z of [x,y]){z.do("Q","APPEND",A);z.do("Q","APPEND",A)}
if(x.k!==1||y.k!==2)throw Error("counterexample");
if(JSON.stringify(unit(3))!==JSON.stringify({c:3,w:3,m:1}))throw Error("positive BRC carrier");
return {marker:"STAGE437B_TWO_SIDED_CORRIDOR_CWM_PASS",cases,
 future_prefixes:prefixes,replayed_step_comparisons:comparisons,
 maximum_original_label_slots_with_suffix_duplicates:max_slots,
 native_signed_append_directions:12,
 counterexample:{P:"AAABAAA",P_prime:"ABAAAAA",Q:"CC",budgets:[1,1,0,2],initial_K:0,
 after_Q_APPEND_A_twice:[x.k,y.k],P_corridor:"AB",P_prime_corridor:"AA"},
 positive_unit_CWM_three_branches:unit(3),
 verification_scope:"exact finite positive BRC unit-weight matching observer; not runtime physics"};
