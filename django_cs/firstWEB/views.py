from django.http import HttpResponse
from django.shortcuts import render

from .models import cal
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, '自定义.html')
    # return HttpResponse('ok')

def calpage(request):
    return render(request, 'cal.html')
    # return HttpResponse('ok')

def deal_date1(request):
    if request.POST:
        v_a = request.POST["valueA"]
        v_b = request.POST["valueB"]
        print("成功2")
        print(v_a, v_b)
        result = int(v_a) + int(v_b)

        cal.objects.create(value_a=v_a, value_b=v_b, result=result)

        return render(request, 'result.html', context={'data': result})  # data对应到resquest.html的data内部
    else:
        return HttpResponse("请通过 calpage/ 节点来进入返回页面")


def calList(request):
    data = cal.objects.all() #获取定义的cal表全部的信息
    for i in data: #这里打印了所有已储存的表的信息
        print(i.value_a,i.value_b,i.result)

    return render(request,'list.html',context ={"data":data}) #这里是一个字典的返回

def del_data(request):
    cal.objects.all().delete()
    print("已进行清库操作!")
    return HttpResponse("已进行清库操作")
