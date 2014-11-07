import threading
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from async.processor import Processor


@csrf_protect
def request_handler(request):
    if request.is_ajax() and request.method == 'POST':
        if "count" in request.POST and request.POST["count"]:
            count = int(request.POST["count"])
        else:
            count = 1
        processor = Processor()
        thread = threading.Thread(target=processor.process, args=(count,))
        thread.start()
        return render_to_response(
            "index.html",
            {},
            context_instance=RequestContext(request),
        )
    else:
        return render_to_response(
            "index.html",
            {},
            context_instance=RequestContext(request),
        )