from django.shortcuts import render

# Create your views here.
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader('./templates/pyecharts/templates'))
print('*'*100, CurrentConfig.GLOBAL_ENV.loader.searchpath)


from pyecharts import options as opts
from pyecharts.charts import Bar


def job_page(request):
    return render(request, 'job_position.html')


def index(request):
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return HttpResponse(c.render_embed())


def echarts(request):
    return render(request, 'analysis.html')
