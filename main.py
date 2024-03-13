from conway import ConwaysGameOfLife

if __name__ == '__main__':
    game = ConwaysGameOfLife(150, 30)
    game.random_activation()
    game.run()
