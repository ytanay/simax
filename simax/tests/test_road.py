import pytest
from transport.road import Road

@pytest.mark.parametrize(
    'road',
    [
        (Road(80, 100, 90, 250), 15, -1100),
        (Road(90, 250, 250, 150), -0.625, 306.25)
    ]
)
def test_road_line_representation(road):
    assert road[0].slope == road[1] and road[0].intercept == road[2]