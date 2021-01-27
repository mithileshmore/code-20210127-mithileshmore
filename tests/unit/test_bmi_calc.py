import logging
import pytest
import bmi_calc
from tests.testutils.fixtures import bmi_calc_fixture


@pytest.fixture
def input_sample_data():
    return bmi_calc_fixture.sample_data


@pytest.fixture
def input_sample_data_with_bmi():
    return bmi_calc_fixture.sample_data_with_bmi


@pytest.fixture
def summarized_data_return_data():
    return bmi_calc_fixture.summarized_data_return_data


def test_calculate_bmi(input_sample_data, input_sample_data_with_bmi):
    """Test calculate_bmi."""
    log= logging.getLogger( "Running test_calculate_bmi.." )
    bmi_calc.calculate_bmi(input_sample_data)
    assert input_sample_data == input_sample_data_with_bmi


def test_summarize_data(input_sample_data_with_bmi, summarized_data_return_data):
    """Test summarized_data."""
    log= logging.getLogger( "Running summarized_data test.." )
    return_value = bmi_calc.summarize_data(input_sample_data_with_bmi)
    assert return_value == summarized_data_return_data
