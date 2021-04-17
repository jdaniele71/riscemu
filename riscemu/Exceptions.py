class ParseException(BaseException):
    def __init__(self, msg, data=None):
        super().__init__()
        self.msg = msg
        self.data = data

    def message(self):
        return "{}(\"{}\", data={})".format(self.__class__.__name__, self.msg, self.data)


def ASSERT_EQ(a1, a2):
    if a1 != a2:
        raise ParseException("ASSERTION_FAILED: Expected elements to be equal!", (a1, a2))


def ASSERT_LEN(a1, size):
    if len(a1) != size:
        raise ParseException("ASSERTION_FAILED: Expected {} to be of length {}".format(a1, size), (a1, size))


def ASSERT_NOT_NULL(a1):
    if a1 is None:
        raise ParseException("ASSERTION_FAILED: Expected {} to be non null".format(a1), (a1,))


def ASSERT_NOT_IN(a1, a2):
    if a1 in a2:
        raise ParseException("ASSERTION_FAILED: Expected {} to not be in {}".format(a1, a2), (a1,a2))


def ASSERT_IN(a1, a2):
    if a1 not in a2:
        raise ParseException("ASSERTION_FAILED: Expected {} to not be in {}".format(a1, a2), (a1,a2))