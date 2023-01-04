def get_elements_from_stack(stack):
    return stack.pop(), stack.pop()


def handle_division(x, y, stack):
    if y == 0:
        return {'message':
                    "division par 0",
                'stack': stack}

    stack.append(x / y)
    return {'message':
                "operation reussi",
            'stack': stack}


class RpnService():
    async def rpn_operation(self, stack, operand):
        if len(stack) < 2:
            return {'message':
                        "Il faut au moins deux elements pour une operation",
                    'stack': stack}
        x, y = get_elements_from_stack(stack)

        if operand == 'add':
            stack.append(x + y)
        if operand == 'mul':
            stack.append(x * y)
        if operand == 'sub':
            stack.append(x - y)
        if operand == 'div':
            return handle_division(x, y, stack)
        else:
            message = "operande non géré"
        return {'message':
                    'operation reussi',
                'stack': stack}
