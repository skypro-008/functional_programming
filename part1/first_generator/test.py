import sys
import unittest
from pathlib import Path
import os
from types import GeneratorType
from collections import Iterable

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase, StdoutCapturing  # noqa: E402


class IterTestCase(SkyproTestCase):
    def test_iter_works_correct(self):
        with StdoutCapturing() as func_output:
            import main

        self.assertTrue(
            isinstance(main.gen, GeneratorType),
            "%@Проверьте что переменная gen является генератором",
        )

        self.assertTrue(
            isinstance(main.it, Iterable),
            "%@Проверьте что переменная it является итератором",
        )

        self.assertTrue(
            func_output == ["1", "2", "3", "1", "2", "3"],
            "%@Проверьте что вывели в терминал три первых элемента массива с помощью "
            "функции iter и 3 первых элемента массива с помощью функции arr_generator",
        )

        self.assertTrue(
            next(main.it) == 4 and next(main.gen) == 4,
            "%@Проверьте что вывели в терминал три первых элемента массива с помощью "
            "переменной iter и 3 первых элемента массива с переменной arr_generator с "
            "помощью функции next",
        )


if __name__ == "__main__":
    unittest.main()
