from simax.typing import Tuple

import pytest

from simax.person.preson_vectors import PersonalityVector

VECTORS = [
    (PersonalityVector(0, 0), PersonalityVector(0, 0), 0),
    (PersonalityVector(1, 1), PersonalityVector(0, 0), 0),
    (PersonalityVector(1, 1), PersonalityVector(1, 1), 2),
    (PersonalityVector(0.5, 0.2), PersonalityVector(-0.1, 0.8), 0.11000000000000003 )
]


@pytest.mark.parametrize('vectors', VECTORS)
def test_personality_vector_multiplication(vectors: Tuple[PersonalityVector, PersonalityVector, float]) -> None:
    assert vectors[0].dot(vectors[1]) == vectors[2]
