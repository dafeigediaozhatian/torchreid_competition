#把准确率最高的放到第一个
#如果都只出现一次就按准确率最高的
#否则则按照次数最多的
#

import json

with open("D:\Graduate\strong-baseline\strong-baseline提交/rerank_submission_A.json",'r') as json_max:
    
    json_dict = json.load(json_max)
    
    
    
with open("D:\Graduate\strong-baseline\strong-baseline提交/rerank_submission_A.json",'r') as json_a:
    
    json_ans = json.load(json_a)

with open("D:\Graduate\strong-baseline\strong-baseline提交/rerank_submission_A2.json",'r') as json1:
    
    json_dict1 = json.load(json1)
    
with open("D:\Graduate\strong-baseline\strong-baseline提交/rerank_submission_A150.json",'r') as json2:
    
    json_dict2 = json.load(json2)
    





ans={}




#
#print(json_dict.keys())

#print(json_dict.values())

#print(len(json_dict.keys()))
#
#
    
    
    
for i in json_dict.keys():
    
    print(" ")
    
    print(i)
    
    
    
    
    
    for j in range(0,200):
        
        
#        count.setdefault(json_dict[i][j],0)
#        
#        count[json_dict[i][j]]=count[json_dict[i][j]]+1
#        
#        count[json_dict1[i][j]]=count[json_dict1[i][j]]+1
#        
#        count[json_dict2[i][j]]=count[json_dict2[i][j]]+1
#        
#        
#        print(count)
#        
#        
#        #在这里对每个value进行计数，数值最大的value赋值给新的dict即可
#        
##        count[json_dict[i][0]]++
#        
#        print(json_dict[i][j])
#        
#        print(json_dict1[i][j])
#        
#        print(json_dict2[i][j])
#        
        
        
   
    
        count = {}
    
        print("next")
    
        
#    count.setdefault(json_dict[i][0],0)
#    
#    count.setdefault(json_dict1[i][0],0)
#    
#    count.setdefault(json_dict2[i][0],0)
#    
    
        count[json_dict[i][j]]=0
    

        
        count[json_dict1[i][j]]=0
    
 
        
        count[json_dict2[i][j]]=0
    
                
        print(json_dict[i][j],count[json_dict[i][j]])
    
        print(" ")
    
        print(json_dict1[i][j],count[json_dict1[i][j]])
    
        print(" ")
    
        print(json_dict2[i][j],count[json_dict2[i][j]])
    
        print(" ")
    
    
        
        count[json_dict[i][j]]=count[json_dict[i][j]]+1
    

        
        count[json_dict1[i][j]]=count[json_dict1[i][j]]+1
    
 
        
        count[json_dict2[i][j]]=count[json_dict2[i][j]]+1
    

        
        print(json_dict[i][j],count[json_dict[i][j]])
    
        print(" ")
    
        print(json_dict1[i][j],count[json_dict1[i][j]])
    
        print(" ")
    
        print(json_dict2[i][j],count[json_dict2[i][j]])
    
        print(" ")
    
        print(type(count))
    
    
    
    
    
        print(max(count,key=count.get))
    
#    print(type(json_ans[i][0]))
    
#    
        json_ans[i][j] = max(count,key=count.get)
    
        print(json_ans[i][j])
    

    
#    ans = json.dumps(json_ans)
#    
    
    
with open('D:\Graduate\strong-baseline\strong-baseline提交/ans.json', 'w') as ans:
    
    json.dump(json_ans, ans)    
    
            

    
#
#
##print(len(json_dict.values()))
#
#print(json_dict["296384983.png"][199])
#
#
#print(json_dict["843519641.png"][1])
#print(json_dict["843519641.png"][0])
#
#print(len(json_dict))
    
#for i = 0:199:
#    cmp()
    
    
        
        
        
        
    
 #   print(len(load_dict["843519641.png"]))
    
    
    
    
    
#
#    
#    print(load_dict)
#    
#    print(type(load_dict))
    
#load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
#
#print(load_dict)
#
#with open("D:\Graduate\strong-baseline\strong-baseline提交/rerank_submission_A.json","w") as dump_f:
#    
#    json.dump(load_dict,dump_f)