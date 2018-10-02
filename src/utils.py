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
    A dict or a list of rows depending on header

    Examples
    --------

    """

    path = pathlib.Path(path)
    if not path.exists():
        raise ValueError('File missing')

    with path.open('r') as f:
        lines = csv.reader(f, delimiter=sep, **kwargs)

        if header:
            columns = next(lines)

        # Transpose rows into columns
        df = list(map(list, zip(*lines)))

        if header:
            return list(zip(columns, df))
        else:
            return df
