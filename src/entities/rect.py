class Rect:
    """Class for easy handling of rectangular areas that serve as nodes for the BSP tree.
    Args:
        corners
    """

    def __init__(self, x, y, x_2, y_2, child_left=None, child_right=None) -> None:
        self.x = x
        self.x_2 = x_2
        self.y = y
        self.y_2 = y_2
        self.child_left = child_left
        self.child_right = child_right
