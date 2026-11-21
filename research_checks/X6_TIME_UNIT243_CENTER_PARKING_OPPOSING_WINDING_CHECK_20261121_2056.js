// X6 native C12 plus relative anchor P, two intact labeled triads.
// Exact finite certificate; conditional signed-Port/target-empty law only.
const e=(i,s=1)=>Array.from({length:6},(_,j)=>i===j?s:0);
const a=[e(0),e(1),e(2),e(0,-1),e(1,-1),e(2,-1)];
const x=Array(13);for(let r=0;r<6;r++){x[2*r]=a[r];x[2*r+1]=a[r].map((v,i)=>v+a[(r+1)%6][i]);}x[12]=Array(6).fill(0);
const unique=new Set(x.map(v=>v.join(',')));if(unique.size!==13)throw Error('cell collision');
const edges=Array.from({length:13},()=>[]);
function edge(u,v,delta,kind){const d=x[v].map((n,i)=>n-x[u][i]);const nz=d.map((n,i)=>[i,n]).filter(p=>p[1]!==0);if(nz.length!==1||Math.abs(nz[0][1])!==1)throw Error('not native axis');edges[u].push({v,delta,kind,axis:nz[0][0]+1,sign:nz[0][1]});}
for(let q=0;q<12;q++){edge(q,(q+1)%12,1,'ring');edge(q,(q+11)%12,-1,'ring');if(q%2===0){edge(q,12,0,'spoke');edge(12,q,0,'spoke');}}
const steps=[['A',0,12],...Array.from({length:12},(_,k)=>['B',(2+k)%12,(3+k)%12]),['A',12,0],['B',2,12],...Array.from({length:12},(_,k)=>['A',(12-k)%12,(11-k)%12]),['B',12,2]];
const pos={A:0,B:2},wind={A:0,B:0};let ring=0,spoke=0;
for(const [who,u,v] of steps){if(pos[who]!==u||Object.values(pos).includes(v))throw Error('occupancy');const E=edges[u].find(z=>z.v===v);if(!E)throw Error('non-native');pos[who]=v;wind[who]+=E.delta;if(E.kind==='ring')ring++;else spoke++;}
if(steps.length!==28||ring!==24||spoke!==4||pos.A!==0||pos.B!==2||wind.A!==-12||wind.B!==12)throw Error('witness failure');
const key=s=>s.join(',');const start=[0,2,0,0],goal=key([0,2,-12,12]);const visited=new Map([[key(start),0]]),queue=[start];let qi=0,shortest=null;const layers=[1];
while(qi<queue.length){const s=queue[qi++],depth=visited.get(key(s));if(key(s)===goal){shortest=depth;break;}
for(let who=0;who<2;who++)for(const E of edges[s[who]]){if(E.v===s[1-who])continue;const t=s.slice();t[who]=E.v;t[2+who]+=E.delta;if(Math.abs(t[2+who])>12)continue;const k=key(t);if(!visited.has(k)){visited.set(k,depth+1);layers[depth+1]=(layers[depth+1]||0)+1;queue.push(t);}}}
if(shortest!==28)throw Error('minimality failed '+shortest);
const answer={schema:'X6_TIME_UNIT243_CENTER_PARKING_CERT_V1',conditional:true,source_pin:'a72226e2430ffa4786321ac86e7f0c599d5f0389',cells:13,directed_edges:36,ring_edges:24,spoke_edges:12,initial_final:{A:0,B:2},ring_windings:{A:-12,B:12},shortest_steps:shortest,ring_events:ring,center_spoke_events:spoke,bfs_visited:visited.size,bfs_states_depth_le_27:layers.slice(0,28).reduce((a,b)=>a+(b||0),0),bfs_states_depth_28:layers[28],depth_layers_0_to_28:layers.slice(0,29),failures:0};
console.log(JSON.stringify(answer,null,2));
