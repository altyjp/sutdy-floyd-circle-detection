def detect_cycle(ary:list) -> bool:
    """
    フロイドの循環検出法 に従って、ループを雑に検出します。
    aryにループがある場合はTrueを返却します。

    Args:
        ary list:
            ループを検出したいリスト

    Returns:
        bool:
            aryにループがある場合はTrue。それ以外はFalse

    """
    hare_iter = iter(ary)

    for tortoise in ary:
        try:
            hare = next(hare_iter)
            hare = next(hare_iter)
        except StopIteration as e:
            return False
        
        if tortoise == hare:
            return True

    return False

a = [1, 2, 1, 2]
print(detect_cycle(a)) # return True

b = [1, 2, 3, 1, 2, 3]
print(detect_cycle(b)) # return True

c = [1, 2]
print(detect_cycle(c)) # return False

d = [1, 2, 3, 1, 2]
print(detect_cycle(d)) # return False

e = [0, 1, 2, 3, 1, 2, 3]
print(detect_cycle(e)) # return True