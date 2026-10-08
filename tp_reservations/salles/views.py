"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets  # noqa: F401  (a utiliser)

from .models import Reservation, Salle  # noqa: F401  (a utiliser)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime

from .models import Salle, Reservation
from .serializers import SalleSerializer, ReservationSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly

# TODO : votre code ici

class SalleViewSet(viewsets.ModelViewSet):
      queryset = Salle.objects.all()
      serializer_class = SalleSerializer
      permission_classes = [IsAdminUserOrReadOnly]

      @action(detail=True, methods=['get'], url_path='occupation')
      def occupation(self, request, salle_id=None):
            Salle = Salle.objects.get(pk=salle_id)
            current_time = parse_datetime(request.query_params.get('date'))
            reservations = Reservation.objects.filter(
                  salle=Salle,
                  statut=Reservation.Statut.CONFIRMEE,
                  debut__lte=current_time,
                  fin__gte=current_time
            )
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data)

class ReservationViewSet(viewsets.ModelViewSet):
      pass
      
class ReservationPagination(viewsets.ModelViewSet):
      page_size = 10
      page_size_query_param = 'page_size'
      max_page_size = 100



