#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;using M=__uint128_t;using Q=uint64_t;
const M FULL=(M(1)<<125)-1;
int bit(M m){return Q(m)?__builtin_ctzll(Q(m)):64+__builtin_ctzll(Q(m>>64));}
int cnt(M m){return __builtin_popcountll(Q(m))+__builtin_popcountll(Q(m>>64));}
struct Row{M mask;array<int,3>def; bool premium;};
vector<Row> all;M planes[15];uint64_t nodes;
vector<M> answer; bool solve(M free,int left,const vector<int>& pool,int premium){
 ++nodes;if(!free)return left==0&&premium==0;
 int deficits[15];for(int i=0;i<15;i++){deficits[i]=2*left-cnt(free&planes[i]);if(deficits[i]<0||deficits[i]>left)return false;}
 int choices[2]={};M seen=0;array<int,125> cv{};array<int,15> cd{};vector<int> next;next.reserve(pool.size());
 for(int ix:pool){const Row&r=all[ix];if(r.mask&~free||(r.premium?premium==0:left==premium))continue;
 if(!deficits[r.def[0]]||!deficits[r.def[1]]||!deficits[r.def[2]])continue;
 ++choices[int(r.premium)];next.push_back(ix);seen|=r.mask;for(M m=r.mask;m;m&=m-1)++cv[bit(m)];for(int d:r.def)++cd[d];
 }
 if(seen!=free||choices[1]<premium||choices[0]<left-premium)return false;
 int fewest=100000, pivot=-1;for(M m=free;m;m&=m-1){int p=bit(m);if(cv[p]<fewest){fewest=cv[p];pivot=p;}}
 for(int d=0;d<15;d++){if(cd[d]<deficits[d])return false;if(deficits[d]==1&&cd[d]<fewest){fewest=cd[d];pivot=125+d;}}
 if(premium==1&&choices[1]<fewest)pivot=140;for(int k:next){auto&r=all[k];if(pivot==140?!r.premium:pivot<125?!(r.mask>>pivot&1):r.def[(pivot-125)/5]!=pivot-125)continue;
 answer.push_back(r.mask);if(solve(free^r.mask,left-1,next,premium-r.premium))return true;answer.pop_back();}
 return false;
}
int main(int argc,char**argv){
 ifstream f(argv[1]),j(argv[2]);int begin=stoi(argv[3]),end=stoi(argv[4]);
 for(int i=0;i<125;i++){planes[i/25]|=M(1)<<i;planes[5+i/5%5]|=M(1)<<i;planes[10+i%5]|=M(1)<<i;}
 int nt;f>>nt;while(nt--){int s,c,n;f>>s>>c>>n;while(n--){Q a,b;f>>a>>b;if(c==557||c==564){M m=(M(b)<<64)|a;Row row{m,{},c==564};
 for(int k=0;k<15;k++){int s=cnt(m&planes[k]);if(s==1)row.def[k/5]=k;else if(s!=2)exit(3);}all.push_back(row);}}}
 int id=0,n=0;Q a,b,c,d,e,h;uint64_t total=0;
 while(j>>a>>b>>c>>d>>e>>h>>n){int idx=id++;if(idx<begin||idx>=end)continue;
 M used=M(a|c|e)|(M(b|d|h)<<64);vector<int>pool;for(int i=0;i<all.size();++i)if(!(all[i].mask&used))pool.push_back(i);
 nodes=0;answer.clear();bool found=solve(FULL^used,n,pool,1);if(found){for(auto m:answer)cerr<<Q(m)<<" "<<Q(m>>64)<<endl;}cout<<idx<<" "<<nodes<<" "<<found<<"\n";
 if(idx%100==0)cout.flush();if(found)return 1;total+=nodes;}
 cerr<<begin<<" "<<min(end,id)<<" nodes "<<total<<endl;
}
