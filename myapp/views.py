from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class GoodMorningView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"morning.html")


class HelloWorldView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"helloworld.html")
    

class GoodAfternoonView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"afternoon.html")
    

class GoodEveningView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")
    
class GoodNightView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"night.html")
    
class HowAreYouView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"howareyou.html")
    
class NiceToMeetYouView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"meet.html")
    


class SelfIntroView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"intro.html")

class BatchInfoView(View):

    def get(self,request,*args,**kwargs):
        data={"batch_name":"python november","student_count":45,"faculty":"sajay"}
        return render(request,"batchinfo.html",data)
    
class CourseInfoView(View):

    def get(self,request,*args,**kwargs):
        data={"course_name":"python django","duration":6,"fee":35000}
        return render(request,"course.html",data)

class SachinInfoView(View):

    def get(self,request,*args,**kwargs):
        data={"name":"sachin","place":"mumbai","age":35}
        return render(request,"sachin.html",data)
    

class DhoniInfoView(View):

    def get(self,request,*args,**kwargs):
        data={"name":"dhoni","place":"mumbai","age":40}
        return render(request,"dhoni.html",data)
