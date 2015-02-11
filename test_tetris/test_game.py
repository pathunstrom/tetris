import logging
import tetris.game as game
import time


def test_constants():
    try:
        I = game.I
        J = game.J
        L = game.L
        O = game.O
        S = game.S
        T = game.T
        Z = game.Z
    except Exception:
        print("Constants test failure.")
        logging.exception("Constants test failure.")
        return True
    print "Constants tests passed"


def test_node():
    try:
        node = game.Node(3, 2)
        assert node.x == 3
        assert node.y == 2
        assert node.color is None
    except Exception:
        print "Node test failure."
        logging.exception("Node test failure.")
        return True
    print "Node tests passed"


def test_tableau():
    try:
        tableau = game.Tableau()
        for y, row in enumerate(tableau.model):
            for x, node in enumerate(row):
                assert node.x == x
                assert node.y == y
                assert node.color is None
    except Exception:
        print "Tableau test failure"
        logging.exception("Tableau test failure")
        return True
    print "Tableau tests passed"


def test_tetromino_I():
    try:
        table = game.Tableau()
        tetromino = game.Tetromino(game.I, table)
        assert tetromino.x == 3
        assert tetromino.y == 22
        assert tetromino.rotation == 0
        tetromino.clockwise()
        assert tetromino.rotation == 1
        tetromino.counterclockwise()
        assert tetromino.rotation == 0
        tetromino.left(1)
        assert tetromino.x == 2
        tetromino.left(3)
        assert tetromino.x == 0
        tetromino.clockwise()
        tetromino.left()
        assert tetromino.x == -1
        tetromino.left()
        assert tetromino.x == -2
        tetromino.left()
        assert tetromino.x == -2
    except Exception:
        print "Tetromino I test failed"
        logging.exception("Tetromino test failed")
        return True
    print "Tetromino I tests passed"


def test_speed(function1, function2, loops=1000, *args, **kwargs):
    f1_start = time.time()
    for x in xrange(loops):
        function1(*args, **kwargs)
    f1_total = time.time() - f1_start

    f2_start = time.time()
    for x in xrange(loops):
        function2(*args, **kwargs)
    f2_total = time.time() - f2_start

    report = "{func} runtime: {runtime}"
    print(report.format(func=function1.__name__, runtime=f1_total))
    print(report.format(func=function2.__name__, runtime=f2_total))
    report = "{func} is faster over {loops} loops by {diff}."
    if f1_total < f2_total:
        func = function1
        diff = f2_total - f1_total
    else:
        func = function2
        diff = f1_total - f2_total
    print(report.format(func=func, diff=diff, loops=loops))


if __name__ == "__main__":
    tests = [test_constants, test_node, test_tableau, test_tetromino_I]
    tests_start_time = time.time()
    success = 0
    failure = 0
    for test in tests:
        start_test = time.time()
        failed = test()
        test_time=time.time() - start_test
        if failed:
            failure += 1
        else:
            success += 1
        print "Test completed in {} seconds.".format(test_time)
    total_time = time.time() - tests_start_time
    print "{} Tests completed in {} seconds.".format(len(tests), total_time)
    print "{} tests passed. {} tests failed.".format(success, failure)