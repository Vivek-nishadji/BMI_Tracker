from django.shortcuts import render, redirect
from .forms import BMIForm
from .models import BMIRecord

def bmi_input(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi_record = form.save()
            bmi_record.calculate_bmi()  # Calculate BMI after saving the record
            return redirect('bmi_result', pk=bmi_record.pk)
    else:
        form = BMIForm()

    return render(request, 'bmi_input.html', {'form': form})

def bmi_result(request, pk):
    bmi_record = BMIRecord.objects.get(pk=pk)
    return render(request, 'bmi_result.html', {'bmi_record': bmi_record})