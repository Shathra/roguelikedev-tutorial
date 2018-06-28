import libtcodpy as libtcod


def render_all(con, entity_lst, game_map, screen_width, screen_height, color_table):

	for y in range(game_map.height):
		for x in range(game_map.width):
			wall = game_map.tile_map[x][y].block_sight

			if wall:
				libtcod.console_set_char_background(con, x, y, color_table.get("dark_wall"), libtcod.BKGND_SET)
			else:
				libtcod.console_set_char_background(con, x, y, color_table.get("dark_ground"), libtcod.BKGND_SET)


	# Draw all entities in the list
	for entity in entity_lst:
		draw_entity(con, entity)

	libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entity_lst):
	for entity in entity_lst:
		clear_entity(con, entity)

def draw_entity(con, entity):
	libtcod.console_set_default_foreground(con, entity.color)
	libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
	# Erase the character that represents this object
	libtcod.console_put_char(con, entity.x, entity.y, " ", libtcod.BKGND_NONE)
