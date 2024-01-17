from formatter import test


def sum_of_intervals(intervals):
    s, ret = [list(x) for x in sorted(intervals)], 0

    if len(s) == 1:
        return abs(s[0][0] - s[0][1])

    for i in range(len(s)):
        if i + 1 > len(s) - 1:
            break

        if s[i][0] <= s[i + 1][0] <= s[i][1]:
            if i + 1 > len(s) - 1:
                break

            while s[i][0] <= s[i + 1][0] <= s[i][1]:
                if s[i][1] <= s[i + 1][1]:
                    s[i][1] = s[i + 1][1]

                del s[i + 1]

                if i + 1 > len(s) - 1:
                    break

    for i in s:
        ret += abs(i[0] - i[1])


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(sum_of_intervals([(1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
        test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

    @test.it("Large numbers")
    def it_2():
        test.assert_equals(
            sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000
        )
        test.assert_equals(
            sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030
        )
