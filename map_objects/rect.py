class Rect:

	def __init__(self, x, y, w, h):
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h

	def center(self):
		return ((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2)

	def intersect(self, other):
		h_intersect = (self.x1 <= other.x2 and self.x2 >= other.x1) or \
			(other.x1 <= self.x2 and other.x2 >= self.x1)
		v_intersect = (self.y1 <= other.y2 and self.y2 >= other.y1) or \
			(other.y1 <= self.y2 and other.y2 >= self.y1)
		return h_intersect and v_intersect