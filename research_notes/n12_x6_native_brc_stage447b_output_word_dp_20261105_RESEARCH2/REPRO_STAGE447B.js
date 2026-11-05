// Stage447-B exact self-contained checker. Node.js with BigInt. No dependencies.
// Run: node REPRO_STAGE447B.js
function main(){
 const fail=(p,m)=>{if(!p)throw Error(m)}, pack=x=>x.join(","), unpack=k=>k.split(",").map(Number);
 function legal(n,k){
  const out=[];function rec(i,last,num,w){if(num>k)return;if(i===n){if(num===k)out.push(w);return;}
   rec(i+1,0,num,w+"A");if(i>0&&i<n-1&&!last)rec(i+1,1,num+1,w+"B");
  }rec(0,0,0,"");return out;
 }
 function prefix(m,kp,kq,d){
  let cur=new Map([["0,0,0,0,0",1n]]);
  for(let i=1;i<=m;i++){
   const next=new Map();
   for(const [id,c] of cur){const [a,b,h,u,v]=unpack(id);
    for(let s=0;s<2;s++)for(let t=0;t<2;t++){
     if(s&&(i===1||i===m||u)||t&&(i===1||v))continue;
     if(a+s>kp||b+t>kq||h+(s!==t)>d)continue;
     const z=pack([a+s,b+t,h+(s!==t),s,t]);next.set(z,(next.get(z)||0n)+c);
    }
   }cur=next;
  }
  const T=new Map();for(const [id,c] of cur){const [a,b,h,u,v]=unpack(id);
   if(a===kp&&h===d&&u===0){const z=pack([b,v]);T.set(z,(T.get(z)||0n)+c);}
  }return T;
 }
 function tail(t,kq){
  const all=new Map();
  for(let prev=0;prev<2;prev++){
   let cur=new Map([[pack([0,prev]),1n]]);
   for(let j=1;j<=t;j++){const nxt=new Map();
    for(const [id,c] of cur){const [b,v]=unpack(id);
     for(let x=0;x<2;x++){if(x&&(v||j===t)||b+x>kq)continue;
      const z=pack([b+x,x]);nxt.set(z,(nxt.get(z)||0n)+c);
     }
    }cur=nxt;
   }
   for(let r=0;r<=kq;r++){all.set(pack([prev,r]),t===0?(prev===0&&r===0?1n:0n):(cur.get(pack([r,0]))||0n));}
  }return all;
 }
 function model(m,n,kp,kq,d,r){
  const l=Math.min(r,n-m),t=n-m-l,T=prefix(m,kp,kq,d),U=tail(t,kq), memo=new Map(),massMemo=new Map();
  function mass(s,f,v){const id=pack([s,f,v]);if(massMemo.has(id))return massMemo.get(id);
   let M=0n;for(const [id,c] of T){const [b,prev]=unpack(id);const need=kq-b-s;
    if(prev===1&&f===1||need<0||need>kq)continue;
    M+=c*(U.get(pack([v,need]))||0n);
   }massMemo.set(id,M);return M;
  }
  function count(j,s,f,v){const id=pack([j,s,f,v]);if(memo.has(id))return memo.get(id);
   if(j===l){const x=mass(s,f,v)>0n?1n:0n;memo.set(id,x);return x;}
   let x=count(j+1,s,j===0?0:f,0);
   if(v===0)x+=count(j+1,s+1,j===0?1:f,1);
   memo.set(id,x);return x;
  }
  function unrank(x){fail(x>=0n&&x<count(0,0,0,0),"unrank range");
   let w="",s=0,f=0,v=0;
   for(let j=0;j<l;j++){const A=count(j+1,s,j===0?0:f,0);
    if(x<A){w+="A";if(j===0)f=0;v=0;}else{fail(!v,"unrank adjacency");x-=A;w+="B";s++;if(j===0)f=1;v=1;}
   }return w;
  }
  function rank(w){fail(w.length===l,"rank length");
   let id=0n,s=0,f=0,v=0;
   for(let j=0;j<l;j++){
    if(w[j]==="B"){fail(!v,"rank adjacency");id+=count(j+1,s,j===0?0:f,0);s++;if(j===0)f=1;v=1;}
    else{fail(w[j]==="A","rank alphabet");if(j===0)f=0;v=0;}
   }fail(mass(s,f,v)>0n,"rank unsupported");return id;
  }
  let W=new Map([[pack([0,0,0,0]),1n]]);
  for(let j=0;j<l;j++){const next=new Map();
   for(const [id,num] of W){const [pos,s,f,v]=unpack(id),a=pack([pos+1,s,pos===0?0:f,0]);
    next.set(a,(next.get(a)||0n)+num);
    if(!v){const b=pack([pos+1,s+1,pos===0?1:f,1]);next.set(b,(next.get(b)||0n)+num);}
   }W=next;
  }
  let q=0n,pop=0n;const histogram=[];
  for(const [id,num] of W){const [j,s,f,v]=unpack(id),M=mass(s,f,v);
   if(M>0n){q+=num;pop+=num*M;histogram.push({Bs:s,first:f?"B":"A",last:v?"B":"A",classes:num.toString(),each_mass:M.toString()});}
  }fail(count(0,0,0,0)===q,"support consistency");
  return {l,q,pop,mass,rank,unrank,histogram};
 }
 const mismatch=(P,Q)=>P.split("").filter((c,i)=>c!==Q[i]).length;
 let trials=0,nonempty=0,historyChecks=0,classChecks=0,rankChecks=0,saturated=0;
 for(let m=3;m<=6;m++)for(let n=m+1;n<=m+3;n++)
 for(let kp=0;kp<=Math.min(3,m);kp++)for(let kq=0;kq<=Math.min(3,n);kq++)
 for(let d=0;d<=Math.min(2,m);d++)for(let r=1;r<=n-m+1;r++){
  const M=model(m,n,kp,kq,d,r),counts=new Map();
  for(const P of legal(m,kp))for(const Q of legal(n,kq)){
   if(mismatch(P,Q.slice(0,m))!==d)continue;
   const w=Q.slice(m,m+M.l);counts.set(w,(counts.get(w)||0n)+1n);
  }
  fail(BigInt(counts.size)===M.q,"class count parameter "+[m,n,kp,kq,d,r]);
  let total=0n;for(const [w,c] of counts){
   const s=w.split("").filter(x=>x==="B").length, f=w[0]==="B"?1:0,v=w.at(-1)==="B"?1:0;
   fail(M.mass(s,f,v)===c,"class population "+[m,n,kp,kq,d,r,w]);
   fail(M.unrank(M.rank(w))===w,"lex rank");
   total+=c;classChecks++;rankChecks++;
  }
  fail(total===M.pop,"fiber mass");historyChecks+=Number(total);
  trials++;if(total>0n)nonempty++;if(r>n-m)saturated++;
 }
 const dirs=["A","B","C","D","E","F","G","H","I","J","K","L"];
 function obs(P,Q){
  const v=w=>{let o=[0,0,0,0,0,0];for(const c of w){let id=dirs.indexOf(c);o[Math.floor(id/2)]+=id%2?-1:1;}return o;};
  const J=w=>{let a=Array(144).fill(0);for(let i=1;i<w.length;i++)a[dirs.indexOf(w[i-1])*12+dirs.indexOf(w[i])]++;return a;};
  return JSON.stringify([P.length,Q.length,v(P),v(Q),J(P),J(Q),P.split("").filter((x,i)=>i<Q.length&&x===Q[i]).length]);
 }
 function trace(P,Q,r){const arr=[obs(P,Q)];
  function visit(w,j){if(j>=r)return;for(const z of dirs){const next=w+z;arr.push(obs(next,Q));visit(next,j+1);}}
  visit(P,0);return arr.join("\n");
 }
 let trees=0,tracePrefixes=0,fibers=0;
 const testCases=[[4,7,1,2,1,3],[5,7,1,1,1,2],[5,8,1,2,1,3],[4,6,1,1,0,2]];
 for(const [m,n,kp,kq,d,r] of testCases){
  const seen=new Map();let used=0;
  for(const P of legal(m,kp))for(const Q of legal(n,kq)){
   if(mismatch(P,Q.slice(0,m))!==d)continue;
   const w=Q.slice(m,m+Math.min(r,n-m)),z=trace(P,Q,r);
   if(seen.has(w))fail(seen.get(w)===z,"full future within class");
   else seen.set(w,z);
   trees++;used++;tracePrefixes+=(12**(r+1)-1)/11;
  }
  if(used){fail(new Set(seen.values()).size===seen.size,"full future between class");fibers++;}
 }
 const P="AABAA",Q1="AAAAAABABAA",Q2="AAAAAAABABA";
 fail(obs(P,Q1)===obs(P,Q2),"witness same O");
 const K=w=>w.split("").filter((c,i)=>c==="AB".charAt(-1)&&false).length; // never used; kept empty to avoid effect
 const match=(a,b)=>a.split("").filter((x,i)=>i<b.length&&x===b[i]).length;
 fail(match(P,Q1)===4&&match(P,Q2)===4,"witness initial");
 fail(match(P+"AB",Q1)===6&&match(P+"AB",Q2)===5,"witness separated after two appends");
 const big=model(64,80,15,17,1,12);
 fail(big.q>0n&&big.pop>0n,"large nonempty");
 for(const index of [0n,big.q/2n,big.q-1n])fail(big.rank(big.unrank(index))===index,"large rank");
 return {marker:"STAGE447B_OUTPUT_WORD_POLYNOMIAL_SUPPORT_PASS",provenance:"P000 native X6; A=+E1, B=-E1; Q static; P APPEND arbitrary one of all 12 signed directions",
  finite:{parameter_cases:trials,nonempty_fibers:nonempty,raw_history_instances:historyChecks,output_class_checks:classChecks,lexicographic_rank_checks:rankChecks,saturation_cases:saturated},
  independent_full_future:{fibers,history_trees:trees,observation_prefixes:tracePrefixes,all_12_signed_directions:true,testCases},
  witness:{P,Q1,Q2,initial_K:4,trace:"P:APPEND(A);P:APPEND(B)",final_K:[6,5]},
  large:{m:64,n:80,kP:15,kQ:17,d:1,rP:12,classes:big.q.toString(),population:big.pop.toString(),histogram:big.histogram,rank_samples:["0",(big.q/2n).toString(),(big.q-1n).toString()]},
  exact_arithmetic:"JavaScript BigInt; complete specified finite domains; no numerical approximations",pass:true};
}
console.log(JSON.stringify(main(), null, 2));
