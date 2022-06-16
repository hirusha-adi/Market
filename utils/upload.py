# Upload Handling

from typing import Union

def allowed_file(filename: Union[str, bytes]):
    if isinstance(filename, bytes):
        filename = filename.decode(encoding='utf-8')
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'bmp', 'webp'}
            