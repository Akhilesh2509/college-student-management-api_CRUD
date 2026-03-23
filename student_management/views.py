import json
import re
from django.http import JsonResponse
from .models import College, Student
from django.views.decorators.csrf import csrf_exempt

# create college
@csrf_exempt
def create_college(request):
    if request.method == "POST":
        data = json.loads(request.body)

        college = College.objects.create(
            name=data.get("name"),
            city=data.get("city"),
            address=data.get("address")
        )

        return JsonResponse({"message": "College created"}, status=201)

    return JsonResponse({"error": "Invalid method"}, status=405)

# get all colleges
def get_colleges(request):
    colleges = list(College.objects.values())
    return JsonResponse(colleges, safe=False)

# get single college details
def get_college(request, id):
    try:
        college = College.objects.get(id=id)

        data = {
            "id": college.id,
            "name": college.name,
            "city": college.city,
            "address": college.address
        }

        return JsonResponse(data)

    except College.DoesNotExist:
        return JsonResponse({"error": "College not found"}, status=404)
    
# update college details
@csrf_exempt
def update_college(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)

        try:
            college = College.objects.get(id=id)
        except College.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        college.name = data.get("name", college.name)
        college.city = data.get("city", college.city)
        college.address = data.get("address", college.address)
        college.save()

        return JsonResponse({"message": "Updated"})

    return JsonResponse({"error": "Invalid method"}, status=405)

# delete college
@csrf_exempt
def delete_college(request, id):
    if request.method == "DELETE":
        try:
            college = College.objects.get(id=id)
            college.delete()
            return JsonResponse({"message": "Deleted"})
        except College.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({"error": "Invalid method"}, status=405)

# for POST /students/ to create a new student with validation
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data.get("email")
        phone = data.get("phone")

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"error": "Invalid email"}, status=400)

        # Phone validation (10 digits)
        if not re.match(r"^\d{10}$", phone):
            return JsonResponse({"error": "Invalid phone number"}, status=400)

        student = Student.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            email=email,
            phone=phone,
            college_id=data.get("college_id")
        )

        return JsonResponse({"message": "Student created"}, status=201)

    
# for PUT /students/ to update an existing student
@csrf_exempt
def update_student(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)

        try:
            student = Student.objects.get(id=id)
            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.email = data.get("email", student.email)
            student.phone = data.get("phone", student.phone)
            student.save()
            return JsonResponse({"message": "Updated successfully"})
        
        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

# for DELETE /students/ to delete an existing student
@csrf_exempt
def delete_student(request, id):
    if request.method == "DELETE":

        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Deleted successfully"})
        
        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        

# get single student details
@csrf_exempt
def get_student(request, id):
    try:
        student = Student.objects.get(id=id)
        data = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "phone": student.phone,
            "college": student.college.name
        }
        return JsonResponse(data)

    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
    
# get all students details with search function and pagination
@csrf_exempt
def get_students(request):
    from django.core.paginator import Paginator

    search = request.GET.get('search', '')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 5)

    students = Student.objects.all()

    if search:
        students = students.filter(name__icontains=search)

    paginator = Paginator(students.values(), limit)
    page_obj = paginator.get_page(page)

    return JsonResponse({
        "page": page_obj.number,
        "total_pages": paginator.num_pages,
        "total_records": paginator.count,
        "data": list(page_obj)
    })

