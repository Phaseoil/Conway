from conway import ConwaysGameOfLife

if __name__ == '__main__':
    game = ConwaysGameOfLife()
    game.set_cell(1, 0)
    game.set_cell(1, 2)
    game.set_cell(1, 1)
    game.run()
