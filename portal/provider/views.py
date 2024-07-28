from django.views.generic import TemplateView
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
def calculations(request):
    result=0
    return result

def downloadPdf(request):

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Report")

    p.showPage()
    p.save()

    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    return response