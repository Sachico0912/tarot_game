# Create your views here.
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TarotCard
from .serializers import TarotCardSerializer
import google.generativeai as genai
from tarot_game import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

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

@api_view(['POST'])
def explain_card(request):
    
    name = request.data.get('name')
    position = request.data.get('position')

    prompt = f"請以塔羅師口吻解釋「{name}（{position}）」這張牌，約 200 字。"

    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)

    return Response({"explanation": response.text})