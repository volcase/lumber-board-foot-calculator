import subprocess
import sys
import unittest

from board_foot_calculator import calc_board_feet, parse_dimension


class TestCalculator(unittest.TestCase):
    def test_parse_dimension(self):
        self.assertEqual(parse_dimension("2x4x8"), (2.0, 4.0, 8.0))

    def test_calc_board_feet(self):
        self.assertAlmostEqual(calc_board_feet(2, 4, 8), 64 / 12)

    def test_cli_output(self):
        result = subprocess.check_output(
            [sys.executable, "board_foot_calculator.py", "--file", "examples/sample_load.csv"],
            text=True,
        )
        self.assertIn("Total board-feet: 21.33", result)

    def test_summary_flag(self):
        result = subprocess.check_output(
            [
                sys.executable,
                "board_foot_calculator.py",
                "--file",
                "examples/sample_load.csv",
                "--summary",
            ],
            text=True,
        )
        self.assertIn("Total board-feet: 21.33", result)
        self.assertIn("Total cost: $14.75", result)
        self.assertNotIn("2x4x16", result)


if __name__ == "__main__":
    unittest.main()

