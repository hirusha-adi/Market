# Upload Handling

from typing import Optional


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
