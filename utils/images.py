# Upload Handling

from typing import Optional, Iterable


def get_image_list(
        img1: Optional[str] = None,
        img2: Optional[str] = None,
        img3: Optional[str] = None
):
    result = []
    for img in (img1, img2, img3):
        try:
            if str(img).lower().startswith('http'):
                result.append(img)
        except:
            continue
    return result


def get_options_list(
    options: Optional[Iterable[str]] = None
):
    result = []
    for option in options:
        try:
            if option in ('AIR CONDITION', 'POWER STEERING', 'POWER MIRROR',
                          'POWER WINDOW', 'Electrcity', 'Water'):
                result.append(str(option))
        except:
            continue
    return result
