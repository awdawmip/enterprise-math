#!/usr/bin/env node
'use strict';
// R762AF exact star physical DP versus independent cycle-cut DP; normalized labels.
function popcount(x){let k=0;while(x){x&=x-1;k++}return k}

function oneCycle(word,lo,hi){
 let t=null,v=null,u=null,ins=0,outs=0;
 for(const [kind,j] of word){
  if(j<lo||j>=hi)continue;
  if(kind==="I"){if(t===null){t=j;v=j}else if(u===null)u=j;else return false;ins++}
  else{if(u!==null){if(j===u)t=u;else if(j===v)v=u;else return false;u=null}
       else if(t!==null){if(ins!==hi-lo||j!==v||t===j)return false;t=v=null}
       else return false;outs++}
 }
 return t===null&&u===null&&ins===hi-lo&&outs===hi-lo;
}

function cutCount(word,n){
 const dp=Array(n+1).fill(0);dp[0]=1;
 for(let end=2;end<=n;end++)for(let start=0;start<=end-2;start++)if(dp[start]&&oneCycle(word,start,end))dp[end]+=dp[start];
 return dp[n];
}

function traceCount(word,n){
 let states=new Map([[0,1]]),entered=0,departed=0;
 for(const [kind,j] of word){
  const next=new Map();
  if(kind==="I"){if(entered&(1<<j))return 0;entered|=1<<j;for(const [mask,v] of states)next.set(mask|(1<<j),(next.get(mask|(1<<j))||0)+v)}
  else{if(!(entered&(1<<j))||(departed&(1<<j)))return 0;departed|=1<<j;for(const [mask,v] of states){let opts=mask&~(1<<j);while(opts){let bit=opts&-opts;opts-=bit;let after=mask^bit;next.set(after,(next.get(after)||0)+v)}}}
  states=next;
 }
 return entered===(1<<n)-1&&departed===(1<<n)-1?(states.get(0)||0):0;
}

function fib(n){let a=0,b=1;for(let i=0;i<n;i++)[a,b]=[b,a+b];return a}

function canonical(n){let w=[["I",0],["I",1],["O",0]];for(let i=2;i<n;i++)w.push(["I",i],["O",i-1]);w.push(["O",n-1]);return w}

function verify(n){
 const out={n,normalizedTranscripts:0,maximum:0,histogram:{},checks:0};
 const walk=(k,done,w,states)=>{
  const h=k-popcount(done);
  if(done===(1<<n)-1){
   const c=states.get(0)||0;
   if(c===0||c!==cutCount(w,n))throw Error("Physical/composition mismatch n="+n+" word="+JSON.stringify(w));
   out.normalizedTranscripts++;out.checks++;out.histogram[c]=(out.histogram[c]||0)+1;out.maximum=Math.max(out.maximum,c);return
  }
  if(k<n&&h<2){const next=new Map();for(const [mask,v] of states)next.set(mask|(1<<k),(next.get(mask|(1<<k))||0)+v);walk(k+1,done,w.concat([["I",k]]),next)}
  if(h)for(let j=0;j<k;j++){
   if(done&(1<<j))continue;
   const next=new Map();
   for(const [mask,v] of states){let opts=mask&~(1<<j);while(opts){let bit=opts&-opts;opts-=bit;let after=mask^bit;next.set(after,(next.get(after)||0)+v)}}
   if(next.size)walk(k,done|(1<<j),w.concat([["O",j]]),next);
  }
 };
 walk(0,0,[],new Map([[0,1]]));
 const target=fib(n-1);
 if(out.maximum!==target||traceCount(canonical(n),n)!==target||cutCount(canonical(n),n)!==target)throw Error("Sharpness mismatch "+n);
 return out;
}

function run(){
 const rows=[];for(let n=2;n<=11;n++)rows.push(verify(n));
 return {schema:"R762AF_SHARP_FIBONACCI_FIBER_V1",model:"conditional two-slot star shortest transfers",proofScope:"all integers m>=2",exactTestScope:"exhaustive normalized physically-realizable logs m=2..11",rows,scientificInput:"a72226e2430ffa4786321ac86e7f0c599d5f0389",parentCommit:"02c36f124254fb5da5122ebf3d1c6251001c0eb8",status:"AUTHOR_SIDE_NOT_NATIVE_ADMITTED_NOT_REVIEWED"};
}
console.log(JSON.stringify(run(),null,2));
