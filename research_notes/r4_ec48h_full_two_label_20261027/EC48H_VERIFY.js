#!/usr/bin/env node
"use strict";
const report=(function verifyEC48H(){
  "use strict";
  const V=[[0,0],[1,0],[0,1],[1,1]];
  const E=[];for(let b=0;b<4;b++)for(let a=0;a<4;a++)if((b&a)===b)E.push([b,a]);
  if(E.length!==9)throw Error("not nine comparable pairs");
  const C=[[0,0],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[3,3]];
  const out={schema:"EC48H_EXACT_JS_V1",templates_total:511,eligible:0,ineligible:0,stages:0,coordinate_inequalities:0,cases:{},dyadic_witness_samples:0,arithmetic:"binary-exact dyadic rational endpoint checks",status:"PASS"};
  function read(w,dec){let v=[0,0];for(const[k,t]of Object.entries(w)){v[0]+=t*dec[k][0];v[1]+=t*dec[k][1]}return v}
  function solve(T){
    let B=new Set(T.map(e=>e[0])),A=new Set(T.map(e=>e[1]));
    let chosen=C.find(([ob,oa])=>[...B].every(v=>v!==ob)&&[...A].every(v=>v!==oa));
    if(!chosen)throw Error("no compatible padding");
    const [ob,oa]=chosen, key=`${ob},${oa}`;out.cases[key]=(out.cases[key]||0)+1;
    let dec={};for(let k=0;k<4;k++)if(k!==ob)dec[k]=V[k].slice();
    let ws=T.map(([b])=>({[b]:1}));
    const measure=()=>ws.map(w=>read(w,dec));
    const check=(start,stop,label)=>{
      for(let i=0;i<T.length;i++){
        let [b,a]=T[i];
        for(let j=0;j<2;j++){
          if(!(V[b][j]<=start[i][j]&&start[i][j]<=stop[i][j]&&stop[i][j]<=V[a][j]))throw Error(`nonmonotone ${key}:${label}:${i}:${j}`);
          out.coordinate_inequalities++;
        }
        if(Object.values(ws[i]).some(v=>v<0)||Object.values(ws[i]).reduce((a,b)=>a+b,0)!==1)throw Error("invalid encoder distribution");
      }
      out.stages++;
    };
    const assign=(changes,label)=>{
      let start=measure();for(const[k,w]of Object.entries(changes))ws[Number(k)]=w;
      check(start,measure(),label);
    };
    const shift=(slot,v,label)=>{let start=measure();dec[slot]=V[v].slice();check(start,measure(),label)};
    const jump=(slot,v,label)=>{
      if(ws.some(w=>(w[slot]||0)!==0))throw Error("reset occupied decoder");
      let before=measure();dec[slot]=V[v].slice();let after=measure();
      if(JSON.stringify(before)!==JSON.stringify(after))throw Error("reset changed kernel");
      check(before,after,label);
    };
    const finish=()=>{
      let inverse={};for(const[k,v]of Object.entries(dec))inverse[v.join(",")]=Number(k);
      if(Object.keys(inverse).length!==3)throw Error("three decoder corners required");
      let changes={};for(let i=0;i<T.length;i++)changes[i]={[inverse[V[T[i][1]].join(",")]]:1};
      assign(changes,"final");
    };
    if(ob===oa){finish()}
    else if((ob===1||ob===2)&&oa===0){
      let changes={};for(let i=0;i<T.length;i++){let[b,a]=T[i];if(b===0&&a!==ob)changes[i]={[a]:1}}
      assign(changes,"free00");shift(0,ob,"slide00");finish();
    }else if((ob===1&&oa===2)||(ob===2&&oa===1)){
      let changes={};for(let i=0;i<T.length;i++)if(T[i][0]===oa)changes[i]={3:1};
      assign(changes,"freeSide");jump(oa,ob,"recycleSide");finish();
    }else if(ob===3&&(oa===1||oa===2)){
      shift(oa,3,"slideTo11");finish();
    }else if(ob===3&&oa===0){
      let changes={};for(let i=0;i<T.length;i++){let[b,a]=T[i];if(b===0)changes[i]=a===3?{1:0.5,2:0.5}:{[a]:1}}
      assign(changes,"antiDiagonal");jump(0,3,"recycle00");finish();
    }else throw Error("unlisted support case");
    let final=measure();for(let i=0;i<T.length;i++)if(JSON.stringify(final[i])!==JSON.stringify(V[T[i][1]]))throw Error("bad target");
  }
  for(let mask=1;mask<512;mask++){
    let T=E.filter((_,i)=>(mask&(1<<i))!==0);
    if(new Set(T.map(z=>z[0])).size>3||new Set(T.map(z=>z[1])).size>3){out.ineligible++;continue}
    out.eligible++;solve(T);
  }
  if(out.eligible!==291||out.ineligible!==220||out.stages!==667||out.coordinate_inequalities!==4964)throw Error("unexpected exhaustive checksum");
  const P=[[1,2],[2,1],[2,3],[3,2],[2,2]],Q=Array.from({length:5},()=>[2,2]);
  for(const stage of [1,2])for(const s of [0,0.25,0.5,1]){
    const W=stage===1?[[0,s],[s,0],[0,1],[1,0],[s/2,s/2]]:[[0,1],[1,0],[s,1],[1,s],[(1+s)/2,(1+s)/2]];
    let aa=0,bb=0;for(let h=0;h<5;h++)for(let y=0;y<2;y++){aa+=P[h][y]*W[h][y];bb+=Q[h][y]*W[h][y]}
    if(aa-bb!==2||bb!==(stage===1?4+6*s:10+6*s))throw Error("bad rational face witness");
    out.dyadic_witness_samples++;
  }
  return out;
})();
process.stdout.write(JSON.stringify(report,null,2)+"\n");
