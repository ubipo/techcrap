from data import data

def safe_eval(expr):
    return eval(expr, {"__builtins__":None})

def eval_doors(doors):
    return dict(map(lambda kv: (kv[0], safe_eval(kv[1])), doors.items()))




if __name__ == "__main__":
    print(data[0])

# print(eval_doors(doors))
