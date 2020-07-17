# -----------------------------------------------------------------------------
# Created: Wed  3 Jun 2020 18:39:27 IST
# Last-Updated: Fri 17 Jul 2020 13:57:30 IST
#
# test_schema.py is part of devinstaller
# URL: https://gitlab.com/justinekizhak/devinstaller
# Description:
#
# Copyright (c) 2020, Justine Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of The MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "software"), to deal
#   in the software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the software, and to permit persons to whom the software is
#   furnished to do so, subject to the following conditions:
#
#   the above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the software.
#
#   the software is provided "as is", without warranty of any kind,
#   express or implied, including but not limited to the warranties of
#   merchantability, fitness for a particular purpose and noninfringement.
#   in no event shall the authors or copyright holders be liable for any claim,
#   damages or other liability, whether in an action of contract, tort or
#   otherwise, arising from, out of or in connection with the software or the use
#   or other dealings in the software.
# -----------------------------------------------------------------------------
import pytest

from devinstaller import exceptions as e
from devinstaller import file_handler as f
from devinstaller import models as m
from devinstaller import schema as s


@pytest.fixture(scope="class")
def expected_schema():
    return f.read("tests/data/schema.yml")


@pytest.fixture(scope="class")
def schema():
    return m.schema()


class TestSchemaValidity:
    def test_top_level(self, expected_schema, schema):
        assert expected_schema["version"] == schema["version"]
        assert expected_schema["author"] == schema["author"]
        assert expected_schema["description"] == schema["description"]
        assert expected_schema["url"] == schema["url"]

    def test_preset_block(self, expected_schema, schema):
        expected_presets = expected_schema["platforms"]["schema"]["schema"]["presets"]
        schema_presets = schema["platforms"]["schema"]["schema"]["presets"]
        assert expected_presets == schema_presets

    def test_platform_info_block(self, expected_schema, schema):
        expected_version = expected_schema["platforms"]["schema"]["schema"][
            "platform_info"
        ]
        schema_version = schema["platforms"]["schema"]["schema"]["platform_info"]
        assert expected_version == schema_version

    def test_modules_block(self, expected_schema, schema):
        expected_apps = expected_schema["platforms"]["schema"]["schema"]["modules"]
        schema_apps = schema["platforms"]["schema"]["schema"]["modules"]
        assert expected_apps == schema_apps

    def test_full(self, expected_schema, schema):
        assert expected_schema == schema


@pytest.fixture
def mocked_system(mocker):
    return mocker.patch("platform.system")


@pytest.fixture
def mocked_version(mocker):
    return mocker.patch("platform.version")


@pytest.fixture
def mocked_mac_ver(mocker):
    return mocker.patch("platform.mac_ver")


class TestGetCurrentPlatform:
    def test_mac(self, mocked_mac_ver, mocked_system, mocked_version):
        expected_response = {"system": "Darwin", "version": "10.10.10"}
        mocked_mac_ver_response = ("10.10.10", ("", "", ""), "x86_64")
        mocked_system.return_value = expected_response["system"]
        mocked_mac_ver.return_value = mocked_mac_ver_response
        response = s.get_current_platform()
        mocked_version.assert_called_once()
        mocked_mac_ver.assert_called_once()
        assert response == expected_response

    def test_others(self, mocked_mac_ver, mocked_system, mocked_version):
        expected_response = {"system": "Linux", "version": "10.14.6"}
        mocked_system.return_value = expected_response["system"]
        mocked_version.return_value = expected_response["version"]
        response = s.get_current_platform()
        mocked_mac_ver.assert_not_called()
        assert response == expected_response


class TestCompareStrings:
    def test_no_arg(self):
        assert s.compare_strings() is False

    def test_one_arg(self):
        assert s.compare_strings("foo") is True

    def test_two_arg(self):
        assert s.compare_strings("foo", "Foo") is True

    def test_negative_arg(self):
        assert s.compare_strings("foo", "bar") is False
