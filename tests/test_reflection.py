from dataclasses import dataclass

from pytest import raises

from info.gianlucacosta.eos.core.reflection import get_single_parameter


@dataclass
class Bear:
    age: int


class TestGetSingleParameter:
    def test_with_single_arg_function_with_annotations(self):
        def my_function(yogi: Bear) -> int:
            return yogi.age

        parameter = get_single_parameter(my_function)
        assert parameter.name == "yogi"
        assert parameter.annotation == Bear

    def test_with_no_arg_function(self):
        def my_function():
            pass

        with raises(ValueError) as ex:
            get_single_parameter(my_function)

        assert ex.value.args == (0,)

    def test_with_multi_arg_function(self):
        def my_function(alpha: int, beta: int) -> int:
            return alpha + beta

        with raises(ValueError) as ex:
            get_single_parameter(my_function)

        assert ex.value.args == (2,)
