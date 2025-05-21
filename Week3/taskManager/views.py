from django.shortcuts import render, redirect
from django.http import Http404

valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def landingPage(request):
    days_list = [{'day': day.capitalize()} for day in valid_days]
    return render(request, 'index.html', {"days": days_list})

def dayView(request, day_name):
    day_name = day_name.lower()
    if day_name not in valid_days:
        raise Http404("Invalid day")

  
    tasks = request.session.get(day_name, [])

    if request.method == "POST":
        if 'task' in request.POST:
            new_task_text = request.POST.get("task").strip()
            if new_task_text:
                tasks.append({"task": new_task_text, "done": False})
        else:
            
            for i in range(len(tasks)):
                tasks[i]["done"] = f"check_{i}" in request.POST
        

        request.session[day_name] = tasks
        request.session.modified = True
        return redirect(f"/{day_name}/")

    return render(request, 'day.html', {
        "day": day_name.capitalize(),
        "tasks": tasks

    
    })
