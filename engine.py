import libtcodpy as libtcod
from input_handler import handle_key
from entity import Entity
from render_functions import render_all, clear_all
from map_objects.game_map import GameMap

def main():
	screen_width = 80
	screen_height = 50
	map_width = 80
	map_height = 45

	room_max_size = 10
	room_min_size = 6
	max_rooms = 30

	color_table = {
		"dark_wall": libtcod.Color(0, 0, 100),
		"dark_ground": libtcod.Color(50, 50, 150)
	}

	player_x = screen_width // 2
	player_y = screen_height // 2
	player = Entity(player_x, player_y, char="@", color=(255, 255, 255))

	npc = Entity(player_x - 5, player_y - 5, char="@",
		color = libtcod.yellow)

	entity_lst = [player, npc]

	libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

	libtcod.console_init_root(screen_width, screen_height, "Title", False)

	con = libtcod.console_new(screen_width, screen_height)

	game_map = GameMap(map_width, map_height)
	game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

	key = libtcod.Key()
	mouse = libtcod.Mouse()

	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

		render_all(con, entity_lst, game_map, screen_width, screen_height, color_table)

		libtcod.console_flush()

		clear_all(con, entity_lst)

		# key = libtcod.console_check_for_keypress()
		action = handle_key(key)

		move = action.get("move")
		exit = action.get("exit")
		fullscreen = action.get("fullscreen")

		if move:
			dx, dy = move
			if not game_map.is_blocked(player.x + dx, player.y + dy):
				player.move(*move)

		# if key.vk == libtcod.KEY_ESCAPE:
		if exit:
			return True

		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == "__main__":
	main()