# Create your views here.
from django.shortcuts import render,HttpResponse

# def index(request):
   
import json
import facebook


#long lived token till 20th july
#EAAJZARoLHLRYBO9agVkmIygUv5pBZAcfwhkUzmByUDZCMSZAZCa0vyAX0ZBXCZCeNN46mryo18wuMs9HOFncEPWhsmKcIKL5z9xTFwakWkXM5FjVfr0Gf5RiaPknjmQf86kypSXCLOrvoyWo6aF8Cy4aslZAnDNTGCa6PBo0uBY74CgDq2k6uXBL
ACCESS_TOKEN={"EAAJZARoLHLRYBO2JG63xFblvcrq6yJYt8CemPe5g7RUqkWpaKRANbzZAydHZBUjN3WJITKKFrF0L9GufTG2SuplRgxfhfnXW4ZBZBb820XNX39UxfnZAK51ouy7ZCvoe4lUKbrswaqpMtO7uRJaZCDBK3pa8Vv2Sai1fGRttvFlsissyCa1xpCYzbCJ7hULLHzuwjoTSmu4VV2qRkcogt7fP7ReGpwC0UyL2vJzjhcjfMICMdwZCGnrKZBjZBbg9ZCnCqd0ZD"}
def index(request):
    token=ACCESS_TOKEN
    graph=facebook.GraphAPI(token)
    page=graph.get_object('me',fields='id,name, gender,email')

    print("printing page")
    print(type(page))




    print(json.dumps(page,indent=4))
    print(type(json.dumps(page,indent=4)))
    
    
    # return HttpResponse("facebook api text shivam")  
    return HttpResponse(json.dumps(page, indent=4))
  



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