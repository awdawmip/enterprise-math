#!/usr/bin/env node
'use strict';
function verify(){
  "use strict";
  const md=(x,m)=>((x%m)+m)%m, iv=(a,p)=>{for(let u=1;u<p;u++)if(md(a*u,p)===1)return u;throw Error("inverse");};
  const gcd=(a,b)=>b?gcd(b,a%b):a, ck=(x,msg)=>{if(!x)throw Error(msg);};
  const RF=(S,c,m)=>new Set([...S].map(x=>md(c-x,m)));
  const DI=(S,T)=>new Set([...S,...T].filter(x=>S.has(x)!==T.has(x)));
  function graph(S){
    const W=Array.from({length:10},(_,c)=>DI(S,RF(S,c,10))),D=Math.min(...W.map(z=>z.size));
    const centers=W.flatMap((v,c)=>v.size===D?[c]:[]);
    const edges=D===2?centers.map(c=>{const [x,y]=[...W[c]].sort((a,b)=>a-b);
      ck(x!==y&&md(x+y,10)===c&&S.has(x)!==S.has(y),"signed reflection pair");
      return {center:c,plus:S.has(x)?x:y,minus:S.has(x)?y:x};
    }):[];
    const V=[...new Set(edges.flatMap(e=>[e.plus,e.minus]))],adj=new Map(V.map(x=>[x,new Set()]));
    for(const e of edges){adj.get(e.plus).add(e.minus);adj.get(e.minus).add(e.plus);}
    const seen=new Set(),components=[];
    for(const v of V)if(!seen.has(v)){let stack=[v],n=0;seen.add(v);
      while(stack.length){const x=stack.pop();n++;for(const y of adj.get(x))if(!seen.has(y)){seen.add(y);stack.push(y);}}
      components.push(n);
    }
    components.sort((a,b)=>a-b);
    return {D,centers,edges,components};
  }
  const masks={D0:0,D2_N1_P2:0,D2_N2_P2P2:0,D2_N3_P2P2P2:0,D2_N4_P3P3:0};
  for(let m=0;m<1024;m++){
    const S=new Set(Array.from({length:10},(_,x)=>x).filter(x=>m&(1<<x))),g=graph(S);
    if(g.D===0){masks.D0++;continue;}
    ck(g.D===2,"D not 0 or 2");
    const shape=`D2_N${g.edges.length}_${g.components.map(x=>`P${x}`).join("")}`;
    ck(Object.hasOwn(masks,shape),"universal graph "+m);
    masks[shape]++;
  }
  ck(JSON.stringify(masks)===JSON.stringify({D0:424,D2_N1_P2:160,D2_N2_P2P2:240,D2_N3_P2P2P2:80,D2_N4_P3P3:120}),"universal census");
  const pw=(a,k,p)=>{let x=1;for(let i=0;i<k;i++)x=md(x*a,p);return x;};
  const U=md(4822040484*iv(md(8132285009,11),11),11),gma=md(141024*iv(md(1653649,11),11),11),I=iv(md(637,11),11),C=md(-3*I,11),T=md(U*gma,11);
  ck(U===4&&gma===6&&C===3&&T===2,"BRC16943");
  const rows=Array.from({length:11},(_,z)=>{const l=md((637-3*z)*I,11),r=md(U*(1+gma*z),11);return {z,l,r,A:md(1-(1-z)*l,11),B:md(1-(1-z)*r,11)};});
  const P=new Set();
  for(let h=0;h<10;h++)for(let n=0;n<10;n++){
    if(rows.filter(x=>x.z!==3).every(x=>md(pw(x.A,h,11)*pw(x.l,n,11)-pw(x.B,h,11)*pw(x.r,n,11),11)!==0)&&
      md(pw(C,h+n,11)-pw(T,h+n,11),11)!==0)P.add(10*h+n);
  }
  ck(P.size===44,"P10 size");
  const F={"00":[3],"01":[0,3,4,"inf"],"10":[2,3,4,"inf"],"11":[2,3]};
  const project=(h,n)=>{h=md(h,5);n=md(n,5);return h===0?(n===0?"zero":"inf"):md(n*iv(h,5),5);};
  const phi=(s,q)=>s==="inf"?q:q==="inf"?0:iv(md(q-s,5),5);
  for(let h=0;h<10;h++)for(let n=0;n<10;n++)
    ck(P.has(10*h+n)===F[`${h%2}${n%2}`].includes(project(h,n)),"fiber match");
  const H={},classes={},directions=[];
  for(let a=0;a<10;a++)for(let b=0;b<10;b++){
    if(gcd(gcd(a,b),10)!==1)continue;
    let h0=null,n0=null;
    for(let h=0;h<10&&h0===null;h++)for(let n=0;n<10;n++)if(md((b-a)*h-a*n+1,10)===0){h0=h;n0=n;break;}
    ck(h0!==null,"affine anchor");
    const S=new Set();
    for(let t=0;t<10;t++)if(P.has(10*md(h0+a*t,10)+md(n0+(b-a)*t,10)))S.add(t);
    const aa=md(a,5),bb=md(b,5),s=aa===0?"inf":md((b-a)*iv(aa,5),5);
    const alpha=aa===0?md(-bb*bb,5):md(aa*aa,5),beta=aa===0?md(-bb*n0,5):md(aa*h0,5);
    const Z=[0,1].map(t=>{const tag=`${md(h0+a*t,2)}${md(n0+(b-a)*t,2)}`;
      return new Set(F[tag].filter(q=>q!==s).map(q=>phi(s,q)));
    });
    const predicted=new Set();
    for(let t=0;t<10;t++)if(Z[t%2].has(md(alpha*t+beta,5)))predicted.add(t);
    ck(DI(S,predicted).size===0,"CRT decoder mask");
    const g=graph(S);
    for(let c=0;c<10;c++){
      const cc=md(2*beta+alpha*c,5),cp=c%2,sites=[];
      for(let t=0;t<10;t++){const z=md(alpha*t+beta,5),p=t%2;
        if(Z[p].has(z)!==Z[md(cp-p,2)].has(md(cc-z,5)))sites.push(t);
      }
      ck(JSON.stringify(sites)===JSON.stringify([...DI(S,RF(S,c,10))].sort((x,y)=>x-y)),"CRT decoder signed mismatch");
    }
    const N=g.centers.length,shape={D:g.D,N,E:g.centers.filter(c=>c%2===0).length,O:g.centers.filter(c=>c%2===1).length,components:g.components};
    ck(g.D===0||(N===1&&g.components.join()==="2")||(N===2&&g.components.join()==="2,2")||(N===4&&g.components.join()==="3,3"),"frozen forest");
    const label=`${a%2}${b%2}/${aa===0?"inf":md(bb*iv(aa,5),5)}`;
    if(Object.hasOwn(classes,label))ck(JSON.stringify(classes[label])===JSON.stringify(shape),"class invariant");
    else classes[label]=shape;
    const hk=`D${g.D}_N${N}`;H[hk]=(H[hk]||0)+1;
    directions.push({a,b,crt_class:label,...shape,signed_optimal_edges:g.edges});
  }
  ck(directions.length===72&&Object.keys(classes).length===18,"class coverage");
  ck(H.D0_N1===8&&H.D2_N1===24&&H.D2_N2===24&&H.D2_N4===16&&Object.keys(H).length===4,"frozen census");
  return {status:"ALL PASS",scientific_input:"BRC16943",domain:"Z/10 binary masks and frozen auxiliary P10",arithmetic:"exact integer modulo 5/10/11",universal_masks:1024,universal_graph_census:masks,frozen_P10_cells:P.size,source_fiber_checks:100,primitive_directions:directions.length,CRT_classes:Object.keys(classes).length,frozen_graph_census:H,CRT_class_graphs:classes,all_72_direction_signed_edges:directions,limitations:"Upstream Bernoulli reduction inherited; full mod11, global Farey, X6 native interpretations and independent review unresolved."};
}
console.log(JSON.stringify(verify(),null,2));
