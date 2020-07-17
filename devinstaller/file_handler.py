# -----------------------------------------------------------------------------
# Created: Mon 25 May 2020 15:40:37 IST
# Last-Updated: Fri 17 Jul 2020 14:22:59 IST
#
# file_handler.py is part of devinstaller
# URL: https://gitlab.com/justinekizhak/devinstaller
# Description: Handles everything file related
#
# Copyright (c) 2020, Justin Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of The MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "software"), to deal in the software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the software, and to permit
# persons to whom the software is furnished to do so, subject to the
# following conditions:
#
# the above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the software.
#
# the software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and noninfringement.
# in no event shall the authors or copyright holders be liable for any claim,
# damages or other liability, whether in an action of contract, tort or
# otherwise, arising from, out of or in connection with the software or the
# use or other dealings in the software.
# -----------------------------------------------------------------------------

"""Handles everything file_handler"""
import re

import anymarkup


def read(file_path: str) -> dict:
    """Reads the file at the path and returns the data as dict object

    Args:
        file_path: The path to the file

    Returns:
        Python object

    Raises:
        ValueError: If the anymarkup syntax is invalid
    """
    with open(file_path, "r") as stream:
        try:
            return anymarkup.parse(stream)
        except Exception:
            raise ValueError(
                "Couln't load up your devfile. Somethings wrong with your anymarkup syntax"
            )


def download(url: str) -> dict:
    """Downloads file from the internet

    Args:
        url: Url of the file

    Returns:
        Python object
    """
    # TODO


def parse_and_download(input_str: str) -> dict:
    """Checks the input_str and downloads or reads the file.

    Steps:
        1. Extract the method: `file` or `url`
        2. If file then expand the file path and stores it for checking dependency cycle and downloads the file
        3. If url the stores the it for checking the dependency cycle
        4. Either way reads the file and returns the object.

    Args:
        input_str: path to file. Follows the spec format

    Returns:
        Python dict
    """
    # TODO Write the function to parse and download the file
    # Make sure to expand the path.

    pattern = r"^(url|file): (.*)"
    result = re.match(pattern, input_str)
    method = result.group(1)
    function = {"file": read, "url": download}
    full_path = result.group(2)
    data = function[method](full_path)
    return data
