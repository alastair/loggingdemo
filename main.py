import logging
import mypackage.somethingelse
from mypackage.somethingelse import module

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)-20s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)

_logger = logging.getLogger("mypackage")
_logger.setLevel(logging.INFO)
_logger.addHandler(handler)

mypackage.do_something()
mypackage.somethingelse.do_something_else()
mypackage.somethingelse.module.do_module()
