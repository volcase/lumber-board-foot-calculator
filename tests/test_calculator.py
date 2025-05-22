import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

from board_foot_calculator import parse_dimension, calc_board_feet


class CalculatorTests(unittest.TestCase):
    def test_parse_dimension(self):
        self.assertEqual(parse_dimension('2x4x8'), (2.0, 4.0, 8.0))

    def test_calc_board_feet(self):
        self.assertEqual(calc_board_feet(2, 4, 8), 64 / 12)

    def test_cli_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / 'load.csv'
            csv_path.write_text('Dimension,Price\n2x4x16,6.0\n')
            result = subprocess.check_output(
                [sys.executable, 'board_foot_calculator.py', '--file', str(csv_path)],
                text=True,
            )
            self.assertIn('Total board-feet: 10.67', result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
