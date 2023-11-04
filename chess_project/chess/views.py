from django.http import HttpResponse
import subprocess

def run_chess_game(request):
    # Run your main.py script
    result = subprocess.run(['python', 'chess/main.py'], capture_output=True, text=True)
    game_output = result.stdout
    
    return HttpResponse(game_output)
