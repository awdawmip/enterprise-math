(() => {
"use strict";
const colors=["a","b","B","c","x"], reps={a:"a",b:"b",B:"B",c:"c",x:"A"};
function nextq(g,q,ch) {
  const s=g.slice(0,q)+ch;
  for(let j=g.length;j>=0;j--) if(s.endsWith(g.slice(0,j)))return j;
}
function advance(g,s,c) {
  let [q,t]=s.split(":"); q=Number(q);
  if(t==="N") {if(c==="b"||c==="B")t="B";else if(c==="c")t="C";}
  return nextq(g,q,reps[c])+":"+t;
}
function machine(g) {
  const states=["0:N"], T={};let p=0;
  while(p<states.length){let s=states[p++];
    for(const c of colors){let e=advance(g,s,c); T[s+"|"+c]=e;
      if(!states.includes(e))states.push(e);
    }
  }
  return {states,T};
}
function reconstruct(start,T,z) {
  const left={...z},stack=[[start,null]],back=[];
  while(stack.length) {
    const v=stack[stack.length-1][0];
    let c=colors.find(c=>(left[v+"|"+c]||0)>0);
    if(c!==undefined){left[v+"|"+c]--;stack.push([T[v+"|"+c],c]);}
    else{let [,used]=stack.pop();if(used!==null)back.push(used);}
  }
  if(Object.values(left).some(x=>x!==0))throw Error("unused edges");
  return back.reverse().join("");
}
function edges(start,T,w) {
  let z={},s=start;
  for(const c of w){let k=s+"|"+c;z[k]=(z[k]||0)+1;s=T[k];}
  return {z,end:s};
}
function check(z,f,states,T) {
  const ino={},out={},adj={};for(const s of states){ino[s]=0;out[s]=0;adj[s]=new Set();}
  for(const [k,n] of Object.entries(z)){let [s,c]=k.split("|"),t=T[k];
    if(!Number.isInteger(n)||n<0)throw Error("bad multiplicity");
    out[s]+=n;ino[t]+=n;if(n){adj[s].add(t);adj[t].add(s);}
  }
  for(const s of states)
    if(out[s]-ino[s] !== (s==="0:N"?1:0)-(s===f?1:0))return false;
  const used=states.filter(s=>ino[s]+out[s]>0);
  if(!used.length)return f==="0:N";
  if(!used.includes("0:N"))return false;
  const seen=new Set(["0:N"]),todo=["0:N"];
  while(todo.length){let s=todo.pop();for(let t of adj[s])if(!seen.has(t)){seen.add(t);todo.push(t);}}
  return used.every(s=>seen.has(s));
}
const gates=[];
for(const g of ["aab","aba"]) {
  const {states,T}=machine(g),s0="0:N";let count=0,witness=0;
  function visit(w,s,z) {
    if(!check(z,s,states,T))throw Error("Euler criterion failure");
    const rw=reconstruct(s0,T,z), e=edges(s0,T,rw);
    if(e.end!==s||JSON.stringify(e.z)!==JSON.stringify(z)) {
      // Different key insertion order is immaterial.
      if(e.end!==s||Object.keys(z).some(k=>e.z[k]!==z[k])||
         Object.keys(e.z).some(k=>e.z[k]!==z[k]))throw Error("Euler reconstruction failure");
    }
    for(const c of colors)if(w.split(c).length!==rw.split(c).length)throw Error("color count");
    count++;witness++;
    if(w.length===6)return;
    for(const c of colors){
      const k=s+"|"+c, zz={...z};zz[k]=(zz[k]||0)+1;
      visit(w+c,T[k],zz);
    }
  }
  visit("",s0,{});
  gates.push({gate:g,states:states.length,complete_five_color_words_through_length_6:count,exact_euler_witnesses:witness});
}
return {id:"PREFIX-498",certificate:"five-color transition-flow Euler equivalence",gates,status:"ALL_CHECKS_PASS"};
})()