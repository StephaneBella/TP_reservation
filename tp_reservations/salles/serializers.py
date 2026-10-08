"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from .permissions import IsOwnerOrReadOnly

from .models import Reservation, Salle  

# TODO : votre code ici
class SalleSerializer(serializers.ModelSerializer):
      class Meta:
            model = Salle
            fields = ['nom', 'capacite', 'batiment']



class ReservationSerializer(serializers.ModelSerializer):
      utilisateur = serializers.ReadOnlyField(source='utilisateur.username')

      class Meta:
            model = Reservation
            fields = ['salle', 'utilisateur', 'debut', 'fin', 'motif', 'statut', 'cree_le']
            read_only_fields = ['utilisateur', 'cree_le']
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

      def validate(self, attrs):
          pass
