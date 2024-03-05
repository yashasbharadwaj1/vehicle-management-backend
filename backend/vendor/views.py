from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import string
import random
from agent.models import *
from agent.serializers import *
from userauths.models import *


def generate_password():
    password_length = 8
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(password_length))
    return password


class AssignQa(views.APIView):
    permission_classes = ((IsAuthenticated),)

    def post(self, request):
        data = request.data
        vendor_id = data.get("vendor_id", None)
        email = data.get("email", None)
        name = data.get("name", None)

        if email is None:
            return Response(
                {"msg": "email is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        elif vendor_id is None:
            return Response(
                {"msg": "vendor_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        elif name is None:
            return Response(
                {"msg": "name is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            password = generate_password()
            qa_queryset = QAGuy.objects.filter(email=email)
            if qa_queryset.exists():
                print("already exists")
                qa_queryset.update(
                    vendor_id=vendor_id, email=email, pass_code=password, name=name
                )
                updated_qa_queryset = QAGuy.objects.filter(email=email)
                serializer = QaSerializer(updated_qa_queryset, many=True)
                if serializer.data:
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors)
            else:
                try:
                    user = User.objects.create(
                        username=name,
                        email=email,
                        type_of_user="qa_agent",
                    )
                    user.set_password(password)
                    user.save() 
                    
                    qa_obj = QAGuy.objects.create(
                        vendor_id=vendor_id, email=email, pass_code=password, name=name
                    )
                    qa_obj.save()

                    serializer = QaSerializer(qa_obj)

                    if serializer.data:
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(
                            serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    return Response(
                        {"error": "An error occurred while processing your request."},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
