import pytest

from webviz_config.utils._dash_component_utils import calculate_slider_step


@pytest.mark.parametrize(
    "min_value,max_value,steps,res",
    [
        (5, 10, 100, 0.01),
        (-10, -5, 100, 0.01),
        (-10, 10, 100, 0.1)
    ]
)
def test_calculate_slider_step(min_value, max_value, steps, res):
    assert(
        calculate_slider_step(
            min_value=min_value, max_value=max_value, steps=steps
        )
        == res
    )
