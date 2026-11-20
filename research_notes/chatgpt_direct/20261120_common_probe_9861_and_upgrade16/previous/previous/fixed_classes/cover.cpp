#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;
int at(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
struct Row{M m;int price;};
vector<Row> trail;long long leaves=0,nodes=0;
bool cover(M f,int k,int slack,const vector<Row>& rows){
 ++nodes;if(k==0)return f==0;
 if(k==1){for(auto r:rows)if(r.m==f&&r.price<=slack){++leaves;for(auto &t:trail)cout<<W(t.m)<<" "<<W(t.m>>64)<<" ";cout<<W(r.m)<<" "<<W(r.m>>64)<<"\n";}return false;}
 vector<Row>active;array<int,125>d{},cheap;cheap.fill(100000000);M reach=0;
 for(auto r:rows)if(!(r.m&~f)&&r.price<=slack){active.push_back(r);reach|=r.m;for(M a=r.m;a;a&=a-1){int x=at(a);d[x]++;cheap[x]=min(cheap[x],r.price);}}
 if(reach!=f)return false;
 int pivot=at(f),sum=0;
 for(M a=f;a;a&=a-1){int x=at(a);if(d[x]<d[pivot])pivot=x;sum+=cheap[x];}
 if(sum>10*slack)return false;
 for(auto r:active)if(r.m&(M(1)<<pivot)){int left=sum;for(M a=r.m;a;a&=a-1)left-=cheap[at(a)];
 if(left>10*(slack-r.price))continue;trail.push_back(r);
 if(cover(f^r.m,k-1,slack-r.price,active))return true;trail.pop_back();}
 return false;
}

int main(int argc,char**argv){
 ifstream in(argv[1]),wf(argv[2]);int budget=stoi(argv[3]),shard=stoi(argv[4]),stride=stoi(argv[5]);int w[126];
 for(int &v:w)wf>>v;W l,h;int size,cost;vector<Row> all;M full=0;
 while(in>>l>>h>>size>>cost){M m=(M(h)<<64)|l;int weight=0;for(M a=m;a;a&=a-1)weight+=w[at(a)];int rc=1000*cost-weight;if(rc<0)return 2;all.push_back({m,rc});full|=m;}
 int total=0;for(M p=full;p;p&=p-1)total+=w[at(p)];
 int slack=budget*1000-total;vector<Row> rows;array<int,125>deg{};
 for(auto r:all)if(r.price<=slack){rows.push_back(r);for(M b=r.m;b;b&=b-1)deg[at(b)]++;}
 int point=at(full);for(M b=full;b;b&=b-1)if(deg[at(b)]<deg[point])point=at(b);
 vector<Row> first;for(auto r:rows)if(r.m&(M(1)<<point))first.push_back(r);
 sort(first.begin(),first.end(),[](Row a,Row b){return a.price<b.price;});
 cerr<<point<<" "<<first.size()<<" "<<rows.size()<<" "<<slack<<endl;long long done=0;
 for(int i=shard;i<(int)first.size();i+=stride){auto r=first[i];trail={r};
 if(cover(full^r.m,8,slack-r.price,rows)){for(auto v:trail)cout<<W(v.m)<<" "<<W(v.m>>64)<<"\n";return 0;}
 ++done;if(done%100==0)cerr<<done<<" "<<nodes<<endl;}
 cerr<<"done "<<done<<" "<<nodes<<endl;
}