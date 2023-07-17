from translit.cases import Case
from translit.converters.translit_cyr_taras_to_lat import convert as convert_cyr_taras_to_lat

"""
Converter functions map
"""
converters = {
    Case.CYR_TARAS + "_TO_" + Case.LAT: convert_cyr_taras_to_lat,
}


def convert(text, source_case, target_case):
    """
    Convert function select implementation based on source and target cases.
    """
    return converters[source_case + '_TO_' + target_case](text)