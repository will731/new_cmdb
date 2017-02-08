#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author:Eric.xin
"""
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(parentdir)


from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required



def index(request):
    return render_to_response('base/index.html',locals(),context_instance=RequestContext(request))



