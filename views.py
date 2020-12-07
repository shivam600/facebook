# Create your views here.
from django.shortcuts import render,HttpResponse

# def index(request):
   
import json
import facebook


ACCESS_TOKEN={"EAAVrWZCLcZClkBAC4LtUxPnkt9ZAwkM9DvHpz3cZBj6OwcKLNX4EhwXPdJNZAYHLOkWNZBzsnxxNx3SHI7oFalb4N7itnn4ENNqYUlrQrOtQ8beM7Lh8YiROFvKnEZBC7tvXXMMC5J3UrKD0ZBMKuJhAaIoumBvhAvNhUd1EBKS6f5u8rZCF5d0h0GgZCwkhuoAmTvvwnCWQis2RbxVCICUrxH"}
def index():
    token=ACCESS_TOKEN
    graph=facebook.GraphAPI(token)
    page=graph.get_object('me',fields='id,name,talking_about_count,about,picture,likes,country_page_likes,published_posts,photos,unread_message_count,unseen_message_count,new_like_count,unread_notif_count')

    print("printing page")
    print(type(page))




    print(json.dumps(page,indent=4))
    print(type(json.dumps(page,indent=4)))
    
    
    # return HttpResponse("facebook api text shivam")  
    return HttpResponse("facebook api text shivam")
  



if __name__== "__main__":
    index()


# def index(request):
#     return HttpResponse("facebook api text shivam")    

# ,HttpResponse
# from django.shortcuts import render
# return HttpResponse("facebook api text shivam")



# import os
# import json
# import facebook
# from argparse import ArgumentParser

# ACCESS_TOKEN={"EAAVrWZCLcZClkBAHKocilAYfz9oEk9KFiWmSsGzPDSSs65c4XdtQDVjMdtSX4YrOUKtfSm1AbUqC05lpS0wICFeT1THMi2jljT6S8kSOZAapIG5UNrk6sKvflRZAUsBbAY9QF57rfjwUj6bgG9tV2OL1eE5ZB5lTLB5Wlutlevtj4UBzPyJu3X2ytVktnIE9BVGzDdL10M8sEAK7sM4AE"}
# def main():
#     parser=ArgumentParser()
#     parser.add_argument('--page')
#     return parser

# if __name__=='__main__':
#     parser=main()
#     args=parser.parse_args()

#     token= os.environ.get('ACCESS_TOKEN')  
#     # fields=['id',
#     #         'name',


#     #     ]

# graph=facebook.GraphAPI(token)
# page=graph.get_object(args.page)  
# print(json.dumps(page,indent=4))   
# print(type(json.dumps(page,indent=4))) 

