from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .forms import TestcasedetailForm, NewUserForm, TestcasedetailCreateForm
from .models import *
from .serializers import *


# Create your views here.

class moduleapi(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModulSerializer


class testcaseapi(viewsets.ModelViewSet):
    queryset = Testcase.objects.all()
    serializer_class = TestcaseSerializer


class testcasedetailapi(viewsets.ModelViewSet):
    queryset = Testcasedetail.objects.all()
    serializer_class = TestcasedetailSerializer


class clientapi(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


def single_slug(request, single_slug):
    tescase = [t.testcase_slug for t in Testcase.objects.all()]
    if single_slug in tescase:
        matching_teststep = Testcasedetail.objects.filter(testcase__testcase_slug=single_slug)
        return render(request, "testcase_detail.html",
                      {'matching_teststep': matching_teststep, 'single_slug': single_slug})


def index_view(request):
    return render(request, "index.html")


def home_view(request):
    modules = Module.objects.all()
    testcases = Testcase.objects.all()
    modules_no = Module.objects.count()
    clients_no = Client.objects.count()
    context = {'modules': modules, 'testcases': testcases, 'modules_no': modules_no, 'clients_no': clients_no}
    return render(request, "home.html", context)


def load_clients(request):
    module_id = request.GET.get('module')
    print(module_id)
    clients = Client.objects.filter(module_id=module_id).order_by('client_name')
    return render(request, 'module_dropdown_list_options.html', {'clients': clients})


def load_testcases(request):
    client_id = request.GET.get('client')
    print(client_id)
    testcases = Testcase.objects.filter(client_id=client_id)
    return render(request, 'load_testcase.html', {'testcases': testcases})


def updateStep(request, single_slug, pk):
    item = get_object_or_404(Testcasedetail, pk=pk)
    if request.method == "POST":
        form = TestcasedetailForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('single_slug', single_slug)
    else:
        form = TestcasedetailForm(instance=item)
        return render(request, 'edit_teststep.html', {'form': form,'pk':pk})


def createOrder(request, single_slug):
    form = TestcasedetailCreateForm
    if request.method == "POST":
        form = TestcasedetailCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single_slug', single_slug)
    context = {'form': form}
    return render(request, 'create_step.html', context=context)


def deleteStep(request, single_slug, pk):
    testCaseDetail = Testcasedetail.objects.get(Test_Step_Id=pk)
    if request.method == "POST":
        testCaseDetail.delete()
        return redirect('single_slug', single_slug)
    context = {'item': testCaseDetail,'single_slug':single_slug}
    return render(request, 'delete.html', context)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    return render(request, 'register.html', {'form': form})


def logout_from_app(request):
    logout(request)
    messages.info(request, f"successfully logout!")
    return redirect("homepage")


def login_app(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"successfully login")
                return redirect("homepage")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")
    form = AuthenticationForm
    return render(request, 'login.html', {'form': form})
