import pytest
import tasks


@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not support until version 0.2.0')
def test_unique_id():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2
