from app.crud.merge_sort import MergeSort


def test_with_one_input():
    lst = [34, 67, 8, 2, 9]
    ms = MergeSort(lst)
    final_lst = ms.merge_sort()

    print(final_lst)
    