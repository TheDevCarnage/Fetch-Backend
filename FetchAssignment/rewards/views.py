from rest_framework import viewsets
from rest_framework import generics, status
from .models import Users, Payer
from rest_framework.response import Response
from .serializers import UsersSerializer, PayerSerializer, SpendPointsSerializer, UsersBalanceSerializer


class WelcomeMessageView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        welcome_message = "Welcome to Fetch Assignment Solution!"
        return Response({"message": welcome_message})
    

class UsersViewSet(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return Response(self.get_serializer(instance).data)


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class PayerCreateView(generics.CreateAPIView):
    queryset = Payer.objects.all()
    serializer_class = PayerSerializer

    def create(self, request, *args, **kwargs):
        payer_name = request.data.get('payer_name')
        points_given = int(request.data.get('points_given'))

        user_id = request.data.get('paid_to')  

        try:
            user = Users.objects.get(id=int(user_id))
        except Users.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        payer, created = Payer.objects.get_or_create(payer_name=payer_name, paid_to=user)
        payer.points_given += points_given
        payer.save()

        user.total_points += int(points_given)
        user.save()

        return Response({'message': 'Points added successfully.'}, status=status.HTTP_201_CREATED)
    

class SpendPointsView(generics.CreateAPIView):
    serializer_class = SpendPointsSerializer

    def create(self, request, *args, **kwargs):
        user_id = int(request.data.get('user_id'))
        try:
            
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        total_points = user.total_points

        if total_points <= 0:
            return Response({"error": "User has no points to spend"}, status=status.HTTP_400_BAD_REQUEST)

        payers = Payer.objects.filter(paid_to=user).order_by('paid_at')

        if not payers:
            return Response({"error": "No payers found for the user"}, status=status.HTTP_400_BAD_REQUEST)

        oldest_payer = payers.first()
        points_to_spend = int(self.request.data.get('points_to_spend', 0))

        if points_to_spend <= 0:
            return Response({"error": "Invalid points to spend"}, status=status.HTTP_400_BAD_REQUEST)

        if points_to_spend > total_points:
            return Response({"error": "Insufficient points to spend"}, status=status.HTTP_400_BAD_REQUEST)

        
        user.total_points -= points_to_spend
        user.save()
        oldest_payer.points_given -= points_to_spend
        oldest_payer.save()
        payers_list = [{"Payer":payer.payer_name, "Points": payer.points_given} for payer in payers ]
        response_data = {
            "Message": f"{points_to_spend} Points spent successfully",
            "Payers List": payers_list
        }
        return Response(
            response_data,
            status=status.HTTP_200_OK
        )


class UserPayersBalanceListView(generics.RetrieveAPIView):
    serializer_class = UsersBalanceSerializer
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        
        try:
            user = Users.objects.get(pk=user_id)
            queryset = Payer.objects.filter(paid_to=user)

            if not queryset:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            
            payers = Payer.objects.filter(paid_to=user)
            payers_list = [{"Payer":payer.payer_name, "Points": payer.points_given} for payer in payers ]
            total_balance = user.total_points

            
            message = f"Total balance for user {user.username} is {total_balance} points."

            
            response_data = {
                "message": message,
                "user_id": user_id,
                "total_balance": total_balance,
                "payers": payers_list,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

