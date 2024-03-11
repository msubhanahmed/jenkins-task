import pytest
from main import MLOpsClass

@pytest.fixture
def mlops_class():
    return MLOpsClass()

def test_enroll_students(mlops_class):
    mlops_class.enrollStudents(5)
    assert mlops_class.getTotalStrength() == 5

def test_drop_students(mlops_class):
    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(3)
    assert mlops_class.getTotalStrength() == 7

def test_get_total_strength(mlops_class):
    mlops_class.enrollStudents(8)
    assert mlops_class.getTotalStrength() == 8

def test_get_class_name(mlops_class):
    assert mlops_class.getClassName() == "MLOps"

def test_enroll_negative_students(mlops_class):
    with pytest.raises(ValueError):
        mlops_class.enrollStudents(-5)

def test_drop_more_than_enrolled_students(mlops_class):
    with pytest.raises(ValueError):
        mlops_class.dropStudents(10)

def test_drop_negative_students(mlops_class):
    with pytest.raises(ValueError):
        mlops_class.dropStudents(-3)

if __name__ == "__main__":
    pytest.main()
