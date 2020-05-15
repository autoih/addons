from tensorflow_addons.utils.test_utils import (  # noqa: F401
    maybe_run_functions_eagerly,
    pytest_make_parametrize_id,
    data_format,
    set_seeds,
    pytest_addoption,
    set_global_variables,
    pytest_configure,
    device,
    pytest_generate_tests,
)

import numpy as np
import pytest

import tensorflow as tf
import tensorflow_addons as tfa


# fixtures present in this file will be available
# when running tests and can be referenced with strings
# https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions


@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["np"] = np
    doctest_namespace["tf"] = tf
    doctest_namespace["tfa"] = tfa
