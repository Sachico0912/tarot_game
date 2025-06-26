# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TarotCard
from .serializers import TarotCardSerializer
import random

@api_view(['GET'])
def draw_cards(request):
    all_cards = list(TarotCard.objects.all())

    if len(all_cards) < 3:
        return Response({"error": "塔羅牌資料不足"}, status=400)

    drawn = random.sample(all_cards, 3)
    result = []

    for card in drawn:
        is_upright = random.choice([True, False])
        result.append({
            "card": TarotCardSerializer(card).data,
            "position": "正位" if is_upright else "逆位",
            "meaning": card.upright_meaning if is_upright else card.reversed_meaning
        })

    return Response(result)