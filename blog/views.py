from django.shortcuts import render, HttpResponse, redirect
import json
from datetime import datetime, date


# from date import date


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.
def index(request):
    # print(request, "哈哈哈")
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(request, "user_list.html")


from blog.models import Department, Story, Works, Image


def user_add(request):
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='IT部')
    # Department.objects.create(title='运营部')
    # c = request.META.items()
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    a = []
    data_list = Department.objects.order_by("-id")[:3]
    for data in data_list:
        b = {'id': data.id, 'title': data.title}
        a.append(b)
    data = {
        "code": 200,
        "data": a,
        "msg": "请求成功"
    }
    res = HttpResponse(json.dumps(data))
    res['Content-Type'] = 'application/json'
    return res


def something(request):
    print(request.method, request.GET, request.POST)
    # query = request.GET
    # print(query.json)
    # return HttpResponse("返回内容")
    # return render(request, "user_list.html", {"title": "来了"})
    return redirect("http://www.baidu.com")


from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def add_story(request):
    if request.method != 'POST':
        return HttpResponse("请求错误！")
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')
    time_tuple = time.localtime(time.time())
    time01 = time.mktime(time_tuple)
    tuple02 = time.localtime(time01)
    date_time_now = time.strftime("%Y-%m-%d %H:%M:%S", tuple02)
    date_now = time.strftime("%Y-%m-%d", tuple02)
    a = Story.objects.filter(date_now=date_now, ip=ip)
    count = 0
    for item in a:
        count = count + 1
    if count >= 3:
        data = {
            "code": 4433,
            "msg": "每天只能发布3次！"
        }
        res = HttpResponse(json.dumps(data))
        res['Content-Type'] = 'application/json'
        return res

    name = request.POST.get("name")
    content = request.POST.get("content")
    Story.objects.create(name=name, content=content, date_time_now=date_time_now, date_now=date_now, ip=ip)
    res = HttpResponse('发布成功')
    return res


def index_story(request):
    if request.method != 'GET':
        return HttpResponse("请求错误！")
    data_list = []
    story_data = Story.objects.order_by("-id")[:3]
    for item in story_data:
        items = {'id': item.id, 'name': item.name, 'content': item.content, 'time': item.date_time_now}
        data_list.append(items)
    data = {
        "code": 200,
        "data": data_list,
        "msg": "请求成功"
    }
    res = HttpResponse(json.dumps(data, cls=DateEncoder))
    res['Content-Type'] = 'application/json'
    return res


def index_works(request):
    if request.method != 'GET':
        return HttpResponse("请求错误！")
    data_list = []
    works_data = Works.objects.order_by("-id")[:6]
    for item in works_data:
        items = {'id': item.id, 'name': item.name, 'src': item.src, 'href': item.href, 'time': item.time}
        data_list.append(items)
    data = {
        "code": 200,
        "data": data_list,
        "msg": "请求成功"
    }
    res = HttpResponse(json.dumps(data, cls=DateEncoder))
    res['Content-Type'] = 'application/json'
    return res


def index_image(request):
    if request.method != 'GET':
        return HttpResponse("请求错误！")
    data_list = []
    image_data = Image.objects.order_by("-id")[:10]
    for item in image_data:
        items = {'id': item.id, 'url': item.url}
        data_list.append(items)
    data = {
        "code": 200,
        "data": data_list,
        "msg": "请求成功"
    }
    res = HttpResponse(json.dumps(data, cls=DateEncoder))
    res['Content-Type'] = 'application/json'
    return res


def story(request):
    if request.method != 'GET':
        return HttpResponse("请求错误！")
    data_list = []
    story_data = Story.objects.order_by("-id")
    for item in story_data:
        items = {'id': item.id, 'name': item.name, 'content': item.content, 'time': item.date_time_now}
        data_list.append(items)
    data = {
        "code": 200,
        "data": data_list,
        "msg": "请求成功"
    }
    res = HttpResponse(json.dumps(data, cls=DateEncoder))
    res['Content-Type'] = 'application/json'
    return res
