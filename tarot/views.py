# Create your views here.
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TarotCard
from .serializers import TarotCardSerializer

@api_view(['GET'])
def draw_card(request):
    cards = TarotCard.objects.all()
    card = random.choice(cards)
    is_upright = random.choice([True, False])
    
    data = {
        'card': TarotCardSerializer(card).data,
        'position': '正位' if is_upright else '逆位',
        'meaning': card.upright_meaning if is_upright else card.reversed_meaning
    }
    return Response(data)