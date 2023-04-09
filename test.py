import requests

BASE = "http://127.0.0.1:5000/"
# data= [{"likes": 78, "name":"Tutorial1","views": 100},
#         {"likes": 1000, "name":"Tutorial2","views": 50000},
#         {"likes": 35, "name":"Tutorial3","views": 100},]

# for i in range(len(data)):
#      response= requests.put(BASE + "video/" + str(i) , data[i])
#      print(response.json())

# input()
# response= requests.get(BASE + "video/1")
# print(response.json())

response= requests.patch(BASE + "video/2", {"views" : 99, "likes": 101})
print(response.json())


