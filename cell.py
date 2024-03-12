"""file containing the Cell class for conways game of life.
    """
class Cell:
    """a single cell in Conways game of life.

    Returns:
        __str__: an X if it is alive, Blank otherwise.
    """
    _is_alive = False

    @property
    def is_alive(self):
        return self._is_alive

    def __init__(self, is_alive=False):
        self._is_alive = is_alive

    def __str__(self):
        if self._is_alive:
            return "X"
        return " "

    def ressurect(self):
        """sets the _is_alive attribute to True
        """
        self._is_alive = True

    def death(self):
        """sets the _is_alive attribute to False
        """
        self._is_alive = False
