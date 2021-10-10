def superposition(funmod, funseq):
    answer = []
    for fun in funseq:
        answer.append(lambda x, f=fun: funmod(f(x)))
    return answer
