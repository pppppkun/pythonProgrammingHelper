import queue
map={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
test=int(input())
for t in range(test):
    expr=input()
    post=[]
    q=queue.LifoQueue()
    for c in expr:
        if c.isdigit() or c.isalpha():
            post.append(c)
        elif c=='(':
            q.put(c)
        elif c==')':
            tmp=q.get()
            while tmp!='(':
                post.append(tmp)
                tmp=q.get()
        else:
            if q.qsize()!=0:
                tmp=q.get()
                while map[tmp]>=map[c]:
                    post.append(tmp)
                    if q.qsize()>0:
                        tmp=q.get()
                    else:
                        break
                else:
                    q.put(tmp)
            q.put(c)
    while q.qsize()>0:
        post.append(q.get())
    print(''.join(post))