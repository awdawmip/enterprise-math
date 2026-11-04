/* PREFIX-486: independent JavaScript reachability DP plus brute enumerator; run: node prefix486_three_source_certificate.js */
function certificate(){
 const L="aAbBcCdDeE", V=[0,1,0,2,1], W=[0,0,1,0,1];
 function invariant(x,why){if(!x)throw Error(why)}
 function choose(n,k){if(n<k||n<0)return 0;let r=1;for(let i=1;i<=k;i++)r=r*(n-k+i)/i;return Math.round(r)}
 function kmp(q,c,w){const s=w.slice(0,q)+c;for(let j=w.length;j>=0;j--)if(s.endsWith(w.slice(0,j)))return j;throw Error("KMP")}
 function move(o,i){const r=o.slice();if(i===10){r[0]++;return r;}const a=Math.floor(i/2),pos=i%2===0,y=r[a+1],d=pos?Number(y<0):Number(y>0);r[a+1]+=pos?1:-1;r[6]+=d*V[a];r[7]+=d*W[a];return r;}
 function source(t,c){return t || ("bB".includes(c)?1:("cC".includes(c)?2:0));}
 function key2(o,q,t){return [...o,q,t].join(",")}
 function decode(s){return s.split(",").map(Number)}
 function summarize(cur,n,w){
   let fibers=new Map(),types=[0,0,0,0],by={};
   for(const key of cur){const a=decode(key),b=a.slice(0,9).join(",");fibers.set(b,(fibers.get(b)||0)|(1<<a[9]));}
   let H0=0;
   for(const [key,mask] of fibers){
     const z=Number(!!(mask&1))+Number(!!(mask&2))+Number(!!(mask&4));types[z]++;
     H0+=1+Number(Boolean((mask&2)&&(mask&5)));
     invariant(mask!==5,`{N,C} without B at ${w} n=${n}`);
     if(z===3){const a=decode(key),s=a[0],q=a[8],k=`${s}/${q}`;by[k]=(by[k]||0)+1;}
   }
   const allowed=w==="aab"?[0,1,2]:[0,1];
   let T=0;
   for(let s=0;s<=1;s++)for(let q of allowed){
     const actual=by[`${s}/${q}`]||0, expected=choose(n+1-s-q,5);
     invariant(actual===expected,`${w} n=${n} s=${s} q=${q}: ${actual} != ${expected}`);T+=expected;
   }
   for(const k of Object.keys(by))invariant(allowed.includes(Number(k.split("/")[1])),"disallowed q");
   invariant(types[3]===T&&cur.size-H0===T,"triple saving identity");
   return {n,base:fibers.size,H0,H1:cur.size,one:types[1],two:types[2],three:T,by,fibers};
 }
 function brute(w,n){
   const mask=new Map();let count=0;
   function visit(o,q,t,len){if(len===n){count++;const k=[...o,q].join(",");mask.set(k,(mask.get(k)||0)|(1<<t));return;}
     for(let i=0;i<10;i++)visit(move(o,i),kmp(q,L[i],w),source(t,L[i]),len+1);
     if(len===0||q===w.length)visit(move(o,10),0,t,len+1);
   }
   visit(Array(8).fill(0),0,0,0);return {mask,count};
 }
 const out=["PREFIX-486 exact reachability and combinatorial-formula certificate","Models: native X6 restricted a/A,b/B,c/C,d/D,e/E plus x; source N/B/C; KMP w=aab or aba","Arithmetic: integers within exact IEEE-754 safe range; counts are reachability sets (not path multiplicities)."];
 const all={};
 for(const w of ["aab","aba"]){
   let cur=new Set([key2(Array(8).fill(0),0,0)]);
   out.push(`GATE=${w}`);
   const rows=[];
   for(let n=0;n<=9;n++){
     const r=summarize(cur,n,w);rows.push(r);
     out.push(`n=${n} base=${r.base} H0=${r.H0} H1=${r.H1} types=${r.one},${r.two},${r.three} triples_by_s/q=${JSON.stringify(r.by)}`);
     if(n<=4){const b=brute(w,n);invariant(b.mask.size===r.fibers.size,`brute size ${w} ${n}`);for(const [k,v] of b.mask)invariant(r.fibers.get(k)===v,`brute mask ${w} ${n}`);out.push(`BRUTE_EXHAUSTIVE n=${n} paths=${b.count} mask_equivalence=PASS`);}
     if(n===9)break;
     const nxt=new Set();
     for(const key of cur){const a=decode(key),o=a.slice(0,8),q=a[8],t=a[9];
       for(let i=0;i<10;i++)nxt.add(key2(move(o,i),kmp(q,L[i],w),source(t,L[i])));
       if(n===0||q===w.length)nxt.add(key2(move(o,10),0,t));
     }
     cur=nxt;
   }
   all[w]=rows;
 }
 for(const n of [6,7,8,9]){
   const a=all.aab[n],b=all.aba[n],diff=a.three-b.three,formula=choose(n-1,5)+choose(n-2,5);
   invariant(diff===formula,`difference ${n}`);out.push(`DIFF n=${n} aab_minus_aba=${diff} exact_formula=${formula}`);
 }
 invariant(all.aab[8].three===286&&all.aba[8].three===259,"inherited n8 data mismatch");
 invariant(all.aab[9].three===637&&all.aba[9].three===560,"new n9 data mismatch");
 out.push("ALL_CHECKS_PASS");return out.join("\n")+"\n";
}
console.log(certificate());
