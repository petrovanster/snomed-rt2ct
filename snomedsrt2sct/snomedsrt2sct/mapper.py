import typing
from .dictionary import dictionary
import itertools


def map(srt_code: str)->typing.Dict[str,str]:
    """
    returns a dict with the SCT code and description as:
    {
        "SCT": "111002",
        "Description": "Parathyroid structure (body structure)"
    }
    """
    code = srt_code.strip()
    for line in dictionary:
        if line["SRT"]==code:
            return line
            
    pass