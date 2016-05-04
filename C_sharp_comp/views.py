from django.shortcuts import render, render_to_response
import os
import sys
import subprocess
# Create your views here.
from django.template import RequestContext


def submit_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        f = open('code_C_sharp.cs','r+')
        f.truncate()
        f.write(code)
        f.close()

        #compile this code_C_sharp.cs and run it store output in string ans
        os_env_dir = os.path.expanduser('~')
        path_req = ''
        filename = 'code_C_sharp.cs'
        filepath = path_req + filename
        test =  subprocess.Popen(["gmcs", filepath], stdout=subprocess.PIPE)
        output1 = test.communicate()[0]
        filename = 'code_C_sharp.exe'
        filepath = path_req+filename
        if os.path.exists(filepath):
            #print "file found at " + filepath
            test =  subprocess.Popen(["mono", filepath], stdout=subprocess.PIPE)
            output = test.communicate()[0]
            ans = output
            os.remove(filename)
        else:
            #error occured in compilation
            ans = output1


        variables = RequestContext(request,{
            'output': ans
        })
        return render_to_response('main_page.html',variables)

    return render_to_response('main_page.html',RequestContext(request))