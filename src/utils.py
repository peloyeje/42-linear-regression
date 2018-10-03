import csv
import pathlib

def read_csv(path, sep=',', header=True, **kwargs):
    """Reads and parses a CSV file from disk

    Parameters
    ----------
    path: str
        Path to the dataset
    sep: str
        Field delimiter
    header: bool
        Has header ?
    kwargs: other arguments passed to the csv module

    Returns
    -------
    A list of columns (tuples or list depending on header)

    """

    path = pathlib.Path(path)
    if not path.exists():
        raise ValueError('File missing')

    with path.open('r') as f:
        lines = csv.reader(f, delimiter=sep, **kwargs)

        if header:
            # Pop the first line of the file
            columns = next(lines)

        # Transpose rows into columns
        df = zip(*lines)

        if header:
            return list(zip(columns, df))
        else:
            return list(df)
