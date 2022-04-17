from typing import Optional

from info.gianlucacosta.eos.core.functional import Consumer
from info.gianlucacosta.eos.core.functional.callback import CallbackExceptionCapturer


def send_to_function(target: Consumer[Optional[Exception]], to_send: Optional[Exception]):
    target(to_send)


class TestCallbackExceptionCapturer:
    def test_with_none(self):
        capturer = CallbackExceptionCapturer()

        send_to_function(capturer, None)

        assert capturer.exception is None

    def test_with_exception(self):
        capturer = CallbackExceptionCapturer()
        test_exception = OSError("Example!")

        send_to_function(capturer, test_exception)

        assert capturer.exception is test_exception
