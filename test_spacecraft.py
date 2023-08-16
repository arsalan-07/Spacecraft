import unittest
from spacecraft import Spacecraft

class TestSpacecraft(unittest.TestCase):
    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_forward()
        self.assertEqual(spacecraft.get_position(), "(0, 1, 0)")

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_backward()
        self.assertEqual(spacecraft.get_position(), "(0, -1, 0)")

    def test_turn_left(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_left()
        self.assertEqual(spacecraft.get_direction(), 'W')

    def test_turn_right(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_right()
        self.assertEqual(spacecraft.get_direction(), 'E')

    def test_turn_up(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_up()
        self.assertEqual(spacecraft.get_direction(), 'U')

    def test_turn_down(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_down()
        self.assertEqual(spacecraft.get_direction(), 'D')

    def execute_commands(commandSequence):
        spacecraft = Spacecraft()

        for cm in commandSequence:
            if cm == 'f':
                spacecraft.move_forward()
            elif cm == 'b':
                spacecraft.move_backward()
            elif cm == 'l':
                spacecraft.turn_left()
            elif cm == 'r':
                spacecraft.turn_right()
            elif cm == 'u':
                spacecraft.move_up()
            elif cm == 'd':
                spacecraft.move_down()
            else:
                raise ValueError("Invalid command:", cm)

        return spacecraft



if __name__ == '__main__':
    unittest.main()
