from django.shortcuts import render
import math

def calculator(request):
    result = None

    if request.method == "POST":
        number = float(request.POST.get("number"))
        operation = request.POST.get("operation")

        if operation == "square":
            result = number ** 2

        elif operation == "sqrt":
            result = math.sqrt(number)

        elif operation == "sin":
            result = math.sin(math.radians(number))

        elif operation == "cos":
            result = math.cos(math.radians(number))

        elif operation == "tan":
            result = math.tan(math.radians(number))

        elif operation == "log":
            result = math.log10(number)

    return render(request, "calculator.html", {
    "result": result
})                                
# Create your views here.
