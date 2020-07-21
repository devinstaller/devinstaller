import pytest

from devinstaller import app
from devinstaller import models as m


@pytest.fixture
def mock_questionary(mocker):
    return mocker.patch("questionary.checkbox")


def test_ask_user_for_req_list(mock_questionary, mocker):
    module_objects = [
        m.Module(
            name="foo",
            module_type="app",
            alias="foo alias",
            display="Foo as displayed",
            description="Foo description",
        ),
        m.Module(
            name="bar", module_type="app", alias="bar alias", display="Bar as displayed"
        ),
    ]
    app.ask_user_for_the_requirement_list(module_objects)
    mock_questionary.assert_called_with(
        "Do you mind selected a few for me?",
        choices=["Foo as displayed - Foo description", "Bar as displayed"],
    )
