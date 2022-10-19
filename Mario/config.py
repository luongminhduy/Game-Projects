level_map = [
'                           ',
'                           ',
'                           ',
' XX     XXX          XXX   ',
' XX P                      ',
' XXXX         XX        XX ',
' XXX    X   XXXX   XX      ',
'       XX   XXXX   XX  XX  ',
'    XXXXX   XXXXX  XX  XXX ',
'XXXXXXXXX   XXXXX  XX  XXX ']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
player_speed = 8
player_gravity = 0.8
player_jump_speed = -16
animation_speed = 0.15