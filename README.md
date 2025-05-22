# lumber-board-foot-calculator

A simple Python 3.11+ script to compute board-feet and cost per board-foot from a CSV file.

## Usage

```bash
python board_foot_calculator.py --file path/to/load.csv
python board_foot_calculator.py --file path/to/load.csv --summary  # totals only
```

The CSV must contain `Dimension` and `Price` columns. `Dimension` uses the format
`TxWxL` where thickness **T** and width **W** are inches and length **L** is in feet.
Board feet are calculated as `(T × W × L) / 12`.

See `examples/sample_load.csv` for an example input.

