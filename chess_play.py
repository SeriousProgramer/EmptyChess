import unittest

class MiniChess:
    """
    A simplified 5x5 two-player MiniChess implementation with check enforcement.
    White pieces are uppercase, black pieces are lowercase:
       R = Rook, N = Knight, B = Bishop, Q = Queen, K = King, P = Pawn
    """
    
    def __init__(self):
        # Originally: Initialize the board, set starting positions, current player, and castling flags.
        pass

    def print_board(self):
        # Originally: Print the board in a human-readable format with coordinates.
        pass

    def _parse_position(self, pos):
        # Originally: Parse a chess notation string (e.g., "a5") into board indices.
        pass

    def _is_valid_move(self, start, end):
        # Originally: Validate if a move from start to end is legal (including check enforcement).
        pass

    def _valid_castling_move(self, start, end):
        # Originally: Check if a castling move is valid based on board state and movement conditions.
        pass

    def _simulate_castling_rook_move(self, king_start, king_end):
        # Originally: Temporarily move the rook during a castling simulation.
        pass

    def _undo_simulate_castling_rook_move(self, king_start, king_end):
        # Originally: Revert the simulated rook move after castling check simulation.
        pass

    def _square_is_attacked(self, row, col, by_color):
        # Originally: Determine if a square is under attack by any piece of the specified color.
        pass

    def _valid_pawn_move(self, sr, sc, er, ec, piece):
        # Originally: Validate pawn movement including forward moves and captures.
        pass

    def _valid_rook_move(self, row_diff, col_diff, sr, sc, er, ec):
        # Originally: Validate that a rook move is along a straight line with no obstacles.
        pass

    def _valid_bishop_move(self, sr, sc, er, ec):
        # Originally: Validate that a bishop move is diagonal and unobstructed.
        pass

    def _valid_knight_move(self, row_diff, col_diff):
        # Originally: Validate that a knight's move follows the "L" shape.
        pass

    def make_move(self, start, end):
        # Originally: Execute the move from start to end, update board, handle castling and change turns.
        pass

    def _is_in_check(self, color):
        # Originally: Determine if the specified player's king is currently in check.
        pass

    def _can_attack(self, start, end):
        # Originally: Check if the piece at the start position can attack the end position.
        pass

    def is_in_checkmate(self):
        # Originally: Determine if the current player is in checkmate (stubbed as always returning False).
        pass


def main():
    # Originally: Main game loop to run the MiniChess game in console mode.
    pass


class TestMiniChess(unittest.TestCase):
    passed_count = 0
    @classmethod
    def setUpClass(cls):
        # Initialize the counter at 0 before the tests start
        cls.passed_count = 0
    def run(self, result=None):
        """
        Override run so we can print pass/fail for each test method individually.
        """
        if result is None:
            result = self.defaultTestResult()
        super().run(result)
        test_name = self._testMethodName

        # If the current test method is recorded in errors or failures, we say 'failed', else 'passed'
        fails = any(test_name in str(failure[0]) for failure in result.failures)
        errs = any(test_name in str(error[0]) for error in result.errors)
        if fails or errs:
            print(f"{test_name} failed!")
        else:
            print(f"{test_name} passed!")
            TestMiniChess.passed_count += 2

        return result
    @classmethod
    def tearDownClass(cls):
        """
        After all tests have run, display how many have passed out of 32.
        """
        super().tearDownClass()
        print(f"\nYou have passed {cls.passed_count} tests out of 32")


    def test_parse_position(self):
        game = MiniChess()
        self.assertEqual(game._parse_position('a5'), (0, 0))
        self.assertEqual(game._parse_position('e5'), (0, 4))
        self.assertEqual(game._parse_position('a1'), (4, 0))
        self.assertEqual(game._parse_position('e1'), (4, 4))

    def test_valid_pawn_move(self):
        game = MiniChess()
        # White pawn at a2 => (3,0) moving to a3 => (2,0)
        self.assertTrue(game._valid_pawn_move(3, 0, 2, 0, 'P'))
        self.assertFalse(game._valid_pawn_move(3, 0, 1, 0, 'P'))
        self.assertFalse(game._valid_pawn_move(3, 0, 2, 1, 'P'))

    def test_valid_rook_move(self):
        game = MiniChess()
        game.board[2][0] = 'R'
        self.assertTrue(game._valid_rook_move(0, 4, 2, 0, 2, 4))
        game.board[2][2] = 'p'
        self.assertFalse(game._valid_rook_move(0, 4, 2, 0, 2, 4))

    def test_valid_knight_move(self):
        game = MiniChess()
        self.assertTrue(game._valid_knight_move(2, 1))
        self.assertTrue(game._valid_knight_move(-2, 1))
        self.assertTrue(game._valid_knight_move(1, 2))
        self.assertFalse(game._valid_knight_move(2, 2))

    def test_forced_check_removal(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[3][3] = 'K'
        game.board[4][0] = 'N'
        game.board[3][4] = 'r'
        game.current_player = 'W'
        start = (4, 0)
        end = (2, 1)
        self.assertFalse(game._is_valid_move(start, end))
        start_king = (3, 3)
        end_king = (2, 3)
        self.assertTrue(game._is_valid_move(start_king, end_king))

    def test_bishop_blocked(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[2][2] = 'B'
        game.board[1][1] = 'P'
        start = (2, 2)
        end = (0, 0)
        self.assertFalse(game._is_valid_move(start, end))
        game.board[1][1] = '.'
        self.assertTrue(game._is_valid_move(start, end))

    def test_king_cannot_move_into_check(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[2][3] = 'K'
        game.board[0][3] = 'r'
        game.current_player = 'W'
        start = (2, 3)
        end = (1, 3)
        self.assertFalse(game._is_valid_move(start, end))
        game.board[0][3] = '.'
        game.board[0][4] = 'r'
        self.assertTrue(game._is_valid_move(start, end))

    def test_knight_can_jump_over_pieces(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[2][2] = 'N'
        for (rr, cc) in [(2,1), (2,3), (1,2), (3,2)]:
            game.board[rr][cc] = 'P'
        game.current_player = 'W'
        start = (2, 2)
        end = (3, 0)
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        self.assertTrue(game._valid_knight_move(row_diff, col_diff))
        self.assertTrue(game._is_valid_move(start, end))

    def test_cannot_capture_own_piece(self):
        game = MiniChess()
        start = (4, 0)
        end = (3, 0)
        self.assertFalse(game._is_valid_move(start, end))

    def test_out_of_bounds_is_invalid(self):
        game = MiniChess()
        start = (4, 0)
        outsides = [(-1, 0), (5, 0), (4, 5), (4, -1)]
        for end in outsides:
            self.assertFalse(game._is_valid_move(start, end))

    def test_check_detection(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[4][4] = 'K'
        game.board[0][4] = 'r'
        self.assertTrue(game._is_in_check('W'))
        game.board[0][4] = '.'
        self.assertFalse(game._is_in_check('W'))
        game.board[2][2] = 'b'
        self.assertTrue(game._is_in_check('W'))

    def test_make_move_and_switch_player(self):
        game = MiniChess()
        start = (3, 0)
        end = (2, 0)
        self.assertTrue(game._is_valid_move(start, end))
        self.assertEqual(game.current_player, 'W')
        game.make_move(start, end)
        self.assertEqual(game.board[2][0], 'P')
        self.assertEqual(game.board[3][0], '.')
        self.assertEqual(game.current_player, 'B')

    def test_castling_valid(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[4][4] = 'K'
        game.board[4][0] = 'R'
        game.board[4][1] = game.board[4][2] = game.board[4][3] = '.'
        game.white_king_moved = False
        game.white_rook_moved = False
        game.current_player = 'W'
        start = (4, 4)
        end = (4, 2)
        self.assertTrue(game._is_valid_move(start, end))
        game.make_move(start, end)
        self.assertEqual(game.board[4][2], 'K')
        self.assertEqual(game.board[4][3], 'R')

    def test_castling_blocked(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[4][4] = 'K'
        game.board[4][0] = 'R'
        game.board[4][3] = 'P'
        game.white_king_moved = False
        game.white_rook_moved = False
        game.current_player = 'W'
        start = (4, 4)
        end = (4, 2)
        self.assertFalse(game._is_valid_move(start, end))

    def test_castling_through_check(self):
        game = MiniChess()
        for r in range(5):
            for c in range(5):
                game.board[r][c] = '.'
        game.board[4][4] = 'K'
        game.board[4][0] = 'R'
        game.board[4][1] = game.board[4][2] = game.board[4][3] = '.'
        game.white_king_moved = False
        game.white_rook_moved = False
        game.current_player = 'W'
        game.board[0][3] = 'r'
        start = (4, 4)
        end = (4, 2)
        self.assertFalse(game._is_valid_move(start, end))

    def test_castling_after_moved(self):
        game1 = MiniChess()
        for r in range(5):
            for c in range(5):
                game1.board[r][c] = '.'
        game1.board[4][4] = 'K'
        game1.board[4][0] = 'R'
        game1.board[4][1] = game1.board[4][2] = game1.board[4][3] = '.'
        game1.white_king_moved = True
        game1.white_rook_moved = False
        game1.current_player = 'W'
        start = (4, 4)
        end = (4, 2)
        self.assertFalse(game1._is_valid_move(start, end))

        game2 = MiniChess()
        for r in range(5):
            for c in range(5):
                game2.board[r][c] = '.'
        game2.board[4][4] = 'K'
        game2.board[4][0] = 'R'
        game2.board[4][1] = game2.board[4][2] = game2.board[4][3] = '.'
        game2.white_king_moved = False
        game2.white_rook_moved = True
        game2.current_player = 'W'
        self.assertFalse(game2._is_valid_move(start, end))






if __name__ == "__main__":
    # main()
    unittest.main(verbosity = 0)
