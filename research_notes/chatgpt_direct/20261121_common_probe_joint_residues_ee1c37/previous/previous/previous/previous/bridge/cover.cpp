#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
int sz(M x){return __builtin_popcountll(U(x))+__builtin_popcountll(U(x>>64));}int cap;
M bad[125][125];array<U,4> obs[125][125];int min_single[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
int price(M m){int ans=0;for(M a=m;a;a&=a-1){array<U,4>w{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)w[j]|=obs[at(a)][at(b)][j];for(U h:w)ans+=__builtin_popcountll(h);}return ans;}
struct Row{M mask;int s,c;};vector<Row> big;int low[14][12][126];long long events,leaves;vector<Row> path;ofstream tails;
void gen(M row,int s,M pool,const M *blocked,int threshold){
 if(s>=threshold)big.push_back({row,s,price(row)});
 while(pool&&s+sz(pool)>=threshold){int p=at(pool);pool&=pool-1;M next=pool&~blocked[p];if(s+1+sz(next)<threshold)continue;M f[125];for(M a=next;a;a&=a-1)f[at(a)]=blocked[at(a)]|bad[at(a)][p];gen(row|(M(1)<<p),s+1,next,f,threshold);}
}
void pack(M free,int n,int k,int base,int top,int start){
 ++events;if(!k){if(!free){cerr<<"SOL "<<base<<"\n";for(auto&r:path){for(M a=r.mask;a;a&=a-1)cerr<<at(a)<<" ";cerr<<"\n";}exit(3);}return;}
 if(n<k||n>k*top||base+low[top][k][n]>cap)return;
 if(n<=k*10&&base+low[10][k][n]<=cap){++leaves;tails<<U(free)<<" "<<U(free>>64)<<" "<<k<<" "<<base<<"\n";}
 int need=max(11,(n+k-1)/k);
 for(int i=start;i<big.size();i++){auto&r=big[i];if(r.s>top||r.mask&~free)continue;if(r.s<need)break;if(base+r.c+low[r.s][k-1][n-r.s]>cap)continue;path.push_back(r);pack(free^r.mask,n-r.s,k-1,base+r.c,r.s,i+1);path.pop_back();}
}
int main(int argc,char**argv){if(argc!=7)return 2;ifstream f(argv[1],ios::binary);f.read((char*)obs,sizeof(obs));array<unsigned char,3> edge;while(f.read((char*)edge.data(),3))do{bad[edge[0]][edge[1]]|=M(1)<<edge[2];}while(next_permutation(edge.begin(),edge.end()));ifstream jobs(argv[2]);int a=stoi(argv[3]),b=stoi(argv[4]);cap=stoi(argv[5]);tails.open(argv[6]);int id=0;string line;
 while(getline(jobs,line)){int j=id++;if(j<a||j>=b)continue;istringstream ss(line);U l,h;int k,c;ss>>l>>h>>k>>c;M free=M(h)<<64|l,none[125]{};int n=sz(free);big.clear();gen(0,0,free,none,max(11,n-13*(k-1)));
 sort(big.begin(),big.end(),[](Row a,Row b){return a.s!=b.s?a.s>b.s:a.mask<b.mask;});
 int prices[14];copy(min_single,min_single+14,prices);for(int s=11;s<=13;s++)prices[s]=99999;for(auto&r:big)prices[r.s]=min(prices[r.s],r.c);
 for(int top=1;top<=13;top++){for(int v=0;v<=k;v++)for(int p=0;p<=n;p++)low[top][v][p]=99999;low[top][0][0]=0;
 for(int v=1;v<=k;v++)for(int p=v;p<=n;p++)for(int s=1;s<=min(p,top);s++)low[top][v][p]=min(low[top][v][p],prices[s]+low[top][v-1][p-s]);}
 events=leaves=0;pack(free,n,k,c,13,0);cout<<j<<" "<<events<<" "<<leaves<<endl;
 }
}
