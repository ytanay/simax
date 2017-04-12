from typing import Tuple

import pytest

from simax.person.preson_vectors import PersonalityVector

VECTORS = [
    (PersonalityVector(a=0, b=0), PersonalityVector(a=0, b=0), 0),
    (PersonalityVector(a=1, b=1), PersonalityVector(a=0, b=0), 0),
    (PersonalityVector(a=1, b=1), PersonalityVector(a=1, b=1), 2),
    (PersonalityVector(a=0.5, b=0.2), PersonalityVector(a=-0.1, b=0.8), 0.11000000000000003)
]


@pytest.mark.parametrize('vectors', VECTORS)
def test_personality_vector_multiplication(vectors: Tuple[PersonalityVector, PersonalityVector, float]) -> None:
    assert vectors[0].dot(vectors[1]) == vectors[2]
