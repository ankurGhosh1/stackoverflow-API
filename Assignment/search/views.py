import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# from rest_framework.throttling import UserRateThrottle, throttle_classes
# from rest_framework import api_view, throttle_classes
# from rest_framework.views import APIView


# Create your views here.

# @throttle_classes([UserRateThrottle,])
def home(request):
    throttle_scope = 'perday'
    return render(request, 'home.html')

def search(request):
    throttle_scope = 'search'
    query = request.GET['query']
    order = request.GET['order']
    pages = request.GET['page']
    pagesize = request.GET['pagesize']
    title = request.GET['title']
    body = request.GET['body']
    view = request.GET['view']
    answer = request.GET['answer']
    url = request.GET['url']
    sort = request.GET['sort']
    accept = request.GET['accept']
    closed = request.GET['closed']
    migrate = request.GET['migrated']
    wiki = request.GET['wiki']
    notice = request.GET['notice']
    fromdate = request.GET['fromdate']
    todate = request.GET['todate']
    mini = request.GET['min']
    maxi = request.GET['max']
    user = request.GET['user']
    tagged = request.GET['tagged']
    nottagged = request.GET['nottagged']

    response = requests.get('https://api.stackexchange.com/2.2/search/advanced?page=' + pages + '&pagesize=' + pagesize + '&fromdate=' + fromdate + '&todate=' + todate + '&order=' + order + '&min=' + mini + '&max=' + maxi + '&sort=' + sort + '&q=' + query + '&accepted=' + accept + '&answers=' + answer + '&body=' + body + '&closed=' + closed + '&migrated=' + migrate + '&notice=' + notice + '&nottagged=' + nottagged + '&tagged=' + tagged + '&title=' + title + '&user=' + user + '&url=' + url + '&views=' + view + '&wiki=' + wiki + '&site=stackoverflow')
    apiResponse = response.json()
    
    allData = []

    for eachtitle in apiResponse['items']:
        allData.append(eachtitle)

    paginator = Paginator(allData, 10)
    pageNumber = request.GET.get('page', 1)
    page = paginator.get_page(pageNumber)
    return render(request, 'search.html', {"eachdata": page, "query": query, "order": order, "page": pages, "pagesize": pagesize, "title": title, "body": body, "view": view, "answer": answer, "url": url, "sort": sort, "accept": accept, "closed": closed, "migrate": migrate, "wiki": wiki, "notice": notice, "min": mini, "maxi": maxi, "user": user, "todate": todate, "fromdate": fromdate, "tagged": tagged, "nottagged": nottagged})