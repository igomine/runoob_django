from django.shortcuts import render


def runoob(request):
  views_num = 98
  return render(request, "runoob.html", {"num": views_num})
