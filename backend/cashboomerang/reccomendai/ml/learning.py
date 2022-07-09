import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from scipy import sparse as sp
import implicit
import pickle


def train_model_and_save(modelname):
    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='mysecretpassword',
        host="127.0.0.1",
        port="5432"
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con.cursor() as cur:
        query_string_products = 'SELECT * FROM RECCOMENDAI_PRODUCTS'
        query_string_purch_stat = 'SELECT COUNT(cheque_id) from reccomendai_cheque rcc' \
                                  ' join reccomendai_chequeproduct rccp on (rcc.check_id = rccp.cheque_id) group by user_id'
        users_products = cur.execute(query_string_purch_stat)
        user_products_stat = cur.fetchall()
        cur.execute('SELECT count( DISTINCT(user_id) ) FROM reccomendai_cheque')
        n_users = cur.fetchone()
        cur.execute('select count(id) from reccomendai_product')
        n_products = cur.fetchone()
        cur.execute('SELECT rc.user_id, rcp.id, count(rcp.id) from reccomendai_cheque as rc ' \
                    'join reccomendai_chequeproduct as rcc on rc.id = rcc.cheque_id ' \
                    'join reccomendai_shopproduct as rccc on rcc.shop_product_id = rccc.id ' \
                    'join reccomendai_product as rcp on rccc.product_id = rcp.id group by user_id, rcp.id;')
        stat_data = cur.fetchall()
        row_ids = [val[0] for val in stat_data]
        col_ids = [val[1] for val in stat_data]
        data_ids = [val[2] for val in stat_data]
        print(n_users)
        #print(max(row_ids))
        #print(max(col_ids))
        sp_matrix = sp.csr_matrix((data_ids, (row_ids, col_ids)), shape=(n_users[0], n_products[0]+2))

        model = implicit.als.AlternatingLeastSquares(factors=11, regularization=0.0, iterations=9)
        model.fit(sp_matrix)

        pickle.dump(model, open(modelname, 'wb'))


# train_model_and_save('CashboomerangModel.sav')


def get_reccomendation(user_purchases, sum_products, first_n_recommendations=10):
    with open('CashboomerangModel.sav', 'rb') as pickle_in:
        pickled_model = pickle.load(pickle_in)
    user_id = user_purchases[0]
    u_ps_col = list(user_purchases[1].keys())
    u_ps_row = [0]*len(u_ps_col)
    u_ps_data = list(user_purchases[1].values())
    user_pchs_matr = sp.csr_matrix((u_ps_data, (u_ps_row, u_ps_col)), shape=(1, sum_products))
    returned_data = pickled_model.recommend(user_id, user_pchs_matr, first_n_recommendations)
    with open('CashboomerangModel.sav', 'wb') as pickle_out:
        pickle.dump(pickled_model, pickle_out)
    return returned_data
