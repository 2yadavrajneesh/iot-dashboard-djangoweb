from msilib.schema import ListView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Profile, IOTDevice
from django.contrib.auth.models import User
from django.contrib import messages
# import data
data = """
[{
		"deviceid": "0001",
		"latitude": "25.7",
		"longitude": "78.8",
		"devicename": "weatherdatacollector",
		"deviceinstalldate": "15-03-2020",
		"deviceexpirydate": "20-09-2023",
	    "category":  "weather",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh...." ,



		"deviceinfo": [{
				"temperature": "34"
			},
			{
				"humidity": "14"
			},
			{
				"winddirection": "North"
			}

		]

	},
	{
		"deviceid": "0002",
		"latitude": "25.4",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "15-03-2021",
		"deviceexpirydate": "20-09-2023",
		"category":  "smarthome",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "31"
			},
			{
				"humidity": "11"
			},
			{
				"waterlabel": "20"
			}

		]

	},
	{
		"deviceid": "0003",
		"latitude": "25.5",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "15-04-2021",
		"deviceexpirydate": "20-05-2023",
		"category":  "moter",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "30"
			},
			{
				"humidity": "12"
			},
			{
				"waterlabel": "22"
			}

		]

	},
	{
		"deviceid": "0004",
		"latitude": "25.4",
		"longitude": "74.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "14-04-2021",
		"deviceexpirydate": "20-04-2023",
		"category":  "airpump",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "31"
			},
			{
				"humidity": "15"
			},
			{
				"waterlabel": "21"
			}

		]

	},

	{
		"deviceid": "0005",
		"latitude": "25.2",
		"longitude": "75.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "15-10-2021",
		"deviceexpirydate": "20-05-2023",
		"category":  "school",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "35"
			},
			{
				"humidity": "169"
			},
			{
				"waterlabel": "25"
			}

		]

	},
	{
		"deviceid": "0006",
		"latitude": "26.5",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "15-09-2021",
		"deviceexpirydate": "20-08-2023",
		"category":  "smartflat",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "30"
			},
			{
				"humidity": "12"
			},
			{
				"waterlabel": "22"
			}

		]

	},
	{
		"deviceid": "0007",
		"latitude": "29.5",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "13-04-2021",
		"deviceexpirydate": "24-05-2023",
		"category":  "airpump",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "33"
			},
			{
				"humidity": "12"
			},
			{
				"waterlabel": "22"
			}

		]

	},
	{
		"deviceid": "0008",
		"latitude": "26.5",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "29-06-2021",
		"deviceexpirydate": "21-05-2023",
		"category":  "waterpump",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "35"
			},
			{
				"humidity": "12"
			},
			{
				"waterlabel": "65"
			}

		]

	},
	{
		"deviceid": "0009",
		"latitude":"65.5",
		"longitude": "78.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "29-06-2021",
		"deviceexpirydate": "20-06-2023",
		"category":  "moter",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "30"
			},
			{
				"humidity": "12"
			},
			{
				"waterlabel": "22"
			}

		]

	},
	{
		"deviceid": "0010",
		"latitude": "26.5",
		"longitude": "88.1",
		"devicename": "waterlabelcollector",
		"deviceinstalldate": "11-04-2021",
		"deviceexpirydate": "20-11-2023",
		"category":  "park",
        "imageurl": "https://images.google.com/",
		"videourl": "htpp///ddfgfgghgh....",



		"deviceinfo": [{
				"temperature": "35"
			},
			{
				"humidity": "15"
			},
			{
				"waterlabel": "25"
			}

		]

	}
]
"""

def register(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, "Username is taken")
                return render(request, "auth/sign-up.html", )
            if User.objects.filter(email__iexact=email).exists():
                messages.error(request, "Email id already in use.")
                return render(request, "auth/sign-up.html", )
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user)
            messages.success(request, "Sign Up Successfull! ")
            return redirect('login')
        elif request.method == "GET":
            return render(request, "auth/sign-up.html", )
        else:
            return render(request, "auth/sign-up.html", )
    except:
        messages.error(request, "Something went wrong. Please try again.")
        return render(request, "auth/sign-up.html", )


def login_view(request):
    # form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password, end="\n\n", sep=" | ")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                messages.success(request, "Sign in Successful.")
                return redirect('/index')
            messages.success(request, "Sign in Successful.")
            return redirect("/index")

        else:
            messages.error(request, "Username or Password Doesn't match")
            return render(request, "auth/sign-in.html", )
    elif request.method == "GET":
        return render(request, "auth/sign-in.html", )
    else:
        messages.error(request, "Error validating the form")
        return render(request, "auth/sign-in.html", )

import json


@login_required
def index(request):
    # portfolio_list = IOTDevice.objects.all().order_by('-created_date')

    # print(data)
    jsonData = json.loads(data)

    # print(jsonData)
    context = {
        "portfolios": jsonData,
    }
    return render(request, "index.html", context)


@login_required
def addDevice(request):
    if request.method == "POST":
        device_name = request.POST.get("device_name")
        registration_number = request.POST.get("registration_number")
        city = request.POST.get("city")
        IOTRecord = IOTDevice.objects.create(device_name=device_name, city=city,
                                             registration_number=registration_number)
        print('Successfully Created')
        IOTRecord.save()
        return HttpResponseRedirect(reverse('addDevice'))
    return render(request, "device-upload.html")


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        jsonData = json.loads(data)
        listd = []
        try:
            for i in range(len(jsonData)):
                if jsonData[i]['category'] == query:
                    d = jsonData[i]
                    listd.append(json.dumps(d))
            print(listd)
                # print(i)
            # status = IOTDevice.objects.filter(
            #     Q(device_name__icontains=query) | Q(city__icontains=query) | Q(registration_number__icontains=query))
        except:
            return render(request, "search.html")
        context = {
            'all_search_results': listd,
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", context='Not Found')
