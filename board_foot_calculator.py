import argparse
import csv
from dataclasses import dataclass

@dataclass
class Record:
    dimension: str
    price: float
    board_feet: float
    cost_per_bf: float


def parse_dimension(dim: str) -> tuple[float, float, float]:
    t, w, l = dim.lower().split('x')
    return float(t), float(w), float(l)


def calc_board_feet(t: float, w: float, l: float) -> float:
    return (t * w * l) / 12


def read_records(path: str) -> list[Record]:
    records: list[Record] = []
    with open(path, newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            t, w, l = parse_dimension(row['Dimension'])
            price = float(row['Price'])
            bf = calc_board_feet(t, w, l)
            records.append(
                Record(row['Dimension'], price, bf, price / bf)
            )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description='Lumber board-foot calculator')
    parser.add_argument('--file', required=True, help='CSV with Dimension and Price')
    parser.add_argument('--summary', action='store_true', help='Print only totals')
    args = parser.parse_args()
    recs = read_records(args.file)
    total_bf = sum(r.board_feet for r in recs)
    total_cost = sum(r.price for r in recs)
    if not args.summary:
        for r in recs:
            print(f"{r.dimension}: {r.board_feet:.2f} bf @ ${r.cost_per_bf:.2f}/bf")
    print(f"Total board-feet: {total_bf:.2f}")
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == '__main__':
    main()
