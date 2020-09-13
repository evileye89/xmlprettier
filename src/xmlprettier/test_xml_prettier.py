import xml_prettier


def equals(expected, actual):
    if actual == expected:
        return
    print(actual, " didn't equal ", expected)
    raise Exception()


xml_prettier.format(
    "src/test/resource/preformat-test.xml", "src/test/resource/actual-test.xml"
)
equals(
    xml_prettier.read("src/test/resource/expected-test.xml"),
    xml_prettier.read("src/test/resource/actual-test.xml"),
)
