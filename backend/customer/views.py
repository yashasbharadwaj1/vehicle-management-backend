from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from vendor.models import *
#from backend.supabase import get_supabase_connection
from rest_framework.response import Response
from vendor.serializers import VendorSerializer

#supabase_connction = get_supabase_connection()


class ListVendors(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # using orm

        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response({"data": serializer.data})

        # using raw sql query

        # cur = supabase_connction.cursor()
        # cur.execute("SELECT * FROM public.vendor_vendor")
        # rows = cur.fetchall()

        # data = []
        # # print(cur.description)
        # # print(type(cur.description))
        # # (Column(name='id', type_code=20), Column(name='name', type_code=1043), Column(name='details', type_code=1043))
        # # <class 'tuple'>
        # for row in rows:
        #     # each row is a tuple (1, 'tvs', 'vendor details')
        #     row_dict = {}
        #     for i, field in enumerate(cur.description):
        #         field_name = field.name
        #         row_dict[field_name] = row[i]

        #     data.append(row_dict)

        # cur.close()
        # supabase_connction.close()
        # return Response({"data": data})


