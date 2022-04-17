from datetime import datetime
from os import stat, utime

from info.gianlucacosta.eos.core.io.files import get_modification_datetime, get_size_in_mb
from info.gianlucacosta.eos.core.io.files.temporary import Uuid4TemporaryPath


class TestGetModificationTime:
    def test_for_inexisting_file(self):
        with Uuid4TemporaryPath(".gianlucacosta.info") as temp_path:
            assert get_modification_datetime(temp_path) is None

    def test_for_existing_file(self):
        with Uuid4TemporaryPath(".gianlucacosta.info") as temp_path:
            with open(temp_path, "w") as temp_file:
                temp_file.write("Hello! ^__^")

            file_stat = stat(temp_path)

            expected_modification_time = datetime(1986, 4, 29, 3, 50, 7, 5)
            utime(
                temp_path,
                times=(
                    file_stat.st_atime,
                    expected_modification_time.timestamp(),
                ),
            )

            assert get_modification_datetime(temp_path) == expected_modification_time


class TestGetSizeInMb:
    def test_for_inexisting_file(self):
        with Uuid4TemporaryPath(".gianlucacosta.info") as temp_path:
            assert get_size_in_mb(temp_path) is None

    def test_for_existing_file(self):
        with Uuid4TemporaryPath(".gianlucacosta.info") as temp_path:
            with open(temp_path, "w") as temp_file:
                temp_file.write("X" * 2 * 1024 * 1024)

            assert get_size_in_mb(temp_path) == 2.0
