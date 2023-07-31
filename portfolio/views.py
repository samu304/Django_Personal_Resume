from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs, Details, Skills

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    about = Details.objects.all()
    skills = Skills.objects.all()
    context = {'about':about,'skills':skills}
    return render(request, 'about.html',context)

def service(request):
    return render(request, 'services.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphone = request.POST.get('phone')
        fdesc = request.POST.get('message')
        query = Contact(name=fname,email=femail,phone=fphone,description=fdesc)
        query.save()
        
        messages.info(request, 'Thank you for contacting me!')
        return redirect('contact_page')
    
    return render(request, 'contact.html')

def blog(request):
    posts = Blogs.objects.all()
    context = {'posts':posts}
    return render(request, 'blog.html',context)
