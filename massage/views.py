from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddMassageSerializer, UpdateMessageSerializer, ListOfMassageSerializer, MassageSerializer
from .models import Messages, Conversation


class Add_massage(APIView):
    def post(self, request):
        massage = AddMassageSerializer(data=request.POST,
                                       context={'user': request.user})
        if massage.is_valid():
            massage.save()
            return Response({'text': 'your massage saved'})

        else:
            return Response({'text': 'please enter valid data'})

    def put(self, request):
        u_massage = UpdateMessageSerializer(data=request.data,
                                            instance=Messages.objects.get(id=request.data['id']),)
        if u_massage.is_valid():
            u_massage.save()
            return Response({'text': 'your massage updated'})
        else:
            return Response({'text': 'please enter valid data'})

    def get(self, request):
        s = ListOfMassageSerializer(data=request.GET)
        if s.is_valid():
            c = Conversation.objects.get(
                id=request.GET['conversation_id']
            )
            messages = Messages.objects.filter(
                conversation=c
            )
            list_of_massage = []
            for massage in messages:
                m = MassageSerializer(massage)
                m = m.data
                list_of_massage.append(m)
            return Response(list_of_massage)
        else:
            return Response({'text': 'please enter valid data'})
