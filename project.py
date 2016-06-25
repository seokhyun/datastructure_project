def parent(n):
	return (n-1)/2

def left(n):
	return 2*n+1

def right(n):
	return 2*n+2


def heapify(A,i,heapsize):
	l=left(i)
	r=right(i)
	if l<heapsize and A[l]>A[i]:
		largest =l
	else:
		largest=i
	if r<heapsize and A[r]>A[largest]:
		largest=r
	if largest!=i:
		A[i], A[largest]=A[largest],A[i]
		heapify(A,largest,heapsize)

def build_a_heap(A):
	for i in range(len(A)//2,0,-1):
		heapify(A,i-1,len(A))
def heapsort(A):
	build_a_heap(A)
	for i in range(len(A),1,-1):
		A[i-1],A[0]=A[0],A[i-1]
		heapify(A,0,i-1)







def print_menu():
	
	print("0. Read data files")
	print("1. display statistics")
	print("2. Top 5 most tweeted words")
	print("3. Top 5 most tweeted users")
	print("4. Find users who tweeted a word (e.g.)")
	print("5. Find all people who are friends of the above users")
	print("6. Delete users who mentioned a word")
	print("7. Delete all users who mentioned a word")
	print("8. Find strongly connected components")
	print("9. Find shortest path from a given user")
	print("99. Quit")



class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []
    def create_queue(self,sz):
        self.sz = sz
        self.buf = list(range(sz))  # malloc(sizeof(int)*sz)
    def enqueue(self,val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz
    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res
    def is_empty(self):
        return self.front == self.rear
WHITE = 0
GRAY = 1
BLACK = 2





def count_linked_list(a):
	i=0
	while a !=None:
		i=i+1
		a=a.next
	return i
class User_word_node:
	def __init__(self):
		self.num=0
		self.date=None
		self.word=None
		self.next=None
		self.linked_list_num=0




class User_friend_node:
	def __init__(self):
		self.me=None
		self.friend=None
def get_count(word_count_tuple):
	return word_count_tuple[1]
def making_word_dic(word_list):##making dictionary for counting
	word_dic={}
	for word_info in word_list:
		if (word_info.word in word_dic):
			word_dic[word_info.word]=word_dic[word_info.word]+1
		else:
			word_dic[word_info.word]=1
	items = sorted(word_dic.items(), key=get_count, reverse=True)
	return items

	


def menu_0():
	file_user=open("user.txt")
	i=0
	user_list=[] ##making user_list
	
	for line in file_user:
		line = line[0:-1]
		if((i%4)==0):
			user=User_node()
			user.num=(line)
		if((i%4)==1):
			user.date=(line)
		if((i%4)==2):
			user.id_eng=(line)
			user_list.append(user)
		i=i+1

	file_word=open("word.txt")
	i=0
	user_word_list=[] ##making word_list
	for line in file_word:
		line = line[0:-1]
		if((i%4)==0):
			user=User_word_node()
			user.num=(line)
		if((i%4)==1):
			user.date=(line)
		if((i%4)==2):
			user.word=(line)
			user_word_list.append(user)
		i=i+1
	top_word_dic=making_word_dic(user_word_list)

	file_friend=open("friend.txt")
	i=0
	user_friend_list=[] ##making friend_list
	for line in file_friend:
		line = line[0:-1]
		if((i%3)==0):
			user=User_friend_node()
			user.me=(line)
		if((i%3)==1):
			user.friend=(line)
			user_friend_list.append(user)
		i=i+1





	a=[user_list,user_word_list,user_friend_list,top_word_dic]
	return a

def menu_1(a):
	
	print("total_users =",len(a[0]))
	print("total_tweets=",len(a[1]))
	print("total_friendship=",len(a[2]))
	user_list=a[0]

	user_word_list=a[1]
	for word in user_word_list:			#word in wordlist
		for user in user_list:			#user in userlist
			if(word.num == user.num):
				user.add_word(word)	#if two of them are same
	
	user_list=sorted(user_list,key=sorting_key_for_menu3,reverse=True)
	total=0
	for user in user_list:
		print(count_linked_list(user.tweet_word_by_user))

		total=total+count_linked_list(user.tweet_word_by_user)
	Average=total/len(user_list)
	print("Average tweets per user:", Average)
	print("Minium tweets per user: ",count_linked_list(user_list[-1].tweet_word_by_user))
	print("Maximum tweets per user: ",count_linked_list(user_list[0].tweet_word_by_user))



def menu_2(items):
	items=items[3]
	for item in items[:5]:##print top5 words
		print(item[0], item[1])

def sorting_key_for_menu3(user):
	
	return count_linked_list(user.tweet_word_by_user) 
def menu_3(a):
	user_list=a[0]
	user_word_list=a[1]
	for word in user_word_list:			#word in wordlist
		for user in user_list:			#user in userlist
			if(word.num == user.num):
				user.add_word(word)	#if two of them are same
	
	user_list=sorted(user_list,key=sorting_key_for_menu3,reverse=True)
	print("top 5 most tweeted user")
	for user in user_list[:5]:
		print (user.num)
		print(count_linked_list(user.tweet_word_by_user))
		print("")

def menu_4(a):
	user_word_list=a[1]
	user_word_list_only_word=[]
	for i in user_word_list:
		user_word_list_only_word.append(i.word)
	print("Find users who tweeted a word")
	searching_word=input("word is :")
	for i in range(len(user_word_list_only_word)):
		if searching_word == user_word_list_only_word[i]:
			print (user_word_list[i].num)

def menu_5(a):
	user_friend_list=a[2]##friend number two of them giving point=me, getting point =friend
	user_list=a[0]#user information
	making_friend_adj_list(user_list,user_friend_list)
	print_user_friend(user_list)

	
	

def menu_6(a):#delete user who mentioned a word
	user_friend_list=a[2]
	user_list=a[0]
	user_word_list=a[1]
	top_word_dic=a[3]
	print("Delete users who mentioned a word")
	delete_word_input= input("word:")
	user_word_list_only_word=[]
	user_who_mention_a_word=[]
	for i in user_word_list:
		user_word_list_only_word.append(i.word)#put only word in the list
	for i in range(len(user_word_list_only_word)):
		if delete_word_input == user_word_list_only_word[i]:#if they are same
			
			if(delete_word_input not in user_who_mention_a_word):
				
				user_who_mention_a_word.append(user_word_list[i].num) 
	user_who_mention_a_word=list(set(user_who_mention_a_word))
	j=0
	for i in user_who_mention_a_word:
		print(j,i)
		j=j+1

	
	delete_user_number=input("choose the member you want to delete from 0 to %d:"%(j-1))
	delete_user_number=int(delete_user_number)
	
	for i in user_list:
		if i.num==user_who_mention_a_word[delete_user_number]:
			user_list.remove(i)
	print("The user who mentioned a word is deleted")


def menu_7(a):
	user_friend_list=a[2]
	user_list=a[0]
	user_word_list=a[1]
	top_word_dic=a[3]
	print("Delete all users who mentioned a word")
	delete_word_input= input("word:")
	user_word_list_only_word=[]
	user_who_mention_a_word=[]
	for i in user_word_list:
		user_word_list_only_word.append(i.word)#put only word in the list
	for i in range(len(user_word_list_only_word)):
		if delete_word_input == user_word_list_only_word[i]:#if they are same
			
			if(delete_word_input not in user_who_mention_a_word):
				
				user_who_mention_a_word.append(user_word_list[i].num) 
	user_who_mention_a_word=list(set(user_who_mention_a_word))
	for j in user_who_mention_a_word:
		print(j)
	for i in user_list:
		for j in user_who_mention_a_word:
			if i.num ==j:
				user_list.remove(i)

	print("all user who mentioned a word is deleted")




def menu_9(a):##not finished
	user_friend_list=a[2]##friend number two of them giving point=me, getting point =friend
	user_list=a[0]#user information
	i=0#put all the number from 0-181
	for user in user_list:
		user.n_bfs=i
		i=i+1
	user_n_bfs_dic={}
	for user in user_list:
		user_n_bfs_dic[user.num]=user.n_bfs
		
	for user in user_list:
		print (user.num, user_n_bfs_dic[user.num])

	for user in user_list:
		for friend in user_friend_list:
			if(user.num==friend.me):	
				user.add_friend(friend.friend)

	for user in user_list:
		print(user.num ,"'s friend")
		p=user.friend
		while p !=None:
			if p.num in user_n_bfs_dic:
				print(p.num , user_n_bfs_dic[p.num])

			p=p.next
		print("-----------------------------------")
	bfs(user_list, user_list[0],user_n_bfs_dic)
	#for user in user_list:
		
	#	for user in user_list:
	#		print(user.num ,"'s friend")
	#		p=user.friend
	#		while p !=None:
	#			print(p.num)

	#			p=p.next
	#	print("-----------------------------------")





def bfs(vertices, s,user_n_bfs_dic):

    for u in vertices:
        if u.n_bfs != s.n_bfs:
            u.color = WHITE
            u.d = 1E10
            u.parent = -1
    s.color = GRAY
    s.d = 0
    s.parent = -1
    
    q = Queue()
    q.create_queue(len(vertices))
    q.enqueue(s.n_bfs)        # enquque node number
    while not q.is_empty():
        u = q.dequeue()   # node number
        adj_v = vertices[u].friend

        while adj_v:
            if vertices[user_n_bfs_dic[adj_v]].color == WHITE:
                vertices[user_n_bfs_dic[adj_v]].color = GRAY   # gray
                vertices[user_n_bfs_dic[adj_v]].d = vertices[u].d + 1
                vertices[user_n_bfs_dic[adj_v]].parent = u
                q.enqueue(user_n_bfs_dic[adj_v])
            adj_v = adj_v.next
        vertices[u].color = BLACK           # black



class DepthFirstSearch:
    def __init__(self):
        self.time = 0;
        self.vertices = None
        self.user_n_dfs_dic=None
    def set_vertices(self,vertices,user_n_dfs_dic):
        self.vertices = vertices
        for i in range(len(self.vertices)):
            self.vertices[i].n_dfs = i
        self.user_n_dfs_dic=user_n_dfs_dic
    def dfs(self):
        for u in self.vertices:
            u.color = WHITE
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == WHITE:
                self.dfs_visit(u)
    def dfs_visit(self, u):
        self.time = self.time + 1
        u.d_dfs = self.time
        u.color = GRAY
        v = u.friend#only 242134141
        
        while v:
            if self.vertices[self.user_n_dfs_dic[v.num]].color == WHITE:
                self.vertices[self.user_n_dfs_dic[v.num]].parent = u.num
                self.dfs_visit(self.vertices[self.user_n_dfs_dic[v.num]])
            v = v.next;
        u.color = BLACK
        self.time = self.time + 1
        u.f_dfs = self.time
    def dfs_print(self):
    	for user in self.vertices:
    		print(user.num, user.n_dfs, user.d_dfs, user.f_dfs)
    def dfs_f_sort(self):
    	self.vertices= sorted(self.vertices, key= sorting_key_for_dfs_f_sort, reverse=True)
    	self.dfs_print()

def sorting_key_for_dfs_f_sort(user):
	return user.f_dfs

	

class Adj:
	def __init__(self):

		self.next=None
		self.num=None

class User_node:
	def __init__(self):
		self.num=0
		self.date=None
		self.id_eng=None
		self.tweet_word_by_user=None
		self.friend=None
		self.color = WHITE
		self.parent=-1
		self.d_dfs=0
		self.f_dfs=0
		self.n_dfs=0

	def add_word(self,word):
		new_word=User_word_node()
		new_word.num=word.num
		new_word.date=word.date
		new_word.word=word.word
		new_word.next=self.tweet_word_by_user
		self.tweet_word_by_user=new_word#how many word did he used
	def add_friend(self,friend):
		new_friend=Adj()

		new_friend.num=friend

		new_friend.next=self.friend
		self.friend =new_friend



def menu_8(a):
	user_friend_list=a[2]##friend number two of them giving point=me, getting point =friend
	user_list=a[0]#user information
	i=0#put all the number from 0-181
	for user in user_list:
		user.n_dfs=i
		i=i+1
	user_n_dfs_dic={}
	for user in user_list:
		user_n_dfs_dic[user.num]=user.n_dfs
		
	#for user in user_list:
	#	print (user.num, user_n_dfs_dic[user.num])

	making_friend_adj_list(user_list,user_friend_list)
	#print_user_friend(user_list)
	user_list_transpose=transpose(user_list, user_n_dfs_dic)
	#print_user_friend(user_list_transpose)
	DFS=DepthFirstSearch()
	DFS.set_vertices(user_list,user_n_dfs_dic)
	DFS.dfs()
	#DFS.dfs_print()
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	vertices= DFS.dfs_f_sort()


def transpose(user_list,user_n_dfs_dic):
	user_list1=[]
	for user in user_list:
		x=User_node()
		x.num=user.num
		x.n_dfs=user.n_dfs
		user_list1.append(x)
	
	
	for user in user_list1:
		user.friend=None

	for user in user_list:
		
		p=user.friend
		
		while p:
			if p.num in user_n_dfs_dic:
				user_list1[user_n_dfs_dic[p.num]].add_friend(user.num)
			p=p.next


	
	return user_list1



def print_user_friend(user_list):
	for user in user_list:
		print(user.num ,"'s friend")
		p=user.friend
		while p !=None:
			print(p.num)

			p=p.next
		print("-----------------------------------")
def making_friend_adj_list(user_list, user_friend_list):
	for user in user_list:
		for friend in user_friend_list:
			if(user.num==friend.me):	
				user.add_friend(friend.friend)	

def print_user(user_list,n_bfs):
	print(user_list[n_bfs].num)
	print(user_list[n_bfs].color)
	print(user_list[n_bfs].parent)
	p=user_list[n_bfs].friend
	while p:
		print(user_list[p.n_bfs].num)
		p=p.next
	print("")






def main():
	print_menu()
	
	menu_input=input("Select Menu:")
	menu_input = int(menu_input)
	if(menu_input==0):
		a=menu_0()
	if(menu_input==2):
		menu_2(a[2])


a=menu_0()
menu_8(a)
#menu_2(a)
#menu_4(a)






