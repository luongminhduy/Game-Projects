# level_map = [
# '                                                                                          ',
# '  $      $             $                                                                  ',
# '  C K     E    T                                                                          ',
# ' XX K   XXX          XXX                                                                  ',
# ' XXP                     K                                        XXXXX                   ',
# ' XXXX         XX        XX                       X                                        ',
# ' XXX    X   XXXX   XX                         X                                           ',
# '       XX   XXXX   XX  XX              C   X                 XXXXX                        ',
# '    XXXXX   XXXXX  XX  XXX            XXX                XXXXXXXXX                        ',
# 'XXXXXXXXX   XXXXX  XX  XXX      XXX                     XXXXXXXXXX         XXXXXX         ']

level_map =[
'                          ' * 4 + ' ' + 'X'*4,
'  $       K   $$          ' * 4 + ' ' + 'X'*4,
'P    XX            $   E  ' + '                        T ' * 3 + ' ' + 'X'*4,
'XX       $     XX    XXX  ' * 4 + ' ' + 'X'*4,
'XXX   E  XX   E XX      X ' * 4 + ' ' + 'X'*4,
'$   XXX     XXX      XX   ' * 4 + ' ' + 'X'*4,
' XX      X       XX     X ' * 4 + ' ' + 'X'*4,
'XXXXX   XX      XXXXC  XX ' * 4 + ' ' + 'X'*4,
'XXXXXXX XXXX  XXXXXXXX  X ' * 4 + ' ' + 'X'*4
]


tile_size = 64
screen_width = 1180
screen_height = len(level_map) * tile_size
player_speed = 5
player_gravity = 0.8
player_jump_speed = -20
animation_speed = 0.15

