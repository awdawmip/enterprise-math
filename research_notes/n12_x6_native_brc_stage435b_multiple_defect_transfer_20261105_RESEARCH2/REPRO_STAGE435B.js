"use strict";
// Stage435-B: exact integer nonadjacent-defect observer quotient.
// Native X6 labels are twelve signed primitive directions; no projection of
// the native path occurs before the scope-typed future-quotient certificate.
const DIRS = Array.from({length:6},(_,j)=>["+E"+(j+1),"-E"+(j+1)]).flat();
const A="+E1", B="-E1", C="+E2";
function check(test,message){if(!test)throw Error(message)}
function choose(N,K){if(K<0||K>N)return 0n;let z=1n;for(let i=1;i<=K;i++)z=z*BigInt(N-K+i)/BigInt(i);return z}
function defectSets(m,k){
  const answer=[];
  function go(pos,last,chosen){
    if(chosen.length===k){answer.push(chosen.slice());return}
    for(let i=pos;i<=m-1;i++){
      chosen.push(i);go(i+2,i,chosen);chosen.pop()
    }
  }
  go(2,0,[]);return answer
}
function fullPath(m,set){let P=Array(m).fill(A);for(const i of set)P[i-1]=B;return P}
function mask(set,a,z){return set.filter(i=>i>=a&&i<=z).join(",")}
function massDP(m,k,a,z,maskText){
  const fixed=new Set(maskText?maskText.split(",").map(Number):[]);
  let d0=Array(k+1).fill(0n),d1=Array(k+1).fill(0n);d0[0]=1n;
  for(let pos=2;pos<=m-1;pos++){
    const e0=Array(k+1).fill(0n),e1=Array(k+1).fill(0n);
    const inWindow=pos>=a&&pos<=z, one=fixed.has(pos);
    for(let j=0;j<=k;j++){
      if(!inWindow||!one)e0[j]=d0[j]+d1[j];
      if((!inWindow||one)&&j>0)e1[j]=d0[j-1];
    }
    d0=e0;d1=e1
  }
  return d0[k]+d1[k]
}
function masks(a,z,k){
  const out=[];
  function go(i,S){
    if(i>z){out.push(S.join(","));return}
    go(i+1,S);
    if(S.length<k && (!S.length||S[S.length-1]<i-1)){
      S.push(i);go(i+1,S);S.pop()
    }
  }
  go(a,[]);return out
}
function K(P,Q){let n=Math.min(P.length,Q.length),t=0;for(let i=0;i<n;i++)if(P[i]===Q[i])t++;return t}
function qObs(Q){
  const end=Array(6).fill(0),j={};
  for(let i=0;i<Q.length;i++){
    const v=Q[i],axis=Number(v.slice(2))-1;end[axis]+=(v[0]==="+"?1:-1);
    if(i>0){const e=Q[i-1]+"/"+v;j[e]=(j[e]||0)+1}
  }
  return JSON.stringify([Q.length,end,Object.entries(j).sort()])
}
function legalWords(n,p,r){
  const answer=[];
  function go(words,pops,apps,len){
    answer.push(words.slice());
    if(pops<p&&len>0){words.push(["POP"]);go(words,pops+1,apps,len-1);words.pop()}
    if(apps<r)for(const d of DIRS){words.push(["APPEND",d]);go(words,pops,apps+1,len+1);words.pop()}
  }
  go([],0,0,n);return answer
}
function finalQ(n,ops){const q=Array(n).fill(C);for(const op of ops)if(op[0]==="POP")q.pop();else q.push(op[1]);return q}
function witness(i,n){
  let ops=[];
  if(i<=n){for(let j=0;j<n-i+1;j++)ops.push(["POP"])}
  else{for(let j=0;j<i-n-1;j++)ops.push(["APPEND",C])}
  ops.push(["APPEND",B]);return ops
}
function verify(){
  const cases=[[9,3,1,2,2],[10,5,1,1,2],[12,6,1,2,2],[13,6,2,2,2],[15,7,2,3,2]];
  const results=[];let histories=0,wordsSeen=0,trajectoryChecks=0,dpChecks=0,witnessChecks=0,classComparisons=0;
  for(const [m,n,p,r,k] of cases){
    const a=n-p+1,z=n+r,w=z-a+1;
    check(n>=p+1&&m>=n+r+2&&m>=2*k+1,"domain");
    const sets=defectSets(m,k),wordList=legalWords(n,p,r);
    const grouped=new Map();
    for(const set of sets){const key=mask(set,a,z);if(!grouped.has(key))grouped.set(key,[]);grouped.get(key).push(set)}
    histories+=sets.length;wordsSeen+=wordList.length;
    check(BigInt(sets.length)===choose(m-k-1,k),"whole fiber count");
    const allMasks=masks(a,z,k);let weight=0n;
    for(const key of allMasks){
      const dp=massDP(m,k,a,z,key);
      const actual=BigInt((grouped.get(key)||[]).length);
      check(dp===actual,"DP mass mismatch "+[m,n,p,r,k,key,dp,actual]);
      weight+=dp;dpChecks++
    }
    check(weight===BigInt(sets.length),"mass partition");
    const codebook=Array.from(grouped.keys()).sort((x,y)=>{
      let xx=x?x.split(",").map(Number):[], yy=y?y.split(",").map(Number):[];
      for(let i=0;i<Math.min(xx.length,yy.length);i++)if(xx[i]!==yy[i])return xx[i]-yy[i];
      return xx.length-yy.length
    });
    const representativeSignatures=new Map();
    for(const [key, members] of grouped){
      for(const set of members){
        const P=fullPath(m,set),s=[];
        for(const ops of wordList){
          let q=Array(n).fill(C),cached=0;
          const observations=[String(K(P,q))];
          check(cached===K(P,q),"initial readout");
          for(const op of ops){
            if(op[0]==="POP"){
              const i=q.length, letter=q.pop();
              if(i>=a&&i<=z)cached-=key.split(",").filter(Boolean).map(Number).includes(i)?Number(letter===B):Number(letter===A)
            }else{
              const i=q.length+1,letter=op[1];q.push(letter);
              if(i>=a&&i<=z)cached+=key.split(",").filter(Boolean).map(Number).includes(i)?Number(letter===B):Number(letter===A)
            }
            check(cached===K(P,q),"class reader mismatch");
            observations.push(String(cached));trajectoryChecks++
          }
          // Q's complete endpoint/J observer is independent of which P in this fiber.
          check(qObs(q)===qObs(finalQ(n,ops)),"Q observable mismatch");
          s.push(observations.join(":"))
        }
        const signature=s.join("|");
        if(!representativeSignatures.has(key))representativeSignatures.set(key,signature);
        else check(representativeSignatures.get(key)===signature,"fiber constancy");
      }
    }
    for(let i=0;i<codebook.length;i++)for(let j=i+1;j<codebook.length;j++){
      const x=codebook[i],y=codebook[j],S=grouped.get(x)[0],T=grouped.get(y)[0];
      check(representativeSignatures.get(x)!==representativeSignatures.get(y),"quotient separation");
      const diff=Array.from(new Set([...S,...T].filter(t=>t>=a&&t<=z))).find(v=>S.includes(v)!==T.includes(v));
      check(diff!==undefined,"symmetric difference");
      const ops=witness(diff,n);
      check(ops.filter(op=>op[0]==="POP").length<=p&&ops.filter(op=>op[0]==="APPEND").length<=r,"witness budget");
      check(K(fullPath(m,S),finalQ(n,ops))!==K(fullPath(m,T),finalQ(n,ops)),"witness readout");
      witnessChecks++;classComparisons++
    }
    if(a-2>=2*k-1){
      let expected=0n;
      for(let j=0;j<=k;j++)expected+=choose(w-j+1,j);
      check(BigInt(codebook.length)===expected,"buffered closed formula")
    }
    results.push({m,n,p,r,k,window:[a,z],full_fiber:sets.length,class_count:codebook.length,class_masses:codebook.map(key=>({B_positions:key||"(none)",mass:grouped.get(key).length})),future_operation_words:wordList.length,minimum_fixed_class_bits:Math.ceil(Math.log2(codebook.length))});
  }
  // Check one explicit POP and APPEND distinction in the same original fiber.
  const p1=fullPath(13,[5,7]),p2=fullPath(13,[6,8]),n=6;
  const w1=witness(5,n),w2=witness(8,n);
  check(K(p1,finalQ(n,w1))===1&&K(p2,finalQ(n,w1))===0,"POP/APPEND example");
  check(K(p1,finalQ(n,w2))===0&&K(p2,finalQ(n,w2))===1,"APPEND example");
  return {status:"STAGE435B_MULTIDEFECT_EXACT_TRANSFER_PASS",arithmetic:"integer (BigInt) and equality of finite native labels",native_append_directions:DIRS.length,cases:results,totals:{original_histories:histories,legal_operation_words_per_case_total:wordsSeen,transfer_matrix_masses_checked:dpChecks,stepwise_reader_checks:trajectoryChecks,distinguishing_pairs_checked:witnessChecks,class_pairs_checked:classComparisons},witnesses:{POP_then_APPEND_B:{operations:w1,match_counts:[1,0]},APPEND_C_then_APPEND_B:{operations:w2,match_counts:[0,1]}}}
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));
