class Rect:
    """Class for easy handling of rectangular areas that serve as nodes for the BSP tree.
    Args:
        corners
    """
    def __init__(self, x,y,x2,y2, child_left=None, child_right=None) -> None:
        self.x = x
        self.x2 = x2
        self.y = y
        self.y2 = y2
        self.child_left = child_left
        self.child_right = child_right