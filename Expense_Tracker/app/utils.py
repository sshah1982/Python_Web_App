
from app.schemas.users import UserOut
from app.schemas.expenses import ExpenseOut


def extract_search_clause_for_users(params):
    p_arr = params.split('&')

    if len(p_arr) == 3:
        where_clause = p_arr[len(p_arr) - 1]
        w_arr = where_clause.split('=')
        if w_arr[0] == 'first_name' or w_arr[0] == 'last_name' or w_arr[0] == 'email': #Implement for created_date as well
            w_list = [w_arr[0], '=', "'", w_arr[1], "'"]
            return "".join(w_list)
        elif w_arr[0] == 'user_id':
            w_list = [w_arr[0], '=', w_arr[1]]
            return "".join(w_list)
        else:
            raise Exception("Allowed Search Fields: user_id, first_name, last_name, email")
    elif len(p_arr) == 2:
        return ""


def extract_search_clause_for_expenses(params):
    p_arr = params.split('&')

    if len(p_arr) == 3:
        where_clause = p_arr[len(p_arr) - 1]
        w_arr = where_clause.split('=')
        if w_arr[0] == 'exp_type' or w_arr[0] == 'exp_desc': #Implement for created_date as well
            w_list = [w_arr[0], '=', "'", w_arr[1], "'"]
            return "".join(w_list)
        elif w_arr[0] == 'user_id' or w_arr[0] == 'amount':
            w_list = [w_arr[0], '=', w_arr[1]]
            return "".join(w_list)
        else:
            raise Exception("Allowed Search Fields: user_id, exp_type, exp_desc, amount")
    elif len(p_arr) == 2:
        return ""


def convert_to_pydantic(recs):
    user_out_lst = []

    if recs is not None:
        for rec in recs:
            exp_out_lst = []
            if rec.expenses is not None:
                for rec_exp in rec.expenses:
                    exp_out = ExpenseOut(exp_type=rec_exp.exp_type, exp_desc=rec_exp.exp_desc,
                                         amount=rec_exp.amount, created_date=str(rec_exp.created_date))
                    exp_out_lst.append(exp_out)

            user_out = UserOut(first_name=rec.first_name, last_name=rec.last_name, email=rec.email,
                                   created_date=str(rec.created_date), birth_date=str(rec.birth_date),
                                   expenses=exp_out_lst)
            user_out_lst.append(user_out)

    return user_out_lst
