# -----------------------------------------------------------------------------
# Created: Wed  3 Jun 2020 19:06:45 IST
# Last-Updated: Tue 21 Jul 2020 21:34:27 IST
#
# exceptions.py is part of devinstaller
# URL: https://gitlab.com/justinekizhak/devinstaller
# Description: All the exceptions
#
# Copyright (c) 2020, Justine Kizhakkinedath
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

"""Houses all the custom exceptions in the app
"""

spec_errors = {
    "S100": "Your devfile is not a valid.",
    "S101": "There was an error parsing the `file_path` statement",
}

dev_errors = {"D100": "Schema object not found."}


class SpecificationError(Exception):
    """Exception when there is a violation of the Specification.

    These errors are unique to the specification. All programs implementing devinstaller
    specification raises the same error.
    """

    def __init__(self, error: str, error_code: str = "S100", message: str = "") -> None:
        self.error = error
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        response = (
            f"\nErrors: { self.error }"
            f"\nI found a violation of code {self.error_code}."
            f"\n{self.error_code}: {spec_errors[self.error_code]}"
            f"\n{ self.message }"
        )
        return response


class DevinstallerError(Exception):
    """Exception when there is a runtime error.

    These errors are unique to the implementaion of devinstaller runtime.
    """

    def __init__(self, error: str, error_code: str, message: str = "") -> None:
        self.error = error
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        response = (
            f"\nErrors: { self.error }"
            f"\nI found a violation of code {self.error_code}."
            f"\n{self.error_code}: {dev_errors[self.error_code]}"
            f"\n{ self.message }"
        )
        return response


class ModuleRollbackFailed(Exception):
    pass


class ModuleInstallationFailed(Exception):
    pass
