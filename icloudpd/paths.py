"""Path functions"""
import os
import re
from icloudpd import constants


def local_download_path(media, size, download_dir):
    """Returns the full download path, including size"""
    filename = filename_with_size(media, size)
    download_path = os.path.join(download_dir, filename)
    return download_path


def filename_with_size(media, size):
    """Returns the filename with size, e.g. IMG1234.jpg, IMG1234-small.jpg"""
    # Strip any non-ascii characters.
    filename = media.filename
    match = re.match(constants.MATCH_RE, filename)
    if not match:
        version = media.versions[size if size in ["original"] else "original"]
        photo_size = version["size"]
        photo_size_suffix = "-%s." % photo_size
        if not (photo_size_suffix in filename):
            filename = photo_size_suffix.join(filename.rsplit(".", 1))
    filename = filename.encode("utf-8").decode("ascii", "ignore")
    if size == 'original':
        return filename
    return ("-%s." % size).join(filename.rsplit(".", 1))
