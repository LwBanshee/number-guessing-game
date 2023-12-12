def isCollide(player_x, player_y, upperPipes, lowerPipes):
    if player_y>ground_y-25 or player_y<0:
        game_sounds['hit'].play()
        return True
 
    for pipe in upperPipes:
        pipeHeight = game_images['pipe'][0].get_height()
        if (player_y < pipeHeight + pipe['y']) and (abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            game_sounds['hit'].play()
            return True
 
    for pipe in lowerPipes:
        if (player_y + game_images['player'].get_height() > pipe['y']) and (abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            game_sounds['hit'].play()
            return True
 
    return False
 
 
def getRandomPipe():
    pipeHeight = game_images['pipe'][0].get_height()    
    offset = screen_height/3
    y2 = offset + random.randrange(0, int(screen_height - game_images['base'].get_height() - 1.2*offset))
    pipeX = screen_width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe