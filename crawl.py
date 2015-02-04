# -*- coding: utf-8 -*-
from zhihu import User
from collections import deque
#max user number “关注关系图”的节点数V
MAXTOT=200;
#change 'qheldiv' to your desired username，把qheldiv换成你希望的起始用户名
firstuser_url = "http://www.zhihu.com/people/qheldiv"
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
userque=deque()
userque.append(User(firstuser_url))
recorder=dict()
total=1;
num=1;
flag=False;			
with open("DirectedGraph.txt", "w") as myfile:
	myfile.write("{")
#DirectedGraph="{"
while num>=1:
	num-=1;
	user=userque.popleft()
	print user.get_user_id()
	followees_num =user.get_followees_num()
	followees = user.get_followees()
	for i in range(1,followees_num):
		cuser=followees.next()
		# when total<=MAXTOT,then cuser will be in userque.
		# when total> MAXTOT,we only count users who have appeard in userque.
		if total<=MAXTOT or (total>MAXTOT and cuser.user_url in recorder):
			with open("DirectedGraph.txt", "a") as myfile:
 			   myfile.write('<"'+user.user_url[28:]+'","'+cuser.user_url[28:]+'">,')
		if total<=MAXTOT:
			if cuser.user_url not in recorder:
				userque.append(cuser)
				num+=1;
				total+=1;
				recorder[cuser.user_url]=True;
#DirectedGraph=DirectedGraph[:-1]+"}"
