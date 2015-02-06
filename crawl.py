# -*- coding: utf-8 -*-
from zhihu import User
from collections import deque
myfile=open("DirectedGraph.txt", "w");
#max user number “关注关系图”的节点数V
MAXTOT=100;
#起始用户列表
start_url = ["http://www.zhihu.com/people/chenyao-45"]
"""
user = User(user_url)
user_id = user.get_user_id()
followers_num = user.get_followers_num()
followees_num =user.get_followees_num()
asks_num = user.get_asks_num()
answers_num = user.get_answers_num()
collections_num = user.get_collections_num()
agree_num = user.get_agree_num()
thanks_num = user.get_thanks_num()
followees = user.get_followees()
followers = user.get_followers()
asks = user.get_asks()
answers = user.get_answers()
collections = user.get_collections()
"""
recorder=dict();
userque=deque();
for suser in start_url:
        tuser=User(suser);
        userque.append( tuser );
        recorder[suser[28:]]=tuser.get_user_id();
total=len(userque);
num=total;
flag=False;
#DirectedGraph="{"
while num>=1:
	num-=1;
	user=userque.popleft()
	print user.get_user_id()
	followees_num =user.get_followees_num()
	followees = user.get_followees()
	for i in range(1,followees_num+1):
		cuser=followees.next()
		# when total<=MAXTOT,then cuser will be in userque.
		# when total> MAXTOT,we only count users who have appeard in userque.
		if total<=MAXTOT or (total>MAXTOT and (cuser.user_url[28:] in recorder)):
		        myfile.write('{"'+user.user_url[28:]+'","'+cuser.user_url[28:]+'"},')
		if total<=MAXTOT:
			if cuser.user_url not in recorder:
				userque.append(cuser)
				num+=1;
				total+=1;
				recorder[cuser.user_url[28:]]=cuser.get_user_id();
myfile.write('\n\n\n');
st="{";
for url in recorder:
        st+="{0}\"{1}\",\"{2}\"{3},".format("{",str(url),str(recorder[url]),"}");
myfile.write(st[:-1]+'}');

