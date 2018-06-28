import random
from map_objects.tile import Tile
from map_objects.rect import Rect


class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tile_map = self.initialize_tile_map()

	def initialize_tile_map(self):

		tile_map = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

		return tile_map

	def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):

		room_lst = []
		no_of_room = 0

		for i in range(max_rooms):
			w = random.randint(room_min_size, room_max_size)
			h = random.randint(room_min_size, room_max_size)

			x = random.randint(0, map_width - w - 1)
			y = random.randint(0, map_height - h - 1)

			new_room = Rect(x, y, w, h)

			for room in room_lst:
				if new_room.intersect(room):
					break
			else:
				self.create_room(new_room)

				new_x, new_y = new_room.center()

				if no_of_room == 0:
					# If this is the first room, we put player into this room
					player.x, player.y = new_room.center()
				else:

					prev_x, prev_y = room_lst[no_of_room - 1].center()

					if random.randint(0, 1) == 1:
						# first move horizontally, then vertically
						self.create_h_tunnel(prev_x, new_x, prev_y)
						self.create_v_tunnel(prev_y, new_y, new_x)

					else:
						# first move vertically, then horizontally
						self.create_v_tunnel(prev_y, new_y, prev_x)
						self.create_h_tunnel(prev_x, new_x, new_y)

				# Lastly, add new room to the list
				room_lst.append(new_room)
				no_of_room += 1

	def is_blocked(self, x, y):
		return self.tile_map[x][y].blocked

	def create_h_tunnel(self, x1, x2, y):
		for x in range(min(x1, x2), max(x1, x2) + 1):
			self.tile_map[x][y].blocked = False
			self.tile_map[x][y].block_sight = False

	def create_v_tunnel(self, y1, y2, x):
		for y in range(min(y1, y2), max(y1, y2) + 1):
			self.tile_map[x][y].blocked = False
			self.tile_map[x][y].block_sight = False

	def create_room(self, room):
		# go through the tiles in the rectangle and make them passable
		for x in range(room.x1 + 1, room.x2):
			for y in range(room.y1 + 1, room.y2):
				self.tile_map[x][y].blocked = False
				self.tile_map[x][y].block_sight = False