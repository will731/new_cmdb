

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from models import *

import datetime
import json
import xlwt

def host_list(request):
    return render_to_response('cmdb/host_list.html',locals())